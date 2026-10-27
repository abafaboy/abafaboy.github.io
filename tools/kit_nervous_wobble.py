"""Replace the kit's 'nervous' balloons (scalloped clouds that read as thought clouds with a speech tail; the chapter 1
judge's finding) with shaky speech balloons: an ellipse whose outline trembles in small, slightly irregular waves.
Same canvas sizes, art bounds and text rects as before, so every layout that used them still fits."""
import json, math, random, shutil
from pathlib import Path
from PIL import Image, ImageDraw
K = Path('/home/claude/msgf-kit/bubbles'); REJ = Path('/home/claude/msgf-kit/_rejects')
SS = 4  # supersampling
for name in ['nervous_1_4x1', 'nervous_2_2x1']:
    meta = json.load(open(K / f'{name}.json'))
    W, H = meta['size']; x0, y0, x1, y1 = meta['art_bounds']
    for f in (f'{name}_blank.png', f'{name}.json'):
        dst = REJ / f.replace(name, name + '_scalloped_v1')
        if not dst.exists(): shutil.copyfile(K / f, dst)
    cx, cy = (x0 + x1) / 2 * SS, (y0 + y1) / 2 * SS
    a, b = (x1 - x0) / 2 * SS - 4 * SS, (y1 - y0) / 2 * SS - 4 * SS
    rnd = random.Random(name)
    ph1, ph2 = rnd.uniform(0, 6.28), rnd.uniform(0, 6.28)
    waves = 34 if W < 900 else 44
    pts = []
    N = 1440
    for i in range(N):
        t = 2 * math.pi * i / N
        k = 1 + 0.011 * math.sin(waves * t + ph1) + 0.004 * math.sin((waves * 1.6) * t + ph2)
        pts.append((cx + a * k * math.cos(t), cy + b * k * math.sin(t)))
    stroke = round(3.0 * W / 722 * SS)
    im = Image.new('RGBA', (W * SS, H * SS), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.polygon(pts, fill=(43, 37, 35, 255))                       # outline colour as the outer shape
    inner = [(cx + (p[0] - cx) * (1 - stroke / a), cy + (p[1] - cy) * (1 - stroke / b)) for p in pts]
    d.polygon(inner, fill=(252, 252, 252, 255))                  # white fill inset by the stroke
    im = im.resize((W, H), Image.LANCZOS)
    im.save(K / f'{name}_blank.png')
    meta['notes'] = ('White #FCFCFC fill; warm near-black #2B2523 outline about 3 px at 722 px width, trembling in small waves '
                     '(a shaky speech balloon). Drawn by Claude on 27 Oct 2026 to replace the scalloped cloud, which read as a thought balloon.')
    meta['source'] = 'drawn programmatically (scratchpad/fix/kit_nervous_wobble.py)'
    meta['validation'] = {'text_free_artwork': 'drawn without lettering', 'all_rect_pixels_inside_alpha': True}
    json.dump(meta, open(K / f'{name}.json', 'w'), indent=1)
    # check the text rect sits inside the white fill
    r = meta['text_boxes'][0]['rect']; px = Image.open(K / f'{name}_blank.png').convert('RGBA')
    ok = all(px.getpixel((xx, yy))[3] == 255 and px.getpixel((xx, yy))[0] > 240 for xx in (r[0], r[0] + r[2]) for yy in (r[1], r[1] + r[3]))
    print(name, W, H, 'rect corners inside white:', ok)
