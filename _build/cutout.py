#!/usr/bin/env python3
"""Row-wise background keying: estimates the (smooth) background colour from the
image edges for each row and turns distance-from-background into alpha."""
import sys
import numpy as np
from PIL import Image, ImageFilter

src, dst = sys.argv[1], sys.argv[2]
t0 = float(sys.argv[3]) if len(sys.argv) > 3 else 14.0   # fully transparent below
t1 = float(sys.argv[4]) if len(sys.argv) > 4 else 42.0   # fully opaque above

im = Image.open(src).convert('RGB')
a = np.asarray(im).astype(np.float32)
h, w, _ = a.shape
edge = max(4, w // 25)
# per-row background estimate: mean of left and right edge strips, smoothed vertically
bg = (a[:, :edge].mean(axis=1) + a[:, -edge:].mean(axis=1)) / 2.0
k = 41
pad = np.pad(bg, ((k // 2, k // 2), (0, 0)), mode='edge')
bg = np.stack([np.convolve(pad[:, c], np.ones(k) / k, mode='valid') for c in range(3)], axis=1)

d = a - bg[:, None, :]
# warm/cool axis separates the warm-white crown from the cool blue backdrop far
# better than plain RGB distance, which reads both as "light"
warm = (d[:, :, 0] - d[:, :, 2])
luma = d @ np.array([0.299, 0.587, 0.114], dtype=np.float32)
dist = np.sqrt((warm * 2.2) ** 2 + luma ** 2)
alpha = np.clip((dist - t0) / (t1 - t0), 0, 1)

am = Image.fromarray((alpha * 255).astype(np.uint8), 'L')
# morphological opening kills the speckles the keyer picks out of the backdrop,
# then a small dilate+blur gives the edge back its anti-aliasing
am = am.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(1.4))
out = im.copy(); out.putalpha(am)
out.save(dst)
print('saved', dst, out.size)
