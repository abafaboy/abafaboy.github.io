from pathlib import Path
import json,sys
from PIL import Image,ImageDraw,ImageChops
from build_chapter import balloon,PANELS,glyphs,wrap,rect_overlap
B=Path(__file__).resolve().parents[1];cfg=json.loads((B/'source/layout_config.json').read_text());reports=[]
for key,c in cfg['panels'].items():
 n=int(key);src=Image.open(B/c['source']).crop(c['crop']);aw=c.get('art_width',800);ax=(800-aw)//2;ah=round(src.height*aw/src.width);top,bottom=c.get('extension',[0,0]);h=ah+top+bottom
 im=Image.new('RGB',(1600,h*2),'#faf9f7');im.paste(src.resize((aw*2,ah*2)),(ax*2,top*2));d=ImageDraw.Draw(im)
 if c.get('black_beat_height'):d.rectangle((0,0,1600,c['black_beat_height']*2),fill='#111217')
 protection=Image.new('1',(800,h));pd=ImageDraw.Draw(protection)
 for x,y,w,hh in c.get('protected_boxes',[]):pd.rectangle((x,y,x+w,y+hh),fill=1)
 for poly in c.get('protected_polygons',[]):pd.polygon(poly,fill=1)
 balloon_masks=[]
 for k,lay in c['items'].items():
  item=PANELS[n]['items'][int(k)]
  if item['kind'] not in ('dialogue','sfx'):
   box=lay['box'];x,y,w,hh=box;kind=item['kind'];size=lay.get('font_size',30)
   if not lay.get('text_only'):d.rounded_rectangle((x*2,y*2,(x+w)*2,(y+hh)*2),radius=16,fill='#142b43' if kind=='ui' else '#edf3f6',outline='#88b3c6',width=3)
   bounds=glyphs(d,lay.get('lines',wrap(item['text'],kind,size,w-48)),x+w/2,y+hh/2,kind,size,lay.get('color','#effcff' if kind=='ui' else '#152b3a'))
   hit=[b for b in c.get('protected_boxes',[]) if any(rect_overlap(cb,b)>0 for cb in (bounds if lay.get('text_only') else [box]))] if not lay.get('intentional_surface') else []
   reports.append({'panel':n,'item':k,'collision':hit or None,'kind':kind})
   continue
  if item['kind']!='dialogue' or lay.get('shared_balloon'):continue
  geom=balloon(d,lay.get('body_box',lay['box']),lay.get('tip'),attachment_angle=lay.get('attachment_angle'));mask=Image.new('1',(800,h));ImageDraw.Draw(mask).polygon(geom,fill=1);hit=ImageChops.logical_and(mask,protection).getbbox()
  for prev,prev_mask in balloon_masks:
   cross_hit=ImageChops.logical_and(mask,prev_mask).getbbox()
   reports.append({'panel':n,'item':k,'other_item':prev,'collision':cross_hit,'test':'pairwise balloon/tail'})
  balloon_masks.append((k,mask))
  reports.append({'panel':n,'item':k,'collision':hit})
 im.resize((390,round(h*390/800))).save(B/'qa'/f'geometry_panel_{n:02}.png')
(B/'qa/geometry_report.json').write_text(json.dumps(reports,indent=2));print(json.dumps([r for r in reports if r['collision']],indent=2))
