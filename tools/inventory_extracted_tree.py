#!/usr/bin/env python3
"""Create a reproducible inventory of a locally extracted game tree.

This tool does not dump, decrypt, download, or redistribute game content. It only
reads a directory that the researcher already has locally and writes metadata
(relative path, size, SHA-256, and a lightweight classification) to JSON.
"""
from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
CHUNK_SIZE = 1024 * 1024

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        while chunk := handle.read(CHUNK_SIZE):
            digest.update(chunk)
    return digest.hexdigest()

def classify(rel: Path) -> str:
    parts = {part.lower() for part in rel.parts}
    name = rel.name.lower()
    if "exefs" in parts or name in {".code", "code.bin", ".code.bin", "main", "rtld", "sdk"} or name.startswith("subsdk"):
        return "executable"
    if "romfs" in parts:
        return "romfs"
    if name in {"exheader.bin", "header.bin", "ncchheader.bin"}:
        return "container-metadata"
    return "other"

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("inventory.json"))
    parser.add_argument("--project", default=None)
    parser.add_argument("--platform", default=None)
    args = parser.parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir(): parser.error(f"not a directory: {root}")
    records=[]
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel=path.relative_to(root); stat=path.stat()
        records.append({"path":rel.as_posix(),"size":stat.st_size,"sha256":sha256_file(path),"class":classify(rel)})
    payload={"schema":"sakurai.decompilation.inventory.v1","generated_at":datetime.now(timezone.utc).isoformat(),"project":args.project,"platform":args.platform,"source_root_name":root.name,"file_count":len(records),"total_size":sum(i["size"] for i in records),"files":records}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"wrote {len(records)} records to {args.output}")
    return 0
if __name__=="__main__": raise SystemExit(main())
