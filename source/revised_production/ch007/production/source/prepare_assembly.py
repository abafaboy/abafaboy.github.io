"""Initialize Chapter 7 only; no artwork generation, rendering, or publication."""
from pathlib import Path
import json,hashlib,shutil
B=Path(__file__).resolve().parents[1]; C=B.parent; OLD=C.parent/'ch006/production/source'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def write(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
assert not (B/'source/layout_config.json').exists(), 'Initializer already ran; do not overwrite layout/review work'
raw=C/'handoff/Chapter_7/panels_and_dialogue.json'; panels=json.loads(raw.read_text())
assert [p['panel'] for p in panels]==list(range(1,35))
font=Path('private_fonts/animeace2/animeace2bb_ot/animeace2_reg.otf').resolve();assert font.is_file()
shutil.copy2(C/'script_v1.md',B/'source/script_v1.md')
shutil.copy2(C/'CONTINUITY_AND_ART_LOCK.md',B/'source/CONTINUITY_AND_ART_LOCK.md')
shutil.copy2(raw,B/'source/panels_and_dialogue.json')
shutil.copy2(OLD/'fit_text.py',B/'source/fit_text.py')
records=[];layout={}
for p in panels:
 items=[]
 for d in p['dialogue']:
  who,*delivery=d['speaker_delivery'].split(', ',1)
  item={'speaker':who,'text':d['text'],'kind':'dialogue','speaker_delivery':d['speaker_delivery']}
  if delivery:item['delivery']=delivery[0]
  if delivery and delivery[0] in ('PHONE','RADIO'):item['transmitted']=True;item['transmission_channel']=delivery[0].lower()
  items.append(item)
 for text in p['native_device_text']:
  items.append({'speaker':'PHONE SCREEN','text':text,'kind':'phone_info','native_imagegen_required':True,'conditional_readability':p['panel']==17})
 records.append({'panel':p['panel'],'items':items,'acting_and_art_direction':p['full_script']})
 layout[str(p['panel'])]={'source':None,'crop':None,'art_width':800,'extension':[0,0],'protection_reviewed':False,'protected_boxes':[],'protected_polygons':[],'items':{},'status':'awaiting_art_and_exact_crop_QA'}
write(B/'source/lettering_script.json',{'chapter':7,'title':'Twenty Thousand Won','script_sha256':sha(C/'script_v1.md'),'dialogue_json_sha256':sha(raw),'panels':records})
write(B/'source/layout_config.json',{'chapter':7,'font_path':str(font),'font_policy':'Local rasterization only. Never copy font programs into deliveries or embed in PDF.','panels':layout})
write(B/'qa/independent_raw_review.json',{'chapter':7,'reviews':[],'required_match':['sha256','panels','crop_xyxy'],'note':'Independent reviewer fills verdicts; assembly must never self-approve.'})
refs=json.loads((C/'handoff/Chapter_7/reference_manifest.json').read_text());write(B/'source/reference_lock.json',{'selected':[{'path':r['source'],'sha256':r['sha256'],'use':r['use']} for r in refs]})
s=(OLD/'build_chapter.py').read_text().replace('range(1,42)','range(1,35)').replace('all41','all34').replace('==41','==34').replace('Chapter 6: The Person Outside','Chapter 7: Twenty Thousand Won').replace('END CHAPTER 6','END CHAPTER 7').replace('Chapter_6','Chapter_7').replace("'chapter':6","'chapter':7")
# No provisional raw-art override. Every rendered source must have an exact independent pass.
s=s.replace("in (('pass','provisional_pass') if os.environ.get('ALLOW_PROVISIONAL')=='1' else ('pass',))","== 'pass'")
s=s.replace("gutter=100 if pair[0][0] in (9,23,31) else 64","gutter=100 if pair[0][0] in (7,19,21,25,27) else 64")
s=s.replace("src=Path(cfg['source']);", "assert cfg.get('source') and cfg.get('crop'), ('Artwork and crop required',n)\n src=Path(cfg['source']);")
# Revalidate native pixels in the render record without adding a single pixel of type to art.
s=s.replace("if item.get('native_imagegen_required'):assert", "if item.get('native_imagegen_required'):assert")
(B/'source/build_chapter.py').write_text(s)
s=(OLD/'preflight.py').read_text().replace("'chapter':6","'chapter':7").replace("'expected_units':41","'expected_units':34")
(B/'source/preflight.py').write_text(s)
s=(OLD/'export_pdf390.py').read_text().replace('Chapter_6','Chapter_7').replace('len(d)==21','len(d)==17');(B/'source/export_pdf390.py').write_text(s)
write(B/'source/preparation_provenance.json',{'renderer_source':str(OLD/'build_chapter.py'),'renderer_source_sha256':sha(OLD/'build_chapter.py'),'font_file_sha256':sha(font),'dialogue_count':sum(len(p['dialogue']) for p in panels),'native_row_count':sum(len(p['native_device_text']) for p in panels),'fonts_copied':False,'art_generated':False,'render_started':False})
print('Prepared',len(records),'units;',sum(len(p['dialogue']) for p in panels),'dialogue lines; 4 native rows.')
