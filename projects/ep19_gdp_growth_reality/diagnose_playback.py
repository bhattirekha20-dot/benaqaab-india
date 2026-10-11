import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        console_logs = []
        page.on('console', lambda msg: console_logs.append(f'[{msg.type}] {msg.text}'))
        page.on('pageerror', lambda err: console_logs.append(f'[PAGE_ERROR] {err}'))

        print('Navigating to comp.html...')
        await page.goto('http://localhost:8765/projects/ep19_gdp_growth_reality/comp.html')
        await page.wait_for_timeout(1000)

        # Click play button
        print('Clicking play button...')
        await page.click('#btn-play')

        # Monitor currentTime over 3 seconds
        times = []
        for i in range(10):
            await page.wait_for_timeout(300)
            t = await page.evaluate('currentTime')
            audio_t = await page.evaluate('masterAudio.currentTime')
            audio_paused = await page.evaluate('masterAudio.paused')
            audio_ready = await page.evaluate('masterAudio.readyState')
            times.append((t, audio_t, audio_paused, audio_ready))

        print('Observed times (currentTime, audio.currentTime, audio.paused, audio.readyState):')
        for idx, (t, at, ap, ar) in enumerate(times):
            print(f'  Sample {idx}: canvas_t={t:.3f}s, audio_t={at:.3f}s, audio_paused={ap}, readyState={ar}')

        print('\nConsole logs:')
        for l in console_logs:
            print(' ', l)

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
