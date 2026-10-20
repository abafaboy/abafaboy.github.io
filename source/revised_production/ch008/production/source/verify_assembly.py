"""Read-only Chapter 8 source/reader delivery audit, safe at any progress point."""
from pathlib import Path
import json,hashlib,zipfile
import fitz
B=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s=json.loads((B/'source/lettering_script.json').read_text());auth=json.loads((B/'source/panels_and_dialogue.json').read_text());cfg=json.loads((B/'source/layout_config.json').read_text())
assert s['chapter']==8 and cfg['chapter']==8
assert [p['panel'] for p in s['panels']]==list(range(1,37))
assert sha(B/'source/script_v1.md')==s['script_sha256']=='edc573f7ec3ed6b39b6da072c395b87d6d19147b79b5947c6d7151c8c7410a38'
assert sha(B/'source/panels_and_dialogue.json')==s['dialogue_json_sha256']
assert all([x['text'] for x in a['dialogue']]==[x['text'] for x in b['items']] for a,b in zip(auth,s['panels']))
assert not any(B.rglob('*.otf')) and not any(B.rglob('*.ttf')) and not any(B.rglob('*.woff')) and not any(B.rglob('*.woff2'))
report={'chapter':8,'script_and_text_integrity':'pass','source_font_programs':0,'reader':None}
pdf=B/'lettered/My_Summons_Go_First_Chapter_8.pdf'
if pdf.exists():
 assert pdf.stat().st_size<25_000_000
 with fitz.open(pdf) as d:
  assert len(d)==18
  assert all(not page.get_fonts() for page in d)
  assert all(not page.get_text().strip() for page in d)
 report['reader']={'bytes':pdf.stat().st_size,'sha256':sha(pdf),'pages':18,'font_programs':0,'raster_only':True}
for z in (B/'delivery').glob('*.zip') if (B/'delivery').exists() else []:
 assert z.stat().st_size<512*1024*1024
 with zipfile.ZipFile(z) as f:assert not [n for n in f.namelist() if Path(n).suffix.lower() in ('.otf','.ttf','.woff','.woff2')]
(B/'qa/assembly_integrity.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
