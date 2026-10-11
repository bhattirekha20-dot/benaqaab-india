import os
import sys
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR = Path(__file__).parent
ASSETS_DIR = DIR / "assets"
AI_DIR = ASSETS_DIR / "ai_plates"
AI_DIR.mkdir(parents=True, exist_ok=True)

# Font picker
font_paths = [
    Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/Anton.ttf"),
    Path("c:/Windows/Fonts/calibrib.ttf"),
    Path("c:/Windows/Fonts/arialbd.ttf")
]
body_paths = [
    Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/Inter.ttf"),
    Path("c:/Windows/Fonts/calibri.ttf"),
    Path("c:/Windows/Fonts/arial.ttf")
]
mono_paths = [
    Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/JetBrainsMono.ttf"),
    Path("c:/Windows/Fonts/consola.ttf")
]

def pick_font(plist):
    for p in plist:
        if p.exists(): return str(p)
    return "arial.ttf"

HEAD_FONT = pick_font(font_paths)
BODY_FONT = pick_font(body_paths)
MONO_FONT = pick_font(mono_paths)

def get_font(path, sz):
    try:
        return ImageFont.truetype(path, sz)
    except Exception:
        return ImageFont.load_default()

# Cinematic Palette Generator
def make_cinematic_plate(filename, title, category, stat_badge, prompt_desc, color_scheme, draw_custom_fn=None):
    w, h = 1920, 1080
    img = Image.new("RGB", (w, h), color_scheme["bg_base"])
    draw = ImageDraw.Draw(img)

    # 1. Volumetric ambient glow / mesh gradient
    center_col = color_scheme.get("glow_color", (30, 45, 80))
    glow_r = color_scheme.get("glow_radius", 650)
    glow_cx = color_scheme.get("glow_cx", 960)
    glow_cy = color_scheme.get("glow_cy", 540)
    
    for r in range(glow_r, 50, -40):
        intensity = (1.0 - r / glow_r) * color_scheme.get("glow_intensity", 0.45)
        cr = int(color_scheme["bg_base"][0] + (center_col[0] - color_scheme["bg_base"][0]) * intensity)
        cg = int(color_scheme["bg_base"][1] + (center_col[1] - color_scheme["bg_base"][1]) * intensity)
        cb = int(color_scheme["bg_base"][2] + (center_col[2] - color_scheme["bg_base"][2]) * intensity)
        draw.ellipse([(glow_cx - r, glow_cy - r), (glow_cx + r, glow_cy + r)], fill=(cr, cg, cb))

    # 2. Geometric architectural & perspective grid lines
    grid_col = color_scheme.get("grid_color", (25, 35, 55))
    if color_scheme.get("has_grid", True):
        for y in range(0, h, 80):
            draw.line([(0, y), (w, y)], fill=grid_col, width=1)
        for x in range(0, w, 120):
            draw.line([(x, 0), (x, h)], fill=grid_col, width=1)

    # 3. Custom illustrative graphics hook
    if draw_custom_fn:
        draw_custom_fn(draw, w, h, color_scheme)

    # 4. Cinematic Dark Vignette
    for r in range(400, 1100, 50):
        alpha = int(120 * ((r - 400) / 700))
        # Draw dark outer borders
        pass



    # 6. Hero Cinematic Headline Card (Lower Third Glassmorphism)
    c_y = h - 230
    draw.rounded_rectangle([(70, c_y), (w - 70, h - 70)], radius=18, fill=(8, 12, 20), outline=(255, 255, 255, 35), width=1)
    draw.rectangle([(70, c_y), (82, h - 70)], fill=color_scheme.get("accent_color", "#38BDF8"))
    
    draw.text((110, c_y + 35), title.upper(), fill="#FFFFFF", font=get_font(HEAD_FONT, 38))
    draw.text((110, c_y + 88), prompt_desc, fill="#94A3B8", font=get_font(BODY_FONT, 20))

    # Watermark
    draw.text((w - 110, c_y + 40), "BENAQAAB FORENSIC VISUALS", fill="#475569", font=get_font(MONO_FONT, 14), anchor="rt")

    out_file = AI_DIR / filename
    img.save(out_file, quality=95)
    return out_file

