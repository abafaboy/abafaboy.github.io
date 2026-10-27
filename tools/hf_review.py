#!/usr/bin/env python3
"""hf_review: compare Codex hand fixes with their base panels, for Claude's review.

usage: hf_review.py BASE_DIR FIXED_DIR OUT_DIR [P04 P10 ...]
For each panel: checks the size, finds the changed region (pixels that differ by more than a small threshold),
and writes OUT_DIR/<P>_pair.jpg (base | fixed, the changed box outlined), OUT_DIR/<P>_zoom.jpg (the changed
region from both, at 2x when it is small) and OUT_DIR/<P>_diff.png (where the pixels changed).
Prints one line per panel: size check, changed box, share of the panel changed, and whether the change
reaches the panel edge (a sign of a whole-panel redraw or a shifted composite).
"""
import os
import sys

from PIL import Image, ImageChops, ImageDraw, ImageFilter

THR = 24  # per-channel difference that counts as a change (ignores PNG/quantisation noise)


def changed_mask(a, b):
    d = ImageChops.difference(a.convert("RGB"), b.convert("RGB"))
    r, g, bl = d.split()
    m = ImageChops.lighter(ImageChops.lighter(r, g), bl)
    m = m.point(lambda v: 255 if v > THR else 0)
    # drop speckle
    return m.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.MinFilter(5))


def main(base_dir, fixed_dir, out_dir, panels):
    os.makedirs(out_dir, exist_ok=True)
    if not panels:
        panels = sorted(f[:-4] for f in os.listdir(fixed_dir) if f.endswith(".png"))
    for p in panels:
        bp, fp = os.path.join(base_dir, p + ".png"), os.path.join(fixed_dir, p + ".png")
        if not os.path.exists(fp):
            print(f"{p}: no fixed file")
            continue
        a, b = Image.open(bp).convert("RGB"), Image.open(fp).convert("RGB")
        if a.size != b.size:
            print(f"{p}: SIZE MISMATCH base {a.size} fixed {b.size}")
            b2 = b.resize(a.size)
        else:
            b2 = b
        m = changed_mask(a, b2)
        box = m.getbbox()
        share = m.histogram()[255] / (a.size[0] * a.size[1])
        edge = bool(box) and (box[0] <= 2 or box[1] <= 2 or box[2] >= a.size[0] - 2 or box[3] >= a.size[1] - 2)
        print(f"{p}: size {'ok' if a.size == b.size else 'WRONG'} {a.size}; changed box {box}; "
              f"{share:.1%} of the panel changed{'; reaches the edge' if edge else ''}")
        # pair
        w, h = a.size
        pair = Image.new("RGB", (w * 2 + 20, h), "white")
        pair.paste(a, (0, 0))
        pair.paste(b2, (w + 20, 0))
        if box:
            d = ImageDraw.Draw(pair)
            for off in (0, w + 20):
                d.rectangle([box[0] + off, box[1], box[2] + off, box[3]], outline=(255, 0, 255), width=4)
        pair.thumbnail((2400, 1200))
        pair.save(os.path.join(out_dir, f"{p}_pair.jpg"), quality=88)
        m.save(os.path.join(out_dir, f"{p}_diff.png"))
        if box:
            pad = 40
            bx = (max(0, box[0] - pad), max(0, box[1] - pad), min(w, box[2] + pad), min(h, box[3] + pad))
            ca, cb = a.crop(bx), b2.crop(bx)
            k = 2 if max(ca.size) < 700 else 1
            ca, cb = ca.resize((ca.width * k, ca.height * k), Image.LANCZOS), cb.resize((cb.width * k, cb.height * k), Image.LANCZOS)
            z = Image.new("RGB", (ca.width * 2 + 20, ca.height), "white")
            z.paste(ca, (0, 0))
            z.paste(cb, (ca.width + 20, 0))
            z.thumbnail((2400, 1600))
            z.save(os.path.join(out_dir, f"{p}_zoom.jpg"), quality=90)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4:])
