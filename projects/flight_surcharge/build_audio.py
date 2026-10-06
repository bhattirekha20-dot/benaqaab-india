#!/usr/bin/env python3
"""
build_audio.py — audio master for "फ्लाइट क्यों महँगी" (film 3, flight surcharge).

Recipe (house, compact §12): narration placed at the measured times + one DISTINCT
SFX per cut + beds + scene accents -> sidechain duck under speech -> sample-peak
normalise in numpy (-2.0 dBFS) -> two-pass linear loudnorm to I -14 / TP -1.5 / LRA 6.

Everything is synthesised from scratch in numpy (no samples, no libraries beyond numpy).
Run:  python3 build_audio.py        (writes audio/master.wav then audio/master_loud.wav)
"""
import json, os, subprocess, sys, wave
import numpy as np

SR = 48000
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)

T = json.load(open('TIMELINE.json'))
TOTAL = T['total']
N = int(round((TOTAL + 0.5) * SR))
t_axis = np.arange(N) / SR
rng = np.random.default_rng(20261006)

# ---------------------------------------------------------------- helpers ----
def read_wav(path):
    with wave.open(path, 'rb') as w:
        n, ch, sw = w.getnframes(), w.getnchannels(), w.getsampwidth()
        raw = w.readframes(n)
    assert sw == 2, f'{path}: expected 16-bit'
    x = np.frombuffer(raw, '<i2').astype(np.float64) / 32768.0
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    return x

def place(buf, sig, t0, gain=1.0):
    i0 = int(round(t0 * SR))
    i1 = min(i0 + len(sig), len(buf))
    if i1 <= i0:
        return
    buf[i0:i1] += sig[:i1 - i0] * gain

def fade(x, ms=6.0):
    n = max(2, int(SR * ms / 1000))
    if len(x) <= 2 * n:
        return x
    e = np.linspace(0, 1, n)
    x = x.copy()
    x[:n] *= e
    x[-n:] *= e[::-1]
    return x

def env_exp(n, tau, attack=0.002):
    t = np.arange(n) / SR
    a = np.clip(t / max(attack, 1e-4), 0, 1)
    return a * np.exp(-t / tau)

def noise(n, seed):
    return np.random.default_rng(seed).normal(0, 1, n)

def band(x, lo, hi, order=2):
    """Zero-phase FFT band-pass (smooth raised-cosine edges)."""
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    mask = np.ones_like(f)
    lo_w = lo * 0.6
    hi_w = hi * 1.8
    mask *= np.clip((f - lo_w) / max(lo - lo_w, 1e-6), 0, 1)
    mask *= np.clip((hi_w - f) / max(hi_w - hi, 1e-6), 0, 1)
    mask = mask ** order
    return np.fft.irfft(X * mask, n=len(x))

def sweep(f0, f1, dur, curve='exp'):
    n = int(dur * SR)
    t = np.arange(n) / SR
    u = t / dur
    if curve == 'exp':
        k = (f1 / f0) ** (1 / dur)
        ph = 2 * np.pi * f0 * (k ** t - 1) / np.log(k)
    else:
        ph = 2 * np.pi * (f0 * t + (f1 - f0) * u ** 2 / (2 * dur))
    return np.sin(ph)

def tone(f, dur, tau=None):
    n = int(dur * SR)
    x = np.sin(2 * np.pi * f * np.arange(n) / SR)
    return x * (env_exp(n, tau) if tau else 1.0)

def bell(f, dur, tau):
    """small two-partial bell — used for UI reveals, never on top of a number"""
    n = int(dur * SR)
    t = np.arange(n) / SR
    x = 0.7 * np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 2.76 * t)
    return x * np.exp(-t / tau) * np.clip(t / 0.004, 0, 1)

# ------------------------------------------------------------- 1 · voices ----
voc = np.zeros(N)
for i in range(7):
    x = read_wav(f'audio/vo_{i+1}_48.wav')
    place(voc, x, T['narration_at'][i], 1.0)
    print(f'[vo] {i+1} @ {T["narration_at"][i]:7.3f}s  {len(x)/SR:6.3f}s')

# --------------------------------------------------------------- 2 · beds ----
pad = np.zeros(N)
for f, amp, lfo in [(110.0, 1.00, 0.031), (164.81, 0.62, 0.043), (220.0, 0.46, 0.027),
                    (329.63, 0.22, 0.037), (82.41, 0.55, 0.021)]:
    pad += amp * np.sin(2 * np.pi * f * t_axis + 1.7 * np.sin(2 * np.pi * lfo * t_axis))
