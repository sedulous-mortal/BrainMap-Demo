import sys
from PIL import Image
src, dst = sys.argv[1], sys.argv[2]
im = Image.open(src).convert("L"); px = im.load(); W, H = im.size
orig = im.copy().load()
def fill(x0, y0, x1, y1):
    for y in range(max(0,y0), min(H,y1)):
        for x in range(max(0,x0), min(W,x1)): px[x, y] = 255
def light(x, y): return 0 <= x < W and 0 <= y < H and orig[x, y] > 200
def thin_v(x, y): return orig[x, y] < 200 and light(x-3, y) and light(x+3, y)
def thin_h(x, y): return orig[x, y] < 200 and light(x, y-3) and light(x, y+3)
# Find leader lines: columns/rows holding a long unbroken thin run (engraving strokes are short).
def longest(cells):
    best = run = 0
    for c in cells:
        run = run + 1 if c else 0; best = max(best, run)
    return best
cols = [x for x in range(250, 425) if longest(thin_v(x, y) for y in range(H)) >= 30]
rows = [y for y in range(250, 455) if longest(thin_h(x, y) for x in range(140, 245)) >= 12]
cols2 = [x for x in range(225, 252) if longest(thin_v(x, y) for y in range(440, 560)) >= 25]
print("line columns", cols, "rows", rows, "mammillary columns", cols2)
for x in cols + cols2:
    for y in range(H):
        for dx in (-2, -1, 0, 1, 2):
            xx = x + dx
            if 0 <= xx < W and light(xx-3, y) and light(xx+3, y): px[xx, y] = 255
for y in rows:
    for x in range(140, 245):
        for dy in (-2, -1, 0, 1, 2):
            yy = y + dy
            if light(x, yy-3) and light(x, yy+3): px[x, yy] = 255
for box in [(258,8,312,30),(288,23,382,38),(318,36,410,51),(330,48,418,62),(352,59,407,74),(365,71,429,86),(386,83,430,98),
            (0,258,153,445),(200,528,262,560),(296,6,330,32),(226,466,252,528),(240,536,274,562),(256,570,372,590)]:
    fill(*box)
im.save(dst, optimize=True)
