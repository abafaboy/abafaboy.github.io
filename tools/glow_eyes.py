#!/usr/bin/env python3
"""glow_eyes: light the eye holes of a white mask with a glowing colour (light shining out from behind the mask).

usage: glow_eyes.py IN.png OUT.png --box x0,y0,x1,y1 [--core R,G,B] [--mid R,G,B] [--bloom 1.0]
The box should hold the mask's face. The mask is the largest bright area in the box; the eye holes are the dark blobs
inside its convex hull (so teeth, buttons or shadows outside the mask are never lit). Each hole keeps a thin dark rim,
gets a hot core and a coloured middle, and a soft bloom spills onto the mask around it.
Defaults: Borro's field-form moss green (CHARACTER_DESIGNS 2.12).
"""
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()
ap.add_argument("inp"); ap.add_argument("out")
ap.add_argument("--box", required=True)
ap.add_argument("--core", default="236,255,200")
ap.add_argument("--mid", default="128,196,86")
ap.add_argument("--bloom", type=float, default=1.0)
ap.add_argument("--dark", type=int, default=90)
ap.add_argument("--n", type=int, default=2, help="light only the N largest holes (the eyes; a cord hole is smaller)")
a = ap.parse_args()
x0, y0, x1, y1 = [int(v) for v in a.box.split(",")]
core = np.array([int(v) for v in a.core.split(",")][::-1], np.float32)  # BGR
mid = np.array([int(v) for v in a.mid.split(",")][::-1], np.float32)
img = cv2.imread(a.inp).astype(np.float32)
sub = img[y0:y1, x0:x1]
L = sub.mean(2)
bright = (L > 165).astype(np.uint8)
n, lab, st, _ = cv2.connectedComponentsWithStats(bright)
if n < 2:
    raise SystemExit("no mask found in the box")
k = 1 + int(np.argmax(st[1:, 4]))
cnts, _ = cv2.findContours((lab == k).astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
hull = np.zeros_like(bright)
cv2.fillPoly(hull, [cv2.convexHull(max(cnts, key=cv2.contourArea))], 1)
hull = cv2.erode(hull, np.ones((3, 3), np.uint8))
dark = ((L < a.dark) & (hull > 0)).astype(np.uint8)
n2, lab2, st2, cen2 = cv2.connectedComponentsWithStats(dark)
H, W = L.shape
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
out = sub.copy()
glow = np.zeros((H, W), np.float32)
cands = [i for i in range(1, n2) if 10 <= st2[i][4] <= 0.05 * H * W and st2[i][2] <= 3 * st2[i][3] and st2[i][3] <= 3 * st2[i][2]]
cands = sorted(cands, key=lambda i: -st2[i][4])[:a.n]
found = 0
for i in cands:
    x, y, w, h, ar = st2[i]
    found += 1
    m = cv2.dilate((lab2 == i).astype(np.uint8), np.ones((3, 3), np.uint8)) > 0
    cx, cy = cen2[i]
    r = max(2.0, np.sqrt(ar / np.pi))
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r
    t_core = np.clip(1 - d / 0.55, 0, 1)[..., None]
    t_rim = np.clip((d - 0.78) / 0.3, 0, 1)[..., None]   # the outer rim stays the hole's own dark
    col = mid * (1 - t_core) + core * t_core
    col = col * (1 - t_rim) + sub * t_rim
    out[m] = col[m]
    glow += np.exp(-((d / 1.9) ** 2))
glow = np.clip(glow * 0.42 * a.bloom, 0, 0.6)[..., None]
glow_col = mid * 0.55 + core * 0.45
out = 255 - (255 - out) * (1 - glow * glow_col / 255.0)   # screen
img[y0:y1, x0:x1] = out
cv2.imwrite(a.out, np.clip(img, 0, 255).astype(np.uint8))
print("eye holes lit:", found)
