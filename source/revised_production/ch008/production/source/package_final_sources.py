"""Package exact, reviewed final assembly plus untouched intake archives; never upload."""
from pathlib import Path
import argparse,json,hashlib,zipfile
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=argparse.ArgumentParser();a.add_argument('--reviewed-pdf-sha256',required=True);args=a.parse_args()
pdf=B/'lettered/My_Summons_Go_First_Chapter_8.pdf';assert sha(pdf)==args.reviewed_pdf_sha256
m=json.loads((B/'lettered/placement_manifest.json').read_text());assert [p['panel'] for p in m['panels']]==list(range(1,37))
inv=json.loads((B/'source/source_archive_inventory.json').read_text())
files={}
def add(p):
 assert p.is_file()
 assert p.suffix.lower() not in ('.otf','.ttf','.woff','.woff2','.pyc')
 files[str(p.relative_to(B))]=p
for root in ('source','qa'):
 for p in (B/root).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:add(p)
for root in ('lettered/full','lettered/phone','lettered/reader'):
 for p in (B/root).glob('*'):
  if p.is_file():add(p)
add(pdf);add(B/'lettered/placement_manifest.json')
for p in m['panels']:
 src=B/p['source'];assert sha(src)==p['sha256'];add(src)
for row in inv['intake_archives']:
 p=B/row['archive_file'];assert sha(p)==row['sha256'];add(p)
out=B/'delivery';out.mkdir(exist_ok=True)
assert not list(out.glob('Chapter_8_Source_Part_*.zip')), 'Preserve existing delivery; choose a new version before rebuilding.'
limit=480*1024*1024;parts=[];group=[];size=0
for name,p in sorted(files.items(),key=lambda x:(x[0].startswith('incoming/'),x[0])):
 n=p.stat().st_size;assert n<limit
 if group and size+n>limit:parts.append(group);group=[];size=0
 group.append((name,p));size+=n
if group:parts.append(group)
inventory=[]
readme='Chapter 8: The Empty Bit\nExtract every independently openable part into one directory. The production folder contains exact accepted art, raster lettering, scripts, QA and the final reader. Untouched intake ZIPs retain all native attempts, prompts and provenance; source/source_archive_inventory.json identifies their Library IDs and versions. No font programs are distributed. To rebuild, install a licensed Anime Ace locally and set ANIME_ACE_FONT to its path before running source/build_chapter.py. All source artworks and authorized derivative hashes are bound in the placement manifest and independent review ledger. This package authorizes no publication.\n'
for i,group in enumerate(parts,1):
 z=out/f'Chapter_8_Source_Part_{i:02}_of_{len(parts):02}.zip'
 with zipfile.ZipFile(z,'w',compression=zipfile.ZIP_STORED,allowZip64=True) as f:
  f.writestr('README.txt',readme)
  f.writestr('PART_CONTENTS.json',json.dumps([{'path':n,'bytes':p.stat().st_size,'sha256':sha(p)} for n,p in group],indent=2))
  for n,p in group:f.write(p,'production/'+n)
 assert z.stat().st_size<512*1024*1024
 with zipfile.ZipFile(z) as f:assert f.testzip() is None
 inventory.append({'file':z.name,'bytes':z.stat().st_size,'sha256':sha(z)})
(out/'SOURCE_DELIVERY_MANIFEST.json').write_text(json.dumps({'chapter':8,'reviewed_reader_sha256':sha(pdf),'parts':inventory,'font_programs':0},indent=2)+'\n')
print(json.dumps(inventory,indent=2))
