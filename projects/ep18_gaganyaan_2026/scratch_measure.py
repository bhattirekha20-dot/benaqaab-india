from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1360, 'height': 880})
    with open('projects/ep18_gaganyaan_2026/render_pib_gazette.py', 'r', encoding='utf-8') as f:
        code = f.read()
    start = code.find('doc_html = """') + len('doc_html = """')
    end = code.find('"""', start)
    html = code[start:end]
    page.set_content(html)
    
    title_box = page.locator('.title').bounding_box()
    hl_box = page.locator('.highlight-box').bounding_box()
    points = page.locator('.key-points li')
    pt_boxes = [points.nth(i).bounding_box() for i in range(points.count())]
    
    res = {
        'title': title_box,
        'highlight_box': hl_box,
        'points': pt_boxes
    }
    print(json.dumps(res, indent=2))
    browser.close()
