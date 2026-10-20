from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];P=B/'source/layout_config.json';c=json.loads(P.read_text());os.environ['ANIME_ACE_FONT']=c['font_path']
from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());r=c['panels']['6'];r.update(extension=[0,0],protection_reviewed=True,items={},status='raw_pass_inset_provisional_lettering',native_detail_inset={'crop_xyxy':[60,420,400,700],'x':100,'y':1100,'width':600,'canvas_height':1850,'same_moment':True,'reason':'Unchanged geography above, enlarged native cast detail for same-unit exact dialogue; no new event'})
# Entire wide view is protected. Inset features are mapped directly from native coordinates.
r['protected_boxes']=[[0,0,800,533]]
regions=[[100,435,165,495],[80,500,180,680],[180,535,240,665],[295,433,333,475],[335,445,390,475],[270,485,335,690]]
for x,y,xx,yy in regions:r['protected_boxes'].append([100+(x-60)*600/340,1100+(y-420)*600/340,(xx-x)*600/340,(yy-y)*600/340])
for i,(box,tip) in enumerate([([400,570,400,260],[590,1138]),([0,850,400,190],[290,1190]),([400,1630,400,210],[590,1205])]):
 text=s['panels'][5]['items'][i]['text'];r['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(text,box[2],box[3],31)}
r['items']['1']['attachment_angle']=0.7
r['items']['2']['attachment_angle']=-1.2
P.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
