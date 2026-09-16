#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TOOLS="$ROOT/.tools"; BIN="$TOOLS/bin"; SRC="$TOOLS/src"; DL="$TOOLS/downloads"; EMU="$TOOLS/emulators"; GHIDRA_DIR="$TOOLS/ghidra"
mkdir -p "$BIN" "$SRC" "$DL" "$EMU"
log(){ printf '[gen7-switch] %s\n' "$*"; }; have(){ command -v "$1" >/dev/null 2>&1; }
install_system_deps(){ if ! have apt-get; then return 0; fi; local SUDO=""; if [ "$(id -u)" -ne 0 ]; then if have sudo; then SUDO=sudo; else return 0; fi; fi; $SUDO apt-get update; $SUDO apt-get install -y --no-install-recommends ca-certificates git curl unzip make cmake ninja-build build-essential pkg-config python3 python3-pip clang llvm lldb binutils-aarch64-linux-gnu openjdk-21-jdk libssl-dev liblz4-dev zlib1g-dev; }
clone_or_update(){ local url="$1" dst="$2"; if [ -d "$dst/.git" ]; then git -C "$dst" fetch --depth=1 origin; git -C "$dst" reset --hard origin/HEAD; git -C "$dst" submodule update --init --recursive; else git clone --depth=1 --recursive "$url" "$dst"; fi; }
download_verify(){ local url="$1" dst="$2" sha="$3"; [ -f "$dst" ] || curl -fL --retry 3 --retry-delay 2 "$url" -o "$dst"; printf '%s  %s\n' "$sha" "$dst" | sha256sum -c -; }
install_hactool(){ local d="$SRC/hactool"; clone_or_update https://github.com/SciresM/hactool.git "$d"; cp "$d/config.mk.template" "$d/config.mk"; make -C "$d" -j"$(nproc)"; install -m755 "$d/hactool" "$BIN/hactool"; }
install_ghidra(){ local zip="$DL/ghidra_12.1.3_PUBLIC_20260817.zip"; download_verify https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_12.1.3_build/ghidra_12.1.3_PUBLIC_20260817.zip "$zip" 93a5d11a9ad510622acaaf908c556a7b9b764d338e78a7567f3689bf5081fd54; rm -rf "$GHIDRA_DIR"; mkdir -p "$GHIDRA_DIR"; unzip -q "$zip" -d "$GHIDRA_DIR"; local home; home="$(find "$GHIDRA_DIR" -mindepth 1 -maxdepth 1 -type d | head -n1)"; ln -sfn "$home/ghidraRun" "$BIN/ghidraRun"; ln -sfn "$home/support/analyzeHeadless" "$BIN/analyzeHeadless"; }
install_eden(){ local api="https://git.eden-emu.dev/api/v1/repos/eden-emu/eden/releases"; local meta="$DL/eden-releases.json"; curl -fL --retry 3 "$api" -o "$meta"; local tuple; tuple="$(python3 - "$meta" <<'PY'
import json, platform, sys
rels=json.load(open(sys.argv[1], encoding='utf-8'))
arch=platform.machine().lower(); want=('aarch64','arm64') if arch in ('aarch64','arm64') else ('amd64','x86_64')
for rel in rels:
    if rel.get('draft') or rel.get('prerelease'): continue
    imgs=[a for a in (rel.get('assets') or []) if (a.get('name') or '').lower().endswith('.appimage') and any(x in (a.get('name') or '').lower() for x in want)]
    if not imgs: continue
    imgs.sort(key=lambda a:(0 if 'pgo' in (a.get('name') or '').lower() else 1,a.get('name') or ''))
    a=imgs[0]; url=a.get('browser_download_url') or a.get('download_url')
    if url:
        print(rel.get('tag_name','unknown')+'\t'+(a.get('name') or 'eden.AppImage')+'\t'+url); break
PY
)"; [ -n "$tuple" ] || { log "no stable Eden AppImage found from official release API"; return 1; }; local tag name url; IFS=$'\t' read -r tag name url <<< "$tuple"; local dst="$EMU/eden.AppImage"; curl -fL --retry 3 --retry-delay 2 "$url" -o "$dst"; chmod +x "$dst"; ln -sfn "$dst" "$BIN/eden"; printf '%s\n' "$tag" > "$TOOLS/eden-version.txt"; sha256sum "$dst" > "$TOOLS/eden-appimage.sha256"; }
install_system_deps; for c in git curl make python3 unzip sha256sum java; do have "$c" || { log "missing required command: $c"; exit 1; }; done; install_hactool; install_ghidra; install_eden
cat > "$TOOLS/env.sh" <<'ENV'
#!/usr/bin/env bash
_TOOLS_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; export PATH="$_TOOLS_DIR/bin:$PATH"; unset _TOOLS_DIR
ENV
chmod +x "$TOOLS/env.sh"; printf 'platform=nintendo-switch\nghidra=12.1.3\neden=%s\n' "$(cat "$TOOLS/eden-version.txt")" > "$TOOLS/versions.txt"; log "done. Run: source .tools/env.sh"
