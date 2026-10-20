from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']};root='raw/B01_complete/Chapter_8_B01';pr=json.loads((B/root/'protected_regions.json').read_text())
data={1:([70,0],[([20,5,200,55],None)]),2:([0,0],[([15,300,300,150],[195,670]),([540,440,200,100],[525,230])]),3:([150,200],[([450,0,330,120],[500,180]),([0,350,330,150],[325,340]),([440,650,350,190],[640,380])]),4:([200,0],[([250,0,330,130],[300,195]),([600,90,180,100],[700,260]),([570,560,220,170],[700,390])])}
for n,(extension,items) in data.items():
 top=extension[0];p=c['panels'][str(n)];crop=pr[f'P{n:02}']['selected_crop'];scale=800/crop[2];p.update(source=f'{root}/selected/P{n:02}.png',crop=crop,extension=extension,protection_reviewed=True,status='independent_raw_pass_lettering_proof',protected_boxes=[[x*scale,y*scale+top,(xx-x)*scale,(yy-y)*scale] for k,(x,y,xx,yy) in pr[f'P{n:02}']['protected_regions'].items() if k!='common_ground_scale'],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):
  item={'box':box,'font_size':31,'lines':fit(ps[n]['items'][i]['text'],box[2],box[3],31) if n!=1 else ['Sunday.']}
  if tip:item['tip']=tip
  p['items'][str(i)]=item
c['panels']['2']['items']['1']['attachment_angle']=-2.3
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
