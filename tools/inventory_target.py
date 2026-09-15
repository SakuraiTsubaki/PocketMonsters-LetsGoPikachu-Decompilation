#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

def sha256(path):
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''): h.update(chunk)
    return h.hexdigest()

def main():
    p=argparse.ArgumentParser(); p.add_argument('target',type=Path); p.add_argument('--target-id',required=True); p.add_argument('--product',required=True); p.add_argument('--output',type=Path,required=True); a=p.parse_args()
    root=a.target.resolve(); paths=[root] if root.is_file() else sorted(x for x in root.rglob('*') if x.is_file())
    files=[]
    for path in paths:
        if path.name.lower() in {'prod.keys','title.keys'} or path.suffix.lower()=='.keys': continue
        rel=path.name if root.is_file() else path.relative_to(root).as_posix(); files.append({'path':rel,'size':path.stat().st_size,'sha256':sha256(path)})
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps({'schema_version':1,'target_id':a.target_id,'product':a.product,'verification':'Observed','files':files},indent=2)+'\n')
if __name__=='__main__': main()
