#!/usr/bin/env python3
"""Exercise the unchanged repository reader with private Chapter 5 assets.

No site file is edited. This script does not supply a substitute audio fixture.
"""
import argparse
import functools
import hashlib
import http.server
import json
import mimetypes
from pathlib import Path
import shutil
import subprocess
import threading
import time
from urllib.parse import unquote, urlparse

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]
REPO = Path('/workspace/abafaboy.github.io')
HERE = ROOT / 'qa'


def sha256(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def source_runtime():
    names = ['read.html', 'series.js', 'narration.js', 'series.css']
    return {name: sha256(REPO / 'manhwa/series' / name) for name in names}


def main():
    global REPO
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, default=ROOT / 'assets/series.json')
    parser.add_argument('--output', type=Path, default=HERE / 'browser_results.json')
    parser.add_argument('--repository', type=Path, default=REPO)
    parser.add_argument('--timing', type=Path)
    parser.add_argument('--geometry', type=Path, default=ROOT / 'qa/follow_geometry.json')
    args = parser.parse_args()
    REPO = args.repository.resolve(strict=True)
    manifest_path = args.manifest.resolve(strict=True)
    manifest = json.loads(manifest_path.read_text())
    chapter = next(c for c in manifest['chapters'] if c['n'] == 5)
    if 'audio' not in chapter:
        raise RuntimeError('Real Chapter 5 audio is required; no substitute is used.')
    timing_path = args.timing or manifest_path.parent / 'timing.private.json'
    timing = json.loads(timing_path.read_text())
    source_lines = timing['lines']
    if len(source_lines) != 56 or timing.get('test_only'):
        raise RuntimeError('Expected 56 real source dialogue recordings, with test_only false.')
    geometry = json.loads(args.geometry.read_text())
    geometry_by_record = {(d['panel'], d['item_index'] + 1): d for d in geometry['dialogue']}
    wrapped = {line['id']: line for line in geometry['lines']}
    expected_clamps = sum(d['anchor_clamped'] for d in geometry['dialogue'])
    segments = dict(chapter['segments'])
    assets = {}
    for name in [s[0] for s in chapter['segments']] + [chapter['audio']['file']]:
        candidates = [manifest_path.parent / 'ch/005' / name,
                      manifest_path.parent / 'assets/ch/005' / name,
                      manifest_path.parent / name,
                      ROOT / 'assets/ch/005' / name]
        assets[name] = next((p for p in candidates if p.is_file()), None)
        if assets[name] is None:
            raise FileNotFoundError(f'No private asset for {name}; checked {candidates}')
    report = {
        'status': 'running', 'scope': 'Private local browser integration; no site mutation, publication or deployment',
        'manifest': str(manifest_path), 'manifest_sha256': sha256(manifest_path),
        'timing_sha256': sha256(timing_path),
        'reader_runtime_sha256': source_runtime(),
        'repo_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=REPO, text=True).strip(),
        'assets': {name: {'path': str(path), 'bytes':path.stat().st_size, 'sha256':sha256(path)} for name,path in assets.items()},
        'viewports': [], 'failures': [],
        'limitations': [
            'Headless Chromium exercises native media decoding and clock, but no subjective listening or pronunciation/performance assessment is claimed.',
            'This is a private interception of the unchanged repository reader. It does not establish deployed website availability.',
            'No screenshots are saved or uploaded. Geometry measurements use actual decoded approved-reader JPEG assets and source placement rectangles.',
        ],
    }
    server = http.server.ThreadingHTTPServer(('127.0.0.1',0), functools.partial(QuietHandler, directory=str(REPO)))
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    origin = f'http://127.0.0.1:{server.server_port}'
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True, executable_path=shutil.which('chromium'))
            report['browser_version'] = browser.version
            for viewport in [{'width':390,'height':844}, {'width':1440,'height':900}]:
                result = {'viewport':viewport, 'checks':{}, 'dialogue_visibility':[], 'final_panel_visibility':{}, 'media_requests':[], 'page_errors':[]}
                report['viewports'].append(result)
                context = browser.new_context(viewport=viewport, is_mobile=viewport['width']<600, has_touch=viewport['width']<600)
                page = context.new_page()
                page.on('pageerror', lambda error: result['page_errors'].append(str(error)))
                page.route('https://fonts.googleapis.com/**', lambda route: route.abort())
                page.route('https://fonts.gstatic.com/**', lambda route: route.abort())
                page.route(f'**/manhwa/series/{manifest["slug"]}/series.json', lambda route: route.fulfill(content_type='application/json', body=json.dumps(manifest)))

                def asset_route(route):
                    name = Path(unquote(urlparse(route.request.url).path)).name
                    if name not in assets:
                        return route.fulfill(status=404, body='Not part of private Chapter 5 package')
                    path = assets[name]
                    data = path.read_bytes()
                    content_type = mimetypes.guess_type(name)[0] or 'application/octet-stream'
                    if name == chapter['audio']['file']:
                        result['media_requests'].append({'url':route.request.url,'range':route.request.headers.get('range')})
                    requested = route.request.headers.get('range','')
                    if requested.startswith('bytes='):
                        lo, hi = requested[6:].split('-',1)
                        start = int(lo or 0); end = min(int(hi) if hi else len(data)-1,len(data)-1)
                        return route.fulfill(status=206, content_type=content_type, headers={'Accept-Ranges':'bytes','Content-Range':f'bytes {start}-{end}/{len(data)}'}, body=data[start:end+1])
                    return route.fulfill(content_type=content_type, headers={'Accept-Ranges':'bytes'}, body=data)

                page.route(f'**/manhwa/series/{manifest["slug"]}/ch/005/*', asset_route)

                def check(name, value, details=None):
                    result['checks'][name] = {'pass':bool(value), 'details':details}
                    if not value:
                        report['failures'].append({'viewport':viewport,'check':name,'details':details})

                def seek(t):
                    page.locator('#audio').evaluate('(audio,t) => { audio.currentTime = t; }',t)
                    page.wait_for_function('(t) => !document.querySelector("#audio").seeking && Math.abs(document.querySelector("#audio").currentTime - t) < .035',arg=t)
                    page.wait_for_timeout(25)

                def measure_line(line, label):
                    record = geometry_by_record[(line['panel'],line['line'])]
                    geom_lines = [wrapped[id_] for id_ in record['line_ids']]
                    image = page.locator(f'#strip img[src$="/{line["segment"]}"]')
                    box = image.bounding_box()
                    page_data = next(p for p in geometry['pages'] if p['page']==record['page'])
                    scale_y = box['height']/page_data['size_master'][1]
                    scale_x = box['width']/page_data['size_master'][0]
                    bounds = []
                    sticky = page.locator('#narration').bounding_box()
                    inset = sticky['y']+sticky['height']
                    def viewport_rect(rect):
                        x,y,w,h=rect
                        return {'left':box['x']+x*scale_x,'top':box['y']+y*scale_y,
                                'right':box['x']+(x+w)*scale_x,'bottom':box['y']+(y+h)*scale_y}
                    def fully_visible(rect):
                        return rect['top']>=inset-1 and rect['bottom']<=viewport['height']+1 and rect['left']>=-1 and rect['right']<=viewport['width']+1
                    for gl in geom_lines:
                        bounds.append(viewport_rect(gl['bounds_page_master_xywh']))
                    bubble=viewport_rect(record['bubble_bounds_page_master_xywh'])
                    same_row=None
                    if line['monotonic_clamp']:
                        previous=geometry['dialogue'][record['sequence']-2]
                        joint_records=[previous,record]
                        joint_bubbles=[viewport_rect(r['bubble_bounds_page_master_xywh']) for r in joint_records]
                        joint_lines=[viewport_rect(wrapped[id_]['bounds_page_master_xywh']) for r in joint_records for id_ in r['line_ids']]
                        same_row={'record_ids':[r['id'] for r in joint_records],
                                  'bubble_bounds':joint_bubbles,'text_line_bounds':joint_lines,
                                  'all_joint_bubbles_and_text_visible':all(fully_visible(b) for b in joint_bubbles+joint_lines)}
                    visible=all(fully_visible(b) for b in bounds)
                    bubble_visible=fully_visible(bubble)
                    joint_visible=same_row is None or same_row['all_joint_bubbles_and_text_visible']
                    observed = {'id':line['id'],'panel':line['panel'],'line':line['line'],'phase':label,
                                'time':page.locator('#audio').evaluate('a=>a.currentTime'),
                                'scroll_y':page.evaluate('scrollY'),'sticky_bottom':inset,
                                'wrapped_line_bounds':bounds,'all_wrapped_lines_visible':visible,
                                'bubble_bounds':bubble,'full_bubble_box_visible':bubble_visible,
                                'same_row_joint_check':same_row,
                                'monotonic_clamp':line['monotonic_clamp']}
                    result['dialogue_visibility'].append(observed)
                    if not visible or not bubble_visible or not joint_visible:
                        report['failures'].append({'viewport':viewport,'check':'source_dialogue_visibility','details':observed})

                try:
                    page.goto(f'{origin}/manhwa/series/read.html?series={manifest["slug"]}&ch=5')
                    page.wait_for_function('document.querySelector("#status").hidden || !document.querySelector("#status").textContent.startsWith("Loading")')
                    check('reader_visible',page.locator('#reader').is_visible(),page.locator('#status').text_content())
                    check('narration_visible',page.locator('#narration').is_visible())
                    check('follow_initially_on',page.locator('#follow').get_attribute('aria-pressed')=='true')
                    check('no_autoplay',page.locator('#audio').evaluate('a=>a.paused && !a.autoplay && a.preload === "none" && a.currentTime === 0'))
                    check('no_media_request_before_interaction',not result['media_requests'])
                    page.locator('#strip img').evaluate_all('images=>images.forEach(image=>image.loading="eager")')
                    page.wait_for_function('[...document.querySelectorAll("#strip img")].length===19 && [...document.querySelectorAll("#strip img")].every(i=>i.complete && i.naturalWidth>0)')
                    page.locator('#strip img').evaluate_all('images=>Promise.all(images.map(i=>i.decode()))')
                    dimensions = page.locator('#strip img').evaluate_all('images=>images.map(i=>({file:i.src.split("/").at(-1),width:i.naturalWidth,height:i.naturalHeight,renderedWidth:i.clientWidth,renderedHeight:i.clientHeight}))')
                    check('all_19_dimensions_match_manifest',len(dimensions)==19 and all(i['width']==chapter['width'] and i['height']==segments[i['file']] for i in dimensions),dimensions)
                    check('no_horizontal_overflow',not page.evaluate('document.documentElement.scrollWidth > innerWidth'))
                    page.locator('#audio').evaluate('a=>a.play()')
                    page.wait_for_function('document.querySelector("#audio").currentTime>.1')
                    page.locator('#audio').evaluate('a=>a.pause()')
                    duration = page.locator('#audio').evaluate('a=>a.duration')
                    check('native_media_duration_matches',abs(duration-chapter['audio']['duration'])<.2,{'native':duration,'manifest':chapter['audio']['duration']})
                    old_y = page.evaluate('scrollY')
                    old_t = page.locator('#audio').evaluate('a=>a.currentTime')
                    page.wait_for_timeout(220)
                    check('pause_stops_clock_and_follow',abs(page.evaluate('scrollY')-old_y)<1 and abs(page.locator('#audio').evaluate('a=>a.currentTime')-old_t)<.001)
                    for line in source_lines:
                        seek(line['start']+.001)
                        measure_line(line,'start')
                        seek(line['end']-.001)
                        measure_line(line,'end')
                    check('all_56_source_dialogue_records_visible_at_start_and_end',len(result['dialogue_visibility'])==112 and all(v['all_wrapped_lines_visible'] for v in result['dialogue_visibility']))
                    check('all_56_full_bubble_boxes_visible_at_start_and_end',len(result['dialogue_visibility'])==112 and all(v['full_bubble_box_visible'] for v in result['dialogue_visibility']))
                    check('all_clamped_records_checked',sum(v['monotonic_clamp'] for v in result['dialogue_visibility'])==expected_clamps*2)
                    check('all_shared_row_pairs_fully_visible',all(v['same_row_joint_check'] is None or v['same_row_joint_check']['all_joint_bubbles_and_text_visible'] for v in result['dialogue_visibility']))
                    seek(source_lines[45]['start'])
                    page.locator('#audio').evaluate('a=>a.play()')
                    page.wait_for_function('!document.querySelector("#audio").paused')
                    page.mouse.wheel(0,230)
                    page.wait_for_function('document.querySelector("#follow").getAttribute("aria-pressed")==="false"')
                    check('manual_scroll_turns_follow_off_without_pausing_audio',not page.locator('#audio').evaluate('a=>a.paused'))
                    page.locator('#audio').evaluate('a=>a.pause()')
                    page.wait_for_timeout(180)
                    manual_y = page.evaluate('scrollY')
                    seek(source_lines[-1]['start'])
                    check('seek_with_follow_off_preserves_scroll',abs(page.evaluate('scrollY')-manual_y)<1)
                    page.locator('#follow').click()
                    page.wait_for_timeout(30)
                    check('follow_on_realigns_current_seek',page.locator('#follow').get_attribute('aria-pressed')=='true' and abs(page.evaluate('scrollY')-manual_y)>100)
                    seek(chapter['audio']['duration']-.01)
                    last_panel = next(p for p in geometry['panels'] if p['panel']==38)
                    last_image = page.locator('#strip img').nth(18).bounding_box()
                    page_h = geometry['pages'][-1]['size_master'][1]
                    _, y, _, h = last_panel['bounds_page_master_xywh']
                    final_top = last_image['y']+y*last_image['height']/page_h
                    final_bottom = last_image['y']+(y+h)*last_image['height']/page_h
                    controls = page.locator('#narration').bounding_box()
                    result['final_panel_visibility'] = {'top':final_top,'bottom':final_bottom,'sticky_bottom':controls['y']+controls['height'],'viewport_height':viewport['height']}
                    check('final_panel_and_lower_edge_visible',final_top>=controls['y']+controls['height']-1 and final_bottom<=viewport['height']+1,result['final_panel_visibility'])
                    bar = page.locator('.reader-bar').bounding_box()
                    check('sticky_controls_remain_accessible',abs(bar['y'])<1 and controls['y']>=bar['height']-1 and controls['y']+controls['height']<viewport['height'])
                    check('audio_did_not_error',not page.locator('#audio-error').is_visible())
                    check('no_page_errors',not result['page_errors'],result['page_errors'])
                except Exception as error:
                    report['failures'].append({'viewport':viewport,'check':'harness_exception','details':repr(error)})
                    result['exception']=repr(error)
                finally:
                    context.close()
            browser.close()
    finally:
        server.shutdown();server.server_close();thread.join()
    report['status']='pass' if not report['failures'] else 'fail'
    report['reader_runtime_unchanged']=source_runtime()==report['reader_runtime_sha256']
    if not report['reader_runtime_unchanged']:
        report['status']='fail'
        report['failures'].append({'check':'reader_runtime_unchanged','details':'Reader source changed during test'})
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({'status':report['status'],'viewports':len(report['viewports']),'source_dialogue_checks':sum(len(r['dialogue_visibility']) for r in report['viewports']),'failures':report['failures'],'output':str(args.output)},indent=2))
    return 0 if report['status']=='pass' else 1


if __name__=='__main__':
    raise SystemExit(main())
