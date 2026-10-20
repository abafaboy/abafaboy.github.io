"""Package only after exact full-reader independent acceptance. Never includes fonts."""
from pathlib import Path
import json,hashlib,zipfile
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads((B/'qa/final_acceptance.json').read_text());pdf=B/'lettered/My_Summons_Go_First_Chapter_6.pdf';assert a['verdict']=='pass' and a['pdf_sha256']==sha(pdf)
c=json.loads((B/'source/layout_config.json').read_text());assert set(map(int,c['panels']))==set(range(1,42));files={}
def put(p):
 assert p.suffix.lower() not in ('.otf','.ttf','.woff','.woff2','.pyc')
 files[str(p.relative_to(B))]=p
for n,p in c['panels'].items():
 src=B/p['source'];assert sha(src)==p['source_sha256'];put(src)
 for kind in ['full','phone']:put(B/f'lettered/{kind}/panel_{int(n):02}.png')
for p in (B/'source').iterdir():
 if p.is_file() and p.suffix in ('.py','.md','.json') and p.name not in ['pending_layouts.json']:put(p)
for p in (B/'qa').iterdir():
 if p.is_file() and p.suffix in ('.md','.json','.png'):put(p)
for root in ['raw','repairs']:
 for p in (B/root).rglob('*'):
  if p.is_file() and p.suffix.lower() in ('.json','.txt','.md') and '__pycache__' not in str(p):put(p)
put(B/'lettered/placement_manifest.json')
for p in (B/'lettered/reader').glob('*.png'):put(p)
for p in (B/'qa/pdf390').glob('*'):put(p)
refs=json.loads((B/'source/reference_lock.json').read_text())
for ref in refs['selected']:
 p=Path(ref['path']);assert sha(p)==ref['sha256'];name='references/'+p.name;files[name]=p;ref['path']=name
out=B/'deliverables';out.mkdir(exist_ok=True);dest=out/'My_Summons_Go_First_Chapter_6_Source_and_Reader_Assets.zip'
index=[]
with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for name,p in sorted(files.items()):
  data=p.read_bytes()
  z.writestr('Chapter_6/'+name,data);index.append(dict(path=name,bytes=len(data),sha256=hashlib.sha256(data).hexdigest()))
 readme='''Chapter 6: The Person Outside\n\n41 accepted story units; 21 reader pages. Exact script, native art, crop and lettering geometry, final full/phone PNGs, actual compressed PDF proofs and independent acceptance are included. The reader PDF is delivered separately.\n\nSet ANIME_ACE_FONT to your licensed Anime Ace 2.0 BB font before running source/build_chapter.py. No font binaries are included or embedded in the reader. Artwork is imagegen-derived. P20 contains a declared composited imagegen radio repair; its provenance is explicit in the layout and placement manifest.\n\nOnly selected native art is duplicated here. Earlier rejected variants and upstream packages are retained in Library via source IDs and hash manifests under qa, raw and repairs. Original candidates are not approved alternatives.\n\nFull panel images are twice the geometry manifest master size. Phone images are 390px wide. Use placement_manifest.json output_size, glyph_bounds, balloon_outline, page offsets and source transforms for alignment.\n'''
 z.writestr('Chapter_6/references/portable_reference_lock.json',json.dumps(refs,indent=2));z.writestr('Chapter_6/README_DELIVERY.txt',readme);z.writestr('Chapter_6/CONTENTS.json',json.dumps(index,indent=2))
with zipfile.ZipFile(dest) as z:
 assert z.testzip() is None
 assert not any(Path(n).suffix.lower() in ('.ttf','.otf','.woff','.woff2','.pyc') for n in z.namelist())
assert dest.stat().st_size<512*1024*1024
rec=dict(file=dest.name,bytes=dest.stat().st_size,sha256=sha(dest),entries=len(index)+3,fonts_included=False)
(out/'package_verification.json').write_text(json.dumps(rec,indent=2));print(json.dumps(rec,indent=2))
