from playwright.sync_api import sync_playwright

doc_html = """<!DOCTYPE html>
<html>
<head>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { background: #07090e; font-family: 'Inter', -apple-system, sans-serif; display: flex; justify-content: center; align-items: center; min-height: 100vh; padding: 20px; }
    .doc-page { width: 1240px; background: #ffffff; color: #0f172a; border-radius: 12px; box-shadow: 0 30px 80px rgba(0,0,0,0.85); padding: 50px 65px; }
    .header-bar { display: flex; justify-content: space-between; align-items: center; border-bottom: 2px solid #e2e8f0; padding-bottom: 20px; }
    .pib-badge { text-align: right; font-family: monospace; font-size: 14px; font-weight: 700; color: #475569; }
    .title { font-size: 27px; font-weight: 900; line-height: 1.35; color: #090d16; margin-top: 26px; border-left: 6px solid #2563eb; padding-left: 18px; }
    .meta { font-size: 14px; color: #64748b; margin: 14px 0 24px 0; font-weight: 600; }
    .highlight-box { background: #fef9c3; border: 2px solid #facc15; border-radius: 8px; padding: 20px 24px; font-size: 19px; font-weight: 800; color: #854d0e; line-height: 1.5; margin-bottom: 24px; }
    .content-body { font-size: 16px; line-height: 1.7; color: #1e293b; }
    .key-points { margin-top: 18px; padding-left: 24px; font-size: 16px; line-height: 1.8; }
    .key-points li strong { color: #0f172a; }
  </style>
</head>
<body>
  <div class="doc-page">
    <div class="header-bar">
      <div>
        <h2 style="font-size:22px; color:#1e3a8a; font-weight:900;">PRESS INFORMATION BUREAU</h2>
        <p style="font-size:13px; color:#64748b; font-weight:700; margin-top:3px;">GOVERNMENT OF INDIA · CABINET SECRETARIAT</p>
      </div>
      <div class="pib-badge">
        <div>PIB PRID: 2055978</div>
        <div>NEW DELHI · 18 SEP 2024</div>
      </div>
    </div>
    
    <div class="title">
      Cabinet approves expansion of the Gaganyaan Programme: Bharatiya Antariksh Station (BAS) and Revised Funding of ₹20,193 Crore
    </div>
    
    <div class="meta">
      Posted On: 18 SEP 2024 3:10 PM by PIB Delhi | Dept of Space / Prime Minister's Office
    </div>

    <div class="highlight-box">
      "The Union Cabinet, chaired by Prime Minister Shri Narendra Modi, has approved the revised Gaganyaan Programme with an enhanced total allocation of ₹20,193 Crore, an additional ₹11,170 Crore to execute eight missions by Dec 2028 and launch BAS-01 module by 2028."
    </div>

    <div class="content-body">
      The Cabinet Committee on Economic Affairs (CCEA) approved significant expansion in the scope of the Human Spaceflight Programme to establish Bharatiya Antariksh Station:
      <ul class="key-points">
        <li><strong>Revised Budget Outlay:</strong> ₹20,193 Crore (Enhanced from baseline ₹9,023 Crore with net additional ₹11,170 Crore).</li>
        <li><strong>Mission Roadmap:</strong> Eight precursor and flight missions approved by December 2028.</li>
        <li><strong>BAS-01 Space Station Module:</strong> First module of Bharatiya Antariksh Station to be launched and operational by 2028.</li>
        <li><strong>Human Moon Landing Target:</strong> Establishes foundational operational capability towards crewed lunar touchdown by 2040.</li>
      </ul>
    </div>
  </div>
</body>
</html>
"""

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={'width': 1360, 'height': 880})
    page.set_content(doc_html)
    page.screenshot(path='projects/ep18_gaganyaan_2026/assets/official_sources/src_01_pib_cabinet_approval_gazette.png')
    browser.close()

print('Rendered official PIB Gazette document image successfully.')
