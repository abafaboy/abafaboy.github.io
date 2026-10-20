from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']}
# Protected native faces, hands, equipment and story props. Coordinates are rectangles xyxy.
protected={
5:[[290,75,455,240],[875,55,1070,255],[1220,50,1410,245],[190,410,260,535],[385,415,460,550],[390,490,475,715],[825,350,980,440],[1050,440,1135,585],[1240,340,1450,550],[455,500,640,850],[190,740,435,870]],
6:[[470,10,680,215],[1125,35,1330,250],[205,435,285,585],[595,485,660,625],[550,570,710,815],[1110,440,1175,570],[1290,455,1380,595],[725,480,895,900],[210,745,550,970]],
7:[[475,40,630,225],[1160,205,1450,480],[375,440,440,580],[630,430,690,580],[595,550,725,780],[220,515,360,860],[1060,695,1410,810],[1440,730,1536,835],[15,710,165,810],[425,835,640,950]]}
placements={
5:([0,0],[([300,70,150,100],[337,280]),([345,312,445,200],[630,110])]),
6:([300,0],[([15,10,460,230],[365,380]),([470,90,320,190],[575,395])]),
7:([150,0],[([380,0,410,100],[600,253]),([365,105,235,150],[335,245]),([365,275,230,200],[600,335])])}
for n,(extension,items) in placements.items():
 top=extension[0];p=c['panels'][str(n)];p.update(source=f'raw/B02_geography_repair/Chapter_8_B02_Door_Repair/selected/Chapter_8_P{n:02}_REVIEW.png',crop=[0,0,1536,1024],extension=extension,protection_reviewed=True,status='independent_raw_pass_lettering_proof',protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in protected[n]],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(ps[n]['items'][i]['text'],box[2],box[3],31)}
c['panels']['6']['items']['0']['attachment_angle']=0.9
c['panels']['6']['items']['1']['attachment_angle']=2.2
c['panels']['7']['items']['0']['attachment_angle']=0.8
c['panels']['5']['items']['1']['attachment_angle']=-1.32
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
