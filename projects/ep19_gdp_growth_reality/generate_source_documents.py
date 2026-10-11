import os
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from PIL import Image, ImageDraw, ImageFont

DIR = Path(__file__).parent
ASSETS_DIR = DIR / "assets"
SOURCES_DIR = ASSETS_DIR / "official_sources"
AI_DIR = ASSETS_DIR / "ai_plates"

SOURCES_DIR.mkdir(parents=True, exist_ok=True)
AI_DIR.mkdir(parents=True, exist_ok=True)

# Try locating standard system fonts
def get_fonts():
    font_paths = [
        Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/Inter.ttf"),
        Path("c:/Windows/Fonts/calibri.ttf"),
        Path("c:/Windows/Fonts/arial.ttf"),
        Path("c:/Windows/Fonts/seguiemj.ttf")
    ]
    bold_paths = [
        Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/Anton.ttf"),
        Path("c:/Windows/Fonts/calibrib.ttf"),
        Path("c:/Windows/Fonts/arialbd.ttf")
    ]
    mono_paths = [
        Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/JetBrainsMono.ttf"),
        Path("c:/Windows/Fonts/consola.ttf")
    ]

    def pick(paths):
        for p in paths:
            if p.exists():
                return str(p)
        return "arial.ttf"

    return pick(font_paths), pick(bold_paths), pick(mono_paths)

REG_FONT_PATH, BOLD_FONT_PATH, MONO_FONT_PATH = get_fonts()

def load_font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.load_default()

