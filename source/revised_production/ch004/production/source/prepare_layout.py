from pathlib import Path
import json,os,math
from fit_text import fit
B=Path(__file__).resolve().parents[1]
script={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']}
cf=B/'source/layout_config.json';cfg=json.loads(cf.read_text());cfg['font_path']=''
def fitted(text,maxw=620):
 choices=[]
 for h in range(110,431,20):
  for w in range(200,maxw+1,30):
   try:
    lines=fit(text,w-8,h-12,31)
    choices.append((w*h+h*70+max(0,w/h-3)*10000,[w,h],lines))
   except ValueError:pass
 if not choices:raise ValueError(text)
 _,shape,lines=min(choices,key=lambda x:x[0]);return shape,lines
for mf in sorted((B/'source').glob('manifest_*.json')):
 for p in json.loads(mf.read_text()).get('panels',[]):
  n=int(p['panel_id']);key=str(n)
  if key in cfg['panels']:continue
  r=p['crop_xyxy'];sc=800/(r[2]-r[0]);ah=round((r[3]-r[1])*sc)
  def box(b):return [(b[0]-r[0])*sc,(b[1]-r[1])*sc,(b[2]-b[0])*sc,(b[3]-b[1])*sc]
  safe=[box(b) for b in p.get('negative_space_boxes',[])];prot=[box(b) for b in p.get('protected_boxes',[])]
  mouths={k.upper():[(v[0]-r[0])*sc,(v[1]-r[1])*sc] for k,v in p.get('mouths',{}).items()}
  if 'CHAE' in mouths:mouths['ASSESSOR']=mouths['CHAE']
  if 'SEORYUN' in mouths:mouths['SEORYUN, TV']=mouths['SEORYUN']
  c={'source':p['source_image'],'crop':r,'extension':[0,0],'protected_boxes':prot,'mouths':mouths,'source_safe_boxes':safe,'items':{},'auto_layout_unreviewed':True}
  items=script[n]['items'];yy=14;i=0
  # Opposite speakers may share a row only when their actual positions match reading order.
  while i<len(items):
   first=items[i];fm=mouths.get(first['speaker'])
   second=items[i+1] if i+1<len(items) else None;sm=mouths.get(second['speaker']) if second else None
   paired=bool(second and fm and sm and fm[0]+130<sm[0] and first['speaker']!=second['speaker'])
   group=items[i:i+2] if paired else items[i:i+1];ends=[];prev_first=None
   for j,it in enumerate(group):
    (w,h),lines=fitted(it['text'],350 if paired else 620)
    mouth=mouths.get(it['speaker']);mx=mouth[0] if mouth else 400
    x=(24 if j==0 else 776-w) if paired else max(24,min(776-w,mx-w/2))
    y=yy;glyphfirst=y+(h-((len(lines)-1)*31*1.35+24))/2
    if prev_first is not None and glyphfirst<prev_first+24:y+=prev_first+24-glyphfirst;glyphfirst=prev_first+24
    prev_first=glyphfirst
    lay={'box':[x,y,w,h],'lines':lines,'font_size':31}
    if mouth and not it.get('off_panel'):
     dx=max(-55,min(55,mx-(x+w/2)));lay['tip']=[x+w/2+dx,y+h+32]
    c['items'][str(i+j)]=lay;ends.append(y+h+55)
   yy=max(ends);i+=len(group)
  top=math.ceil(yy+10) if items else 0
  c['extension'][0]=top;c['protected_boxes']=[[x,y+top,w,h] for x,y,w,h in prot];c['mouths']={k:[x,y+top] for k,(x,y) in mouths.items()}
  cfg['panels'][key]=c
cf.write_text(json.dumps(cfg,indent=2));print('Prepared',len(cfg['panels']),'panel layouts; visual refinement pending.')
