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

HTML_PATH = os.path.abspath("projects/ep18_gaganyaan_short_promo/comp.html")
PREVIEW_DIR = "projects/ep18_gaganyaan_short_promo/previews_v3"
os.makedirs(PREVIEW_DIR, exist_ok=True)

TIMESTAMPS = [
    (1.5, "01_scene1_rocket_launch_hook.jpg"),
    (8.5, "02_scene1_budget_odometer.jpg"),
    (16.5, "03_scene2_myth_bust_galat.jpg"),
    (20.0, "04_scene2_space_station.jpg"),
    (26.0, "05_scene3_vyommitra_robot.jpg"),
    (37.0, "06_scene4_zero_human_risk.jpg"),
    (49.0, "07_scene5_live_premiere_cta.jpg"),
    (52.0, "08_scene5_subscribe_button.jpg")
]


def capture_previews():
    print("📸 Capturing 1080x1920 stills from comp.html...")
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
        print(f"Loading: {url}")
        page.goto(url)
        page.wait_for_function('window.ready === true', timeout=30000)
        time.sleep(1.0)
        
        for t_sec, fname in TIMESTAMPS:
            page.evaluate(f'window.seek({t_sec})')
            time.sleep(0.2)
            out_file = os.path.join(PREVIEW_DIR, fname)
            canvas_el = page.locator('#shortCanvas')
            canvas_el.screenshot(path=out_file, quality=95, type='jpeg')
            print(f"✅ Saved: {out_file} at t={t_sec}s")
            
        browser.close()

if __name__ == '__main__':
    capture_previews()
