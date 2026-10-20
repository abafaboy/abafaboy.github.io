from pathlib import Path
import os,json,math,hashlib,io,argparse
from PIL import Image,ImageDraw,ImageFont
import fitz
B=Path(__file__).resolve().parents[1]; SCRIPT=json.loads((B/'source/lettering_script.json').read_text()); PANELS={p['panel']:p for p in SCRIPT['panels']}

W=800; SCALE=2; LAST_GLYPHS=[]
FONT=os.environ.get('ANIME_ACE_FONT',''); UI=os.environ.get('UI_FONT','/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def rect_overlap(a,b):return max(0,min(a[0]+a[2],b[0]+b[2])-max(a[0],b[0]))*max(0,min(a[1]+a[3],b[1]+b[3])-max(a[1],b[1]))
def comic_case(s):
 import re
 return re.sub(r"\bi(?=[’'….,!? ]|$)",'I',s.lower())
def font_for(kind,size):return ImageFont.truetype(FONT if kind in ('dialogue','sfx') else UI,round(size*SCALE))
def wrap(s,kind,size,width):
 d=ImageDraw.Draw(Image.new('RGB',(1,1)));f=font_for(kind,size);ls=[];line=''
 for word in s.split():
  trial=(line+' '+word).strip();show=comic_case(trial) if kind in ('dialogue','sfx') else trial
  if d.textlength(show,font=f)>width*SCALE and line:ls.append(line);line=word
  else:line=trial
 if line:ls.append(line)
 return ls

def glyphs(d,lines,cx,cy,kind,size,color='#15191c',halo=False):
 global LAST_GLYPHS
 LAST_GLYPHS=[]
 from fontTools.ttLib import TTFont
 f=font_for(kind,size);fallback=ImageFont.truetype(UI,round(size*SCALE));cmap=TTFont(FONT if kind in ('dialogue','sfx') else UI).getBestCmap()
 pitch=size*1.35;show=[comic_case(t) if kind in ('dialogue','sfx') else t for t in lines]
 missing={c for line in show for c in line if ord(c) not in cmap}
 assert missing <= {'—'}, ('Unexpected missing font glyphs', missing)
 runs=[[(c,f if ord(c) in cmap else fallback) for c in line] for line in show]
 hh=max(d.textbbox((0,0),'H',font=ft)[3]-d.textbbox((0,0),'H',font=ft)[1] for run in runs for c,ft in run);total=(len(lines)-1)*pitch*SCALE+hh;out=[]
 for j,run in enumerate(runs):
  width=sum(d.textlength(c,font=ft) for c,ft in run);x=cx*SCALE-width/2;start=x;y=cy*SCALE-total/2+j*pitch*SCALE
  for c,ft in run:
   top=d.textbbox((0,0),'H',font=ft)[1];bb=d.textbbox((x,y-top),c,font=ft);LAST_GLYPHS.append({'glyph':c,'bounds_xyxy':[v/SCALE for v in bb],'fallback':ft==fallback});d.text((x,y-top),c,font=ft,fill=color,stroke_width=2*SCALE if halo else 0,stroke_fill='white');x+=d.textlength(c,font=ft)
  out.append([start/SCALE,y/SCALE,width/SCALE,hh/SCALE])
 return out

def balloon(d,box,tip=None,signal=False,attachment_angle=None):
 x,y,w,h=box;cx=x+w/2;cy=y+h/2;rx=w/2;ry=h/2
 def pt(t):return (cx+rx*math.cos(t)*(1+.007*math.sin(3*t+.7)),cy+ry*math.sin(t)*(1+.008*math.sin(2*t+.2)))
 if tip is None:pts=[pt(2*math.pi*k/240) for k in range(241)]
 else:
  angle=attachment_angle if attachment_angle is not None else math.atan2((tip[1]-cy)/ry,(tip[0]-cx)/rx);spread=.075
  pts=[pt(angle+spread+(2*math.pi-2*spread)*k/200) for k in range(201)]
  # Smooth two-sided taper, straight shared centerline: no neck or contour crossing.
  a,z=pts[0],pts[-1];mid=((a[0]+z[0])/2,(a[1]+z[1])/2)
  for k in range(1,25):
   t=k/25;pts.append((z[0]*(1-t)+tip[0]*t,z[1]*(1-t)+tip[1]*t))
  pts.append(tuple(tip))
  for k in range(1,25):
   t=k/25;pts.append((tip[0]*(1-t)+a[0]*t,tip[1]*(1-t)+a[1]*t))
 def cross(a,b,c):return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
 edges=list(zip(pts,pts[1:]+[pts[0]]))
 for ii,(a,b) in enumerate(edges):
  for jj in range(ii+2,len(edges)):
   if ii==0 and jj==len(edges)-1:continue
   c,e=edges[jj]
   assert not (cross(a,b,c)*cross(a,b,e)<-1e-8 and cross(c,e,a)*cross(c,e,b)<-1e-8),('Self-intersecting balloon outline',box,tip,ii,jj)
 pp=[(round(a*SCALE),round(b*SCALE)) for a,b in pts];d.polygon(pp,fill='#fffefd');d.line(pp+[pp[0]],fill='#20232a',width=3*SCALE,joint='curve')
 # Phone-transmitted dialogue remains tailless where configured; avoid interior signal marks touching glyphs.
 return pts

def render_panel(n,cfg):
 p=PANELS[n];
 assert set(cfg['items'])=={str(i) for i in range(len(p['items']))}, ('Missing or extra text placements',n)
 assert cfg.get('protection_reviewed') is True, ('Pixel-based protected art review required',n)
 assert cfg.get('source') and cfg.get('crop'), ('Artwork and crop required',n)
 src=Path(cfg['source']);src=src if src.is_absolute() else B/src
 review_path=B/'qa/independent_raw_review.json'
 reviewed=json.loads(review_path.read_text())['reviews']
 source_hash=digest(src)
 matches=[r for r in reviewed if r.get('sha256')==source_hash and n in r.get('panels',[]) and r.get('crop_xyxy')==cfg['crop']]
 assert matches and matches[-1].get('verdict') == 'pass',('Source lacks current independent pass',n,str(src))
 im0=Image.open(src).convert('RGB');crop=cfg['crop'];cropped=im0.crop(crop);aw=cfg.get('art_width',W);ax=(W-aw)//2;ah=round(cropped.height*aw/cropped.width)
 top,bottom=map(round,cfg.get('extension',[0,0]));h=ah+top+bottom
 im=Image.new('RGB',(W*SCALE,h*SCALE),'#faf9f7');im.paste(cropped.resize((aw*SCALE,ah*SCALE),Image.Resampling.LANCZOS),(ax*SCALE,top*SCALE));d=ImageDraw.Draw(im)
 if cfg.get('black_beat_height'):d.rectangle((0,0,W*SCALE,cfg['black_beat_height']*SCALE),fill='#111217')
 records=[];balloon_masks=[]
 for i,item in enumerate(p['items']):
  lay=cfg['items'][str(i)];kind=item['kind']
  if item.get('native_imagegen_required'):assert lay.get('native_imagegen_text') and lay.get('native_visual_qa')=='pass', (n,i,'Exact native imagegen UI pixels require visual approval')
  if lay.get('native_imagegen_text'):
   assert lay['verified_text']==item['text'],(n,i,'Native text mismatch')
   assert kind in ('phone','ui','prop','phone_info'),(n,i,'Unexpected native dialogue')
   records.append({'panel':n,'index':i,**item,**lay,'rendering_source':'unchanged_native_imagegen_pixels','source_sha256':source_hash,'line_bounds':[],'glyph_bounds':[],'balloon_outline':None})
   continue
  size=lay.get('font_size',31 if kind=='dialogue' else 30);box=lay['box'];x,y,w,bh=box
  assert x>=0 and y>=0 and x+w<=W and y+bh<=h,(n,i,'Balloon outside canvas',box,h)
  lines=lay.get('lines',wrap(item['text'],kind,size,w-48));assert ' '.join(lines)==' '.join(item['text'].split()),(n,i,lines)
  geom=None
  if kind=='dialogue':
   assert size*390/800>=14, (n,i,'Dialogue too small for phone')
   assert lay.get('tip') or (item.get('transmitted') and lay.get('radio_source_reviewed')), (n,i,'Speaker tail or reviewed radio source required')
   if not lay.get('shared_balloon'):geom=balloon(d,lay.get('body_box',box),lay.get('tip'),signal=item.get('transmitted',False),attachment_angle=lay.get('attachment_angle'))
   col='#15191c'
  elif kind=='ui':
   if not lay.get('text_only'):d.rounded_rectangle((x*SCALE,y*SCALE,(x+w)*SCALE,(y+bh)*SCALE),radius=10*SCALE,fill='#142b43',outline='#7fd8f2',width=2*SCALE)
   col=lay.get('color','#f0fcff')
  elif kind in ('phone','phone_info','prop'):
   d.rounded_rectangle((x*SCALE,y*SCALE,(x+w)*SCALE,(y+bh)*SCALE),radius=12*SCALE,fill='#e8f0f4' if kind=='phone' else '#fbfcfd',outline='#8d9ba7',width=2*SCALE);col='#152b3a'
  else:col='#17273c'
  bounds=glyphs(d,lines,x+w/2,y+bh/2,kind,size,col,kind=='sfx')
  assert all(g[0]>=x and g[0]+g[2]<=x+w and g[1]>=y and g[1]+g[3]<=y+bh for g in bounds),(n,i,'glyph outside balloon',bounds,box)
  if kind=='dialogue':
   bx,by,bw,bheight=lay.get('body_box',box)
   for gx,gy,gw,gh in bounds:
    yy=max(abs(gy-(by+bheight/2)),abs(gy+gh-(by+bheight/2)))+12
    available=(bw/2-12)*math.sqrt(max(0,1-(yy/(bheight/2))**2))
    assert max(abs(gx-(bx+bw/2)),abs(gx+gw-(bx+bw/2)))<=available,(n,i,'Ellipse padding failure; enlarge balloon',bounds,box)
   mask=Image.new('1',(W,h));md=ImageDraw.Draw(mask);md.polygon(geom,fill=1) if geom else None
   protection=Image.new('1',(W,h));pd=ImageDraw.Draw(protection)
   for px,py,pw,ph in cfg.get('protected_boxes',[]):pd.rectangle((px,py,px+pw,py+ph),fill=1)
   for polygon in cfg.get('protected_polygons',[]):pd.polygon(polygon,fill=1)
   from PIL import ImageChops
   if geom:
    for earlier_index,earlier_mask in balloon_masks:assert ImageChops.logical_and(mask,earlier_mask).getbbox() is None,(n,i,'Distinct balloons/tails overlap',earlier_index)
    balloon_masks.append((i,mask))
   collisions=ImageChops.logical_and(mask,protection).getbbox()
   assert collisions is None,(n,i,'Balloon/tail protected-art collision',collisions)
  if kind not in ('dialogue','sfx') and not lay.get('intentional_surface'):
   for protected in cfg.get('protected_boxes',[]):
    assert all(rect_overlap(check_box,protected)==0 for check_box in (bounds if lay.get('text_only') else [box])),(n,i,'UI overlaps protected artwork',box,protected)
  records.append({'panel':n,'index':i,**item,**lay,'lines':lines,'line_bounds':bounds,'glyph_bounds':LAST_GLYPHS.copy(),'balloon_outline':geom,'render_font':'Anime Ace 2.0 BB' if kind in ('dialogue','sfx') else 'DejaVu Sans','font_size':size,'phone_equivalent_px':round(size*390/800,3)})
 dialogue_records=[r for r in records if r['kind']=='dialogue']
 for before,after in zip(dialogue_records,dialogue_records[1:]):
  a=min(g['bounds_xyxy'][1] for g in before['glyph_bounds'] if g['glyph'].strip());b=min(g['bounds_xyxy'][1] for g in after['glyph_bounds'] if g['glyph'].strip())
  assert b>=a-2,(n,'Actual first-glyph reading order failure',before['index'],after['index'],a,b)
 full=B/'lettered/full';phone=B/'lettered/phone';full.mkdir(exist_ok=True,parents=True);phone.mkdir(exist_ok=True,parents=True)
 im.save(full/f'panel_{n:02}.png',compress_level=2);im.resize((390,round(h*390/W)),Image.Resampling.LANCZOS).save(phone/f'panel_{n:02}.png')
 return im,{'panel':n,'source':str(src.relative_to(B)),'sha256':source_hash,'source_size':list(im0.size),'source_crop_xyxy':crop,'scale_xy':[aw/cropped.width,ah/cropped.height],'translation_xy':[ax-crop[0]*aw/cropped.width,top-crop[1]*ah/cropped.height],'output_size':[W,h],'protected_boxes':cfg.get('protected_boxes',[]),'protected_polygons':cfg.get('protected_polygons',[]),'items':records}

def build(config_path,subset=None):
 global FONT
 cfg=json.loads(Path(config_path).read_text());FONT=FONT or cfg['font_path'];assert FONT and Path(FONT).is_file(),'Required Anime Ace font is unavailable'
 if subset is not None:assert subset and subset<=set(map(int,cfg['panels'])), 'Requested proof panels are missing from active layout'
 if subset is None:assert set(map(int,cfg['panels']))==set(range(1,35)),'Complete final export requires all34 independently accepted panels'
 from fontTools.ttLib import TTFont
 names=' '.join(str(n.toUnicode()).lower().replace(' ','') for n in TTFont(FONT)['name'].names if n.nameID in (1,4,6))
 assert 'animeace' in names,'Required Anime Ace font identity mismatch'
 assert digest(B/'source/script_v1.md')==SCRIPT['script_sha256'],'Script changed; reconcile before rendering';out=[];frames=[]
 for key,c in sorted(cfg['panels'].items(),key=lambda x:int(x[0])):
  n=int(key)
  if subset and n not in subset:continue
  im,record=render_panel(n,c);out.append((n,im));frames.append(record)
 # Assemble sequential panel pairs with scene-sensitive gutters and no cropping.
 pdf=fitz.open();pages=[];r=B/'lettered/reader';r.mkdir(exist_ok=True,parents=True)
 groups={}
 for n,im in out:groups.setdefault((n-1)//2,[]).append((n,im))
 for group,pair in groups.items():
  gutter=100 if pair[0][0] in (7,19,21,25,27) else 64
  top_space=140 if pair[0][0]==1 else 32;bottom_space=90 if pair[-1][0]==34 else 32
  height=sum(im.height for _,im in pair)+gutter*SCALE*(len(pair)-1)+(top_space+bottom_space)*SCALE
  canvas=Image.new('RGB',(W*SCALE,height),'#faf9f7');y=top_space*SCALE;mapping=[]
  cd=ImageDraw.Draw(canvas)
  if pair[0][0]==1:
   glyphs(cd,['My Summons Go First'],400,42,'ui',30)
   glyphs(cd,['Chapter 7: Twenty Thousand Won'],400,92,'ui',23)
  if pair[-1][0]==34:glyphs(cd,['END CHAPTER 7'],400,height/SCALE-bottom_space/2,'ui',24)
  for n,im in pair:canvas.paste(im,(0,y));mapping.append({'panel':n,'offset_y':y/SCALE,'height':im.height/SCALE});y+=im.height+gutter*SCALE
  pn=(pair[0][0]+1)//2;path=r/f'page_{pn:02}.png';canvas.resize((800,height//2),Image.Resampling.LANCZOS).save(path)
  canvas.resize((390,round(height*390/(W*SCALE))),Image.Resampling.LANCZOS).save(r/f'page_{pn:02}_phone.png')
  stream=io.BytesIO();canvas.resize((1200,round(height*1200/(W*SCALE))),Image.Resampling.LANCZOS).save(stream,format='JPEG',quality=85,subsampling=0);pg=pdf.new_page(width=390,height=height*390/(W*SCALE));pg.insert_image(pg.rect,stream=stream.getvalue());pages.append({'page':pn,'panels':mapping,'size':[800,height/2]})
 if out:
  target=B/('lettered/PROVISIONAL_Chapter_7_Preview.pdf' if subset else 'lettered/My_Summons_Go_First_Chapter_7.pdf')
  pdf.save(target,deflate=True)
  assert target.stat().st_size < 25_000_000, 'PDF exceeds strict 25MB delivery limit; recompress and re-review'
  with fitz.open(target) as check:assert all(not page.get_fonts() for page in check), 'PDF must contain no embedded fonts'
 (B/('lettered/provisional_placement_manifest.json' if subset else 'lettered/placement_manifest.json')).write_text(json.dumps({'chapter':7,'script_sha256':SCRIPT['script_sha256'],'font_file_sha256':digest(FONT),'master_width':800,'reader_width':390,'presentation_text':['My Summons Go First','Chapter 7: Twenty Thousand Won','END CHAPTER 7'],'panels':frames,'pages':pages},ensure_ascii=False,indent=2))
 print('Rendered',len(out),'panels;',len(pages),'pages.')
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--config',default=str(B/'source/layout_config.json'));a.add_argument('--panels');args=a.parse_args();build(args.config,set(map(int,args.panels.split(','))) if args.panels else None)
