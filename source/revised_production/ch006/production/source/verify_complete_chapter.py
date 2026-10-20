from pathlib import Path
import json,hashlib,fitz
from PIL import Image
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s=json.loads((B/'source/lettering_script.json').read_text());m=json.loads((B/'lettered/placement_manifest.json').read_text());c=json.loads((B/'source/layout_config.json').read_text());assert [p['panel'] for p in m['panels']]==list(range(1,42));assert len(m['pages'])==21
count=0;records=[]
for sp,p in zip(s['panels'],m['panels']):
 assert len(sp['items'])==len(p['items'])
 for i,(a,b) in enumerate(zip(sp['items'],p['items'])):
  assert a['text']==b['text'] and a['kind']==b['kind'] and b['index']==i;count+=1
 for kind in ['full','phone']:
  f=B/f"lettered/{kind}/panel_{p['panel']:02}.png";im=Image.open(f);assert im.width==(1600 if kind=='full' else 390);records.append(dict(path=str(f.relative_to(B)),bytes=f.stat().st_size,sha256=sha(f)))
assert count==70
pdf=B/'lettered/My_Summons_Go_First_Chapter_6.pdf';d=fitz.open(pdf);assert len(d)==21 and pdf.stat().st_size<25_000_000 and all(not p.get_fonts() for p in d)
for name in ['lettered/My_Summons_Go_First_Chapter_6.pdf','lettered/placement_manifest.json','source/layout_config.json','source/lettering_script.json','source/script_v1.md']:
 f=B/name;records.append(dict(path=name,bytes=f.stat().st_size,sha256=sha(f)))
for f in sorted((B/'qa/pdf390').glob('*.png')):records.append(dict(path=str(f.relative_to(B)),bytes=f.stat().st_size,sha256=sha(f)))
report=dict(chapter=6,units=41,reader_pages=21,text_items=70,pdf_bytes=pdf.stat().st_size,pdf_sha256=sha(pdf),font_resources=0,script_sha256=sha(B/'source/script_v1.md'),mechanical_checks='pass',independent_visual_acceptance='separate_required',files=records)
(B/'qa/final_mechanical_verification.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='files'},indent=2))
