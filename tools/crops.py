#!/usr/bin/env python3
"""crops: cut regions (fractions of each image) at full resolution and lay them on one sheet for close checks.
usage: crops.py OUT.png "IMG:x0,y0,x1,y1[:label]" ... [--h 420]"""
import sys
from PIL import Image, ImageDraw, ImageFont
out = sys.argv[1]
H = 420
args = [a for a in sys.argv[2:] if not a.startswith("--h")]
if any(a.startswith("--h") for a in sys.argv): H = int([a for a in sys.argv if a.startswith("--h")][0].split("=")[1])
tiles = []
for a in args:
    parts = a.split(":")
    p, box = parts[0], [float(v) for v in parts[1].split(",")]
    lab = parts[2] if len(parts) > 2 else p.rsplit("/", 1)[-1]
    im = Image.open(p).convert("RGB")
    W, Hh = im.size
    c = im.crop((int(box[0] * W), int(box[1] * Hh), int(box[2] * W), int(box[3] * Hh)))
    s = H / c.height
    c = c.resize((max(1, int(c.width * s)), H), Image.LANCZOS if s < 1 else Image.NEAREST)
    tiles.append((lab, c))
f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
maxw = 1560
rows, cur, w = [], [], 0
for t in tiles:
    if cur and w + t[1].width + 8 > maxw:
        rows.append(cur); cur, w = [], 0
    cur.append(t); w += t[1].width + 8
if cur: rows.append(cur)
sheet = Image.new("RGB", (maxw, len(rows) * (H + 30) + 8), (40, 40, 44))
d = ImageDraw.Draw(sheet)
y = 4
for r in rows:
    x = 4
    for lab, c in r:
        d.text((x, y), lab, fill=(255, 255, 255), font=f)
        sheet.paste(c, (x, y + 22)); x += c.width + 8
    y += H + 30
sheet.save(out); print(out, sheet.size)
