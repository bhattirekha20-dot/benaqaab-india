import os
import sys
import time
from playwright.sync_api import sync_playwright

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_PATH = os.path.join(PROJECT_DIR, "comp.html")
PREVIEW_DIR = os.path.join(PROJECT_DIR, "previews")
os.makedirs(PREVIEW_DIR, exist_ok=True)

TIMESTAMPS = [
    (1.0, "qa_01_beat01_metro_gate_hook.jpg"),
    (6.8, "qa_02_beat04_flight_arrest.jpg"),
    (11.2, "qa_03_beat06_cjp_emblem.jpg"),
    (17.3, "qa_04_beat09_yellow_highlighter.jpg"),
    (26.4, "qa_05_beat14_cec_loupe.jpg"),
    (30.8, "qa_06_beat17_odometer_3m.jpg"),
    (35.2, "qa_07_beat21_empty_railway.jpg"),
    (40.3, "qa_08_beat26_sc_hammer_quote.jpg"),
    (41.7, "qa_09_beat27_verdict_stamp.jpg"),
    (46.0, "qa_10_beat30_subscribe_cta.jpg")
]

def capture():
    print("📸 Launching headless Chromium to capture QA frames...")
    with sync_playwright() as p:
        browser = p.chromium.launch(args=[
            '--no-sandbox',
            '--disable-gpu',
            '--hide-scrollbars',
            '--force-color-profile=srgb',
            '--allow-file-access-from-files'
        ])
        page = browser.new_page(viewport={'width': 1080, 'height': 1920}, device_scale_factor=1)
        url = 'file:///' + HTML_PATH.replace('\\', '/') + '?render=1'
        print(f"🌐 Loading: {url}")
        page.goto(url)
        time.sleep(2.0)
        
        for t_sec, fname in TIMESTAMPS:
            page.evaluate(f'window.seek({t_sec})')
            time.sleep(0.3)
            out_file = os.path.join(PREVIEW_DIR, fname)
            canvas_el = page.locator('#videoCanvas')
            canvas_el.screenshot(path=out_file, quality=95, type='jpeg')
            print(f"✅ Captured QA Frame: {fname} at t={t_sec}s")
            
        browser.close()
    print("🎉 All QA snapshots captured successfully!")

if __name__ == '__main__':
    capture()
