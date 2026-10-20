from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
regions=[[425,20,575,225],[570,270,690,380],[780,0,930,340],[435,315,600,465],[535,465,655,530],[425,530,555,715],[980,390,1180,575],[880,685,1040,790],[1240,380,1445,685],[510,510,1040,740],[560,730,850,890],[175,680,485,885]]
p=c['panels']['23'];p.update(source='raw/P23_composite_repair/Chapter_8_B07_P23_Composite_02/candidates/Chapter_8_P23_SOCKET_COMPOSITE_REVIEW_v1.png',crop=[0,0,1536,1024],extension=[180,0],protection_reviewed=True,status='independent_raw_pass_lettering_proof',protected_boxes=[[x*800/1536,y*800/1536+180,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in regions],protected_polygons=[],items={'0':{'box':[10,0,420,170],'tip':[220,370],'font_size':31,'attachment_angle':2.0,'lines':fit("This bit's yours.",420,170,31)}})
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
