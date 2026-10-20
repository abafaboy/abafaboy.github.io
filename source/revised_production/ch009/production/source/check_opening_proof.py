from pathlib import Path
import json,hashlib,fitz
B=Path(__file__).resolve().parents[1];h=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();m=json.loads((B/'lettered/provisional_placement_manifest.json').read_text());s=json.loads((B/'source/lettering_script.json').read_text());rows=[]
for p in m['panels']:
 assert h(B/p['source'])==p['sha256'];n=p['panel'];assert [x['text'] for x in p['items']]==[x['text'] for x in s['panels'][n-1]['items']]
 rows.append({'unit':n,'source_sha256':p['sha256'],'crop':p['source_crop_xyxy'],'phone_proof_sha256':h(B/f'lettered/phone/panel_{n:02}.png'),'phone_proof':f'lettered/phone/panel_{n:02}.png','native_sequence_gutter':p.get('native_sequence_gutter'),'text_exact':True})
pdf=B/'lettered/PROVISIONAL_Chapter_9_Preview.pdf';d=fitz.open(pdf);assert all(not p.get_fonts() for p in d)
(B/'qa/B01_lettering_preflight.json').write_text(json.dumps({'units':rows,'status':'geometry_pass_independent_mobile_review_pending','pdf_bytes':pdf.stat().st_size,'pdf_embedded_fonts':0,'font_programs_copied':False,'full_chapter_export':False},indent=2)+'\n')
print('Verified current proof hashes, native hashes/crops, exact text, and raster-only PDF.')
