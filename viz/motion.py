#!/usr/bin/env python3
"""
MOTION CORE v2 — the technique layer extracted from the Opus-5.5 motion-graphics
pipelines (see MEMORY §58/§59/§62 and MOTION_RESEARCH_Opus55.md).

Verified directly from Barty-Bart/motion-graphics, which states:
  "Every frame is a pure function of time. Springs are closed-form step responses,
   and a value that changes target many times is the sum of one spring per change.
   There are no CSS transitions or timers, so any frame can be rendered on its own."
  "Headless Chromium captures 4 sub-frames per frame across a 180 degree shutter,
   and ffmpeg blends them into motion blur."
and from howseen-ai/claude-motion-design: "6-8 subframes for fast moves, 4 = ghosting".

Our Pillow pipeline is the same architecture, so all of it ports directly.
viz/motion.js is a line-for-line port with the same numbers (for HTML/Chromium renders).

Provides:
  spring() / spring_velocity()   closed-form damped step response and its derivative
  Track           value whose target changes over time = SUM of one spring per change
  ARRIVE/SETTLE/SWEEP/CUT        the four named curves; use these and nothing else
  Beat            120 BPM grid helpers
  Morph           ONE shape that never cuts: edges on springs (lead edge stiffer, so it
                  stretches), radius on a spring, colour switches on the beat
  Camera          one transform for the whole stage; zoom interpolated in LOG space
  render_blurred() motion blur: adaptive subframes across a 180 degree shutter,
                  linear-light blend, premultiplied alpha, SAFE frame reuse
  handoff() / appear() / leave()  text in/out that can never overlap or pop
  contact_sheet() / motion_report() / loop_seam()   QA

v2 changes (2026-09-30), after testing v1:
  * FIXED: v1 reused the previous frame whenever moving_fn said "not moving", without
    checking that anything was unchanged. A slow push-in lost half its frames (judder),
    hard cuts landed a frame late, and two render functions could swap frames. Reuse now
    happens ONLY when the caller's state_fn(t) signature matches, keyed per render_fn.
  * Adaptive sample count from on-screen speed (speed_fn, px/s): 1 sample when the
    smear is sub-pixel, up to max_samples on fast moves, so fast moves don't ghost.
  * Blur averages in linear light (like a real shutter) with premultiplied alpha,
    and rounds instead of truncating.
  * Track keeps keys sorted (out-of-order .to() calls are safe), supports per-change
    springs, velocity(), settled(), rest_at().
  * handoff() eases its fades (linear reads as robotic, per house rules).
"""
import math
import subprocess
from collections import OrderedDict

import numpy as np
from PIL import Image, ImageDraw, ImageFont


# ────────────────────────────── curves
def _bezier(p1x, p1y, p2x, p2y):
    """Cubic-bezier easing, Newton-solved with a bisection fallback. Matches CSS."""
    def bez(t, a, b):
        return 3*(1-t)**2*t*a + 3*(1-t)*t*t*b + t**3
    def slope(t, a, b):
        return 3*(1-t)**2*a + 6*(1-t)*t*(b-a) + 3*t*t*(1-b)
    def f(x):
        if x <= 0: return 0.0
        if x >= 1: return 1.0
        t = x
        for _ in range(8):
            s = slope(t, p1x, p2x)
            if abs(s) < 1e-6: break
            t -= (bez(t, p1x, p2x) - x) / s
            t = min(1.0, max(0.0, t))
        if abs(bez(t, p1x, p2x) - x) > 1e-7:          # rare: fall back to bisection
            lo, hi = 0.0, 1.0
            for _ in range(40):
                t = (lo + hi) / 2
                if bez(t, p1x, p2x) < x: lo = t
                else: hi = t
        return bez(t, p1y, p2y)
    return f

cubic_bezier = _bezier


def spring(t, d=0.68, w=13.0):
    """Closed-form damped step response. 0 -> 1.

    d=0.68, w=13 (measured): 5.4% overshoot at 0.33 s, within 2% by 0.46 s, at rest
    (1/2000 of the swing) by 0.84 s. 'Critically damped spring, tiny overshoot, no
    repeated bouncing'. Deterministic: depends only on t, never on previous frames.
    """
    if t <= 0.0:
        return 0.0
    if d >= 1.0:                                   # critically damped
        return 1.0 - math.exp(-w*t) * (1.0 + w*t)
    wd = w * math.sqrt(1.0 - d*d)
    return 1.0 - math.exp(-d*w*t) * (math.cos(wd*t) + (d*w/wd) * math.sin(wd*t))


