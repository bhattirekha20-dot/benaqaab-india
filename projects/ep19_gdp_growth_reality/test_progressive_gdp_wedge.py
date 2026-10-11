import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    os.makedirs('projects/ep19_gdp_growth_reality/previews', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                '--enable-gpu-rasterization',
                '--ignore-gpu-blocklist',
                '--no-sandbox'
            ]
        )
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        # comp.html via local range daemon
        await page.goto('http://localhost:8765/projects/ep19_gdp_growth_reality/comp.html?render=1', wait_until='networkidle')
        await page.wait_for_timeout(1000)

        # Timestamps for the 6 progressive phases of Diagram 1 (64.29s - 83.45s)
        stages = [
            (65.5, 'projects/ep19_gdp_growth_reality/previews/progressive_gdp_p1_headline_center.png'),
            (67.5, 'projects/ep19_gdp_growth_reality/previews/progressive_gdp_p2_headline_top.png'),
            (70.5, 'projects/ep19_gdp_growth_reality/previews/progressive_gdp_p3_gva_entered.png'),
            (74.5, 'projects/ep19_gdp_growth_reality/previews/progressive_gdp_p4_wedge_entered.png'),
            (78.0, 'projects/ep19_gdp_growth_reality/previews/progressive_gdp_p5_result_entered.png'),
            (81.5, 'projects/ep19_gdp_growth_reality/previews/progressive_gdp_p6_verdict_connected.png'),
        ]

        for t, out_path in stages:
            await page.evaluate(f'window.seek({t});')
            await page.wait_for_timeout(250)
            canvas = page.locator('#stage')
            await canvas.screenshot(path=out_path)
            print(f'Captured: {out_path} at t={t}s')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
