#!/usr/bin/env python3
"""autostrip2: chapter YAML + panel art + the Codex UI kit become a lettered vertical webtoon strip.

Format: msgf-bible/SCRIPT_FORMAT.md. Kit: Codex's kit/ folder (bubbles, system, phone), read by kitlib.py.

How it letters:
- Bubbles use the Codex blanks: the best-fitting aspect is chosen for each line, scaled to the measured text,
  with tails drawn as SVG. Each tail joins the bitmap's outline by reading its outline radius per degree,
  and points at the speaker's side of the panel (`side: l|c|r`).
- Dialogue sits in the white gutters, straddling the panel edge. Insets and narrow panels get a column
  of bubbles beside them.
- System windows (`ui: system.*`, `on: float`) use the kit blanks, float over the art in perspective,
  and their text is fitted into the kit's text boxes.
- Phone screens (`on: screen`) are rendered from the kit app blanks (or HTML in the kit palette) and
  perspective-warped into the art's #00FF00 screen; fingers stay on top. `on: panel` puts app chrome over the panel.
- SFX are hand-lettered with per-letter jitter. Title and end cards are built in.

Outputs (OUT_DIR): strip.png, NNN.webp segments, layout.json (voiced lines with y positions, panels, segments, warnings).

Image quality (owner, 25 October: "make sure no images look compressed ever in the manhwa"):
- the strip is rendered at --dpr (default 2): a 1080 px layout becomes a 2160 px wide strip, so a 1440p video
  downscales it instead of upscaling it, and lettering stays sharp;
- strip.png is lossless; the NNN.webp segments are LOSSLESS WebP (never lossy);
- layout.json keeps every coordinate in layout (CSS) px and records "scale" (= dpr) for the strip image;
- art that arrives as JPEG or lossy WebP is flagged in the warnings: panel art must be PNG;
- every panel image is enlarged 2x with Real-ESRGAN (upscale_art.py) before layout, so the browser only ever
  shrinks art: a 1024 px tall panel fills 2160 px of strip without the soft, stretched look of a plain resize.

usage: autostrip2.py chNNN.yaml ART_DIR OUT_DIR [--kit KIT_DIR] [--placeholders] [--only P01-P20]
"""
import argparse
import html
import json
import math
import random
import re
from pathlib import Path

import cv2
import numpy as np
import yaml
from PIL import Image, ImageDraw, ImageFont
from playwright.sync_api import sync_playwright

import kitlib

Image.MAX_IMAGE_PIXELS = None
HERE = Path(__file__).resolve().parent
FP = HERE / "fontpkgs/node_modules/@fontsource"
E = html.escape
LINE = "#2B2523"


def uri(p):
    return Path(p).resolve().as_uri()


def lossy_image(p):
    """True for JPEG files and lossy WebP files (lossless WebP carries a VP8L chunk)."""
    suf = Path(p).suffix.lower()
    if suf in (".jpg", ".jpeg"):
        return True
    if suf == ".webp":
        with open(p, "rb") as fh:
            head = fh.read(4096)
        return b"VP8L" not in head
    return False


# ----------------------------------------------------------------------------------------------- script loading
def _fix_keys(o):
    """YAML 1.1 reads the key `on:` as True. Restore it (and `off:`)."""
    if isinstance(o, dict):
        out = {}
        for k, v in o.items():
            if k is True:
                k = "on"
            elif k is False:
                k = "off"
            out[k] = _fix_keys(v)
        return out
    if isinstance(o, list):
        return [_fix_keys(x) for x in o]
    return o


def load_script(path):
    return _fix_keys(yaml.safe_load(open(path, encoding="utf-8")))


# ----------------------------------------------------------------------------------------------- config
SHAPES = {  # final width, height (None = from art aspect), alignment, frame style
    "full": (1080, None, "c", "framed"),
    "wide": (1000, 667, "c", "framed"),
    "strip": (1000, 333, "c", "framed"),
    "tall": (1080, 1620, "c", "framed"),
    "bleed": (1080, 1620, "c", "bleed"),
    "inset-l": (600, 600, "l", "framed"),
    "inset-r": (600, 600, "r", "framed"),
    "narrow-l": (380, 760, "l", "framed"),
    "narrow-r": (380, 760, "r", "framed"),
    "vignette": (1080, 720, "c", "vig"),
}
GAPS = {"none": 28, "short": 84, "long": 380, "black": 640, "fade-black": 520, "fade-white": 520}
BGS = {"white": "#ffffff", "black": "#0a0a0d", "navy": "#0b1530", "paper": "#f6f3ec"}
# lettering: family, weight, size px, line height, colour
TYPE_FONT = {
    "speech": ("Letter", 600, 31, 1.16, "#1d1917"),
    "nervous": ("Letter", 600, 30, 1.16, "#1d1917"),
    "thought": ("Letter", 600, 30, 1.16, "#1d1917"),
    "whisper": ("Letter", 600, 26, 1.16, "#3a3430"),
    "shout": ("Letter", 800, 40, 1.04, "#1d1917"),
    "intense": ("Letter", 800, 34, 1.10, "#1d1917"),
    "menace": ("Letter", 600, 31, 1.16, "#f4f1ec"),
    "monster": ("Letter", 800, 32, 1.12, "#e2484c"),
    "phone": ("Letter", 600, 29, 1.16, "#1d1917"),
    "announce": ("Letter", 700, 30, 1.12, "#1d1917"),
}
BITMAP_TYPES = set(TYPE_FONT)
VOICED = BITMAP_TYPES | {"float", "narr", "narr_dark", "inner", "note", "link"}  # inner: Jaeha's inner voice; note: his notebook; link: an order sent down the Link (what the summon hears)
MIN_BUBBLE = {"shout": (230, 150), "intense": (240, 180)}
WIDTH_CANDS = list(range(140, 581, 30))
SYS_WFRAC = {"notice": .80, "notice_small": .62, "window": .66, "summon_card": .44, "warning": .80,
             "log": .44, "glitch": .66, "button": .40}


def bg_hex(bg):
    if not bg or str(bg).startswith("gradient:"):
        return BGS["white"]
    return BGS.get(bg, bg)


def is_dark(bg):
    h = bg_hex(bg).lstrip("#")
    if len(h) == 6:
        r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
        return (0.299 * r + 0.587 * g + 0.114 * b) < 90
    return False


def fmt_text(t):
    s = E(str(t))
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    return s.replace("\n", "<br>")


def tokenize(text):
    """Words of a line as (word, bold, hard_break_before)."""
    toks = []
    for li, hard in enumerate(str(text).split("\n")):
        first = True
        for m in re.finditer(r"\*\*(.+?)\*\*|(\S+)", hard):
            words = m.group(1).split() if m.group(1) else [m.group(2)]
            for w in words:
                toks.append((w, bool(m.group(1)), li > 0 and first))
                first = False
    return toks


def word_html(tok):
    w = E(tok[0])
    return f"<b>{w}</b>" if tok[1] else w


def measure_html(toks):
    out = []
    for k, t in enumerate(toks):
        if t[2]:
            out.append("<br>")
        elif k:
            out.append(" ")
        out.append(f'<span class="w" data-k="{k}">{word_html(t)}</span>')
    return "".join(out)


def lines_html(toks, lines):
    return "<br>".join("&nbsp;".join(word_html(toks[k]) for k in ln) for ln in lines)


# ----------------------------------------------------------------------------------------------- fonts
def _ff(fam, pkg, file, weight=400, style="normal"):
    return f"@font-face{{font-family:'{fam}';src:url('{uri(FP / pkg / 'files' / file)}');font-weight:{weight};font-style:{style}}}"


FONTS = "\n".join([
    _ff("Letter", "shantell-sans", "shantell-sans-latin-600-normal.woff2", 600),
    _ff("Letter", "shantell-sans", "shantell-sans-latin-700-normal.woff2", 700),
    _ff("Letter", "shantell-sans", "shantell-sans-latin-800-normal.woff2", 800),
    _ff("Letter", "shantell-sans", "shantell-sans-latin-600-italic.woff2", 600, "italic"),
    _ff("Letter", "shantell-sans", "shantell-sans-latin-800-italic.woff2", 800, "italic"),
    _ff("LetterSoft", "shantell-sans", "shantell-sans-latin-500-normal.woff2", 500),
    _ff("LetterSoft", "shantell-sans", "shantell-sans-latin-500-italic.woff2", 500, "italic"),
    _ff("Impact", "luckiest-guy", "luckiest-guy-latin-400-normal.woff2", 400),
    _ff("Bang", "bangers", "bangers-latin-400-normal.woff2", 400),
    _ff("Marker", "permanent-marker", "permanent-marker-latin-400-normal.woff2", 400),
    _ff("UI", "barlow-condensed", "barlow-condensed-latin-500-normal.woff2", 500),
    _ff("UI", "barlow-condensed", "barlow-condensed-latin-600-normal.woff2", 600),
    _ff("UI", "barlow-condensed", "barlow-condensed-latin-700-normal.woff2", 700),
    _ff("UI", "barlow-condensed", "barlow-condensed-latin-700-italic.woff2", 700, "italic"),
    _ff("Mono", "share-tech-mono", "share-tech-mono-latin-400-normal.woff2", 400),
    _ff("Pencil", "patrick-hand", "patrick-hand-latin-400-normal.woff2", 400),
    _ff("App", "ibm-plex-sans-kr", "ibm-plex-sans-kr-latin-500-normal.woff2", 500),
    _ff("App", "ibm-plex-sans-kr", "ibm-plex-sans-kr-latin-700-normal.woff2", 700),
    _ff("App", "ibm-plex-sans-kr", "ibm-plex-sans-kr-korean-500-normal.woff2", 500),
    _ff("App", "ibm-plex-sans-kr", "ibm-plex-sans-kr-korean-700-normal.woff2", 700),
])
FONT_LINKS = f'<link rel="stylesheet" href="{uri(FP / "gaegu" / "700.css")}">'


