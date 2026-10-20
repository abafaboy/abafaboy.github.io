"""Package selected native artwork and editable lettering after final reader QA."""
from pathlib import Path
import json,hashlib,zipfile,os,shutil
B=Path(__file__).resolve().parents[1];OUT=B/'delivery';OUT.mkdir(exist_ok=True)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
c=json.loads((B/'source/layout_config.json').read_text());s=json.loads((B/'source/lettering_script.json').read_text());manifest=json.loads((B/'lettered/placement_manifest.json').read_text());assert len(manifest['panels'])==34
proof=B/'qa/final_reader_review.json';assert proof.is_file(),'Final independent reader review required before source packaging'
verdict=json.loads(proof.read_text());assert verdict.get('verdict')=='pass' and verdict.get('pdf_sha256')==sha(B/'lettered/My_Summons_Go_First_Chapter_7.pdf'),'Final reader verdict must match final PDF'
selected={n:(B/cfg['source']).resolve() for n,cfg in c['panels'].items()};hashes={n:sha(p) for n,p in selected.items()};wanted_names={p.name for p in selected.values()};archives=[]
for zpath in sorted((B.parent/'incoming').rglob('*.zip')):
 try:lid=os.getxattr(zpath,'user.library-file-id').decode();version=int(os.getxattr(zpath,'user.library-file-version').decode())
 except OSError:continue
 with zipfile.ZipFile(zpath) as z:
  for member in z.namelist():
   if Path(member).name not in wanted_names:continue
   digest=hashlib.sha256(z.read(member)).hexdigest()
   if digest in hashes.values():archives.append({'source_sha256':digest,'library_file_id':lid,'library_version':version,'library_archive_filename':zpath.name,'archive_sha256':sha(zpath),'member':member})
index=[]
for n,p in selected.items():
 origins=[r for r in archives if r['source_sha256']==hashes[n]];assert origins,('Missing Library provenance',n,p)
 index.append({'panel':int(n),'native_file':f'raw/selected/ch007_p{int(n):02}_native.png','sha256':hashes[n],'crop_xyxy':c['panels'][n]['crop'],'library_originals':origins})
index.sort(key=lambda r:r['panel']);(OUT/'Chapter_7_Source_Index.json').write_text(json.dumps(index,indent=2)+'\n')
portable=json.loads(json.dumps(c));portable['font_path']='';portable['font_policy']='Set ANIME_ACE_FONT to your separately licensed local Anime Ace 2.0 BB. Font programs intentionally excluded.'
for row in index:portable['panels'][str(row['panel'])]['source']=row['native_file']
files={}
for n,p in selected.items():files[f'raw/selected/ch007_p{int(n):02}_native.png']=p
for name in ['build_chapter.py','fit_text.py','export_pdf390.py','lettering_script.json','script_v1.md','CONTINUITY_AND_ART_LOCK.md'] :files['source/'+name]=B/'source'/name
for d in ['full','phone','reader']:
 for p in sorted((B/'lettered'/d).glob('*.png')):files['lettered/'+d+'/'+p.name]=p
for name in ['independent_raw_review.json','final_reader_review.json','final_technical_verification.json'] :files['qa/'+name]=B/'qa'/name
files['lettered/placement_manifest.json']=B/'lettered/placement_manifest.json';files['Chapter_7_Source_Index.json']=OUT/'Chapter_7_Source_Index.json'
readme='''# Chapter 7 editable source\n\n34 acting units. Native source PNGs are unchanged imagegen outputs; crop, scaling, protection regions, balloon outlines, glyph bounds and exact text are recorded in the layout and placement manifests. Full/phone panels and paired reader pages are included. No publication is performed by this package.\n\nThe source index identifies exact Library archives and versions retaining the original generation attempts and prompts. Only selected native outputs are duplicated here.\n\nNo font programs are embedded or supplied. Obtain Anime Ace 2.0 BB under its applicable license and set ANIME_ACE_FONT to that local font file. The saved PDF consists of raster images. To rebuild, run python source/build_chapter.py from this directory; source/layout_config.json holds all placements. Pillow, PyMuPDF and fontTools are required.\n\nProtected regions and native phone text must be preserved. Device lettering comes from native artwork, never an assembly text patch. Independent source review and final compressed-reader review accompany the package.\n'''
parts=[];items=list(files.items());limit=480*1024*1024;batch=[];size=0
for item in items:
 n=item[1].stat().st_size
 if batch and size+n>limit:parts.append(batch);batch=[];size=0
 batch.append(item);size+=n
if batch:parts.append(batch)
results=[]
for i,part in enumerate(parts,1):
 name=f'My_Summons_Go_First_Chapter_7_Sources_Part_{i}_of_{len(parts)}.zip';dest=OUT/name
 with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  z.writestr('README.md',readme);z.writestr('source/layout_config.json',json.dumps(portable,indent=2)+'\n')
  for arc,path in part:z.write(path,arc)
 with zipfile.ZipFile(dest) as z:assert not any(Path(n).suffix.lower() in ('.otf','.ttf','.woff','.woff2') for n in z.namelist());assert z.testzip() is None
 assert dest.stat().st_size<512*1024*1024
 results.append({'path':str(dest),'bytes':dest.stat().st_size,'sha256':sha(dest),'font_programs':0})
(OUT/'source_package_index.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))
