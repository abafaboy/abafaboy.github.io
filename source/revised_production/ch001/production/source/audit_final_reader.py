from pathlib import Path
import json,hashlib,fitz
from PIL import Image
B=Path(__file__).resolve().parents[1]
m=json.loads((B/'lettered/placement_manifest.json').read_text());s=json.loads((B/'source/lettering_script.json').read_text());assert len(m['panels'])==64 and len(m['pages'])==32
expected={(p['panel'],i):r['text'] for p in s['panels'] for i,r in enumerate(p['items'])};actual={(p['panel'],r['index']):r['text'] for p in m['panels'] for r in p['items']};assert all(actual[k]==v for k,v in expected.items());assert len(expected)==71 and len(actual)==78
for p in m['panels']:assert hashlib.sha256((B/p['source']).read_bytes()).hexdigest()==p['sha256']
for p in m['pages']:assert Image.open(B/f"lettered/reader/page_{p['page']:02}_phone.png").width==390
pdf=B/'lettered/My_Summons_Go_First_Chapter_1.pdf';doc=fitz.open(pdf);assert len(doc)==32;assert all(not p.get_fonts() and not p.get_text().strip() and len(p.get_images())==1 for p in doc)
report={'status':'pass','canonical_records_exact':71,'tagged_props_and_continuity':7,'panels':64,'reader_pages':32,'phone_width':390,'minimum_dialogue_phone_px':min(r['phone_equivalent_px'] for p in m['panels'] for r in p['items'] if r['kind']=='dialogue'),'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'pdf_font_programs':0,'flattened_page_images':32,'source_hashes_verified':True,'visual_independent_review':'separate report'}
(B/'qa/final_reader_technical_audit.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
