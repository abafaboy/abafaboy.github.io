from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
n=33;p=c['panels'][str(n)];p.update(source='raw/B09_repair/Chapter_8_B09/selected/P33.png',crop=[0,0,1536,1024],extension=[150,0],protection_reviewed=True,status='independent_raw_gate_required',protected_boxes=[[0,150,800,800*1024/1536]],protected_polygons=[],items={'0':{'box':[10,0,350,140],'tip':[110,148],'font_size':31,'lines':fit('Your bit.',350,140,31)}})
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
