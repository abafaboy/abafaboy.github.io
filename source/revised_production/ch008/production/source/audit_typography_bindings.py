"""Verify existing independent typography verdicts against current proof bytes."""
from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def walk(x):
 if isinstance(x,list):
  for y in x:yield from walk(y)
 elif isinstance(x,dict):
  if 'panel' in x:yield x
  for y in x.values():
   if isinstance(y,(dict,list)):yield from walk(y)
records=[]
for f in sorted((B/'qa').glob('*typography*.json')):
 for r in walk(json.loads(f.read_text())):
  if r.get('typography_verdict',r.get('verdict'))!='pass':continue
  ph=r.get('phone_sha256',r.get('phone',{}).get('sha256'));fh=r.get('full_sha256',r.get('full',{}).get('sha256'))
  if ph and fh:records.append((int(r['panel']),ph,fh,str(f.relative_to(B))))
m=json.loads((B/'lettered/provisional_placement_manifest.json').read_text());out=[]
for p in m['panels']:
 n=p['panel'];ph=sha(B/f'lettered/phone/panel_{n:02}.png');fh=sha(B/f'lettered/full/panel_{n:02}.png')
 matches=[r[3] for r in records if r[:3]==(n,ph,fh)]
 out.append({'panel':n,'phone_sha256':ph,'full_sha256':fh,'matching_independent_typography_reports':matches,'current_proof_independently_passed':bool(matches)})
(B/'qa/current_typography_bindings.json').write_text(json.dumps(out,indent=2)+'\n')
print(f'{sum(x["current_proof_independently_passed"] for x in out)}/{len(out)} current units have exact independent typography PASS bindings')
print('Missing:',[x['panel'] for x in out if not x['current_proof_independently_passed']])
