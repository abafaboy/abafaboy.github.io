from pathlib import Path
import json,hashlib,os
B=Path(__file__).resolve().parents[1];c=json.loads((B/'source/layout_config.json').read_text());os.environ['ANIME_ACE_FONT']=c['font_path'];from fit_text import fit
s={p['panel']:p for p in json.loads((B/'source/lettering_script.json').read_text())['panels']};rp=B/'qa/independent_raw_review.json';r=json.loads(rp.read_text())
def add(n,src,sha,crop,ext,boxes,evidence,placements=[]):
 assert hashlib.sha256((B/src).read_bytes()).hexdigest()==sha
 p=dict(source=src,source_sha256=sha,crop=crop,extension=ext,protected_boxes=boxes,protected_polygons=[],protection_reviewed=True,items={})
 for i,(box,tip,angle) in enumerate(placements):p['items'][str(i)]={'box':box,'tip':tip,'attachment_angle':angle,'font_size':31,'lines':fit(s[n]['items'][i]['text'],box[2]-8,box[3]-12,31)}
 c['panels'][str(n)]=p;rec=dict(panels=[n],sha256=sha,crop_xyxy=crop,verdict='pass',evidence='qa/'+evidence)
 if rec not in r['reviews']:r['reviews'].append(rec)
 return p
root='repairs/Chapter6_Panels22_27_CartRadio_Repair_PENDING_QA/candidates/'
ev='independent_p22_p27_p41_v4_review.md'
add(22,root+'p022_repair_v1.png','6fe6622a2f31c12e19228d34d7672c933ac7a81083aadee3ffae223bfaf59081',[0,0,1214,1295],[240,0],[[173,271,147,156],[493,306,98,129],[66,440,72,103],[293,551,54,72],[613,506,76,67],[395,586,347,343],[555,591,67,125]],ev,[([0,0,600,220],[165,350],2.3)])
add(27,root+'p027_repair_v2.png','4c7edcbc7de74d6353b350cbe6262dcfb46551653b91217ea771c66dcb5834fd',[0,0,1536,1024],[0,0],[[0,0,800,533]],ev)
p=add(41,'repairs/updated_v1/My_Summons_Go_First_CH6_Panel41_Source/My_Summons_Go_First_CH6_Panel41_Source/art/originals/P41_v4.png','c5d5b9df46512869b20e4783365a2c4be021dce5cad932cad08930001bc11da6',[0,0,1024,1536],[0,0],[[0,0,800,1200]],ev)
p['items']['0']={'native_imagegen_text':True,'verified_text':s[41]['items'][0]['text'],'native_visual_qa':'pass','evidence':'qa/'+ev}
p['art_provenance']='Native imagegen v4 repair; lower region visually re-reviewed, not byte-unchanged from v3. Phone text retained as native image pixels.'
root='repairs/Chapter6_P23_P28_Cart_Handle_Repairs/originals/';ev='independent_p23_p28_handle_repairs_review.md'
add(23,root+'p023_handle_repair_v3.png','5f1bec70cfdcf321123e5fe8bd4fa37fa544b3da7cbb3124297a3edcc538daf2',[150,150,1500,950],[0,0],[[0,0,800,474]],ev)
# Both radio transmissions stay in exterior gutter. Nib's reply originates from Taeo's handheld radio.
add(28,root+'p028_handle_repair_v1.png','918232b72e3a5b4566ac21098b524a1018c6e97bd5c5ea6c9d77ea77ada84fb9',[0,0,1536,1024],[360,0],[[185,391,81,76],[198,446,63,73],[278,566,48,47],[208,571,222,274],[229,430,37,69],[474,406,243,306]],ev,[([0,0,480,220],[180,424],2.3),([470,140,330,200],[271,470],2.4)])
(B/'source/layout_config.json').write_text(json.dumps(c,indent=2));rp.write_text(json.dumps(r,indent=2))
