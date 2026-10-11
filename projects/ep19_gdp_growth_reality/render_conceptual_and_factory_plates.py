import asyncio
import sys
import os
import time
import urllib.request
import urllib.parse
import json
from pathlib import Path
from PIL import Image
from playwright.async_api import async_playwright

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR = Path(__file__).parent
AI_DIR = DIR / "assets" / "ai_plates"
AI_DIR.mkdir(parents=True, exist_ok=True)

# 1. Download real photos for ai_12 (robot) and ai_15 (lab)
def fetch_and_save(file_title, dest_filename):
    try:
        url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'BenaqaabBot/4.0 (journalism)'})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode())
        pages = data.get('query', {}).get('pages', {})
        for pid, pinfo in pages.items():
            if 'imageinfo' in pinfo:
                img_url = pinfo['imageinfo'][0]['url']
                dest_path = AI_DIR / dest_filename
                temp_path = AI_DIR / f"temp_{dest_filename}"
                req2 = urllib.request.Request(img_url, headers={'User-Agent': 'BenaqaabBot/4.0 (journalism)'})
                with urllib.request.urlopen(req2, timeout=20) as resp2:
                    with open(temp_path, "wb") as f:
                        f.write(resp2.read())
                with Image.open(temp_path) as im:
                    im = im.convert("RGB")
                    target_w, target_h = 1920, 1080
                    src_w, src_h = im.size
                    src_ratio = src_w / src_h
                    target_ratio = 16 / 9
                    if src_ratio > target_ratio:
                        new_w = int(src_h * target_ratio)
                        left = (src_w - new_w) // 2
                        im = im.crop((left, 0, left + new_w, src_h))
                    else:
                        new_h = int(src_w / target_ratio)
                        top = (src_h - new_h) // 2
                        im = im.crop((0, top, src_w, top + new_h))
                    im = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
                    im.save(dest_path, "JPEG", quality=92)
                if temp_path.exists():
                    temp_path.unlink()
                print(f"✅ Created real plate: {dest_filename}")
                return True
    except Exception as e:
        print(f"Error fetching {dest_filename}: {e}")
    return False

