from pathlib import Path
import json,hashlib,fitz
from PIL import Image
B=Path(__file__).resolve().parents[1]
m=json.loads((B/'lettered/placement_manifest.json').read_text());s=json.loads((B/'source/lettering_script.json').read_text());assert len(m['panels'])==61 and len(m['pages'])==31
expected={(p['panel'],i):r['text'] for p in s['panels'] for i,r in enumerate(p['items'])};actual={(p['panel'],r['index']):r['text'] for p in m['panels'] for r in p['items']};assert all(actual[k]==v for k,v in expected.items());assert len(expected)==58 and len(actual)==58
for p in m['panels']:assert hashlib.sha256((B/p['source']).read_bytes()).hexdigest()==p['sha256']
for p in m['pages']:assert Image.open(B/f"lettered/reader/page_{p['page']:02}_phone.png").width==390
pdf=B/'lettered/My_Summons_Go_First_Chapter_2.pdf';doc=fitz.open(pdf);assert len(doc)==31;assert all(not p.get_fonts() and not p.get_text().strip() and len(p.get_images())==1 for p in doc)
assert pdf.stat().st_size < 25*1024*1024, 'Reader exceeds requested attachment target'
report={'pdf_bytes':pdf.stat().st_size,'status':'pass','canonical_records_exact':58,'tagged_props_and_continuity':0,'panels':61,'reader_pages':31,'phone_width':390,'minimum_dialogue_phone_px':min(r['phone_equivalent_px'] for p in m['panels'] for r in p['items'] if r['kind']=='dialogue'),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pdf_font_programs':0,'flattened_page_images':31,'source_hashes_verified':True,'visual_independent_review':'separate report'}

raw_reviews=json.loads((B/'qa/independent_raw_review.json').read_text())['reviews']
raw_pass={r['sha256'] for r in raw_reviews if r['verdict']=='pass'}
assert all(p['sha256'] in raw_pass for p in m['panels'])
lettered_reviews=json.loads((B/'qa/independent_lettered_review.json').read_text())['reviews']
phone_pass={r['sha256'] for r in lettered_reviews if r['verdict']=='pass'}
assert all(hashlib.sha256((B/f"lettered/reader/page_{p['page']:02}_phone.png").read_bytes()).hexdigest() in phone_pass for p in m['pages']), 'Current reader page lacks independent 390px PASS'
report.update({'independent_raw_current_hashes_pass':61,'independent_390px_current_page_hashes_pass':31})
(B/'qa/final_reader_technical_audit.json').write_text(json.dumps(report,indent=2))
print('All current independent review hashes verified.')
