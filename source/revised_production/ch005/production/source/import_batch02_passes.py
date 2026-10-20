from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1];q=json.loads((B/'qa/incoming_v1/Chapter5_Independent_QA/qa_ledger.json').read_text());cfg=json.loads((B/'source/layout_config.json').read_text());pending=json.loads((B/'source/batch02_pending_layouts.json').read_text());review=json.loads((B/'qa/independent_raw_review.json').read_text())
for p in q['panels']:
 n=p['panel']
 if n not in (29,30,31,33,35) or p['raw_art_verdict']!='PASS':continue
 c=pending[str(n)];path=B/c['source'];assert hashlib.sha256(path.read_bytes()).hexdigest()==p['source_native_sha256'];assert c['crop']==p['source_crop_xyxy'];c['acceptance_status']='independent_pass';cfg['panels'][str(n)]=c
 review['reviews'].append({'panels':[n],'sha256':p['source_native_sha256'],'crop_xyxy':p['source_crop_xyxy'],'verdict':'pass','source_qa_library_id':'libfile_9d04b5e512248191bd50e39772462c99','source_qa_version':1})
(B/'qa/independent_raw_review.json').write_text(json.dumps(review,indent=2));(B/'source/layout_config.json').write_text(json.dumps(cfg,indent=2))
