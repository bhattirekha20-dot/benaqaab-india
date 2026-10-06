#!/usr/bin/env python3
"""render.py — frame renderer for film.html (run on YOUR PC).
Reads timeline.json, seeks film.html?render=1 to every frame, saves PNG frames.
Resumable: already-saved frames are skipped.
Usage:  python3 render.py [out_dir]        (default: frames)
Then:   bash render.sh                     (frames -> FINAL film + audio mux)
"""
import json, os, sys, math, time

PROJ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(PROJ, "frames")

def main():
    from playwright.sync_api import sync_playwright
    with open(os.path.join(PROJ, "timeline.json")) as f:
        TL = json.load(f)
    total, fps = TL["total"], TL["fps"]
    nframes = int(math.ceil(total * fps))
    os.makedirs(OUT, exist_ok=True)
    t_start = time.time()
    print("frames to render: %d  (total %.1fs @ %dfps)" % (nframes, total, fps))
    with sync_playwright() as pw:
        b = pw.chromium.launch(args=["--force-device-scale-factor=1"])
        pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=1)
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto("file://" + os.path.join(PROJ, "film.html") + "?render=1")
        pg.wait_for_timeout(1500)
        info = pg.evaluate("window.__info()")
        print("page info:", info)
        done = 0
        for i in range(nframes):
            path = os.path.join(OUT, "f_%06d.png" % i)
            if os.path.exists(path) and os.path.getsize(path) > 1000:
                done += 1
                continue
            pg.evaluate("window.__seek(%f)" % (i / fps))
            pg.screenshot(path=path, clip={"x": 0, "y": 0, "width": 1920, "height": 1080})
            done += 1
            if done % 150 == 0:
                el = time.time() - t_start
                rate = done / el if el else 0
                eta = (nframes - done) / rate if rate else 0
                print("  %d/%d  (%.1f fps, ETA %.0fs)" % (done, nframes, rate, eta), flush=True)
        b.close()
        if errs:
            print("PAGE ERRORS:", errs[:5])
    print("DONE -> %s" % OUT)

if __name__ == "__main__":
    main()
