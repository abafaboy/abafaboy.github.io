from pathlib import Path
import os,json
B=Path(__file__).resolve().parents[1];p=B/'source/layout_config.json';c=json.loads(p.read_text());s=json.loads((B/'source/lettering_script.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
rows={r['panel']:r for r in json.loads((B/'qa/B02_B04_B07_B08_intake.json').read_text())}
def place(n,top,bottom,protect,placements):
 r=rows[n];cfg=c['panels'][str(n)];cfg.update(source=str(Path(r['source']).relative_to(B)),crop=r['crop_xyxy'],extension=[top,bottom],protected_boxes=[[x*800/390,y*800/390+top,w*800/390,h*800/390] for x,y,w,h in protect],protection_reviewed=True,status='layout_pending_exact_raw_pass')
 for i,(box,tip) in enumerate(placements):
  cfg['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(s['panels'][n-1]['items'][i]['text'],box[2],box[3],31)}
  if s['panels'][n-1]['items'][i].get('transmitted'):cfg['items'][str(i)]['radio_source_reviewed']=True
place(26,250,0,[(55,60,75,65),(238,18,80,90),(28,116,144,69),(195,133,68,68),(245,200,74,40),(200,130,47,26)], [([10,10,350,140],[200,360]),([390,40,400,190],[665,290])])
place(27,260,0,[(52,60,91,67),(244,15,91,91),(235,59,44,84),(68,111,98,51),(201,131,62,62)], [([10,10,250,100],None),([290,50,500,190],[620,280]),([10,180,270,120],None)])
place(25,400,210,[(59,45,62,63),(230,16,68,67),(66,91,73,44),(183,111,66,50),(238,150,43,30),(207,102,36,19)], [([10,10,700,210],[500,425]),([10,275,400,160],[200,480]),([430,960,350,150],[710,590])])
p.write_text(json.dumps(c,indent=2)+'\n')