def spring_velocity(t, d=0.68, w=13.0):
    """d/dt of spring(): swing-lengths per second. Peaks ~6.1/s at t~0.09 s (defaults)."""
    if t <= 0.0:
        return 0.0
    if d >= 1.0:
        return w*w*t*math.exp(-w*t)
    wd = w * math.sqrt(1.0 - d*d)
    return math.exp(-d*w*t) * (w*w/wd) * math.sin(wd*t)


def spring_settled(t, d=0.68, w=13.0, eps=1/2000):
    """True once the spring is within eps of rest — used for frame reuse.
    (The thursday/motion PR measured 41% of frames reusable with this at 1/2000.)"""
    return t > 0 and abs(1.0 - spring(t, d, w)) < eps and math.exp(-min(d, 1.0)*w*t) < eps


# The only four curves allowed. A limited, named vocabulary is what makes motion
# read as art-directed instead of assembled.
ARRIVE = lambda t: spring(t)                        # everything that enters
SETTLE = _bezier(0.16, 1.00, 0.30, 1.00)            # brakes hard into position
SWEEP  = _bezier(0.80, 0.00, 0.12, 1.00)            # masks, wipes, camera moves
CUT    = lambda t: 1.0 if t > 0 else 0.0            # colour, on the beat only


def _clamp01(x):
    return 0.0 if x <= 0 else 1.0 if x >= 1 else x


def smoothstep(x):
    x = _clamp01(x)
    return x * x * (3 - 2 * x)


class Track:
    """A value whose target changes over time.

    Per the verified rule: 'a value that changes target many times is the SUM of
    one spring per change'. Closed-form and seekable — no integration, no state.
    Retargeting mid-flight stays smooth (position AND velocity continuous).

        x = Track(0).to(1.0, 400).to(2.6, 180)     # at t=1.0 go to 400, at 2.6 to 180
        x.at(t), x.velocity(t), x.moving(t)

    Keys are kept sorted, so .to() calls may arrive in any order. Each change may
    use its own spring (d, w) — Morph uses that to make leading edges stiffer.
    """
    def __init__(self, start=0.0, d=0.68, w=13.0):
        self.v0 = float(start); self.d = d; self.w = w
        self._keys = []                              # (t, target, d, w), sorted by t
        self._steps = []                             # derived: (t, delta, d, w)
        self.steps = []                              # v1-compatible view: (t, delta)

    def to(self, t_start, value, d=None, w=None):
        self._keys.append((float(t_start), float(value),
                           self.d if d is None else d, self.w if w is None else w))
        self._keys.sort(key=lambda k: k[0])
        prev, steps = self.v0, []
        for ts, v, dd, ww in self._keys:
            steps.append((ts, v - prev, dd, ww)); prev = v
        self._steps = steps
        self.steps = [(ts, dv) for ts, dv, _, _ in steps]
        return self

    def target_before(self, t):
        v = self.v0
        for ts, dv, _, _ in self._steps:
            if ts <= t: v += dv
        return v

    target = target_before

    def at(self, t):
        v = self.v0
        for ts, dv, dd, ww in self._steps:
            if t > ts:
                v += dv * spring(t - ts, dd, ww)
        return v

    def velocity(self, t):
        return sum(dv * spring_velocity(t - ts, dd, ww)
                   for ts, dv, dd, ww in self._steps if t > ts)

    def moving(self, t, eps=1/2000):
        """False when every spring has come to rest -> the frame can be reused."""
        for ts, dv, dd, ww in self._steps:
            if abs(t - ts) < 1e-9 and abs(dv) > 1e-9:
                return True
            if t > ts and abs(dv) > 1e-9 and not spring_settled(t - ts, dd, ww, eps):
                return True
        return False

    def settled(self, t, eps=1/2000):
        return not self.moving(t, eps)

    def rest_at(self, t, eps=1/2000):
        """Exact target once at rest (sub-pixel tail snapped), else the live value.
        Use in state signatures so rested frames are recognised as identical."""
        return self.target_before(t) if self.settled(t, eps) else self.at(t)