# --- CUSTOM ILLUSTRATIVE GRAPHIC HOOKS ---

def draw_stock_bull(draw, w, h, col):
    # Dramatic financial trendlines & Candlesticks
    coords = [(150, 700), (350, 620), (550, 680), (800, 480), (1050, 520), (1300, 360), (1550, 410), (1750, 240)]
    for i in range(len(coords)-1):
        draw.line([coords[i], coords[i+1]], fill="#34D399", width=6)
    for x, y in coords:
        draw.ellipse([(x-8, y-8), (x+8, y+8)], fill="#FFFFFF", outline="#10B981", width=3)
        draw.text((x, y-25), f"+{(1800-y)//15}%", fill="#34D399", font=get_font(MONO_FONT, 16), anchor="mb")

def draw_parliament_dome(draw, w, h, col):
    # Majestic architectural dome silhouette with tricolor ambient backlighting
    cx, cy = 960, 480
    draw.arc([(cx-320, cy-220), (cx+320, cy+420)], start=180, end=360, fill="#F59E0B", width=6)
    draw.line([(cx-340, cy+100), (cx+340, cy+100)], fill="#FFFFFF", width=4)
    # Pillars
    for px in range(cx-300, cx+320, 50):
        draw.line([(px, cy+100), (px, cy+280)], fill="#38BDF8", width=3)

def draw_k_shape_split(draw, w, h, col):
    # Huge glowing 'K' divergence
    cx, cy = 960, 460
    # Stem
    draw.line([(cx-180, cy-220), (cx-180, cy+220)], fill="#38BDF8", width=14)
    # Upper branch (+24.5% Luxury)
    draw.line([(cx-180, cy), (cx+220, cy-200)], fill="#34D399", width=12)
    draw.text((cx+240, cy-210), "TOP 10% ASSET BOOM (+24.5%)", fill="#34D399", font=get_font(HEAD_FONT, 28), anchor="lm")
    # Lower branch (-42.0% Mass Middle)
    draw.line([(cx-180, cy), (cx+220, cy+200)], fill="#F43F5E", width=12)
    draw.text((cx+240, cy+210), "BOTTOM 60% REAL WAGE SQUEEZE (-42%)", fill="#F43F5E", font=get_font(HEAD_FONT, 28), anchor="lm")

def draw_luxury_suv(draw, w, h, col):
    # Sleek dark silhouette of high-end vehicle with glowing matrix headlights
    draw.ellipse([(960-350, 460-60), (960+350, 460+60)], fill=(20, 30, 45))
    # Headlight lasers
    draw.line([(720, 450), (300, 520)], fill="#38BDF8", width=6)
    draw.line([(1200, 450), (1620, 520)], fill="#38BDF8", width=6)
    draw.text((960, 400), "LUXURY SUV & PENTHOUSE CONSUMPTION BOOM", fill="#FBBF24", font=get_font(HEAD_FONT, 34), anchor="mm")

def draw_rural_tractor(draw, w, h, col):
    # Arid agricultural soil lines & dry horizon
    for y in range(440, 750, 35):
        draw.line([(100, y), (1820, y)], fill=(65, 45, 25), width=2)
    draw.text((960, 400), "45.4% WORKFORCE GENERATING 15% GDP", fill="#F59E0B", font=get_font(HEAD_FONT, 36), anchor="mm")

def draw_broken_piggy_bank(draw, w, h, col):
    # Cracked vault / savings meter falling
    draw.arc([(960-180, 420-180), (960+180, 420+180)], start=30, end=330, fill="#F43F5E", width=10)
    # Crack zigzag
    draw.line([(960, 300), (960-20, 360)], fill="#FFFFFF", width=4)
    draw.line([(960-20, 360), (960+25, 420)], fill="#FFFFFF", width=4)
    draw.line([(960+25, 420), (960-15, 480)], fill="#FFFFFF", width=4)
    draw.text((960, 530), "NET FINANCIAL SAVINGS: 5.3% OF GDP (50-YEAR LOW)", fill="#F43F5E", font=get_font(HEAD_FONT, 32), anchor="mt")

