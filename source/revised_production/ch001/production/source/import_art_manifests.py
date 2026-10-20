from pathlib import Path
import json
B=Path(__file__).resolve().parents[1];cf=B/'source/layout_config.json';cfg=json.loads(cf.read_text());
for mf in list((B/'source').glob('manifest_*.json'))+list((B/'manifests').glob('*.json')):
 data=json.loads(mf.read_text());pages=data if isinstance(data,list) else ([data] if 'panels' in data else data.get('pages',[]))
 for page in pages:
  for p in page['panels']:
   n=p.get('id',p.get('panel'));r=p.get('rect',p.get('crop'));c=cfg['panels'].setdefault(str(n),{'source':page.get('path',page.get('image','')).removeprefix('production/'),'items':{}});aw=c.get('art_width',800);sc=aw/(r[2]-r[0]);ax=(800-aw)//2;top=c.get('extension',[0,0])[0]
   c['source']=page.get('path',page.get('image','')).removeprefix('production/');c['crop']=r;c['protected_boxes']=[[(a-r[0])*sc+ax,(b-r[1])*sc+top,(x-a)*sc,(y-b)*sc] for a,b,x,y in p.get('protected_boxes',p.get('protected',[]))];c['mouths']={k:[(v[0]-r[0])*sc+ax,(v[1]-r[1])*sc+top] for k,v in p.get('mouths',{}).items()};c['source_safe_boxes']=p.get('safe_boxes',p.get('safe',[]))
   if c.get('protection_override'):c['protected_boxes']=[]
cf.write_text(json.dumps(cfg,indent=2))