# ────────────────────────────── beat grid
class Beat:
    """120 BPM grid. Something should happen on every beat."""
    def __init__(self, bpm=120.0, offset=0.0):
        self.period = 60.0 / bpm
        self.offset = offset

    def snap(self, t):
        """Nearest beat to t — snap every entrance to this."""
        return self.offset + round((t - self.offset)/self.period) * self.period

    def index(self, t):
        return int((t - self.offset) // self.period)

    def times(self, total):
        out, k = [], 0
        while self.offset + k*self.period < total:
            out.append(self.offset + k*self.period); k += 1
        return out


# ────────────────────────────── one shape, never cut
def _lin(c):   # sRGB 0..255 -> linear 0..1
    c = c / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

def _srgb(x):  # linear 0..1 -> sRGB 0..255
    x = _clamp01(x)
    return 255.0 * (12.92 * x if x <= 0.0031308 else 1.055 * x ** (1 / 2.4) - 0.055)

def mix_color(a, b, k):
    """Blend two RGB(A) colours in LINEAR light (no muddy midpoint)."""
    k = _clamp01(k)
    out = [round(_srgb(_lin(x) + (_lin(y) - _lin(x)) * k)) for x, y in zip(a[:3], b[:3])]
    if len(a) > 3 or len(b) > 3:
        aa = a[3] if len(a) > 3 else 255; bb = b[3] if len(b) > 3 else 255
        out.append(round(aa + (bb - aa) * k))
    return tuple(out)


class Morph:
    """ONE element that never cuts (MakerMap / Barty-Bart 'one shape, never cut').

    Every state is the same rectangle changing edges, corner radius and colour while
    the content inside swaps. Each edge rides its own spring; on every move the edge
    travelling in the direction of motion is stiffer than the one behind it, so the
    shape stretches and then catches up, like the tab indicators in the references.

        m = Morph(x=90, y=800, w=300, h=90, r=45, color=(255,210,63))
        m.to(1.0, x=90, y=500, w=900, h=640, r=36)          # pill -> card
        m.to(2.4, color=(63,227,255))                        # colour on the beat (CUT)
        s = m.at(t)   # {'x','y','w','h','r','color','box'}
    """
    def __init__(self, x, y, w, h, r=0.0, color=(255, 255, 255), d=0.68,
                 w_lead=15.0, w_trail=11.0, color_blend=0.0):
        self.L, self.T = Track(x, d), Track(y, d)
        self.R, self.B = Track(x + w, d), Track(y + h, d)
        self.rad = Track(r, d, 12.0)
        self.d, self.w_lead, self.w_trail = d, w_lead, w_trail
        self.colors = [(-1e9, tuple(color))]
        self.color_blend = color_blend              # 0 = CUT (house default)

    def to(self, t, x=None, y=None, w=None, h=None, r=None, color=None):
        L0, T0 = self.L.target(t), self.T.target(t)
        R0, B0 = self.R.target(t), self.B.target(t)
        L1 = L0 if x is None else float(x)
        T1 = T0 if y is None else float(y)
        R1 = (L1 + (R0 - L0)) if w is None else L1 + float(w)
        B1 = (T1 + (B0 - T0)) if h is None else T1 + float(h)
        # direction of travel on each axis decides which edge leads
        cx = (L1 + R1) - (L0 + R0); cy = (T1 + B1) - (T0 + B0)
        wl, wt = self.w_lead, self.w_trail
        self.R.to(t, R1, w=(wl if cx >= 0 else wt)); self.L.to(t, L1, w=(wt if cx >= 0 else wl))
        self.B.to(t, B1, w=(wl if cy >= 0 else wt)); self.T.to(t, T1, w=(wt if cy >= 0 else wl))
        if r is not None: self.rad.to(t, float(r))
        if color is not None:
            self.colors.append((float(t), tuple(color))); self.colors.sort(key=lambda c: c[0])
        return self

    def color_at(self, t):
        prev = self.colors[0][1]
        for tc, c in self.colors[1:]:
            if t < tc: break
            if self.color_blend > 0 and t < tc + self.color_blend:
                return mix_color(prev, c, SETTLE((t - tc) / self.color_blend))
            prev = c
        return prev

    def at(self, t):
        L, T, R, B = self.L.at(t), self.T.at(t), self.R.at(t), self.B.at(t)
        w, h = max(0.0, R - L), max(0.0, B - T)
        r = max(0.0, min(self.rad.at(t), w / 2, h / 2))
        return dict(x=L, y=T, w=w, h=h, r=r, color=self.color_at(t), box=(L, T, R, B))

    def speed(self, t):
        return max(abs(k.velocity(t)) for k in (self.L, self.T, self.R, self.B))

    def moving(self, t):
        return any(k.moving(t) for k in (self.L, self.T, self.R, self.B, self.rad))

    def signature(self, t, nd=2):
        tr = lambda k: round(k.rest_at(t), nd)
        return (tr(self.L), tr(self.T), tr(self.R), tr(self.B), tr(self.rad), self.color_at(t))

    def draw(self, img, t, fill_override=None):
        """Draw onto a PIL RGBA image with 4x-supersampled anti-aliased corners."""
        s = self.at(t)
        if s['w'] < 0.5 or s['h'] < 0.5: return img
        rounded_box(img, s['box'], s['r'], fill_override or s['color'])
        return img


def rounded_box(img, box, radius, fill, ss=4):
    """Anti-aliased rounded rectangle composited onto an RGBA image (Pillow's own
    rounded_rectangle has hard stair-step edges). Handles sub-pixel positions."""
    L, T, R, B = box
    x0, y0 = int(math.floor(L)) - 1, int(math.floor(T)) - 1
    x1, y1 = int(math.ceil(R)) + 1, int(math.ceil(B)) + 1
    W, H = max(1, x1 - x0), max(1, y1 - y0)
    m = Image.new('L', (W * ss, H * ss), 0)
    ImageDraw.Draw(m).rounded_rectangle(
        [(L - x0) * ss, (T - y0) * ss, (R - x0) * ss - 1, (B - y0) * ss - 1],
        radius=max(0, radius * ss), fill=255)
    m = m.resize((W, H), Image.LANCZOS)
    fill = tuple(fill) + ((255,) if len(fill) == 3 else ())
    layer = Image.new('RGBA', (W, H), fill[:3] + (0,))
    a = np.asarray(m, dtype=np.float32) * (fill[3] / 255.0)
    layer.putalpha(Image.fromarray(np.clip(a + 0.5, 0, 255).astype(np.uint8)))
    sx, sy = max(0, -x0), max(0, -y0)
    if sx >= W or sy >= H:
        return img
    dx, dy = max(0, x0), max(0, y0)
    if img.mode == 'RGBA':
        img.alpha_composite(layer, (dx, dy), (sx, sy))
    else:
        base = img.convert('RGBA'); base.alpha_composite(layer, (dx, dy), (sx, sy))
        img.paste(base.convert(img.mode))
    return img


# ────────────────────────────── camera
class Camera:
    """One transform for the whole content layer (captions/HUD stay in screen space).

    Keys are moves: key(t0, t1, zoom=, x=, y=). Zoom is interpolated in LOG space,
    so 1 -> 2 feels as fast as 2 -> 4. validate() flags a zoom-in immediately
    followed by a zoom-out (or vice versa), which the references ban.
    """
    def __init__(self, zoom=1.0, x=0.0, y=0.0):
        self.start = (float(zoom), float(x), float(y))
        self.moves = []                              # (t0, t1, z, x, y, curve)

    def key(self, t0, t1, zoom=None, x=None, y=None, curve=None):
        self.moves.append((float(t0), float(t1), zoom, x, y, curve or SWEEP))
        self.moves.sort(key=lambda m: m[0])
        return self

    def at(self, t):
        z, x, y = self.start
        for t0, t1, zz, xx, yy, curve in self.moves:
            if t <= t0: break
            k = curve(_clamp01((t - t0) / max(1e-6, t1 - t0)))
            if zz is not None: z = math.exp(math.log(z) + (math.log(zz) - math.log(z)) * k)
            if xx is not None: x = x + (xx - x) * k
            if yy is not None: y = y + (yy - y) * k
        return z, x, y

    def speed(self, t, radius=1101.0, dt=1/240):
        """Fastest on-screen pixel speed (px/s): pan plus zoom at the frame edge."""
        z0, x0, y0 = self.at(t - dt); z1, x1, y1 = self.at(t + dt)
        pan = math.hypot(x1 - x0, y1 - y0) * (z0 + z1) / 2
        return (pan + abs(z1 - z0) * radius) / (2 * dt)

    def validate(self):
        warn, last_dir = [], 0
        z = self.start[0]
        for t0, t1, zz, *_ in self.moves:
            if zz is None: continue
            dirn = (zz > z) - (zz < z)
            if dirn and last_dir and dirn != last_dir:
                warn.append(f"zoom reverses at t={t0:.2f}s (in/out back-to-back)")
            last_dir, z = dirn or last_dir, zz
        return warn


# ────────────────────────────── motion blur
_TO_LIN = np.array([_lin(i) for i in range(256)], dtype=np.float32)
_TO_SRGB = np.array([round(_srgb(i / 4095.0)) for i in range(4096)], dtype=np.uint8)


class FrameCache:
    """Tiny LRU for rested frames. Key = (render_fn, state signature)."""
    def __init__(self, maxsize=8):
        self.maxsize, self.d = maxsize, OrderedDict()
    def get(self, k):
        if k in self.d:
            self.d.move_to_end(k); return self.d[k]
        return None
    def put(self, k, v):
        self.d[k] = v; self.d.move_to_end(k)
        while len(self.d) > self.maxsize: self.d.popitem(last=False)
    def clear(self):
        self.d.clear()

_FRAME_CACHE = FrameCache()


def _freeze(x):
    if isinstance(x, dict): return tuple(sorted((k, _freeze(v)) for k, v in x.items()))
    if isinstance(x, (list, tuple)): return tuple(_freeze(v) for v in x)
    if isinstance(x, float): return round(x, 4)
    if isinstance(x, np.ndarray): return tuple(np.round(x.astype(float), 4).ravel().tolist())
    return x


def signature(*values, nd=2):
    """Build a state signature: floats rounded to nd decimals (0.01 px by default)."""
    return tuple(round(v, nd) if isinstance(v, float) else _freeze(v) for v in values)


def _to_array(img):
    return np.asarray(img) if not isinstance(img, np.ndarray) else img


def blend_frames(frames, linear=True):
    """Average frames like a camera shutter: linear light, premultiplied alpha,
    rounded. Accepts PIL images or uint8 arrays (H,W,3|4 or H,W)."""
    arrs = [_to_array(f) for f in frames]
    n = len(arrs)
    if n == 1:
        return Image.fromarray(arrs[0])
    a0 = arrs[0]
    has_alpha = a0.ndim == 3 and a0.shape[2] == 4
    if has_alpha:
        acc_c = np.zeros(a0.shape[:2] + (3,), np.float32); acc_a = np.zeros(a0.shape[:2], np.float32)
        for a in arrs:
            al = a[..., 3].astype(np.float32) / 255.0
            c = _TO_LIN[a[..., :3]] if linear else a[..., :3].astype(np.float32) / 255.0
            acc_c += c * al[..., None]; acc_a += al
        cov = acc_a / n
        col = np.divide(acc_c, acc_a[..., None], out=np.zeros_like(acc_c), where=acc_a[..., None] > 1e-6)
        rgb = _TO_SRGB[np.clip(col * 4095 + 0.5, 0, 4095).astype(np.uint16)] if linear \
            else np.clip(col * 255 + 0.5, 0, 255).astype(np.uint8)
        alpha = np.clip(cov * 255 + 0.5, 0, 255).astype(np.uint8)
        return Image.fromarray(np.dstack([rgb, alpha]), 'RGBA')
    if linear:
        acc = np.zeros(a0.shape, np.float32)
        for a in arrs: acc += _TO_LIN[a]
        out = _TO_SRGB[np.clip(acc / n * 4095 + 0.5, 0, 4095).astype(np.uint16)]
    else:
        acc = np.zeros(a0.shape, np.float32)
        for a in arrs: acc += a
        out = np.clip(acc / n + 0.5, 0, 255).astype(np.uint8)
    return Image.fromarray(out)


def samples_for_speed(speed_px_s, fps, shutter=0.5, max_gap=3.0, max_samples=12):
    """How many subframes keep neighbouring samples <= max_gap px apart.
    Sub-pixel smear -> 1 (no blur). The references: 4 = ghosting on fast moves."""
    smear = abs(speed_px_s) * shutter / fps
    if smear < 0.75:
        return 1
    return int(max(2, min(max_samples, math.ceil(smear / max_gap) + 1)))


def render_blurred(render_fn, t, fps, samples=4, shutter=0.5, moving_fn=None,
                   state_fn=None, speed_fn=None, max_samples=12, max_gap=3.0,
                   linear=True, cache=None):
    """One output frame = blend of sub-frames across a 180 degree shutter.

    render_fn(t)  -> PIL image or uint8 array. Must be a pure function of t.
    speed_fn(t)   -> fastest on-screen speed in px/s (preferred). Picks the sample
                     count: 1 when the smear is sub-pixel, up to max_samples.
    moving_fn(t)  -> bool (v1 API). True = `samples` subframes, False = 1 sample.
    state_fn(t)   -> hashable signature of EVERYTHING visible. A still frame is
                     reused only if its signature was seen before for this render_fn.
                     Without state_fn nothing is ever reused (correct, just slower).

    shutter=0.5 = 180 degrees, the film-standard look the reference pipeline uses.
    """
    cache = _FRAME_CACHE if cache is None else cache
    dt = 1.0 / fps
    if speed_fn is not None:
        n = samples_for_speed(float(speed_fn(t) or 0.0), fps, shutter, max_gap, max_samples)
    elif moving_fn is not None:
        n = samples if moving_fn(t) else 1
    else:
        n = samples

    if n == 1:
        key = None
        if state_fn is not None:
            key = (render_fn, _freeze(state_fn(t)))
            hit = cache.get(key)
            if hit is not None:
                return hit
        img = render_fn(t)
        img = img if isinstance(img, Image.Image) else Image.fromarray(img)
        if key is not None:
            cache.put(key, img)
        return img

    subs = []
    for k in range(n):
        off = ((k + 0.5) / n - 0.5) * shutter * dt      # stratified, centred on t
        subs.append(render_fn(t + off))
    return blend_frames(subs, linear=linear)


# ────────────────────────────── text handoff / entrances / exits
def handoff(t, out_at, in_at, fade=0.18, curve=None):
    """Enforces: outgoing text reaches 0 BEFORE incoming starts.

    Returns (alpha_out, alpha_in). `in_at` is clamped so the two never overlap —
    this exact collision produced real bugs in episodes 4 and 5. Fades are eased
    (smoothstep by default); pass curve=lambda x: x only if you really want linear.
    """
    curve = curve or smoothstep
    in_at = max(in_at, out_at + fade)
    a_out = 1.0 - curve(_clamp01((t - out_at) / fade))
    a_in = curve(_clamp01((t - in_at) / fade))
    return a_out, a_in


def appear(t, t0, dur=0.6, curve=ARRIVE):
    """0 until the word lands, then the curve. 'Not shown before its beat': nothing
    is dimmed or greyed in advance — it is fully invisible until t0.
    ARRIVE runs on seconds (settles by itself); other curves run over `dur`."""
    if t <= t0:
        return 0.0
    return curve(t - t0) if curve is ARRIVE else curve(_clamp01((t - t0) / dur))


def leave(t, t0, dur=0.25):
    """Exit: 1 -> exactly 0 over dur (1 - n^1.5). Exits are faster than entrances.
    Hard cuts are only allowed after this has reached 0."""
    return 1.0 - _clamp01((t - t0) / dur) ** 1.5


# ────────────────────────────── caption timing (measured numbers)
# From the thursday/motion research pass: words ~70ms apart, letters ~25ms,
# and roughly three words per second is the comfortable reading rate.
WORD_STAGGER = 0.070
LETTER_STAGGER = 0.025
READ_RATE_WPS = 3.0

def read_time(text, floor=1.2):
    """How long a line must stay on screen to be readable."""
    return max(floor, len(str(text).split()) / READ_RATE_WPS)


# ────────────────────────────── QA
def contact_sheet(frames, labels=None, cols=4, thumb_w=270, pad=8, bg=(18, 18, 18)):
    """Grid of frames (PIL/arrays) with optional labels — review one frame per beat."""
    ims = [f if isinstance(f, Image.Image) else Image.fromarray(f) for f in frames]
    if not ims: return Image.new('RGB', (thumb_w, thumb_w), bg)
    w0, h0 = ims[0].size
    th = int(thumb_w * h0 / w0); lab_h = 22 if labels else 0
    rows = math.ceil(len(ims) / cols)
    sheet = Image.new('RGB', (cols * (thumb_w + pad) + pad, rows * (th + lab_h + pad) + pad), bg)
    d = ImageDraw.Draw(sheet)
    try: font = ImageFont.truetype('DejaVuSans.ttf', 14)
    except Exception: font = ImageFont.load_default()
    for i, im in enumerate(ims):
        x = pad + (i % cols) * (thumb_w + pad); y = pad + (i // cols) * (th + lab_h + pad)
        sheet.paste(im.convert('RGB').resize((thumb_w, th), Image.LANCZOS), (x, y + lab_h))
        if labels: d.text((x + 2, y + 3), str(labels[i]), fill=(230, 230, 230), font=font)
    return sheet


def loop_seam(render_fn, duration, fps):
    """Mean abs difference (0-255) between frame 0 and the frame after the last
    one. ~0 means the loop is invisible."""
    a = _to_array(render_fn(0.0)).astype(np.float32)
    b = _to_array(render_fn(duration)).astype(np.float32)
    return float(np.abs(a - b).mean())


def motion_report(video, cuts=(), still_frac=0.002, still_px=0.02, still_d=0.8, pop_k=3.0,
                  ffmpeg='ffmpeg', size=(90, 160)):
    """Dead-beat and pop detector on a rendered file. Findings are WARNINGS to look at,
    not verdicts: for each window, say what is moving (video-talkcraft rule).

    * freezes: windows >= still_d seconds where fewer than still_frac of the pixels change
      by more than still_px (0-1 scale). LOCAL measure: a single word rising counts as
      motion even on a dark frame (a whole-frame average misses it — measured 2026-09-30).
    * pops:    frames whose mean difference is > pop_k x the median of their neighbours and
      are not listed in `cuts` (seconds): flashes, jumps, one-frame glitches.
    """
    w, h = size
    raw = subprocess.run([ffmpeg, '-v', 'error', '-i', str(video), '-vf',
                          f'scale={w}:{h},format=gray', '-f', 'rawvideo', '-'],
                         capture_output=True, check=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32) / 255.0
    probe = subprocess.run([ffmpeg, '-i', str(video)], capture_output=True, text=True).stderr
    fps = 30.0
    for tok in probe.split(','):
        if ' fps' in tok:
            try: fps = float(tok.strip().split(' ')[0])
            except ValueError: pass
    d = np.abs(np.diff(fr, axis=0))
    changed = (d > still_px).mean(axis=(1, 2))                  # share of pixels that moved
    mean = d.mean(axis=(1, 2))
    still = changed < still_frac
    freezes, start = [], None
    for i, s_ in enumerate(np.append(still, False)):
        if s_ and start is None: start = i
        elif not s_ and start is not None:
            if (i - start) / fps >= still_d: freezes.append((round(start / fps, 2), round(i / fps, 2)))
            start = None
    pops = []
    for i in range(2, len(mean) - 2):
        neigh = np.median(np.r_[mean[i - 2:i], mean[i + 1:i + 3]])
        t = (i + 1) / fps
        if mean[i] > pop_k * max(neigh, 1e-3) and mean[i] > 0.02 and \
                not any(abs(t - c) <= 1.5 / fps for c in cuts):
            pops.append(round(t, 3))
    return dict(frames=len(fr), fps=fps, duration=round(len(fr) / fps, 3), freezes=freezes,
                pops=pops, still_ratio=round(float(still.mean()) if len(still) else 0.0, 3))

# Benaqaab India toolkit file: KEEP. Never delete (user rule, 30 Sep 2026). Canonical copy: viz/motion.py; mirror: /home/user/motion.py
