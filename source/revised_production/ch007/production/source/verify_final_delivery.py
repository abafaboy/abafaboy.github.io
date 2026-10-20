from pathlib import Path
import json,hashlib,fitz
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
pdf=B/'lettered/My_Summons_Go_First_Chapter_7.pdf';m=json.loads((B/'lettered/placement_manifest.json').read_text());s=json.loads((B/'source/lettering_script.json').read_text());raw=json.loads((B/'qa/independent_raw_review.json').read_text())['reviews'];a=json.loads((B/'source/panels_and_dialogue.json').read_text());cfg=json.loads((B/'source/layout_config.json').read_text())
assert [p['panel'] for p in m['panels']]==list(range(1,35))
assert m['script_sha256']==sha(B/'source/script_v1.md')==sha(B.parent/'script_v1.md')
spoken=[];native=[]
for original,script,rendered in zip(a,s['panels'],m['panels']):
 n=rendered['panel'];assert [x['text'] for x in rendered['items']]==[x['text'] for x in script['items']]
 assert [x['text'] for x in rendered['items'] if x['kind']=='dialogue']==[x['text'] for x in original['dialogue']]
 source=(B/rendered['source']);assert sha(source)==rendered['sha256'];matches=[r for r in raw if n in r['panels'] and r['sha256']==rendered['sha256'] and r['crop_xyxy']==rendered['source_crop_xyxy']];assert matches and matches[-1]['verdict']=='pass'
 for x in rendered['items']:
  if x['kind']=='dialogue':assert x['phone_equivalent_px']>=14;spoken.append(x)
  if x.get('native_imagegen_required'):assert x['rendering_source']=='unchanged_native_imagegen_pixels' and x['native_visual_qa']=='pass' and x['verified_text']==x['text'];native.append(x)
with fitz.open(pdf) as d:
 assert len(d)==17;assert all(not p.get_fonts() for p in d);assert all(round(p.rect.width)==390 for p in d)
assert len(spoken)==70 and len(native)==4 and pdf.stat().st_size<25_000_000
out={'chapter':7,'pdf_sha256':sha(pdf),'pdf_bytes':pdf.stat().st_size,'pages':17,'panels':34,'spoken_lines':70,'native_device_rows':4,'embedded_font_count':0,'dialogue_min_phone_px':min(x['phone_equivalent_px'] for x in spoken),'script_sha256':m['script_sha256'],'exact_text_order_verified':True,'current_raw_source_hash_crop_passes_verified':True,'native_device_text_unmodified':True,'technical_verdict':'pass','independent_final_reader_verdict_required_separately':True}
(B/'qa/final_technical_verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
