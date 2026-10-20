from pathlib import Path
import sys,zipfile,json,hashlib
B=Path(__file__).resolve().parents[1];id,name,kind,recordname=sys.argv[1:];p=B.parent/'incoming'/name;dest=B/kind/p.stem
with zipfile.ZipFile(p) as z:
 assert z.testzip() is None;assert all(not Path(n).is_absolute() and '..' not in Path(n).parts for n in z.namelist());z.extractall(dest)
r={'library_file_id':id,'archive':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size,'extracted_root':str(dest),'status':'unreviewed','files':[{'path':str(f.relative_to(dest)),'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'bytes':f.stat().st_size} for f in sorted(dest.rglob('*')) if f.is_file()]};(B/'qa'/recordname).write_text(json.dumps(r,indent=2));print(dest);print('\n'.join(x['path'] for x in r['files'] if 'manifest' in x['path'] or 'v11' in x['path']))
