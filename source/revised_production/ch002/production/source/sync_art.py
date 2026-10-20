from pathlib import Path
import json
B=Path(__file__).resolve().parents[1]; cp=B/'source/layout_config.json';cfg=json.loads(cp.read_text())
for mf in sorted((B/'source').glob('manifest_*.json')):
 data=json.loads(mf.read_text())
 panels=data.get('panels',[]) if isinstance(data,dict) else []
 for p in panels:
  n=str(p.get('panel_id',p.get('id',p.get('panel'))))
  if n not in cfg['panels']:continue
  c=cfg['panels'][n];r=p.get('crop_xyxy',p.get('rect',p.get('crop')));sc=800/(r[2]-r[0]);top=c.get('extension',[0,0])[0]
  path=p.get('source_image',p.get('source'))
  if not path:continue
  if c['source']!=path:c['source_revision_needs_visual_recheck']=True
  c['source']=path;c['crop']=r
  c['protected_boxes']=[[(a-r[0])*sc,(b-r[1])*sc+top,(x-a)*sc,(y-b)*sc] for a,b,x,y in p.get('protected_boxes',[])]
  if c.get('protected_boxes_override'):c['protected_boxes']=c['protected_boxes_override']
  c['mouths']={k.upper():[(v[0]-r[0])*sc,(v[1]-r[1])*sc+top] for k,v in p.get('mouths',{}).items()}
cp.write_text(json.dumps(cfg,indent=2))
print('Synchronized current art source/crop/protection; existing lettering retained for review.')
