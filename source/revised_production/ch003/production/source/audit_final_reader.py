from pathlib import Path
import json,hashlib,fitz
from PIL import Image
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
m=json.loads((B/'lettered/placement_manifest.json').read_text());s=json.loads((B/'source/lettering_script.json').read_text())
assert len(m['panels'])==62 and len(m['pages'])==31
layout=json.loads((B/'source/layout_config.json').read_text())
assert all(not p.get('auto_layout_unreviewed',True) and not p.get('source_revision_needs_visual_recheck',False) for p in layout['panels'].values())
expected={(p['panel'],i):r['text'] for p in s['panels'] for i,r in enumerate(p['items'])};actual={(p['panel'],r['index']):r['text'] for p in m['panels'] for r in p['items']}
assert actual==expected and len(expected)==89
assert m['script_sha256']==sha(B/'source/script_v1.md')==s['script_sha256']
rr=json.loads((B/'qa/independent_raw_review.json').read_text())['reviews']
for p in m['panels']:
 assert sha(B/p['source'])==p['sha256']
 matches=[r for r in rr if r['sha256']==p['sha256'] and p['panel'] in r.get('panels',[]) and r.get('crop_xyxy')==p['source_crop_xyxy']]
 assert matches and matches[-1]['verdict']=='pass'
pdf=B/'lettered/My_Summons_Go_First_Chapter_3.pdf';doc=fitz.open(pdf)
assert len(doc)==31 and all(not p.get_fonts() and not p.get_text().strip() and len(p.get_images())==1 for p in doc)
assert pdf.stat().st_size<25*1024*1024
fr=json.loads((B/'qa/independent_lettered_review.json').read_text())
assert fr['pdf_sha256']==sha(pdf)
for i,page in enumerate(doc,1):
 p=B/f'qa/pdf390/page_{i:02}.png';assert Image.open(p).width==390
 pix=page.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False)
 assert Image.open(p).convert('RGB').tobytes()==pix.samples,('Actual PDF pixel mismatch',i)
 assert any(r['verdict']=='pass' and r['sha256']==sha(p) and r['page']==i for r in fr['reviews'])
report={'status':'pass','panels':62,'reader_pages':31,'dialogue_records_exact':89,'image_generated_text_records':sum(len(p['generated_text']) for p in s['panels']),'pdf_bytes':pdf.stat().st_size,'pdf_sha256':sha(pdf),'pdf_font_programs':0,'reader_width':390,'minimum_dialogue_phone_px':min(r['phone_equivalent_px'] for p in m['panels'] for r in p['items']),'source_hashes_and_panel_passes_verified':True,'actual_compressed_pdf_390_pages_independently_reviewed':31}
(B/'qa/final_reader_technical_audit.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
