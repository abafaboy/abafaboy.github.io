from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']};root='raw/B06/Chapter_8_B06'
protected={19:[[0,180,230,430],[420,80,635,320],[935,145,1185,350],[350,340,735,455],[710,310,1030,510],[1070,360,1320,590],[200,485,330,600],[530,755,620,855],[845,440,1110,730],[200,550,495,820],[280,390,1205,800]],21:[[240,90,440,320],[720,85,915,300],[950,245,1230,510],[1320,300,1536,700],[620,305,930,455],[345,385,535,490],[110,420,375,650],[325,565,470,700],[775,665,925,790],[900,590,995,700],[280,430,1450,780]]}
data={19:([430,0],[([0,0,250,120],[210,470]),([200,130,220,120],[320,470]),([440,270,350,150],[530,500])]),21:([450,350],[([0,0,430,170],[175,490]),([300,180,490,260],[590,575]),([0,990,350,160],[110,810]),([430,1160,360,160],[650,910])])}
for n,(extension,items) in data.items():
 top=extension[0];p=c['panels'][str(n)];p.update(source=f'{root}/selected/Chapter_8_P{n:02}_B06_REVIEW.png',crop=[0,0,1536,1024],extension=extension,protection_reviewed=True,status='independent_raw_pass_lettering_proof',protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in protected[n]],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(ps[n]['items'][i]['text'],box[2],box[3],31)}
c['panels']['21']['items']['1']['attachment_angle']=0.5
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
