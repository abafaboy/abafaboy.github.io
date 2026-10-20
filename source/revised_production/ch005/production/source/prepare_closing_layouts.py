from pathlib import Path
import json
from fit_text import fit
B=Path(__file__).resolve().parents[1];sp={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};out={}
for p in json.loads((B/'raw/closing/panel_manifest.json').read_text())['panels']:
 n=p['panel']
 if n not in (27,28,36,37,38):continue
 r=p['crop_rect_xyxy'];sc=800/(r[2]-r[0]);ah=round((r[3]-r[1])*sc)
 if n==27:ex=[250,335];end=250+ah;boxes=[[350,10,430,210],[15,end+40,430,250],[460,end+85,325,220]];tips=[[480,245],[200,end+12],[570,end+20]]
 if n==28:ex=[300,210];end=300+ah;boxes=[[15,10,620,260],[500,end+40,280,150]];tips=[[200,290],[600,end+12]]
 if n==36:ex=[175,0];boxes=[[355,12,425,150]];tips=[[780,145]]
 if n==37:ex=[250,210];end=250+ah;boxes=[[350,10,430,210],[20,end+40,250,140]];tips=[[470,245],[220,end+12]]
 if n==38:ex=[0,0];boxes=[];tips=[]
 prot=[]
 for x1,y1,x2,y2 in p.get('protected_face_rects_xyxy',[])+p.get('protected_prop_rects_xyxy',[]):prot.append([x1*sc,y1*sc+ex[0],(x2-x1)*sc,(y2-y1)*sc])
 c={'source':'raw/closing/'+p['native_original'],'crop':r,'extension':ex,'protected_boxes':prot,'items':{},'acceptance_status':'pending_independent_QA'}
 for i,it in enumerate(sp[n]['items']):
  if n==36 and it['kind']=='phone':c['items'][str(i)]={'native_imagegen_text':True,'verified_text':it['text'],'art_manifest_native_text':p['native_ui_text']};continue
  box=boxes[i];c['items'][str(i)]={'box':box,'lines':fit(it['text'],box[2]-8,box[3]-12,31),'font_size':31,'tip':tips[i]}
 out[str(n)]=c
(B/'source/closing_pending_layouts.json').write_text(json.dumps(out,indent=2))
