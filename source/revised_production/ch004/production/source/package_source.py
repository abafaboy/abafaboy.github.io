from pathlib import Path
import zipfile,hashlib,json
B=Path(__file__).resolve().parents[1];files=[]
for name in ('source','models','raw','qa','lettered'):
 for p in sorted((B/name).rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix.lower() not in ('.otf','.ttf','.woff','.woff2','.pyc','.zip'):
   files.append(p)
groups=[[]];size=0
for p in files:
 if size+p.stat().st_size>350_000_000 and groups[-1]:groups.append([]);size=0
 groups[-1].append(p);size+=p.stat().st_size
index={str(p.relative_to(B)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'archive_part':i} for i,g in enumerate(groups,1) for p in g}
(B/'Source_File_Index.json').write_text(json.dumps(index,indent=2))
receipts=[]
for i,g in enumerate(groups,1):
 out=B/f'My_Summons_Go_First_Chapter_4_Source_Part_{i}_of_{len(groups)}.zip'
 with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in g+[B/'Source_File_Index.json']:z.write(p,'My_Summons_Go_First_Chapter_4/'+str(p.relative_to(B)))
 assert out.stat().st_size<536870912
 with zipfile.ZipFile(out) as z:
  assert z.testzip() is None
  assert not any(Path(n).suffix.lower() in ('.otf','.ttf','.woff','.woff2') for n in z.namelist())
  for p in g:
   rel=str(p.relative_to(B));assert hashlib.sha256(z.read('My_Summons_Go_First_Chapter_4/'+rel)).hexdigest()==index[rel]['sha256']
 rec={'part':i,'file':str(out),'files':len(g)+1,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()};receipts.append(rec);print(json.dumps(rec),flush=True)
(B/'source_archive_receipts.json').write_text(json.dumps(receipts,indent=2))
print('All archive CRCs, indexed hashes and font exclusion verified.',flush=True)
