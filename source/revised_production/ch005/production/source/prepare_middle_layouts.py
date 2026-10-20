from pathlib import Path
import json
from fit_text import fit
B=Path(__file__).resolve().parents[1];sp={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};out={}
for batch,mfile in [('middle_a','panel_manifest.json'),('middle_b','batch_B_manifest.json'),('middle_map','route_map_panel20_manifest.json')]:
 for p in json.loads((B/'raw'/batch/mfile).read_text())['panels']:
  n=p['panel'];r=p['crop_xyxy'];sc=800/(r[2]-r[0]);ah=round((r[3]-r[1])*sc)
  if n==16:ex=[0,0];boxes=[];tips=[]
  if n==17:ex=[270,0];boxes=[[15,10,430,210],[455,55,330,205]];tips=[[305,265],[485,270]]
  if n==18:ex=[270,210];end=270+ah;boxes=[[15,10,480,240],[550,65,230,135],[45,end+40,250,150]];tips=[[165,265],[650,230],[160,end+12]]
  if n==19:ex=[270,195];end=270+ah;boxes=[[320,12,460,230],[80,end+40,230,140]];tips=[[500,265],[220,end+10]]
  if n==20:ex=[280,370];end=280+ah;boxes=[[30,10,680,240],[15,end+35,350,180],[390,end+70,395,270]];tips=[None,None,None]
  if n==21:ex=[280,0];boxes=[[10,10,500,240],[540,85,230,130]];tips=[[320,275],[615,270]]
  if n==22:ex=[280,210];end=280+ah;boxes=[[350,10,430,240],[80,end+45,300,145]];tips=[[620,275],[215,end+12]]
  prot=[]
  for kind,bs in p['protection_coordinates'].items():
   if kind=='mouths_xyxy':continue
   for x1,y1,x2,y2 in bs:prot.append([x1*sc,y1*sc+ex[0],(x2-x1)*sc,(y2-y1)*sc])
  c={'source':'raw/'+batch+'/'+p['original'],'crop':r,'extension':ex,'protected_boxes':prot,'items':{},'acceptance_status':'pending_independent_QA'}
  for i,it in enumerate(sp[n]['items']):
   box=boxes[i];l={'box':box,'lines':fit(it['text'],box[2]-8,box[3]-12,31),'font_size':31}
   if tips[i]:l['tip']=tips[i]
   else:l['off_panel']=True
   c['items'][str(i)]=l
  out[str(n)]=c
(B/'source/middle_pending_layouts.json').write_text(json.dumps(out,indent=2))
