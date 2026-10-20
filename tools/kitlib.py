"""kitlib: loads the Codex UI kit (bubbles, system windows, phone apps, phone hands) for autostrip2.

Every blank is cropped to its artwork and saved, with measured metadata, under <kit>/_engine/:
- bubbles: text rect, centre, outline radius per degree (for tails), outline thickness, fill and line colours;
- system windows and phone apps: text boxes, as delivered by Codex.
The cache is rebuilt whenever a source PNG or JSON changes.
"""
import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image

BUBBLE_SETS = {
    "speech": ["speech_1x1", "speech_1_3x1", "speech_1_7x1", "speech_2_2x1", "speech_3x1", "speech_1x1_3"],
    "shout": ["shout_small", "shout_medium", "shout_wide"],
    "intense": ["intense_1x1", "intense_1_6x1", "intense_2_4x1"],
    "thought": ["thought_1_3x1", "thought_2x1"],
    "nervous": ["nervous_1_4x1", "nervous_2_2x1"],
    "whisper": ["whisper_1_4x1", "whisper_2_2x1"],
    "menace": ["menace_1_4x1", "menace_2_2x1"],
    "monster": ["menace_monster_1_4x1", "menace_monster_2_2x1"],
    "phone": ["phone_voice_1_4x1", "phone_voice_2_2x1"],
    "announce": ["announce_1_3x1", "announce_2x1"],
}
DARK_FILL = {"menace", "monster"}
APP_KINDS = {  # ui kind -> kit/phone blank name
    "phone.ttok_chat": "ttok_chat", "phone.ttok_call": "ttok_call", "phone.ttok_notification": "ttok_notification",
    "phone.ttok_video_call": "ttok_video_call", "phone.bank_transfer": "bank_transfer",
    "phone.emergency_alert": "emergency_alert", "phone.gate_status": "gate_status",
    "phone.aao_booking": "aao_booking", "phone.aao_result": "aao_result", "phone.quickhaul_order": "quickhaul_order",
    "phone.hunterlink_rank": "hunterlink_rank", "phone.live_stream": "live_stream",
}
HANDS = ["taeo_right_front", "taeo_left_tilt", "taeo_thumb_tap", "taeo_pov_ots", "grandma_phone", "chae_tablet", "phone_on_table"]
VERSION = 3


def _hex(rgb):
    return "#%02X%02X%02X" % tuple(int(c) for c in rgb[:3])


def _sig(*paths):
    h = hashlib.sha1(str(VERSION).encode())
    for p in paths:
        p = Path(p)
        if p.exists():
            st = p.stat()
            h.update(f"{p.name}:{st.st_size}:{int(st.st_mtime)}".encode())
    return h.hexdigest()[:16]


def measure_bubble(png, meta, kind):
    """Crop a bubble blank to its alpha box; measure the outline for tails."""
    im = Image.open(png).convert("RGBA")
    a = np.array(im)[:, :, 3]
    ys, xs = np.nonzero(a > 24)
    m = 3
    x0, y0 = max(0, xs.min() - m), max(0, ys.min() - m)
    x1, y1 = min(im.width, xs.max() + 1 + m), min(im.height, ys.max() + 1 + m)
    crop = im.crop((x0, y0, x1, y1))
    arr = np.array(crop).astype(np.int32)
    alpha = arr[:, :, 3] > 128
    lum = 0.299 * arr[:, :, 0] + 0.587 * arr[:, :, 1] + 0.114 * arr[:, :, 2]
    dark = alpha & (lum < 120)
    H, W = alpha.shape
    ys, xs = np.nonzero(alpha)
    cx, cy = (xs.min() + xs.max()) / 2.0, (ys.min() + ys.max()) / 2.0
    n = 360
    steps = np.arange(0, np.hypot(W, H), 0.5)
    radii, thick = [], []
    for k in range(n):
        th = 2 * np.pi * k / n
        px = np.clip((cx + steps * np.cos(th)).astype(int), 0, W - 1)
        py = np.clip((cy + steps * np.sin(th)).astype(int), 0, H - 1)
        inside = alpha[py, px]
        outs = np.nonzero(~inside)[0]
        e = int(outs[0]) if len(outs) else len(steps) - 1
        radii.append(round(float(steps[max(0, e - 1)]), 1))
        if kind not in DARK_FILL:
            run = dark[py[:e], px[:e]][::-1]
            t = 0
            gap = 0
            for v in run:
                if v:
                    t += 1
                    gap = 0
                else:
                    gap += 1
                    if gap > 1 or t == 0:
                        break
            thick.append(t * 0.5)
    stroke = float(np.median([t for t in thick if t > 0])) if thick and any(t > 0 for t in thick) else 3.0
    # colours: fill = median of the inner 30% box; line = median of dark pixels
    ih, iw = int(H * 0.35), int(W * 0.35)
    inner = arr[ih:H - ih, iw:W - iw][..., :3].reshape(-1, 3)
    fill = np.median(inner, axis=0)
    if kind in DARK_FILL:
        ring = arr[(alpha) & (lum > 30) & (lum < 200)]
        line = np.median(ring[:, :3], axis=0) if len(ring) > 50 else fill
        if kind == "menace":
            line = fill
    else:
        line = np.median(arr[dark][:, :3], axis=0) if dark.any() else np.array([43, 37, 35])
    rect = None
    for b in meta.get("text_boxes", []):
        if b.get("id") in ("dialogue", "text", "body"):
            rect = b["rect"]
    if rect is None and meta.get("text_boxes"):
        rect = meta["text_boxes"][0]["rect"]
    if rect is None:
        rect = [W * 0.2, H * 0.25, W * 0.6, H * 0.5]
    else:
        rect = [rect[0] - x0, rect[1] - y0, rect[2], rect[3]]
    return crop, {
        "size": [int(W), int(H)], "rect": [round(float(v), 1) for v in rect], "cx": round(float(cx), 1), "cy": round(float(cy), 1),
        "r": radii, "stroke": round(stroke, 2), "fill": _hex(fill), "line": _hex(line),
    }