pad *= 1.0 + 0.12 * np.sin(2 * np.pi * 0.043 * t_axis)
pad = band(pad, 60, 1400) * 0.055
fade_in = np.clip(t_axis / 4.0, 0, 1)
fade_out = np.clip((TOTAL - t_axis) / 5.0, 0, 1)
pad *= fade_in * fade_out

air = band(noise(N, 11), 900, 5200) * 0.010 * (0.65 + 0.35 * np.sin(2 * np.pi * 0.017 * t_axis))
air *= fade_in * fade_out

heart = np.zeros(N)                                   # slow sub pulse, 4-beat pattern
for k in range(int(TOTAL / 1.25) + 1):
    g = 1.0 if k % 4 == 0 else 0.45
    place(heart, tone(55.0, 0.55, 0.11), k * 1.25, g)
heart *= 0.10 * fade_in * fade_out

# tick beds (scale moments: the five tiers, the ATF ladder) — deliberately quiet
ticks = np.zeros(N)
for k in range(int(21.75 / 0.5) + 2, int(45.0 / 0.5)):        # S2 bars
    place(ticks, tone(2100.0, 0.05, 0.012), k * 0.5, 0.5)
for k in range(int(45.772 / 0.5) + 2, int(73.5 / 0.5)):       # S3 ladder
    place(ticks, tone(1750.0, 0.05, 0.012), k * 0.5, 0.5)
ticks *= 0.035

bed = pad + air + heart + ticks
print(f'[bed] pad+air+heart+ticks  peak {np.abs(bed).max():.4f}')

# ----------------------------------------------------------- 3 · cut SFX -----
CUTS = [(20.649979, 'Zoom to Change'), (45.222291, 'Signal Glitch 2'), (73.414270, 'White Flash'),
        (99.613499, 'Dissolve'), (119.506166, 'Fold Over'), (153.581187, 'Light Leaks')]
DUR = {'Zoom to Change': 0.80, 'Signal Glitch 2': 0.67, 'White Flash': 0.40,
       'Dissolve': 0.50, 'Fold Over': 1.00, 'Light Leaks': 1.00}
sfx = np.zeros(N)

def cut_zoom(t0):
    """1 · riser into a snap — the frame 'changes gear'"""
    n = int(0.70 * SR)
    sw = sweep(260, 1500, 0.70) * env_exp(n, 0.30, 0.05) * 0.30
    nz = band(noise(n, 21), 700, 4500) * env_exp(n, 0.22, 0.05) * 0.16
    place(sfx, fade(sw + nz), t0 - 0.42)
    place(sfx, fade(bell(2400, 0.18, 0.035)), t0 + 0.20, 0.30)
    place(sfx, fade(tone(70, 0.30, 0.07)), t0 + 0.20, 0.34)

def cut_glitch(t0):
    """2 · digital stutter + zip"""
    n = int(0.42 * SR)
    base = np.sign(np.sin(2 * np.pi * 3000 * np.arange(n) / SR)) * band(noise(n, 33), 800, 7000)
    gate = (noise(n, 34) > (-0.2 + 0.9 * np.linspace(0, 1, n))).astype(float)
    g2 = np.repeat(gate[::96], 96)[:n]
    place(sfx, fade(base * (0.4 + 0.6 * g2) * env_exp(n, 0.13, 0.004)), t0 - 0.10, 0.42)
    place(sfx, fade(sweep(2200, 380, 0.22) * env_exp(int(0.22 * SR), 0.07, 0.004)), t0 + 0.12, 0.30)
    place(sfx, fade(tone(58, 0.26, 0.06)), t0 + 0.10, 0.30)

def cut_flash(t0):
    """3 · reversed whoosh + sub thump (white flash)"""
    n = int(0.46 * SR)
    nz = band(noise(n, 45), 400, 9000)
    rev = nz * (np.linspace(0, 1, n) ** 2.2)
    place(sfx, fade(rev), t0 - 0.06, 0.34)
    place(sfx, fade(tone(54, 0.34, 0.09)), t0 + 0.16, 0.46)
    place(sfx, fade(bell(3100, 0.22, 0.05)), t0 + 0.16, 0.16)

