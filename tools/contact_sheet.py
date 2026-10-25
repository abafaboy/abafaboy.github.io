#!/usr/bin/env python3
"""contact_sheet: lay panel PNGs out on one labelled sheet for a quick visual review.

usage: contact_sheet.py OUT.png IMG [IMG ...] [--cell 640] [--cols 2]
Each image is fitted inside a cell (long side = --cell px), labelled with its file name.
"""
import argparse
import os

from PIL import Image, ImageDraw, ImageFont


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("imgs", nargs="+")
    ap.add_argument("--cell", type=int, default=640)
    ap.add_argument("--cols", type=int, default=2)
    A = ap.parse_args()
    c = A.cell
    lab = 26
    rows = (len(A.imgs) + A.cols - 1) // A.cols
    sheet = Image.new("RGB", (A.cols * (c + 12) + 12, rows * (c + lab + 12) + 12), (40, 40, 44))
    d = ImageDraw.Draw(sheet)
    try:
        f = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 18)
    except OSError:
        f = ImageFont.load_default()
    for i, p in enumerate(A.imgs):
        im = Image.open(p).convert("RGB")
        im.thumbnail((c, c), Image.LANCZOS)
        r, k = divmod(i, A.cols)
        x = 12 + k * (c + 12)
        y = 12 + r * (c + lab + 12)
        d.text((x, y), f"{os.path.basename(p)}  {Image.open(p).size[0]}x{Image.open(p).size[1]}", fill=(240, 240, 240), font=f)
        sheet.paste(im, (x + (c - im.width) // 2, y + lab + (c - im.height) // 2))
    sheet.save(A.out)
    print(A.out, sheet.size)


if __name__ == "__main__":
    main()
