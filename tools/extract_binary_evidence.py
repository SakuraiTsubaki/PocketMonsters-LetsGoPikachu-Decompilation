#!/usr/bin/env python3
"""Build a non-redistributive evidence index for a local executable/data binary.

By default the report stores only offsets, lengths, encodings, and SHA-256 hashes
for discovered strings; literal string contents are not embedded. Use
--include-text only for local/private research outputs not intended for redistribution.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def is_ascii_byte(b: int) -> bool:
    return 0x20 <= b <= 0x7E or b == 0x09

def scan_ascii(data: bytes, minimum: int):
    out=[]; start=None
    for i,b in enumerate(data+b"\0"):
        if i < len(data) and is_ascii_byte(b):
            if start is None: start=i
        elif start is not None:
            if i-start >= minimum: out.append((start,data[start:i]))
            start=None
    return out

def scan_utf16le_ascii(data: bytes, minimum: int):
    out=[]; i=0
    while i+1 < len(data):
        if is_ascii_byte(data[i]) and data[i+1]==0:
            start=i; chars=[]
            while i+1 < len(data) and is_ascii_byte(data[i]) and data[i+1]==0:
                chars.append(data[i]); i+=2
            if len(chars) >= minimum: out.append((start,bytes(chars)))
        else: i+=1
    return out

def record(offset,raw,encoding,base,include_text):
    item={"offset":offset,"offset_hex":f"0x{offset:X}","length_chars":len(raw),"encoding":encoding,"sha256":sha256_bytes(raw)}
    if base is not None:
        item["address"]=base+offset; item["address_hex"]=f"0x{base+offset:X}"
    if include_text: item["text"]=raw.decode("ascii",errors="replace")
    return item

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("binary",type=Path); ap.add_argument("-o","--output",type=Path,default=Path("binary_evidence.json"))
    ap.add_argument("--base-address",type=lambda x:int(x,0)); ap.add_argument("--min-ascii",type=int,default=4); ap.add_argument("--min-utf16",type=int,default=4)
    ap.add_argument("--include-text",action="store_true")
    a=ap.parse_args(); raw=a.binary.read_bytes(); entries=[]
    for off,s in scan_ascii(raw,a.min_ascii): entries.append(record(off,s,"ascii",a.base_address,a.include_text))
    for off,s in scan_utf16le_ascii(raw,a.min_utf16): entries.append(record(off,s,"utf-16le-ascii-subset",a.base_address,a.include_text))
    entries.sort(key=lambda e:(e["offset"],e["encoding"]))
    payload={"schema":"sakurai.decompilation.binary-evidence.v1","source_name":a.binary.name,"source_size":len(raw),"source_sha256":sha256_bytes(raw),"base_address":a.base_address,"literal_text_included":bool(a.include_text),"string_candidate_count":len(entries),"strings":entries,"notes":["Default output omits literal string content and stores hashes only.","Offsets are file-relative; address is emitted only when --base-address is supplied."]}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(payload,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
    print(f"indexed {len(entries)} string candidates -> {a.output}"); return 0
if __name__=="__main__": raise SystemExit(main())