def cut_dissolve(t0):
    """4 · airy swell — the softest of the six, a pad hand-off"""
    n = int(0.60 * SR)
    sw = band(noise(n, 57), 300, 3400) * np.sin(np.pi * np.linspace(0, 1, n)) ** 1.6
    place(sfx, fade(sw), t0 - 0.10, 0.26)
    place(sfx, fade(tone(330, 0.30, 0.10)), t0 + 0.22, 0.10)

def cut_fold(t0):
    """5 · paper fold — flutter sweep down + flap tick"""
    n = int(0.55 * SR)
    down = sweep(1900, 320, 0.55) * env_exp(n, 0.26, 0.01)
    flut = 0.55 + 0.45 * np.abs(np.sin(2 * np.pi * 7.5 * np.arange(n) / SR))
    place(sfx, fade(down * flut), t0 - 0.08, 0.26)
    place(sfx, fade(band(noise(n, 69), 500, 3000) * env_exp(n, 0.10, 0.004)), t0 + 0.34, 0.20)
    place(sfx, fade(tone(62, 0.24, 0.06)), t0 + 0.30, 0.28)

def cut_leaks(t0):
    """6 · shimmer rise + airy tail (light leaks)"""
    n = int(0.95 * SR)
    t = np.arange(n) / SR
    up = np.linspace(0, 1, n) ** 1.4
    shim = sum(np.sin(2 * np.pi * f * t) for f in (2200, 3300, 4400, 5500)) / 4
    shim *= (0.5 + 0.5 * np.abs(np.sin(2 * np.pi * 5.5 * t)))
    place(sfx, fade(shim * up * env_exp(n, 0.55, 0.06)), t0 - 0.12, 0.20)
    place(sfx, fade(band(noise(n, 81), 600, 6000) * up * env_exp(n, 0.40, 0.05)), t0 - 0.12, 0.16)
    place(sfx, fade(tone(66, 0.30, 0.08)), t0 + 0.30, 0.26)

for t0, name in CUTS:
    {'Zoom to Change': cut_zoom, 'Signal Glitch 2': cut_glitch, 'White Flash': cut_flash,
     'Dissolve': cut_dissolve, 'Fold Over': cut_fold, 'Light Leaks': cut_leaks}[name](t0)
    print(f'[cut] {name:16s} @ {t0:7.3f}s')

# -------------------------------------------------------- 4 · accents --------
acc = np.zeros(N)
# S1 — plane enters (whoosh), then fuel drips
place(acc, fade(band(noise(int(0.7 * SR), 91), 200, 2600) * np.sin(np.pi * np.linspace(0, 1, int(0.7 * SR))) ** 1.5), 5.6, 0.13)
for k, dt in enumerate([8.2, 9.3, 10.4, 11.5, 12.6]):
    place(acc, fade(tone(760 - 40 * k, 0.18, 0.05)), dt, 0.13)
# S4 — war rumble, tanker horn, brent rise + $100 ding
rum = band(noise(int(9.0 * SR), 103), 40, 180) * (0.6 + 0.4 * np.sin(2 * np.pi * 0.21 * np.arange(int(9.0 * SR)) / SR))
place(acc, fade(rum, 40), 73.9, 0.16)
for th in (76.6, 80.8):
    place(acc, fade(tone(118, 0.9, 0.45) + 0.4 * tone(176, 0.9, 0.40)), th, 0.075)
place(acc, fade(sweep(300, 900, 2.2, 'lin') * env_exp(int(2.2 * SR), 1.4, 0.5)), 81.2, 0.085)
place(acc, fade(bell(1320, 0.5, 0.16)), 83.4, 0.11)
# S5 — four route cards swoosh in, festive chip lands
for k in range(4):
    t0 = T['start'][4] + 1.2 + k * 2.0
    place(acc, fade(band(noise(int(0.3 * SR), 121 + k), 500, 4800) * env_exp(int(0.3 * SR), 0.09, 0.006)), t0, 0.12)
place(acc, fade(bell(660, 0.9, 0.30) + 0.4 * bell(990, 0.9, 0.32)), T['start'][4] + 12.4, 0.13)
# S6 — four honesty cards: UI ticks, the toggle click, a cooling sweep
for k in range(4):
    t0 = T['start'][5] + 1.4 + k * 7.6
    place(acc, fade(tone(1450, 0.09, 0.02)), t0, 0.11)
