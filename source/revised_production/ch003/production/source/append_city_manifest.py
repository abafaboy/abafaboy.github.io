from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parents[1]; P=R/'source/manifest_21_40.json'
data=json.loads(P.read_text())
def add(id,src,crop,mouths,neg,protect,beat,qa,review='pass'):
 path=R/'raw/batch_21_40'/src
 panel={'panel_id':id,'source_image':str(path.relative_to(R)),'crop_xyxy':crop,'mouths':mouths,'negative_space_boxes':neg,'protected_boxes':protect,'beat':beat,'qa':qa,'source_size':[1024,1536],'source_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'source_reviewed':True,'phone_390_reviewed':True,'independent_review_status':review}
 data['panels']=[x for x in data['panels'] if x['panel_id']!=id]+[panel]
add(25,'p025_026_v3.png',[8,8,1017,725],{},[],[[750,382,918,688],[220,266,439,472]],'Passing scooter and near pedestrian cause Nib to step back into entry recess without drawing weapon.','Source and390 reviewed. Mature reactive staging, sheath and pouch consistent, height corrected.')
add(26,'p025_026_v3.png',[8,744,1017,1528],{'TAEO':[397,864]},[[570,770,982,1085]],[[325,752,478,918],[428,1060,552,1140],[579,1153,744,1527]],'Taeo offers to wait; Nib looks up at unfamiliar buildings.','Source and390 reviewed. Upward architectural gaze corrected; Taeo mouth speaking and clear relaxed hand.')
add(31,'p031_032_v1.png',[8,8,1017,718],{},[],[[242,58,533,689],[400,410,530,674]],'Modest office arrival; Taeo checks address and holds entrance for Nib.','Source and390 reviewed. Phone front/back, independent arrival, small scale acceptable.')
add(32,'p031_032_v1.png',[8,742,1017,1528],{'TAEO':[436,840],'RECEPTIONIST':[740,924]},[[20,765,340,880],[602,759,976,832],[525,1150,981,1440]],[[378,751,495,877],[478,931,586,982],[674,840,974,1050],[160,1143,272,1443]],'Taeo presents ID and introduces Nib; receptionist records note and indicates waiting area.','Source and390 reviewed. Natural five-finger hand support, distinct receptionist, Nib below counter.')
add(33,'p033_034_v1.png',[8,4,1017,765],{},[],[[222,170,372,338],[398,345,573,710],[820,8,1010,221]],'Taeo sits bench end, Nib chooses open space with view of both doors; Taeo sees TV.','Source and390 reviewed. Coherent waiting-room geometry, small adult proportions, TV establishes next scene.')
add(34,'p033_034_v1.png',[8,796,1017,1528],{'SEORYUN':[520,1097]},[[635,850,966,1135],[50,860,318,1005]],[[273,847,649,1197],[663,1150,945,1453],[46,1374,982,1427]],'TV interview shows Han Seoryun by rescue vehicle with crew moving equipment; exact hunter lower-third.','Source and390 reviewed. Han Seoryun matches model, speaking mouth, exact readable lower-third and ordinary crew action.')
data['batch']='21-38 (panels39-40 delegated separately)';data['panels'].sort(key=lambda p:p['panel_id']);P.write_text(json.dumps(data,indent=2)+'\n')
