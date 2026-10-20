from pathlib import Path
import subprocess,sys,json,hashlib
B=Path(__file__).resolve().parents[1]
for step in ['prepare_layout.py','sync_art.py']:subprocess.run([sys.executable,str(B/'source'/step)],check=True)
r=json.loads((B/'qa/independent_raw_review.json').read_text())['reviews'];c=json.loads((B/'source/layout_config.json').read_text())['panels'];passed=[]
for n,p in c.items():
 h=hashlib.sha256((B/p['source']).read_bytes()).hexdigest();matches=[x for x in r if x['sha256']==h and int(n) in x.get('panels',[]) and x.get('crop_xyxy')==p['crop']]
 if matches and matches[-1]['verdict']=='pass':passed.append(int(n))
pairs=[i for o in range(1,63,2) if o in passed and o+1 in passed for i in [o,o+1]]
print('Independent passes:',len(passed),'complete pair panels:',len(pairs),flush=True)
(B/'qa/render_ready.txt').write_text(','.join(map(str,pairs)))
if pairs:subprocess.run([sys.executable,str(B/'source/build_chapter.py'),'--panels',','.join(map(str,pairs))],check=True)
