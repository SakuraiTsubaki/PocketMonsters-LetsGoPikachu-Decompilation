#!/usr/bin/env python3
"""Scan a locally extracted Switch ExeFS and map every NSO0 module.

The report contains only module metadata, section ranges, and SHA-256 hashes.
No executable content is embedded in the generated JSON.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

HEADER_SIZE = 0x100
CANDIDATES = {"main", "rtld", "sdk"}


def u32(data: bytes, off: int) -> int:
    return struct.unpack_from("<I", data, off)[0]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def classify(name: str) -> str:
    if name == "main":
        return "main"
    if name == "rtld":
        return "runtime-loader"
    if name == "sdk":
        return "sdk"
    if name.startswith("subsdk"):
        return "subsdk"
    return "other-nso"


def parse(path: Path) -> dict:
    raw = path.read_bytes()
    if len(raw) < HEADER_SIZE or raw[:4] != b"NSO0":
        raise ValueError(f"not an NSO0 module: {path}")

    flags = u32(raw, 0xC)
    specs = (
        (".text", 0x10, 0x60, 0, 3),
        (".rodata", 0x20, 0x64, 1, 4),
        (".data", 0x30, 0x68, 2, 5),
    )
    segments = []
    for name, base, size_off, cbit, hbit in specs:
        file_off = u32(raw, base)
        mem_off = u32(raw, base + 4)
        mem_size = u32(raw, base + 8)
        stored = u32(raw, size_off)
        segments.append({
            "name": name,
            "file_offset": file_off,
            "file_offset_hex": f"0x{file_off:X}",
            "stored_size": stored,
            "memory_offset": mem_off,
            "memory_offset_hex": f"0x{mem_off:X}",
            "memory_size": mem_size,
            "memory_end": mem_off + mem_size,
            "compressed": bool(flags & (1 << cbit)),
            "hash_checked": bool(flags & (1 << hbit)),
            "stored_range_within_file": file_off + stored <= len(raw),
        })

    return {
        "name": path.name,
        "kind": classify(path.name),
        "size": len(raw),
        "sha256": sha256_file(path),
        "version": u32(raw, 0x4),
        "flags": flags,
        "flags_hex": f"0x{flags:08X}",
        "module_id": raw[0x40:0x60].hex(),
        "bss_size": u32(raw, 0x3C),
        "segments": segments,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("exefs", type=Path, help="locally extracted ExeFS directory")
    parser.add_argument("-o", "--output", type=Path, default=Path("nso_modules.json"))
    args = parser.parse_args()

    root = args.exefs.expanduser().resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    modules = []
    skipped = []
    for path in sorted(p for p in root.iterdir() if p.is_file()):
        head = path.read_bytes()[:4]
        if head == b"NSO0":
            modules.append(parse(path))
        elif path.name in CANDIDATES or path.name.startswith("subsdk"):
            skipped.append(path.name)

    payload = {
        "schema": "sakurai.decompilation.nso-module-map.v1",
        "exefs_root_name": root.name,
        "module_count": len(modules),
        "modules": modules,
        "expected_name_but_not_nso0": skipped,
        "notes": [
            "Analyze main separately from runtime/SDK/subsdk modules.",
            "Compressed NSO segments must be decompressed before instruction-level matching.",
        ],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"mapped {len(modules)} NSO0 modules -> {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
