from pathlib import Path
import json,hashlib,fitz
B=Path(__file__).resolve().parents[1];p=B/'lettered/My_Summons_Go_First_Chapter_3.pdf';d=fitz.open(p);m=json.loads((B/'lettered/placement_manifest.json').read_text());assert len(d)==len(m['pages']);out=B/'qa/pdf390';out.mkdir(exist_ok=True,parents=True);records=[]
for page,rec in zip(d,m['pages']):
 dest=out/f"page_{rec['page']:02}.png";pix=page.get_pixmap(matrix=fitz.Matrix(1,1),alpha=False);assert pix.width==390;pix.save(dest);records.append({'page':rec['page'],'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'panels':[r['panel'] for r in rec['panels']],'width':pix.width,'height':pix.height})
(out/'render_index.json').write_text(json.dumps({'pdf_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'complete_chapter':len(d)==31,'pages':records},indent=2));print('Exported',len(records),'actual compressed PDF pages at390.')
