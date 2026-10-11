import asyncio
import os
from playwright.async_api import async_playwright

async def main():
    os.makedirs('projects/ep19_gdp_growth_reality/previews', exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        errors = []
        page.on('pageerror', lambda err: errors.append(str(err)))

        await page.goto('http://localhost:8765/projects/ep19_gdp_growth_reality/comp.html')
        await page.wait_for_timeout(1000)

        # Activate clean render mode so no UI chrome is present
        await page.evaluate("document.body.classList.add('render-mode');")
        await page.wait_for_timeout(200)

        test_points = [
            (10.0, 'previews/test_beat2_top_left.png', 'Beat 2: Kitchen Table Inflation (top-left)'),
            (48.6, 'previews/progressive_beat7_phase1_entry.png', 'Beat 7 Phase 1: Card Entry & Tag Wipe'),
            (49.3, 'previews/progressive_beat7_phase2_pod1.png', 'Beat 7 Phase 2: Title & Pod 1 MoSPI/RBI'),
            (50.2, 'previews/progressive_beat7_phase3_pod2_stream.png', 'Beat 7 Phase 3: Pod 2 World Bank & Data Packet'),
            (51.5, 'previews/progressive_beat7_phase4_full_verdict.png', 'Beat 7 Phase 4: Divider & Sach/Saboot Verdict'),
            (90.0, 'previews/test_beat10_top_left.png', 'Beat 10: Slum & Luxury Split (top-left)'),
            (118.0, 'previews/test_beat12_top_right.png', 'Beat 12: Train Doorway Commuter (top-right exception)'),
            (230.0, 'previews/test_beat22_top_left.png', 'Beat 22: Farmer Tractor Loan (top-left)'),
            (305.0, 'previews/test_beat31_top_left.png', 'Beat 31: Broken Piggy Bank (top-left)'),
        ]

        for t, out_path, desc in test_points:
            await page.evaluate(f'window.seek({t});')
            await page.wait_for_timeout(250)
            canvas = await page.query_selector('canvas#stage')
            if canvas:
                full_path = os.path.join('projects/ep19_gdp_growth_reality', out_path)
                await canvas.screenshot(path=full_path)
                print(f"Captured: {desc} -> {full_path}")

        print("Errors encountered:", errors)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
