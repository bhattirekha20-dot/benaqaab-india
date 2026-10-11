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

TIMESTAMPS_TO_CHECK = [
    (2.5, "qa_01_hook_roadmap.png"),
    (62.0, "qa_02_cta_subscribe_like.png"),
    (73.0, "qa_03_diagram_gdp_gva_wedge.png"),
    (130.0, "qa_04_worldbank_per_capita_loupe.png"),
    (160.0, "qa_05_diagram_per_capita_comparison.png"),
    (205.0, "qa_06_diagram_k_shaped_divergence.png"),
    (345.0, "qa_07_diagram_household_debt_flow.png"),
    (385.0, "qa_08_diagram_missing_factory_gap.png"),
    (512.0, "qa_09_diagram_demographic_clock_2045.png"),
    (550.0, "qa_10_diagram_four_pillars_blueprint.png"),
    (602.0, "qa_11_closing_verdict_stamp.png")
]

async def run_qa():
    print(f"🔍 Running Playwright Browser QA on: {URL}")
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

        for t, fname in TIMESTAMPS_TO_CHECK:
            print(f"📸 Seeking to t={t}s...")
            await page.evaluate(f"window.seek({t})")
            await page.wait_for_timeout(500)
            
            # Take screenshot of the pure canvas
            canvas = page.locator("#stage")
            out_path = PREVIEWS_DIR / fname
            await canvas.screenshot(path=str(out_path))
            print(f"✅ Captured QA Frame: {fname}")

        await browser.close()
    print("🎯 QA frame captures completed!")

if __name__ == "__main__":
    asyncio.run(run_qa())
