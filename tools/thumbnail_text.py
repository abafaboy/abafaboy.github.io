#!/usr/bin/env python3
"""thumbnail_text: turn Codex key art (thumbnails_v2/T1_*.png, 1536x1024) into a YouTube thumbnail with recap-style words.

- Crops the art to 16:9 through the middle (or at --crop, 0 = top, 1 = bottom), renders at 1280x720.
- One big outlined word (Anton, SIL Open Font License: free for any use, unlike the Blambot lettering font) in the
  calm top-left area, an optional second word, an optional tag badge (e.g. "1-33") and an optional arrow to a point.
- Saves PNG; if that is over YouTube's 2 MB thumbnail limit, saves the highest JPEG quality that fits instead.

usage: thumbnail_text.py ART.png OUT_BASENAME --word OPERATOR [--word2 "F-RANK BAIT"] [--tag "1-33"]
                         [--arrow 0.40,0.30,0.62,0.55] [--crop 0.5] [--color "#FFE14D"]
"""
import argparse
import json
import base64
import io
import tempfile
from pathlib import Path

from PIL import Image

FONTS = Path("/home/claude/msgf-tools/fontpkgs/node_modules/@fontsource")
W, H = 1280, 720
LIMIT = 2 * 1024 * 1024


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("art")
    ap.add_argument("out", help="output path without extension")
    ap.add_argument("--word", default="")
    ap.add_argument("--layout", default="", help="JSON: {crop, labels:[{text,x,y,size,color,rot,stroke}], arrows:[[x1,y1,x2,y2,color]], tag}")
    ap.add_argument("--word2", default="")
    ap.add_argument("--tag", default="")
    ap.add_argument("--arrow", default="", help="x1,y1,x2,y2 as fractions of the thumbnail")
    ap.add_argument("--crop", type=float, default=0.5)
    ap.add_argument("--color", default="#FFE14D")
    ap.add_argument("--size", type=int, default=170, help="big word size in px")
    A = ap.parse_args()
    LAY = json.loads(Path(A.layout).read_text()) if A.layout else {}
    if "crop" in LAY:
        A.crop = float(LAY["crop"])
    if LAY.get("tag"):
        A.tag = LAY["tag"]

    im = Image.open(A.art).convert("RGB")
    w, h = im.size
    ch = round(w * 9 / 16)
    if ch > h:  # wider than 16:9 art: crop the sides instead
        cw = round(h * 16 / 9)
        x0 = (w - cw) // 2
        im = im.crop((x0, 0, x0 + cw, h))
    else:
        y0 = round((h - ch) * min(max(A.crop, 0.0), 1.0))
        im = im.crop((0, y0, w, y0 + ch))
    im = im.resize((W, H), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "PNG")
    bg = base64.b64encode(buf.getvalue()).decode()

    arrow = ""
    arrows = [list(map(float, A.arrow.split(","))) + [A.color]] if A.arrow else []
    arrows += [a[:4] + [a[4] if len(a) > 4 else A.color] for a in LAY.get("arrows", [])]
    for n_, (x1, y1, x2, y2, acol) in enumerate(arrows):
        X1, Y1, X2, Y2 = x1 * W, y1 * H, x2 * W, y2 * H
        bend = 60 if X2 >= X1 else -60
        arrow += f"""<svg width="{W}" height="{H}" style="position:absolute;left:0;top:0">
<defs><marker id="h{n_}" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="4.2" markerHeight="4.2" orient="auto-start-reverse">
<path d="M0,0 L10,5 L0,10 z" fill="{acol}" stroke="#000" stroke-width="1.2"/></marker></defs>
<path d="M{X1:.0f},{Y1:.0f} Q{(X1 + X2) / 2 + bend:.0f},{(Y1 + Y2) / 2 - 60:.0f} {X2:.0f},{Y2:.0f}" fill="none" stroke="#000" stroke-width="30" stroke-linecap="round"/>
<path d="M{X1:.0f},{Y1:.0f} Q{(X1 + X2) / 2 + bend:.0f},{(Y1 + Y2) / 2 - 60:.0f} {X2:.0f},{Y2:.0f}" fill="none" stroke="{acol}" stroke-width="18" stroke-linecap="round" marker-end="url(#h{n_})"/>
</svg>"""
    labels = "".join(
        f'<div class="lab" style="left:{l["x"] * W:.0f}px;top:{l["y"] * H:.0f}px;font-size:{l.get("size", 120)}px;color:{l.get("color", A.color)};'
        f'-webkit-text-stroke:{l.get("stroke", 14)}px #000;transform:translate(-50%,0) rotate({l.get("rot", -4)}deg)">{l["text"]}</div>'
        for l in LAY.get("labels", []))
    anton = (FONTS / "anton/files/anton-latin-400-normal.woff2").as_uri()
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Big';src:url('{anton}') format('woff2')}}
html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:#000}}
.bg{{position:absolute;inset:0;background:url(data:image/png;base64,{bg}) center/cover no-repeat}}
.word{{position:absolute;left:44px;top:34px;font:{A.size}px/0.92 'Big';color:{A.color};letter-spacing:1px;
  -webkit-text-stroke:16px #000;paint-order:stroke fill;transform:rotate(-4deg);transform-origin:left top;
  filter:drop-shadow(0 8px 0 rgba(0,0,0,.85))}}
.word2{{position:absolute;left:52px;top:{34 + int(A.size * 0.95)}px;font:{int(A.size * 0.48)}px/1 'Big';color:#fff;
  -webkit-text-stroke:10px #000;paint-order:stroke fill;transform:rotate(-4deg);transform-origin:left top;
  filter:drop-shadow(0 5px 0 rgba(0,0,0,.85))}}
.lab{{position:absolute;font-family:'Big';line-height:.92;letter-spacing:1px;white-space:nowrap;paint-order:stroke fill;
  transform-origin:center top;filter:drop-shadow(0 7px 0 rgba(0,0,0,.85))}}
.tag{{position:absolute;right:34px;top:30px;font:64px/1 'Big';color:#fff;background:#E0262B;padding:10px 22px 14px;
  border:6px solid #000;border-radius:14px;transform:rotate(3deg);box-shadow:0 7px 0 rgba(0,0,0,.85)}}
</style></head><body><div class="bg"></div>{arrow}
{f'<div class="word">{A.word}</div>' if A.word else ''}{f'<div class="word2">{A.word2}</div>' if A.word2 else ''}{labels}{f'<div class="tag">{A.tag}</div>' if A.tag else ''}
</body></html>"""
    from playwright.sync_api import sync_playwright
    with tempfile.TemporaryDirectory() as td:
        page_file = Path(td) / "thumb.html"
        page_file.write_text(html, encoding="utf-8")
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
            pg.goto(page_file.as_uri())
            pg.evaluate("document.fonts.ready")
            png = pg.screenshot(type="png")
            b.close()
    out = Path(A.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    if len(png) <= LIMIT:
        out.with_suffix(".png").write_bytes(png)
        print("saved", out.with_suffix(".png"), len(png), "bytes")
        return
    img = Image.open(io.BytesIO(png)).convert("RGB")
    for q in range(97, 79, -1):
        jb = io.BytesIO()
        img.save(jb, "JPEG", quality=q, subsampling=0, optimize=True)
        if jb.tell() <= LIMIT:
            out.with_suffix(".jpg").write_bytes(jb.getvalue())
            print("saved", out.with_suffix(".jpg"), jb.tell(), "bytes, JPEG quality", q, "(PNG was over 2 MB)")
            return
    raise SystemExit("could not fit 2 MB")


if __name__ == "__main__":
    main()
