#!/usr/bin/env python3
"""
hrender.py — render a seekable HTML composition to MP4 in real Chromium, with
adaptive motion blur and safe frame reuse (viz/motion.py). House renderer since
2026-09-30; the Pillow pipeline stays as the fallback when no browser is available.

Composition contract (see viz/motion.js):
  window.seek(t)     REQUIRED  draw the frame at t seconds. Pure function of t. May be async.
  window.ready       REQUIRED  true once fonts/images are loaded.
  window.DURATION    REQUIRED  seconds.
  window.FPS / WIDTH / HEIGHT  optional (defaults 30 / 1080 / 1920).
  window.speed(t)    optional  fastest on-screen speed in px/s  -> adaptive motion blur
  window.state(t)    optional  signature of everything visible -> reuse of identical frames

Usage:
  python3 viz/hrender.py comp.html out.mp4 [--audio vo.wav] [--crf 18] [--start S --end E]
  python3 viz/hrender.py comp.html outdir --stills 0.4,1.2,2.0     # PNG stills + contact sheet
  python3 viz/hrender.py comp.html outdir --beats 0.5               # one still per beat
Always launch full renders with start_process, never inside a bash call (MEMORY §14).
"""
import argparse, base64, io, json, os, subprocess, sys, time
import numpy as np
from PIL import Image

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import motion as M  # noqa: E402

CHROME = ['/usr/lib/chromium/chromium-headless-shell', '/usr/lib/chromium/chromium',
          '/usr/bin/chromium-headless-shell', '/usr/bin/chromium']
ARGS = ['--no-sandbox', '--disable-gpu', '--hide-scrollbars', '--force-color-profile=srgb',
        '--disable-lcd-text', '--font-render-hinting=none', '--disable-dev-shm-usage',
        '--allow-file-access-from-files', '--mute-audio', '--disable-background-timer-throttling',
        '--disable-renderer-backgrounding', '--disable-backgrounding-occluded-windows']


class Comp:
    """One Chromium page holding the composition."""
    def __init__(self, html, jpeg=False):
        from playwright.sync_api import sync_playwright
        self.pw = sync_playwright().start()
        exe = next((p for p in CHROME if os.path.exists(p)), None)
        self.browser = self.pw.chromium.launch(executable_path=exe, args=ARGS) if exe \
            else self.pw.chromium.launch(args=ARGS)
        self.page = self.browser.new_page(viewport={'width': 1080, 'height': 1920}, device_scale_factor=1)
        self.errors = []
        self.page.on('pageerror', lambda e: self.errors.append(str(e)))
        self.page.goto('file://' + os.path.abspath(html))
        self.page.wait_for_function('window.ready === true', timeout=120000)
        # will-change / compositor hints make Chromium keep stale rasters when an ancestor
        # scales (camera zoom) -> the same t renders differently depending on the previous
        # frame. Measured 2026-09-30: 14,699 px differed. Strip them for deterministic output.
        self.page.add_style_tag(content='*{will-change:auto !important}')
        meta = self.page.evaluate("""() => ({d: window.DURATION, fps: window.FPS || 30,
            w: window.WIDTH || 1080, h: window.HEIGHT || 1920,
            sp: typeof window.speed === 'function', st: typeof window.state === 'function'})""")
        if not meta['d']:
            raise SystemExit('composition has no window.DURATION')
        if (meta['w'], meta['h']) != (1080, 1920):
            self.page.set_viewport_size({'width': meta['w'], 'height': meta['h']})
        self.duration, self.fps, self.W, self.H = float(meta['d']), float(meta['fps']), meta['w'], meta['h']
        self.has_speed, self.has_state = meta['sp'], meta['st']
        self.cdp = self.page.context.new_cdp_session(self.page)
        self.shot = ({'format': 'jpeg', 'quality': 95} if jpeg else {'format': 'png', 'optimizeForSpeed': True})
        self.shot['captureBeyondViewport'] = False
        self.captures = 0

    def determinism_check(self):
        """Same t must give the same pixels whatever was rendered before it."""
        d, t1 = self.duration, self.duration * 0.37
        a = self.capture(t1); self.capture(d * 0.93); self.capture(0.0); b = self.capture(t1)
        return bool(np.array_equal(a, b))

    def capture(self, t):
        self.page.evaluate('t => window.seek(t)', float(t))
        data = base64.b64decode(self.cdp.send('Page.captureScreenshot', self.shot)['data'])
        self.captures += 1
        return np.asarray(Image.open(io.BytesIO(data)).convert('RGB'))

    def speed(self, t):
        return float(self.page.evaluate('t => window.speed(t)', float(t)) or 0.0)

    def state(self, t):
        return self.page.evaluate('t => JSON.stringify(window.state(t))', float(t))

    def close(self):
        try: self.browser.close()
        finally: self.pw.stop()


def frame(comp, t, max_samples=12, fixed_samples=None):
    """Blurred frame at t. Returns (PIL image, samples used)."""
    sp = comp.speed(t) if comp.has_speed and not fixed_samples else None
    n = fixed_samples or (M.samples_for_speed(sp, comp.fps, max_samples=max_samples) if sp is not None else 1)
    img = M.render_blurred(comp.capture, t, comp.fps,
                           speed_fn=(lambda _t: sp) if sp is not None else None,
                           moving_fn=None if sp is not None else (lambda _t: n > 1),
                           samples=n, max_samples=max_samples,
                           state_fn=comp.state if comp.has_state else None)
    return img, n


