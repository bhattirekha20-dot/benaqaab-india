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
    (0.8, "qa_01_beat01_debit_alert.jpg"),
    (2.4, "qa_02_beat02_rupay_card.jpg"),
    (7.5, "qa_03_beat05_silicone_ungli.jpg"),
    (12.0, "qa_04_beat08_rural_bharat.jpg"),
    (15.2, "qa_05_beat10_jamabandi_portal.jpg"),
    (18.2, "qa_06_beat12_loupe_thumbprint.jpg"),
    (22.8, "qa_07_beat15_butter_paper.jpg"),
    (24.5, "qa_08_beat16_poly_stamper.jpg"),
    (28.5, "qa_09_beat19_l0_scanner.jpg"),
    (31.8, "qa_10_beat21_odometer_10k.jpg"),
    (36.2, "qa_11_beat24_biometric_locked.jpg"),
    (41.2, "qa_12_beat27_error_330.jpg"),
    (43.2, "qa_13_beat28_helpline_1930.jpg"),
    (47.5, "qa_14_beat30_subscribe_cta.jpg")
]

def capture():
    print("📸 Launching headless Chromium to capture QA frames for SH-13...")
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
        time.sleep(2.5)
        
        for t_sec, fname in TIMESTAMPS:
            page.evaluate(f'window.seek({t_sec})')
            time.sleep(0.3)
            out_file = os.path.join(PREVIEW_DIR, fname)
            canvas_el = page.locator('#videoCanvas')
            canvas_el.screenshot(path=out_file, quality=95, type='jpeg')
            print(f"✅ Captured QA Frame: {fname} at t={t_sec}s")
            
        browser.close()
    print("🎉 All 10 QA snapshots captured successfully!")

if __name__ == '__main__':
    capture()