def draw_credit_card_overdue(draw, w, h, col):
    # Floating credit card with high limit alert
    draw.rounded_rectangle([(700, 300), (1220, 580)], radius=20, fill=(20, 25, 40), outline="#FBBF24", width=3)
    draw.rectangle([(700, 350), (1220, 400)], fill="#0F172A")
    draw.text((740, 480), "UNSECURED CONSUMPTION DEBT: 58.2%", fill="#F8FAFC", font=get_font(MONO_FONT, 20))
    draw.text((740, 520), "HOUSEHOLD DEBT TO GDP: 45.8% PEAK", fill="#F43F5E", font=get_font(HEAD_FONT, 24))

def draw_automated_fab(draw, w, h, col):
    # High-tech robotic arms & silicon wafer lines
    cx, cy = 960, 440
    for ang in range(0, 360, 45):
        rad = math.radians(ang)
        x2 = cx + int(240 * math.cos(rad))
        y2 = cy + int(240 * math.sin(rad))
        draw.line([(cx, cy), (x2, y2)], fill="#0284C7", width=2)
    draw.ellipse([(cx-120, cy-120), (cx+120, cy+120)], fill=(10, 25, 45), outline="#38BDF8", width=4)
    draw.text((cx, cy), "MANUFACTURING: 15.8% (CHINA: 27.4%)", fill="#38BDF8", font=get_font(HEAD_FONT, 28), anchor="mm")

def draw_youth_clock(draw, w, h, col):
    # Clock with 2045 deadline
    cx, cy = 960, 440
    draw.ellipse([(cx-200, cy-200), (cx+200, cy+200)], fill=(15, 20, 35), outline="#F59E0B", width=6)
    # Hands pointing to 2045
    draw.line([(cx, cy), (cx, cy-140)], fill="#FFFFFF", width=6)
    draw.line([(cx, cy), (cx+110, cy-60)], fill="#F43F5E", width=6)
    draw.text((cx, cy+70), "2045", fill="#F59E0B", font=get_font(HEAD_FONT, 44), anchor="mm")
    draw.text((cx, cy+120), "DEMOGRAPHIC DIVIDEND CLOSES", fill="#94A3B8", font=get_font(BODY_FONT, 18), anchor="mm")

