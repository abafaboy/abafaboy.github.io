#!/usr/bin/env python3
"""check_art_v2: mechanical checks on a chapter's art folder before Claude's visual review (PANEL_BRIEF_v2).

For every panel of scripts_v2/chNNN.yaml that needs art (not kind title/caption):
- the file exists, is a real PNG (signature), at the brief's size for its shape (section 4);
- no lossy block grid (8x8 JPEG / 4x4 and 16x16 WebP-VP8 ratios; > 1.12 is suspicious, section 13 / 11b.11);
- sharpness (Laplacian variance) so a soft, re-enlarged image stands out against its neighbours;
- P-panels with a `ui` entry `on: screen` contain flat #00FF00;
- END.png is 1024x1024 on white.
Also parses every REVIEW_<part>.json: valid JSON, a head box for each kept panel, boxes inside 0..1.

usage: check_art_v2.py SCRIPT.yaml ART_DIR [--allow P32=1536x512 ...]
"""
import argparse
import glob
import json
import os
import sys

import numpy as np
import yaml
from PIL import Image

SIZES = {"full": (1536, 1024), "wide": (1536, 1024), "vignette": (1536, 1024), "strip": (1536, 1024),
         "tall": (1024, 1536), "narrow-l": (1024, 1536), "narrow-r": (1024, 1536), "bleed": (1024, 1536),
         "inset-l": (1024, 1024), "inset-r": (1024, 1024)}
PNG_SIG = b"\x89PNG\r\n\x1a\n"


def grid_ratio(L, period):
    dx = np.abs(np.diff(L, axis=1))
    dy = np.abs(np.diff(L, axis=0))
    cols = np.arange(dx.shape[1])
    rows = np.arange(dy.shape[0])
    bx = dx[:, (cols % period) == period - 1].mean()
    ix = dx[:, (cols % period) != period - 1].mean() + 1e-6
    by = dy[(rows % period) == period - 1, :].mean()
    iy = dy[(rows % period) != period - 1, :].mean() + 1e-6
    return float((bx / ix + by / iy) / 2)


def lap_var(L):
    import cv2
    return float(cv2.Laplacian(L.astype(np.float32), cv2.CV_32F).var())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("art")
    ap.add_argument("--allow", nargs="*", default=["P32=1536x512"], help="size exceptions, e.g. P32=1536x512")
    A = ap.parse_args()
    allow = {}
    for a in A.allow:
        k, v = a.split("=")
        w, h = v.lower().split("x")
        allow[k] = (int(w), int(h))
    S = yaml.safe_load(open(A.script, encoding="utf-8"))
    panels = S["panels"]
    errs, warns, rows = [], [], []
    have = {}
    for p in panels:
        pid = str(p["id"])
        kind = p.get("kind")
        if kind in ("title", "caption"):
            continue
        fn = "END.png" if kind == "end" else f"{pid}.png"
        path = os.path.join(A.art, fn)
        if not os.path.exists(path):
            rows.append((pid, "missing", "", "", "", ""))
            continue
        with open(path, "rb") as f:
            sig = f.read(8)
        if sig != PNG_SIG:
            errs.append(f"{fn}: not a PNG file (signature {sig[:4]!r})")
        im = Image.open(path)
        want = (1024, 1024) if kind == "end" else allow.get(pid, SIZES.get(p.get("shape"), None))
        if want and im.size != want:
            errs.append(f"{fn}: size {im.size[0]}x{im.size[1]}, brief wants {want[0]}x{want[1]} for shape {p.get('shape') or kind}")
        a = np.asarray(im.convert("RGB")).astype(np.float32)
        L = 0.299 * a[..., 0] + 0.587 * a[..., 1] + 0.114 * a[..., 2]
        g8, g4, g16 = grid_ratio(L, 8), grid_ratio(L, 4), grid_ratio(L, 16)
        sh = lap_var(L)
        if max(g8, g4, g16) > 1.12:
            warns.append(f"{fn}: block-grid ratio g8={g8:.3f} g4={g4:.3f} g16={g16:.3f} (lossy compression somewhere?)")
        for u in p.get("ui") or []:
            if isinstance(u, dict) and u.get("on") == "screen":
                rgb = np.asarray(im.convert("RGB"))
                green = ((rgb[..., 0] < 40) & (rgb[..., 1] > 215) & (rgb[..., 2] < 40)).mean()
                if green < 0.01:
                    errs.append(f"{fn}: ui on screen, but no flat #00FF00 screen found ({green:.4f} of pixels)")
        if kind == "end":
            rgb = np.asarray(im.convert("RGB")).astype(int)
            corners = [rgb[:24, :24], rgb[:24, -24:], rgb[-24:, :24], rgb[-24:, -24:]]
            if min(c.mean() for c in corners) < 235:
                warns.append(f"{fn}: corners are not white (END is a chibi gag on plain white)")
        have[pid] = True
        rows.append((pid, f"{im.size[0]}x{im.size[1]}", im.mode, f"{g8:.3f}/{g4:.3f}/{g16:.3f}", f"{sh:.0f}", os.path.getsize(path) // 1024))
    # REVIEW files
    heads = {}
    for rf in sorted(glob.glob(os.path.join(A.art, "REVIEW_*.json"))):
        try:
            R = json.load(open(rf, encoding="utf-8"))
        except Exception as e:  # noqa: BLE001
            errs.append(f"{os.path.basename(rf)}: invalid JSON ({e})")
            continue
        for pid, v in R.items():
            hb = (v or {}).get("heads") or {}
            heads[pid] = hb
            for who, box in hb.items():
                ok = isinstance(box, list) and len(box) == 4 and all(isinstance(x, (int, float)) for x in box)
                if not ok or not (0 <= box[0] < box[2] <= 1 and 0 <= box[1] < box[3] <= 1):
                    errs.append(f"{os.path.basename(rf)} {pid} {who}: bad head box {box}")
    for pid in have:
        if pid not in heads and pid != "END":
            warns.append(f"{pid}: no entry in any REVIEW_*.json")
    print(f"{'panel':6s} {'size':>10s} {'mode':>5s} {'grid 8/4/16':>18s} {'sharp':>7s} {'KB':>6s}")
    for r in rows:
        print(f"{r[0]:6s} {r[1]:>10s} {r[2]:>5s} {r[3]:>18s} {r[4]:>7s} {str(r[5]):>6s}")
    done = sum(1 for r in rows if r[1] != "missing")
    print(f"\n{done}/{len(rows)} art panels present")
    for e in errs:
        print("ERROR", e)
    for w in warns:
        print("WARN ", w)
    sys.exit(1 if errs else 0)


if __name__ == "__main__":
    main()
