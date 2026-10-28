#!/usr/bin/env python3
"""review_cards: one card per panel for Claude's visual review: the art beside what the script asks of it.

usage: review_cards.py scripts_v2/chNNN.yaml ART_DIR OUT_DIR [P01 P02 ... | P01-P09] [--w 1100]

Each card (OUT_DIR/<id>.jpg) shows the panel (long side about --w px) and, under it, the script's camera, art,
acting, hands, eyeline and the lines' speakers, so every check (sides, hands, props, scale, acting) is made
against the script in one look. Panels with no art file get a note instead of a card.
"""
import sys
import textwrap
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONTB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(size, bold=False):
    try:
        return ImageFont.truetype(FONTB if bold else FONT, size)
    except OSError:
        return ImageFont.load_default()


def panel_ids(spec, all_ids):
    if not spec:
        return all_ids
    out = []
    for s in spec:
        if "-" in s:
            a, b = s.split("-")
            ia, ib = all_ids.index(a), all_ids.index(b)
            out += all_ids[ia:ib + 1]
        else:
            out.append(s)
    return out


def text_block(p):
    rows = []
    def add(label, val):
        if not val:
            return
        if isinstance(val, dict):
            for k, v in val.items():
                rows.append((f"{label} {k}", str(v)))
        elif isinstance(val, list):
            rows.append((label, "; ".join(str(v) for v in val)))
        else:
            rows.append((label, " ".join(str(val).split())))
    add("shape", f"{p.get('shape', '')}  recipe {p.get('recipe', '')}  face {p.get('face', '')}".strip())
    add("camera", p.get("camera"))
    add("light", p.get("light"))
    add("art", p.get("art"))
    add("acting", p.get("acting"))
    add("hands", p.get("hands"))
    add("hand_ref", p.get("hand_ref"))
    add("eyeline", p.get("eyeline"))
    add("foreground", p.get("foreground"))
    add("calm", p.get("calm"))
    whos = [f"{l.get('who')}({l.get('type', 'speech')})" for l in (p.get("lines") or [])]
    add("lines", ", ".join(whos))
    ui = [u.get("kind") + (" on screen" if u.get("on") == "screen" else "") for u in (p.get("ui") or [])]
    add("ui", ", ".join(ui))
    return rows


def card(p, img_path, out_path, w):
    im = Image.open(img_path).convert("RGB")
    scale = w / max(im.size)
    im = im.resize((max(1, int(im.width * scale)), max(1, int(im.height * scale))), Image.LANCZOS)
    f, fb = font(17), font(17, True)
    rows = text_block(p)
    lines = []
    for label, val in rows:
        wrapped = textwrap.wrap(val, width=104) or [""]
        lines.append((label, wrapped[0]))
        for more in wrapped[1:]:
            lines.append(("", more))
    lh = 22
    cw = max(im.width, 1200)
    hdr = 34
    H = hdr + im.height + 10 + lh * len(lines) + 12
    out = Image.new("RGB", (cw, H), (250, 250, 247))
    d = ImageDraw.Draw(out)
    d.text((10, 6), f"{p['id']}  {img_path.name}  {Image.open(img_path).size[0]}x{Image.open(img_path).size[1]}", fill=(180, 0, 0), font=font(20, True))
    out.paste(im, (0, hdr))
    y = hdr + im.height + 10
    for label, val in lines:
        if label:
            d.text((10, y), label, fill=(20, 60, 140), font=fb)
        d.text((250, y), val, fill=(20, 20, 20), font=f)
        y += lh
    out.save(out_path, quality=86)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    w = 1100
    if "--w" in sys.argv:
        w = int(sys.argv[sys.argv.index("--w") + 1])
        args = [a for a in args if a != str(w)]
    script, art, out = Path(args[0]), Path(args[1]), Path(args[2])
    out.mkdir(parents=True, exist_ok=True)
    data = yaml.safe_load(open(script))
    panels = [p for p in data.get("panels", []) if isinstance(p, dict) and p.get("id")]
    by_id = {p["id"]: p for p in panels}
    ids = panel_ids(args[3:], [p["id"] for p in panels])
    made = 0
    for pid in ids:
        p = by_id.get(pid)
        if p is None:
            print(f"{pid}: not in the script")
            continue
        img = next((art / f"{pid}{x}" for x in (".png", ".jpg", ".webp") if (art / f"{pid}{x}").exists()), None)
        if img is None:
            print(f"{pid}: no art file")
            continue
        card(p, img, out / f"{pid}.jpg", w)
        made += 1
    print(f"{made} cards in {out}")


if __name__ == "__main__":
    main()
