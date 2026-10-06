#!/usr/bin/env python3
"""
source_style.py: Benaqaab "SOURCE FOOTAGE" look (user reference, 30 Sep 2026: brand/style_refs/source_footage_ref.png)

Every third-party clip or photo (news footage, official video, file photos) gets the SAME treatment, so it reads as
"quoted evidence inside our own design":
  1. high-contrast black & white (crushed blacks)
  2. fine halftone / dot-screen texture
  3. soft colour glows, screen-blended (dark red on one side, olive in the top corner)
  4. a translucent RED BAND across the eye line, screen-blended (the image shows through, tinted red)
  5. vignette

Deterministic (pure numpy), so it is safe for frame-exact renders. Works on videos (→ JPEG frame sequence and/or MP4)
and on still images.

  python3 viz/source_style.py IN.mp4  OUTDIR  --start 12.5 --dur 4 --size 1920x1080 --band 0.27,0.38 [--mp4 out.mp4]
  python3 viz/source_style.py IN.jpg  OUT.jpg --size 1920x1080 --band none
  python3 viz/source_style.py IN.mp4  OUTDIR  --band 0.30,0.41 --glow left      (mirror the glow side)
  python3 viz/source_style.py IN.mp4  OUTDIR  --dynamic                          (moving grain + band wipe-in)

Honest note: a stylised look does NOT by itself make copyrighted footage "safe". Keep clips short, credited, muted,
used for commentary/reporting, and prefer official or free-licence sources.
"""
import argparse, os, subprocess, sys, json
import numpy as np
from PIL import Image

RED_BAND = np.array([140, 20, 16], np.float32) / 255.0      # screen-blend colour measured from the reference
GLOW_RED = np.array([70, 8, 8], np.float32) / 255.0
GLOW_OLIVE = np.array([46, 42, 6], np.float32) / 255.0


def cover(img: Image.Image, W: int, H: int, cx=0.5, cy=0.5) -> Image.Image:
    w, h = img.size; r = W / H
    if w / h > r: nw, nh = int(round(h * r)), h
    else: nw, nh = w, int(round(w / r))
    x0 = int(round((w - nw) * cx)); y0 = int(round((h - nh) * cy))
    return img.crop((x0, y0, x0 + nw, y0 + nh)).resize((W, H), Image.LANCZOS)


_cache = {}
def _static_layers(W, H, pitch, band, glow_side, vignette):
    key = (W, H, pitch, band, glow_side, vignette)
    if key in _cache: return _cache[key]
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    # dot screen: bright round dots on a darker grid (multiplied into the luminance)
    cxm = (xx % pitch) - pitch / 2 + 0.5; cym = (yy % pitch) - pitch / 2 + 0.5
    d = np.sqrt(cxm ** 2 + cym ** 2) / (pitch / 2)                      # 0 at dot centre, ~1 at cell edge
    dots = np.clip(1.0 - np.clip((d - 0.55) / 0.35, 0, 1) * 0.42, 0, 1)   # 1.0 inside dot → 0.58 between dots
    # glows (screen-blended colour light)
    gx = W * (0.98 if glow_side == 'right' else 0.02)
    g1 = np.exp(-(((xx - gx) / (W * 0.30)) ** 2 + ((yy - H * 0.52) / (H * 0.45)) ** 2))
    g2 = np.exp(-(((xx - (W * 0.97 if glow_side == 'right' else W * 0.03)) / (W * 0.16)) ** 2 + ((yy - H * 0.02) / (H * 0.14)) ** 2))
    glow = np.clip(g1[..., None] * GLOW_RED * 0.6 + g2[..., None] * GLOW_OLIVE * 0.62, 0, 1)   # subtle, as in the reference
    # red band with soft 2 px edges
    bandm = np.zeros((H, W), np.float32)
    if band:
        t, b = band[0] * H, band[1] * H
        bandm = np.clip(np.minimum(yy - t + 1, b - yy + 1) / 2.0, 0, 1)
    # vignette
    vx = (xx / W - 0.5) * 2; vy = (yy / H - 0.5) * 2
    vig = np.clip(1 - vignette * (0.55 * vx ** 2 + 0.75 * vy ** 2), 0, 1)
    _cache[key] = (dots, glow, bandm, vig)
    return _cache[key]


def style_array(rgb: np.ndarray, pitch=11, band=(0.27, 0.38), glow_side='right', vignette=0.38,
                black=0.10, white=0.94, gamma=1.12, frame=0, grain=0.0, band_k=1.0) -> np.ndarray:
    """rgb: HxWx3 uint8 → styled HxWx3 uint8."""
    H, W = rgb.shape[:2]
    x = rgb.astype(np.float32) / 255.0
    lum = x[..., 0] * 0.299 + x[..., 1] * 0.587 + x[..., 2] * 0.114
    lum = np.clip((lum - black) / (white - black), 0, 1) ** gamma            # crushed blacks, punchy mids
    if grain > 0:   # DYNAMIC: film grain that changes every frame (seeded by frame index → deterministic renders)
        rng = np.random.default_rng(1000 + int(frame)); lum = np.clip(lum + rng.normal(0, grain, lum.shape).astype(np.float32), 0, 1)
    dots, glow, bandm, vig = _static_layers(W, H, pitch, band, glow_side, vignette)
    g = lum * dots * vig
    base = np.repeat(g[..., None], 3, axis=2) * np.array([1.0, 0.975, 0.965], np.float32)   # faint warm grey (as in the ref)
    screen = lambda a, c: 1 - (1 - a) * (1 - c)
    out = screen(base, glow)
    if band and band_k > 0:
        bm = bandm
        if band_k < 1:   # DYNAMIC: the red band wipes in left→right
            edge = int(W * (1 - (1 - band_k) ** 3)); bm = bandm.copy(); bm[:, edge:] = 0
        out = out * (1 - bm[..., None]) + screen(out, RED_BAND * 1.0) * bm[..., None]
    return (np.clip(out, 0, 1) * 255 + 0.5).astype(np.uint8)


