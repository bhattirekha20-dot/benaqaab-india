import sys, json, glob, os
from playwright.sync_api import sync_playwright
times = [float(x) for x in sys.argv[1:]] or [6, 45, 95, 145, 205, 265, 335, 405, 465]
os.makedirs("qa", exist_ok=True)
with sync_playwright() as pw:
    b = pw.chromium.launch()
    pg = b.new_page(viewport={"width":1920,"height":1080})
    errs=[]
    pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto("file://"+os.path.abspath("film.html")+"?render=1")
    pg.wait_for_timeout(1200)
    print("info:", pg.evaluate("window.__info()"))
    for k,t in enumerate(times):
        pg.evaluate("window.__seek(%f)" % t)
        pg.wait_for_timeout(120)
        pg.screenshot(path="qa/still_%02d_t%04d.png" % (k, int(t)))
    b.close()
    print("errors:", [e for e in errs if "FILE_NOT" not in e][:8] or "NONE(js)")
    print("stills:", len(glob.glob("qa/still_*.png")))
