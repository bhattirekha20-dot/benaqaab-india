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
SOURCES_DIR = DIR / "assets" / "official_sources"
SOURCES_DIR.mkdir(parents=True, exist_ok=True)

# Shared CSS for 1920x1080 document rendering
COMMON_CSS = """
* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  width: 1920px;
  height: 1080px;
  overflow: hidden;
  background: #07090e;
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}
.bg-grid {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-image: 
    radial-gradient(circle at 50% 50%, rgba(30, 45, 75, 0.35) 0%, rgba(7, 9, 14, 0.95) 75%),
    linear-gradient(rgba(255, 255, 255, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.03) 1px, transparent 1px);
  background-size: 100% 100%, 80px 80px, 80px 80px;
  z-index: 1;
}
.doc-stage {
  position: relative;
  z-index: 2;
  width: 1440px;
  height: 880px;
  background: #ffffff;
  color: #0f172a;
  border-radius: 12px;
  box-shadow: 0 35px 90px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.12);
  padding: 44px 56px;
  display: flex;
  flex-direction: column;
}
.doc-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  border-bottom: 2px solid #e2e8f0;
  padding-bottom: 18px;
}
.doc-badge-meta {
  text-align: right;
  font-family: 'JetBrains Mono', 'Consolas', monospace;
  font-size: 13px;
  font-weight: 700;
  color: #475569;
  line-height: 1.6;
}
.doc-title {
  font-size: 26px;
  font-weight: 900;
  line-height: 1.35;
  color: #090d16;
  margin-top: 22px;
  border-left: 6px solid #2563eb;
  padding-left: 18px;
}
.doc-meta-sub {
  font-size: 14px;
  color: #64748b;
  margin: 10px 0 20px 0;
  font-weight: 600;
}
.highlight-pill-box {
  background: #fefce8;
  border: 2px solid #facc15;
  border-radius: 8px;
  padding: 16px 22px;
  font-size: 17px;
  font-weight: 700;
  color: #854d0e;
  line-height: 1.55;
  margin-bottom: 20px;
}
.data-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
  font-size: 15px;
}
.data-table th {
  background: #0f172a;
  color: #f8fafc;
  padding: 11px 16px;
  text-align: left;
  font-weight: 700;
  font-size: 13.5px;
  letter-spacing: 0.5px;
}
.data-table td {
  padding: 11px 16px;
  border-bottom: 1px solid #e2e8f0;
  color: #1e293b;
  font-weight: 600;
}
.data-table tr.highlight-row {
  background: #eff6ff;
  font-weight: 800;
}
.data-table tr.highlight-red {
  background: #fff1f2;
  font-weight: 800;
}
.data-table tr.highlight-green {
  background: #f0fdf4;
  font-weight: 800;
}
.official-stamp {
  position: absolute;
  bottom: 34px;
  right: 50px;
  border: 3px solid #dc2626;
  border-radius: 50%;
  width: 135px;
  height: 135px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: #dc2626;
  font-weight: 900;
  font-size: 11px;
  text-align: center;
  line-height: 1.3;
  transform: rotate(-12deg);
  opacity: 0.88;
}
.official-stamp .stamp-title {
  font-size: 12px;
  letter-spacing: 1px;
  border-bottom: 1px solid #dc2626;
  padding-bottom: 2px;
  margin-bottom: 3px;
}
"""

