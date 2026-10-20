from pathlib import Path
import json
from fit_text import fit
B=Path(__file__).resolve().parents[1];ps={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};out={}
for p in json.loads((B/'raw/middle_final_selected/panel_manifest.json').read_text())['panels']:
 n=p['panel']
 if n not in (14,15,23,24,25,26):continue
 r=p['crop_xyxy'];sc=800/(r[2]-r[0]);ah=round((r[3]-r[1])*sc)
 if n==14:ex=[170,0];boxes=[[20,12,330,140]];tips=[[5,145]]
 if n==15:ex=[170,0];boxes=[[465,12,310,140]];tips=[[785,145]]
 if n==23:ex=[280,0];boxes=[[15,12,650,240]];tips=[[310,275]]
 if n==24:ex=[220,245];end=220+ah;boxes=[[470,10,310,170],[20,end+35,450,190]];tips=[[600,215],[290,end+10]]
 if n==25:ex=[170,0];boxes=[[490,12,280,140]];tips=[[595,165]]
 if n==26:ex=[230,0];boxes=[[10,10,400,200],[500,60,270,140]];tips=[None,[650,225]]
 prot=[]
 for kind,bs in p['protection_coordinates'].items():
  if kind=='mouths_xyxy':continue
  for x1,y1,x2,y2 in bs:prot.append([x1*sc,y1*sc+ex[0],(x2-x1)*sc,(y2-y1)*sc])
 c={'source':'raw/middle_final_originals/'+p['original'],'crop':r,'extension':ex,'protected_boxes':prot,'items':{},'acceptance_status':'pending_independent_QA'}
 for i,it in enumerate(ps[n]['items']):
  box=boxes[i];c['items'][str(i)]={'box':box,'lines':fit(it['text'],box[2]-8,box[3]-12,31),'font_size':31}
  if tips[i]:c['items'][str(i)]['tip']=tips[i]
  else:c['items'][str(i)]['off_panel']=True
 out[str(n)]=c
(B/'source/final_middle_pending_layouts.json').write_text(json.dumps(out,indent=2))
