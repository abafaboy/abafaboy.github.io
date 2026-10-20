from pathlib import Path
import os,json
B=Path(__file__).resolve().parents[1];p=B/'source/layout_config.json';c=json.loads(p.read_text());s=json.loads((B/'source/lettering_script.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
rows={r['panel']:r for r in json.loads((B/'qa/B03_intake.json').read_text())}
def place(n,top,bottom,protect,placements):
 r=rows[n];cfg=c['panels'][str(n)];cfg.update(source=str(Path(r['source']).relative_to(B)),crop=r['crop_xyxy'],extension=[top,bottom],protected_boxes=[[x*800/390,y*800/390+top,w*800/390,h*800/390] for x,y,w,h in protect],protection_reviewed=True,status='layout_pending_raw_pass')
 for i,(box,tip) in enumerate(placements):cfg['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(s['panels'][n-1]['items'][i]['text'],box[2],box[3],31)}
place(7,200,0,[(86,55,58,82),(284,45,66,85),(20,218,51,88),(119,168,77,41),(194,306,65,171)], [([10,10,500,170],[230,300])])
place(8,300,210,[(93,0,91,90),(261,59,92,80),(74,112,192,68),(95,181,83,66),(266,169,109,89),(354,68,32,74)], [([10,10,430,180],[200,280]),([460,50,320,180],[650,410]),([20,870,260,120],[175,420])])
c['panels']['8']['items']['2']['attachment_angle']=4
place(9,250,0,[(77,50,163,111),(221,0,165,129),(60,226,145,84),(56,280,99,89)], [([20,10,650,210],[300,330])])
p.write_text(json.dumps(c,indent=2)+'\n')
