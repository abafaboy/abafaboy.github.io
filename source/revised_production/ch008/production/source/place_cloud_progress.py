from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']};root='raw/B09/Chapter_8_B09'
protected={30:[[30,0,445,350],[920,0,1430,400],[300,115,1230,750],[270,590,655,815],[790,820,1120,1015],[410,610,1010,990]],31:[[30,0,445,350],[920,0,1430,400],[300,115,1230,750],[250,335,385,420],[300,620,510,755],[790,820,1120,1015],[410,610,1010,990],[820,340,1120,490]],32:[[45,125,355,400],[955,300,1240,580],[1240,125,1375,235],[1090,200,1300,265],[1190,225,1410,410],[285,390,475,635],[910,715,980,815],[290,175,1040,790],[360,615,815,990]]}
data={30:([310,0],[([10,0,260,120],[150,300]),([500,35,290,130],[650,300]),([230,160,340,140],[245,360])]),31:([340,0],[([330,0,140,70],None),([500,75,280,115],[650,335]),([0,210,290,120],[160,335])]),32:([150,0],[([300,0,350,150],[640,240])])}
for n,(extension,items) in data.items():
 top=extension[0];p=c['panels'][str(n)];p.update(source=f'{root}/selected/P{n:02}.png',crop=[0,0,1536,1024],extension=extension,protection_reviewed=True,status='independent_raw_pass_lettering_proof',protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in protected[n]],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):
  it=ps[n]['items'][i];lay={'box':box,'font_size':31,'lines':fit(it['text'],box[2],box[3],31) if it['kind']=='dialogue' else [it['text']]}
  if tip:lay['tip']=tip
  p['items'][str(i)]=lay
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
