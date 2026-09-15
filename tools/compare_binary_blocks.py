#!/usr/bin/env python3
"""Compare two local binaries by fixed-size SHA-256 blocks without embedding data."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

def h(b:bytes)->str: return hashlib.sha256(b).hexdigest()
def main()->int:
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("left",type=Path); ap.add_argument("right",type=Path); ap.add_argument("-o","--output",type=Path,default=Path("binary_block_diff.json")); ap.add_argument("--block-size",type=lambda x:int(x,0),default=0x1000); a=ap.parse_args()
    if a.block_size<=0: ap.error("block size must be > 0")
    l=a.left.read_bytes(); r=a.right.read_bytes(); n=max(len(l),len(r)); rows=[]; same=changed=left_only=right_only=0
    for off in range(0,n,a.block_size):
        lb=l[off:off+a.block_size]; rb=r[off:off+a.block_size]
        if not lb: status="right-only"; right_only+=1
        elif not rb: status="left-only"; left_only+=1
        elif lb==rb: status="same"; same+=1
        else: status="changed"; changed+=1
        rows.append({"offset":off,"offset_hex":f"0x{off:X}","left_size":len(lb),"right_size":len(rb),"left_sha256":h(lb) if lb else None,"right_sha256":h(rb) if rb else None,"status":status})
    payload={"schema":"sakurai.decompilation.binary-block-diff.v1","block_size":a.block_size,"left":{"name":a.left.name,"size":len(l),"sha256":h(l)},"right":{"name":a.right.name,"size":len(r),"sha256":h(r)},"summary":{"same":same,"changed":changed,"left_only":left_only,"right_only":right_only},"blocks":rows}
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8"); print(f"compared {len(rows)} blocks -> {a.output}"); return 0
if __name__=="__main__": raise SystemExit(main())
