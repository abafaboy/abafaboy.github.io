from pathlib import Path
import json,os
B=Path(__file__).resolve().parents[1];P=B/'source/layout_config.json';c=json.loads(P.read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());r=c['panels']['14'];r.update(extension=[0,0],native_detail_inset={'crop_xyxy':[290,180,900,900],'x':200,'y':1000,'width':600,'canvas_height':1850,'same_moment':True,'reason':'Parent-approved unchanged full geography above with bordered same-moment cast detail; no new event'},protection_reviewed=True,status='provisional_detail_lettering_review_pending',protected_boxes=[[0,0,800,534]],protected_polygons=[],items={})
scale=600/610
def poly(a):return [[200+(x-290)*scale,1000+(y-180)*scale] for x,y in a]
r['protected_polygons']=[poly(a) for a in [ [(350,520),(405,510),(432,560),(430,585),(415,600),(420,660),(447,735),(438,755),(415,745),(420,815),(442,850),(440,865),(405,867),(382,850),(355,862),(313,870),(310,845),(330,770),(313,730),(298,725),(300,690),(320,600),(350,580)], [(550,205),(620,200),(639,250),(632,280),(680,310),(710,380),(830,427),(830,450),(790,460),(720,430),(685,410),(677,490),(665,615),(690,780),(735,825),(730,846),(680,850),(630,830),(610,750),(590,680),(566,760),(550,840),(500,857),(457,850),(452,835),(481,790),(485,650),(485,570),(465,555),(462,495),(470,400),(480,330),(550,285)]]]
r['protected_polygons'] += [poly(a) for a in [[(290,180),(520,180),(520,490),(290,490)],[(720,210),(850,210),(850,500),(720,500)]]]
placements=[([0,560,380,190],[340,1388]),([400,780,400,200],[550,1090])]
for i,(box,tip) in enumerate(placements):r['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(s['panels'][13]['items'][i]['text'],box[2],box[3],31)}
r['items']['0'].update(attachment_angle=1.6,tail_spread=.025,tail_waypoints=[[180,950],[180,1312],[352,1312],[352,1370]])
r['items']['1'].update(attachment_angle=2.0,tail_waypoints=[[570,1030]])
P.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
