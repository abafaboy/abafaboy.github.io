#!/usr/bin/env python3
"""thumb_compose: build a 1280x720 YouTube thumbnail from layered art + words (HTML/CSS rendered by Chromium).

spec JSON:
{
  "bg": "#000",
  "layers": [
    {"img": "path.png", "x": 0, "y": 0, "w": 1280,            # placed image (h follows aspect unless "h")
     "filter": "saturate(.5)", "clip": "polygon(...)", "opacity": 1, "blend": "normal", "mirror": false},
    {"html": "<div ...>...</div>"},                             # raw HTML/SVG overlay (absolute positioned by you)
    {"text": "F-RANK", "x": 40, "y": 30, "size": 150, "font": "Anton", "color": "#fff",
     "grad": ["#fff", "#9aa"], "stroke": 16, "rot": -4, "glow": "#ff2a2a", "anchor": "left|center|right",
     "shadow": 8, "spacing": 1}
  ]
}
Fonts available: Anton, Bangers, Luckiest Guy, Oswald, Barlow Condensed, Permanent Marker (SIL OFL, free to use).
Saves PNG, or the best JPEG under YouTube's 2 MB limit.
usage: thumb_compose.py spec.json OUT_BASENAME [--small]   (--small also writes a 320x180 and 168x94 preview sheet)
"""
import base64
import io
import json
import sys
import tempfile
from pathlib import Path

from PIL import Image

FS = Path("/home/claude/msgf-tools/fontpkgs/node_modules/@fontsource")
FONTS = {
    "Anton": FS / "anton/files/anton-latin-400-normal.woff2",
    "Bangers": FS / "bangers/files/bangers-latin-400-normal.woff2",
    "Luckiest Guy": FS / "luckiest-guy/files/luckiest-guy-latin-400-normal.woff2",
    "Oswald": FS / "oswald/files/oswald-latin-700-normal.woff2",
    "Barlow Condensed": FS / "barlow-condensed/files/barlow-condensed-latin-800-normal.woff2",
    "Permanent Marker": FS / "permanent-marker/files/permanent-marker-latin-400-normal.woff2",
}
W, H = 1280, 720
LIMIT = 2 * 1024 * 1024


def data_uri(path):
    im = Image.open(path).convert("RGB")
    b = io.BytesIO()
    im.save(b, "PNG")
    return "data:image/png;base64," + base64.b64encode(b.getvalue()).decode(), im.size


def text_html(t):
    size = t.get("size", 120)
    font = t.get("font", "Anton")
    stroke = t.get("stroke", 14)
    rot = t.get("rot", 0)
    anchor = t.get("anchor", "left")
    tx = {"left": "0", "center": "-50%", "right": "-100%"}[anchor]
    fill = f"color:{t.get('color', '#FFE14D')};"
    if t.get("grad"):
        g = ",".join(t["grad"])
        fill = (f"background:linear-gradient(180deg,{g});-webkit-background-clip:text;background-clip:text;"
                f"color:transparent;")
    shadow = t.get("shadow", 8)
    glow = t.get("glow")
    filt = f"drop-shadow(0 {shadow}px 0 rgba(0,0,0,.9))"
    if glow:
        filt += f" drop-shadow(0 0 {t.get('glow_r', 18)}px {glow})"
    lh = t.get("lh", 0.92)
    spacing = t.get("spacing", 1)
    # stroke layer underneath (a gradient-clipped fill cannot carry its own outside stroke), fill layer on top
    common = (f"position:absolute;left:{t['x']}px;top:{t['y']}px;font-family:'{font}';font-size:{size}px;"
              f"line-height:{lh};letter-spacing:{spacing}px;white-space:pre;text-align:{t.get('align', 'left')};"
              f"transform:translate({tx},0) rotate({rot}deg);transform-origin:{anchor} top;")
    under = (f'<div style="{common}color:#000;-webkit-text-stroke:{stroke * 2}px #000;filter:{filt}">{t["text"]}</div>')
    over = f'<div style="{common}{fill}">{t["text"]}</div>'
    extra = t.get("inner_stroke")
    if extra:  # a thin coloured keyline just inside the black stroke
        over = (f'<div style="{common}color:transparent;-webkit-text-stroke:{extra[1]}px {extra[0]}">{t["text"]}</div>' + over)
    return under + over


def build(spec):
    parts = []
    for L in spec["layers"]:
        if "img" in L:
            uri, (iw, ih) = data_uri(L["img"])
            w = L.get("w", iw)
            h = L.get("h", round(w * ih / iw))
            st = (f"position:absolute;left:{L.get('x', 0)}px;top:{L.get('y', 0)}px;width:{w}px;height:{h}px;"
                  f"opacity:{L.get('opacity', 1)};mix-blend-mode:{L.get('blend', 'normal')};")
            if L.get("filter"):
                st += f"filter:{L['filter']};"
            if L.get("mirror"):
                st += "transform:scaleX(-1);"
            img = f'<img src="{uri}" style="{st}">'
            if L.get("clip"):
                img = f'<div style="position:absolute;inset:0;clip-path:{L["clip"]}">{img}</div>'
            parts.append(img)
        elif "html" in L:
            parts.append(L["html"])
        elif "text" in L:
            parts.append(text_html(L))
    faces = "".join(f"@font-face{{font-family:'{k}';src:url('{v.as_uri()}') format('woff2')}}" for k, v in FONTS.items() if v.exists())
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{faces}
html,body{{margin:0;width:{W}px;height:{H}px;overflow:hidden;background:{spec.get('bg', '#000')}}}
div,img{{box-sizing:border-box}}
</style></head><body>{''.join(parts)}</body></html>"""


def render(html):
    from playwright.sync_api import sync_playwright
    with tempfile.TemporaryDirectory() as td:
        f = Path(td) / "t.html"
        f.write_text(html, encoding="utf-8")
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
            pg.goto(f.as_uri())
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(150)
            png = pg.screenshot(type="png")
            b.close()
    return png


def save(png, out):
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    if len(png) <= LIMIT:
        out.with_suffix(".png").write_bytes(png)
        return out.with_suffix(".png")
    img = Image.open(io.BytesIO(png)).convert("RGB")
    for q in range(97, 79, -1):
        jb = io.BytesIO()
        img.save(jb, "JPEG", quality=q, subsampling=0, optimize=True)
        if jb.tell() <= LIMIT:
            out.with_suffix(".jpg").write_bytes(jb.getvalue())
            return out.with_suffix(".jpg")
    raise SystemExit("could not fit 2 MB")


if __name__ == "__main__":
    spec = json.loads(Path(sys.argv[1]).read_text())
    png = render(build(spec))
    p = save(png, sys.argv[2])
    print("saved", p, p.stat().st_size)