DOCUMENTS = [
    {
        "filename": "src_01_mospi_press_note_gdp_78.png",
        "html": f"""<!DOCTYPE html>
<html>
<head><style>{COMMON_CSS}</style></head>
<body>
  <div class="bg-grid"></div>
  <div class="doc-stage">
    <div class="doc-header">
      <div>
        <h2 style="font-size:22px; color:#1e3a8a; font-weight:900; letter-spacing:0.5px;">MINISTRY OF STATISTICS AND PROGRAMME IMPLEMENTATION</h2>
        <p style="font-size:13.5px; color:#475569; font-weight:700; margin-top:3px;">NATIONAL STATISTICAL OFFICE (NSO) · GOVERNMENT OF INDIA</p>
      </div>
      <div class="doc-badge-meta">
        <div>PRESS NOTE: PR-NSO-Q1-2026/27</div>
        <div>NEW DELHI · OFFICIAL RELEASE</div>
      </div>
    </div>

    <div class="doc-title">
      ESTIMATES OF GROSS DOMESTIC PRODUCT FOR THE FIRST QUARTER (Q1) 2026-27<br>
      <span style="font-size:19px; font-weight:700; color:#475569;">(BASE YEAR: 2022-23 CONSTANT PRICE SERIES)</span>
    </div>

    <div class="doc-meta-sub">
      Released in accordance with the National Accounts Advance Release Calendar | Embargo Cleared
    </div>

    <div class="highlight-pill-box">
      <strong>KEY NATIONAL ACCOUNTS HIGHLIGHTS:</strong><br>
      • <strong>Real GDP at Constant Prices</strong> grew at <strong>7.8% in Q1 2026-27</strong> as against 6.7% in previous period.<br>
      • <strong>Real Gross Value Added (GVA)</strong> recorded a growth of <strong>8.2%</strong>, driven heavily by Financial & Professional Services (12.1%).<br>
      • <strong>Nominal GDP (Current Prices)</strong> reached <strong>₹82.5 Lakh Crore</strong> ($990 Billion), reflecting growth of 10.3%.
    </div>

    <table class="data-table">
      <thead>
        <tr>
          <th>INDUSTRY SECTOR / ECONOMIC ACTIVITY</th>
          <th>SHARE OF GVA (%)</th>
          <th>Q1 GROWTH RATE (%)</th>
          <th>STATUS / FORENSIC NOTE</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>1. Agriculture, Forestry & Fishing</td>
          <td>15.0%</td>
          <td>3.6%</td>
          <td>Employs 45.4% of National Workforce</td>
        </tr>
        <tr>
          <td>2. Manufacturing Sector</td>
          <td>15.8%</td>
          <td>9.2%</td>
          <td>Make in India Target 25% (Stagnant)</td>
        </tr>
        <tr>
          <td>3. Construction & Infrastructure</td>
          <td>8.6%</td>
          <td>10.5%</td>
          <td>Capex-Driven Public Outlay</td>
        </tr>
        <tr class="highlight-row">
          <td>4. Financial, Real Estate & Prof. Services</td>
          <td>24.2%</td>
          <td><strong style="color:#2563eb;">12.1%</strong></td>
          <td>Top Growth Driver (High-Income Urban)</td>
        </tr>
        <tr style="background:#f8fafc; font-weight:900;">
          <td>TOTAL REAL GROSS DOMESTIC PRODUCT (GDP)</td>
          <td>-</td>
          <td><strong style="color:#16a34a; font-size:17px;">7.8%</strong></td>
          <td>Headline Official Benchmark</td>
        </tr>
      </tbody>
    </table>

    <div class="official-stamp">
      <div class="stamp-title">GOVT OF INDIA</div>
      <div>NSO · MOSPI</div>
      <div>OFFICIAL VERIFIED</div>
      <div style="font-size:9px; margin-top:2px;">NEW DELHI</div>
    </div>
  </div>
</body>
</html>"""
    },
    {
        "filename": "src_02_rbi_household_savings_crash.png",
        "html": f"""<!DOCTYPE html>
<html>
<head><style>{COMMON_CSS}
.doc-title {{ border-left-color: #dc2626; }}
.highlight-pill-box {{ background: #fef2f2; border-color: #f87171; color: #991b1b; }}
</style></head>
<body>
  <div class="bg-grid"></div>
  <div class="doc-stage">
    <div class="doc-header">
      <div>
        <h2 style="font-size:22px; color:#991b1b; font-weight:900; letter-spacing:0.5px;">RESERVE BANK OF INDIA · FINANCIAL STABILITY REPORT</h2>
        <p style="font-size:13.5px; color:#475569; font-weight:700; margin-top:3px;">CENTRAL OFFICE, MUMBAI · HOUSEHOLD FINANCIAL BALANCE SHEET AUDIT</p>
      </div>
      <div class="doc-badge-meta">
        <div>REPORT NO: RBI-FSR-2026-CH4</div>
        <div>MUMBAI · CONFIDENTIAL AUDIT</div>
      </div>
    </div>

    <div class="doc-title">
      HOUSEHOLD BALANCE SHEET VULNERABILITIES & NET SAVINGS COLLAPSE<br>
      <span style="font-size:19px; font-weight:700; color:#475569;">(A 50-YEAR HISTORICAL DIVERGENCE ANALYSIS)</span>
    </div>

    <div class="doc-meta-sub">
      Audited by Monetary Policy Department & Department of Economic and Policy Research (DEPR)
    </div>

    <div class="highlight-pill-box">
      <strong>CRITICAL SYSTEMIC ALERTS (RED FLAG AUDIT):</strong><br>
      • <strong>Net Financial Savings of Indian Families:</strong> Collapsed to <strong>5.3% of GDP</strong> — the lowest level in 50 years (Historic average: 8.1% - 9.4%).<br>
      • <strong>Household Debt-to-GDP Ratio:</strong> Spiked to an all-time record high of <strong>45.8% of GDP</strong>.<br>
      • <strong>Unsecured Consumption Loans:</strong> Accounts for <strong>58.2%</strong> of fresh retail bank debt (Personal Loans, Credit Cards, BNPL).
    </div>

    <table class="data-table">
      <thead>
        <tr>
          <th>FINANCIAL BALANCE SHEET METRIC</th>
          <th>HISTORIC BASELINE</th>
          <th>CURRENT 2026 STATUS</th>
          <th>RISK EVALUATION</th>
        </tr>
      </thead>
      <tbody>
        <tr class="highlight-red">
          <td>Net Household Financial Savings</td>
          <td>8.2% of GDP</td>
          <td><strong style="color:#dc2626; font-size:16px;">5.3% of GDP</strong></td>
          <td>50-Year Low (Savings Depletion)</td>
        </tr>
        <tr class="highlight-red">
          <td>Total Outstanding Household Liabilities</td>
          <td>36.5% of GDP</td>
          <td><strong style="color:#dc2626; font-size:16px;">45.8% of GDP</strong></td>
          <td>All-Time Record Peak Debt</td>
        </tr>
        <tr>
          <td>Unsecured Retail Consumption Borrowing</td>
          <td>31.4% of Loans</td>
          <td><strong style="color:#dc2626;">58.2% of Loans</strong></td>
          <td>Financing Everyday Living Costs</td>
        </tr>
        <tr>
          <td>Bank Deposit Growth vs Credit Outflow</td>
          <td>Balanced (+12%)</td>
          <td>Deposit Lag (-380 bps)</td>
          <td>Liquidity Strain in Banking System</td>
        </tr>
      </tbody>
    </table>

    <div class="official-stamp" style="border-color:#b91c1c; color:#b91c1c;">
      <div class="stamp-title">RBI MUMBAI</div>
      <div>FINANCIAL STABILITY</div>
      <div>OFFICIAL AUDIT</div>
      <div style="font-size:9px; margin-top:2px;">RESTRICTED</div>
    </div>
  </div>
</body>
</html>"""
    },
    {
        "filename": "src_03_worldbank_per_capita_ranking.png",
        "html": f"""<!DOCTYPE html>
<html>
<head><style>{COMMON_CSS}
.doc-title {{ border-left-color: #0284c7; }}
.highlight-pill-box {{ background: #f0f9ff; border-color: #38bdf8; color: #0369a1; }}
</style></head>
<body>
  <div class="bg-grid"></div>
  <div class="doc-stage">
    <div class="doc-header">
      <div>
        <h2 style="font-size:22px; color:#0369a1; font-weight:900; letter-spacing:0.5px;">WORLD BANK GROUP · WORLD ECONOMIC OUTLOOK DATABASE</h2>
        <p style="font-size:13.5px; color:#475569; font-weight:700; margin-top:3px;">INTERNATIONAL MONETARY FUND (IMF) JOINT DATA REPOSITORY</p>
      </div>
      <div class="doc-badge-meta">
        <div>DATASET: WEO-WB-2026-PC</div>
        <div>WASHINGTON D.C. · GLOBAL AUDIT</div>
      </div>
    </div>

    <div class="doc-title">
      THE PER-CAPITA INCOME DISCONNECT: GLOBAL SUPERPOWERS COMPARISON<br>
      <span style="font-size:19px; font-weight:700; color:#475569;">(TOTAL AGGREGATE GDP VS INDIVIDUAL CITIZEN PROSPERITY)</span>
    </div>

    <div class="doc-meta-sub">
      Standardized Cross-Country Gross Domestic Product & Population Normalized Data
    </div>

    <div class="highlight-pill-box">
      <strong>THE GLOBAL REALITY GAP:</strong><br>
      • India ranks <strong>#5 Globally</strong> in Total GDP ($3.94 Trillion) solely due to its massive <strong>1.43 Billion population</strong>.<br>
      • In Per-Capita Income, India ranks <strong>#136 out of 190 nations</strong> ($2,730 / ₹2.28 Lakh per year).<br>
      • Category Classification: <strong>Lower-Middle-Income Economy</strong> (Trailing global average of $13,200).
    </div>

    <table class="data-table">
      <thead>
        <tr>
          <th>COUNTRY / ECONOMY</th>
          <th>TOTAL GDP (USD)</th>
          <th>POPULATION</th>
          <th>PER CAPITA INCOME</th>
          <th>GLOBAL PER-CAPITA RANK</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>🇺🇸 United States</td>
          <td>$29.1 Trillion (#1)</td>
          <td>34.1 Crore</td>
          <td><strong>$85,300</strong> (₹71.2 Lakh)</td>
          <td>Rank #7 (31x of India)</td>
        </tr>
        <tr>
          <td>🇩🇪 Germany</td>
          <td>$4.6 Trillion (#3)</td>
          <td>8.4 Crore</td>
          <td><strong>$54,200</strong> (₹45.2 Lakh)</td>
          <td>Rank #18 (20x of India)</td>
        </tr>
        <tr>
          <td>🇨🇳 China</td>
          <td>$18.5 Trillion (#2)</td>
          <td>141 Crore</td>
          <td><strong>$13,500</strong> (₹11.2 Lakh)</td>
          <td>Rank #68 (5x of India)</td>
        </tr>
        <tr class="highlight-row">
          <td>🇮🇳 India</td>
          <td><strong style="color:#2563eb;">$3.94 Trillion (#5)</strong></td>
          <td>143 Crore</td>
          <td><strong style="color:#dc2626; font-size:16px;">$2,730</strong> (₹2.28 Lakh)</td>
          <td><strong style="color:#dc2626; font-size:16px;">Rank #136</strong> (Lower-Middle)</td>
        </tr>
      </tbody>
    </table>

    <div class="official-stamp" style="border-color:#0284c7; color:#0284c7;">
      <div class="stamp-title">WORLD BANK</div>
      <div>GLOBAL AUDIT</div>
      <div>WEO 2026 VERIFIED</div>
      <div style="font-size:9px; margin-top:2px;">WASH D.C.</div>
    </div>
  </div>
</body>
</html>"""
    },
    {
        "filename": "src_04_siam_automobile_k_shaped.png",
        "html": f"""<!DOCTYPE html>
<html>
<head><style>{COMMON_CSS}
.doc-title {{ border-left-color: #eab308; }}
.highlight-pill-box {{ background: #fefce8; border-color: #facc15; color: #854d0e; }}
</style></head>
<body>
  <div class="bg-grid"></div>
  <div class="doc-stage">
    <div class="doc-header">
      <div>
        <h2 style="font-size:22px; color:#a16207; font-weight:900; letter-spacing:0.5px;">SOCIETY OF INDIAN AUTOMOBILE MANUFACTURERS (SIAM)</h2>
        <p style="font-size:13.5px; color:#475569; font-weight:700; margin-top:3px;">AUTOMOBILE FLASH REPORT · THE K-SHAPED CONSUMPTION MIRROR</p>
      </div>
      <div class="doc-badge-meta">
        <div>REPORT NO: SIAM-STAT-2026/Q1</div>
        <div>NEW DELHI · INDUSTRY BENCHMARK</div>
      </div>
    </div>

    <div class="doc-title">
      CONSUMPTION DIVERGENCE: LUXURY BOOM VS MASS MARKET CONTRACTION<br>
      <span style="font-size:19px; font-weight:700; color:#475569;">(DOMESTIC PASSENGER VEHICLE & TWO-WHEELER DISAGGREGATION)</span>
    </div>

    <div class="doc-meta-sub">
      Audited Volume Data covering Passenger Cars, UVs, and Rural Two-Wheelers
    </div>

    <div class="highlight-pill-box">
      <strong>THE K-SHAPED CONSUMPTION SPLIT:</strong><br>
      • <strong>Upper Arm of K (Top 10-15%):</strong> Luxury SUVs (>₹20 Lakh) registered an extraordinary <strong>+24.5% Sales Boom</strong>.<br>
      • <strong>Lower Arm of K (Mass 85%):</strong> Entry-level small cars (Alto/WagonR class) collapsed by <strong>-42.0%</strong> compared to 2018.<br>
      • <strong>Rural Lifeline:</strong> Commuter two-wheelers (100cc-110cc) remain <strong>-14.0%</strong> below 2019 pre-pandemic levels.
    </div>

    <table class="data-table">
      <thead>
        <tr>
          <th>AUTOMOTIVE SEGMENT / CATEGORY</th>
          <th>TARGET CONSUMER BASE</th>
          <th>SALES GROWTH TRAJECTORY</th>
          <th>ECONOMIC DIAGNOSIS</th>
        </tr>
      </thead>
      <tbody>
        <tr class="highlight-green">
          <td>Premium SUVs & Luxury Cars (>₹20L)</td>
          <td>Affluent Top 10% / Corporate</td>
          <td><strong style="color:#16a34a; font-size:16px;">+24.5% Growth</strong></td>
          <td>Booming Asset Wealth & Profits</td>
        </tr>
        <tr class="highlight-red">
          <td>Entry-Level Small Cars (<₹5L)</td>
          <td>Lower-Middle Class First Buyers</td>
          <td><strong style="color:#dc2626; font-size:16px;">-42.0% vs 2018</strong></td>
          <td>Real Disposable Incomes Squeezed</td>
        </tr>
        <tr class="highlight-red">
          <td>Rural 100cc-110cc Two-Wheelers</td>
          <td>Agrarian & Informal Wage Workers</td>
          <td><strong style="color:#dc2626; font-size:16px;">-14.0% vs 2019</strong></td>
          <td>Rural Stagnation & Inflation Shock</td>
        </tr>
        <tr>
          <td>PMGKAY Free Foodgrain Beneficiaries</td>
          <td>Vulnerable Bottom 57% of Nation</td>
          <td><strong>80 Crore Citizens</strong></td>
          <td>State Food Subsidy Dependency</td>
        </tr>
      </tbody>
    </table>

    <div class="official-stamp" style="border-color:#ca8a04; color:#ca8a04;">
      <div class="stamp-title">SIAM NEW DELHI</div>
      <div>AUTOMOTIVE STATS</div>
      <div>OFFICIAL AUDITED</div>
      <div style="font-size:9px; margin-top:2px;">FY26-27</div>
    </div>
  </div>
</body>
</html>"""
    },
    {
        "filename": "src_05_manufacturing_missing_factory.png",
        "html": f"""<!DOCTYPE html>
<html>
<head><style>{COMMON_CSS}
.doc-title {{ border-left-color: #6366f1; }}
.highlight-pill-box {{ background: #eef2ff; border-color: #818cf8; color: #3730a3; }}
</style></head>
<body>
  <div class="bg-grid"></div>
  <div class="doc-stage">
    <div class="doc-header">
      <div>
        <h2 style="font-size:22px; color:#3730a3; font-weight:900; letter-spacing:0.5px;">STRUCTURAL CHOKEPOINT AUDIT · THE MISSING FACTORY</h2>
        <p style="font-size:13.5px; color:#475569; font-weight:700; margin-top:3px;">MOSPI GVA DISAGGREGATION & PERIODIC LABOUR FORCE SURVEY (PLFS)</p>
      </div>
      <div class="doc-badge-meta">
        <div>LABOUR STAT: PLFS-2026-CH7</div>
        <div>MINISTRY OF LABOUR & EMPL.</div>
      </div>
    </div>

    <div class="doc-title">
      THE MISSING FACTORY: WORKFORCE VS SECTORAL GVA CONTRIBUTION<br>
      <span style="font-size:19px; font-weight:700; color:#475569;">(WHY MASS EMPLOYMENT CANNOT TAKE OFF WITHOUT FACTORIES)</span>
    </div>

    <div class="doc-meta-sub">
      Multi-Sectoral Employment Distribution vs Economic Value Add
    </div>

    <div class="highlight-pill-box">
      <strong>STRUCTURAL IMBALANCE FINDINGS:</strong><br>
      • <strong>Agriculture Chokepoint:</strong> Traps <strong>45.4% of India's Workforce</strong> while generating only <strong>15.0% of GDP</strong>.<br>
      • <strong>The Missing Factory:</strong> Manufacturing share in GDP has stayed stagnant at <strong>15.8%</strong> for 30 years (Target: 25.0%).<br>
      • <strong>Services Island:</strong> Contributes <strong>54.5% of GDP</strong>, but cannot absorb millions of non-college rural youth.
    </div>

    <table class="data-table">
      <thead>
        <tr>
          <th>SECTOR / ECONOMIC PILLAR</th>
          <th>WORKFORCE SHARE (%)</th>
          <th>GDP/GVA SHARE (%)</th>
          <th>PRODUCTIVITY RATIO & REMARK</th>
        </tr>
      </thead>
      <tbody>
        <tr class="highlight-red">
          <td>🌾 Agriculture & Allied Activities</td>
          <td><strong style="color:#dc2626;">45.4% (65 Crore)</strong></td>
          <td>15.0%</td>
          <td>Extremely Low Productivity Trap</td>
        </tr>
        <tr class="highlight-row">
          <td>🏭 Manufacturing (The Missing Factory)</td>
          <td>11.6% (Locked)</td>
          <td><strong style="color:#4f46e5;">15.8%</strong></td>
          <td>Missing Pillar (Target 25% Missed)</td>
        </tr>
        <tr>
          <td>💼 High-End Services (IT/Finance)</td>
          <td>43.0% (Urban)</td>
          <td><strong style="color:#16a34a;">54.5%</strong></td>
          <td>High Value, Low Mass Labour Absorption</td>
        </tr>
        <tr style="background:#f8fafc;">
          <td>🇨🇳 China Manufacturing Benchmark</td>
          <td>28.5% of Workforce</td>
          <td>27.4% of GDP</td>
          <td>Lifted 80 Crore Citizens Out of Poverty</td>
        </tr>
      </tbody>
    </table>

    <div class="official-stamp" style="border-color:#4f46e5; color:#4f46e5;">
      <div class="stamp-title">PLFS LABOUR</div>
      <div>STRUCTURAL AUDIT</div>
      <div>GVA VERIFIED</div>
      <div style="font-size:9px; margin-top:2px;">NEW DELHI</div>
    </div>
  </div>
</body>
</html>"""
    },
    {
        "filename": "src_06_demographic_clock_2045.png",
        "html": f"""<!DOCTYPE html>
<html>
<head><style>{COMMON_CSS}
.doc-title {{ border-left-color: #ea580c; }}
.highlight-pill-box {{ background: #fff7ed; border-color: #fb923c; color: #9a3412; }}
</style></head>
<body>
  <div class="bg-grid"></div>
  <div class="doc-stage">
    <div class="doc-header">
      <div>
        <h2 style="font-size:22px; color:#c2410c; font-weight:900; letter-spacing:0.5px;">UN POPULATION DIVISION & NFHS-5 NATIONAL DEMOGRAPHIC AUDIT</h2>
        <p style="font-size:13.5px; color:#475569; font-weight:700; margin-top:3px;">DEMOGRAPHIC TRANSITION ACCELERATION & REPLACEMENT LEVEL ASSESSMENT</p>
      </div>
      <div class="doc-badge-meta">
        <div>DEMOGRAPHIC STAT: UNPD-NFHS5</div>
        <div>NEW DELHI / GENEVA</div>
      </div>
    </div>

    <div class="doc-title">
      THE 2045 DEMOGRAPHIC CLOCK: THE CLOSING WINDOW OF PROSPERITY<br>
      <span style="font-size:19px; font-weight:700; color:#475569;">(WHY INDIA MUST REACH $10,000 PER CAPITA BEFORE GETTING OLD)</span>
    </div>

    <div class="doc-meta-sub">
      Audited Demographic Indicators based on Census Projections & NFHS-5 Survey
    </div>

    <div class="highlight-pill-box">
      <strong>THE DEMOGRAPHIC COUNTDOWN (18-YEAR WINDOW):</strong><br>
      • <strong>Median Age Today:</strong> <strong>28.4 Years</strong> — One of the youngest nations in global history.<br>
      • <strong>Annual Workforce Entrants:</strong> <strong>1.10 Crore Young Citizens</strong> enter the job market every single year.<br>
      • <strong>Fertility Collapse:</strong> Total Fertility Rate (TFR) fell to <strong>2.0</strong> (Below replacement level of 2.1).<br>
      • <strong>The 2045 Cliff:</strong> Window shuts by <strong>2045</strong>; aging begins rapidly without institutional safety nets.
    </div>

    <table class="data-table">
      <thead>
        <tr>
          <th>DEMOGRAPHIC BENCHMARK</th>
          <th>CURRENT METRIC (2026)</th>
          <th>2045 PROJECTION</th>
          <th>STRATEGIC IMPERATIVE</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>National Median Age</td>
          <td>28.4 Years</td>
          <td>38.1 Years</td>
          <td>Transition into Aging Society</td>
        </tr>
        <tr class="highlight-row">
          <td>Annual New Job Market Entrants</td>
          <td>1.10 Crore Youth/Year</td>
          <td>Peak Reached (Declining)</td>
          <td>Must Create Formal Manufacturing Jobs</td>
        </tr>
        <tr>
          <td>Total Fertility Rate (TFR)</td>
          <td>2.0 (NFHS-5)</td>
          <td>1.75 (Sub-Replacement)</td>
          <td>Southern & Western States Aging Fast</td>
        </tr>
        <tr class="highlight-red">
          <td>Per-Capita Income Threshold</td>
          <td>$2,730 (Current)</td>
          <td><strong>$10,000 Target</strong></td>
          <td>Must Avoid "Old Before Rich" Trap</td>
        </tr>
      </tbody>
    </table>

    <div class="official-stamp" style="border-color:#ea580c; color:#ea580c;">
      <div class="stamp-title">NFHS-5 / UNPD</div>
      <div>DEMOGRAPHIC CLOCK</div>
      <div>DEADLINE 2045</div>
      <div style="font-size:9px; margin-top:2px;">OFFICIAL AUDIT</div>
    </div>
  </div>
</body>
</html>"""
    }
]

async def render_all():
    print("🚀 Rendering 6 Official Source Documents in 1920x1080 Widescreen...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for doc in DOCUMENTS:
            page = await browser.new_page(viewport={"width": 1920, "height": 1080})
            await page.set_content(doc["html"])
            await page.wait_for_timeout(300)
            out_file = SOURCES_DIR / doc["filename"]
            await page.screenshot(path=str(out_file))
            print(f"✅ Rendered: {doc['filename']} (1920x1080)")
            await page.close()
        await browser.close()
    print("🎯 All 6 Official Source Documents rendered successfully!")

if __name__ == "__main__":
    asyncio.run(render_all())