_n = int(0.04 * SR)
place(acc, fade(tone(3000, 0.04, 0.008) + band(noise(_n, 131), 1500, 6000) * env_exp(_n, 0.02, 0.002)), T['start'][5] + 7.6 + 0.9, 0.09)
place(acc, fade(sweep(320, 120, 0.55, 'lin') * env_exp(int(0.55 * SR), 0.28, 0.01)), T['start'][5] + 15.2, 0.10)
# S7 — question motif, then the Like/Subscribe sparkle
place(acc, fade(bell(440, 0.45, 0.22)), T['start'][6] + 1.3, 0.10)
place(acc, fade(bell(660, 0.55, 0.28)), T['start'][6] + 1.9, 0.085)
place(acc, fade(sum(bell(f * 2, 0.5, 0.14) for f in (880, 1108, 1320)) / 3), T['start'][6] + 2.35, 0.10)
sfx = sfx + acc

# ------------------------------------------------------- 5 · duck + mix ------
def speech_duck(sig, max_reduce, atk=0.09, rel=0.30, thr=0.012):
    """envelope-follower duck — smooth, computed on a 100 Hz control signal"""
    c = 100
    env = np.abs(voc[::int(SR / c)])
    e = np.zeros_like(env)
    a = 1 - np.exp(-1.0 / (atk * c))
    r = 1 - np.exp(-1.0 / (rel * c))
    v = 0.0
    for i, x in enumerate(env):
        v = v + a * (x - v) if x > v else v + r * (x - v)
        e[i] = v
    e = np.clip(e / thr, 0, 1) ** 0.85
    g = np.interp(np.arange(len(sig)) / SR, np.arange(len(e)) / c, e, right=0.0)
    return sig * (1.0 - max_reduce * g)

bed_d = speech_duck(bed, 0.75)
sfx_d = speech_duck(sfx, 0.55)
mix = voc + bed_d + sfx_d
mix = np.tanh(mix * 1.02) * 0.995                       # gentle glue, no clipping
mix += 0.0002 * rng.normal(0, 1, N)                     # dither
mix = fade(mix, 350)
mix *= (10 ** (-2.0 / 20)) / max(np.abs(mix).max(), 1e-9)
print(f'[mix] speech {np.sqrt((voc**2).mean()):.4f} rms  bed {np.sqrt((bed_d**2).mean()):.4f}  '
      f'sfx {np.sqrt((sfx_d**2).mean()):.4f}  peak {np.abs(mix).max():.4f}')

st = np.stack([mix, mix], axis=1)
with wave.open('audio/master.wav', 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((np.clip(st, -1, 1) * 32767).astype('<i2').tobytes())
print(f'[write] audio/master.wav  {os.path.getsize("audio/master.wav")/1e6:.1f} MB  {N/SR:.2f}s')

# ------------------------------------------------- 6 · two-pass loudnorm -----
p1 = subprocess.run(['ffmpeg', '-nostats', '-i', 'audio/master.wav',
                     '-af', 'loudnorm=I=-14:TP=-1.5:LRA=6:print_format=json', '-f', 'null', '-'],
                    capture_output=True, text=True)
blob = p1.stderr[p1.stderr.rfind('{'):p1.stderr.rfind('}') + 1]
m = json.loads(blob)
flt = ('loudnorm=I=-14:TP=-1.5:LRA=6:'
       f'measured_I={m["input_i"]}:measured_LRA={m["input_lra"]}:measured_TP={m["input_tp"]}:'
       f'measured_thresh={m["input_thresh"]}:offset={m["target_offset"]}:linear=true')
p2 = subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', 'audio/master.wav', '-af', flt,
                     'audio/master_loud.wav'], capture_output=True, text=True)
if p2.returncode:
    sys.exit('[FAIL] loudnorm pass 2: ' + p2.stderr[-400:])
print(f'[loudnorm] in {m["input_i"]} LUFS / TP {m["input_tp"]} -> audio/master_loud.wav')
print(subprocess.run(['ffmpeg', '-nostats', '-i', 'audio/master_loud.wav', '-filter:a',
                      'ebur128=peak=true', '-f', 'null', '-'],
                     capture_output=True, text=True).stderr.strip().splitlines()[-6:])
print('[ok] master ready — render with --audio audio/master_loud.wav')
