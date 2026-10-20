from pathlib import Path
import json,hashlib,fitz
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((B/'source/layout_config.json').read_text());raw=json.loads((B/'qa/independent_raw_review.json').read_text())['reviews'];reviews=[]
for p in sorted((B/'qa').glob('independent_lettering*.json'),key=lambda p:p.stat().st_mtime):
 for r in json.loads(p.read_text()).get('reviews',[]):reviews.append({**r,'ledger':p.name})
out=[]
for n in range(1,34):
 cfg=c['panels'][str(n)];phone=B/f'lettered/phone/panel_{n:02}.png';r={'unit':n,'raw_sources':[],'phone_exists':phone.exists()}
 for frame in [cfg]+cfg.get('native_following_frames',[]):
  if not frame.get('source'):continue
  src=B/frame['source'];h=sha(src);matches=[v for v in raw if v.get('sha256')==h and n in v.get('panels',[]) and v.get('crop_xyxy')==frame['crop']]
  r['raw_sources'].append({'source':frame['source'],'sha256':h,'crop':frame['crop'],'latest_verdict':matches[-1]['verdict'] if matches else 'unreviewed'})
 if phone.exists():
  h=sha(phone);matches=[v for v in reviews if v.get('sha256')==h and n in v.get('panels',[]) and v.get('proof_path','').endswith(f'panel_{n:02}.png')];r.update(phone_sha256=h,lettering_verdict=matches[-1]['verdict'] if matches else 'unreviewed',lettering_ledger=matches[-1]['ledger'] if matches else None)
 r['accepted_exact_current']=bool(r['raw_sources']) and all(v['latest_verdict']=='pass' for v in r['raw_sources']) and r.get('lettering_verdict')=='pass';out.append(r)
pdf=B/'lettered/My_Summons_Go_First_Chapter_9.pdf'
if not pdf.exists():pdf=B/'lettered/PROVISIONAL_Chapter_9_Preview.pdf'
doc=fitz.open(pdf)
result={'scope':'Exact current hash-bound raw and actual390 lettering gates only. Full paired-page/continuity/final delivery acceptance separate.','units':out,'accepted_units':[r['unit'] for r in out if r['accepted_exact_current']],'pending_units':[r['unit'] for r in out if not r['accepted_exact_current']],'current_pdf':{'name':pdf.name,'bytes':pdf.stat().st_size,'under_25MB':pdf.stat().st_size<25000000,'pages':len(doc),'fonts_embedded':any(p.get_fonts() for p in doc)},'script_hash_matches':sha(B/'source/script_v1.md')==json.loads((B/'source/lettering_script.json').read_text())['script_sha256']}
(B/'qa/current_acceptance_preflight.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps({k:v for k,v in result.items() if k!='units'},indent=2))
