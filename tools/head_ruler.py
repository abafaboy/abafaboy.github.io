#!/usr/bin/env python3
"""head_ruler: overlay a head-count ruler on panels so body proportions can be measured, not guessed.

For every head box recorded in the art folder's REVIEW_*.json files, draws the box and then tick lines every head
height downward from the top of the box (1..9), labelled, in that character's colour. A standing adult on the model
sheets is 7.5-8 heads (Yerin, Seoa, Bomi ~7; Nib ~6): if the feet land well above the expected tick, the body is
compressed (unless the pose is crouched, seated, foreshortened toward the camera, or cropped).

usage: head_ruler.py ART_DIR OUT_DIR [P01 P02 ...]   (default: every panel with a head box)
"""
import glob
import json
import os
import sys

from PIL import Image, ImageDraw, ImageFont

EXPECT = {"kang_jaeha": 7.75, "mok_hangyu": 8, "choi_dongmin": 7.75, "lyra": 8, "moon_ahin": 8, "song_yerin": 7,
          "kang_seoa": 7.25, "yoo_bomi": 7.25, "nib": 6, "kett": 6, "borro": 7, "baek_taegun": 8}
COLS = [(255, 64, 64), (64, 200, 255), (255, 200, 40), (120, 255, 120), (255, 120, 255), (255, 255, 255)]


def main():
    art, out = sys.argv[1], sys.argv[2]
    want = set(sys.argv[3:])
    os.makedirs(out, exist_ok=True)
    heads = {}
    for rf in sorted(glob.glob(os.path.join(art, "REVIEW_*.json"))):
        try:
            R = json.load(open(rf, encoding="utf-8"))
        except Exception:
            continue
        for pid, v in R.items():
            if isinstance(v, dict) and v.get("heads"):
                heads[pid] = v["heads"]
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
    done = []
    for pid, hb in sorted(heads.items()):
        if want and pid not in want:
            continue
        fn = os.path.join(art, ("END" if pid == "END" else pid) + ".png")
        if not os.path.exists(fn):
            continue
        im = Image.open(fn).convert("RGB")
        W, H = im.size
        d = ImageDraw.Draw(im)
        for k, (who, box) in enumerate(hb.items()):
            if not (isinstance(box, list) and len(box) == 4):
                continue
            c = COLS[k % len(COLS)]
            x0, y0, x1, y1 = box[0] * W, box[1] * H, box[2] * W, box[3] * H
            hh = y1 - y0
            d.rectangle([x0, y0, x1, y1], outline=c, width=3)
            exp = EXPECT.get(who)
            for n in range(1, 10):
                y = y0 + n * hh
                if y > H:
                    break
                w = 4 if exp and abs(n - round(exp)) < 0.6 else 2
                d.line([(x0 - 30, y), (x1 + 30, y)], fill=c, width=w)
                d.text((x1 + 34, y - 12), str(n), fill=c, font=font)
            label = f"{who}" + (f" (~{exp:g} heads)" if exp else "")
            d.text((x0, max(0, y0 - 26)), label, fill=c, font=font)
        im.save(os.path.join(out, f"{pid}_ruler.png"))
        done.append(pid)
    print(len(done), "panels:", " ".join(done))


if __name__ == "__main__":
    main()
