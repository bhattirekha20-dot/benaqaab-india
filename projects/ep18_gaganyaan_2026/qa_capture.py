import os
import time
from playwright.sync_api import sync_playwright

def qa_test():
    comp_url = 'file:///' + os.path.abspath('projects/ep18_gaganyaan_2026/comp.html').replace('\\', '/')
    print(f'Loading comp: {comp_url}')
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={'width': 1920, 'height': 1080})
        
        errors = []
        page.on('console', lambda msg: errors.append(f'[{msg.type}] {msg.text}') if msg.type in ['error', 'warn'] else None)
        page.on('pageerror', lambda exc: errors.append(f'[PAGE ERROR] {exc}'))
        
        page.goto(comp_url)
        page.wait_for_timeout(2000) # Wait for images to load
        
        # Test timestamps to capture
        test_points = [
            (8.5, 'qa_beat_02_lively_highlighter_pib.png'),
            (14.5, 'qa_beat_03_burning_question_01.png'),
            (27.8, 'qa_beat_05_cta_like_state.png'),
            (28.8, 'qa_beat_05_cta_subscribed_state.png'),
            (45.0, 'qa_beat_08_geopolitical_stakes.png'),
            (149.0, 'qa_beat_25_abort_stamp.png')
        ]
        
        for t, filename in test_points:
            page.evaluate(f'window.seek({t})')
            page.wait_for_timeout(300)
            
            # Capture canvas
            canvas = page.locator('#viewCanvas')
            canvas.screenshot(path=os.path.join('projects/ep18_gaganyaan_2026', filename))
            print(f'Captured {filename} at t={t}s')
            
        print('Console errors/warnings encountered:', errors)
        browser.close()

if __name__ == '__main__':
    qa_test()
