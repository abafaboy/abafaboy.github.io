from pathlib import Path
import os,json
from fit_text import fit
B=Path(__file__).resolve().parents[1];m=json.loads((B/'raw/opening/batch_manifest.json').read_text());ps={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']}
# Coordinates in800px assembly units. Unlettered art remains intact.
spec={3:([430,0],[[440,10,340,170],[270,230,450,170]],[[660,205],[590,425]]),4:([300,0],[[10,12,440,240],[475,75,300,180]],[[300,285],[570,290]]),5:([200,180],[[400,12,360,170],[70,810,240,130]],[[470,195],[214,795]]),8:([200,0],[[335,10,440,175]],[[590,195]]),9:([260,0],[[15,10,345,210],[400,55,380,195]],[[160,255],[600,260]]),10:([210,0],[[340,12,440,185]],[[600,205]]),11:([235,0],[[20,10,270,100],[380,60,400,160]],[None,[550,235]]),13:([250,0],[[320,12,460,220]],[[610,245]])}
out={}
for p in m['panels']:
 n=p['panel_id'];crop=p['crop_xyxy'];sc=800/(crop[2]-crop[0]);ex,boxes,tips=spec.get(n,([0,0],[],[]));prot=[[(x1-crop[0])*sc,(y1-crop[1])*sc+ex[0],(x2-x1)*sc,(y2-y1)*sc] for x1,y1,x2,y2 in p['protected_boxes']]
 c={'source':'raw/opening/'+p['source_image'],'crop':crop,'extension':ex,'protected_boxes':prot,'items':{},'acceptance_status':'pending_independent_QA'}
 for i,it in enumerate(ps[n]['items']):
  box=boxes[i];c['items'][str(i)]={'box':box,'lines':fit(it['text'],box[2]-8,box[3]-12,31) if it['kind']=='dialogue' else [it['text']],'font_size':31}
  if tips[i]:c['items'][str(i)]['tip']=tips[i]
 out[str(n)]=c
(B/'source/opening_pending_layouts.json').write_text(json.dumps(out,indent=2))
