from pathlib import Path
import json,hashlib,shutil,fitz
B=Path(__file__).resolve().parents[1];p=B/'lettered/PROVISIONAL_Chapter_6_Preview.pdf';m=json.loads((B/'lettered/provisional_placement_manifest.json').read_text());nums=[x['panel'] for x in m['panels']];out=B/f'qa/partial_reader_{len(nums)}units';snap=out/'snapshot';snap.mkdir(parents=True,exist_ok=True);records=[]
with fitz.open(p) as pdf:
 assert len(pdf)==len(m['pages']);assert p.stat().st_size<25_000_000
 for i,page in enumerate(pdf):
  assert not page.get_fonts();pix=page.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False);assert pix.width==390;dest=out/f'page_{i+1:02}.png';pix.save(dest);records.append({'reader_page':i+1,'panels':[x['panel'] for x in m['pages'][i]['panels']],'path':str(dest.relative_to(B)),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
for src in [B/'source/layout_config.json',B/'source/lettering_script.json',B/'source/build_chapter.py',B/'lettered/provisional_placement_manifest.json',p]:shutil.copy2(src,snap/src.name)
(snap/'phone').mkdir(exist_ok=True)
for n in nums:shutil.copy2(B/f'lettered/phone/panel_{n:02}.png',snap/f'phone/panel_{n:02}.png')
(out/'render_index.json').write_text(json.dumps({'status':'partial_proof_not_final','pdf_bytes':p.stat().st_size,'pdf_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'panels':nums,'font_resources':0,'pages':records},indent=2))
(snap/'snapshot_hashes.json').write_text(json.dumps({str(f.relative_to(snap)):hashlib.sha256(f.read_bytes()).hexdigest() for f in snap.rglob('*') if f.is_file() and f.name!='snapshot_hashes.json'},indent=2));print(out, len(nums), 'units',p.stat().st_size,'bytes')
