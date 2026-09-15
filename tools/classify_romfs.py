#!/usr/bin/env python3
"""Create a content-free structural classification of a locally extracted RomFS.

The generated JSON records paths, sizes, hashes, suffixes, top-level groups,
and the first four bytes as a format-discovery hint. It never embeds payloads.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def magic4(path: Path) -> tuple[str, str | None]:
    with path.open("rb") as f:
        raw = f.read(4)
    text = raw.decode("ascii", errors="ignore")
    printable = text if len(raw) == 4 and len(text) == 4 and all(32 <= b < 127 for b in raw) else None
    return raw.hex(), printable


def add(counter: dict, key: str, size: int) -> None:
    item = counter.setdefault(key, {"files": 0, "bytes": 0})
    item["files"] += 1
    item["bytes"] += size


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("romfs", type=Path, help="locally extracted RomFS directory")
    parser.add_argument("-o", "--output", type=Path, default=Path("romfs_classification.json"))
    args = parser.parse_args()

    root = args.romfs.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    files = []
    by_suffix: dict[str, dict] = {}
    by_top: dict[str, dict] = {}
    by_magic: dict[str, dict] = {}

    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = path.relative_to(root)
        size = path.stat().st_size
        suffix = path.suffix.lower() or "<none>"
        top = rel.parts[0] if len(rel.parts) > 1 else "<root>"
        mhex, mascii = magic4(path)
        magic_key = mascii if mascii is not None else (mhex or "<empty>")
        add(by_suffix, suffix, size)
        add(by_top, top, size)
        add(by_magic, magic_key, size)
        files.append({
            "path": rel.as_posix(),
            "size": size,
            "sha256": sha256_file(path),
            "suffix": suffix,
            "top_level": top,
            "magic4_hex": mhex,
            "magic4_ascii": mascii,
        })

    payload = {
        "schema": "sakurai.decompilation.romfs-classification.v1",
        "root_name": root.name,
        "file_count": len(files),
        "total_bytes": sum(x["size"] for x in files),
        "summary": {
            "by_suffix": dict(sorted(by_suffix.items())),
            "by_top_level": dict(sorted(by_top.items())),
            "by_magic4": dict(sorted(by_magic.items())),
        },
        "files": files,
        "notes": [
            "Magic values are discovery hints, not asserted format identifications.",
            "Name formats only after validating structure against real files.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"classified {len(files)} RomFS files -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
