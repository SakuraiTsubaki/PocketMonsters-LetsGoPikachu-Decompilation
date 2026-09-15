#!/usr/bin/env python3
"""Scan a local binary for aligned little-endian values inside a target address range."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("binary",type=Path); ap.add_argument("--width",type=int,choices=(4,8),required=True)
    ap.add_argument("--min-address",type=lambda x:int(x,0),required=True); ap.add_argument("--max-address",type=lambda x:int(x,0),required=True)
    ap.add_argument("--alignment",type=int,default=None); ap.add_argument("-o","--output",type=Path,default=Path("pointer_candidates.json"))
    a=ap.parse_args(); raw=a.binary.read_bytes(); align=a.alignment or a.width
    if align<=0: ap.error("alignment must be > 0")
    candidates=[]
    for off in range(0,len(raw)-a.width+1,align):
        v=int.from_bytes(raw[off:off+a.width],"little")
        if a.min_address <= v < a.max_address:
            candidates.append({"file_offset":off,"file_offset_hex":f"0x{off:X}","value":v,"value_hex":f"0x{v:X}"})
    payload={"schema":"sakurai.decompilation.pointer-candidates.v1","source_name":a.binary.name,"source_size":len(raw),"source_sha256":hashlib.sha256(raw).hexdigest(),"width":a.width,"alignment":align,"range":{"min":a.min_address,"max_exclusive":a.max_address},"candidate_count":len(candidates),"candidates":candidates,"notes":["Candidates are unverified integer values, not confirmed pointers.","Validate references against mapped sections before assigning symbols."]}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
    print(f"found {len(candidates)} candidates -> {a.output}"); return 0
if __name__=="__main__": raise SystemExit(main())
