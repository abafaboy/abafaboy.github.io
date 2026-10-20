"""Index untouched intake archives and stable Library provenance without transport tokens."""
from pathlib import Path
import json,hashlib
B=Path(__file__).resolve().parents[1]
rows=[]
for p in sorted((B/'incoming').glob('*library_receipt.json')):
 obj=json.loads(p.read_text())
 for tr in obj.get('transfers',obj.get('structuredContent',{}).get('transfers',obj.get('result',{}).get('transfers',[]))):
  local=Path(tr.get('workspace_path',''))
  if not local.is_file():continue
  rows.append({'receipt_file':str(p.relative_to(B)),'archive_file':str(local.relative_to(B)),'bytes':local.stat().st_size,'sha256':hashlib.sha256(local.read_bytes()).hexdigest(),'library_file_id':tr.get('library_file_id'),'file_id':tr.get('file_id'),'file_name':tr.get('file_name'),'version':tr.get('current_version_number')})
out={'chapter':8,'intake_archives':rows,'total_archive_bytes':sum(r['bytes'] for r in rows),'archive_count':len(rows),'retention':'Every listed intake archive is retained untouched. Repeated/superseded checkpoints preserve full native-generation history. No font programs are delivery assets.','export_note':'Use this stable provenance index in deliveries, not transport-bearing raw tool receipts.'}
(B/'source/source_archive_inventory.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(len(rows),'archives;',out['total_archive_bytes'],'bytes')
