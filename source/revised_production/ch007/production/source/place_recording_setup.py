from pathlib import Path
import os,json
B=Path(__file__).resolve().parents[1];p=B/'source/layout_config.json';c=json.loads(p.read_text());s=json.loads((B/'source/lettering_script.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
rows={r['panel']:r for r in json.loads((B/'qa/B02_B04_B07_B08_intake.json').read_text())}
def place(n,top,bottom,protect,placements):
 r=rows[n];cfg=c['panels'][str(n)];cfg.update(source=str(Path(r['source']).relative_to(B)),crop=r['crop_xyxy'],extension=[top,bottom],protected_boxes=[[x*800/390,y*800/390+top,w*800/390,h*800/390] for x,y,w,h in protect],protection_reviewed=True,status='blocked_native_repair_pending')
 for i,(box,tip) in enumerate(placements):cfg['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(s['panels'][n-1]['items'][i]['text'],box[2],box[3],31)}
place(10,300,310,[(137,7,42,51),(271,3,49,52),(188,149,29,34),(20,46,100,32),(167,116,23,44),(271,115,84,43),(192,178,29,65)], [([10,10,480,220],[320,285]),([390,250,400,130],[410,590]),([10,900,470,210],[185,510])])
c['panels']['10']['items']['2']['attachment_angle']=4
place(11,400,0,[(146,8,98,101),(294,78,82,71),(249,150,135,80),(73,158,115,103),(269,221,115,136)], [([430,10,350,180],[650,545]),([10,210,400,180],[350,390])])
place(12,220,0,[(252,12,74,99),(251,110,112,75),(58,188,80,91),(187,305,61,80),(174,381,90,130),(24,330,98,112)], [([290,10,500,200],[630,215]),([10,270,370,220],[430,830])])
p.write_text(json.dumps(c,indent=2)+'\n')
