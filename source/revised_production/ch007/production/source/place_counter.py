from pathlib import Path
import os,json
B=Path(__file__).resolve().parents[1];p=B/'source/layout_config.json';c=json.loads(p.read_text());s=json.loads((B/'source/lettering_script.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
rows={r['panel']:r for r in json.loads((B/'qa/B02_B04_B07_B08_intake.json').read_text())}
def place(n,top,bottom,protect,placements):
 r=rows[n];cfg=c['panels'][str(n)];cfg.update(source=str(Path(r['source']).relative_to(B)),crop=r['crop_xyxy'],extension=[top,bottom],protected_boxes=[[x*800/390,y*800/390+top,w*800/390,h*800/390] for x,y,w,h in protect],protection_reviewed=True,status='raw_pass_lettering_proof_pending')
 for i,(box,tip) in enumerate(placements):cfg['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(s['panels'][n-1]['items'][i]['text'],box[2],box[3],31)}
place(21,200,0,[(106,0,45,45),(63,92,83,55),(146,135,89,104),(267,21,46,45),(260,90,82,23),(229,144,86,49)], [([10,10,400,170],[346,465]),([430,30,350,170],[600,235])])
place(23,300,0,[(115,28,100,89),(188,0,75,92),(273,0,116,87),(279,112,100,106),(147,160,64,66),(73,113,39,102)], [([10,10,430,170],[0,225]),([480,70,270,120],[350,340])])
place(22,350,270,[(95,30,100,80),(86,101,193,50),(250,60,113,57),(88,140,34,83),(142,160,40,54),(52,0,44,75)], [([430,10,350,110],[400,390]),([10,140,400,160],[0,345]),([20,930,450,150],[170,550])])
c['panels']['22']['items']['2']['attachment_angle']=4
c['panels']['21']['items']['0']['attachment_angle']=0.6
c['panels']['23']['items']['1']['attachment_angle']=2.7
p.write_text(json.dumps(c,indent=2)+'\n')
