from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]
P=R/'source/manifest_21_40.json'
data=json.loads(P.read_text()) if P.exists() else {'batch':'21-40','coordinate_space':'absolute source pixels; xyxy exclusive crop/box boundaries; mouths xy','panels':[]}
def add(id,src,crop,mouths,neg,protect,beat,qa,review='pending'):
    path=R/'raw/batch_21_40'/src
    panel={'panel_id':id,'source_image':str(path.relative_to(R)),'crop_xyxy':crop,'mouths':mouths,'negative_space_boxes':neg,'protected_boxes':protect,'beat':beat,'qa':qa,'source_size':[1024,1536],'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'source_reviewed':True,'phone_390_reviewed':True,'independent_review_status':review}
    data['panels']=[x for x in data['panels'] if x['panel_id']!=id]+[panel]
add(21,'p021_022_v3.png',[8,8,1017,700],{'TAEO':[416,208],'NIB':[713,371]},[[515,35,985,260]],[[325,58,505,245],[276,440,537,647],[675,294,864,643]],'Taeo puts on shoes; notices already-sheathed blade, asks Nib to keep it sheathed; Nib answers.','Source and 390px reviewed. Nib scale corrected; mouth acting subtle but visible.','pass')
add(22,'p021_022_v3.png',[8,735,1017,1526],{'TAEO':[398,843]},[[550,778,975,1130]],[[317,742,461,883],[409,965,468,1034],[551,1182,697,1445]],'Taeo acknowledges and holds entrance door while Nib checks hall and goes first.','Source and 390px reviewed. Nib head corrected to Taeo mid-thigh; clear autonomous adult gesture.')
add(23,'p023_024_v1.png',[8,8,1017,758],{},[],[[128,14,413,697],[426,336,767,743]],'Taeo holds stairwell door as Nib descends independently near wall.','Source and 390px reviewed. Stair support, door hold, adult scale in perspective, hip props pass.','pass')
add(24,'p023_024_v1.png',[8,778,1017,1528],{},[],[[8,778,302,1528],[295,1140,535,1528]],'Nib emerges from apartment building; broad ordinary city view with Taeo one pace behind.','Source and 390px reviewed. Broad city scope and rear-view scale coherent.','pass')
data['panels'].sort(key=lambda p:p['panel_id'])
P.write_text(json.dumps(data,indent=2)+'\n')
