import numpy as np, json
from PIL import Image, ImageFilter, ImageDraw
H = '/home/user/brand/host'
ld = lambda n: np.asarray(Image.open(f'{H}/{n}.jpg').convert('RGB').resize((896,1200), Image.LANCZOS)).astype(np.float32)
base, mid, opn = ld('host_base'), ld('host_mid'), ld('host_open')
gray = lambda a: a.mean(2)
def align(ref, img, r=16):                      # integer shift by FFT cross-correlation on the face area
    A, B = gray(ref)[150:750, 200:700], gray(img)[150:750, 200:700]
    A, B = A - A.mean(), B - B.mean()
    c = np.fft.ifft2(np.fft.fft2(A) * np.conj(np.fft.fft2(B))).real
    dy, dx = np.unravel_index(np.argmax(c), c.shape); dy = dy - c.shape[0] if dy > c.shape[0]//2 else dy; dx = dx - c.shape[1] if dx > c.shape[1]//2 else dx
    dy, dx = int(np.clip(dy, -r, r)), int(np.clip(dx, -r, r))
    return np.roll(np.roll(img, dy, 0), dx, 1), (dy, dx)
mid, s1 = align(base, mid); opn, s2 = align(base, opn)
# mouth = where the open frame differs most from the base, inside the lower face
d = np.abs(gray(opn) - gray(base)); d = np.asarray(Image.fromarray(d.astype(np.uint8)).filter(ImageFilter.GaussianBlur(4))).astype(float)
d[:250] = 0; d[800:] = 0; d[:, :250] = 0; d[:, 650:] = 0
ys, xs = np.nonzero(d > max(18, d.max()*0.35))
cy, cx = int(np.median(ys)), int(np.median(xs))
w_, h_ = int(np.clip(np.percentile(xs,97)-np.percentile(xs,3), 60, 200)) + 50, int(np.clip(np.percentile(ys,97)-np.percentile(ys,3), 30, 130)) + 44
mask = Image.new('L', (896,1200), 0); ImageDraw.Draw(mask).ellipse([cx-w_//2, cy-h_//2, cx+w_//2, cy+h_//2], fill=255)
m = np.asarray(mask.filter(ImageFilter.GaussianBlur(14))).astype(np.float32)[..., None]/255
frames = [base, base*(1-m) + mid*m, base*(1-m) + opn*m]
# chroma key on the base (mouth changes never touch the green)
r, g, b = base[...,0], base[...,1], base[...,2]
spill = g - np.maximum(r, b)
alpha = np.clip(1 - (spill - 18) / (62 - 18), 0, 1)
alpha = np.asarray(Image.fromarray((alpha*255).astype(np.uint8)).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2)))
for k, f in enumerate(frames):
    f = f.copy(); gg = f[...,1]; lim = (f[...,0] + f[...,2]) / 2 + 6
    f[...,1] = np.where(gg > lim, lim, gg)                  # despill green fringes
    Image.fromarray(np.dstack([np.clip(f,0,255).astype(np.uint8), alpha])).save(f'{H}/host_rgba_{k}.png')
json.dump(dict(mouth=[cx, cy, w_, h_], shift_mid=s1, shift_open=s2), open(f'{H}/host_meta.json','w'))
print("aligned shifts", s1, s2, "| mouth centre", (cx, cy), "size", (w_, h_), "| alpha coverage %.1f%%" % (alpha.mean()/2.55))
# check sheet: cut-out over dark grey, three mouth crops zoomed, new s4
sheet = Image.new('RGB', (1500, 700), (24,24,24))
for k in range(3):
    im = Image.open(f'{H}/host_rgba_{k}.png'); bg = Image.new('RGBA', im.size, (60,64,70,255)); bg.alpha_composite(im)
    if k == 0: sheet.paste(bg.convert('RGB').resize((448,600)), (10,50))
    crop = bg.crop((cx-110, cy-80, cx+110, cy+80)).resize((330,240)); sheet.paste(crop.convert('RGB'), (470, 10+k*232))
s4 = Image.open('/home/user/projects/ep7_mule/img/s4_handcuffs.jpg').convert('RGB'); sheet.paste(s4.resize((360, 645)), (820, 30))
edge = Image.open(f'{H}/host_rgba_0.png'); bgw = Image.new('RGBA', edge.size, (250,250,250,255)); bgw.alpha_composite(edge)
sheet.paste(bgw.convert('RGB').crop((250,60,650,460)).resize((300,300)), (1190, 30))
sheet.save('/home/user/.cache/host_check.jpg', quality=88)
