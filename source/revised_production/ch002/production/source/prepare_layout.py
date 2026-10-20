from pathlib import Path
import json,math,os
from PIL import ImageFont,ImageDraw,Image
B=Path(__file__).resolve().parents[1]
FONT=os.environ.get('ANIME_ACE_FONT','')
font=ImageFont.truetype(FONT,31)
d=ImageDraw.Draw(Image.new('RGB',(1,1)))
script={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']}
cf=B/'source/layout_config.json';cfg=json.loads(cf.read_text());cfg['font_path']=''
def normalize_pages(data):
 if isinstance(data,list):return data
 
 if 'panels' in data and data['panels'] and 'source_image' in data['panels'][0]:
  grouped={}
  for p in data['panels']:grouped.setdefault(p['source_image'],[]).append(p)
  return [{'path':k,'panels':v} for k,v in grouped.items()]
 return data.get('pages',data.get('images',[data]))
def wrap(text,width):
 lines=[];line=''
 for word in text.split():
  t=(line+' '+word).strip()
  if d.textlength(t.lower(),font=font)>width and line:lines.append(line);line=word
  else:line=t
 if line:lines.append(line)
 return lines
for mf in sorted((B/'source').glob('manifest_*.json')):
 for page in normalize_pages(json.loads(mf.read_text())):
  path=page.get('path',page.get('image',page.get('file')))
  if not path:continue
  for p in page.get('panels',[]):
   n=int(p.get('id',p.get('panel',p.get('panel_id'))))
   if str(n) in cfg['panels']:continue
   r=p.get('rect',p.get('crop',p.get('crop_xyxy'))); scale=800/(r[2]-r[0]); ah=round((r[3]-r[1])*scale)
   def box(b):return [(b[0]-r[0])*scale,(b[1]-r[1])*scale,(b[2]-b[0])*scale,(b[3]-b[1])*scale]
   safe=[box(b) for b in p.get('safe_boxes',p.get('safe',p.get('negative_space_boxes',[])))]
   prot=[box(b) for b in p.get('protected_boxes',p.get('protected',[]))]
   mouths={k.upper():[(v[0]-r[0])*scale,(v[1]-r[1])*scale] for k,v in p.get('mouths',{}).items()}
   c={'source':path.removeprefix('production/'),'crop':r,'extension':[0,0],'protected_boxes':prot,'mouths':mouths,'source_safe_boxes':safe,'items':{},'auto_layout_unreviewed':True}
   items=script[n]['items']
   # Initial conservative placement is a review draft. Explicit later layout edits
   # may move balloons into useful art spaces after the actual panel is inspected.
   if items:
    layouts=[]
    for i,it in enumerate(items):
     maxw=650 if len(items)==1 else 330
     lines=wrap(it['text'],maxw-100)
     widest=max(d.textlength(t.lower(),font=font) for t in lines)
     w=min(maxw,max(190,widest+110));h=round(len(lines)*42+75)
     layouts.append({'box':[0,0,w,h],'lines':lines,'font_size':31})
    if len(layouts)==1:
     l=layouts[0];w,h=l['box'][2:];found=None
     for sx,sy,sw,sh in safe:
      if sw>=w+20 and sh>=h+20:found=[sx+10,sy+10,w,h];break
     if found:l['box']=found
     else:c['extension'][0]=h+30;l['box']=[(800-w)/2,12,w,h]
    else:
     yy=12
     for i,l in enumerate(layouts):
      w,h=l['box'][2:];l['box']=[30 if i%2==0 else 770-w,yy,w,h]
      if i%2==0 and i+1<len(layouts): yy+=max(0,h-layouts[i+1]['box'][3])+10
      else:yy+=h+15
     c['extension'][0]=max(l['box'][1]+l['box'][3] for l in layouts)+20
    top=c['extension'][0]
    if top:
     c['protected_boxes']=[[x,y+top,w,h] for x,y,w,h in prot]
     c['mouths']={k:[x,y+top] for k,(x,y) in mouths.items()}
    for i,(it,l) in enumerate(zip(items,layouts)):
     if it['kind']=='dialogue':
      mouth=c['mouths'].get(it['speaker'])
      if mouth:
       cx=l['box'][0]+l['box'][2]/2;cy=l['box'][1]+l['box'][3]/2
       dx,dy=cx-mouth[0],cy-mouth[1];length=math.hypot(dx,dy)
       # Start with a short, intelligible pointer; exact tail route is visually reviewed.
       l['tip']=[mouth[0]+dx/length*65,mouth[1]+dy/length*65] if length else mouth
     c['items'][str(i)]=l
   cfg['panels'][str(n)]=c
cf.write_text(json.dumps(cfg,indent=2))
print('Configured',len(cfg['panels']),'panels; new layouts require actual visual review.')
