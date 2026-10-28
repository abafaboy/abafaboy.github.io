#!/usr/bin/env python3
"""Paint objects out of a panel whose background is a fine, even texture (water, sky, fog, plain walls).

The object pixels are found automatically inside each removal polygon (pixels that differ from the
background colour statistics), grown and feathered; the hole is filled with the background's own
low-frequency colour (interpolated from the clean pixels around it) plus fine texture copied in
overlapping tiles from clean areas of the same panel at a similar height.

Usage:
  paint_out.py IN.png OUT.png --remove "x,y x,y x,y ..." [--remove ...] [--protect "x,y ..."]
               [--bright 31] [--grey 13] [--grow 9] [--feather 9] [--debug DEBUG.png] [--seed 1]

--bright: a pixel is "object" when its mean RGB is above this (background highlights stay below it);
--grey:   or when its blue-minus-red is below this (grey or warm object against a blue background).
Defaults suit ch009's black-navy water. Check the debug overlay and the result at 2x before using it.
"""
import argparse
import cv2
import numpy as np


def poly_mask(shape, pts):
    m = np.zeros(shape[:2], np.uint8)
    cv2.fillPoly(m, [np.array(pts, np.int32)], 1)
    return m


def parse_pts(s):
    return [tuple(int(float(v)) for v in p.split(",")) for p in s.split()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("inp")
    ap.add_argument("out")
    ap.add_argument("--remove", action="append", required=True)
    ap.add_argument("--protect", action="append", default=[])
    ap.add_argument("--bright", type=float, default=31)
    ap.add_argument("--grey", type=float, default=13)
    ap.add_argument("--grow", type=int, default=9)
    ap.add_argument("--feather", type=int, default=9)
    ap.add_argument("--tile", type=int, default=128)
    ap.add_argument("--debug")
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)

    bgr = cv2.imread(a.inp, cv2.IMREAD_COLOR)
    img = bgr[:, :, ::-1].astype(np.float32)
    H, W = img.shape[:2]
    R, G, B = img[..., 0], img[..., 1], img[..., 2]
    L = img.mean(2)
    obj = ((L > a.bright) | ((B - R) < a.grey)).astype(np.uint8)
    clean = 1 - cv2.dilate(obj, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9)))

    protect = np.zeros((H, W), np.uint8)
    for p in a.protect:
        protect |= poly_mask(img.shape, parse_pts(p))

    # what to remove: object pixels inside the removal polygons, closed and grown
    rem = np.zeros((H, W), np.uint8)
    for p in a.remove:
        rem |= poly_mask(img.shape, parse_pts(p))
    m = obj & rem & (1 - protect)
    m = cv2.morphologyEx(m, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15, 15)))
    m = cv2.dilate(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * a.grow + 1, 2 * a.grow + 1)))
    m = m & rem & (1 - protect)
    # a soft edge across the hole's border; total fill a few pixels in from it
    alpha = cv2.GaussianBlur(m.astype(np.float32), (0, 0), a.feather / 2.0)
    core = cv2.erode(m, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * (a.feather // 2) + 1,) * 2))
    alpha[core > 0] = 1.0
    alpha = np.clip(alpha * (1 - protect), 0, 1)

    # background low frequency, from clean pixels only
    cl = clean.astype(np.float32) * (1 - m)
    s = 35
    num = cv2.GaussianBlur(img * cl[..., None], (0, 0), s)
    den = cv2.GaussianBlur(cl, (0, 0), s)[..., None]
    low = num / np.maximum(den, 1e-3)
    hp = img - low

    # clean tiles to copy texture from
    t = a.tile
    ii = cv2.integral((1 - cl).astype(np.float32))
    cands = []
    for y in range(0, H - t, 8):
        for x in range(0, W - t, 8):
            bad = ii[y + t, x + t] - ii[y, x + t] - ii[y + t, x] + ii[y, x]
            if bad == 0:
                cands.append((x, y))
    cands = np.array(cands)
    if len(cands) == 0:
        raise SystemExit("no clean tiles: lower --tile")

    win1 = np.sin(np.linspace(0, np.pi, t)) ** 2 + 1e-3
    win = np.outer(win1, win1)[..., None]
    tex = np.zeros_like(img)
    wsum = np.zeros((H, W, 1), np.float32)
    ys, xs = np.nonzero(m)
    y0, y1 = max(ys.min() - t, 0), min(ys.max() + t, H)
    x0, x1 = max(xs.min() - t, 0), min(xs.max() + t, W)
    step = t // 2
    for ty in range(y0, y1 - t // 2, step):
        for tx in range(x0, x1 - t // 2, step):
            ty2, tx2 = min(ty, H - t), min(tx, W - t)
            if m[ty2:ty2 + t, tx2:tx2 + t].max() == 0:
                continue
            d = np.abs(cands[:, 1] - ty2)
            pool = cands[d <= max(200, np.sort(d)[min(len(d) - 1, 40)])]
            sx, sy = pool[rng.integers(len(pool))]
            tex[ty2:ty2 + t, tx2:tx2 + t] += hp[sy:sy + t, sx:sx + t] * win
            wsum[ty2:ty2 + t, tx2:tx2 + t] += win
    tex = tex / np.maximum(wsum, 1e-3)
    fill = low + tex
    out = img * (1 - alpha[..., None]) + fill * alpha[..., None]
    out = np.clip(out, 0, 255).astype(np.uint8)
    cv2.imwrite(a.out, out[:, :, ::-1])
    if a.debug:
        vis = img.copy()
        vis[m > 0] = vis[m > 0] * 0.35 + np.array([255, 40, 40]) * 0.65
        vis[protect > 0] = vis[protect > 0] * 0.6 + np.array([40, 255, 40]) * 0.4
        cv2.imwrite(a.debug, np.clip(vis, 0, 255).astype(np.uint8)[:, :, ::-1])
    print(f"removed {int(m.sum())} px; {len(cands)} clean tiles")


if __name__ == "__main__":
    main()
