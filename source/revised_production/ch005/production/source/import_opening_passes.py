from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1];m=json.loads((B/'raw/opening/batch_manifest.json').read_text());cfg=json.loads((B/'source/layout_config.json').read_text());pending=json.loads((B/'source/opening_pending_layouts.json').read_text());rev=json.loads((B/'qa/independent_raw_review.json').read_text())
for p in m['panels']:
 n=p['panel_id']
 if n>12:continue
 c=pending[str(n)];assert hashlib.sha256((B/c['source']).read_bytes()).hexdigest()==p['source_sha256'];c['acceptance_status']='independent_pass';cfg['panels'][str(n)]=c
 rev['reviews'].append({'panels':[n],'sha256':p['source_sha256'],'crop_xyxy':p['crop_xyxy'],'verdict':'pass','reviewer':'review_fifth_opening_art','authorization':'Exact batch manifest selections passed in independent reviewer report and parent relay, 2026-10-18 19:57 UTC'})
(B/'qa/independent_raw_review.json').write_text(json.dumps(rev,indent=2));(B/'source/layout_config.json').write_text(json.dumps(cfg,indent=2))