def auto_band(frames, default=(0.27, 0.38)):
    """Eye-line band from the largest detected face (OpenCV Haar, placement only, no identification)."""
    try:
        import cv2
    except Exception:
        return default
    casc = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'); ys = []
    for fr in frames:
        H = fr.shape[0]; g = cv2.cvtColor(fr, cv2.COLOR_RGB2GRAY)
        faces, _, wts = casc.detectMultiScale3(g, scaleFactor=1.1, minNeighbors=5, minSize=(int(H * 0.05), int(H * 0.05)), outputRejectLevels=True)
        cand = [(float(wt), f) for f, wt in zip(faces, wts) if float(wt) >= 5.0]   # confident faces only (round patterns like the Ashoka Chakra score 3-5)
        if cand:
            x, y, w, h = max(cand, key=lambda c: c[0])[1]; ys.append(((y + 0.42 * h) / H, h / H))
    if not ys: return default
    ey = float(np.median([a for a, _ in ys])); fh = float(np.median([b for _, b in ys]))
    bh = min(0.12, max(0.07, 0.42 * fh))
    return (max(0.0, ey - bh / 2), min(1.0, ey + bh / 2))


def style_image(path_in, path_out, W, H, **kw):
    img = cover(Image.open(path_in).convert('RGB'), W, H, kw.pop('cx', 0.5), kw.pop('cy', 0.5))
    arr = np.asarray(img)
    if kw.get('band') == 'auto': kw['band'] = auto_band([arr])
    Image.fromarray(style_array(arr, **kw)).save(path_out, quality=92)
    return kw.get('band')


def style_video(path_in, outdir, W, H, start=0.0, dur=None, fps=30, mp4=None, **kw):
    os.makedirs(outdir, exist_ok=True)
    cx, cy = kw.pop('cx', 0.5), kw.pop('cy', 0.5)
    # decode → raw RGB frames at the target fps, cover-cropped to W×H by ffmpeg
    vf = f"fps={fps},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}:(in_w-{W})*{cx}:(in_h-{H})*{cy}"
    cmd = ['ffmpeg', '-v', 'error'] + (['-ss', str(start)] if start else []) + ['-i', path_in] + (['-t', str(dur)] if dur else []) + \
          ['-an', '-vf', vf, '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-']
    fsz = W * H * 3
    if kw.get('band') == 'auto':   # sample ~1 fps for face detection first
        sc = [c if c != f'fps={fps},' else c for c in cmd]
        sc[sc.index('-vf') + 1] = vf.replace(f'fps={fps}', 'fps=1.5')
        raw = subprocess.run(sc, capture_output=True).stdout
        smp = [np.frombuffer(raw[i:i + fsz], np.uint8).reshape(H, W, 3) for i in range(0, len(raw) - fsz + 1, fsz)]
        kw['band'] = auto_band(smp); print('auto band:', tuple(round(v, 3) for v in kw['band']))
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE); n = 0
    while True:
        buf = p.stdout.read(fsz)
        if len(buf) < fsz: break
        fr = np.frombuffer(buf, np.uint8).reshape(H, W, 3)
        n += 1
        dyn = kw.pop('dynamic', None) if 'dynamic' in kw else None
        if dyn is not None: kw['_dyn'] = dyn
        d = kw.get('_dyn')
        extra = dict(frame=n, grain=0.045, band_k=min(1.0, (n - 1) / (fps * 0.45))) if d else {}
        Image.fromarray(style_array(fr, **{k: v for k, v in kw.items() if k != '_dyn'}, **extra)).save(os.path.join(outdir, f'f_{n:04d}.jpg'), quality=90)
    p.wait()
    if mp4:
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-framerate', str(fps), '-i', os.path.join(outdir, 'f_%04d.jpg'),
                        '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18', mp4], check=True)
    return n


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('inp'); ap.add_argument('out')
    ap.add_argument('--size', default='1920x1080'); ap.add_argument('--start', type=float, default=0.0); ap.add_argument('--dur', type=float)
    ap.add_argument('--fps', type=int, default=30); ap.add_argument('--mp4')
    ap.add_argument('--band', default='auto', help="'auto' (eye line of the largest face), 'top,bottom' fractions, or 'none'")
    ap.add_argument('--pitch', type=int, default=0, help='dot pitch in px (default: height/98)')
    ap.add_argument('--glow', default='right', choices=['right', 'left'])
    ap.add_argument('--cx', type=float, default=0.5); ap.add_argument('--cy', type=float, default=0.5)
    ap.add_argument('--dynamic', action='store_true', help='moving film grain + red band wipes in over the first 0.45 s')
    a = ap.parse_args()
    W, H = map(int, a.size.lower().split('x'))
    band = None if a.band == 'none' else ('auto' if a.band == 'auto' else tuple(float(v) for v in a.band.split(',')))
    kw = dict(pitch=a.pitch or max(6, round(min(W, H) / 88)), band=band, glow_side=a.glow, cx=a.cx, cy=a.cy)
    if a.dynamic and not a.inp.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')): kw['dynamic'] = True
    if a.inp.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        b = style_image(a.inp, a.out, W, H, **kw); print('styled image →', a.out, '| band', b)
    else:
        n = style_video(a.inp, a.out, W, H, start=a.start, dur=a.dur, fps=a.fps, mp4=a.mp4, **kw)
        print(f'styled {n} frames → {a.out}' + (f' (+ {a.mp4})' if a.mp4 else ''))
