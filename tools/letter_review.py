#!/usr/bin/env python3
"""letter_review: contact pages of a lettered chapter strip for Claude's lettering review.

usage: letter_review.py OUT_DIR PAGES_DIR [--per 6] [--width 520] [--only P01,P05]
Reads OUT_DIR/layout.json and OUT_DIR/strip.png (autostrip2 output) and writes PAGES_DIR/page_NN.jpg:
each panel cropped with a margin above and below (balloons straddle the panel edges), labelled with its id,
two columns, --per panels per page.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw

Image.MAX_IMAGE_PIXELS = None


def main(a):
    out, pages = Path(a[0]), Path(a[1])
    per, width, only = 6, 520, None
    if "--per" in a: per = int(a[a.index("--per") + 1])
    if "--width" in a: width = int(a[a.index("--width") + 1])
    if "--only" in a: only = set(a[a.index("--only") + 1].split(","))
    L = json.loads((out / "layout.json").read_text())
    s = L["scale"]
    strip = Image.open(out / "strip.png").convert("RGB")
    pages.mkdir(parents=True, exist_ok=True)
    crops = []
    for p in L["panels"]:
        if only and p["id"] not in only:
            continue
        y0 = max(0, p["y_top"] - 140) * s
        y1 = min(L["height"], p["y_bottom"] + 140) * s
        c = strip.crop((0, y0, strip.width, y1))
        c = c.resize((width, round(c.height * width / c.width)), Image.LANCZOS)
        d = ImageDraw.Draw(c)
        d.rectangle((0, 0, 44, 18), fill=(255, 0, 0)); d.text((3, 3), p["id"], fill=(255, 255, 255))
        crops.append(c)
    for k in range(0, len(crops), per):
        grp = crops[k:k + per]
        rows = [grp[i:i + 2] for i in range(0, len(grp), 2)]
        H = sum(max(c.height for c in r) for r in rows)
        page = Image.new("RGB", (width * 2 + 10, H), (128, 128, 128))
        y = 0
        for r in rows:
            for j, c in enumerate(r):
                page.paste(c, (j * (width + 10), y))
            y += max(c.height for c in r)
        page.save(pages / f"page_{k // per + 1:02d}.jpg", quality=82)
    print(f"{len(crops)} panels on {(len(crops) + per - 1) // per} pages in {pages}")


if __name__ == "__main__":
    main(sys.argv[1:])
