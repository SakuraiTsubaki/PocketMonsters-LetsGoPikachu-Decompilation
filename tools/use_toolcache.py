#!/usr/bin/env python3
from __future__ import annotations
import hashlib, os, re, shutil, subprocess, tarfile, tempfile, urllib.request
from pathlib import Path
TAG=os.environ.get("GEN7_TOOLCACHE_TAG","toolcache-2026-09-16"); ROOT=Path(__file__).resolve().parent.parent; TOOLS=ROOT/".tools"; CACHE=ROOT/".cache"/"toolcache"
def repo_name():
    o=os.environ.get("GEN7_TOOLCACHE_REPO")
    if o:return o
    p=subprocess.run(["git","-C",str(ROOT),"config","--get","remote.origin.url"],text=True,capture_output=True); r=p.stdout.strip(); m=re.search(r"github\.com[/:]([^/]+)/([^/]+?)(?:\.git)?$",r)
    if not m: raise SystemExit("cannot determine GitHub repository; set GEN7_TOOLCACHE_REPO=owner/repo")
    return f"{m.group(1)}/{m.group(2)}"
def download(url,dst):
    req=urllib.request.Request(url,headers={"User-Agent":"gen7-toolcache/1"})
    with urllib.request.urlopen(req) as src,dst.open("wb") as out:
        while True:
            c=src.read(1024*1024)
            if not c: break
            out.write(c)
def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for c in iter(lambda:f.read(1024*1024),b""): h.update(c)
    return h.hexdigest()
def safe_extract(archive,destination):
    root=destination.resolve()
    with tarfile.open(archive,"r:gz") as tf:
        for member in tf.getmembers():
            target=(destination/member.name).resolve()
            if target!=root and root not in target.parents: raise SystemExit(f"unsafe archive member: {member.name}")
        tf.extractall(destination)
def main():
    platform="switch" if (ROOT/"tools"/"inspect_nso.py").exists() else "3ds"; asset=f"gen7-{platform}-toolcache-linux-x86_64.tar.gz"; identity=f"{TAG}:{asset}"; marker=TOOLS/".toolcache-version"
    if marker.exists() and marker.read_text(encoding="utf-8").strip()==identity: print(f"toolcache already ready: {identity}"); return 0
    repo=repo_name(); base=f"https://github.com/{repo}/releases/download/{TAG}"; CACHE.mkdir(parents=True,exist_ok=True); archive=CACHE/asset; checksum=CACHE/f"{asset}.sha256"
    print(f"fetching prebuilt toolcache from {repo} release {TAG}"); download(f"{base}/{asset}.sha256",checksum); expected=checksum.read_text(encoding="utf-8").split()[0].lower(); download(f"{base}/{asset}",archive); actual=sha256(archive)
    if actual!=expected: raise SystemExit(f"SHA-256 mismatch: expected {expected}, got {actual}")
    staging=Path(tempfile.mkdtemp(prefix=".tools-staging-",dir=ROOT))
    try:
        safe_extract(archive,staging); (staging/".toolcache-version").write_text(identity+"\n",encoding="utf-8")
        if TOOLS.exists(): shutil.rmtree(TOOLS)
        staging.replace(TOOLS)
    finally:
        if staging.exists(): shutil.rmtree(staging,ignore_errors=True)
    print("toolcache ready. Run: source .tools/env.sh"); return 0
if __name__=="__main__": raise SystemExit(main())