# Master List of Cinematic Plates to generate
PLATES = [
    {
        "filename": "ai_01_global_gdp_celebration_bull.jpg",
        "title": "The $3.94 Trillion Headline Celebration",
        "category": "Chapter 1: The Global Headline",
        "stat_badge": "REAL GDP: 7.8% | GVA: 8.2%",
        "prompt_desc": "Dalal Street Bombay Stock Exchange bronze charging bull bathed in vibrant green laser lighting and global financial tickers.",
        "color_scheme": {"bg_base": (7, 10, 16), "glow_color": (16, 185, 129), "accent_color": "#34D399"},
        "fn": draw_stock_bull
    },
    {
        "filename": "ai_02_parliament_cabinet_national_accounts.jpg",
        "title": "MoSPI National Accounts Formulation",
        "category": "Chapter 1: The Official Series",
        "stat_badge": "BASE YEAR: 2022-23 SERIES",
        "prompt_desc": "Architectural silhouette of Indian Parliament building with digital economic stream and national ledger data.",
        "color_scheme": {"bg_base": (8, 12, 20), "glow_color": (56, 189, 248), "accent_color": "#38BDF8"},
        "fn": draw_parliament_dome
    },
    {
        "filename": "ai_03_middle_class_kitchen_table_inflation.jpg",
        "title": "The Household Living Cost Reality",
        "category": "Chapter 1: Everyday Reality",
        "stat_badge": "CONSUMER DIVERGENCE",
        "prompt_desc": "Indian middle-class dining table with electric bills, grocery receipts, and monthly expense calculation notepad.",
        "color_scheme": {"bg_base": (12, 10, 14), "glow_color": (245, 158, 11), "accent_color": "#FBBF24"},
        "fn": draw_broken_piggy_bank
    },
    {
        "filename": "ai_04_crowded_mumbai_commuter_train.jpg",
        "title": "143 Crore Citizens: The Population Multiplier",
        "category": "Chapter 2: The Per-Capita Math",
        "stat_badge": "TOTAL GDP #5 vs PER-CAPITA #136",
        "prompt_desc": "Cinematic high-contrast view of thousands of daily commuters at Mumbai CST station moving in synchronous stream.",
        "color_scheme": {"bg_base": (9, 11, 18), "glow_color": (99, 102, 241), "accent_color": "#818CF8"},
        "fn": draw_stock_bull
    },
    {
        "filename": "ai_05_global_superpowers_per_capita_towers.jpg",
        "title": "The 31x Wealth Disconnect: US & China",
        "category": "Chapter 2: Global Benchmarks",
        "stat_badge": "USA: $85,000 | INDIA: $2,730",
        "prompt_desc": "Manhattan financial skyscraper towers compared side-by-side with global emerging market income bars.",
        "color_scheme": {"bg_base": (6, 9, 15), "glow_color": (56, 189, 248), "accent_color": "#38BDF8"},
        "fn": draw_parliament_dome
    },
    {
        "filename": "ai_06_k_shaped_economic_divergence.jpg",
        "title": "The Anatomy of K-Shaped Recovery",
        "category": "Chapter 3: The K-Shaped Divide",
        "stat_badge": "DIVERGING ECONOMIC REALITIES",
        "prompt_desc": "Massive forensic vector graphic showing the upper arm (+24.5% asset boom) and lower arm (-42% wage squeeze).",
        "color_scheme": {"bg_base": (10, 10, 18), "glow_color": (244, 63, 94), "accent_color": "#F43F5E"},
        "fn": draw_k_shape_split
    },
    {
        "filename": "ai_07_luxury_suv_gurugram_cybercity.jpg",
        "title": "The Upper Arm: Luxury SUVs & Penthouses",
        "category": "Chapter 3: Premium Boom",
        "stat_badge": "LUXURY SUVS: +24.5% YoY",
        "prompt_desc": "Gleaming luxury SUV parked outside glass skyscraper in Gurugram CyberCity with modern corporate illumination.",
        "color_scheme": {"bg_base": (8, 12, 20), "glow_color": (251, 191, 36), "accent_color": "#FBBF24"},
        "fn": draw_luxury_suv
    },
    {
        "filename": "ai_08_rural_village_stagnant_two_wheelers.jpg",
        "title": "The Lower Arm: Small Cars & Two-Wheelers",
        "category": "Chapter 3: Mass Middle Collapse",
        "stat_badge": "SMALL CARS: -42% VS 2018",
        "prompt_desc": "Dusty rural tea stall with entry-level 100cc motorcycle standing idle in arid agricultural countryside.",
        "color_scheme": {"bg_base": (14, 11, 10), "glow_color": (239, 68, 68), "accent_color": "#EF4444"},
        "fn": draw_rural_tractor
    },
    {
        "filename": "ai_09_pmgkay_free_ration_distribution.jpg",
        "title": "80 Crore Citizens on Free Foodgrains",
        "category": "Chapter 3: Food Security Reality",
        "stat_badge": "57% OF INDIA ON PMGKAY",
        "prompt_desc": "Government fair-price ration shop with 80 crore beneficiaries lining up for essential foodgrain sacks.",
        "color_scheme": {"bg_base": (10, 10, 14), "glow_color": (245, 158, 11), "accent_color": "#F59E0B"},
        "fn": draw_k_shape_split
    },
    {
        "filename": "ai_10_rbi_financial_stability_vault.jpg",
        "title": "RBI Bulletin: Net Financial Savings Crash",
        "category": "Chapter 4: Household Balance Sheet",
        "stat_badge": "NET SAVINGS: 5.3% OF GDP",
        "prompt_desc": "Reserve Bank of India Mumbai headquarters façade with ominous descending savings curve and cracked piggy bank.",
        "color_scheme": {"bg_base": (12, 8, 12), "glow_color": (244, 63, 94), "accent_color": "#F43F5E"},
        "fn": draw_broken_piggy_bank
    },
    {
        "filename": "ai_11_debt_financed_consumption_credit_card.jpg",
        "title": "Unsecured Debt-Driven Consumption",
        "category": "Chapter 4: Debt Spike",
        "stat_badge": "HOUSEHOLD DEBT: 45.8% OF GDP",
        "prompt_desc": "Smartphone displaying personal loans, BNPL apps, and credit card notifications fueling urban consumption.",
        "color_scheme": {"bg_base": (8, 10, 18), "glow_color": (56, 189, 248), "accent_color": "#38BDF8"},
        "fn": draw_credit_card_overdue
    },
    {
        "filename": "ai_12_the_missing_factory_shenzhen_comparison.jpg",
        "title": "The Missing Factory: Manufacturing Deficit",
        "category": "Chapter 5: Industrial Chokepoint",
        "stat_badge": "MFG SHARE: 15.8% (TARGET 25%)",
        "prompt_desc": "Automated high-tech industrial assembly line with robotic arms contrasted against vacant factory floors.",
        "color_scheme": {"bg_base": (7, 10, 16), "glow_color": (14, 165, 233), "accent_color": "#0EA5E9"},
        "fn": draw_automated_fab
    },
    {
        "filename": "ai_13_agriculture_45pct_workforce_chokepoint.jpg",
        "title": "45.4% Workforce Trapped in Farming",
        "category": "Chapter 5: Agriculture Paradox",
        "stat_badge": "AGRI GVA: 15.0% | WORKERS: 45.4%",
        "prompt_desc": "Vast agricultural plains with hundreds of manual farm laborers working under harsh sun for subsistence wages.",
        "color_scheme": {"bg_base": (12, 10, 8), "glow_color": (245, 158, 11), "accent_color": "#F59E0B"},
        "fn": draw_rural_tractor
    },
    {
        "filename": "ai_14_youth_demographic_clock_2045.jpg",
        "title": "The 2045 Demographic Clock Deadline",
        "category": "Chapter 6: Demographic Window",
        "stat_badge": "1.1 CRORE YOUTH ENTERING / YR",
        "prompt_desc": "Dramatic giant stopwatch counting down to 2045 behind thousands of ambitious young Indian university graduates.",
        "color_scheme": {"bg_base": (10, 10, 16), "glow_color": (239, 68, 68), "accent_color": "#EF4444"},
        "fn": draw_youth_clock
    },
    {
        "filename": "ai_15_vocational_skilling_and_reforms_future.jpg",
        "title": "The 4 Urgent Structural Reforms",
        "category": "Chapter 7: The Road Ahead",
        "stat_badge": "CITIZEN PROSPERITY ROADMAP",
        "prompt_desc": "High-tech vocational precision engineering laboratory with young Indian workers mastering semiconductor tools.",
        "color_scheme": {"bg_base": (7, 11, 18), "glow_color": (16, 185, 129), "accent_color": "#10B981"},
        "fn": draw_automated_fab
    },
    {
        "filename": "ai_16_benaqaab_final_verdict_stamp.jpg",
        "title": "Final Forensic Verdict: Reality Unveiled",
        "category": "Chapter 7: Closing Verdict",
        "stat_badge": "SACH · SABOOT · BEBAK",
        "prompt_desc": "High-impact forensic stamp slamming down on national accounts with official Benaqaab India seal and tricolor glow.",
        "color_scheme": {"bg_base": (9, 8, 14), "glow_color": (244, 63, 94), "accent_color": "#F43F5E"},
        "fn": draw_k_shape_split
    }
]

def generate_all():
    print(f"🎨 Generating {len(PLATES)} cinematic composite visual plates...")
    for p in PLATES:
        out = make_cinematic_plate(
            p["filename"],
            p["title"],
            p["category"],
            p["stat_badge"],
            p["prompt_desc"],
            p["color_scheme"],
            p.get("fn")
        )
        print(f"✅ Created: {out.name}")

if __name__ == "__main__":
    generate_all()
    print("🚀 All cinematic plates generated successfully!")
