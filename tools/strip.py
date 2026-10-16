"""Lay out webtoon strip in HTML, screenshot full page, export anchor positions.
Every text element (narration, speech, SFX) is checked against annotated face boxes; any overlap fails the build."""
import builtins as _b
def open(f, mode='r', *a, **k):  # UTF-8 everywhere (Windows defaults to cp1252)
    if 'b' not in mode and 'encoding' not in k: k['encoding'] = 'utf-8'
    return _b.open(f, mode, *a, **k)
import json, sys, html as H
from pathlib import Path
from playwright.sync_api import sync_playwright

ART, FONTS, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
# optional 5th arg: the end-card image (defaults to ART/end.png)
END = sys.argv[5] if len(sys.argv) > 5 else str(Path(ART, "end.png"))
def uri(p): return Path(p).resolve().as_uri()
FONTS_URI = uri(FONTS)

LAYOUT = sys.argv[4]
FACES = {}

def img(name, cls="", style=""):
    f = ";".join(",".join(map(str, b)) for b in FACES.get(name, []))
    return f'<img class="pn {cls}" data-name="{name}" data-faces="{f}" src="{uri(END) if name == 'end' else uri(Path(ART, name + '.png'))}" style="{style}">'

def narr(text, anchor, style=""):
    return f'<div class="narr txt" data-a="{anchor}" style="{style}">{H.escape(text)}</div>'

def bub(text, anchor, tail="left", style=""):
    lg = " long" if len(text) > 100 else ""
    return f'<div class="bub txt t-{tail}{lg}" data-a="{anchor}" style="{style}">{H.escape(text)}</div>'

def sfx(text, style, cls=""):
    return f'<div class="sfx txt {cls}" style="{style}">{H.escape(text)}</div>'

def gap(h, bg=None):
    return f'<div style="height:{h}px;{("background:"+bg) if bg else ""}"></div>'

G = dict(img=img, narr=narr, bub=bub, sfx=sfx, gap=gap)
exec(open(LAYOUT).read(), G)
FACES.update(G["FACES"])
body = G["build"]()

css = f"""
@font-face{{font-family:Cinzel;src:url('{FONTS_URI}/expo-google-fonts-cinzel-0.4.2/700Bold/Cinzel_700Bold.ttf');font-weight:700}}
@font-face{{font-family:Cinzel;src:url('{FONTS_URI}/expo-google-fonts-cinzel-0.4.2/900Black/Cinzel_900Black.ttf');font-weight:900}}
@font-face{{font-family:Fell;src:url('{FONTS_URI}/expo-google-fonts-im-fell-english-0.4.0/400Regular/IMFellEnglish_400Regular.ttf')}}
@font-face{{font-family:Fell;font-style:italic;src:url('{FONTS_URI}/expo-google-fonts-im-fell-english-0.4.0/400Regular_Italic/IMFellEnglish_400Regular_Italic.ttf')}}
html,body{{margin:0;width:1080px;overflow-x:hidden}}
.sec.white{{background:#fff}} .sec.black{{background:#05060a}}
.rel{{position:relative;width:fit-content}}
.pn{{display:block;object-fit:cover;border:4px solid #111;box-sizing:border-box}}
.black .pn{{border-color:#2a2f45}}
.pn.full{{width:1080px;height:720px;border-left:0;border-right:0}}
.sepia{{filter:sepia(.35) saturate(.85) brightness(1.03)}}
.row{{display:flex;justify-content:center;gap:24px;align-items:flex-start}}
/* narration: soft oval bubble, italic serif */
.narr{{position:relative;background:#fffdf7;color:#2a1d10;border:3px solid #3a2a18;border-radius:50%;
  font-family:Fell;font-style:italic;font-size:39px;line-height:1.28;padding:52px 70px;text-align:center;z-index:3;box-sizing:border-box;
  box-shadow:0 4px 0 #3a2a1822}}
.black .narr{{background:#10131f;color:#e8e2d0;border-color:#8b98c8;box-shadow:0 0 18px #4a6aff33}}
/* speech: white oval with a tail, bold lettering */
.bub{{position:absolute;background:#fff;color:#111;border:4px solid #111;border-radius:50%;font-family:Cinzel;font-weight:700;
  font-size:33px;line-height:1.3;padding:54px 56px;text-align:center;z-index:4;box-sizing:border-box}}
.bub:after{{content:'';position:absolute;bottom:-40px;border:16px solid transparent;border-top:44px solid #111;border-bottom:0}}
.bub:before{{content:'';position:absolute;bottom:-31px;border:12px solid transparent;border-top:37px solid #fff;border-bottom:0;z-index:1}}
.bub.t-left:after{{left:calc(30% - 16px);transform:rotate(14deg)}} .bub.t-left:before{{left:calc(30% - 12px);transform:rotate(14deg)}}
.bub.t-up:after{{right:calc(30% - 16px);bottom:auto;top:-40px;border-top:0;border-bottom:44px solid #111;transform:rotate(-14deg)}}
.bub.t-up:before{{right:calc(30% - 12px);bottom:auto;top:-31px;border-top:0;border-bottom:37px solid #fff;transform:rotate(-14deg)}}
.sfx{{position:absolute;font-family:Cinzel;font-weight:900;color:#ffe9a8;-webkit-text-stroke:5px #1a1206;paint-order:stroke fill;
  letter-spacing:4px;z-index:5;white-space:nowrap;text-shadow:0 6px 0 #1a120688}}
.sfx.quiet{{color:#f4f1ea;-webkit-text-stroke:3px #2a2a33;font-family:Fell;font-style:italic;font-weight:400}}
.sec.night{{background:#0b0d16}} .night .pn{{border-color:#2a2f45}}
.night .narr{{background:#10131f;color:#e8e2d0;border-color:#8b98c8}}
.black .bub,.night .bub{{box-shadow:0 0 0 3px #ffffff22}}
.bub.t-right:after{{right:calc(30% - 16px);transform:rotate(-14deg)}} .bub.t-right:before{{right:calc(30% - 12px);transform:rotate(-14deg)}}
.sfx.note{{color:#2a1608;-webkit-text-stroke:0;font-family:Fell;font-style:italic;font-weight:400;text-shadow:none;letter-spacing:1px;background:#f1e3c4cc;padding:6px 18px;border-radius:30px}}
.big.gold{{color:#ffe39a;text-shadow:0 0 40px #ffcc5588,0 4px 0 #3a2410}}
.title{{position:absolute;top:70px;left:0;right:0;text-align:center;z-index:5;font-family:Cinzel;color:#f3dfa6;text-shadow:0 4px 0 #000,0 0 30px #ffcc5566}}
.title .t1{{font-size:62px;font-weight:900;line-height:1.1}} .title .t2{{font-size:140px;font-weight:900;color:#ffd36b;line-height:1.1}} .title .t3{{font-size:30px;font-weight:700;letter-spacing:6px;margin-top:10px;color:#e9d2a0}}
.chap{{text-align:center;font-family:Cinzel;color:#3a2410;padding-top:60px}} .chap .c1{{font-size:34px;font-weight:700;letter-spacing:10px;color:#9a7a3a}} .chap .c2{{font-family:Fell;font-style:italic;font-size:64px;margin-top:8px}} .chap .c0{{font-size:30px;font-weight:900;letter-spacing:6px;color:#2a1d10;margin-bottom:14px}}
.bub.long{{padding:62px 66px;border-radius:46%/42%}}
.sfx.mock{{color:#f2d4ff;-webkit-text-stroke:4px #3b1050;font-family:Fell;font-style:italic;font-weight:400}}
.big{{font-family:Fell;font-style:italic;font-size:150px;color:#e8ecff;text-align:center;letter-spacing:6px;text-shadow:0 0 40px #4a6aff55}}
"""