def open_writer(out, W, H, fps, crf=18, audio=None, preset='medium', dur=None, ss=0.0):
    # Memory-safe on a 2 GB box: x264 threads/lookahead capped; audio padded only up to the video length
    # (apad without whole_dur + -shortest makes ffmpeg queue endless padded audio while video trickles in -> OOM).
    cmd = ['ffmpeg', '-y', '-v', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24',
           '-s', f'{W}x{H}', '-r', f'{fps:g}', '-thread_queue_size', '4', '-i', '-']
    if audio:
        cmd += (['-ss', f'{ss:.3f}'] if ss else []) + ['-i', audio]
    cmd += ['-map', '0:v']
    if audio:
        cmd += ['-map', '1:a', '-c:a', 'aac', '-b:a', '192k', '-ar', '48000']
        if dur: cmd += ['-af', f'apad=whole_dur={dur:.3f}', '-t', f'{dur:.3f}']
    cmd += ['-c:v', 'libx264', '-preset', preset, '-crf', str(crf), '-profile:v', 'high',
            '-threads', '2', '-x264-params', 'rc-lookahead=20:lookahead-threads=1',
            '-vf', 'scale=out_color_matrix=bt709:out_range=tv,format=yuv420p',
            '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709',
            '-max_muxing_queue_size', '256', '-movflags', '+faststart', out]
    log = open(out + '.ffmpeg.log', 'w')
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=log); pr.logpath = log.name
    return pr


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('html'); ap.add_argument('out')
    ap.add_argument('--audio'); ap.add_argument('--crf', type=int, default=18)
    ap.add_argument('--preset', default='medium')
    ap.add_argument('--start', type=float, default=0.0); ap.add_argument('--end', type=float)
    ap.add_argument('--max-samples', type=int, default=12)
    ap.add_argument('--samples', type=int, help='fixed subframes per frame (ignores window.speed)')
    ap.add_argument('--jpeg', action='store_true', help='faster capture; avoid on dark gradients (banding)')
    ap.add_argument('--stills', help='comma-separated times -> PNG stills + contact sheet')
    ap.add_argument('--beats', type=float, help='one still every N seconds -> contact sheet')
    ap.add_argument('--check', action='store_true', help='run motion_report on the result')
    a = ap.parse_args()

    comp = Comp(a.html, jpeg=a.jpeg)
    fps, W, H = comp.fps, comp.W, comp.H
    if not comp.determinism_check():
        print('[WARN] composition is NOT deterministic: the same t renders differently depending on the '
              'previous frame. Look for Math.random/Date/state carried between seek() calls.', flush=True)
    else:
        print('[ok] determinism check passed', flush=True)
    try:
        if a.stills or a.beats:
            os.makedirs(a.out, exist_ok=True)
            times = [float(x) for x in a.stills.split(',')] if a.stills else \
                [round(k * a.beats, 3) for k in range(int(comp.duration / a.beats) + 1)]
            ims = []
            for t in times:
                im, n = frame(comp, min(t, comp.duration - 1 / fps), a.max_samples, a.samples)
                im.save(os.path.join(a.out, f'still_{t:07.3f}.png')); ims.append(im)
            M.contact_sheet(ims, [f'{t:.2f}s' for t in times], cols=min(6, len(ims))).save(
                os.path.join(a.out, 'contact.jpg'), quality=90)
            print(f'[stills] {len(ims)} -> {a.out}/contact.jpg')
        else:
            end = min(a.end or comp.duration, comp.duration)
            i0, i1 = int(round(a.start * fps)), int(round(end * fps))
            w = open_writer(a.out, W, H, fps, a.crf, a.audio, a.preset, dur=(i1 - i0) / fps, ss=i0 / fps)
            t0, used = time.time(), []
            for i in range(i0, i1):
                im, n = frame(comp, i / fps, a.max_samples, a.samples)
                used.append(n)
                try:
                    w.stdin.write(np.asarray(im.convert('RGB')).tobytes())
                except BrokenPipeError:
                    tail = open(w.logpath).read()[-800:]
                    raise SystemExit(f'[FAIL] ffmpeg died at frame {i} (exit {w.poll()}). If exit is -9 it was the OOM killer '
                                     f'(check: dmesg | grep -i oom). Resume with --start {i / fps:.3f} into a new file and concat.\n{tail}')
                done = i - i0 + 1
                if done % 30 == 0 or i == i1 - 1:
                    el = time.time() - t0
                    print(f'[render] {done}/{i1 - i0} frames  {el:5.0f}s  eta {el / done * (i1 - i0 - done):4.0f}s  '
                          f'captures {comp.captures}  avg samples {np.mean(used):.2f}', flush=True)
            w.stdin.close(); w.wait()
            if w.returncode:
                raise SystemExit(f'ffmpeg failed ({w.returncode}): ' + open(w.logpath).read()[-800:])
            os.remove(w.logpath)
            print(f'[done] {a.out}  {os.path.getsize(a.out) / 1e6:.1f} MB  {i1 - i0} frames  '
                  f'{comp.captures} captures  blurred frames {sum(n > 1 for n in used)}')
            if a.check:
                print('[check]', json.dumps(M.motion_report(a.out)))
        if comp.errors:
            print('[page errors]', comp.errors[:5])
    finally:
        comp.close()


if __name__ == '__main__':
    main()
