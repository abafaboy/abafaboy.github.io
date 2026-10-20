from pathlib import Path
import json,threading,functools,http.server,hashlib,shutil
from playwright.sync_api import sync_playwright
R=Path(__file__).resolve().parents[1]; O=R;runtime=R/'runtime';assets=O/'assets';m=json.loads((assets/'series.json').read_text());ch=m['chapters'][0];timing=json.loads((assets/'timing.private.json').read_text());geo=json.loads((O/'qa/geometry.json').read_text());prov=json.loads((runtime/'runtime_provenance.json').read_text())
for name,info in prov.items():
 b=(runtime/'manhwa/series'/name).read_bytes();assert hashlib.sha1(b'blob '+str(len(b)).encode()+bytes([0])+b).hexdigest()==info['sha']
link=runtime/'manhwa/series/my-summons-go-first'
if not link.exists():link.symlink_to(assets.resolve(),target_is_directory=True)
class Quiet(http.server.SimpleHTTPRequestHandler):
 def log_message(self,*a):pass
server=http.server.ThreadingHTTPServer(('127.0.0.1',0),functools.partial(Quiet,directory=str(runtime)));threading.Thread(target=server.serve_forever,daemon=True).start()
report={'scope':'Private localhost test of byte-identical fetched GitHub reader files, not deployed site','runtime':prov,'viewports':[],'failures':[],'subjective_audition':False}
with sync_playwright() as pw:
 browser=pw.chromium.launch(executable_path=shutil.which('chromium'),headless=True)
 for vp in [{'width':390,'height':844},{'width':1440,'height':900}]:
  ctx=browser.new_context(viewport=vp,is_mobile=vp['width']==390,has_touch=vp['width']==390);page=ctx.new_page();res={'viewport':vp,'checks':{},'dialogue':[],'holds':[],'errors':[]};report['viewports'].append(res);page.on('pageerror',lambda e:res['errors'].append(str(e)))
  def check(name,value,detail=None):
   res['checks'][name]={'pass':bool(value),'detail':detail}
   if not value:report['failures'].append({'viewport':vp,'check':name,'detail':detail})
  def seek(t):
   page.locator('#audio').evaluate('(a,t)=>{a.currentTime=t}',t);page.wait_for_function('t=>!document.querySelector("#audio").seeking&&Math.abs(document.querySelector("#audio").currentTime-t)<.035',arg=t);page.wait_for_timeout(30)
  def rects(segment,boxes):
   box=page.locator(f'#strip img[src$="/{segment}"]').bounding_box();scale=box['width']/800; inset=page.locator('#narration').bounding_box();minimum=inset['y']+inset['height']; coords=[{'left':box['x']+x*scale,'top':box['y']+y*scale,'right':box['x']+(x+w)*scale,'bottom':box['y']+(y+h)*scale} for x,y,w,h in boxes];ok=all(c['left']>=-1 and c['right']<=vp['width']+1 and c['top']>=minimum-1 and c['bottom']<=vp['height']+1 for c in coords);return ok,{'bounds':coords,'inset':minimum,'scroll':page.evaluate('scrollY')}
  try:
   page.goto(f'http://127.0.0.1:{server.server_port}/manhwa/series/read.html?series=my-summons-go-first&ch=6');page.wait_for_selector('#reader',state='visible');page.locator('#strip img').evaluate_all('im=>im.forEach(i=>i.loading="eager")');page.wait_for_function('[...document.querySelectorAll("#strip img")].every(i=>i.complete&&i.naturalWidth>0)');page.locator('#strip img').evaluate_all('im=>Promise.all(im.map(i=>i.decode()))')
   check('no_autoplay',page.locator('#audio').evaluate('a=>a.paused&&a.preload==="none"&&a.currentTime===0'));check('follow_default_on',page.locator('#follow').get_attribute('aria-pressed')=='true');check('no_overflow',page.evaluate('document.documentElement.scrollWidth<=innerWidth'))
   dims=page.locator('#strip img').evaluate_all('im=>im.map(i=>[i.naturalWidth,i.naturalHeight])');check('all_21_image_dimensions',dims==[[800,h] for f,h in ch['segments']],dims)
   page.locator('#audio').evaluate('a=>a.play()');page.wait_for_function('document.querySelector("#audio").currentTime>.1');page.locator('#audio').evaluate('a=>a.pause()');dur=page.locator('#audio').evaluate('a=>a.duration');check('actual_mp3_duration',abs(dur-ch['audio']['duration'])<.1,dur)
   for line,g in zip(timing['lines'],geo['dialogue']):
    for phase,t in [('start',line['start']+.002),('middle',(line['start']+line['end'])/2),('end',line['end']-.002)]:
     seek(t);ok,detail=rects(g['segment'],[g['box']]+g['line_bounds']);item={'id':line['id'],'phase':phase,'time':t,'visible':ok,**detail};res['dialogue'].append(item)
     if not ok:report['failures'].append({'viewport':vp,'check':'dialogue_visibility','detail':item})
   for h in timing['visual_holds']:
    p=next(p for p in geo['panels'] if p['panel']==h['panel']);ys=[]
    for phase,t in [('start',h['start']+.002),('middle',(h['start']+h['end'])/2),('end',h['end']-.002)]:
     seek(t);ok,detail=rects(p['segment'],[[0,p['y_top'],800,p['y_bottom']-p['y_top']]]);ys.append(detail['scroll']);item={'panel':p['panel'],'phase':phase,'time':t,'visible':ok,**detail};res['holds'].append(item)
     if not ok:report['failures'].append({'viewport':vp,'check':'visual_hold_visibility','detail':item})
    check(f'hold_stationary_{p["panel"]}',max(ys)-min(ys)<=1,ys)
   seek(ch['audio']['duration']-.01);p=geo['panels'][-1];ok,d=rects(p['segment'],[[0,p['y_top'],800,p['y_bottom']-p['y_top']]]);check('final_panel_lower_edge',ok,d)
   old=page.evaluate('scrollY');t=page.locator('#audio').evaluate('a=>a.currentTime');page.wait_for_timeout(200);check('pause_stops_follow',abs(page.evaluate('scrollY')-old)<1 and abs(page.locator('#audio').evaluate('a=>a.currentTime')-t)<.001)
   seek(timing['lines'][10]['start']);page.locator('#audio').evaluate('a=>a.play()');page.mouse.wheel(0,150);page.wait_for_function('document.querySelector("#follow").getAttribute("aria-pressed")==="false"');check('manual_scroll_keeps_audio',page.locator('#audio').evaluate('a=>!a.paused'));page.locator('#audio').evaluate('a=>a.pause()');page.wait_for_timeout(200);old=page.evaluate('scrollY');seek(timing['lines'][-1]['start']);check('follow_off_keeps_scroll',abs(page.evaluate('scrollY')-old)<1);page.locator('#follow').click();page.wait_for_timeout(50);check('follow_on_realigns',abs(page.evaluate('scrollY')-old)>100)
   seek(ch['audio']['duration']-.3);page.locator('#audio').evaluate('a=>a.play()');page.wait_for_function('document.querySelector("#audio").ended');page.wait_for_timeout(60);check('end_navigation_visible',page.locator('#endnav').bounding_box()['y']<vp['height']);check('no_page_errors',not res['errors']);check('no_audio_error',not page.locator('#audio-error').is_visible())
  except Exception as e:report['failures'].append({'viewport':vp,'check':'exception','detail':repr(e)})
  ctx.close()
 browser.close()
server.shutdown();report['status']='pass' if not report['failures'] else 'fail';(O/'qa/browser_results.json').write_text(json.dumps(report,indent=2));print(json.dumps({'status':report['status'],'checks':sum(len(v['dialogue']) for v in report['viewports']),'failures':report['failures']},indent=2))