class Kit:
    def __init__(self, root):
        self.root = Path(root) if root else None
        self.bubbles = {}   # kind -> list of entries {name, png, ...}
        self.system = {}    # kind -> (png, meta)
        self.apps = {}      # ui kind -> (png, meta)
        self.hands = {}     # name -> (png, mask, meta)
        self.logo = None
        if not self.root or not self.root.exists():
            return
        eng = self.root / "_engine"
        eng.mkdir(exist_ok=True)
        cache_f = eng / "bubbles.json"
        try:
            cache = json.load(open(cache_f)) if cache_f.exists() else {}
        except Exception:
            cache = {}
        changed = False
        for kind, names in BUBBLE_SETS.items():
            for nm in names:
                png = self.root / "bubbles" / f"{nm}_blank.png"
                js = self.root / "bubbles" / f"{nm}.json"
                if not (png.exists() and js.exists()):
                    continue
                sig = _sig(png, js)
                out = eng / f"{nm}.png"
                ent = cache.get(nm)
                if not ent or ent.get("sig") != sig or not out.exists():
                    crop, info = measure_bubble(png, json.load(open(js, encoding="utf-8")), kind)
                    crop.save(out)
                    ent = dict(info, sig=sig, name=nm)
                    cache[nm] = ent
                    changed = True
                self.bubbles.setdefault(kind, []).append(dict(ent, png=str(out)))
        if changed:
            json.dump(cache, open(cache_f, "w"))
        for js in sorted((self.root / "system").glob("system_*.json")) if (self.root / "system").exists() else []:
            try:
                meta = json.load(open(js, encoding="utf-8"))
            except Exception:
                continue
            png = js.with_name(meta.get("file", js.stem + "_blank.png"))
            if png.exists():
                self.system[js.stem.replace("system_", "")] = (png, meta)
        for kind, nm in APP_KINDS.items():
            js = self.root / "phone" / f"{nm}.json"
            png = self.root / "phone" / f"{nm}_blank.png"
            if js.exists() and png.exists():
                self.apps[kind] = (png, json.load(open(js, encoding="utf-8")))
        for nm in HANDS:
            js = self.root / "phone" / f"{nm}.json"
            png = self.root / "phone" / f"{nm}_blank.png"
            mask = self.root / "phone" / f"{nm}_screen_mask.png"
            if js.exists() and png.exists() and mask.exists():
                self.hands[nm] = (png, mask, json.load(open(js, encoding="utf-8")))
        self.cards = {}
        for nm, fn in (("title", "title_card_without_chapter"), ("end", "end_card"), ("intro", "intro_card")):
            js = self.root / "logo" / f"{fn}.json"
            if js.exists():
                meta = json.load(open(js, encoding="utf-8"))
                png = js.with_name(meta.get("file", fn + "_blank.png"))
                if nm != "title" and not png.name.endswith("_blank.png"):
                    png = js.with_name(fn + "_blank.png")
                if png.exists():
                    self.cards[nm] = (png, meta)
        for cand in ["logo/logo_final.png", "logo/logo_transparent.png", "logo/logo.png", "logo/logo_blank.png"]:
            if (self.root / cand).exists():
                self.logo = self.root / cand
                break

    def system_tpl(self, kind):
        return self.system.get(kind) or self.system.get("window")

    def profiles_js(self):
        """Per-blank outline profiles for the page script."""
        out = {}
        for kind, ents in self.bubbles.items():
            for e in ents:
                out[e["name"]] = {k: e[k] for k in ("size", "rect", "cx", "cy", "r", "stroke", "fill", "line")}
        return out
