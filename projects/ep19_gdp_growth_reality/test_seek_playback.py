import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        errors = []
        page.on('pageerror', lambda err: errors.append(str(err)))

        await page.goto('http://localhost:8765/projects/ep19_gdp_growth_reality/comp.html')
        await page.wait_for_timeout(500)

        checkpoints = [0, 70.0, 150.0, 200.0, 350.0, 510.0, 550.0]
        for cp in checkpoints:
            print(f'Testing seek to {cp}s and playing for 1s...')
            await page.evaluate(f'window.seek({cp});')
            await page.wait_for_timeout(100)
            await page.evaluate('if (!isPlaying) togglePlay();')
            await page.wait_for_timeout(1000)
            t_now = await page.evaluate('currentTime')
            audio_now = await page.evaluate('masterAudio.currentTime')
            print(f'  -> Advanced to: canvas={t_now:.2f}s, audio={audio_now:.2f}s')

        print('Errors encountered:', errors)
        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
