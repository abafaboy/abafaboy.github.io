from pathlib import Path
import zipfile,hashlib,json
B=Path(__file__).resolve().parents[1]
files=[]
for name in ('source','raw','qa','lettered'):
 for p in (B/name).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts and p.suffix.lower() not in ('.otf','.ttf','.woff','.woff2','.pyc'):
   files.append(p)
index={str(p.relative_to(B)):{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files}
(B/'Source_File_Index.json').write_text(json.dumps(index,indent=2))
with zipfile.ZipFile(B/'My_Summons_Go_First_Chapter_2_Source.zip','w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in files+[B/'Source_File_Index.json']:z.write(p,'My_Summons_Go_First_Chapter_2/'+str(p.relative_to(B)))
print(json.dumps({'files':len(files)+1,'bytes':(B/'My_Summons_Go_First_Chapter_2_Source.zip').stat().st_size}))
