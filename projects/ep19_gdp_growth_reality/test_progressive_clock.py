import asyncio
import sys
from pathlib import Path
from playwright.async_api import async_playwright

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR = Path(__file__).parent
PREVIEWS_DIR = DIR / "previews"
PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)

URL = "http://localhost:8765/projects/ep19_gdp_growth_reality/comp.html?render=1"

STAGES_TO_CAPTURE = [
    (501.5, "progressive_p1_headline_center.png"),
    (503.8, "progressive_p2_headline_top.png"),
    (506.5, "progressive_p3_left_card_entered.png"),
    (512.0, "progressive_p4_clock_drawing_live.png"),
    (516.5, "progressive_p5_right_card_entered.png"),
    (521.5, "progressive_p6_final_connected_dashboard.png")
]

async def run_test():
    print(f"🔍 Testing Progressive Infographic Motion on: {URL}")
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--enable-gpu-rasterization",
                "--ignore-gpu-blocklist",
                "--disable-web-security"
            ]
        )
        page = await browser.new_page(viewport={"width": 1920, "height": 1080})
        await page.goto(URL, wait_until="networkidle")
        await page.wait_for_timeout(1000)

        for t, fname in STAGES_TO_CAPTURE:
            print(f"📸 Seeking to t={t}s...")
            await page.evaluate(f"window.seek({t})")
            await page.wait_for_timeout(500)
            
            canvas = page.locator("#stage")
            out_path = PREVIEWS_DIR / fname
            await canvas.screenshot(path=str(out_path))
            print(f"✅ Captured Progressive Stage: {fname}")

        await browser.close()
    print("🎯 All progressive stages captured successfully!")

if __name__ == "__main__":
    asyncio.run(run_test())
