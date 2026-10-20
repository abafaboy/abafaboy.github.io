from pathlib import Path
import os,json
from fit_text import fit
B=Path(__file__).resolve().parents[1];manifest=json.loads((B/'raw/batch02/qa/batch02_manifest.json').read_text());pmap={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']}
specs={29:([0,0],[],[]),30:([220,240],[[350,12,430,190],[20,780,350,180],[495,810,230,135]],[[570,215],[245,755],[600,768]]),31:([250,350],[[16,12,430,210],[485,50,285,160],[15,790,520,265]],[[200,260],[650,270],[206,745]]),33:([170,0],[[130,12,310,145]],[[285,165]]),35:([350,0],[[15,10,330,180],[380,55,400,275]],[[239,345],[650,350]]),36:([175,0],[[355,12,425,150]],[[780,145]])}
out={}
for p in manifest['panels']:
 n=p['panel'];ex,boxes,tips=specs[n];sc=800/p['dimensions'][0];prot=[]
 for x1,y1,x2,y2 in p.get('protected_face_rects_xyxy',[])+p.get('protected_prop_rects_xyxy',[]):prot.append([x1*sc,y1*sc+ex[0],(x2-x1)*sc,(y2-y1)*sc])
 c={'source':'raw/batch02/'+p['native_original'],'crop':p['crop_rect_xyxy'],'extension':ex,'protected_boxes':prot,'items':{},'acceptance_status':'pending_independent_QA'}
 for i,it in enumerate(pmap[n]['items']):
  if n==36 and it['kind']=='phone':c['items'][str(i)]={'native_imagegen_text':True,'verified_text':it['text'],'art_manifest_native_text':p['native_ui_text']};continue
  box=boxes[i];c['items'][str(i)]={'box':box,'lines':fit(it['text'],box[2]-8,box[3]-12,31),'font_size':31,'tip':tips[i]}
 out[str(n)]=c
(B/'source/batch02_pending_layouts.json').write_text(json.dumps(out,indent=2))
print('Prepared pending layouts:',list(out))