# ----------------------------------------------------------------------------------------------- art helpers
def placeholder(pid, shape, art_text, path, chibi=False):
    w, h = {"tall": (1024, 1536), "bleed": (1024, 1536), "narrow-l": (1024, 1536), "narrow-r": (1024, 1536),
            "inset-l": (1024, 1024), "inset-r": (1024, 1024)}.get(shape, (1536, 1024))
    rnd = random.Random(pid)
    base = (rnd.randint(150, 196), rnd.randint(152, 196), rnd.randint(160, 206))
    if chibi:
        base = (238, 226, 190)
    im = Image.new("RGB", (w, h), base)
    d = ImageDraw.Draw(im)
    for i in range(0, w + h, 56):
        d.line([(i, 0), (i - h, h)], fill=tuple(c - 10 for c in base), width=12)
    if "screen: green" in (art_text or "").lower():
        cx, cy = int(w * 0.55), h // 2
        pw = int(min(w, h) * 0.30)
        ph = int(pw * 1.9) if h >= w * 0.9 else int(h * 0.62)
        pw = min(pw, int(ph / 1.6))
        quad = [(cx - pw // 2 + 26, cy - ph // 2), (cx + pw // 2 + 26, cy - ph // 2 + 18),
                (cx + pw // 2 - 8, cy + ph // 2), (cx - pw // 2 - 18, cy + ph // 2 - 10)]
        bez = [(quad[0][0] - 16, quad[0][1] - 16), (quad[1][0] + 16, quad[1][1] - 16),
               (quad[2][0] + 16, quad[2][1] + 16), (quad[3][0] - 16, quad[3][1] + 16)]
        d.polygon(bez, fill=(38, 38, 42))
        d.polygon(quad, fill=(0, 255, 0))
        d.ellipse([quad[3][0] + 20, quad[3][1] - 120, quad[3][0] + 120, quad[3][1] + 40], fill=(214, 170, 140))  # a thumb
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 60)
    except Exception:
        f = None
    d.text((40, 30), f"{pid} · {shape}{' · chibi' if chibi else ''}", fill=(70, 70, 82), font=f)
    im.save(path)


def find_green(img_bgr):
    """The art's chroma screen: near-pure #00FF00 (Codex snaps screens to it). Bright green clothing
    (Yerin's cuffs and stripe, mint glows) is not a screen: the core must be strongly saturated, and the
    looser edge pixels join the mask only where they touch that core (27 Oct: the old loose test painted
    the highlight on Yerin's green cuff dark in ch002 P37 and P43)."""
    b, g, r = (img_bgr[:, :, i].astype(np.int32) for i in range(3))
    # 28 Oct: bright off-pure greens count (ch005 P17's phone, ch006 P57's monitor, ch007 P19's phone; the upscaler
    # also lifts red and blue a little); g - max(r, b) >= 130 still keeps mint cuffs and glows out (checked over every
    # panel of chapters 1-10: only those screens change)
    core = ((g >= 200) & (g - np.maximum(r, b) >= 130)).astype(np.uint8) * 255
    core = cv2.morphologyEx(core, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    if cv2.countNonZero(core) < 900:
        return None, None
    loose = ((g > 140) & (g - np.maximum(r, b) > 70)).astype(np.uint8) * 255
    near = cv2.dilate(core, np.ones((9, 9), np.uint8))
    mask = cv2.bitwise_or(core, cv2.bitwise_and(loose, near))
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
    cnts, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if not cnts:
        return None, None
    c = max(cnts, key=cv2.contourArea)
    if cv2.contourArea(c) < 900:
        return None, None
    keep = np.zeros_like(mask)
    cv2.drawContours(keep, [c], -1, 255, -1)
    mask = cv2.bitwise_and(mask, keep)
    hull = cv2.convexHull(c)
    quad = None
    peri = cv2.arcLength(hull, True)
    for eps in (0.01, 0.02, 0.03, 0.05, 0.08, 0.12):
        a = cv2.approxPolyDP(hull, eps * peri, True)
        if len(a) == 4:
            quad = a.reshape(4, 2).astype(np.float32)
            break
    if quad is None:
        quad = cv2.boxPoints(cv2.minAreaRect(hull)).astype(np.float32)
    s = quad.sum(1)
    d = np.diff(quad, axis=1).ravel()
    tl, br = quad[np.argmin(s)], quad[np.argmax(s)]
    tr, bl = quad[np.argmin(d)], quad[np.argmax(d)]
    return np.array([tl, tr, br, bl], np.float32), mask


def quad_size(q):
    w = max(np.linalg.norm(q[1] - q[0]), np.linalg.norm(q[2] - q[3]))
    h = max(np.linalg.norm(q[3] - q[0]), np.linalg.norm(q[2] - q[1]))
    return w, h


def composite_screen(img_bgr, quad, mask, ui_rgba):
    """Warp ui_rgba (H×W×4) into quad; only where mask (screen pixels) is set."""
    h, w = ui_rgba.shape[:2]
    src = np.array([[0, 0], [w - 1, 0], [w - 1, h - 1], [0, h - 1]], np.float32)
    M = cv2.getPerspectiveTransform(src, quad)
    H, W = img_bgr.shape[:2]
    warped = cv2.warpPerspective(ui_rgba, M, (W, H), flags=cv2.INTER_LANCZOS4, borderValue=(0, 0, 0, 0))
    region = cv2.dilate(mask, np.ones((3, 3), np.uint8))
    soft = cv2.GaussianBlur(region, (3, 3), 0).astype(np.float32) / 255.0
    a = (warped[:, :, 3].astype(np.float32) / 255.0)
    screen = warped[:, :, :3].astype(np.float32) * a[..., None] + np.array([28, 26, 30], np.float32) * (1 - a[..., None])
    out = img_bgr.astype(np.float32) * (1 - soft[..., None]) + screen * soft[..., None]
    out = np.clip(out, 0, 255).astype(np.uint8)
    halo = (cv2.dilate(region, np.ones((7, 7), np.uint8)) > 0) & (region == 0)
    g = out[:, :, 1].astype(np.int32)
    lim = np.maximum(out[:, :, 0], out[:, :, 2]).astype(np.int32)
    fix = halo & (g > lim + 8)
    out[:, :, 1][fix] = (lim[fix] + 8).clip(0, 255).astype(np.uint8)
    return out


# ----------------------------------------------------------------------------------------------- app screens
APP_BASE_CSS = f"""{FONTS}
*{{box-sizing:border-box}} html,body{{margin:0;background:transparent;overflow:hidden}}
.app{{position:relative;overflow:hidden;font-family:'App',sans-serif;color:#302C45}}
.tb{{position:absolute;display:flex;align-items:center;line-height:1.18;font-family:'App',sans-serif}}
.tb.nw span{{white-space:nowrap}}
"""
FIT_JS = r"""
() => {
  document.querySelectorAll('.tb,.stx').forEach(el => {
    const sp = el.firstElementChild; if (!sp) return;
    const W = el.clientWidth, H = el.clientHeight;
    let fs = parseFloat(getComputedStyle(sp).fontSize), g = 0;
    while ((sp.scrollWidth > W + 1 || sp.offsetHeight > H + 2) && fs > 7 && g++ < 80) { fs *= 0.95; sp.style.fontSize = fs + 'px'; }
  });
  return true;
}
"""


def load_html(page, html_text, path):
    """Load HTML from a file:// URL so local images and fonts are allowed (set_content pages block file:// loads)."""
    Path(path).write_text(html_text, encoding="utf-8")
    page.goto(uri(path), wait_until="load")
    page.evaluate("document.fonts.ready")


# the video area of a kit app blank that can show another panel's footage (x, y, w, h in the blank's pixels)
KIT_VIDEO = {"phone.live_stream": (45, 174, 946, 603)}


def kit_app_html(png, meta, fills, video=None):
    W, H = meta["size"]
    boxes = []
    if video:  # (image path, (x, y, w, h)): the footage under the app's chrome text, above the blank
        vp, (vx, vy, vw, vh) = video
        boxes.append(f"<img src='{uri(vp)}' style='position:absolute;left:{vx}px;top:{vy}px;width:{vw}px;height:{vh}px;object-fit:cover'>")
        # the blank's chrome that sits inside the video area is drawn again on top of the footage: the viewer pill and a
        # red LIVE badge
        boxes.append("<div style='position:absolute;left:843px;top:206px;width:127px;height:45px;border-radius:23px;background:#fff'></div>"
                     "<div style='position:absolute;left:70px;top:206px;padding:0 16px;height:45px;border-radius:8px;background:#E5484D;"
                     "color:#fff;font:700 24px/45px UI,sans-serif;letter-spacing:.08em'>&#9679; LIVE</div>")
    for b in meta.get("text_boxes", []):
        v = fills.get(b["id"])
        if v in (None, ""):
            continue
        x, y, bw, bh = b["rect"]
        fs = b.get("sample_size") or bh * 0.6
        weight = 700 if b.get("font_kind") == "bold" else 500
        align = b.get("align", "left")
        jc = {"left": "flex-start", "center": "center", "right": "flex-end"}.get(align, "flex-start")
        nw = " nw" if b.get("max_lines", 1) == 1 else ""
        boxes.append(f'<div class="tb{nw}" style="left:{x}px;top:{y}px;width:{bw}px;height:{bh}px;justify-content:{jc};'
                     f'text-align:{align};color:{b.get("color", "#302C45")};font-weight:{weight}"><span style="font-size:{fs}px">{fmt_text(v)}</span></div>')
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{APP_BASE_CSS}</style></head>"
            f"<body style='width:{W}px;height:{H}px'><div class='app' style='width:{W}px;height:{H}px'>"
            f"<img src='{uri(png)}' style='position:absolute;left:0;top:0;width:{W}px;height:{H}px'>{''.join(boxes)}</div></body></html>")


def app_fills(kind, u):
    clock = u.get("clock", "23:31")
    if kind == "phone.emergency_alert":
        return {"clock": u.get("clock", "19:52"), "heading": u.get("heading", "[Emergency Alert]"),
                "body": re.sub(r"^\[Emergency Alert\]\s*", "", u.get("text", ""))}
    if kind == "phone.bank_transfer":
        return {"clock": u.get("clock", "22:41"), "header": u.get("bank", "Saebom Bank"),
                "confirmation": u.get("confirmation", "Transfer sent"), "recipient": "To: " + u.get("to", ""),
                "amount": u.get("amount", ""), "balance": "Available balance\n" + u.get("balance", ""), "button": "Done"}
    if kind == "phone.gate_status":
        return {"clock": clock, "header": "Gate Safety Korea", "status": u.get("status", u.get("text", "")),
                "retained": u.get("retained", "")}
    if kind == "phone.ttok_call":
        return {"clock": clock, "header": "TTOK", "caller": u.get("caller", ""), "accept": "Accept", "decline": "Decline"}
    if kind == "phone.ttok_notification":
        return {"clock": clock, "app": "TTOK", "sender": u.get("sender", u.get("title", "")), "message": u.get("text", "")}
    if kind == "phone.ttok_video_call":
        return {"clock": clock, "caller": u.get("caller", ""), "duration": u.get("duration", "02:14")}
    parts = [x.strip() for x in str(u.get("text", "")).split("·") if x.strip()]
    if kind == "phone.quickhaul_order":
        timer = next((re.search(r"\d\d:\d\d(?::\d\d)?", x).group(0) for x in parts if re.search(r"\d\d:\d\d", x)), "00:00")
        pen = next((x for x in parts if "LATE" in x.upper()), "")
        dest = next((re.sub(r"\d\d:\d\d(?::\d\d)?", "", x).strip() for x in parts if x not in (pen,)), "")
        return {"clock": clock, "header": "QuickHaul", "timer": timer, "destination": dest or "NEXT STOP",
                "rating": u.get("rating", "4.1 · 2,310 deliveries"), "penalty": pen, "button": "Confirm delivery"}
    if kind == "phone.aao_booking":
        return {"clock": clock, "header": "Ability Assessment Office", "heading": u.get("heading", "Appointment booked"),
                "date": u.get("date", ""), "time": u.get("time", ""), "branch": u.get("branch", "MAPO BRANCH"), "button": "View appointment"}
    if kind == "phone.aao_result":
        return {"clock": clock, "header": "Ability Assessment Office", "heading": u.get("heading", "Assessment result"),
                "output": u.get("output", ""), "response": u.get("response", "")}
    if kind == "phone.hunterlink_rank":
        f = {"clock": clock, "header": "HunterLink", "heading": u.get("heading", "WEEKLY FAN RANKING"), "sponsor": u.get("sponsor", "")}
        for i, r in enumerate(u.get("ranks", [])[:3], 1):
            f.update({f"rank_{i}": str(i), f"name_{i}": r.get("name", ""), f"votes_{i}": r.get("votes", "")})
        return f
    if kind == "phone.live_stream":
        f = {"clock": clock, "header": "LIVE", "viewers": u.get("viewers", ""), "donation": u.get("donation", ""), "input": "Say something…"}
        for i, c in enumerate(u.get("chat", [])[:3], 1):
            f[f"chat_{i}"] = c
        return f
    return {}


def html_app(u, w, h):
    """HTML app screens for kinds without a kit blank (or with variable content), in the kit palettes."""
    k = u["kind"]
    V = lambda x: f"{x * w / 100.0:.1f}px"
    head = (f"<!doctype html><html><head><meta charset='utf-8'><style>{APP_BASE_CSS}"
            f".msg{{max-width:74%;padding:{V(2.8)} {V(4)};border-radius:{V(4.5)};font:500 {V(4.3)}/1.32 'App';margin:{V(2.2)} {V(4)}}}"
            f".row{{display:flex;align-items:flex-end;gap:{V(2)}}} .row.me{{justify-content:flex-end}}"
            f".t{{font:500 {V(2.8)}/1 'App';color:#8a8696;margin-bottom:{V(2.4)}}}"
            f"</style></head><body style='width:{w}px;height:{h}px'>")
    if k == "phone.ttok_chat":
        rows = []
        for m in u.get("messages", []):
            if m.get("from") == "me":
                rows.append(f'<div class="row me"><div class="t">{E(m.get("time", ""))}</div><div class="msg" style="background:#DDD4F4;color:#302C45">{fmt_text(m["text"])}</div></div>')
            else:
                rows.append(f'<div class="row"><div style="width:{V(9)};height:{V(9)};border-radius:50%;background:#C9C2DE;margin-left:{V(4)};flex:none"></div>'
                            f'<div class="msg" style="background:#fff;margin-left:0">{fmt_text(m["text"])}</div><div class="t">{E(m.get("time", ""))}</div></div>')
        body = (f'<div class="app" style="width:{w}px;height:{h}px;background:#F0EDF7">'
                f'<div style="background:#6556A8;color:#fff;padding:{V(3)} {V(5)} {V(3.4)}">'
                f'<div style="display:flex;justify-content:space-between;font:600 {V(3.4)}/1 UI">{E(u.get("clock", "23:32"))}<span>▮▮▮ 61%</span></div>'
                f'<div style="display:flex;align-items:center;gap:{V(3)};margin-top:{V(3.2)};font:700 {V(5.6)}/1 App">‹ {E(u.get("title", ""))}'
                f'<span style="margin-left:auto;font:700 {V(3.4)}/1 UI;letter-spacing:.14em;opacity:.85">TTOK</span></div></div>'
                f'<div style="display:flex;flex-direction:column;justify-content:flex-end;height:calc(100% - {V(34)})">'
                f'<div style="align-self:center;background:#DDD4F4;border-radius:99px;padding:{V(1)} {V(3.4)};font:500 {V(2.8)}/1.2 App;margin:{V(3)} 0">{E(u.get("date", "TUE 14 MAR"))}</div>'
                + "".join(rows) + "</div>"
                f'<div style="position:absolute;left:{V(4)};right:{V(4)};bottom:{V(5)};height:{V(10)};border-radius:99px;background:#fff;'
                f'font:500 {V(3.8)}/{V(10)} App;color:#a29db3;padding-left:{V(5)}">Message</div></div>')
    elif k == "phone.quickhaul_order":
        parts = [p.strip() for p in u.get("text", "").split("·")]
        big = next((p for p in parts if re.search(r"\d\d:\d\d", p)), "00:00")
        late = next((p for p in parts if "LATE" in p.upper()), "")
        body = (f'<div class="app" style="width:{w}px;height:{h}px;background:#14161C;color:#fff;padding:{V(7)}">'
                f'<div style="font:700 {V(6)}/1 UI;letter-spacing:.1em;color:#FFB020">QUICKHAUL</div>'
                f'<div style="font:600 {V(4.2)}/1 UI;color:#9aa0ad;margin-top:{V(7)}">NEXT STOP</div>'
                f'<div style="font:700 {V(19)}/1 UI;margin-top:{V(2)}">{E(re.sub("NEXT STOP", "", big).strip())}</div>'
                f'<div style="font:700 {V(8.5)}/1 UI;margin-top:{V(5)};color:#FF4D4D">{E(late)}</div>'
                f'<div style="position:absolute;left:{V(7)};right:{V(7)};bottom:{V(8)};height:{V(13)};border-radius:{V(3)};background:#FFB020;'
                f'color:#14161C;font:700 {V(5)}/{V(13)} UI;text-align:center;letter-spacing:.08em">DELIVERED</div></div>')
    elif k == "phone.gate_status":
        parts = [p.strip() for p in str(u.get("text", "")).split("·") if p.strip()]
        rows = "".join(
            f'<div class="tb" style="position:relative;width:100%;height:{V(15)};justify-content:center">'
            f'<span style="white-space:nowrap;font:800 {V(13)}/1 UI;letter-spacing:.02em;color:{"#C62828" if "PAID" in p_.upper() else "#1d2433"}">{E(p_)}</span></div>'
            for p_ in parts)
        body = (f'<div class="app" style="width:{w}px;height:{h}px;background:#F2F5FA;display:flex;flex-direction:column">'
                f'<div style="background:#1F4E9A;color:#fff;padding:{V(7)} {V(5)} {V(6)};font:700 {V(6.4)}/1.1 UI;letter-spacing:.06em;text-align:center">'
                f'{E(u.get("title", "GATE SAFETY KOREA"))}</div>'
                f'<div style="flex:1;display:flex;flex-direction:column;justify-content:space-evenly;padding:{V(5)} {V(6)}">{rows}</div></div>')
    elif k == "phone.sumex_ad":
        parts = [p.strip() for p in u.get("text", "").split("·")]
        body = (f'<div class="app" style="width:{w}px;height:{h}px;background:linear-gradient(160deg,#3b1d6e,#e0457b);color:#fff;'
                f'display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:{V(6)}">'
                f'<div style="font:700 {V(5)}/1 UI;letter-spacing:.24em;opacity:.85">SUMEX</div>'
                f'<div style="font:700 italic {V(10)}/1.0 UI;margin-top:{V(4)}">{E(parts[0] if parts else "")}</div>'
                + "".join(f'<div style="font:700 {V(6.4)}/1.1 UI;margin-top:{V(4)}">{E(p)}</div>' for p in parts[1:2])
                + "".join(f'<div style="margin-top:{V(5)};padding:{V(1.6)} {V(5)};border-radius:99px;background:#FFD54A;color:#3b1d6e;font:700 {V(5)}/1 UI">{E(p)} ✦</div>' for p in parts[2:3])
                + "</div>")
    elif k == "tv.lowerthird":
        bgc = "linear-gradient(135deg,#1d3557,#3a5a8c 55%,#22314f)" if u.get("on") == "screen" else "transparent"
        body = (f'<div class="app" style="width:{w}px;height:{h}px;background:{bgc}">'
                f'<div style="position:absolute;right:{V(3)};top:{V(3)};background:#C62828;color:#fff;font:700 {V(3.4)}/1 UI;padding:{V(1.2)} {V(2.4)};letter-spacing:.06em">KNN 24 · LIVE</div>'
                f'<div style="position:absolute;left:{V(4)};bottom:{V(9)};background:#fff;border-left:{V(1.4)} solid #C62828;padding:{V(1.6)} {V(3)};font:700 {V(4.2)}/1.1 UI;color:#111">{E(u.get("text", ""))}</div>'
                f'<div style="position:absolute;left:0;right:0;bottom:0;height:{V(6)};background:#C62828;color:#fff;font:600 {V(3)}/{V(6)} UI;padding-left:{V(4)};white-space:nowrap;overflow:hidden">{E(u.get("ticker", ""))}</div></div>')
    elif k == "pc.video_editor":
        # A desktop video editor: a preview of the footage (`source` panel's art, `subject` box), transport and a timeline.
        bg = u.get("_bg")
        ph = float(u.get("playhead", 0.62))
        clips = [(0.00, 0.18, "#E8458B"), (0.19, 0.41, "#3FB6C6"), (0.42, 0.57, "#E6C63F"), (0.58, 0.83, "#E8458B"), (0.84, 1.00, "#7C6CF0")]
        track = lambda y, cl, op: "".join(
            f'<div style="position:absolute;left:{V(4 + a * 92)};width:{V((b - a) * 92 - 0.4)};top:{V(y)};height:{V(4.2)};'
            f'border-radius:{V(0.5)};background:{c};opacity:{op}"></div>' for a, b, c in cl)
        wave = "".join(f'<div style="position:absolute;left:{V(4 + i * 0.92)};width:{V(0.5)};bottom:{V(6)};height:{V(1 + 3.2 * abs(((i * 37) % 23) / 23 - 0.5) * 2)};'
                       f'background:#5FD38D;opacity:.8"></div>' for i in range(100))
        body = (f'<div class="app" style="width:{w}px;height:{h}px;background:#16181d;color:#cfd3dc">'
                f'<div style="position:absolute;left:0;right:0;top:0;height:{V(4.6)};background:#22252c;display:flex;align-items:center;gap:{V(1.2)};padding-left:{V(1.6)};'
                f'font:600 {V(1.7)}/1 UI;letter-spacing:.06em">'
                + "".join(f'<span style="width:{V(1.1)};height:{V(1.1)};border-radius:50%;background:{c}"></span>' for c in ("#ff5f57", "#febc2e", "#28c840"))
                + f'<span style="margin-left:{V(1.4)}">{E(u.get("title", "BOMBOM TV · EDIT"))}</span></div>'
                f'<div style="position:absolute;left:{V(20)};right:{V(20)};top:{V(7)};height:{V(33.75)};background:#000 url(\'{uri(bg) if bg else ""}\') center/cover no-repeat;'
                f'border:{V(0.25)} solid #33363e"></div>'
                f'<div style="position:absolute;left:0;right:0;top:{V(42.5)};text-align:center;font:600 {V(1.9)}/1 UI;color:#9aa0ad">'
                f'&#9664;&#9664;&nbsp;&nbsp;&#10074;&#10074;&nbsp;&nbsp;&#9654;&#9654;&nbsp;&nbsp;&nbsp;{E(u.get("timecode", "00:12:41:08"))}</div>'
                f'<div style="position:absolute;left:0;right:0;top:{V(46.5)};bottom:0;background:#1c1f25;border-top:{V(0.2)} solid #2c3038">'
                + track(2.2, clips, 0.95) + track(7.6, [(0.08, 0.30, "#3FB6C6"), (0.47, 0.70, "#E6C63F")], 0.85)
                + track(13.0, [(0.00, 1.00, "#3a3f4a")], 1.0) + wave
                + f'<div style="position:absolute;left:{V(4 + ph * 92)};top:0;bottom:0;width:{V(0.35)};background:#ff3b30"></div></div></div>')
    elif k == "pc.channel_stats":
        # A channel dashboard on a second monitor: the subscriber count, today's change and a rising graph.
        pts = [0.80, 0.78, 0.74, 0.75, 0.70, 0.66, 0.67, 0.60, 0.52, 0.44, 0.30, 0.18]
        poly = " ".join(f"{i / (len(pts) - 1) * 100:.1f},{y * 100:.1f}" for i, y in enumerate(pts))
        body = (f'<div class="app" style="width:{w}px;height:{h}px;background:#14161b;color:#e9ecf2;padding:{V(4)} {V(5)}">'
                f'<div style="font:700 {V(2.6)}/1 UI;letter-spacing:.12em;color:#E8458B">{E(u.get("title", "BOMBOM TV · CHANNEL"))}</div>'
                f'<div style="font:800 {V(9.5)}/1 UI;margin-top:{V(4)}">{E(u.get("count", "58,912"))}</div>'
                f'<div style="font:600 {V(2.6)}/1 UI;color:#9aa0ad;margin-top:{V(1.4)};letter-spacing:.08em">SUBSCRIBERS</div>'
                f'<div style="font:700 {V(3)}/1 UI;color:#5FD38D;margin-top:{V(2.4)}">{E(u.get("change", "+3,021 TODAY"))}</div>'
                f'<svg viewBox="0 0 100 100" preserveAspectRatio="none" style="position:absolute;left:{V(5)};right:{V(5)};bottom:{V(5)};width:{V(90)};height:{V(26)}">'
                f'<polyline points="{poly}" fill="none" stroke="#E8458B" stroke-width="2.2" vector-effect="non-scaling-stroke"/></svg></div>')
    elif k == "phone.camera":
        # A phone filming: the viewfinder shows the scene it points at (a crop of the panel's own art, `subject` box),
        # with REC and a timer, corner guides and the shutter, like any phone camera app.
        bg = u.get("_bg")
        wide = w >= h
        rec = u.get("timer", "00:12")
        shutter = (f'<div style="position:absolute;{"right" if wide else "bottom"}:{V(3.2)};{"top" if wide else "left"}:50%;'
                   f'transform:translate{"Y" if wide else "X"}(-50%);width:{V(11 if wide else 16)};height:{V(11 if wide else 16)};border-radius:50%;'
                   f'border:{V(1.1)} solid rgba(255,255,255,.92);display:flex;align-items:center;justify-content:center">'
                   f'<div style="width:62%;height:62%;border-radius:{V(1.4)};background:#E5484D"></div></div>')
        corners = "".join(
            f'<div style="position:absolute;{a}:{V(6)};{b}:{V(6 if wide else 9)};width:{V(6)};height:{V(6)};'
            f'border-{a}:{V(.55)} solid rgba(255,255,255,.85);border-{b}:{V(.55)} solid rgba(255,255,255,.85)"></div>'
            for a, b in (("top", "left"), ("top", "right"), ("bottom", "left"), ("bottom", "right")))
        body = (f'<div class="app" style="width:{w}px;height:{h}px;background:#111 url(\'{uri(bg) if bg else ""}\') center/cover no-repeat">'
                f'<div style="position:absolute;inset:0;box-shadow:inset 0 0 {V(9)} rgba(0,0,0,.45)"></div>{corners}'
                f'<div style="position:absolute;left:{V(5)};top:{V(4)};display:flex;align-items:center;gap:{V(1.6)};'
                f'font:700 {V(4.2)}/1 UI;color:#fff;text-shadow:0 0 {V(1)} rgba(0,0,0,.8)">'
                f'<span style="display:inline-block;width:{V(3)};height:{V(3)};border-radius:50%;background:#E5484D"></span>REC {E(rec)}</div>'
                f'<div style="position:absolute;right:{V(17 if wide else 5)};top:{V(4)};font:700 {V(3.6)}/1 UI;color:#fff;'
                f'text-shadow:0 0 {V(1)} rgba(0,0,0,.8)">4K · 60</div>'
                f'<div style="position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:{V(13)};height:{V(13)};'
                f'border:{V(.45)} solid rgba(255,214,10,.9)"></div>{shutter}</div>')
    else:  # info cards, gate status, AAO and anything else: a clean public-service card
        title = u.get("title") or {"phone.gate_status": "GATE SAFETY KOREA", "phone.aao_booking": "ABILITY ASSESSMENT OFFICE",
                                   "phone.aao_result": "ABILITY ASSESSMENT OFFICE", "phone.hunterlink_rank": "HUNTERLINK",
                                   "phone.live_stream": "LIVE"}.get(k, "GATE SAFETY KOREA")
        paras = "".join(f'<p style="margin:0 0 {V(3.6)}">{fmt_text(t.strip())}</p>' for t in u.get("text", "").split("·") if t.strip())
        wide = w > h
        body = (f'<div class="app" style="width:{w}px;height:{h}px;background:#F2F5FA">'
                f'<div style="background:#1F4E9A;color:#fff;padding:{V(4 if wide else 6)} {V(5)};font:700 {V(4.4 if wide else 5.4)}/1.1 UI;letter-spacing:.06em;display:flex;align-items:center;gap:{V(2)}">'
                f'<span style="display:inline-block;width:{V(4)};height:{V(4)};border:{V(.7)} solid #fff;border-radius:{V(.8)}"></span>{E(title)}</div>'
                f'<div style="padding:{V(4 if wide else 7)} {V(6)};font:500 {V(3.8 if wide else 4.9)}/1.42 App;color:#1d2433">{paras}</div></div>')
    return head + body + "</body></html>"


def live_stream_html(u):
    """A livestream chat overlay floating on the panel (drone/stream POV): LIVE badge, then the chat rows.
    `at` is the top centre of the overlay as fractions of the panel; chat entries look like "[user]: message"."""
    x, y = u.get("at", [0.26, 0.08])
    cols = ["#8fd3ff", "#ffb3d1", "#c8f56b", "#ffd36b"]
    rows = []
    for i, c in enumerate(u.get("chat", [])):
        m = re.match(r"^\[([^\]]+)\]:\s*(.*)$", str(c))
        name, msg = (m.group(1), m.group(2)) if m else ("", str(c))
        rows.append(f'<div class="ls-row"><b style="color:{cols[i % len(cols)]}">{E(name)}</b>{fmt_text(msg)}</div>' if name
                    else f'<div class="ls-row">{fmt_text(msg)}</div>')
    head = '<span class="ls-live">● LIVE</span>' + (f'<span class="ls-view">{E(str(u["viewers"]))}</span>' if u.get("viewers") else "")
    return (f'<div class="lstream" style="left:{x * 100:.1f}%;top:{y * 100:.1f}%;width:{u.get("width", 0.46) * 100:.0f}%">'
            f'<div class="ls-head">{head}</div>{"".join(rows)}</div>')


def video_call_chrome(u, w, h):
    V = lambda x: f"{x * w / 100.0:.1f}px"
    return (f"<!doctype html><html><head><meta charset='utf-8'><style>{APP_BASE_CSS}</style></head>"
            f"<body style='width:{w}px;height:{h}px'><div class='app' style='width:{w}px;height:{h}px'>"
            f'<div style="position:absolute;left:0;right:0;top:0;height:{V(9)};background:linear-gradient(rgba(48,44,69,.72),rgba(48,44,69,0));'
            f'color:#fff;display:flex;align-items:center;gap:{V(1.6)};padding:0 {V(3)};font:700 {V(2.8)}/1 App">'
            f'<span style="font-size:{V(3.4)}">‹</span>{E(u.get("caller", ""))}<span style="font:600 {V(2.2)}/1 UI;opacity:.85;margin-left:{V(1)}">{E(u.get("duration", "02:14"))}</span>'
            f'<span style="margin-left:auto;font:700 {V(2.2)}/1 UI;letter-spacing:.14em;opacity:.8">TTOK</span></div>'
            f'<div style="position:absolute;right:{V(2.6)};top:{V(10)};width:{V(15)};height:{V(20)};border-radius:{V(1.6)};background:#4b4660;'
            f'border:{V(.35)} solid rgba(255,255,255,.85);overflow:hidden">'
            f'<div style="position:absolute;left:30%;top:22%;width:40%;height:30%;border-radius:50%;background:#7d7895"></div>'
            f'<div style="position:absolute;left:14%;top:58%;width:72%;height:60%;border-radius:45% 45% 0 0;background:#7d7895"></div></div>'
            f'<div style="position:absolute;left:50%;bottom:{V(2.4)};transform:translateX(-50%);display:flex;gap:{V(3.4)};padding:{V(1.4)} {V(3)};'
            f'border-radius:99px;background:rgba(48,44,69,.62)">'
            + "".join(f'<div style="width:{V(6)};height:{V(6)};border-radius:50%;background:{c}"></div>' for c in ("rgba(255,255,255,.3)", "rgba(255,255,255,.3)", "#E5484D"))
            + "</div></div></body></html>")


# ----------------------------------------------------------------------------------------------- bubble choice
def choose_bubble(kind_entries, tw, th, maxw, minwh, nlines=1):
    """Smallest good-looking bubble that holds a tw×th text block. Prefers wide, isotropic, 2–3 line bubbles."""
    best = None
    for e in kind_entries:
        bw, bh = e["size"]
        rx, ry, rw, rh = e["rect"]
        sx, sy = (tw + 12) / rw, (th + 10) / rh
        s = max(sx, sy)
        sx2, sy2 = max(sx, s / 1.18), max(sy, s / 1.18)
        W, H = bw * sx2, bh * sy2
        if minwh:
            k = max(minwh[0] / W, minwh[1] / H, 1.0)
            sx2, sy2, W, H = sx2 * k, sy2 * k, W * k, H * k
        if W > maxw:
            continue
        pen = 1 + 0.8 * abs(math.log(sx2 / sy2))
        aspect = W / H
        if aspect < 1.2:
            pen *= 1 + 1.6 * (1.2 - aspect)
        if nlines > 3:
            pen *= 1 + 0.12 * (nlines - 3)
        cost = W * H * pen
        if best is None or cost < best[0]:
            best = (cost, e, sx2, sy2, W, H)
    return best


OVL_SKIP = {"kind", "on", "at", "wf", "clock", "subject", "source", "timer", "hand", "button", "tilt", "mirror", "time"}


def ovl_text(u):
    """The words of an overlay card (a screen UI whose art has no green screen): the UI's own text, never its kind's name
    (28 Oct: ch010 P65's call card read "phone.ttok_call")."""
    k = u.get("kind", "")
    if u.get("text"):
        return str(u["text"])
    if u.get("title"):
        return str(u["title"])
    if k == "phone.ttok_call":
        return f"INCOMING CALL · {u.get('caller', '')}".strip(" ·")
    if k == "phone.ttok_video_call":
        return f"VIDEO CALL · {u.get('caller', '')}".strip(" ·")
    if k == "phone.ttok_chat":
        msgs = u.get("messages") or []
        return " / ".join(f"{m.get('from', '')}: {m.get('text', '')}" for m in msgs[-2:] if isinstance(m, dict))
    vals = [str(v) for kk, v in u.items() if kk not in OVL_SKIP and isinstance(v, (str, int, float))]
    return " · ".join(vals)


def card_html(card, fills, W):
    """A full-width kit card (title / end / intro) with its text boxes filled."""
    png, meta = card
    bounds = meta.get("art_bounds")
    if not bounds:  # the kit cards sit on a transparent margin: crop to the painted card so it fills the strip width
        with Image.open(png) as im_:
            bounds = list(im_.convert("RGBA").getchannel("A").point(lambda a: 255 if a > 8 else 0).getbbox()
                          or (0, 0, meta["size"][0], meta["size"][1]))
    x0, y0, x1, y1 = bounds
    cw, ch = x1 - x0, y1 - y0
    k = W / cw
    texts = []
    for b in meta.get("text_boxes", []):
        v = fills.get(b["id"])
        if not v:
            continue
        x, y, bw, bh = b["rect"]
        fs = (b.get("sample_size") or bh * 0.5) * k
        texts.append(f'<div class="ctx" style="left:{(x - x0) * k:.1f}px;top:{(y - y0) * k:.1f}px;width:{bw * k:.1f}px;height:{bh * k:.1f}px;'
                     f'color:{b.get("color", "#F7F5EE")}"><span style="font-size:{fs:.1f}px">{fmt_text(v)}</span></div>')
    return (f'<div class="blk card" style="height:{ch * k:.0f}px;background-color:#101218;background-image:url({uri(png)});background-size:{meta["size"][0] * k:.1f}px auto;'
            f'background-position:{-x0 * k:.1f}px {-y0 * k:.1f}px">{"".join(texts)}</div>')


# ----------------------------------------------------------------------------------------------- page scripts
TAIL_JS = r"""
(PROF) => {
  const NS = 'http://www.w3.org/2000/svg';
  const els = [...document.querySelectorAll('.lt.bm')];
  const boxes = els.map(e => e.getBoundingClientRect());
  const inOther = (x, y, skip) => boxes.some((b, i) => i !== skip && x > b.left + 6 && x < b.right - 6 && y > b.top + 6 && y < b.bottom - 6);
  const f = v => v.toFixed(1);
  let n = 0;
  els.forEach((el, idx) => {
    const t = el.dataset.type;
    if (el.dataset.tail === '0' || t === 'intense') return;
    const P = PROF[el.dataset.blank]; if (!P) return;
    const sx = +el.dataset.sx, sy = +el.dataset.sy, dil = +el.dataset.d || 0;
    const r = boxes[idx];
    const panel = document.querySelector(`.pnl[data-id="${el.dataset.panel}"]`); if (!panel) return;
    const pr = panel.getBoundingClientRect();
    const side = el.dataset.side || 'c', where = el.dataset.where;
    const fx = side === 'l' ? 0.26 : side === 'r' ? 0.74 : 0.5;
    const dy = Math.min(240, Math.max(80, pr.height * 0.24));
    let T = null;
    if (el.dataset.off === '1') {
      // speaker not drawn in this panel: the tail points out past the panel edge, toward where they stand
      const cxr = r.left + r.width / 2, toLeft = side === 'l' || (side === 'c' && cxr < pr.left + pr.width / 2);
      T = [toLeft ? Math.min(pr.left, r.left) - 600 : Math.max(pr.right, r.right) + 600, r.top + r.height * 0.55];
    } else if (el.dataset.hx) {
      // aim at the speaker's head as located by the panel review (maps through object-fit: cover)
      const img = panel.querySelector('img.art');
      if (img && img.naturalWidth) {
        const ir = img.getBoundingClientRect(), W0 = img.naturalWidth, H0 = img.naturalHeight;
        const s = Math.max(ir.width / W0, ir.height / H0);
        const pos = getComputedStyle(img).objectPosition.split(/\s+/);
        const off = (tok, free) => tok && tok.endsWith('%') ? free * parseFloat(tok) / 100 : (tok ? parseFloat(tok) : free / 2);
        const hx = ir.left + off(pos[0], ir.width - W0 * s) + (+el.dataset.hx) * W0 * s;
        const hy = ir.top + off(pos[1], ir.height - H0 * s) + (+el.dataset.hy) * H0 * s;
        if (hx > pr.left + 8 && hx < pr.right - 8 && hy > pr.top + 8 && hy < pr.bottom - 8) T = [hx, hy];
      }
    }
    if (!T) {
      if (where === 'before') T = [pr.left + pr.width * fx, pr.top + dy];
      else if (where === 'after') T = [pr.left + pr.width * fx, pr.bottom - dy];
      else if (where === 'beside') T = [(r.left >= pr.right - 4) ? pr.right - 70 : pr.left + 70, pr.top + pr.height * 0.40];
      else return;
    }
    const C = [P.cx * sx, P.cy * sy];
    const Tl = [T[0] - r.left, T[1] - r.top];
    const ang = Math.atan2(Tl[1] - C[1], Tl[0] - C[0]);
    const N = P.r.length;
    const edge = (a, inset) => {
      let th = Math.atan2(Math.sin(a) / sy, Math.cos(a) / sx); if (th < 0) th += 2 * Math.PI;
      const k = Math.round(th / (2 * Math.PI) * N) % N;
      let rr = P.r[k];
      if (t === 'shout') for (let j = -9; j <= 9; j++) rr = Math.min(rr, P.r[(k + j + N) % N]);
      rr -= P.stroke / 2 + (inset || 0);
      return [(P.cx + rr * Math.cos(th)) * sx, (P.cy + rr * Math.sin(th)) * sy];
    };
    const sw = Math.max(2.2, Math.min(3.6, P.stroke * Math.min(sx, sy) + dil));
    const svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('class', 'tail'); svg.setAttribute('width', 1); svg.setAttribute('height', 1);
    const add = (tag, at) => { const e = document.createElementNS(NS, tag); for (const k in at) e.setAttribute(k, at[k]); svg.appendChild(e); return e; };
    const M0 = edge(ang, 0);
    let ux = Tl[0] - M0[0], uy = Tl[1] - M0[1]; const dist = Math.hypot(ux, uy) || 1; ux /= dist; uy /= dist;
    if (t === 'thought') {
      const R = Math.max(9, Math.min(16, Math.min(r.width, r.height) * 0.075));
      let d = 6;
      [1, 0.66, 0.44].forEach(k => {
        const rr = R * k; d += rr;
        add('circle', {cx: f(M0[0] + ux * d), cy: f(M0[1] + uy * d), r: f(rr), fill: P.fill, stroke: P.line, 'stroke-width': f(sw)});
        d += rr + 6;
      });
      el.insertBefore(svg, el.querySelector('.btxt')); n++; return;
    }
    const base = Math.max(22, Math.min(46, Math.min(r.width, r.height) * 0.17));
    const rd = Math.hypot(M0[0] - C[0], M0[1] - C[1]) || 1;
    const dl = base / 2 / rd;
    const Ae = edge(ang - dl, 0), Be = edge(ang + dl, 0), Ai = edge(ang - dl, 8), Bi = edge(ang + dl, 8);
    const M = [(Ae[0] + Be[0]) / 2, (Ae[1] + Be[1]) / 2];
    // a bubble in the side column beside an inset panel can sit far from its speaker: let its tail run on into the
    // panel until it nearly reaches the head the review located, so it never stops on someone else (ch001 P04)
    // a gutter bubble aimed at a located head may run on into the panel too, so it never ends in the sky (judge, ch 3)
    const cap = el.dataset.hx ? (where === 'beside' ? 380 : 230) : (t === 'shout' ? 90 : 110);
    let L = Math.max(30, Math.min(cap, dist - (cap > 110 ? 46 : 14)));
    while (L > 24 && inOther(r.left + M[0] + ux * L, r.top + M[1] + uy * L, idx)) L -= 6;
    const tip = [M[0] + ux * L, M[1] + uy * L];
    const px = -uy, py = ux;
    const fill = P.fill, line = P.line;
    const P2 = a => f(a[0]) + ' ' + f(a[1]);
    if (t === 'phone') {
      const pts = [Ai, Ae];
      const segs = 3;
      for (let i = 1; i < segs; i++) {
        const q = i / segs, o = (i % 2 ? 1 : -1) * base * 0.55 * (1 - q * 0.6);
        pts.push([M[0] + ux * L * q + px * o - px * base * 0.25, M[1] + uy * L * q + py * o - py * base * 0.25]);
      }
      pts.push(tip);
      for (let i = segs - 1; i >= 1; i--) {
        const q = i / segs, o = (i % 2 ? 1 : -1) * base * 0.55 * (1 - q * 0.6);
        pts.push([M[0] + ux * L * q + px * o + px * base * 0.25, M[1] + uy * L * q + py * o + py * base * 0.25]);
      }
      pts.push(Be, Bi);
      add('path', {d: 'M' + pts.map(P2).join(' L') + ' Z', fill: fill, stroke: 'none'});
      add('path', {d: 'M' + pts.slice(1, -1).map(P2).join(' L'), fill: 'none', stroke: line,
                   'stroke-width': f(sw), 'stroke-linejoin': 'round', 'stroke-linecap': 'round'});
    } else {
      const bend = (t === 'shout') ? 0 : (side === 'l' ? -1 : side === 'r' ? 1 : (ux > 0 ? 1 : -1)) * Math.min(20, L * 0.28);
      const c1 = [(Ae[0] + tip[0]) / 2 + px * bend, (Ae[1] + tip[1]) / 2 + py * bend];
      const c2 = [(Be[0] + tip[0]) / 2 + px * bend * 0.6, (Be[1] + tip[1]) / 2 + py * bend * 0.6];
      add('path', {d: `M${P2(Ai)} L${P2(Ae)} Q${P2(c1)} ${P2(tip)} Q${P2(c2)} ${P2(Be)} L${P2(Bi)} Z`, fill: fill, stroke: 'none'});
      const at = {d: `M${P2(Ae)} Q${P2(c1)} ${P2(tip)} Q${P2(c2)} ${P2(Be)}`, fill: 'none', stroke: line, 'stroke-width': f(sw),
                  'stroke-linejoin': 'round', 'stroke-linecap': 'round'};
      if (t === 'whisper') at['stroke-dasharray'] = '7 6';
      add('path', at);
    }
    el.insertBefore(svg, el.querySelector('.btxt')); n++;
  });
  return n;
}
"""
SYS_JS = r"""
() => {
  document.querySelectorAll('.syswin').forEach(s => {
    const w = s.getBoundingClientRect().width;
    s.querySelectorAll('.stx span').forEach(sp => { sp.style.fontSize = (parseFloat(sp.dataset.fs) * w) + 'px'; });
  });
  document.querySelectorAll('.stx').forEach(el => {
    const sp = el.firstElementChild; const W = el.clientWidth, H = el.clientHeight;
    let fs = parseFloat(sp.style.fontSize), g = 0;
    while ((sp.scrollWidth > W + 1 || sp.offsetHeight > H + 2) && fs > 6 && g++ < 90) { fs *= 0.95; sp.style.fontSize = fs + 'px'; }
  });
  document.querySelectorAll('.syswin').forEach(s => { s.style.setProperty('--tilt', s.dataset.tilt + 'deg'); s.classList.add('tilted'); });
  return true;
}
"""
WINFACE_JS = r"""
() => {
  // A floating system window never covers a drawn face (the head boxes in data-faces). When it does, try smaller widths
  // and other places along the top of the panel, keeping clear of the panel's other windows, and keep the first that
  // covers no face (28 Oct: ch004 P14/P21/P35/P40/P44, ch006 P41/P44, ch008 P09/P53/P66/P67 were all moved by hand).
  const fit = (s) => {
    const w = s.getBoundingClientRect().width;
    s.querySelectorAll('.stx span').forEach(sp => { sp.style.fontSize = (parseFloat(sp.dataset.fs) * w) + 'px'; });
    s.querySelectorAll('.stx').forEach(el => {
      const sp = el.firstElementChild; const W = el.clientWidth, H = el.clientHeight;
      let fs = parseFloat(sp.style.fontSize), g = 0;
      while ((sp.scrollWidth > W + 1 || sp.offsetHeight > H + 2) && fs > 6 && g++ < 90) { fs *= 0.95; sp.style.fontSize = fs + 'px'; }
    });
  };
  let moved = 0;
  // first, every window sits wholly inside its panel: one placed so low (or high) that the panel edge cuts it moves in
  // (28 Oct: ch009 and ch010's bottom timers at y 0.86-0.92 showed only their header strip, the time itself cut off)
  for (const p of document.querySelectorAll('.pnl')) {
    const pb = p.getBoundingClientRect(), fh = p.clientHeight;
    for (const w of p.querySelectorAll('.syswin')) {
      const b = w.getBoundingClientRect(), top = b.top - pb.top, bot = b.bottom - pb.top;
      let dy = 0;
      if (bot > fh * 0.97) dy = fh * 0.97 - bot;
      if (top + dy < fh * 0.01) dy = fh * 0.01 - top;
      if (Math.abs(dy) > 0.5) { w.style.top = (parseFloat(w.style.top) + dy / fh * 100).toFixed(2) + '%'; moved++; }
    }
  }
  // then, windows stacked in one panel never overlap: a later window that runs into an earlier one moves down below it
  // (28 Oct: ch008 P57's second notice hid the first one's text)
  for (const p of document.querySelectorAll('.pnl')) {
    const ws = [...p.querySelectorAll('.syswin')];
    const pb = p.getBoundingClientRect(), fh = p.clientHeight;
    const rr = (w) => { const b = w.getBoundingClientRect(); return [b.left - pb.left, b.top - pb.top, b.right - pb.left, b.bottom - pb.top]; };
    for (let i = 1; i < ws.length; i++) {
      for (let j = 0; j < i; j++) {
        const a = rr(ws[j]), b = rr(ws[i]);
        if (b[0] < a[2] && b[2] > a[0] && b[1] < a[3] && b[3] > a[1]) {
          const dy = a[3] - b[1] + fh * 0.02;
          if (b[3] + dy <= fh * 0.97) { ws[i].style.top = (parseFloat(ws[i].style.top) + dy / fh * 100).toFixed(2) + '%'; moved++; }
        }
      }
    }
  }
  for (const p of document.querySelectorAll('.pnl')) {
    const faces = p.dataset.faces ? JSON.parse(p.dataset.faces) : [];
    const img = p.querySelector('img.art');
    if (!faces.length || !img || !img.naturalWidth) continue;
    const fw = p.clientWidth, fh = p.clientHeight, iw = img.naturalWidth, ih = img.naturalHeight;
    const sc = Math.max(fw / iw, fh / ih);
    const pos = (getComputedStyle(img).objectPosition || '50% 50%').split(' ').map(v => parseFloat(v) / 100);
    const offx = (fw - iw * sc) * (isNaN(pos[0]) ? .5 : pos[0]), offy = (fh - ih * sc) * (isNaN(pos[1]) ? .5 : pos[1]);
    const fb = faces.map(f => [f[0] * iw * sc + offx, f[1] * ih * sc + offy, f[2] * iw * sc + offx, f[3] * ih * sc + offy]);
    const pb = p.getBoundingClientRect();
    const wins = [...p.querySelectorAll('.syswin')];
    const rel = (w) => { const b = w.getBoundingClientRect(); return [b.left - pb.left, b.top - pb.top, b.right - pb.left, b.bottom - pb.top]; };
    const cover = (r) => Math.max(0, ...fb.map(f => {
      const ix = Math.max(0, Math.min(r[2], f[2]) - Math.max(r[0], f[0])), iy = Math.max(0, Math.min(r[3], f[3]) - Math.max(r[1], f[1]));
      const fa = (f[2] - f[0]) * (f[3] - f[1]); return fa > 0 ? ix * iy / fa : 0; }));
    for (const w of wins) {
      if (cover(rel(w)) <= 0.12) continue;
      const others = wins.filter(o => o !== w).map(rel);
      const wf0 = parseFloat(w.style.getPropertyValue('--wf')) || 0.66;
      const left0 = w.style.left, top0 = w.style.top;
      let best = null;
      for (const k of [1, 0.85, 0.72, 0.6]) {
        const wf = Math.max(0.34, wf0 * k);
        for (const cx of [parseFloat(left0), 50, 27, 73, 21, 79]) {
          for (const ty of [parseFloat(top0), 3]) {
            w.style.setProperty('--wf', wf); w.style.left = cx + '%'; w.style.top = ty + '%';
            const r = rel(w);
            if (r[0] < fw * 0.01 || r[2] > fw * 0.99 || r[1] < -2 || r[3] > fh * 0.98) continue;
            if (others.some(o => r[0] < o[2] && r[2] > o[0] && r[1] < o[3] && r[3] > o[1])) continue;
            const c = cover(r);
            if (!best || c < best.c - 1e-6) best = {c, wf, cx, ty};
            if (c <= 0.02) break;
          }
          if (best && best.c <= 0.02) break;
        }
        if (best && best.c <= 0.02) break;
      }
      if (best) {
        w.style.setProperty('--wf', best.wf); w.style.left = best.cx + '%'; w.style.top = best.ty + '%';
        fit(w); moved++;
      } else { w.style.setProperty('--wf', wf0); w.style.left = left0; w.style.top = top0; }
    }
  }
  return moved;
}
"""
TAG_JS = r"""
() => {
  // A place/time tag sits on the panel's top-left corner. When a bubble covers it, it moves to the first free corner:
  // top-right, bottom-left, then bottom-right (28 Oct: ch005 P01's tag was hidden under the eulogy bubble).
  const bubbles = [...document.querySelectorAll('.lt:not(.t-tag)')].map(e => e.getBoundingClientRect());
  const hits = (r) => bubbles.some(b => r.left < b.right - 6 && r.right > b.left + 6 && r.top < b.bottom - 6 && r.bottom > b.top + 6);
  let moved = 0;
  for (const t of document.querySelectorAll('.t-tag')) {
    if (!hits(t.getBoundingClientRect())) continue;
    const top = getComputedStyle(t).top;
    const tries = [{left: 'auto', right: '16px', top: top, bottom: 'auto'}, {left: '16px', right: 'auto', top: 'auto', bottom: '-22px'},
                   {left: 'auto', right: '16px', top: 'auto', bottom: '-22px'}];
    let ok = false;
    for (const c of tries) {
      Object.assign(t.style, c);
      if (!hits(t.getBoundingClientRect())) { ok = true; moved++; break; }
    }
    if (!ok) Object.assign(t.style, {left: '', right: '', top: '', bottom: ''});
  }
  return moved;
}
"""
SFX_JS = r"""
() => {
  // SFX sit above everything in the panel overlay. Nudge each one off any bubble, system window or nameplate it covers,
  // by the smallest move that keeps its centre inside the panel; shrink it when no move fits.
  const pad = 12;
  const boxes = [...document.querySelectorAll('.lt:not(.t-tag), .syswin, .intro')].map(e => e.getBoundingClientRect());
  // Faces too: the head boxes the panel reviews located (data-faces on the panel, in art fractions), mapped through
  // object-fit: cover onto the page. An SFX never sits on a face.
  const facesOf = (pnl) => {
    const out = []; if (!pnl || !pnl.dataset.faces) return out;
    const img = pnl.querySelector('img.art'); if (!img || !img.naturalWidth) return out;
    const ir = img.getBoundingClientRect(), W0 = img.naturalWidth, H0 = img.naturalHeight;
    const sc = Math.max(ir.width / W0, ir.height / H0);
    const pos = getComputedStyle(img).objectPosition.split(/\s+/);
    const off = (tok, free) => tok && tok.endsWith('%') ? free * parseFloat(tok) / 100 : (tok ? parseFloat(tok) : free / 2);
    const ox = ir.left + off(pos[0], ir.width - W0 * sc), oy = ir.top + off(pos[1], ir.height - H0 * sc);
    const pr = pnl.getBoundingClientRect();
    for (const f of JSON.parse(pnl.dataset.faces)) {
      const b = {left: ox + f[0] * W0 * sc, top: oy + f[1] * H0 * sc, right: ox + f[2] * W0 * sc, bottom: oy + f[3] * H0 * sc};
      b.left = Math.max(b.left, pr.left); b.right = Math.min(b.right, pr.right); b.top = Math.max(b.top, pr.top); b.bottom = Math.min(b.bottom, pr.bottom);
      if (b.right - b.left > 4 && b.bottom - b.top > 4) out.push(b);
    }
    return out;
  };
  let moved = 0; const stuck = [], onface = [];
  const placed = [];  // SFX already placed: a later SFX keeps off them too (28 Oct: ch006 P03's FWIP sat on SHK SHK SHK)
  for (const s of document.querySelectorAll('.sfx')) {
    const pov = s.parentElement.getBoundingClientRect();
    const faces = facesOf(s.parentElement.parentElement.querySelector('.pnl'));
    const obst = boxes.concat(faces, placed);
    let shrinks = 0;
    for (let it = 0; it < 12; it++) {
      const r = s.getBoundingClientRect();
      const hit = obst.find(b => r.left < b.right + pad && r.right > b.left - pad && r.top < b.bottom + pad && r.bottom > b.top - pad);
      if (!hit) break;
      const best = [[0, hit.bottom + pad - r.top], [0, hit.top - pad - r.bottom], [hit.right + pad - r.left, 0], [hit.left - pad - r.right, 0]]
        .map(([dx, dy]) => {
          const cx = (r.left + r.right) / 2 + dx - pov.left, cy = (r.top + r.bottom) / 2 + dy - pov.top;
          const inside = cx > pov.width * 0.06 && cx < pov.width * 0.94 && cy > pov.height * 0.06 && cy < pov.height * 0.94;
          return {dx, dy, cost: Math.abs(dx) + Math.abs(dy) + (inside ? 0 : 1e6)};
        }).sort((a, b) => a.cost - b.cost)[0];
      if (best.cost >= 1e6) {
        if (shrinks++ >= 3) { (faces.includes(hit) ? onface : stuck).push(s.textContent.trim()); break; }
        s.style.fontSize = (parseFloat(s.style.fontSize) * 0.84).toFixed(1) + 'px';
        continue;
      }
      s.style.left = (parseFloat(s.style.left) + best.dx / pov.width * 100).toFixed(2) + '%';
      s.style.top = (parseFloat(s.style.top) + best.dy / pov.height * 100).toFixed(2) + '%';
      moved++;
    }
    placed.push(s.getBoundingClientRect());
  }
  // SFX may break the panel frame but never run off the page: keep every one inside the strip's width.
  const pageW = document.documentElement.clientWidth, edge = 14;
  for (const s of document.querySelectorAll('.sfx')) {
    const pov = s.parentElement.getBoundingClientRect();
    for (let it = 0; it < 4; it++) {
      const r = s.getBoundingClientRect();
      if (r.width > pageW - 2 * edge) { s.style.fontSize = (parseFloat(s.style.fontSize) * (pageW - 2 * edge) / r.width * 0.97).toFixed(1) + 'px'; continue; }
      let dx = 0;
      if (r.left < edge) dx = edge - r.left; else if (r.right > pageW - edge) dx = pageW - edge - r.right;
      if (!dx) break;
      s.style.left = (parseFloat(s.style.left) + dx / pov.width * 100).toFixed(2) + '%';
      moved++;
    }
  }
  return {moved, stuck, onface};
}
"""


def strip_css(W):
    return f"""{FONTS}
*{{box-sizing:border-box}} html,body{{margin:0;width:{W}px;overflow-x:hidden;background:#fff}}
.blk{{width:{W}px;position:relative}}
.pwrap{{position:relative;z-index:1}}
.pwrap.a-l .pbox{{margin-left:40px}} .pwrap.a-r .pbox{{margin-right:40px;margin-left:auto}}
.pbox{{position:relative;margin:0 auto}}
.row .pbox{{flex:none;margin:0}}
.pov{{position:absolute;inset:0;z-index:6;pointer-events:none}}
.pnl{{position:relative;overflow:hidden;margin:0 auto}}
.pnl img.art{{display:block;width:100%;height:100%;object-fit:cover}}
.framed{{box-shadow:0 0 0 2px {LINE}}}
.dark .framed{{box-shadow:0 0 0 2px #2a2c36}}
.vig{{-webkit-mask-image:radial-gradient(ellipse 72% 68% at 50% 50%,#000 60%,transparent 100%)}}
.row{{display:flex;align-items:center;gap:26px;padding:0 40px;position:relative;z-index:2}}
.row .pnl{{flex:none;margin:0}}
.beside{{flex:1;display:flex;flex-direction:column;gap:22px;align-items:center;justify-content:center;min-height:160px;position:relative;z-index:3}}
.gut{{position:relative;z-index:3;display:flex;flex-direction:column;gap:18px;padding-top:26px}}
.gut.after{{padding-top:0;padding-bottom:22px}}
.lt{{position:relative;flex:none;z-index:4}}
.pair{{display:flex;justify-content:space-between;align-items:flex-start;padding:0 {int(W * .05)}px;position:relative;z-index:4}}
.pair .lt{{margin-left:0;margin-right:0}}
.lt.bm .bimg{{position:absolute;left:0;top:0;width:100%;height:100%;display:block}}
.lt .btxt{{position:absolute;display:flex;align-items:center;justify-content:center;z-index:3}}
.lt .btxt span{{display:block;text-align:center;text-wrap:balance}}
.lt .tail{{position:absolute;left:0;top:0;overflow:visible;z-index:2}}
.s-l{{margin-left:{int(W * .06)}px;margin-right:auto}} .s-r{{margin-left:auto;margin-right:{int(W * .06)}px}} .s-c{{margin-left:auto;margin-right:auto}}
.beside .lt{{margin-left:auto;margin-right:auto}}
.t-float{{font:500 29px/1.3 'LetterSoft',sans-serif;color:#3b3631;text-align:left;padding:6px 4px;letter-spacing:.2px;text-wrap:pretty}}
.dark .t-float{{color:#ebe6dd}}
.t-narr{{font:600 28px/1.28 'Letter',sans-serif;padding:22px 30px;text-align:center;background:#fff;border:2.5px solid {LINE};color:#1d1917;text-wrap:balance}}
.t-narr_dark{{font:600 28px/1.28 'Letter',sans-serif;padding:22px 30px;text-align:center;background:#141113;color:#f1ede6;text-wrap:balance}}
.dark .t-narr_dark{{border:2px solid #3a3640}}
.t-inner{{font:600 28px/1.28 'Letter',sans-serif;padding:20px 30px;text-align:center;background:#0d0c10;color:#f4f1ec;box-shadow:0 0 0 2px #0d0c10, 0 0 0 4px #f4f1ec;text-wrap:balance}}
.dark .t-inner{{box-shadow:0 0 0 2px #f4f1ec}}
.t-link{{font:700 28px/1.28 'Letter',sans-serif;padding:20px 30px;text-align:center;background:#1c1206;color:#ffd98a;box-shadow:0 0 0 2px #1c1206, 0 0 0 5px #f2a93b, 0 0 22px 6px rgba(242,169,59,.55);text-wrap:balance;letter-spacing:.5px}}
.t-note{{font:400 33px/40px 'Pencil','LetterSoft',cursive;color:#34343a;text-align:left;padding:10px 26px 12px;background:repeating-linear-gradient(180deg,#fbf8ef 0 38px,#c9d4e3 38px 40px);border:1.5px solid #c7bba2;transform:rotate(-1.2deg);box-shadow:2px 3px 0 rgba(0,0,0,.18);text-wrap:pretty}}
.t-tag{{position:absolute;left:16px;top:-22px;white-space:nowrap;padding:9px 20px;font:700 22px/1 'UI',sans-serif;letter-spacing:.09em;
  background:#fff;color:#1d1917;border:2.5px solid {LINE};border-radius:99px;z-index:6}}
.t-footnote{{text-align:right;padding:12px 60px 0 0;font:500 21px/1.2 'LetterSoft',sans-serif;color:#77706a;margin-left:auto}}
.dark .t-footnote{{color:#aaa49b}}
.sfx{{position:absolute;z-index:6;white-space:nowrap;line-height:.92;paint-order:stroke fill;pointer-events:none}}
.sfx.vert{{text-align:center;line-height:.86}}
.x-impact{{font-family:'Impact','Gaegu';color:#fffaf0;-webkit-text-stroke:9px {LINE};letter-spacing:2px;filter:drop-shadow(5px 6px 0 rgba(0,0,0,.28))}}
.x-quiet{{font-family:'Marker','Gaegu';color:#ffffff;-webkit-text-stroke:5px {LINE};letter-spacing:1px}}
.x-alert{{font-family:'Impact','Gaegu';color:#ff3b30;-webkit-text-stroke:7px #2a0505;letter-spacing:2px}}
.x-gate{{font-family:'Bang','Gaegu';color:#b68cff;-webkit-text-stroke:7px #0d2f45;letter-spacing:6px;filter:drop-shadow(0 0 12px rgba(63,227,242,.6))}}
.x-summon{{font:700 italic 1em 'UI','Gaegu',sans-serif;color:#e9fcff;-webkit-text-stroke:5px #06324a;letter-spacing:8px;filter:drop-shadow(0 0 14px rgba(63,227,242,.85))}}
.x-phone{{font-family:'Marker','Gaegu';color:#ffffff;-webkit-text-stroke:5px {LINE}}}
.x-comic{{font-family:'Impact','Gaegu';color:#ffe9a8;-webkit-text-stroke:7px {LINE};letter-spacing:2px}}
.syswin{{position:absolute;width:calc(var(--wf) * 100%);transform:translateX(-50%);z-index:5}}
.syswin.tilted{{transform:translateX(-50%) perspective(1500px) rotateY(var(--tilt)) rotateX(3deg);filter:drop-shadow(0 0 14px rgba(63,227,242,.45))}}
.syswin.mir.tilted{{transform:translateX(-50%) perspective(1500px) rotateY(var(--tilt)) rotateX(3deg) scaleX(-1)}}
.syswin img{{display:block;width:100%;height:100%}}
.syswin.glitchy.tilted{{filter:drop-shadow(0 0 14px rgba(63,227,242,.45)) drop-shadow(5px 0 0 rgba(255,45,85,.42)) drop-shadow(-5px 0 0 rgba(60,230,255,.42))}}
.syswin.glitchy .stx span{{text-shadow:2px 0 0 rgba(255,45,85,.85),-2px 0 0 rgba(60,230,255,.85),0 0 8px rgba(63,227,242,.8)}}
.stx{{position:absolute;display:flex;align-items:center;font-family:'UI',sans-serif;font-weight:700;letter-spacing:.04em;line-height:1.12;
  text-shadow:0 0 8px rgba(63,227,242,.8)}}
.stx.nw span{{white-space:nowrap}}
.stx.mono{{font-family:'Mono',monospace;font-weight:400;align-items:flex-start;letter-spacing:.02em;line-height:1.38}}
.stx.op{{letter-spacing:.32em;font-weight:600;opacity:.85}}
.sysanchor{{position:absolute;left:0;width:1px;height:1px}}
.intro{{position:absolute;left:22px;bottom:22px;z-index:7;background:#fff;border:2.5px solid {LINE};padding:10px 20px 11px;
  font:700 30px/1.05 'UI',sans-serif;letter-spacing:.06em;color:#1d1917;box-shadow:6px 6px 0 rgba(43,37,35,.85)}}
.intro span{{display:block;font:600 19px/1.2 'UI',sans-serif;letter-spacing:.16em;color:#5d6470;margin-top:5px}}
.label{{position:absolute;z-index:3;font-family:'Marker','Gaegu',cursive;white-space:nowrap;letter-spacing:1px;opacity:.92}}
.lstream{{position:absolute;transform:translateX(-50%);z-index:5;background:rgba(10,12,20,.74);border:1.5px solid rgba(255,255,255,.2);
  border-radius:14px;padding:12px 16px 14px;box-shadow:0 4px 16px rgba(0,0,0,.35)}}
.ls-head{{display:flex;align-items:center;gap:10px;margin-bottom:4px;font:700 16px/1 'UI',sans-serif;letter-spacing:.08em;color:#fff}}
.ls-live{{background:#e5383b;padding:5px 9px 4px;border-radius:6px}}
.ls-view{{opacity:.85}}
.ls-row{{font:600 21px/1.28 'App',sans-serif;color:#f4f4f6;margin-top:7px;text-wrap:pretty}}
.ls-row b{{font-weight:700;margin-right:8px}}
body > .blk:first-child .t-tag{{top:18px}}
.ovl{{position:absolute;left:8%;right:8%;top:8%;padding:20px;background:rgba(255,255,255,.94);font:600 26px/1.3 'App';z-index:5;border-radius:12px}}
iframe.appl{{position:absolute;inset:0;width:100%;height:100%;border:0;z-index:4;background:transparent}}
.card{{position:relative;background-repeat:no-repeat}}
.ctx{{position:absolute;display:flex;align-items:center;justify-content:center;text-align:center;font:700 1em/1.15 'UI',sans-serif;letter-spacing:.14em}}
.chibi-end{{width:62%;margin:0 auto;border-radius:18px;overflow:hidden;box-shadow:0 0 0 2px {LINE}}}
.chibi-end img{{display:block;width:100%}}
.title{{padding:150px 40px 140px;text-align:center}}
.logo{{width:78%;display:block;margin:0 auto}}
.logo-t{{font:400 118px/0.92 'Impact',sans-serif;color:#0b1530;letter-spacing:2px}}
.logo-t span{{color:#F2A93B;-webkit-text-stroke:3px #0b1530}}
.dark .logo-t{{color:#e9fcff}}
.t-line{{margin-top:44px;font:700 34px/1 'UI',sans-serif;letter-spacing:.32em;color:#5d6470}}
.endcard{{padding:110px 40px 190px;text-align:center}}
.end-chibi{{width:56%;display:block;margin:0 auto 44px}}
.e-tbc{{font:700 44px/1 'UI',sans-serif;letter-spacing:.42em;color:#2b2523}} .dark .e-tbc{{color:#eee}}
.e-next{{margin-top:28px;font:600 28px/1.3 'UI',sans-serif;letter-spacing:.16em;color:#8a847c}}
"""


# ----------------------------------------------------------------------------------------------- main
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("art")
    ap.add_argument("out")
    ap.add_argument("--kit", default="/home/claude/msgf-kit")
    ap.add_argument("--width", type=int, default=1080)
    ap.add_argument("--seg-max", type=int, default=2400)
    ap.add_argument("--seg-min", type=int, default=700)
    ap.add_argument("--dpr", type=int, default=2, help="pixel ratio of the strip image (2 = 2160 px wide for a 1080 layout)")
    ap.add_argument("--no-upscale", action="store_true", help="skip the 2x anime upscale of panel art (tests only)")
    ap.add_argument("--upscale-models", default="/tmp/claude-0/-home-claude/74687d11-0cc0-5bfd-9d7d-ad4189ed4d7b/scratchpad/upscale/models")
    ap.add_argument("--placeholders", action="store_true")
    ap.add_argument("--only", default=None, help="panel range, e.g. P01-P20")
    ap.add_argument("--letter-font", default="/home/claude/msgf-fonts/anime_ace_2",
                    help="folder with the lettering TTF/OTF files (Anime Ace 2.0 BB, the owner's pick); falls back to Shantell Sans. "
                         "Licensed for flattened use only: never commit these files or publish them.")
    A = ap.parse_args()
    global FONTS
    lf = Path(A.letter_font) if A.letter_font else None
    ttfs = (sorted(lf.glob("*.[tT][tT][fF]")) + sorted(lf.glob("*.[oO][tT][fF]"))) if lf and lf.is_dir() else []
    if ttfs:
        faces = []
        for f_ in ttfs:
            n_ = f_.stem.lower()
            bold = any(k in n_ for k in ("bld", "bold"))
            ital = any(k in n_ for k in ("ital", "obl"))
            st_ = "italic" if ital else "normal"
            for w_ in ((700, 800) if bold else (400, 500, 600)):
                for fam_ in ("Letter", "LetterSoft"):
                    faces.append(f"@font-face{{font-family:'{fam_}';src:url('{uri(f_)}');font-weight:{w_};font-style:{st_}}}")
        FONTS = "\n".join([x_ for x_ in FONTS.split("\n") if "'Letter'" not in x_ and "'LetterSoft'" not in x_] + faces)
        print("lettering font:", ", ".join(f_.name for f_ in ttfs))
    else:
        print(f"lettering font: Shantell Sans (no font files in {lf})")
    W = A.width
    S = load_script(A.script)
    ART, OUT = Path(A.art), Path(A.out)
    OUT.mkdir(parents=True, exist_ok=True)
    WORK = OUT / "_work"
    WORK.mkdir(exist_ok=True)
    kit = kitlib.Kit(A.kit)
    warnings = []
    up_net = None
    if not A.no_upscale:
        import upscale_art
        up_net = upscale_art.load_net(A.upscale_models, 2)

    def upscaled(path):
        """2x Real-ESRGAN copy of an art file (cached in _work/up); the original when upscaling is off."""
        path = Path(path)
        if up_net is None:
            return path
        dst = WORK / "up" / (path.stem + "_x2.png")
        if not dst.exists() or dst.stat().st_mtime < path.stat().st_mtime:
            dst.parent.mkdir(exist_ok=True)
            import upscale_art
            with Image.open(path) as im_:
                upscale_art.upscale(up_net, im_).save(dst, compress_level=6)
        return dst
    panels = S["panels"]
    if A.only:
        a_, b_ = A.only.split("-")
        ids = [p["id"] for p in panels]
        panels = panels[ids.index(a_): ids.index(b_) + 1]

    # Speaker positions from Codex's panel review (art/REVIEW.json, then REVIEW_*.json written by art chats, later wins).
    # A visible speaker's bubble goes on the side where they are drawn and its tail aims at their head; a speaker who
    # is not drawn in the panel (or is marked offpanel:) gets an off-panel tail that points out past the panel edge.
    heads = {}
    for rv in sorted(ART.glob("REVIEW*.json"), key=lambda q: (q.name != "REVIEW.json", q.name)):
        try:
            for pid_, v_ in json.loads(rv.read_text(encoding="utf-8")).items():
                if isinstance(v_, dict) and isinstance(v_.get("heads"), dict):
                    heads[pid_] = v_["heads"]
        except Exception as ex_:
            warnings.append(f"REVIEW FILE UNREADABLE: {rv.name}: {ex_}")
    SPEAKER_TYPES = {"speech", "nervous", "thought", "whisper", "shout", "menace", "monster"}
    n_aim = n_off = 0
    for p in panels:
        H = heads.get(p["id"])
        for ln in p.get("lines") or []:
            if not isinstance(ln, dict) or ln.get("type", "speech") not in SPEAKER_TYPES:
                continue
            who = str(ln.get("who", ""))
            sid = who.split(":", 1)[1] if who.startswith("offpanel:") else who
            box = (H or {}).get(sid)
            if who.startswith("offpanel:") or (H is not None and not box):
                ln["_off"] = True
                n_off += 1
            elif isinstance(box, (list, tuple)) and len(box) == 4:
                cx = (box[0] + box[2]) / 2
                ln["_head"] = (cx, box[1] + (box[3] - box[1]) * 0.6)
                ln["side"] = "l" if cx < 0.42 else "r" if cx > 0.58 else "c"
                n_aim += 1
    print(f"speakers: {n_aim} tails aimed at drawn heads, {n_off} off-panel lines, review for {len(heads)} panels")

    def faces_attr(pid_):
        # every head box the panel review located, for the SFX layout to keep clear of (art fractions x0, y0, x1, y1)
        # A box covering most of the panel is not a head (a review that boxed a whole close-up or a void); it would
        # pin every SFX and window as "on a face", so it is ignored.
        fs = [[round(float(v), 4) for v in b] for b in (heads.get(pid_) or {}).values()
              if isinstance(b, (list, tuple)) and len(b) == 4
              and (float(b[2]) - float(b[0])) * (float(b[3]) - float(b[1])) <= 0.5]
        return f" data-faces='{json.dumps(fs)}'" if fs else ""

    with sync_playwright() as pw:
        br = pw.chromium.launch()
        page = br.new_page(); page.set_default_timeout(240000)
        # ------------------------------------------------ art + screens
        art_for = {}
        ui_tint = {}  # pid -> mean BGR of the UI warped into its screen (reflections of that screen take this colour)
        screens = {}  # pid -> [(screen mask, tint or None for a dark screen)], for the spill pass
        for p in panels:
            if p.get("kind") in ("title", "end"):
                continue
            pid = p["id"]
            if p.get("kind") == "caption":  # narration straight on the page colour: a blank, borderless panel
                cw_, ch_ = {"strip": (1536, 512), "inset-l": (1024, 1024), "inset-r": (1024, 1024)}.get(p.get("shape", "strip"), (1536, 512))
                capf = WORK / f"{pid}_caption.png"
                Image.new("RGB", (cw_, ch_), bg_hex(p.get("bg", "black"))).save(capf)
                art_for[pid] = capf
                continue
            src = next((ART / f"{pid}{x}" for x in (".png", ".jpg", ".jpeg", ".webp") if (ART / f"{pid}{x}").exists()), None)
            hand = next((u.get("hand") for u in (p.get("ui") or []) if u.get("hand")), None)
            if src is None and hand and hand in kit.hands:
                src = kit.hands[hand][0]
            if src is None:
                if not A.placeholders:
                    raise SystemExit(f"missing art for {pid}")
                src = WORK / f"{pid}_ph.png"
                placeholder(pid, p.get("shape", "wide"), p.get("art", ""), src, chibi=p.get("style") == "chibi")
                warnings.append(f"{pid}: placeholder art")
            if lossy_image(src):
                warnings.append(f"{pid}: art is a lossy {Path(src).suffix} file; panel art must be PNG (no compression)")
            is_hand = bool(hand and hand in kit.hands and Path(src) == Path(kit.hands[hand][0]))
            art_for[pid] = Path(src) if str(src).endswith("_ph.png") else upscaled(src)
            for u in p.get("ui") or []:
                if u.get("on") != "screen":
                    continue
                img = cv2.imread(str(art_for[pid]), cv2.IMREAD_COLOR)
                if is_hand:
                    m = cv2.imread(str(kit.hands[hand][1]), cv2.IMREAD_GRAYSCALE)
                    if m.shape[:2] != img.shape[:2]:  # the art was upscaled; scale the kit mask with it
                        m = cv2.resize(m, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_LINEAR)
                    mk = (m > 127).astype(np.uint8) * 255
                    quad, mask = find_green(cv2.merge([np.zeros_like(m), mk, np.zeros_like(m)]))
                else:
                    quad, mask = find_green(img)
                if quad is None:
                    warnings.append(f"{pid}: {u['kind']} is on: screen but the art has no green screen; shown as an overlay card")
                    u["on"] = "overlay"
                    continue
                qw, qh = quad_size(quad)
                kind = u["kind"]
                if kind in kit.apps and kind not in ("phone.ttok_chat", "phone.gate_status") and qh >= qw * 0.9:
                    png, meta = kit.apps[kind]
                    page.set_viewport_size({"width": meta["size"][0], "height": meta["size"][1]})
                    fills = app_fills(kind, u)
                    fills.update({b_["id"]: u[b_["id"]] for b_ in meta.get("text_boxes", []) if b_["id"] in u and b_["id"] not in ("kind", "on")})
                    video = None
                    if kind in KIT_VIDEO and u.get("source"):
                        # a stream showing what the drone filmed: a crop of the `source` panel's art (its `subject` box)
                        srcp = next((ART / f"{u['source']}{x}" for x in (".png", ".jpg", ".webp") if (ART / f"{u['source']}{x}").exists()), None)
                        if srcp:
                            vx, vy, vw, vh = KIT_VIDEO[kind]
                            im0 = Image.open(srcp).convert("RGB")
                            W0, H0 = im0.size
                            sx0, sy0, sx1, sy1 = u.get("subject", [0, 0, 1, 1])
                            bw0, bh0 = (sx1 - sx0) * W0, (sy1 - sy0) * H0
                            asp = vw / vh
                            if bw0 / bh0 < asp:
                                bw0 = bh0 * asp
                            else:
                                bh0 = bw0 / asp
                            bw0, bh0 = min(bw0, W0), min(bh0, H0)
                            cx, cy = (sx0 + sx1) / 2 * W0, (sy0 + sy1) / 2 * H0
                            l_ = min(max(cx - bw0 / 2, 0), W0 - bw0)
                            t_ = min(max(cy - bh0 / 2, 0), H0 - bh0)
                            vf = WORK / f"{pid}_stream.png"
                            im0.crop((int(l_), int(t_), int(l_ + bw0), int(t_ + bh0))).resize((vw, vh), Image.LANCZOS).save(vf)
                            video = (vf, KIT_VIDEO[kind])
                    load_html(page, kit_app_html(png, meta, fills, video), WORK / f"{pid}_app.html")
                    page.evaluate("document.fonts.ready")
                    page.evaluate(FIT_JS)
                    x0, y0, x1, y1 = meta.get("art_bounds") or [0, 0, meta["size"][0], meta["size"][1]]
                    page.screenshot(path=str(WORK / f"{pid}_ui.png"), omit_background=True,
                                    clip={"x": x0, "y": y0, "width": x1 - x0, "height": y1 - y0})
                else:
                    scale = max(1.0, 900.0 / max(qw, qh))
                    uw, uh = int(qw * scale), int(qh * scale)
                    if kind in ("phone.camera", "pc.video_editor"):
                        # the viewfinder or preview image: the subject box of this panel's art (a camera) or of the `source`
                        # panel's art (an editor showing footage), cropped to the screen's (or the preview's 16:9) shape
                        srcp = src
                        if kind == "pc.video_editor":
                            srcp = next((ART / f"{u.get('source', pid)}{x}" for x in (".png", ".jpg", ".webp") if (ART / f"{u.get('source', pid)}{x}").exists()), src)
                        im0 = Image.open(srcp).convert("RGB")
                        W0, H0 = im0.size
                        sx0, sy0, sx1, sy1 = u.get("subject", [0.25, 0.0, 0.75, 0.6] if kind == "phone.camera" else [0, 0, 1, 1])
                        bw0, bh0 = (sx1 - sx0) * W0, (sy1 - sy0) * H0
                        asp = (16 / 9) if kind == "pc.video_editor" else uw / max(1, uh)
                        if bw0 / bh0 < asp:
                            bw0 = bh0 * asp
                        else:
                            bh0 = bw0 / asp
                        bw0, bh0 = min(bw0, W0), min(bh0, H0)
                        cx, cy = (sx0 + sx1) / 2 * W0, (sy0 + sy1) / 2 * H0
                        l_ = min(max(cx - bw0 / 2, 0), W0 - bw0)
                        t_ = min(max(cy - bh0 / 2, 0), H0 - bh0)
                        camf = WORK / f"{pid}_cam.png"
                        ow, oh = (uw, uh) if kind == "phone.camera" else (960, 540)
                        im0.crop((int(l_), int(t_), int(l_ + bw0), int(t_ + bh0))).resize((ow, oh), Image.LANCZOS).save(camf)
                        u["_bg"] = str(camf)
                    page.set_viewport_size({"width": uw, "height": uh})
                    load_html(page, html_app(u, uw, uh), WORK / f"{pid}_app.html")
                    page.evaluate("document.fonts.ready")
                    page.evaluate(FIT_JS)
                    page.screenshot(path=str(WORK / f"{pid}_ui.png"), omit_background=True)
                ui = cv2.imread(str(WORK / f"{pid}_ui.png"), cv2.IMREAD_UNCHANGED)
                if ui.shape[2] == 3:
                    ui = cv2.cvtColor(ui, cv2.COLOR_BGR2BGRA)
                vis = ui[:, :, 3] > 128
                if vis.any():
                    ui_tint[pid] = tuple(float(v) for v in ui[:, :, :3][vis].mean(axis=0))
                out = composite_screen(img, quad, mask, ui)
                screens.setdefault(pid, []).append((mask > 0, ui_tint.get(pid)))
                comp = WORK / f"{pid}_comp.png"
                cv2.imwrite(str(comp), out)
                art_for[pid] = comp

        # ------------------------------------------------ green screens nobody fills: show them as dark screens
        for p in panels:
            pid = p.get("id")
            if p.get("kind") in ("title", "end") or pid not in art_for:
                continue
            img = cv2.imread(str(art_for[pid]), cv2.IMREAD_COLOR)
            tint = ui_tint.get(pid)
            changed = False
            for _ in range(8):  # the largest green area first (an unfilled screen), then reflections and spill
                q, m = find_green(img)
                if q is None:
                    break
                region = cv2.dilate(m, np.ones((5, 5), np.uint8)) > 0
                if tint is None and not changed:
                    img[region] = (30, 27, 31)
                    screens.setdefault(pid, []).append((region, None))
                    warnings.append(f"{pid}: green screen in the art with no `on: screen` ui; filled dark")
                else:
                    # a reflection of the screen (wet road, glass) or spill: keep its brightness, take the screen's
                    # colour (28 Oct: filling ch004 P56's road reflection dark left a black hole in the asphalt)
                    lum = img[:, :, 1][region].astype(np.float32) / 255.0
                    col = np.array(tint if tint is not None else (54, 50, 56), np.float32)
                    img[region] = np.clip(col[None, :] * (0.45 + 0.75 * lum[:, None]), 0, 255).astype(np.uint8)
                    warnings.append(f"{pid}: green reflection recoloured to its screen's colour")
                changed = True
            # The green screen's soft spill (its glow on the desk, a hand, hair, the wall) is too faint for find_green.
            # Around each screen, the green excess becomes the screen's own light (a dark screen casts none), fading
            # with distance (28 Oct: ch005 P39's desk and Seoa's hair stayed lime green beside a white budget page).
            # Natural greens are kept: teal (a painted roof, dark monitors) by hue, a whole green surround (ch010 P24's
            # green roof) by area, and anything else by `despill: false` on the panel (ch005 P17's pot plant).
            if pid in screens and p.get("despill", True):
                f32 = img.astype(np.float32)
                bb, gg, rr = f32[:, :, 0], f32[:, :, 1], f32[:, :, 2]
                hue = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)[:, :, 0]
                for smask, stint in screens[pid]:
                    sm = (smask.astype(np.uint8) if smask.shape[:2] == img.shape[:2]
                          else cv2.resize(smask.astype(np.uint8), (img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST))
                    if not sm.any():
                        continue
                    ys_, xs_ = np.nonzero(sm)
                    reach = 1.4 * max(xs_.max() - xs_.min(), ys_.max() - ys_.min()) + 8
                    dist = cv2.distanceTransform((1 - sm).astype(np.uint8), cv2.DIST_L2, 5)
                    w = np.clip((reach - dist) / (0.4 * reach), 0, 1) * (sm == 0) * (hue <= 72)
                    excess = gg - np.maximum(rr, bb)
                    ring = (dist < reach) & (sm == 0)
                    if ((excess > 12) & ring & (hue <= 72)).sum() > 0.2 * max(1, ring.sum()):  # ch1-10: 0.05 at most, ch010 P24 0.37
                        warnings.append(f"{pid}: screen spill kept (the screen sits in a green surround)")
                        continue
                    spill = np.clip(excess, 0, None) * w
                    if spill.max() < 4:
                        continue
                    gg -= spill
                    if stint is not None:
                        c = np.array(stint, np.float32); c = c / max(1.0, c.max())  # BGR, brightest channel 1
                        bb += spill * c[0]; gg += spill * c[1]; rr += spill * c[2]
                    changed = True
                    warnings.append(f"{pid}: screen spill recoloured" + ("" if stint is not None else " (dark screen)"))
                img = np.clip(np.dstack([bb, gg, rr]), 0, 255).astype(np.uint8)
            if changed:
                fixed = WORK / f"{pid}_dark.png"
                cv2.imwrite(str(fixed), img)
                art_for[pid] = fixed

        # ------------------------------------------------ collect lettering
        items = []
        beside_shapes = ("inset-l", "inset-r", "narrow-l", "narrow-r")
        mode = {}  # panel id -> 'beside' or 'gutter'
        for p in panels:
            if p.get("kind") in ("title", "end"):
                continue
            shape = p.get("shape", "wide")
            fw = SHAPES.get(shape, SHAPES["wide"])[0]
            mode[p["id"]] = "beside" if shape in beside_shapes else "gutter"
            for ln in p.get("lines") or []:
                t = ln.get("type", "speech")
                if t == "system":
                    continue
                items.append({"panel": p["id"], "shape": shape, "ln": ln, "type": t, "toks": tokenize(ln["text"]),
                              "beside_w": W - fw - 40 * 2 - 26, "gutter_w": int(W * (0.94 if t in ("shout", "intense") else 0.66))})

        # ------------------------------------------------ pass 1: measure text at candidate widths (with line breaks)
        meas_divs = []
        for i, it in enumerate(items):
            if it["type"] not in BITMAP_TYPES:
                continue
            fam, wt, fs, lh, col = TYPE_FONT[it["type"]]
            for cw in WIDTH_CANDS:
                meas_divs.append(f'<div class="m" data-i="{i}" data-cw="{cw}" style="max-width:{cw}px;font:{wt} {fs}px/{lh} {fam}">{measure_html(it["toks"])}</div>')
        page.set_viewport_size({"width": 1400, "height": 900})
        load_html(page, f"<!doctype html><html><head><meta charset='utf-8'>{FONT_LINKS}<style>{FONTS}"
                  ".m{display:inline-block;width:fit-content;text-align:center;text-wrap:balance;position:absolute;left:0;top:0;white-space:normal}"
                  f"</style></head><body>{''.join(meas_divs)}</body></html>", WORK / "measure.html")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(150)
        meas = page.evaluate("""() => [...document.querySelectorAll('.m')].map(e => {
            const r0 = e.getBoundingClientRect();
            // a word longer than the box overflows it: measure the words' own extent, not the box's (judge, ch 2-3)
            let L = r0.left, R = r0.right;
            e.querySelectorAll('.w').forEach(w => { const q = w.getBoundingClientRect(); L = Math.min(L, q.left); R = Math.max(R, q.right); });
            const r = {width: R - L, height: r0.height};
            const lines = []; let top = null, cur = [];
            e.querySelectorAll('.w').forEach(w => {
              const t = w.getBoundingClientRect().top;
              if (top === null || Math.abs(t - top) > 4) { if (cur.length) lines.push(cur); cur = []; top = t; }
              cur.push(+w.dataset.k);
            });
            if (cur.length) lines.push(cur);
            return [+e.dataset.i, +e.dataset.cw, r.width, r.height, lines]; })""")
        by_i = {}
        for i, cw, w_, h_, lns in meas:
            by_i.setdefault(i, []).append((cw, w_, h_, lns))

        def pick(it, maxw):
            kind = it["type"]
            ents = kit.bubbles.get(kind) or kit.bubbles.get("speech")
            best = None
            for cw, w_, h_, lns in by_i.get(items.index(it), []):
                if len(lns) > 6:
                    continue
                c = choose_bubble(ents, w_, h_, maxw, MIN_BUBBLE.get(kind), len(lns))
                if c and (best is None or c[0] < best[0][0]):
                    best = (c, cw, lns)
            return best

        for it in items:
            if it["type"] in BITMAP_TYPES and mode[it["panel"]] == "beside" and pick(it, it["beside_w"]) is None:
                mode[it["panel"]] = "gutter"
            if it["type"] in ("narr", "narr_dark", "inner", "note", "link") and mode[it["panel"]] == "beside" and len(it["ln"]["text"]) > 70:
                mode[it["panel"]] = "gutter"
        for it in items:
            kind = it["type"]
            if kind not in BITMAP_TYPES:
                continue
            maxw = it["beside_w"] if mode[it["panel"]] == "beside" else it["gutter_w"]
            best = pick(it, maxw)
            if best is None:
                warnings.append(f"{it['panel']}: line too long for any bubble: {it['ln']['text'][:40]}")
                cw, w_, h_, lns = by_i[items.index(it)][-1]
                ents = kit.bubbles.get(kind) or kit.bubbles.get("speech")
                best = (choose_bubble(ents, w_, h_, 10 ** 6, None, len(lns)), cw, lns)
            (cost, e, sx, sy, BW, BH), cw, lns = best
            it.update(blank=e, sx=sx, sy=sy, bw=BW, bh=BH, cw=cw, lines=lns)
            it["dil"] = 0 if kind == "intense" else round(max(0.0, 2.5 - e["stroke"] * min(sx, sy)), 2)

        # ------------------------------------------------ pass 2: build the strip
        state = {"line_no": 0}
        lines_meta = []
        blocks = []
        prev_bg = None
        pindex = 0
        it_by_line = {id(it["ln"]): it for it in items}

        def letter_html(it, where, tail=True):
            ln, t = it["ln"], it["type"]
            side = ln.get("side", "c")
            attr = ""
            if t in VOICED and not ln.get("unvoiced"):
                state["line_no"] += 1
                attr = f' data-a="L{state["line_no"]}"'
                lines_meta.append({"i": state["line_no"], "who": ln.get("who", "narr"), "type": t, "text": ln["text"], "panel_id": it["panel"]})
            common = f'data-panel="{E(it["panel"])}" data-side="{side}" data-where="{where}" data-type="{t}"'
            if ln.get("_off"):
                common += ' data-off="1"'
            elif ln.get("_head"):
                common += f' data-hx="{ln["_head"][0]:.3f}" data-hy="{ln["_head"][1]:.3f}"'
            if t in BITMAP_TYPES:
                e, sx, sy = it["blank"], it["sx"], it["sy"]
                rx, ry, rw, rh = e["rect"]
                fam, wt, fs, lh, col = TYPE_FONT[t]
                d = it["dil"]
                filt = (f"filter:drop-shadow({d}px 0 0 {e['line']}) drop-shadow(-{d}px 0 0 {e['line']}) drop-shadow(0 {d}px 0 {e['line']}) drop-shadow(0 -{d}px 0 {e['line']});"
                        if d >= 0.4 else "")
                return (f'<div class="lt bm t-{t} s-{side}"{attr} {common} data-blank="{e["name"]}" data-sx="{sx:.4f}" data-sy="{sy:.4f}" data-d="{d}" '
                        f'data-tail="{1 if tail else 0}" style="width:{it["bw"]:.1f}px;height:{it["bh"]:.1f}px">'
                        f'<img class="bimg" src="{uri(e["png"])}" style="{filt}">'
                        f'<div class="btxt" style="left:{rx * sx:.1f}px;top:{ry * sy:.1f}px;width:{rw * sx:.1f}px;height:{rh * sy:.1f}px">'
                        f'<span style="white-space:nowrap;font:{wt} {fs}px/{lh} {fam};color:{col}">{lines_html(it["toks"], it["lines"])}</span></div></div>')
            n = len(ln["text"])
            cap = it["beside_w"] if (where == "beside") else W
            if t in ("narr", "narr_dark", "inner", "link"):
                w = int(min(W * .74, cap, max(W * .30, 240 + n * 6.0)))
            elif t == "note":
                w = int(min(W * .66, cap, max(W * .34, 220 + n * 6.6)))
            elif t == "float":
                w = int(min(W * .62, cap, max(W * .26, 190 + n * 6.2)))
            else:
                w = 0
            style = f"width:{w}px" if w else ""
            return f'<div class="lt t-{t} s-{side}"{attr} {common} style="{style}"><span>{fmt_text(ln["text"])}</span></div>'

        for p in panels:
            kind = p.get("kind")
            bg = p.get("bg", "white")
            if kind in ("title", "end") and kind in kit.cards:
                bg = "#101218"  # the kit cards are dark: blend into them, not into white
            col = bg_hex(bg)
            dark = is_dark(bg)
            gap = p.get("gap", "short")
            gh = GAPS.get(gap, 84)
            pc = bg_hex(prev_bg) if prev_bg else col
            if gap == "black":
                blocks.append(f'<div class="blk gap" style="height:{gh}px;background:linear-gradient({pc},#0a0a0d 22%,#0a0a0d 78%,{col})"></div>')
            elif gap == "fade-black":
                blocks.append(f'<div class="blk gap" style="height:{gh}px;background:linear-gradient({pc},#0a0a0d)"></div>')
            elif gap == "fade-white":
                blocks.append(f'<div class="blk gap" style="height:{gh}px;background:linear-gradient({pc},#ffffff)"></div>')
            elif pc != col:
                blocks.append(f'<div class="blk gap" style="height:{max(gh, 300)}px;background:linear-gradient({pc},{col})"></div>')
            elif prev_bg is not None:
                blocks.append(f'<div class="blk gap" style="height:{gh}px;background:{col}"></div>')
            prev_bg = bg
            dcls = " dark" if dark else ""
            if kind == "title":
                # v2 scripts carry the line as title_card ("MY SUMMONS GO FIRST · CHAPTER 1 · BAIT"); the logo already names the series
                ttl = p.get("title_text") or re.sub(r"^\s*MY SUMMONS GO FIRST\s*·\s*", "", str(p.get("title_card", "")), flags=re.I)
                p["title_text"] = ttl
                if "title" in kit.cards:
                    blocks.append(card_html(kit.cards["title"], {"chapter": ttl}, W))
                else:
                    logo = (f'<img class="logo" src="{uri(kit.logo)}">' if kit.logo else
                            '<div class="logo-t">MY SUMMONS<br><span>GO FIRST</span></div>')
                    blocks.append(f'<div class="blk title{dcls}" style="background:{col}">{logo}<div class="t-line">{E(p.get("title_text", ""))}</div></div>')
                continue
            if kind == "end":
                chibi = next((ART / f"END{x}" for x in (".png", ".jpg", ".webp") if (ART / f"END{x}").exists()), None)
                if chibi:
                    chibi = upscaled(chibi)
                if not chibi:
                    warnings.append("END: no chibi gag art (ART/END.png)")
                if "end" in kit.cards:
                    # the cliffhanger runs straight into TO BE CONTINUED; the chibi gag comes after it, as a bonus (judge, ch 2)
                    blocks.append(card_html(kit.cards["end"], {"continuing": p.get("end_text", "TO BE CONTINUED"), "teaser": p.get("next", "")}, W))
                    if chibi:
                        blocks.append(f'<div class="blk" style="background:{col};padding:110px 0 110px"><div class="pbox chibi-end"><img src="{uri(chibi)}"></div></div>')
                else:
                    cimg = f'<img class="end-chibi" src="{uri(chibi)}">' if chibi else ""
                    blocks.append(f'<div class="blk endcard{dcls}" style="background:{col}"><div class="e-tbc">{E(p.get("end_text", "TO BE CONTINUED"))}</div>'
                                  f'<div class="e-next">{E(p.get("next", ""))}</div>{cimg}</div>')
                continue
            pindex += 1
            pid = p["id"]
            shape = p.get("shape", "wide")
            fw, fh, align, frame = SHAPES.get(shape, SHAPES["wide"])
            if p.get("kind") == "caption":
                frame = "cap"
            src = art_for[pid]
            iw, ih = Image.open(src).size
            if fh is None:
                fh = max(int(fw * 0.62), min(int(round(fw * ih / iw)), fw))
            focus = p.get("focus", [0.5, 0.5])
            inner = []
            ui = p.get("ui") or []
            floats = [u for u in ui if u.get("on") == "float"]
            for k, u in enumerate(floats):
                kk = u["kind"].split(".", 1)[-1]
                # A one-line glitch message would sit alone in the big glitch window (a mostly empty frame that covers the
                # art), so it uses the compact notice bar instead, with a chromatic glitch treatment.
                glitchy = False
                if kk == "glitch" and not u.get("body") and not u.get("button"):
                    glitchy = True
                    kk = "notice_small" if len(str(u.get("text", u.get("headline", "")))) <= 26 else "notice"
                if u["kind"] == "phone.live_stream":
                    inner.append(live_stream_html(u))
                    continue
                if not u["kind"].startswith("system.") or not kit.system_tpl(kk):
                    inner.append(f'<div class="ovl">{fmt_text(u.get("text", u["kind"]))}</div>')
                    continue
                png, meta = kit.system_tpl(kk)
                sw_, sh_ = meta["size"]
                fill = {"operator": "OPERATOR INTERFACE"}
                if kk in ("notice", "notice_small", "warning"):
                    fill["headline"] = u.get("text", u.get("headline", ""))
                elif kk in ("window", "glitch"):
                    # a window's button bar is never left empty (28 Oct: ch006 P41, ch008 P66 showed a blank bar): OK
                    fill.update(headline=u.get("headline", u.get("text", "")), body=u.get("body", ""),
                                button=u.get("button", "OK" if kk == "window" else ""))
                elif kk == "summon_card":
                    fill["name"] = u.get("name", u.get("text", ""))
                elif kk == "log":
                    fill.update(headline=u.get("headline", "[INTERFACE LOG]"), entries="\n".join(u.get("lines", [])))
                elif kk == "button":
                    fill = {"button": u.get("text", "")}
                texts = []
                for b in meta.get("text_boxes", []):
                    v = fill.get(b["id"])
                    if not v:
                        continue
                    x, y, bw_, bh_ = b["rect"]
                    ml = b.get("max_lines", 1)
                    mono = kk == "log" and b["id"] == "entries"
                    fsz = (bh_ / max(1, ml)) * (0.78 if b["id"] != "operator" else 0.72)
                    if mono:
                        fsz = min(fsz, 34)
                    cls = "stx" + (" mono" if mono else "") + (" op" if b["id"] == "operator" else "") + (" nw" if ml == 1 else "")
                    texts.append(f'<div class="{cls}" style="left:{x / sw_ * 100:.3f}%;top:{y / sh_ * 100:.3f}%;width:{bw_ / sw_ * 100:.3f}%;height:{bh_ / sh_ * 100:.3f}%;'
                                 f'color:{b.get("color", "#E8FBFF")};justify-content:{"flex-start" if mono else "center"};text-align:{"left" if mono else "center"}">'
                                 f'<span data-fs="{fsz / sw_:.5f}">{fmt_text(v)}</span></div>')
                at = u.get("at")
                if at:
                    left, top = at[0] * 100, at[1] * 100
                else:
                    left = 50 + (0 if len(floats) == 1 else (-6 if k % 2 == 0 else 6))
                    top = {"top": 9, "top-left": 9, "top-right": 9, "center": 30, "bottom": 58}.get(p.get("calm"), 12) + k * 24
                tilt = u.get("tilt", -8 if k % 2 == 0 else 7)
                mirror = " mir" if u.get("mirror") else ""
                inner.append(f'<div class="syswin k-{kk}{mirror}{" glitchy" if glitchy else ""}" data-tilt="{tilt}" style="--wf:{u.get("wf", SYS_WFRAC.get(kk, .66))};left:{left}%;top:{top}%;aspect-ratio:{sw_}/{sh_}">'
                             f'<img src="{uri(png)}">{"".join(texts)}</div>')
                txt = ". ".join(filter(None, [fill.get("headline"), fill.get("body"), fill.get("name"), fill.get("button")] + list(u.get("lines", []) or [])))
                if txt:
                    state["line_no"] += 1
                    lines_meta.append({"i": state["line_no"], "who": "system", "type": "system", "text": txt, "panel_id": pid})
                    inner.append(f'<div class="sysanchor" data-a="L{state["line_no"]}" style="top:{top}%"></div>')
            for u in ui:
                if u.get("kind") == "label":
                    lx, ly = u.get("at", [0.5, 0.3])
                    inner.append(f'<div class="label" style="left:{lx * 100:.1f}%;top:{ly * 100:.1f}%;font-size:{u.get("size", 44)}px;'
                                 f'color:{u.get("color", "#1f3f9a")};transform:translate(-50%,-50%) rotate({u.get("rot", -3)}deg)">{fmt_text(u.get("text", ""))}</div>')
                    continue
                if u.get("on") == "overlay":
                    ot = ovl_text(u)
                    if ot:
                        inner.append(f'<div class="ovl">{fmt_text(ot)}</div>')
                elif u.get("on") == "panel":
                    if u["kind"] == "phone.ttok_video_call":
                        inner.append(f'<iframe class="appl" srcdoc="{E(video_call_chrome(u, fw, fh))}"></iframe>')
                    else:
                        inner.append(f'<iframe class="appl full" srcdoc="{E(html_app(u, fw, fh))}"></iframe>')
            over = []  # drawn above the panel, unclipped: SFX may break the frame, tags straddle it
            for sx_ in p.get("sfx") or []:
                st = sx_.get("style", "impact")
                size = {"S": 46, "M": 78, "L": 118, "XL": 176}.get(str(sx_.get("size", "M")), 78)
                rot = float(sx_.get("rot", -6))
                x, y = sx_.get("at", [.5, .5])
                txt = str(sx_["text"])
                vertical = abs(abs(rot) - 90) < 1
                est = len(txt) * size * (0.56 if st in ("summon", "gate") else 0.66)  # rough rendered length
                room = (fh if vertical else fw) * 1.05
                if est > room:
                    size = max(30, int(size * room / est))
                rnd = random.Random(f"{pid}{txt}{x}{y}")
                # Each letter bounces a little, but neighbours never drift apart: a letter may not sit more than 1.5 px
                # right of the one before it or more than 7 px above or below it (a gap read as two words: "VMMM M").
                jit, px_, py_ = [], None, None
                for ch in txt:
                    jx, jy, jr, js = rnd.uniform(-3, 3), rnd.uniform(-6, 6), rnd.uniform(-7, 7), rnd.uniform(.93, 1.08)
                    if px_ is not None and not vertical:
                        jx = min(jx, px_ + 1.5)
                        jy = max(min(jy, py_ + 7), py_ - 7)
                    jit.append((jx, jy, jr, js)); px_, py_ = jx, jy
                letters = "".join(
                    f'<span style="display:inline-block;transform:translate({jx:.1f}px,{jy:.1f}px) rotate({jr:.1f}deg) scale({js:.2f})">{E(ch) if ch != " " else "&nbsp;"}</span>'
                    + ("<br>" if vertical else "") for ch, (jx, jy, jr, js) in zip(txt, jit))
                over.append(f'<div class="sfx x-{st}{" vert" if vertical else ""}" style="left:{x * 100:.1f}%;top:{y * 100:.1f}%;font-size:{size}px;'
                            f'transform:translate(-50%,-50%) rotate({0 if vertical else rot}deg)">{letters}</div>')
            if p.get("intro"):  # a character's first appearance: a nameplate in the manhwa style
                nm, _, role = str(p["intro"]).partition("·")
                over.append(f'<div class="intro"><b>{E(nm.strip())}</b>{"<span>" + E(role.strip(" ·")) + "</span>" if role else ""}</div>')
            lines = [ln for ln in (p.get("lines") or []) if ln.get("type") != "system"]
            tags = [ln for ln in lines if ln.get("type") == "tag"]
            foots = [ln for ln in lines if ln.get("type") == "footnote"]
            talk = [ln for ln in lines if ln.get("type") not in ("tag", "footnote")]
            over += [letter_html(it_by_line[id(t_)], "tag") for t_ in tags]
            pnl = (f'<div class="pbox" style="width:{fw}px;height:{fh}px">'
                   f'<div class="pnl {frame} sh-{shape}" data-p="P{pindex}" data-id="{E(pid)}"{faces_attr(pid)} style="width:{fw}px;height:{fh}px">'
                   f'<img class="art" src="{uri(src)}" style="object-position:{focus[0] * 100:.0f}% {focus[1] * 100:.0f}%">{"".join(inner)}</div>'
                   f'<div class="pov">{"".join(over)}</div></div>')

            def group(lns, where):
                # two bubbles from speakers on opposite sides: a staggered pair across the gutter (read order = height)
                if len(lns) == 2 and where in ("before", "after"):
                    a_, b_ = (it_by_line[id(x)] for x in lns)
                    sa, sb = lns[0].get("side", "c"), lns[1].get("side", "c")
                    if (a_["type"] in BITMAP_TYPES and b_["type"] in BITMAP_TYPES and sa != sb and "c" not in (sa, sb)
                            and a_["bw"] + b_["bw"] + 40 <= W * 0.9):
                        h1 = letter_html(a_, where, True)
                        drop = int(a_["bh"] * 0.42)
                        h2 = letter_html(b_, where, True).replace('style="width:', f'style="margin-top:{drop}px;width:', 1)
                        left, right = (h1, h2) if sa == "l" else (h2, h1)
                        return f'<div class="pair">{left}{right}</div>'
                out = []
                for j, ln in enumerate(lns):
                    nxt = lns[j + 1] if j + 1 < len(lns) else None
                    prv = lns[j - 1] if j > 0 else None
                    same = lambda o: o is not None and o.get("who") == ln.get("who") and o.get("type", "speech") == ln.get("type", "speech")
                    tail = not (where == "before" and same(nxt)) and not (where == "after" and same(prv))
                    out.append(letter_html(it_by_line[id(ln)], where, tail))
                return "".join(out)

            def ov(lns, first):
                """How far the gutter group overlaps the panel edge (negative = keeps a gap)."""
                if not lns:
                    return 0
                its = [it_by_line[id(x)] for x in lns]
                if len(its) == 2 and all(i["type"] in BITMAP_TYPES for i in its) and lns[0].get("side", "c") != lns[1].get("side", "c") \
                        and "c" not in (lns[0].get("side", "c"), lns[1].get("side", "c")) and its[0]["bw"] + its[1]["bw"] + 40 <= W * 0.9:
                    if first:   # after-group: the higher bubble (read first) touches the panel
                        return int(min(0.36 * its[0]["bh"], 84))
                    bh1, bh2 = its[0]["bh"], its[1]["bh"]
                    return int(min(0.36 * (bh2 if 0.42 * bh1 + bh2 >= bh1 else bh1), 84))
                it = its[0] if first else its[-1]
                return int(min(0.36 * it["bh"], 84)) if it["type"] in BITMAP_TYPES else -16

            # Gutter bubbles straddle the panel edge, but never over a face: where a drawn head sits near the top
            # (or bottom) edge, the group overlaps the panel only down to just above that head (or sits clear of it).
            Hh_ = heads.get(pid) or {}
            sc_ = max(fw / iw, fh / ih)
            offy_ = (fh - ih * sc_) * focus[1]
            hy_ = [(b_[1] * ih * sc_ + offy_, b_[3] * ih * sc_ + offy_) for b_ in Hh_.values()
                   if isinstance(b_, (list, tuple)) and len(b_) == 4]
            head_top_ = min((a_ for a_, _ in hy_), default=None)
            head_bot_ = max((b_ for _, b_ in hy_), default=None)

            def ov_safe(lns, first):
                v_ = ov(lns, first)
                if first and head_bot_ is not None:
                    v_ = min(v_, int(fh - head_bot_ - 12))
                if not first and head_top_ is not None:
                    v_ = min(v_, int(head_top_ - 12))
                return max(v_, -16)

            if mode.get(pid) == "beside":
                col_html = group(talk, "beside")
                foot_html = "".join(letter_html(it_by_line[id(f_)], "foot") for f_ in foots)
                row = (f'<div class="row">{pnl}<div class="beside">{col_html}</div></div>' if align == "l"
                       else f'<div class="row"><div class="beside">{col_html}</div>{pnl}</div>')
                blocks.append(f'<div class="blk{dcls}" style="background:{col}">{row}{foot_html}</div>')
            else:
                calm = p.get("calm", "")
                if any(isinstance(u, dict) and u.get("kind") == "tv.lowerthird" and u.get("on") == "panel" for u in p.get("ui") or []):
                    calm = "top"  # the news graphic fills the bottom edge: bubbles there would cover it (28 Oct, ch004 P57)
                if calm in ("bottom", "bottom-left", "bottom-right"):
                    before, after = (talk[:1], talk[1:]) if len(talk) >= 3 else ([], talk)
                elif len(talk) >= 3:
                    half = (len(talk) + 1) // 2
                    before, after = talk[:half], talk[half:]
                else:
                    before, after = talk, []
                g1 = group(before, "before")
                pw_html = f'<div class="pwrap a-{align}">{pnl}</div>'
                g2 = group(after, "after")
                foot_html = "".join(letter_html(it_by_line[id(f_)], "foot") for f_ in foots)
                blocks.append(f'<div class="blk{dcls}" style="background:{col}">'
                              + (f'<div class="gut before" style="margin-bottom:{-ov_safe(before, False)}px">{g1}</div>' if g1 else "")
                              + pw_html
                              + (f'<div class="gut after" style="margin-top:{-ov_safe(after, True)}px">{g2}</div>' if g2 else "")
                              + foot_html + "</div>")

        doc = (f'<!doctype html><html><head><meta charset="utf-8">{FONT_LINKS}<style>{strip_css(W)}</style></head>'
               f'<body>{"".join(blocks)}</body></html>')
        (OUT / "strip.html").write_text(doc, encoding="utf-8")
        # the final strip renders at A.dpr device pixels per layout pixel (sharp lettering, no upscaling later)
        sctx = br.new_context(device_scale_factor=A.dpr)
        page = sctx.new_page(); page.set_default_timeout(240000)
        page.set_viewport_size({"width": W, "height": 1600})
        page.goto(uri(OUT / "strip.html"), wait_until="load")
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(400)
        page.evaluate(SYS_JS)
        wins_moved = page.evaluate(WINFACE_JS)
        if wins_moved:
            print(f"system windows moved off faces: {wins_moved}")
        ntails = page.evaluate(TAIL_JS, kit.profiles_js())
        tags_moved = page.evaluate(TAG_JS)
        if tags_moved:
            print(f"place tags moved off bubbles: {tags_moved}")
        sfx_fix = page.evaluate(SFX_JS)
        warnings += [f"SFX COVERS A BUBBLE (no room to move it): {t_}" for t_ in sfx_fix["stuck"]]
        warnings += [f"SFX COVERS A FACE (no room to move it): {t_}" for t_ in sfx_fix.get("onface", [])]
        page.wait_for_timeout(200)
        geo = page.evaluate("""() => {
          const r = e => { const b = e.getBoundingClientRect(); return {x0:b.left, y0:b.top+scrollY, x1:b.right, y1:b.bottom+scrollY}; };
          return {H: document.documentElement.scrollHeight,
            lines: [...document.querySelectorAll('[data-a]')].map(e => ({a:e.dataset.a, ...r(e)})),
            panels: [...document.querySelectorAll('.pnl')].map(e => ({p:e.dataset.p, id:e.dataset.id, ...r(e)})),
            texts: [...document.querySelectorAll('.lt')].map(e => ({t:e.textContent.slice(0,40), cls:e.className, ...r(e)})),
            blocks: [...document.querySelectorAll('.blk')].map(r),
            // system windows that cover a drawn face (28 Oct: ch008 P07's notice sat over Nib's head)
            winface: [...document.querySelectorAll('.pnl')].flatMap(p => {
              const faces = p.dataset.faces ? JSON.parse(p.dataset.faces) : [];
              const img = p.querySelector('img.art');
              if (!faces.length || !img || !img.naturalWidth) return [];
              const fw = p.clientWidth, fh = p.clientHeight, iw = img.naturalWidth, ih = img.naturalHeight;
              const sc = Math.max(fw / iw, fh / ih);
              const pos = (getComputedStyle(img).objectPosition || '50% 50%').split(' ').map(v => parseFloat(v) / 100);
              const offx = (fw - iw * sc) * (isNaN(pos[0]) ? .5 : pos[0]), offy = (fh - ih * sc) * (isNaN(pos[1]) ? .5 : pos[1]);
              const pb = p.getBoundingClientRect(), hits = [];
              p.querySelectorAll('.syswin').forEach(w => {
                const b = w.getBoundingClientRect();
                const wx0 = b.left - pb.left, wy0 = b.top - pb.top, wx1 = b.right - pb.left, wy1 = b.bottom - pb.top;
                faces.forEach(f => {
                  const fx0 = f[0] * iw * sc + offx, fy0 = f[1] * ih * sc + offy, fx1 = f[2] * iw * sc + offx, fy1 = f[3] * ih * sc + offy;
                  const ix = Math.max(0, Math.min(wx1, fx1) - Math.max(wx0, fx0)), iy = Math.max(0, Math.min(wy1, fy1) - Math.max(wy0, fy0));
                  const fa = (fx1 - fx0) * (fy1 - fy0);
                  if (fa > 0 && ix * iy / fa > 0.3) hits.push(p.dataset.id);
                });
              });
              return hits;
            })};
        }""")
        warnings += [f"SYSTEM WINDOW COVERS A FACE: {pid_}" for pid_ in sorted(set(geo.get("winface", [])))]
        # capture in bands (one full-page capture at 2x can exceed the browser's surface limits) and stitch losslessly
        Hc = int(geo["H"])
        page.set_viewport_size({"width": W, "height": min(Hc, 4000)})
        strip_img = Image.new("RGB", (W * A.dpr, Hc * A.dpr), "white")
        band = 4000
        for y_ in range(0, Hc, band):
            h_ = min(band, Hc - y_)
            part = WORK / "strip_band.png"
            page.screenshot(path=str(part), full_page=True, clip={"x": 0, "y": y_, "width": W, "height": h_})
            with Image.open(part) as im_:
                if im_.size != (W * A.dpr, h_ * A.dpr):
                    warnings.append(f"STRIP BAND SIZE {im_.size} at y={y_}, expected {(W * A.dpr, h_ * A.dpr)}")
                strip_img.paste(im_.convert("RGB"), (0, y_ * A.dpr))
        strip_img.save(OUT / "strip.png", compress_level=6)
        br.close()

    # ------------------------------------------------ checks
    for t in geo["texts"]:
        if t["x0"] < -1 or t["x1"] > W + 1:
            warnings.append(f"OFF-PAGE: {t['t']}")
    gl = [t for t in geo["texts"] if "t-tag" not in t["cls"]]
    for tg in [t for t in geo["texts"] if "t-tag" in t["cls"]]:  # 28 Oct: ch005 P01's place tag hidden under a bubble
        for b2 in gl:
            if tg["x0"] < b2["x1"] - 6 and tg["x1"] > b2["x0"] + 6 and tg["y0"] < b2["y1"] - 6 and tg["y1"] > b2["y0"] + 6:
                warnings.append(f"TAG UNDER A BUBBLE: {tg['t'][:25]} / {b2['t'][:25]}")
    for i, a in enumerate(gl):
        for b2 in gl[i + 1:]:
            if a["x0"] < b2["x1"] - 10 and a["x1"] > b2["x0"] + 10 and a["y0"] < b2["y1"] - 10 and a["y1"] > b2["y0"] + 10:
                warnings.append(f"BUBBLE OVERLAP: {a['t'][:25]} / {b2['t'][:25]}")

    # ------------------------------------------------ segments
    H = geo["H"]
    spans = [(p["y0"], p["y1"]) for p in geo["panels"]] + [(t["y0"] - 60, t["y1"] + 60) for t in geo["texts"]]

    def safe(y):
        return all(not (a + 2 < y < b - 2) for a, b in spans)
    cands = sorted({int(round(b["y1"])) for b in geo["blocks"]} | {int(round(b["y0"])) for b in geo["blocks"]})
    cands = [y for y in cands if 0 < y < H and safe(y)]
    cuts, top = [], 0
    while H - top > A.seg_max:
        ok = [y for y in cands if A.seg_min <= y - top <= A.seg_max]
        if not ok:
            ok = [y for y in range(top + A.seg_max, top + A.seg_min, -8) if safe(y)][:1] or [top + A.seg_max]
            if not safe(ok[0]):
                warnings.append(f"HARD CUT at {ok[0]}")
        y = max(ok)
        cuts.append(y)
        top = y
    bounds = [0] + cuts + [H]
    strip = strip_img
    for old in OUT.glob("[0-9][0-9][0-9].webp"):
        old.unlink()
    segs = []
    for k in range(len(bounds) - 1):
        a, b = bounds[k], bounds[k + 1]
        name = f"{k + 1:03d}.webp"
        strip.crop((0, a * A.dpr, W * A.dpr, b * A.dpr)).save(OUT / name, "WEBP", lossless=True, quality=80, method=4)
        segs.append({"file": name, "top": a, "height": b - a})

    def seg_of(y):
        for s in segs:
            if s["top"] <= y <= s["top"] + s["height"]:
                return s
        return segs[-1]
    gl_ = {g["a"]: g for g in geo["lines"]}
    for m in lines_meta:
        g = gl_.get(f"L{m['i']}")
        if not g:
            continue
        s = seg_of(g["y1"] - 1)
        m.update({"y_top": round(g["y0"]), "y_bottom": round(g["y1"]), "segment": s["file"],
                  "seg_y": min(s["height"], round(g["y1"] - s["top"]))})
    pls = []
    for p in geo["panels"]:
        s = seg_of(p["y1"] - 1)
        pls.append({"p": int(p["p"][1:]), "id": p["id"], "y_top": round(p["y0"]), "y_bottom": round(p["y1"]),
                    "segment": s["file"], "seg_y_bottom": min(s["height"], round(p["y1"] - s["top"]))})
    layout = {"chapter": S.get("chapter"), "title": S.get("title"), "width": W, "height": H, "scale": A.dpr,
              "segments": [[s["file"], s["height"]] for s in segs], "segment_tops": [s["top"] for s in segs],
              "lines": lines_meta, "panels": pls, "warnings": warnings}
    json.dump(layout, open(OUT / "layout.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"height {H} | segments {len(segs)} | voiced lines {len(lines_meta)} | panels {len(pls)} | tails {ntails}")
    print("WARNINGS:", warnings[:40] or "none", f"(+{len(warnings) - 40} more)" if len(warnings) > 40 else "")


if __name__ == "__main__":
    main()
