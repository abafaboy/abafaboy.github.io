from pathlib import Path
import json,hashlib,fitz
B=Path(__file__).resolve().parents[1]
p=B/'lettered/My_Summons_Go_First_Chapter_5.pdf';pdf=fitz.open(p);m=json.loads((B/'lettered/placement_manifest.json').read_text());s=json.loads((B/'source/lettering_script.json').read_text());cfg=json.loads((B/'source/layout_config.json').read_text());raw=json.loads((B/'qa/independent_raw_review.json').read_text())['reviews']
assert len(pdf)==19 and len(m['pages'])==19
assert p.stat().st_size<25_000_000
assert [r['panel'] for r in m['panels']]==list(range(1,39))
assert all(not pg.get_fonts(full=True) for pg in pdf),'No font programs may be embedded'
assert hashlib.sha256((B/'source/script_v1.md').read_bytes()).hexdigest()==s['script_sha256']==m['script_sha256']
count=0;native=0
for art,script in zip(m['panels'],s['panels']):
 n=art['panel'];assert n==script['panel'];assert len(art['items'])==len(script['items'])
 source=B/art['source'];h=hashlib.sha256(source.read_bytes()).hexdigest();assert h==art['sha256']
 assert any(r.get('verdict')=='pass' and n in r['panels'] and r['sha256']==h and r['crop_xyxy']==art['source_crop_xyxy'] for r in raw)
 for item,expected in zip(art['items'],script['items']):
  count+=1
  assert item['text']==expected['text'] and item['speaker']==expected['speaker'] and item['kind']==expected['kind']
  if item.get('native_imagegen_text'):
   native+=1;assert n==36 and item['text']=="Got Sunday off. I'll come over.";assert item['rendering_source']=='unchanged_native_imagegen_pixels';continue
  assert ' '.join(item['lines'])==' '.join(expected['text'].split())
  assert item['phone_equivalent_px']>=14
assert count==58 and native==1
for i,page in enumerate(m['pages']):
 assert [x['panel'] for x in page['panels']]==[2*i+1,2*i+2]
 assert round(pdf[i].rect.width)==390
out={'verdict':'PASS','chapter':5,'panels':38,'pages':19,'text_records':count,'native_phone_text_records':native,'font_programs_in_pdf':0,'pdf_bytes':p.stat().st_size,'pdf_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'script_sha256':s['script_sha256'],'checks':['Exact38 panels,19 consecutive pairs','Under25MB','Exact58 text records','Native phone message preserved and not overlaid','Approved current source hashes/crops','Raster typography no embedded fonts']}
(B/'qa/final_reader_preflight.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
