from pathlib import Path
import json,os,hashlib
B=Path(__file__).resolve().parents[1];P=B/'source/layout_config.json';c=json.loads(P.read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
s=json.loads((B/'source/lettering_script.json').read_text());root=B/'raw/B03_repaired/Chapter9_B03_Source_Package_R2';m={r['unit']:r for r in json.loads((root/'provenance/selected_manifest.json').read_text())}
for n in [9,10,11,12]:
 k=f'U{n:02}' if n!=12 else 'U12a';v=m[k];r=c['panels'][str(n)];r.update(source=str((root/v['source_variant']).relative_to(B)),source_sha256=v['sha256'],crop=[0,0,*v['dimensions']],art_width=800,extension=[200 if n in [9,10] else 0,0],protection_reviewed=True,items={},protected_boxes=[],protected_polygons=[],status='repaired_raw_review_gate_enforced_lettering_pending')
 if n==9:r['native_sequence_gutter']={'after_native_y':742,'height_master':700,'reason':'Blank chronological separation between exact native frames; pocketing inset retained unchanged.'}
 if n==11:r['native_sequence_gutter']={'after_native_y':750,'height_master':400,'reason':'Blank chronological separation before exact release/response frame.'}
 if n==12:r['native_following_frames']=[{'source':str((root/m['U12b']['source_variant']).relative_to(B)),'crop':[0,0,1536,1024],'gap_master':220}]
 placements={9:[([0,0,420,160],[315,285]),([0,800,500,220],[445,1820]),([540,1030,260,440],[565,1560])],10:[([0,0,400,160],[297,462])],11:[([200,610,400,200],[275,1180]),([0,850,250,110],[165,1220])],12:[([0,550,380,150],[225,833])]}[n]
 for i,(box,tip) in enumerate(placements):r['items'][str(i)]={'box':box,'tip':tip,'font_size':31,'lines':fit(s['panels'][n-1]['items'][i]['text'],box[2],box[3],31)}
 if n==9:
  regions=[[120,20,310,540],[0,240,140,420],[350,300,460,540],[515,20,735,565],[340,70,425,160],[700,265,800,330],[305,600,520,780],[0,875,80,1070],[480,820,575,885],[570,590,700,730],[560,730,800,1200],[0,590,285,1200],[345,885,440,950],[325,950,465,1175]]
  def sy(y):return y+200+(700 if y>=742*800/1024 else 0)
  r['protected_boxes']=[[x,sy(y),xx-x,yy-y] for x,y,xx,yy in regions]
  r['items']['0'].update(attachment_angle=.5)
  r['items']['1'].update(attachment_angle=.3,tail_spread=.025,tail_waypoints=[[530,1050],[530,1685],[455,1710],[455,1800]])
  r['items']['2'].update(attachment_angle=2.8)
 if n==10:
  regions=[[0,35,180,310],[180,5,325,220],[175,195,285,290],[110,280,305,480],[305,315,675,480],[335,60,480,200],[500,185,700,240],[600,100,800,200],[380,0,475,70]]
  r['protected_boxes']=[[x,y+200,xx-x,yy-y] for x,y,xx,yy in regions];r['items']['0'].update(attachment_angle=.5,tail_spread=.025,tail_waypoints=[[330,190],[330,430]])
 if n==11:
  r['protected_boxes']=[[0,0,800,585],[420,1000,130,140],[410,1100,390,175],[400,1360,360,210],[50,1170,110,320],[280,1120,65,75],[165,1225,240,240]]
  r['items']['0'].update(attachment_angle=1.7,tail_waypoints=[[260,1060],[260,1150]])
  r['items']['1'].update(attachment_angle=1.0,tail_waypoints=[[180,1090],[180,1190]])
 if n==12:
  r['protected_boxes']=[[0,0,800,533],[25,958,65,165],[115,790,105,330],[225,908,410,330],[335,815,145,100],[510,938,190,55],[600,850,200,110]]
  r['items']['0'].update(attachment_angle=.5,tail_waypoints=[[255,745],[250,805]])
P.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
