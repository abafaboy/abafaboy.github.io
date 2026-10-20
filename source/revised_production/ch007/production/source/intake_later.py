from pathlib import Path
import json,hashlib
from PIL import Image
B=Path(__file__).resolve().parents[1];rows=[]
def add(n,p,crop=None):
 im=Image.open(p);crop=crop or [0,0,*im.size];q=im.crop(crop);out=B/f'qa/P{n:02}_intake_390.png';q.resize((390,round(q.height*390/q.width)),Image.Resampling.LANCZOS).save(out);rows.append({'panel':n,'source':str(p),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'crop_xyxy':crop,'preview_390':str(out),'status':'pending_independent_review'})
for sub,key in [('B02/Chapter7_B02','selected'),('B07/B07','selection')]:
 r=B/'raw'/sub
 for n,p in json.loads((r/'manifest.json').read_text())[key].items():add(int(n[1:]),r/p)
r=B/'raw/B08_complete/B08_P24-27'
for p in json.loads((r/'manifests/B08_batch_manifest.json').read_text())['selected']:
 if p['unit']==24:continue
 source=r/f"originals/{p['version']}.png";assert hashlib.sha256(source.read_bytes()).hexdigest()==p['sha256'];add(p['unit'],source,p['crop_xyxy'])
for manifest in (B/'raw/B04').glob('*/selected_crop_mapping.json'):
 for p in json.loads(manifest.read_text())['selected']:add(int(p['unit'][1:]),manifest.parent/p['native_file'],p['crop_source_pixels_xyxy'])
(B/'qa/B02_B04_B07_B08_intake.json').write_text(json.dumps(rows,indent=2));print([(r['panel'],r['crop_xyxy']) for r in rows])
