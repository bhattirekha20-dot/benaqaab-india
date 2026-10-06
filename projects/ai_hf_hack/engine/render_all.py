#!/usr/bin/env python3
"""render_all.py — FULL film renderer (segmented, resumable, size-bounded).

Pipeline per 60s segment:
  1) playwright seeks film.html?render=1 -> PNG frames in /home/user/out/frames
  2) x264 encodes segment -> /home/user/out/seg/seg_KK.ts  (VBV-capped)
  3) frames of that segment deleted (disk stays small)
Final: concat .ts (-c copy) + audio_master.mp4 mux -> AI_hacked_HuggingFace_FINAL.mp4

Sizes: .ts lives under /home/user/out (snapshot-excluded). Final mp4 must fit the
128 MB workspace cap => video VBV maxrate 850k + aac 96k => worst ~83 MB, typical
much lower (static dark editorial content).
"""
import json, math, os, shutil, subprocess, sys, time

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = "/home/user/out"
FR = os.path.join(WORK, "frames")
SEGDIR = os.path.join(WORK, "seg")
SEG_SEC = 60
FPS = 30
X264 = ["-c:v", "libx264", "-preset", "faster", "-crf", "25",
        "-maxrate", "850k", "-bufsize", "1700k", "-pix_fmt", "yuv420p",
        "-x264-params", "keyint=120:min-keyint=60"]


def sh(cmd, **kw):
    r = subprocess.run(cmd, **kw)
    if r.returncode != 0:
        raise SystemExit("cmd failed: %s" % " ".join(str(c) for c in cmd))


def main():
    from playwright.sync_api import sync_playwright
    with open(os.path.join(PROJ, "timeline.json")) as f:
        TL = json.load(f)
    total, fps = TL["total"], TL["fps"]
    assert fps == FPS
    nframes = int(math.ceil(total * fps))
    os.makedirs(FR, exist_ok=True)
    os.makedirs(SEGDIR, exist_ok=True)
    nseg = int(math.ceil(nframes / (SEG_SEC * fps)))
    print("total %.1fs -> %d frames, %d segments of %ds" % (total, nframes, nseg, SEG_SEC), flush=True)

    t_start = time.time()
    with sync_playwright() as pw:
        b = pw.chromium.launch(args=["--force-device-scale-factor=1"])
        pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto("file://" + os.path.join(PROJ, "film.html") + "?render=1")
        pg.wait_for_timeout(1500)
        info = pg.evaluate("window.__info()")
        print("page info:", info, flush=True)
        if info.get("missing"):
            print("WARNING missing audio:", info["missing"], flush=True)

        for k in range(nseg):
            ts = os.path.join(SEGDIR, "seg_%02d.ts" % k)
            if os.path.exists(ts) and os.path.getsize(ts) > 100_000:
                print("[seg %02d] already encoded, skip" % k, flush=True)
                continue
            f0 = k * SEG_SEC * fps
            f1 = min(nframes, f0 + SEG_SEC * fps) - 1
            nf = f1 - f0 + 1
            # --- render frames ---
            t0 = time.time()
            for i in range(f0, f1 + 1):
                path = os.path.join(FR, "f_%06d.png" % i)
                if os.path.exists(path) and os.path.getsize(path) > 1000:
                    continue
                pg.evaluate("window.__seek(%f)" % (i / fps))
                pg.screenshot(path=path, clip={"x": 0, "y": 0, "width": 1920, "height": 1080})
                if (i - f0) % 150 == 0:
                    el = time.time() - t0
                    done = i - f0 + 1
                    rate = done / el if el else 0
                    eta = (nf - done) / rate if rate else 0
                    print("[seg %02d] frame %d/%d  (%.2f f/s, ETA %.0fs)  global %.1f min" %
                          (k, done, nf, rate, eta, (time.time() - t_start) / 60), flush=True)
            if errs:
                print("PAGE ERRORS:", errs[:3], flush=True); errs.clear()
            # --- encode segment ---
            te = time.time()
            sh(["ffmpeg", "-y", "-framerate", str(fps), "-start_number", str(f0),
                "-i", os.path.join(FR, "f_%06d.png"), "-frames:v", str(nf),
                "-output_ts_offset", "%.3f" % (f0 / fps)] + X264 +
               [ts], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            sz = os.path.getsize(ts)
            print("[seg %02d] encoded %.1f MB in %.0fs" % (k, sz / 1e6, time.time() - te), flush=True)
            # --- drop frames of this segment ---
            for i in range(f0, f1 + 1):
                try: os.remove(os.path.join(FR, "f_%06d.png" % i))
                except FileNotFoundError: pass
        b.close()

    # --- concat + mux ---
    print("concat + mux...", flush=True)
    lst = os.path.join(SEGDIR, "list.txt")
    with open(lst, "w") as f:
        for k in range(nseg):
            f.write("file 'seg_%02d.ts'\n" % k)
    out = os.path.join(PROJ, "AI_hacked_HuggingFace_FINAL.mp4")
    sh(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", lst,
        "-i", os.path.join(PROJ, "audio_master.mp3"),
        "-map", "0:v", "-map", "1:a", "-c:v", "copy",
        "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", "-shortest", out],
       cwd=SEGDIR, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    dur = subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                   "-of", "csv=p=0", out]).decode().strip()
    print("DONE -> %s  (%.1f MB, duration %ss, elapsed %.1f h)" %
          (out, os.path.getsize(out) / 1e6, dur, (time.time() - t_start) / 3600), flush=True)


if __name__ == "__main__":
    main()
