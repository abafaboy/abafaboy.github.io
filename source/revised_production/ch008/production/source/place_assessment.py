from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']};root='raw/B05_repair/Chapter_8_B05'
protected=json.loads((B/root/'protected_regions.json').read_text())
data={16:([350,0],[([400,0,390,150],[590,395]),([10,180,390,160],[260,345])]),17:([510,0],[([10,0,410,160],[50,550]),([220,180,570,320],[580,615])])}
for n,(extension,items) in data.items():
 top=extension[0];p=c['panels'][str(n)];regions=list(protected[f'P{n}'].values());p.update(source=f'{root}/selected/Chapter_8_P{n:02}_REVIEW.png',crop=[0,0,1536,1024],extension=extension,protection_reviewed=True,status='independent_raw_pass_lettering_proof',protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in regions],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(ps[n]['items'][i]['text'],box[2],box[3],31)}
c['panels']['17']['items']['0']['attachment_angle']=2.2
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