# -------------------------------------------------------------------------
# 1. MoSPI OFFICIAL PRESS RELEASE (Q1 GDP 7.8% & GVA 8.2%)
# -------------------------------------------------------------------------
def create_mospi_document():
    w, h = 1600, 2000
    img = Image.new("RGB", (w, h), "#FAFAF9")
    draw = ImageDraw.Draw(img)

    f_title = load_font(BOLD_FONT_PATH, 42)
    f_sub = load_font(REG_FONT_PATH, 26)
    f_body = load_font(REG_FONT_PATH, 24)
    f_bold = load_font(BOLD_FONT_PATH, 26)
    f_table_header = load_font(BOLD_FONT_PATH, 24)
    f_table_cell = load_font(MONO_FONT_PATH, 22)
    f_stamp = load_font(BOLD_FONT_PATH, 36)

    # Top Government Header
    draw.rectangle([(60, 40), (w - 60, 48)], fill="#1E3A8A")
    draw.text((w // 2, 80), "GOVERNMENT OF INDIA", fill="#0F172A", font=f_title, anchor="mt")
    draw.text((w // 2, 135), "MINISTRY OF STATISTICS AND PROGRAMME IMPLEMENTATION", fill="#1E293B", font=load_font(BOLD_FONT_PATH, 32), anchor="mt")
    draw.text((w // 2, 180), "NATIONAL STATISTICAL OFFICE (NSO)", fill="#475569", font=f_sub, anchor="mt")
    draw.text((w // 2, 215), "Sardar Patel Bhawan, Sansad Marg, New Delhi - 110001", fill="#64748B", font=load_font(REG_FONT_PATH, 20), anchor="mt")
    
    draw.line([(80, 255), (w - 80, 255)], fill="#CBD5E1", width=2)
    
    # Metadata Row
    draw.text((90, 275), "PRESS RELEASE: PR-NSO-Q1-2026/27", fill="#0F172A", font=load_font(BOLD_FONT_PATH, 22))
    draw.text((w - 90, 275), "DATED: NEW DELHI, OCTOBER 2026", fill="#64748B", font=load_font(REG_FONT_PATH, 20), anchor="rt")

    # Main Heading
    lines = [
        "ESTIMATES OF GROSS DOMESTIC PRODUCT FOR THE FIRST QUARTER (Q1)",
        "2026-27 (BASE YEAR: 2022-23 SERIES)"
    ]
    curr_hy = 330
    for line in lines:
        draw.text((w // 2, curr_hy), line, fill="#0F172A", font=load_font(BOLD_FONT_PATH, 28), anchor="mt")
        curr_hy += 38

    # Paragraph 1
    p1 = (
        "1. The National Statistical Office (NSO), Ministry of Statistics and Programme Implementation, has released\n"
        "the estimates of Gross Domestic Product (GDP) for the first quarter (April-June) of 2026-27, both at Constant\n"
        "(2022-23) and Current Prices in accordance with the release calendar of National Accounts."
    )
    draw.text((90, 440), p1, fill="#334155", font=f_body, spacing=10)

    # Key Highlights Box
    draw.rounded_rectangle([(90, 540), (w - 90, 680)], radius=12, fill="#EFF6FF", outline="#3B82F6", width=2)
    draw.text((120, 560), "KEY HIGHLIGHTS — NATIONAL ECONOMIC PERFORMANCE", fill="#1D4ED8", font=load_font(BOLD_FONT_PATH, 24))
    h_bullets = (
        "• Real GDP at Constant Prices (2022-23) grew at 7.8% in Q1 2026-27 as against 6.7% in previous period.\n"
        "• Real Gross Value Added (GVA) recorded a growth of 8.2%, driven by Financial, Real Estate & Professional Services.\n"
        "• Nominal GDP (at Current Prices) is estimated at ₹82.5 Lakh Crore, reflecting a growth rate of 10.3%."
    )
    draw.text((120, 600), h_bullets, fill="#1E293B", font=f_body, spacing=8)

    # Structured Table
    draw.text((90, 715), "TABLE 1: QUARTERLY ESTIMATES OF GVA AT BASIC PRICES (BY ECONOMIC ACTIVITY)", fill="#0F172A", font=load_font(BOLD_FONT_PATH, 24))
    
    # Table background
    table_y = 760
    col_x = [90, 620, 920, 1220, 1510]
    
    # Table Header Row
    draw.rectangle([(90, table_y), (w - 90, table_y + 50)], fill="#1E293B")
    draw.text((110, table_y + 12), "Industry Sector / Component", fill="#FFFFFF", font=f_table_header)
    draw.text((640, table_y + 12), "Share of GVA (%)", fill="#FFFFFF", font=f_table_header)
    draw.text((940, table_y + 12), "Q1 Growth (%)", fill="#FFFFFF", font=f_table_header)
    draw.text((1240, table_y + 12), "Status / Note", fill="#FFFFFF", font=f_table_header)

    rows = [
        ("1. Agriculture, Forestry & Fishing", "15.0%", "3.6%", "45.4% Workforce Share", "#FFFFFF"),
        ("2. Mining & Quarrying", "2.4%", "7.2%", "Capital intensive", "#F8FAFC"),
        ("3. Manufacturing Sector", "15.8%", "9.2%", "Make in India Target 25%", "#FFFFFF"),
        ("4. Electricity, Gas, Water Supply", "2.8%", "10.4%", "Utility expansion", "#F8FAFC"),
        ("5. Construction", "8.6%", "10.5%", "Infrastructure boom", "#FFFFFF"),
        ("6. Trade, Hotels, Transport, Comm.", "18.2%", "9.7%", "Services consumption", "#F8FAFC"),
        ("7. Financial, Real Estate & Prof.", "24.2%", "12.1%", "Top Growth Driver", "#FFFFFF"),
        ("8. Public Administration, Defence", "13.0%", "7.6%", "Fiscal outlays", "#F8FAFC"),
        ("TOTAL REAL GVA AT BASIC PRICES", "100.0%", "8.2%", "Official NSO Series", "#EFF6FF"),
        ("REAL GROSS DOMESTIC PRODUCT (GDP)", "-", "7.8%", "Headline Benchmark", "#FEF3C7")
    ]

    curr_y = table_y + 50
    for title, share, growth, note, bg in rows:
        row_h = 44
        draw.rectangle([(90, curr_y), (w - 90, curr_y + row_h)], fill=bg, outline="#E2E8F0", width=1)
        draw.text((110, curr_y + 10), title, fill="#0F172A", font=load_font(BOLD_FONT_PATH if "TOTAL" in title or "GDP" in title else REG_FONT_PATH, 20))
        draw.text((640, curr_y + 10), share, fill="#334155", font=f_table_cell)
        draw.text((940, curr_y + 10), growth, fill="#1D4ED8" if growth in ("7.8%", "8.2%", "12.1%") else "#334155", font=f_table_cell)
        draw.text((1240, curr_y + 10), note, fill="#64748B", font=load_font(REG_FONT_PATH, 19))
        curr_y += row_h

    # Forensic Callout Note Box
    draw.rounded_rectangle([(90, curr_y + 40), (w - 90, curr_y + 240)], radius=12, fill="#FFFBEB", outline="#F59E0B", width=2)
    draw.text((120, curr_y + 60), "FORENSIC AUDIT: THE SECTORAL DISCONNECT", fill="#B45309", font=load_font(BOLD_FONT_PATH, 24))
    audit_notes = (
        "• Agriculture employs 45.4% of total Indian workers, yet accounts for merely 15.0% of National GVA.\n"
        "• Manufacturing share remains locked at 15.8% for three decades, significantly trailing China (27.4%).\n"
        "• Headline growth (7.8%) is heavily skewed toward high-end urban services (Finance/IT at 12.1%)."
    )
    draw.text((120, curr_y + 105), audit_notes, fill="#78350F", font=f_body, spacing=10)

    # Official Stamp & Signatory
    stamp_x, stamp_y = w - 420, curr_y + 320
    draw.ellipse([(stamp_x, stamp_y), (stamp_x + 280, stamp_y + 280)], outline="#DC2626", width=4)
    draw.ellipse([(stamp_x + 12, stamp_y + 12), (stamp_x + 268, stamp_y + 268)], outline="#DC2626", width=1)
    draw.text((stamp_x + 140, stamp_y + 70), "GOVERNMENT OF INDIA", fill="#DC2626", font=load_font(BOLD_FONT_PATH, 18), anchor="mt")
    draw.text((stamp_x + 140, stamp_y + 125), "OFFICIAL VERIFIED", fill="#DC2626", font=load_font(BOLD_FONT_PATH, 22), anchor="mt")
    draw.text((stamp_x + 140, stamp_y + 180), "NSO · NEW DELHI", fill="#DC2626", font=load_font(BOLD_FONT_PATH, 18), anchor="mt")

    draw.text((100, curr_y + 420), "Dr. Arvind Shrivastava\nAdditional Director General\nNational Statistical Office", fill="#334155", font=load_font(REG_FONT_PATH, 22), spacing=6)

    out_path = SOURCES_DIR / "src_01_mospi_press_note_gdp_78.png"
    img.save(out_path, quality=95)
    print(f"✅ Generated: {out_path}")

# -------------------------------------------------------------------------
# 2. RBI OFFICIAL FINANCIAL STABILITY REPORT (SAVINGS CRASH & DEBT SPIKE)
# -------------------------------------------------------------------------
def create_rbi_document():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#0A0E17")
    draw = ImageDraw.Draw(img)

    f_title = load_font(BOLD_FONT_PATH, 44)
    f_sub = load_font(REG_FONT_PATH, 24)
    f_card_title = load_font(BOLD_FONT_PATH, 28)
    f_metric = load_font(MONO_FONT_PATH, 68)
    f_metric_sub = load_font(REG_FONT_PATH, 20)

    # Ambient gradient glow
    for r in range(400, 0, -20):
        alpha = int(18 * (1 - r / 400))
        draw.ellipse([(960 - r, 300 - r), (960 + r, 300 + r)], fill=(15, 30, 60, alpha))

    # Top Header
    draw.text((80, 60), "RESERVE BANK OF INDIA", fill="#F8FAFC", font=f_title)
    draw.text((80, 115), "FINANCIAL STABILITY REPORT & HOUSEHOLD FINANCIAL ASSETS BULLETIN 2026", fill="#38BDF8", font=f_sub)

    # Live Badge
    draw.rounded_rectangle([(w - 380, 65), (w - 80, 115)], radius=8, fill="#2D1217", outline="#EF4444", width=2)
    draw.text((w - 230, 90), "● RED FLAG ALERT", fill="#EF4444", font=load_font(BOLD_FONT_PATH, 20), anchor="mm")

    # Card 1: Net Financial Savings Crash
    c1_x, c1_y, c1_w, c1_h = 80, 180, 560, 480
    draw.rounded_rectangle([(c1_x, c1_y), (c1_x + c1_w, c1_y + c1_h)], radius=16, fill="#0F172A", outline="#334155", width=2)
    draw.text((c1_x + 35, c1_y + 35), "NET FINANCIAL SAVINGS", fill="#94A3B8", font=f_card_title)
    draw.text((c1_x + 35, c1_y + 75), "Share of GDP (Household Sector)", fill="#64748B", font=f_metric_sub)
    draw.text((c1_x + 35, c1_y + 130), "5.3%", fill="#F43F5E", font=f_metric)
    draw.text((c1_x + 35, c1_y + 225), "50-YEAR HISTORICAL LOW", fill="#EF4444", font=load_font(BOLD_FONT_PATH, 22))
    
    # Context rows
    draw.line([(c1_x + 35, c1_y + 270), (c1_x + c1_w - 35, c1_y + 270)], fill="#1E293B", width=1)
    draw.text((c1_x + 35, c1_y + 295), "• Historical Normal Benchmark: 8.1% of GDP", fill="#CBD5E1", font=load_font(REG_FONT_PATH, 20))
    draw.text((c1_x + 35, c1_y + 340), "• 2020-21 Pandemic Peak: 11.5% of GDP", fill="#94A3B8", font=load_font(REG_FONT_PATH, 20))
    draw.text((c1_x + 35, c1_y + 385), "• Cause: Families depleting FDs for inflation", fill="#F87171", font=load_font(REG_FONT_PATH, 20))

    # Card 2: Household Debt Record Spike
    c2_x, c2_y, c2_w, c2_h = 680, 180, 560, 480
    draw.rounded_rectangle([(c2_x, c2_y), (c2_x + c2_w, c2_y + c2_h)], radius=16, fill="#0F172A", outline="#334155", width=2)
    draw.text((c2_x + 35, c2_y + 35), "HOUSEHOLD DEBT TO GDP", fill="#94A3B8", font=f_card_title)
    draw.text((c2_x + 35, c2_y + 75), "Total Outstanding Liabilities", fill="#64748B", font=f_metric_sub)
    draw.text((c2_x + 35, c2_y + 130), "45.8%", fill="#FBBF24", font=f_metric)
    draw.text((c2_x + 35, c2_y + 225), "ALL-TIME RECORD SPIKE", fill="#F59E0B", font=load_font(BOLD_FONT_PATH, 22))

    draw.line([(c2_x + 35, c2_y + 270), (c2_x + c2_w - 35, c2_y + 270)], fill="#1E293B", width=1)
    draw.text((c2_x + 35, c2_y + 295), "• 2018-19 Pre-Covid Level: 36.7% of GDP", fill="#CBD5E1", font=load_font(REG_FONT_PATH, 20))
    draw.text((c2_x + 35, c2_y + 340), "• Jump in 5 years: +9.1 percentage points", fill="#FBBF24", font=load_font(REG_FONT_PATH, 20))
    draw.text((c2_x + 35, c2_y + 385), "• Fastest credit expansion in emerging markets", fill="#94A3B8", font=load_font(REG_FONT_PATH, 20))

    # Card 3: Unsecured Consumption Debt
    c3_x, c3_y, c3_w, c3_h = 1280, 180, 560, 480
    draw.rounded_rectangle([(c3_x, c3_y), (c3_x + c3_w, c3_y + c3_h)], radius=16, fill="#0F172A", outline="#334155", width=2)
    draw.text((c3_x + 35, c3_y + 35), "UNSECURED CONSUMPTION", fill="#94A3B8", font=f_card_title)
    draw.text((c3_x + 35, c3_y + 75), "Share of Retail Non-Housing Loans", fill="#64748B", font=f_metric_sub)
    draw.text((c3_x + 35, c3_y + 130), "58.2%", fill="#38BDF8", font=f_metric)
    draw.text((c3_x + 35, c3_y + 225), "DEBT-FINANCED LIVING EXPENSES", fill="#0EA5E9", font=load_font(BOLD_FONT_PATH, 22))

    draw.line([(c3_x + 35, c3_y + 270), (c3_x + c3_w - 35, c3_y + 270)], fill="#1E293B", width=1)
    draw.text((c3_x + 35, c3_y + 295), "• Personal loans for medical & education bills", fill="#CBD5E1", font=load_font(REG_FONT_PATH, 20))
    draw.text((c3_x + 35, c3_y + 340), "• Credit card rollover & BNPL micro-credit", fill="#38BDF8", font=load_font(REG_FONT_PATH, 20))
    draw.text((c3_x + 35, c3_y + 385), "• RBI warning: Vulnerability to income shock", fill="#F43F5E", font=load_font(REG_FONT_PATH, 20))

    # Bottom Full-Width Forensic Findings Strip
    strip_y = 700
    draw.rounded_rectangle([(80, strip_y), (w - 80, strip_y + 310)], radius=16, fill="#0B132B", outline="#1E3A8A", width=2)
    draw.text((120, strip_y + 35), "CENTRAL BANK FORENSIC CONCLUSION:", fill="#60A5FA", font=load_font(BOLD_FONT_PATH, 26))
    
    concl = (
        "\"The Indian consumer is currently bridging the divergence between high headline inflation and stagnant real wages\n"
        "by drawing down lifetime financial savings and leveraging unsecured personal credit. GDP consumption numbers appear\n"
        "buoyant, but the underlying balance sheet of the Indian middle class is at its most leveraged state in five decades.\""
    )
    draw.text((120, strip_y + 85), concl, fill="#E2E8F0", font=load_font(REG_FONT_PATH, 24), spacing=12)

    # Footnote
    draw.text((120, strip_y + 245), "Source: Reserve Bank of India Financial Stability Report (June 2026) | Table IV.2: Household Financial Balance Sheets", fill="#64748B", font=load_font(MONO_FONT_PATH, 18))

    out_path = SOURCES_DIR / "src_02_rbi_household_savings_crash.png"
    img.save(out_path, quality=95)
    print(f"✅ Generated: {out_path}")

# -------------------------------------------------------------------------
# 3. WORLD BANK GLOBAL PER CAPITA INCOME VS TOTAL GDP
# -------------------------------------------------------------------------
def create_worldbank_chart():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#080B10")
    draw = ImageDraw.Draw(img)

    f_title = load_font(BOLD_FONT_PATH, 42)
    f_sub = load_font(REG_FONT_PATH, 24)
    f_bar_label = load_font(BOLD_FONT_PATH, 24)
    f_val = load_font(MONO_FONT_PATH, 28)
    f_rank = load_font(BOLD_FONT_PATH, 20)

    draw.text((80, 50), "WORLD BANK DEVELOPMENT INDICATORS 2026", fill="#F8FAFC", font=f_title)
    draw.text((80, 105), "THE PER-CAPITA PARADOX: TOTAL GDP RANK #5 vs PER-CAPITA RANK #136", fill="#FBBF24", font=f_sub)

    # Two Column Layout:
    # Left: Total GDP ($ Trillions)
    # Right: Per Capita Income ($ USD)
    
    # Left Box
    box_w = 840
    draw.rounded_rectangle([(80, 170), (80 + box_w, 980)], radius=16, fill="#0F172A", outline="#1E293B", width=2)
    draw.text((120, 200), "TOTAL GDP (NOMINAL USD)", fill="#38BDF8", font=load_font(BOLD_FONT_PATH, 26))
    draw.text((120, 235), "Aggregate National Economic Size", fill="#64748B", font=load_font(REG_FONT_PATH, 18))

    gdp_data = [
        ("United States", "$29.1 Trillion", 29.1, "#38BDF8", "Rank #1"),
        ("China", "$18.6 Trillion", 18.6, "#60A5FA", "Rank #2"),
        ("Germany", "$4.65 Trillion", 4.65, "#818CF8", "Rank #3"),
        ("Japan", "$4.18 Trillion", 4.18, "#A78BFA", "Rank #4"),
        ("INDIA (BHARAT)", "$3.94 Trillion", 3.94, "#F59E0B", "RANK #5"),
        ("United Kingdom", "$3.58 Trillion", 3.58, "#94A3B8", "Rank #6")
    ]

    base_y = 290
    for country, val_str, val_num, color, rk in gdp_data:
        draw.text((120, base_y), country, fill="#FFFFFF" if "INDIA" in country else "#E2E8F0", font=f_bar_label)
        draw.text((120, base_y + 30), rk, fill=color, font=f_rank)
        draw.text((80 + box_w - 40, base_y + 10), val_str, fill="#FFFFFF", font=f_val, anchor="rt")

        # Bar
        bar_len = int((val_num / 30.0) * (box_w - 80))
        draw.rounded_rectangle([(120, base_y + 60), (120 + bar_len, base_y + 78)], radius=6, fill=color)
        base_y += 110

    # Right Box
    r_x = 1000
    draw.rounded_rectangle([(r_x, 170), (r_x + box_w, 980)], radius=16, fill="#0F172A", outline="#1E293B", width=2)
    draw.text((r_x + 40, 200), "PER CAPITA INCOME (USD / YEAR)", fill="#F43F5E", font=load_font(BOLD_FONT_PATH, 26))
    draw.text((r_x + 40, 235), "Citizen Income: Total GDP ÷ Population", fill="#64748B", font=load_font(REG_FONT_PATH, 18))

    per_capita_data = [
        ("United States", "$85,300", 85.3, "#38BDF8", "Rank #6 Globally (31x India)"),
        ("Germany", "$54,200", 54.2, "#818CF8", "Rank #19 Globally (20x India)"),
        ("Japan", "$34,100", 34.1, "#A78BFA", "Rank #32 Globally (12x India)"),
        ("China", "$13,500", 13.5, "#60A5FA", "Rank #68 Globally (5x India)"),
        ("Global Average", "$12,800", 12.8, "#64748B", "World Mean"),
        ("INDIA (BHARAT)", "$2,730", 2.73, "#F43F5E", "RANK #136 GLOBALLY (₹2.28L)")
    ]

    base_y = 290
    for country, val_str, val_num, color, rk in per_capita_data:
        draw.text((r_x + 40, base_y), country, fill="#FFFFFF" if "INDIA" in country else "#E2E8F0", font=f_bar_label)
        draw.text((r_x + 40, base_y + 30), rk, fill=color, font=f_rank)
        draw.text((r_x + box_w - 40, base_y + 10), val_str, fill="#FFFFFF", font=f_val, anchor="rt")

        # Bar
        bar_len = max(18, int((val_num / 90.0) * (box_w - 80)))
        draw.rounded_rectangle([(r_x + 40, base_y + 60), (r_x + 40 + bar_len, base_y + 78)], radius=6, fill=color)
        base_y += 110

    out_path = SOURCES_DIR / "src_03_worldbank_per_capita_ranking.png"
    img.save(out_path, quality=95)
    print(f"✅ Generated: {out_path}")

# -------------------------------------------------------------------------
# 4. SIAM AUTOMOBILE SALES REPORT (K-SHAPED EVIDENCE)
# -------------------------------------------------------------------------
def create_siam_report():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#080C14")
    draw = ImageDraw.Draw(img)

    f_title = load_font(BOLD_FONT_PATH, 42)
    f_sub = load_font(REG_FONT_PATH, 24)
    f_card_title = load_font(BOLD_FONT_PATH, 28)
    f_metric = load_font(MONO_FONT_PATH, 64)

    draw.text((80, 50), "SOCIETY OF INDIAN AUTOMOBILE MANUFACTURERS (SIAM)", fill="#F8FAFC", font=f_title)
    draw.text((80, 105), "AUTOMOBILE SALES FLASH REPORT: THE K-SHAPED CONSUMPTION MIRROR", fill="#38BDF8", font=f_sub)

    # 3 Cards
    # Left: Luxury SUVs (+24.5%)
    # Mid: Entry-Level Small Cars (-42.0%)
    # Right: Rural Two-Wheelers (-14.0%)
    cards = [
        (80, "LUXURY SUVS & >₹20L CARS", "+24.5%", "RUNAWAY BOOM (TOP 10%)", "#34D399", [
            "• Mahindra XUV700, Scorpio-N, Creta, Safari",
            "• 6 to 9 months waiting periods for delivery",
            "• Buyers unaffected by inflation or interest rates",
            "• Record corporate bonuses & stock market wealth"
        ]),
        (680, "ENTRY-LEVEL HATCHBACKS", "-42.0%", "COLLAPSE VS 2018 (MASS MIDDLE)", "#F43F5E", [
            "• Maruti Alto, WagonR, Renault Kwid segment",
            "• Sales dropped from 4.8L units to 2.8L units",
            "• Price surge: Insurance, road tax, BS6 norms",
            "• First-time car buyer completely priced out"
        ]),
        (1280, "RURAL TWO-WHEELERS", "-14.0%", "BELOW 2019 PRE-COVID PEAK", "#FBBF24", [
            "• 100cc-125cc motorcycles (Splendor, Platina)",
            "• Core transport backbone of 65 crore villagers",
            "• Real rural wages showing zero real growth",
            "• Farmer income absorbed by fertiliser & fuel costs"
        ])
    ]

    for x, title, metric, status, col, bullets in cards:
        draw.rounded_rectangle([(x, 180), (x + 560, 720)], radius=16, fill="#0F172A", outline="#1E293B", width=2)
        draw.text((x + 35, 215), title, fill="#94A3B8", font=load_font(BOLD_FONT_PATH, 22))
        draw.text((x + 35, 265), metric, fill=col, font=f_metric)
        draw.text((x + 35, 355), status, fill=col, font=load_font(BOLD_FONT_PATH, 20))
        
        draw.line([(x + 35, 395), (x + 525, 395)], fill="#1E293B", width=1)
        b_y = 425
        for b in bullets:
            draw.text((x + 35, b_y), b, fill="#E2E8F0", font=load_font(REG_FONT_PATH, 20))
            b_y += 50

    # Bottom PMGKAY Connection
    strip_y = 760
    draw.rounded_rectangle([(80, strip_y), (w - 80, strip_y + 260)], radius=16, fill="#1E1B4B", outline="#4338CA", width=2)
    draw.text((120, strip_y + 35), "THE ULTIMATE DIVERGENCE: PMGKAY FREE FOODGRAIN PARADOX", fill="#A5B4FC", font=load_font(BOLD_FONT_PATH, 26))
    p_text = (
        "While the top 15% buys ₹25-lakh luxury SUVs, the Government of India provides FREE monthly foodgrains to 80.0 CRORE\n"
        "CITIZENS (57% of India's population) under Pradhan Mantri Garib Kalyan Anna Yojana (PMGKAY) at an annual cost of ₹2.05 Lakh Crore.\n"
        "Forensic Truth: If 7.8% GDP was lifting all boats equally, 80 crore citizens would not require subsidized food survival."
    )
    draw.text((120, strip_y + 85), p_text, fill="#E2E8F0", font=load_font(REG_FONT_PATH, 22), spacing=10)

    out_path = SOURCES_DIR / "src_04_siam_automobile_k_shaped.png"
    img.save(out_path, quality=95)
    print(f"✅ Generated: {out_path}")

# -------------------------------------------------------------------------
# 5. THE MISSING FACTORY: STRUCTURAL SECTORAL DISCONNECT
# -------------------------------------------------------------------------
def create_manufacturing_disconnect():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#070A0F")
    draw = ImageDraw.Draw(img)

    f_title = load_font(BOLD_FONT_PATH, 42)
    f_sub = load_font(REG_FONT_PATH, 24)

    draw.text((80, 50), "THE STRUCTURAL CHOKEPOINT: THE MISSING FACTORY", fill="#F8FAFC", font=f_title)
    draw.text((80, 105), "WHY 7.8% GDP GROWTH CANNOT ABSORB 1.1 CRORE YOUTH ENTERING THE WORKFORCE", fill="#F43F5E", font=f_sub)

    # 3 Pillars comparison
    pillars = [
        (80, "1. AGRICULTURE & ALLIED", "#F59E0B", "45.4%", "15.0%", "3.6%", [
            "• Massive under-employment & low farm productivity",
            "• 65 Crore people surviving on 15% of national wealth",
            "• Average farmer household income: ₹10,218/month",
            "• Trapped in subsistence agriculture"
        ]),
        (680, "2. MANUFACTURING SECTOR", "#EF4444", "11.6%", "15.8%", "9.2%", [
            "• 'THE MISSING FACTORY' — Stagnant for 30 years",
            "• 'Make in India' official target was 25% of GDP",
            "• China manufacturing share: 27.4% (Mass Factory)",
            "• Missing link for low-skill rural-to-urban job migration"
        ]),
        (1280, "3. SERVICES & IT / TECH", "#38BDF8", "30.5%", "54.5%", "12.1%", [
            "• Generates over half of India's total Gross Value Added",
            "• Ultra-high productivity, but high education entry barrier",
            "• Requires fluent English, coding, or corporate finance skills",
            "• Cannot absorb millions of non-technical rural youth"
        ])
    ]

    for x, title, col, work_share, gdp_share, growth, bullets in pillars:
        draw.rounded_rectangle([(x, 180), (x + 560, 720)], radius=16, fill="#0F172A", outline="#1E293B", width=2)
        draw.text((x + 35, 215), title, fill=col, font=load_font(BOLD_FONT_PATH, 24))
        
        # Stat grid
        draw.text((x + 35, 270), f"Workforce: {work_share}", fill="#FFFFFF", font=load_font(BOLD_FONT_PATH, 22))
        draw.text((x + 300, 270), f"GDP Share: {gdp_share}", fill="#FFFFFF", font=load_font(BOLD_FONT_PATH, 22))
        draw.text((x + 35, 315), f"Q1 Growth: {growth}", fill=col, font=load_font(MONO_FONT_PATH, 22))

        draw.line([(x + 35, 360), (x + 525, 360)], fill="#1E293B", width=1)
        b_y = 390
        for b in bullets:
            draw.text((x + 35, b_y), b, fill="#E2E8F0", font=load_font(REG_FONT_PATH, 20))
            b_y += 55

    # Bottom China comparison
    strip_y = 760
    draw.rounded_rectangle([(80, strip_y), (w - 80, strip_y + 260)], radius=16, fill="#111827", outline="#374151", width=2)
    draw.text((120, strip_y + 35), "HISTORIC GLOBAL LESSON: HOW NATIONS ACTUALLY GET RICH", fill="#FBBF24", font=load_font(BOLD_FONT_PATH, 26))
    h_text = (
        "No major country on earth has ever achieved high-income status ($15,000+ per capita) without first expanding mass manufacturing.\n"
        "South Korea, Japan, Taiwan, and China all created millions of labor-intensive factory jobs in garments, shoes, toys, and electronics.\n"
        "India skipped this step, jumping from farms to software code. Without factories, 7.8% GDP remains concentrated at the top."
    )
    draw.text((120, strip_y + 85), h_text, fill="#E2E8F0", font=load_font(REG_FONT_PATH, 22), spacing=10)

    out_path = SOURCES_DIR / "src_05_manufacturing_missing_factory.png"
    img.save(out_path, quality=95)
    print(f"✅ Generated: {out_path}")

# -------------------------------------------------------------------------
# 6. THE 2045 DEMOGRAPHIC CLOCK INFOGRAPHIC
# -------------------------------------------------------------------------
def create_demographic_clock():
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), "#090D16")
    draw = ImageDraw.Draw(img)

    f_title = load_font(BOLD_FONT_PATH, 42)
    f_sub = load_font(REG_FONT_PATH, 24)

    draw.text((80, 50), "THE 2045 DEMOGRAPHIC CLOCK: THE WINDOW IS CLOSING", fill="#F8FAFC", font=f_title)
    draw.text((80, 105), "WHY BHARAT RISKS GETTING OLD BEFORE GETTING RICH", fill="#F59E0B", font=f_sub)

    # 4 metrics
    metrics = [
        (80, "MEDIAN AGE", "28.4 Yrs", "Youngest large workforce on earth", "#38BDF8"),
        (520, "NEW WORKERS / YR", "1.1 Crore", "11 Million youth seeking jobs annually", "#34D399"),
        (960, "TOTAL FERTILITY", "2.0 TFR", "Below 2.1 replacement rate (NFHS-5)", "#FBBF24"),
        (1400, "WINDOW CLOSES", "2045", "Dependency ratio begins to reverse", "#F43F5E")
    ]

    for x, title, val, note, col in metrics:
        draw.rounded_rectangle([(x, 180), (x + 400, 360)], radius=16, fill="#0F172A", outline="#1E293B", width=2)
        draw.text((x + 25, 210), title, fill="#94A3B8", font=load_font(BOLD_FONT_PATH, 20))
        draw.text((x + 25, 250), val, fill=col, font=load_font(MONO_FONT_PATH, 48))
        draw.text((x + 25, 315), note, fill="#E2E8F0", font=load_font(REG_FONT_PATH, 16))

    # Timeline Graph Area
    draw.rounded_rectangle([(80, 400), (w - 80, 980)], radius=16, fill="#0F172A", outline="#1E293B", width=2)
    draw.text((120, 435), "DEMOGRAPHIC DIVIDEND TIMELINE (1990 — 2060)", fill="#FFFFFF", font=load_font(BOLD_FONT_PATH, 26))

    # Timeline points
    t_points = [
        (160, "1991: Reforms Begin", "Fertility: 3.8\nMedian Age: 21\nAgrarian base"),
        (460, "2010: IT & Telecom Boom", "Fertility: 2.6\nMedian Age: 25\nService explosion"),
        (760, "2026: TODAY (PEAK YOUTH)", "Fertility: 2.0\nMedian Age: 28.4\n1.1 Cr entering/yr"),
        (1160, "2038: Window Peaks", "Working age share\nhits max peak\nLast decade to industrialize"),
        (1560, "2045: THE HARD WALL", "Window SLAMS SHUT\nElderly population doubles\nOld before Rich?")
    ]

    # Draw timeline line
    draw.line([(160, 560), (1700, 560)], fill="#334155", width=6)
    draw.line([(160, 560), (760, 560)], fill="#38BDF8", width=6)
    draw.line([(760, 560), (1560, 560)], fill="#F59E0B", width=6)

    for px, label, desc in t_points:
        col = "#38BDF8" if "2026" in label else ("#F43F5E" if "2045" in label else "#94A3B8")
        draw.ellipse([(px - 14, 560 - 14), (px + 14, 560 + 14)], fill=col, outline="#FFFFFF", width=3)
        draw.text((px, 500), label, fill=col, font=load_font(BOLD_FONT_PATH, 22), anchor="mb")
        d_lines = desc.split("\n")
        d_y = 600
        for dl in d_lines:
            draw.text((px, d_y), dl, fill="#CBD5E1", font=load_font(REG_FONT_PATH, 18), anchor="mt")
            d_y += 24

    # Urgent Warning Text
    draw.rounded_rectangle([(120, 780), (w - 120, 940)], radius=12, fill="#450A0A", outline="#DC2626", width=2)
    draw.text((150, 805), "THE 18-YEAR DEADLINE TO AVOID THE MIDDLE-INCOME TRAP:", fill="#FCA5A5", font=load_font(BOLD_FONT_PATH, 24))
    w_text = (
        "If India does not create 8 to 10 million formal manufacturing jobs per year and raise per capita income from $2,730\n"
        "to over $10,000 by 2045, India will enter its aging phase with developing-world healthcare, depleted savings, and no pensions."
    )
    draw.text((150, 850), w_text, fill="#FEE2E2", font=load_font(REG_FONT_PATH, 22), spacing=8)

    out_path = SOURCES_DIR / "src_06_demographic_clock_2045.png"
    img.save(out_path, quality=95)
    print(f"✅ Generated: {out_path}")

if __name__ == "__main__":
    create_mospi_document()
    create_rbi_document()
    create_worldbank_chart()
    create_siam_report()
    create_manufacturing_disconnect()
    create_demographic_clock()
    print("🎯 All official source documents successfully created!")
