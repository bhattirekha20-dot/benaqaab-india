import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    os.makedirs('projects/ep19_gdp_growth_reality/previews', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=['--no-sandbox', '--enable-gpu-rasterization']
        )
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        await page.goto('http://localhost:8765/projects/test_standalone_vector_map.html', wait_until='networkidle')
        await page.wait_for_timeout(500)
        await page.evaluate('window.seek(4.0);')
        await page.wait_for_timeout(300)
        canvas = page.locator('#stage')
        out_path = 'projects/ep19_gdp_growth_reality/previews/standalone_vector_map_geocarto_test.png'
        await canvas.screenshot(path=out_path)
        print(f'Captured: {out_path}')
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
