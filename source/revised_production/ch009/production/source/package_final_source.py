from pathlib import Path
import shutil,json,hashlib,zipfile
B=Path(__file__).resolve().parents[1];D=B/'delivery/Chapter_9_Reproducible_Source';D.mkdir(parents=True,exist_ok=True)
def copy(p,rel=None):
 q=D/(rel or p.relative_to(B));q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q)
c=json.loads((B/'source/layout_config.json').read_text());assets=[]
for n,p in c['panels'].items():
 for frame in [p]+p.get('native_following_frames',[]):
  src=B/frame['source'];copy(src);assets.append({'unit':int(n),'source':frame['source'],'sha256':hashlib.sha256(src.read_bytes()).hexdigest()})
for name in ['build_chapter.py','fit_text.py','verify_current_acceptance.py','script_v1.md','lettering_script.json']:
 copy(B/'source'/name)
c['font_path']='';c['font_policy']='Supply your own authorized local Anime Ace font via ANIME_ACE_FONT. Font program is excluded; final PDF contains raster images only.'
(D/'source/layout_config.json').write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
for p in (B/'source').glob('*.py'):
 if p.name not in ['build_chapter.py','fit_text.py','verify_current_acceptance.py','package_final_source.py']:copy(p,Path('provenance/historical_assembly_scripts')/p.name)
for p in (B/'qa').glob('*.json'):copy(p)
for p in (B/'raw').rglob('*.json'):
 if 'history' in p.parts or p.name.startswith('SHA256'):continue
 copy(p,Path('provenance/original_batch_metadata')/p.relative_to(B/'raw'))
for p in (B/'raw').rglob('*.txt'):
 if 'prompts' in p.parts:copy(p,Path('provenance/generation_prompts')/p.relative_to(B/'raw'))
for name in ['placement_manifest.json','My_Summons_Go_First_Chapter_9.pdf']:copy(B/'lettered'/name)
for folder in ['full','phone','reader']:
 for p in (B/'lettered'/folder).glob('*.png'):copy(p)
(D/'SELECTED_NATIVE_ASSETS.json').write_text(json.dumps(assets,indent=2)+'\n')
(D/'README.md').write_text('''# My Summons Go First — Chapter 9: The Open Side

Complete 33-unit reader, 17 pages. The approved script has 54 text items. U12 contains two distinct native chronological frames, silent handle check then supported lift/hold. Approved same-moment detail insets and added blank lettering spacing are explicitly mapped in the placement manifest.

## Contents
- `lettered/My_Summons_Go_First_Chapter_9.pdf`: image-only reader, no embedded font programs
- `lettered/reader/`: full-width and actual390 reader pages
- `lettered/full/` and `lettered/phone/`: individual unit proofs
- `raw/`: 34 selected untouched native source images, retaining reproducible relative paths
- `source/`: exact script, active layout, renderer, text fitting and acceptance checker
- `qa/`: independent hash-bound raw/lettering/reader reviews, intake and export checks; earlier held versions remain historical records, not approvals
- `provenance/`: batch metadata, generation prompts and historical layout scripts
- `qa/retained_library_sources.json`: immutable Library file IDs and server-returned version metadata for exhaustive retained attempts, variants and references. Those large archives remain in Library and the production workspace and are not duplicated here. An initial upload may return a null version number; its immutable backing file ID pins the content without inventing a version.

## Reproduce
Use Python with Pillow, PyMuPDF, fonttools. Supply your own authorized Anime Ace 2.0 BB Regular font via the ANIME_ACE_FONT environment variable; no font program is included. DejaVu Sans is used only for presentation/caption fallback. Run `python source/build_chapter.py`, then `python source/verify_current_acceptance.py`. Set UI_FONT if the system DejaVu path differs. Environment/software/font differences may change raster hashes; newly rendered images need visual QA before replacement.

Only `source/layout_config.json` is the authoritative final placement. Historical placement scripts preserve production evidence and should not be rerun as the final build.

All selected art remains native and unchanged. Layout uses scaling, approved crops and blank spacing, never redrawing. No website publication has been performed. No audio file is included.

`SHA256_MANIFEST.json` hashes every packaged file except itself. Exhaustive earlier-art files referenced in historical review logs are retained in their source archives, not silently substituted into this reader.
''')
manifest={str(p.relative_to(D)):{'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in sorted(D.rglob('*')) if p.is_file() and p.name!='SHA256_MANIFEST.json'}
(D/'SHA256_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
z=B/'delivery/My_Summons_Go_First_Chapter_9_Reproducible_Source.zip'
with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as f:
 for p in sorted(D.rglob('*')):
  if p.is_file():f.write(p,Path(D.name)/p.relative_to(D))
with zipfile.ZipFile(z) as f:
 assert f.testzip() is None
 for name,r in manifest.items():assert hashlib.sha256(f.read(D.name+'/'+name)).hexdigest()==r['sha256']
 assert not any(Path(n).suffix.lower() in ['.otf','.ttf','.woff','.woff2'] for n in f.namelist())
report={'archive':str(z),'sha256':hashlib.sha256(z.read_bytes()).hexdigest(),'bytes':z.stat().st_size,'verified_files':len(manifest),'native_images':len(assets),'font_programs':0,'zip_crc_and_each_file_sha256':'pass'}
(B/'delivery/archive_integrity.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