# 2. Render conceptual 1080p cinematic plates using Playwright
CONCEPTUAL_PAGES = [
    {
        "filename": "ai_03_middle_class_kitchen_table_inflation.jpg",
        "html": """<!DOCTYPE html>
<html>
<head>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  width: 1920px; height: 1080px; overflow: hidden;
  background: #07090e;
  font-family: 'Inter', -apple-system, sans-serif;
  display: flex; align-items: center; justify-content: center;
  position: relative;
}
.bg-stage {
  position: absolute; top:0; left:0; width:100%; height:100%;
  background: radial-gradient(circle at 50% 40%, rgba(30, 41, 59, 0.4) 0%, rgba(7, 9, 14, 0.98) 80%);
}
.ledger-board {
  position: relative; z-index: 2;
  width: 1400px; height: 860px;
  background: #0f172a;
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  box-shadow: 0 35px 90px rgba(0,0,0,0.9), 0 0 40px rgba(239, 68, 68, 0.1);
  padding: 48px 56px;
  display: flex; flex-direction: column;
}
.header-row {
  display: flex; justify-content: space-between; align-items: flex-start;
  border-bottom: 2px solid rgba(255, 255, 255, 0.1);
  padding-bottom: 20px;
}
.main-title {
  font-size: 32px; font-weight: 900; color: #f8fafc; letter-spacing: 0.5px;
}
.sub-title {
  font-size: 16px; color: #94a3b8; font-weight: 600; margin-top: 6px;
}
.badge-alert {
  background: rgba(239, 68, 68, 0.15); border: 1px solid #ef4444; color: #f87171;
  padding: 8px 18px; border-radius: 20px; font-weight: 800; font-size: 13.5px;
  font-family: monospace;
}
.ledger-content {
  display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-top: 32px;
}
.card-col {
  background: rgba(15, 23, 42, 0.6); border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px; padding: 24px;
}
.col-header {
  font-size: 18px; font-weight: 800; color: #38bdf8; margin-bottom: 18px;
  display: flex; justify-content: space-between; align-items: center;
}
.expense-row {
  display: flex; justify-content: space-between; align-items: center;
  padding: 12px 0; border-bottom: 1px solid rgba(255, 255, 255, 0.06);
  font-size: 16px; color: #e2e8f0; font-weight: 600;
}
.expense-val {
  font-family: 'JetBrains Mono', monospace; font-weight: 800; color: #f43f5e;
}
.summary-bar {
  margin-top: auto;
  background: rgba(30, 41, 59, 0.8); border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 12px; padding: 20px 32px; display: flex; justify-content: space-between;
  align-items: center;
}
.summary-label { font-size: 18px; font-weight: 800; color: #cbd5e1; }
.summary-total { font-family: monospace; font-size: 26px; font-weight: 900; color: #fbbf24; }
</style>
</head>
<body>
  <div class="bg-stage"></div>
  <div class="ledger-board">
    <div class="header-row">
      <div>
        <div class="main-title">THE HOUSEHOLD LIVING COST REALITY</div>
        <div class="sub-title">Indian Middle-Class Monthly Expenditure vs Inflation Erosion</div>
      </div>
      <div class="badge-alert">SAVINGS RATE: 5.3% (50-YR LOW)</div>
    </div>
    <div class="ledger-content">
      <div class="card-col">
        <div class="col-header">
          <span>ESSENTIAL LIVING EXPENSES</span>
          <span style="font-size:13px; color:#94a3b8;">MONTHLY ESTIMATE</span>
        </div>
        <div class="expense-row">
          <span>🛒 Grocery & Kitchen Basket (Food Inflation)</span>
          <span class="expense-val">₹14,200 (+18%)</span>
        </div>
        <div class="expense-row">
          <span>🎓 Children School Fees & Coaching</span>
          <span class="expense-val">₹18,500 (+22%)</span>
        </div>
        <div class="expense-row">
          <span>🏥 Healthcare & Health Insurance (18% GST)</span>
          <span class="expense-val">₹9,800 (+15%)</span>
        </div>
        <div class="expense-row">
          <span>⚡ Electricity, Water & LPG Cylinder</span>
          <span class="expense-val">₹4,650 (+12%)</span>
        </div>
      </div>
      <div class="card-col">
        <div class="col-header">
          <span>DEBT & EMI REPAYMENTS</span>
          <span style="font-size:13px; color:#94a3b8;">RETAIL DEBT</span>
        </div>
        <div class="expense-row">
          <span>🏠 Home Loan EMI (Rising Interest Rates)</span>
          <span class="expense-val">₹24,500</span>
        </div>
        <div class="expense-row">
          <span>💳 Credit Card Minimum Due & Outstandings</span>
          <span class="expense-val">₹6,800</span>
        </div>
        <div class="expense-row">
          <span>📱 Personal Loan / Buy-Now-Pay-Later (BNPL)</span>
          <span class="expense-val">₹5,400</span>
        </div>
        <div class="expense-row">
          <span>📉 Net Monthly Surplus After Expenses</span>
          <span class="expense-val" style="color:#ef4444;">₹ -4,700 (DEFICIT)</span>
        </div>
      </div>
    </div>
    <div class="summary-bar">
      <div class="summary-label">FORENSIC DIAGNOSIS: Families are dipping into ancestral fixed deposits to sustain living standards.</div>
      <div class="summary-total">HOUSEHOLD DEBT: 45.8% GDP</div>
    </div>
  </div>
</body>
</html>"""
    },
    {
        "filename": "ai_06_k_shaped_economic_divergence.jpg",
        "html": """<!DOCTYPE html>
<html>
<head>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  width: 1920px; height: 1080px; overflow: hidden;
  background: #07090e;
  font-family: 'Inter', -apple-system, sans-serif;
  display: flex; align-items: center; justify-content: center;
  position: relative;
}
.bg-grid {
  position: absolute; top:0; left:0; width:100%; height:100%;
  background: radial-gradient(circle at 50% 50%, rgba(15, 23, 42, 0.8) 0%, #07090e 100%);
}
.k-stage {
  position: relative; z-index: 2;
  width: 1440px; height: 860px;
  background: rgba(15, 23, 42, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  box-shadow: 0 40px 100px rgba(0,0,0,0.9);
  padding: 48px 56px;
  display: flex; flex-direction: column;
}
.header-box {
  display: flex; justify-content: space-between; align-items: center;
  border-bottom: 2px solid rgba(255, 255, 255, 0.1); padding-bottom: 20px;
}
.title-k { font-size: 32px; font-weight: 900; color: #fff; }
.sub-k { font-size: 16px; color: #94a3b8; font-weight: 600; margin-top: 4px; }
.k-split-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 40px; flex: 1;
}
.k-pillar {
  border-radius: 14px; padding: 32px; display: flex; flex-direction: column;
}
.k-upper {
  background: linear-gradient(180deg, rgba(16, 185, 129, 0.12) 0%, rgba(15, 23, 42, 0.6) 100%);
  border: 1px solid rgba(16, 185, 129, 0.4);
}
.k-lower {
  background: linear-gradient(180deg, rgba(239, 68, 68, 0.12) 0%, rgba(15, 23, 42, 0.6) 100%);
  border: 1px solid rgba(239, 68, 68, 0.4);
}
.pillar-badge {
  font-family: monospace; font-size: 14px; font-weight: 800; padding: 6px 14px;
  border-radius: 20px; display: inline-block; margin-bottom: 16px; width: fit-content;
}
.k-upper .pillar-badge { background: rgba(16, 185, 129, 0.2); color: #34d399; }
.k-lower .pillar-badge { background: rgba(239, 68, 68, 0.2); color: #f87171; }
.metric-large { font-size: 52px; font-weight: 900; font-family: monospace; margin-bottom: 8px; }
.k-upper .metric-large { color: #10b981; }
.k-lower .metric-large { color: #ef4444; }
.metric-desc { font-size: 18px; font-weight: 800; color: #f8fafc; margin-bottom: 20px; }
.bullet-list { list-style: none; display: flex; flex-direction: column; gap: 14px; }
.bullet-list li { font-size: 15.5px; color: #cbd5e1; font-weight: 600; display: flex; align-items: center; gap: 10px; }
.bullet-list li strong { color: #fff; }
</style>
</head>
<body>
  <div class="bg-grid"></div>
  <div class="k-stage">
    <div class="header-box">
      <div>
        <div class="title-k">THE K-SHAPED CONSUMPTION DIVERGENCE</div>
        <div class="sub-k">Disaggregation of 7.8% Headline Growth: Who Is Actually Spending?</div>
      </div>
      <div style="font-family:monospace; font-size:15px; font-weight:800; color:#fbbf24; background:rgba(251,191,36,0.12); padding:8px 16px; border-radius:20px; border:1px solid #fbbf24;">
        ECONOMIC AUDIT: TWO INDIAS
      </div>
    </div>
    <div class="k-split-grid">
      <div class="k-pillar k-upper">
        <div class="pillar-badge">▲ UPPER ARM OF K (TOP 10-15%)</div>
        <div class="metric-large">+24.5% BOOM</div>
        <div class="metric-desc">Asset-Owners & Corporate Wealth Boom</div>
        <ul class="bullet-list">
          <li>🚗 <strong>Luxury SUVs (>₹20 Lakh):</strong> Massive sales surge of +24.5%.</li>
          <li>📈 <strong>Stock Demat Accounts:</strong> Crossed record 16 Crore holders.</li>
          <li>🏙️ <strong>Luxury Real Estate:</strong> ₹10 Crore flats sold out in hours in Gurugram.</li>
          <li>✈️ <strong>Aviation & High-End Tourism:</strong> Record international leisure trips.</li>
        </ul>
      </div>
      <div class="k-pillar k-lower">
        <div class="pillar-badge">▼ LOWER ARM OF K (MASS 85%)</div>
        <div class="metric-large">-42.0% CONTRACTION</div>
        <div class="metric-desc">Real Wages & Informal Sector Squeeze</div>
        <ul class="bullet-list">
          <li>📉 <strong>Small Cars (Alto/WagonR):</strong> Slashed by -42% vs 2018 peak.</li>
          <li>🛵 <strong>Rural Two-Wheelers:</strong> Sales remain -14% below 2019 levels.</li>
          <li>🍚 <strong>PMGKAY Food Security:</strong> 80 Crore citizens dependent on free ration.</li>
          <li>💳 <strong>Unsecured Loans:</strong> 58.2% of bank borrowing taken for living costs.</li>
        </ul>
      </div>
    </div>
  </div>
</body>
</html>"""
    },
    {
        "filename": "ai_14_youth_demographic_clock_2045.jpg",
        "html": """<!DOCTYPE html>
<html>
<head>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  width: 1920px; height: 1080px; overflow: hidden;
  background: #07090e;
  font-family: 'Inter', -apple-system, sans-serif;
  display: flex; align-items: center; justify-content: center;
  position: relative;
}
.bg-grid {
  position: absolute; top:0; left:0; width:100%; height:100%;
  background: radial-gradient(circle at 50% 50%, rgba(234, 88, 12, 0.25) 0%, #07090e 85%);
}
.clock-stage {
  position: relative; z-index: 2;
  width: 1440px; height: 860px;
  background: rgba(15, 23, 42, 0.88);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 16px;
  box-shadow: 0 40px 100px rgba(0,0,0,0.95);
  padding: 48px 56px;
  display: flex; flex-direction: column;
}
.header-clock {
  display: flex; justify-content: space-between; align-items: center;
  border-bottom: 2px solid rgba(255, 255, 255, 0.1); padding-bottom: 20px;
}
.title-clock { font-size: 32px; font-weight: 900; color: #fff; }
.sub-clock { font-size: 16px; color: #94a3b8; font-weight: 600; margin-top: 4px; }
.clock-body {
  display: grid; grid-template-columns: 1.2fr 1fr; gap: 40px; margin-top: 36px; flex: 1;
}
.clock-dial-card {
  background: rgba(10, 15, 24, 0.8); border: 2px solid rgba(234, 88, 12, 0.5);
  border-radius: 14px; padding: 36px; display: flex; flex-direction: column;
  justify-content: center; align-items: center; text-align: center;
}
.clock-year {
  font-size: 96px; font-weight: 900; font-family: 'JetBrains Mono', monospace;
  color: #ea580c; text-shadow: 0 0 30px rgba(234, 88, 12, 0.6);
}
.clock-subtext {
  font-size: 20px; font-weight: 800; color: #f8fafc; letter-spacing: 2px; margin-top: 6px;
}
.clock-desc {
  font-size: 15px; color: #94a3b8; margin-top: 14px; max-width: 500px; line-height: 1.6;
}
.data-col {
  display: flex; flex-direction: column; gap: 18px;
}
.data-box {
  background: rgba(15, 23, 42, 0.7); border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 12px; padding: 20px 24px;
}
.data-box-title { font-size: 13.5px; color: #94a3b8; font-weight: 700; text-transform: uppercase; }
.data-box-metric { font-size: 26px; font-weight: 900; color: #fbbf24; font-family: monospace; margin-top: 4px; }
.data-box-note { font-size: 14px; color: #cbd5e1; font-weight: 500; margin-top: 4px; }
</style>
</head>
<body>
  <div class="bg-grid"></div>
  <div class="clock-stage">
    <div class="header-clock">
      <div>
        <div class="title-clock">THE 2045 DEMOGRAPHIC CLOCK</div>
        <div class="sub-clock">India's Closing Window of Opportunity: Getting Old Before Getting Rich?</div>
      </div>
      <div style="font-family:monospace; font-size:14px; font-weight:800; color:#ea580c; background:rgba(234,88,12,0.15); padding:8px 16px; border-radius:20px; border:1px solid #ea580c;">
        DEMOGRAPHIC CLIFF: 18 YEARS LEFT
      </div>
    </div>
    <div class="clock-body">
      <div class="clock-dial-card">
        <div class="clock-year">2045</div>
        <div class="clock-subtext">THE DEMOGRAPHIC DEADLINE</div>
        <div class="clock-desc">
          India's working-age population share peaks and begins irreversible contraction by 2045. 
          Without industrial formal jobs, demographic dividend becomes demographic liability.
        </div>
      </div>
      <div class="data-col">
        <div class="data-box">
          <div class="data-box-title">CURRENT MEDIAN AGE</div>
          <div class="data-box-metric">28.4 YEARS</div>
          <div class="data-box-note">Youngest major world economy — peak youth dividend phase today.</div>
        </div>
        <div class="data-box">
          <div class="data-box-title">ANNUAL WORKFORCE ENTRANTS</div>
          <div class="data-box-metric">1.10 CRORE YOUTH</div>
          <div class="data-box-note">11 Million youth enter job market yearly needing formal manufacturing work.</div>
        </div>
        <div class="data-box">
          <div class="data-box-title">TOTAL FERTILITY RATE (NFHS-5)</div>
          <div class="data-box-metric" style="color:#ef4444;">2.0 (BELOW REPLACEMENT)</div>
          <div class="data-box-note">Replacement is 2.1; rapid aging underway in southern and western states.</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>"""
    },
    {
        "filename": "ai_16_benaqaab_final_verdict_stamp.jpg",
        "html": """<!DOCTYPE html>
<html>
<head>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  width: 1920px; height: 1080px; overflow: hidden;
  background: #07090e;
  font-family: 'Inter', -apple-system, sans-serif;
  display: flex; align-items: center; justify-content: center;
  position: relative;
}
.bg-grid {
  position: absolute; top:0; left:0; width:100%; height:100%;
  background: radial-gradient(circle at 50% 50%, rgba(56, 189, 248, 0.15) 0%, #07090e 90%);
}
.verdict-stage {
  position: relative; z-index: 2;
  width: 1440px; height: 860px;
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.14);
  border-radius: 16px;
  box-shadow: 0 40px 100px rgba(0,0,0,0.95);
  padding: 48px 56px;
  display: flex; flex-direction: column;
}
.header-v {
  display: flex; justify-content: space-between; align-items: center;
  border-bottom: 2px solid rgba(255, 255, 255, 0.1); padding-bottom: 20px;
}
.title-v { font-size: 32px; font-weight: 900; color: #fff; }
.sub-v { font-size: 16px; color: #94a3b8; font-weight: 600; margin-top: 4px; }
.reforms-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin-top: 36px; flex: 1;
}
.reform-card {
  background: rgba(10, 15, 24, 0.7); border: 1px solid rgba(56, 189, 248, 0.25);
  border-radius: 12px; padding: 24px 28px; display: flex; flex-direction: column;
}
.card-num {
  font-family: monospace; font-size: 14px; font-weight: 800; color: #38bdf8;
  background: rgba(56, 189, 248, 0.12); padding: 4px 12px; border-radius: 12px;
  width: fit-content; margin-bottom: 12px;
}
.card-h { font-size: 20px; font-weight: 800; color: #f8fafc; margin-bottom: 8px; }
.card-p { font-size: 15px; color: #94a3b8; line-height: 1.55; }
.verdict-stamp-box {
  margin-top: auto;
  background: rgba(251, 191, 36, 0.08); border: 1px solid #fbbf24;
  border-radius: 12px; padding: 18px 28px; display: flex; justify-content: space-between;
  align-items: center;
}
.stamp-text { font-size: 18px; font-weight: 800; color: #fbbf24; }
.stamp-motto { font-size: 16px; font-weight: 900; color: #f8fafc; font-family: monospace; }
</style>
</head>
<body>
  <div class="bg-grid"></div>
  <div class="verdict-stage">
    <div class="header-v">
      <div>
        <div class="title-v">THE ROAD AHEAD: 4 STRUCTURAL REFORMS</div>
        <div class="sub-v">Beyond Headline Celebrations: Transforming Aggregate GDP into Citizen Prosperity</div>
      </div>
      <div style="font-family:monospace; font-size:14px; font-weight:800; color:#38bdf8; background:rgba(56,189,248,0.12); padding:8px 16px; border-radius:20px; border:1px solid #38bdf8;">
        STRATEGIC ROADMAP
      </div>
    </div>
    <div class="reforms-grid">
      <div class="reform-card">
        <div class="card-num">REFORM 01</div>
        <div class="card-h">Labour-Intensive Manufacturing</div>
        <div class="card-p">Eradicate bureaucratic red-tape in textiles, footwear, and consumer electronics to absorb millions from low-yield agriculture.</div>
      </div>
      <div class="reform-card">
        <div class="card-num">REFORM 02</div>
        <div class="card-h">Middle-Class Tax Relief</div>
        <div class="card-p">Remove 18% GST burden on health insurance and adjust income slabs to restore household net savings above 8% baseline.</div>
      </div>
      <div class="reform-card">
        <div class="card-num">REFORM 03</div>
        <div class="card-h">Agrarian Cold-Chain & Processing</div>
        <div class="card-p">Build decentralized storage and food-processing hubs across villages so farmer revenue moves beyond raw crop distress sales.</div>
      </div>
      <div class="reform-card">
        <div class="card-num">REFORM 04</div>
        <div class="card-h">Direct Industrial Skilling</div>
        <div class="card-p">Pivot from generic degrees to hands-on German/Swiss style dual vocational training in CNC robotics, EV assembly, and semiconductor tools.</div>
      </div>
    </div>
    <div class="verdict-stamp-box">
      <div class="stamp-text">FINAL VERDICT: REALITY UNVEILED · BEYOND HEADLINES</div>
      <div class="stamp-motto">BENAQAAB INDIA · SACH · SABOOT · BEBAK</div>
    </div>
  </div>
</body>
</html>"""
    }
]

async def render_conceptual():
    print("🚀 Rendering conceptual 1080p cinematic plates...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for page_data in CONCEPTUAL_PAGES:
            page = await browser.new_page(viewport={"width": 1920, "height": 1080})
            await page.set_content(page_data["html"])
            await page.wait_for_timeout(300)
            out_file = AI_DIR / page_data["filename"]
            await page.screenshot(path=str(out_file))
            print(f"✅ Rendered conceptual plate: {page_data['filename']}")
            await page.close()
        await browser.close()

async def main():
    # 1. Fetch real photos for robot and lab
    fetch_and_save("File:Real-time Quality Control for Welding (5884928619).jpg", "ai_12_the_missing_factory_shenzhen_comparison.jpg")
    fetch_and_save("File:Electronics Laboratory.jpg", "ai_15_vocational_skilling_and_reforms_future.jpg")
    
    # 2. Render conceptual plates
    await render_conceptual()
    print("🎯 Finished all remaining plates!")

if __name__ == "__main__":
    asyncio.run(main())