CHECK = """() => {
  const boxes = [];
  document.querySelectorAll('img.pn').forEach(im => {
    if (!im.dataset.faces) return;
    const r = im.getBoundingClientRect(), b = 4;
    const dw = r.width - 2*b, dh = r.height - 2*b, nw = im.naturalWidth, nh = im.naturalHeight;
    const s = Math.max(dw/nw, dh/nh), ox = (dw - nw*s)/2, oy = (dh - nh*s)/2;
    im.dataset.faces.split(';').forEach(f => { const [x0,y0,x1,y1] = f.split(',').map(Number);
      const L=r.left, T=r.top+scrollY, R=r.right, B=r.bottom+scrollY;
      boxes.push({name: im.dataset.name, x0: Math.max(L, r.left+b+ox+x0*s), y0: Math.max(T, r.top+scrollY+b+oy+y0*s), x1: Math.min(R, r.left+b+ox+x1*s), y1: Math.min(B, r.top+scrollY+b+oy+y1*s)}); });
  });
  const bad = [], txt = [];
  document.querySelectorAll('.txt').forEach(e => {
    const r = e.getBoundingClientRect(); const t = {x0:r.left, y0:r.top+scrollY, x1:r.right, y1:r.bottom+scrollY};
    txt.push(t);
    if (t.x0 < 0 || t.x1 > 1080) bad.push('OFF-PAGE: ' + e.textContent.slice(0,40));
    boxes.forEach(f => { if (t.x0 < f.x1 && t.x1 > f.x0 && t.y0 < f.y1 && t.y1 > f.y0)
      bad.push('FACE ' + f.name + ': ' + e.textContent.slice(0,40)); });
  });
  const els=[...document.querySelectorAll('.txt')];
  for (let i=0;i<els.length;i++) for (let j=i+1;j<els.length;j++) {
    const a=els[i].getBoundingClientRect(), c=els[j].getBoundingClientRect();
    if (a.left < c.right-6 && a.right > c.left+6 && a.top < c.bottom-6 && a.bottom > c.top+6)
      bad.push('TEXT OVERLAP: ' + els[i].textContent.slice(0,25) + ' / ' + els[j].textContent.slice(0,25));
  }
  return {bad, faces: boxes, txt};
}"""

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    open(f"{OUT}/strip.html", "w", encoding="utf-8").write(f"<html><head><meta charset=\"utf-8\"><style>{css}</style></head><body>{body}</body></html>")
    pg.goto(uri(Path(OUT, "strip.html")))
    pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(500)
    chk = pg.evaluate(CHECK)
    anchors = pg.evaluate("""() => { const o={}; document.querySelectorAll('[data-a]').forEach(e=>{const a=e.dataset.a; if(!a) return;
        const r=e.getBoundingClientRect(); o[a]={top:r.top+scrollY, h:r.height}}); o._H=document.body.scrollHeight; return o; }""")
    pg.screenshot(path=f"{OUT}/strip.png", full_page=True)
    b.close()
json.dump(anchors, open(f"{OUT}/anchors.json", "w"), indent=1)
json.dump(chk, open(f"{OUT}/facecheck.json", "w"), indent=1)
print("height", anchors["_H"], "| text elements", len(chk["txt"]), "| face boxes", len(chk["faces"]))
print("OVERLAPS:", chk["bad"] or "none")
