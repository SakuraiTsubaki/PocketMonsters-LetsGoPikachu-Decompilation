#!/usr/bin/env python3
"""Inspect a locally extracted Nintendo Switch NSO0 executable.

Parses the NSO0 header and emits a compact JSON memory/file map suitable for
early decompilation work. It does not decrypt, dump, or redistribute content.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import struct
from pathlib import Path

HEADER_SIZE = 0x100


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def u32(data: bytes, offset: int) -> int:
    return struct.unpack_from("<I", data, offset)[0]


def segment(data: bytes, name: str, base: int, file_size_off: int, compressed: bool, hashed: bool) -> dict:
    file_offset = u32(data, base)
    memory_offset = u32(data, base + 4)
    memory_size = u32(data, base + 8)
    stored_size = u32(data, file_size_off)
    return {
        "name": name,
        "file_offset": file_offset,
        "file_offset_hex": f"0x{file_offset:X}",
        "stored_size": stored_size,
        "stored_size_hex": f"0x{stored_size:X}",
        "memory_offset": memory_offset,
        "memory_offset_hex": f"0x{memory_offset:X}",
        "memory_size": memory_size,
        "memory_size_hex": f"0x{memory_size:X}",
        "memory_end": memory_offset + memory_size,
        "memory_end_hex": f"0x{memory_offset + memory_size:X}",
        "compressed": compressed,
        "hash_checked": hashed,
    }


def parse_nso(path: Path) -> dict:
    raw = path.read_bytes()
    if len(raw) < HEADER_SIZE:
        raise ValueError(f"NSO is too small: {len(raw)} bytes")
    if raw[0:4] != b"NSO0":
        raise ValueError(f"bad NSO0 signature: {raw[0:4]!r}")

    flags = u32(raw, 0xC)
    segs = [
        segment(raw, ".text", 0x10, 0x60, bool(flags & (1 << 0)), bool(flags & (1 << 3))),
        segment(raw, ".rodata", 0x20, 0x64, bool(flags & (1 << 1)), bool(flags & (1 << 4))),
        segment(raw, ".data", 0x30, 0x68, bool(flags & (1 << 2)), bool(flags & (1 << 5))),
    ]

    for seg in segs:
        end = seg["file_offset"] + seg["stored_size"]
        seg["file_end"] = end
        seg["file_end_hex"] = f"0x{end:X}"
        seg["within_file"] = end <= len(raw)

    module_name_offset = u32(raw, 0x1C)
    module_name_size = u32(raw, 0x2C)
    module_name = None
    if module_name_size and module_name_offset + module_name_size <= len(raw):
        module_name = raw[module_name_offset:module_name_offset + module_name_size].rstrip(b"\0").decode(
            "utf-8", errors="replace"
        )

    module_id = raw[0x40:0x60].hex()
    return {
        "schema": "sakurai.decompilation.nso0.v1",
        "path": path.name,
        "file_size": len(raw),
        "sha256": sha256_file(path),
        "version": u32(raw, 0x4),
        "flags": flags,
        "flags_hex": f"0x{flags:08X}",
        "execute_only_memory": bool(flags & (1 << 6)),
        "zbic_compression": bool(flags & (1 << 7)),
        "module_name": module_name,
        "module_name_offset": module_name_offset,
        "module_name_size": module_name_size,
        "module_id": module_id,
        "bss_size": u32(raw, 0x3C),
        "segments": segs,
        "embedded": {
            "offset_in_rodata": u32(raw, 0x88),
            "size": u32(raw, 0x8C),
        },
        "dynamic_string_table": {
            "offset_in_rodata": u32(raw, 0x90),
            "size": u32(raw, 0x94),
        },
        "dynamic_symbol_table": {
            "offset_in_rodata": u32(raw, 0x98),
            "size": u32(raw, 0x9C),
        },
        "notes": [
            "Memory offsets are module-relative NSO mappings.",
            "Compressed segments require decompression before instruction-level matching.",
        ],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("nso", type=Path, help="locally extracted NSO0 file (for example ExeFS/main)")
    parser.add_argument("-o", "--output", type=Path, help="write JSON report here")
    args = parser.parse_args()

    result = parse_nso(args.nso.expanduser().resolve())
    text = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
