"""Place accepted P9/P10 exact text; run renderer only after sequence gate clears."""
from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());ps={p['panel']:p for p in s['panels']}
root='raw/B03_repair/Chapter_8_B03';pr=json.loads((B/root/'protected_regions.json').read_text())
data={8:('08_Settling',[0,220],[([315,165,170,150],[505,240]),([170,325,320,180],[195,135]),([345,555,445,180],[505,285])]),9:('09_Puzzle_Anchor',[200,0],[([0,0,340,130],[170,210]),([400,75,200,100],[410,205]),([20,380,190,100],[150,355])]),10:('10_Home_Table_Anchor',[0,0],[([490,5,230,110],[475,130])])}
for n,(name,extension,items) in data.items():
 top=extension[0];p=c['panels'][str(n)];p.update(source=f'{root}/selected/Chapter_8_P{name}_REVIEW.png',crop=[0,0,1536,1024],extension=extension,protection_reviewed=True,status='independent_raw_pass_sequence_hold',protected_boxes=[[x*800/1536,y*800/1536+top,(xx-x)*800/1536,(yy-y)*800/1536] for x,y,xx,yy in pr[f'P{n:02}']['protected_from_lettering'].values()],protected_polygons=[],items={})
 for i,(box,tip) in enumerate(items):p['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(ps[n]['items'][i]['text'],box[2],box[3],31)}
c['panels']['8']['items']['1']['attachment_angle']=-2.8
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2)+'\n')
