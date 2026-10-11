import os
import sys
import urllib.request
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PROJECT_DIR = Path(__file__).resolve().parent
ASSETS_DIR = PROJECT_DIR / "assets"
VISUALS_DIR = ASSETS_DIR / "visuals"
RAW_DIR = ASSETS_DIR / "real_sources"
RAW_DIR.mkdir(parents=True, exist_ok=True)
VISUALS_DIR.mkdir(parents=True, exist_ok=True)

WORKSPACE = PROJECT_DIR.parent.parent
FONTS_DIR = WORKSPACE / "brand" / "fonts"

FONT_INTER = str(FONTS_DIR / "Inter.ttf") if (FONTS_DIR / "Inter.ttf").exists() else None
FONT_MONO = str(FONTS_DIR / "JetBrainsMono.ttf") if (FONTS_DIR / "JetBrainsMono.ttf").exists() else None
FONT_ANTON = str(FONTS_DIR / "Anton.ttf") if (FONTS_DIR / "Anton.ttf").exists() else None
FONT_SPACE = str(FONTS_DIR / "SpaceGrotesk.ttf") if (FONTS_DIR / "SpaceGrotesk.ttf").exists() else None

def get_font(path, size):
    try:
        if path and os.path.exists(path):
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default()

W, H = 1080, 1920

# High-resolution authentic photographic plates from curated Unsplash editorial collections
PHOTO_URLS = {
    "atm_card": "https://images.unsplash.com/photo-1559526324-4b87b5e36e44?w=1080&q=85", # Cash / card ATM
    "fingerprint_macro": "https://images.unsplash.com/photo-1589829545856-d10d557cf95f?w=1080&q=85", # Legal gavel & evidence
    "cyber_dark": "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=1080&q=85", # Matrix code / cyber
    "cash_rupees": "https://images.unsplash.com/photo-1607604276583-eef5d076aa5f?w=1080&q=85", # Cash stacks money
    "police_evidence": "https://images.unsplash.com/photo-1589994965851-a8f479c573a9?w=1080&q=85", # Police tape / investigation
    "legal_document": "https://images.unsplash.com/photo-1450133064473-71024230f91b?w=1080&q=85", # Stamp deed paper
    "server_rack": "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=1080&q=85", # Server infrastructure
    "smartphone_shield": "https://images.unsplash.com/photo-1563986768609-322da13575f3?w=1080&q=85", # Mobile security lock
    "pos_machine": "https://images.unsplash.com/photo-1556742049-0a67e557229f?w=1080&q=85", # Point of sale POS
    "hacker_setup": "https://images.unsplash.com/photo-1563089145-599997674d42?w=1080&q=85" # Cyber lab lighting
}

def download_source_photos():
    print("📥 Downloading real editorial source photographs...")
    for key, url in PHOTO_URLS.items():
        out_file = RAW_DIR / f"{key}.jpg"
        if out_file.exists() and out_file.stat().st_size > 10000:
            print(f"  ✓ Cached: {key}.jpg")
            continue
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
            with urllib.request.urlopen(req, timeout=15) as resp:
                data = resp.read()
                with open(out_file, 'wb') as f:
                    f.write(data)
            print(f"  ✓ Downloaded: {key}.jpg ({len(data)} bytes)")
        except Exception as e:
            print(f"  ⚠ Failed downloading {key}: {e}")

def create_photographic_base(photo_key, tint_color=(7, 9, 14), brightness=0.45, contrast=1.2):
    photo_path = RAW_DIR / f"{photo_key}.jpg"
    if photo_path.exists():
        im = Image.open(photo_path).convert("RGB")
        # Cover 1080x1920
        iw, ih = im.size
        scale = max(W / iw, H / ih)
        nw, nh = int(iw * scale), int(ih * scale)
        im = im.resize((nw, nh), Image.Resampling.LANCZOS)
        # Crop to center
        left = (nw - W) // 2
        top = (nh - H) // 2
        im = im.crop((left, top, left + W, top + H))
        
        # Adjust brightness & contrast
        im = ImageEnhance.Brightness(im).enhance(brightness)
        im = ImageEnhance.Contrast(im).enhance(contrast)
        
        # Dark color tint overlay
        tint = Image.new("RGB", (W, H), tint_color)
        im = Image.blend(im, tint, 0.45)
        return im
    else:
        # Fallback dark base
        im = Image.new("RGB", (W, H), tint_color)
        return im

def add_scanlines(img, opacity=12):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for y in range(0, H, 6):
        d.line([(0, y), (W, y)], fill=(0, 0, 0, opacity))
    img.paste(overlay, (0, 0), overlay)
    return img

def add_glow_orb(img, cx, cy, radius, color_rgb, intensity=0.45):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -15):
        alpha = int((1.0 - (r / radius)) * intensity * 255)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(color_rgb[0], color_rgb[1], color_rgb[2], alpha))
    overlay = overlay.filter(ImageFilter.GaussianBlur(16))
    img.paste(overlay, (0, 0), overlay)
    return img

def draw_header_tag(draw, text, y=240, accent_color=(251, 191, 36)):
    font = get_font(FONT_MONO, 28)
    draw.rounded_rectangle([60, y, W - 60, y + 54], radius=12, fill=(15, 23, 42), outline=accent_color, width=2)
    draw.text((80, y + 12), text, font=font, fill=accent_color)

def draw_top_left_brand(draw):
    pill_box = [60, 90, 420, 160]
    draw.rounded_rectangle(pill_box, radius=35, fill=(10, 14, 23), outline=(251, 191, 36), width=2)
    draw.ellipse([70, 100, 120, 150], fill=(244, 63, 94))
    font_bold = get_font(FONT_ANTON, 26)
    draw.text((135, 104), "BENAQAAB INDIA", font=font_bold, fill=(255, 255, 255))
    font_sub = get_font(FONT_MONO, 14)
    draw.text((135, 134), "SACH · SABOOT · BEBAK", font=font_sub, fill=(251, 191, 36))

def build_all_composites():
    print("🎬 Generating full-bleed photographic cinema composites for all 30 beats...")
    
    OBSIDIAN = (7, 9, 14)
    CRIMSON = (244, 63, 94)
    AMBER = (251, 191, 36)
    SKY = (56, 189, 248)
    EMERALD = (52, 211, 153)
    WHITE = (255, 255, 255)
    MUTED = (148, 163, 184)

    # BEAT 01: Hook Frame 0 - A/C Debited Alert (Real ATM photo background)
    b1 = create_photographic_base("atm_card", tint_color=(35, 10, 18), brightness=0.45)
    add_glow_orb(b1, 540, 960, 520, CRIMSON, 0.45)
    d1 = ImageDraw.Draw(b1)
    draw_top_left_brand(d1)
    draw_header_tag(d1, "CRITICAL BANKING ALERT", 260, CRIMSON)
    d1.rounded_rectangle([60, 360, W-60, 1080], radius=28, fill=(10, 14, 24), outline=(244, 63, 94), width=4)
    d1.text((100, 420), "A/C DEBITED: ₹10,000.00", font=get_font(FONT_ANTON, 72), fill=CRIMSON)
    d1.text((100, 520), "AePS CASH WITHDRAWAL SUCCESSFUL", font=get_font(FONT_SPACE, 36), fill=WHITE)
    d1.line([(100, 590), (W-100, 590)], fill=(244, 63, 94), width=2)
    d1.text((100, 640), "TIME: 03:14 AM (MIDNIGHT)", font=get_font(FONT_MONO, 32), fill=MUTED)
    d1.text((100, 710), "LOCATION: MICRO-ATM #9412 (BIHAR)", font=get_font(FONT_MONO, 32), fill=MUTED)
    d1.text((100, 780), "AUTHENTICATION: BIOMETRIC THUMBPRINT", font=get_font(FONT_MONO, 32), fill=AMBER)
    d1.rounded_rectangle([100, 890, W-100, 1010], radius=16, fill=(244, 63, 94), outline=WHITE, width=2)
    d1.text((140, 925), "ZERO OTP SENT · VICTIM WAS ASLEEP", font=get_font(FONT_ANTON, 40), fill=WHITE)
    b1 = add_scanlines(b1)
    b1.save(VISUALS_DIR / "beat_01.jpg", quality=95)

    # BEAT 02: Zero OTP · Zero ATM Card (Real ATM Card photo background)
    b2 = create_photographic_base("atm_card", tint_color=(15, 23, 42), brightness=0.4)
    add_glow_orb(b2, 540, 800, 420, AMBER, 0.3)
    d2 = ImageDraw.Draw(b2)
    draw_top_left_brand(d2)
    draw_header_tag(d2, "THE ZERO-AUTHENTICATION MYSTERY", 260, AMBER)
    d2.text((80, 380), "HOW WAS IT SUCKED OUT?", font=get_font(FONT_ANTON, 68), fill=WHITE)
    cards = [
        ("❌ NO OTP RECEIVED", "Bank never triggered an SMS code", CRIMSON),
        ("❌ NO ATM CARD SWIPED", "Victim holds debit card in wallet", CRIMSON),
        ("❌ NO BANK VISIT", "Victim was 1,200 km away", CRIMSON)
    ]
    for i, (title, desc, col) in enumerate(cards):
        cy = 540 + i * 220
        d2.rounded_rectangle([60, cy, W-60, cy+180], radius=20, fill=(10, 16, 28), outline=col, width=2)
        d2.text((100, cy+30), title, font=get_font(FONT_ANTON, 46), fill=col)
        d2.text((100, cy+100), desc, font=get_font(FONT_INTER, 28), fill=MUTED)
    b2 = add_scanlines(b2)
    b2.save(VISUALS_DIR / "beat_02.jpg", quality=95)

    # BEAT 03: Cash Gone (Real Cash Rupees background)
    b3 = create_photographic_base("cash_rupees", tint_color=(40, 10, 18), brightness=0.45)
    add_glow_orb(b3, 540, 900, 480, CRIMSON, 0.45)
    d3 = ImageDraw.Draw(b3)
    draw_top_left_brand(d3)
    draw_header_tag(d3, "FINANCIAL EXTRACTION LEDGER", 260, CRIMSON)
    d3.text((80, 380), "₹10,000 SAAF!", font=get_font(FONT_ANTON, 96), fill=CRIMSON)
    d3.text((80, 500), "MAXIMUM PER-TRANSACTION LIMIT DRAINED", font=get_font(FONT_SPACE, 34), fill=AMBER)
    d3.rounded_rectangle([60, 600, W-60, 1300], radius=24, fill=(10, 14, 23), outline=CRIMSON, width=3)
    d3.text((100, 660), "TRANSACTION RECEIPT", font=get_font(FONT_MONO, 32), fill=MUTED)
    d3.text((100, 740), "AMOUNT: ₹10,000.00", font=get_font(FONT_ANTON, 64), fill=WHITE)
    d3.text((100, 840), "SYSTEM: AePS (NPCI SWITCH)", font=get_font(FONT_MONO, 32), fill=SKY)
    d3.text((100, 920), "UID: XXXXXXXX9012 (MATCHED)", font=get_font(FONT_MONO, 32), fill=EMERALD)
    d3.text((100, 1000), "TERMINAL: BANK MITRA POS", font=get_font(FONT_MONO, 32), fill=MUTED)
    d3.text((100, 1080), "FEE: ₹0.00 | STATUS: SETTLED", font=get_font(FONT_MONO, 32), fill=MUTED)
    d3.rounded_rectangle([100, 1160, W-100, 1250], radius=12, fill=(244, 63, 94), outline=WHITE, width=2)
    d3.text((160, 1185), "ACCOUNT BALANCE: ₹14.20", font=get_font(FONT_ANTON, 42), fill=WHITE)
    b3 = add_scanlines(b3)
    b3.save(VISUALS_DIR / "beat_03.jpg", quality=95)

    # BEAT 04: Criminal Clue (Cyber dark setup background)
    b4 = create_photographic_base("cyber_dark", tint_color=(12, 18, 30), brightness=0.4)
    add_glow_orb(b4, 540, 850, 420, SKY, 0.35)
    d4 = ImageDraw.Draw(b4)
    draw_top_left_brand(d4)
    draw_header_tag(d4, "THE FORENSIC EVIDENCE", 260, SKY)
    d4.text((80, 380), "CHOR KA ASLI HATHYAR?", font=get_font(FONT_ANTON, 72), fill=WHITE)
    d4.text((80, 480), "NOT A GUN. NOT MALWARE. NOT A PASSWORD.", font=get_font(FONT_SPACE, 32), fill=AMBER)
    d4.rounded_rectangle([80, 580, W-80, 1400], radius=24, fill=(10, 16, 28), outline=SKY, width=2)
    d4.ellipse([340, 750, 740, 1150], outline=SKY, width=4)
    d4.ellipse([420, 830, 660, 1070], outline=(251, 191, 36), width=2)
    d4.line([(540, 700), (540, 1200)], fill=SKY, width=2)
    d4.line([(290, 950), (790, 950)], fill=SKY, width=2)
    d4.text((360, 1220), "[ FORENSIC RETICLE ]", font=get_font(FONT_MONO, 28), fill=MUTED)
    d4.text((140, 1300), "A SYNTHETIC PHYSICAL BIOMETRIC CLONE", font=get_font(FONT_ANTON, 40), fill=AMBER)
    b4 = add_scanlines(b4)
    b4.save(VISUALS_DIR / "beat_04.jpg", quality=95)

    # BEAT 05: The Silicone Fake Thumb (Real Hacker lab photo background)
    b5 = create_photographic_base("hacker_setup", tint_color=(25, 12, 35), brightness=0.45)
    add_glow_orb(b5, 540, 900, 480, (168, 85, 247), 0.4)
    d5 = ImageDraw.Draw(b5)
    draw_top_left_brand(d5)
    draw_header_tag(d5, "EXHIBIT A: SYNTHETIC BIOMETRIC", 260, (168, 85, 247))
    d5.text((80, 380), "NAKLI SILICONE UNGLI!", font=get_font(FONT_ANTON, 80), fill=(168, 85, 247))
    d5.text((80, 490), "TRANSLUCENT POLYMER ARTIFICIAL THUMB", font=get_font(FONT_SPACE, 34), fill=WHITE)
    d5.rounded_rectangle([80, 580, W-80, 1420], radius=24, fill=(10, 12, 22), outline=(168, 85, 247), width=3)
    for r in range(40, 240, 20):
        d5.ellipse([540-r, 920-r, 540+r, 920+r], outline=(251, 191, 36), width=3)
    d5.text((120, 1220), "DERMAL RIDGE MATCH: 99.4%", font=get_font(FONT_MONO, 36), fill=EMERALD)
    d5.text((120, 1280), "MATERIAL: MEDICAL GRADE SILICONE GEL", font=get_font(FONT_MONO, 32), fill=MUTED)
    d5.text((120, 1340), "THICKNESS: 1.8mm FLEXIBLE SHELL", font=get_font(FONT_MONO, 32), fill=MUTED)
    b5 = add_scanlines(b5)
    b5.save(VISUALS_DIR / "beat_05.jpg", quality=95)

    # BEAT 06: Police Evidence Raids (Real Police Investigation background)
    b6 = create_photographic_base("police_evidence", tint_color=(35, 12, 16), brightness=0.45)
    add_glow_orb(b6, 540, 850, 450, CRIMSON, 0.45)
    d6 = ImageDraw.Draw(b6)
    draw_top_left_brand(d6)
    draw_header_tag(d6, "POLICE CYBER CELL RAIDS", 260, CRIMSON)
    d6.text((80, 380), "1,000+ NAKLI UNGLIYAN SEIZED!", font=get_font(FONT_ANTON, 68), fill=CRIMSON)
    d6.text((80, 480), "GURUGRAM · PALWAL · NAWADA · GAYA BUSTS", font=get_font(FONT_SPACE, 32), fill=AMBER)
    d6.rounded_rectangle([60, 570, W-60, 1380], radius=24, fill=(12, 16, 26), outline=CRIMSON, width=3)
    d6.text((100, 640), "SEIZURE MEMO: STATE CYBER CELL", font=get_font(FONT_MONO, 32), fill=MUTED)
    d6.text((100, 720), "• 1,240 SILICONE THUMBS IN PLASTIC TRAYS", font=get_font(FONT_INTER, 34), fill=WHITE)
    d6.text((100, 800), "• 18 ULTRA-VIOLET POLY STAMPERS", font=get_font(FONT_INTER, 34), fill=WHITE)
    d6.text((100, 880), "• 5,400 LAND SALE DEED SCANS WITH AADHAAR", font=get_font(FONT_INTER, 34), fill=WHITE)
    d6.text((100, 960), "• 34 MICRO-ATM POS TERMINALS CONFISCATED", font=get_font(FONT_INTER, 34), fill=WHITE)
    d6.rounded_rectangle([100, 1100, W-100, 1300], radius=16, fill=(244, 63, 94), outline=WHITE, width=2)
    d6.text((140, 1150), "TOTAL FRAUD EXPOSURE: ₹14.8+ CRORE", font=get_font(FONT_ANTON, 46), fill=WHITE)
    d6.text((140, 1220), "STATUS: INTER-STATE SYNDICATE EXPOSED", font=get_font(FONT_MONO, 28), fill=(251, 191, 36))
    b6 = add_scanlines(b6)
    b6.save(VISUALS_DIR / "beat_06.jpg", quality=95)

    # BEAT 07: AePS Architecture (Real Server background)
    b7 = create_photographic_base("server_rack", tint_color=(10, 18, 30), brightness=0.45)
    add_glow_orb(b7, 540, 850, 420, SKY, 0.35)
    d7 = ImageDraw.Draw(b7)
    draw_top_left_brand(d7)
    draw_header_tag(d7, "NPCI SYSTEM ARCHITECTURE", 260, SKY)
    d7.text((80, 380), "WHAT IS AePS?", font=get_font(FONT_ANTON, 84), fill=WHITE)
    d7.text((80, 480), "AADHAAR ENABLED PAYMENT SYSTEM", font=get_font(FONT_SPACE, 34), fill=SKY)
    d7.rounded_rectangle([60, 580, W-60, 1400], radius=24, fill=(10, 16, 28), outline=SKY, width=2)
    steps = [
        ("1. CUSTOMER AADHAAR NUMBER", "(Enter 12 digits on POS Machine)"),
        ("2. BANK SELECTION", "(State Bank, PNB, BoB, etc.)"),
        ("3. BIOMETRIC THUMBPRINT", "(Press finger on optical glass)"),
        ("4. NPCI SWITCH ROUTING", "(Direct debit from linked account)")
    ]
    for i, (head, sub) in enumerate(steps):
        sy = 650 + i * 170
        d7.rounded_rectangle([100, sy, W-100, sy+130], radius=14, fill=(15, 23, 42), outline=AMBER, width=2)
        d7.text((130, sy+25), head, font=get_font(FONT_ANTON, 36), fill=WHITE)
        d7.text((130, sy+75), sub, font=get_font(FONT_MONO, 24), fill=MUTED)
    b7 = add_scanlines(b7)
    b7.save(VISUALS_DIR / "beat_07.jpg", quality=95)

    # BEAT 08: Rural Bharat POS (Real POS machine background)
    b8 = create_photographic_base("pos_machine", tint_color=(10, 25, 20), brightness=0.4)
    add_glow_orb(b8, 540, 900, 440, EMERALD, 0.4)
    d8 = ImageDraw.Draw(b8)
    draw_top_left_brand(d8)
    draw_header_tag(d8, "THE NOBLE INTENTION", 260, EMERALD)
    d8.text((80, 380), "BUILT FOR RURAL BHARAT", font=get_font(FONT_ANTON, 72), fill=EMERALD)
    d8.text((80, 480), "NO SMARTPHONE. NO ATM. JUST YOUR FINGER.", font=get_font(FONT_SPACE, 32), fill=WHITE)
    d8.rounded_rectangle([60, 580, W-60, 1360], radius=24, fill=(12, 22, 20), outline=EMERALD, width=2)
    d8.text((100, 660), "PURPOSE: ZERO BARRIER BANKING", font=get_font(FONT_MONO, 32), fill=MUTED)
    d8.text((100, 750), "• Pensioners in remote villages", font=get_font(FONT_INTER, 36), fill=WHITE)
    d8.text((100, 840), "• MGNREGA daily wage disbursements", font=get_font(FONT_INTER, 36), fill=WHITE)
    d8.text((100, 930), "• Direct Benefit Transfer (DBT)", font=get_font(FONT_INTER, 36), fill=WHITE)
    d8.rounded_rectangle([100, 1070, W-100, 1260], radius=16, fill=(16, 185, 129), outline=WHITE, width=2)
    d8.text((130, 1110), "PROMISE: 'YOUR THUMB IS YOUR PIN'", font=get_font(FONT_ANTON, 44), fill=OBSIDIAN)
    d8.text((130, 1180), "BUT WHAT IF YOUR THUMB GETS COPIED?", font=get_font(FONT_SPACE, 28), fill=(15, 23, 42))
    b8 = add_scanlines(b8)
    b8.save(VISUALS_DIR / "beat_08.jpg", quality=95)

    # BEAT 09: Zero 2FA (Real Cyber dark background)
    b9 = create_photographic_base("cyber_dark", tint_color=(35, 10, 16), brightness=0.45)
    add_glow_orb(b9, 540, 850, 480, CRIMSON, 0.45)
    d9 = ImageDraw.Draw(b9)
    draw_top_left_brand(d9)
    draw_header_tag(d9, "SYSTEM VULNERABILITY AUDIT", 260, CRIMSON)
    d9.text((80, 380), "THE LETHAL FLAW: ZERO 2FA", font=get_font(FONT_ANTON, 72), fill=CRIMSON)
    d9.text((80, 480), "NO SECOND-FACTOR AUTHENTICATION REQUIRED", font=get_font(FONT_SPACE, 30), fill=WHITE)
    d9.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(16, 12, 20), outline=CRIMSON, width=3)
    d9.text((100, 660), "AUTHENTICATION COMPARISON:", font=get_font(FONT_MONO, 30), fill=MUTED)
    d9.rounded_rectangle([100, 740, W-100, 900], radius=14, fill=(15, 23, 42), outline=MUTED, width=1)
    d9.text((120, 765), "UPI / NETBANKING:", font=get_font(FONT_ANTON, 32), fill=WHITE)
    d9.text((120, 820), "Password + OTP + Device ID (3 Factors)", font=get_font(FONT_MONO, 26), fill=EMERALD)
    d9.rounded_rectangle([100, 950, W-100, 1150], radius=14, fill=(35, 12, 18), outline=CRIMSON, width=2)
    d9.text((120, 985), "AePS SYSTEM:", font=get_font(FONT_ANTON, 36), fill=CRIMSON)
    d9.text((120, 1050), "Only Aadhaar # + Thumbprint (1 Factor)", font=get_font(FONT_MONO, 28), fill=(251, 191, 36))
    d9.rounded_rectangle([100, 1220, W-100, 1320], radius=12, fill=CRIMSON, outline=WHITE, width=2)
    d9.text((140, 1245), "IF THUMBPRINT LEAKS = FULL ACCOUNT ACCESS!", font=get_font(FONT_ANTON, 34), fill=WHITE)
    b9 = add_scanlines(b9)
    b9.save(VISUALS_DIR / "beat_09.jpg", quality=95)

    # BEAT 10: Land Registry Portals (Real Legal Document photo background)
    b10 = create_photographic_base("legal_document", tint_color=(12, 18, 28), brightness=0.4)
    add_glow_orb(b10, 540, 850, 420, AMBER, 0.35)
    d10 = ImageDraw.Draw(b10)
    draw_top_left_brand(d10)
    draw_header_tag(d10, "SOURCE OF THE DATA LEAK", 260, AMBER)
    d10.text((80, 380), "WHERE IS YOUR THUMB LEAKING?", font=get_font(FONT_ANTON, 64), fill=WHITE)
    d10.text((80, 480), "NOT THE DARK WEB. ON GOVERNMENT WEBSITES!", font=get_font(FONT_SPACE, 30), fill=AMBER)
    d10.rounded_rectangle([60, 570, W-60, 1380], radius=24, fill=(10, 15, 25), outline=AMBER, width=2)
    portals = [
        ("BIHAR IGRS PORTAL", "Registration & Excise Dept. Deed Downloads"),
        ("UP BHULEKH & IGRSUP", "Public Registry Search & Mutation Records"),
        ("HARYANA JAMABANDI", "Tehsil Land Deed Verification Documents"),
        ("RAJASTHAN E-DHARTI", "Sub-Registrar Office Scanned Deeds")
    ]
    for i, (name, desc) in enumerate(portals):
        py = 640 + i * 170
        d10.rounded_rectangle([100, py, W-100, py+130], radius=14, fill=(15, 23, 42), outline=MUTED, width=1)
        d10.text((130, py+20), name, font=get_font(FONT_ANTON, 34), fill=(251, 191, 36))
        d10.text((130, py+70), desc, font=get_font(FONT_MONO, 24), fill=MUTED)
    b10 = add_scanlines(b10)
    b10.save(VISUALS_DIR / "beat_10.jpg", quality=95)

    # BEAT 11: Real Scanned Sale Deed (Legal document background)
    b11 = create_photographic_base("legal_document", tint_color=(20, 24, 30), brightness=0.45)
    add_glow_orb(b11, 540, 850, 400, (226, 232, 240), 0.25)
    d11 = ImageDraw.Draw(b11)
    draw_top_left_brand(d11)
    draw_header_tag(d11, "PRIMARY EVIDENCE DOCUMENT", 260, MUTED)
    d11.text((80, 380), "THE REGISTERED SALE DEED", font=get_font(FONT_ANTON, 68), fill=WHITE)
    d11.text((80, 480), "WHENEVER YOU BUY A FLAT OR PLOT...", font=get_font(FONT_SPACE, 32), fill=AMBER)
    d11.rounded_rectangle([80, 580, W-80, 1420], radius=16, fill=(248, 250, 252), outline=(148, 163, 184), width=3)
    d11.text((120, 630), "GOVERNMENT OF INDIA - REGISTRATION DEPARTMENT", font=get_font(FONT_MONO, 24), fill=(15, 23, 42))
    d11.text((120, 680), "DEED OF CONVEYANCE / SALE DEED #8491/2024", font=get_font(FONT_ANTON, 36), fill=(15, 23, 42))
    d11.line([(120, 740), (W-120, 740)], fill=(203, 213, 225), width=2)
    d11.text((120, 780), "BUYER NAME: RAMESH SHARMA", font=get_font(FONT_MONO, 28), fill=(51, 65, 85))
    d11.text((120, 840), "FATHER: LATE SHRI K.L. SHARMA", font=get_font(FONT_MONO, 28), fill=(51, 65, 85))
    d11.text((120, 900), "PROPERTY: PLOT NO. 42, SECTOR 8", font=get_font(FONT_MONO, 28), fill=(51, 65, 85))
    d11.rectangle([120, 980, 420, 1380], fill=(241, 245, 249), outline=(15, 23, 42), width=3)
    d11.text((140, 1000), "THUMBPRINT OF BUYER", font=get_font(FONT_MONO, 20), fill=(15, 23, 42))
    for r in range(20, 140, 12):
        d11.ellipse([270-r, 1200-r*1.2, 270+r, 1200+r*1.2], outline=(30, 41, 59), width=2)
    d11.text((450, 1040), "HIGH RESOLUTION", font=get_font(FONT_ANTON, 36), fill=CRIMSON)
    d11.text((450, 1100), "300+ DPI SCAN", font=get_font(FONT_MONO, 28), fill=(51, 65, 85))
    d11.text((450, 1160), "UNMASKED BIOMETRIC", font=get_font(FONT_SPACE, 26), fill=CRIMSON)
    b11 = add_scanlines(b11)
    b11.save(VISUALS_DIR / "beat_11.jpg", quality=95)

    # BEAT 12: Highlighter Sweep on Thumbprint (Real Fingerprint Macro photo background)
    b12 = create_photographic_base("fingerprint_macro", tint_color=(20, 22, 32), brightness=0.45)
    add_glow_orb(b12, 540, 850, 450, AMBER, 0.4)
    d12 = ImageDraw.Draw(b12)
    draw_top_left_brand(d12)
    draw_header_tag(d12, "FORENSIC HIGHLIGHTER SWEEP", 260, AMBER)
    d12.text((80, 380), "CLEAR UNMASKED THUMBPRINT", font=get_font(FONT_ANTON, 68), fill=AMBER)
    d12.text((80, 480), "FREE DOWNLOAD FOR ANYONE ON THE INTERNET", font=get_font(FONT_SPACE, 30), fill=WHITE)
    d12.rounded_rectangle([80, 580, W-80, 1400], radius=24, fill=(10, 15, 25), outline=AMBER, width=3)
    d12.rectangle([200, 680, 880, 1250], fill=(248, 250, 252), outline=AMBER, width=4)
    for r in range(25, 200, 15):
        d12.ellipse([540-r, 965-r*1.1, 540+r, 965+r*1.1], outline=(15, 23, 42), width=3)
    d12.rectangle([220, 720, 860, 1210], fill=(255, 230, 0, 120), outline=(251, 191, 36), width=2)
    d12.text((240, 1290), "RIDGES & CORE LOOPS FULLY INTACT", font=get_font(FONT_MONO, 32), fill=AMBER)
    b12 = add_scanlines(b12)
    b12.save(VISUALS_DIR / "beat_12.jpg", quality=95)

    # BEAT 13: Aadhaar Number Leak (Real Legal Document photo background)
    b13 = create_photographic_base("legal_document", tint_color=(35, 12, 18), brightness=0.4)
    add_glow_orb(b13, 540, 850, 420, CRIMSON, 0.4)
    d13 = ImageDraw.Draw(b13)
    draw_top_left_brand(d13)
    draw_header_tag(d13, "UNMASKED IDENTITY RECORD", 260, CRIMSON)
    d13.text((80, 380), "AADHAAR NUMBER LEAKED", font=get_font(FONT_ANTON, 72), fill=CRIMSON)
    d13.text((80, 480), "12 DIGITS UNMASKED RIGHT BESIDE THE THUMB", font=get_font(FONT_SPACE, 30), fill=WHITE)
    d13.rounded_rectangle([60, 580, W-60, 1360], radius=24, fill=(15, 20, 30), outline=CRIMSON, width=3)
    d13.text((100, 660), "GOVERNMENT OF INDIA - AADHAAR CARD ATTACHED", font=get_font(FONT_MONO, 28), fill=MUTED)
    d13.rounded_rectangle([100, 740, W-100, 960], radius=16, fill=(10, 14, 22), outline=(244, 63, 94), width=2)
    d13.text((140, 810), "7412  8956  9012", font=get_font(FONT_MONO, 64), fill=WHITE)
    d13.text((140, 900), "ZERO DIGITS MASKED (SHOULD BE XXXX XXXX 9012)", font=get_font(FONT_MONO, 24), fill=CRIMSON)
    d13.text((100, 1040), "EVERYTHING REQUIRED FOR AePS IS NOW EXPOSED:", font=get_font(FONT_SPACE, 30), fill=AMBER)
    d13.text((100, 1120), "✔ 12-Digit Aadhaar Number", font=get_font(FONT_INTER, 34), fill=WHITE)
    d13.text((100, 1180), "✔ Primary Bank Account Name", font=get_font(FONT_INTER, 34), fill=WHITE)
    d13.text((100, 1240), "✔ 300+ DPI Clean Fingerprint Image", font=get_font(FONT_INTER, 34), fill=WHITE)
    b13 = add_scanlines(b13)
    b13.save(VISUALS_DIR / "beat_13.jpg", quality=95)

    # BEAT 14: 1-Click Download (Server rack background)
    b14 = create_photographic_base("server_rack", tint_color=(12, 18, 30), brightness=0.45)
    add_glow_orb(b14, 540, 850, 400, SKY, 0.35)
    d14 = ImageDraw.Draw(b14)
    draw_top_left_brand(d14)
    draw_header_tag(d14, "PUBLIC EXPLOIT PIPELINE", 260, SKY)
    d14.text((80, 380), "ZERO LOGIN NEEDED", font=get_font(FONT_ANTON, 80), fill=WHITE)
    d14.text((80, 480), "ANYONE CAN DOWNLOAD YOUR COMPLETE DEED", font=get_font(FONT_SPACE, 32), fill=SKY)
    d14.rounded_rectangle([60, 580, W-60, 1360], radius=24, fill=(10, 15, 26), outline=SKY, width=2)
    d14.rounded_rectangle([140, 780, W-140, 940], radius=20, fill=(37, 99, 235), outline=WHITE, width=2)
    d14.text((240, 830), "📥 DOWNLOAD DEED (PDF)", font=get_font(FONT_ANTON, 48), fill=WHITE)
    d14.text((140, 1020), "STATUS: 20-PAGE SCAN FETCHED IN 1.2s", font=get_font(FONT_MONO, 32), fill=EMERALD)
    d14.text((140, 1100), "NO CAPTCHA · NO OTP · NO IDENTITY CHECK", font=get_font(FONT_MONO, 28), fill=CRIMSON)
    b14 = add_scanlines(b14)
    b14.save(VISUALS_DIR / "beat_14.jpg", quality=95)

    # BEAT 15 to 30: Apply photographic bases across all remaining beats
    photo_map = {
        15: ("hacker_setup", (20, 18, 28), (168, 85, 247)),
        16: ("hacker_setup", (25, 12, 35), (236, 72, 153)),
        17: ("hacker_setup", (20, 15, 30), AMBER),
        18: ("atm_card", (30, 15, 20), CRIMSON),
        19: ("atm_card", (15, 25, 20), (34, 197, 94)),
        20: ("server_rack", (10, 25, 20), EMERALD),
        21: ("cash_rupees", (40, 12, 16), CRIMSON),
        22: ("smartphone_shield", (10, 20, 35), SKY),
        23: ("smartphone_shield", (12, 22, 38), SKY),
        24: ("smartphone_shield", (10, 28, 22), EMERALD),
        25: ("smartphone_shield", (12, 20, 35), SKY),
        26: ("atm_card", (35, 12, 18), CRIMSON),
        27: ("atm_card", (40, 10, 18), CRIMSON),
        28: ("police_evidence", (15, 22, 35), AMBER),
        29: ("police_evidence", (40, 12, 18), CRIMSON),
        30: ("server_rack", (15, 18, 30), AMBER)
    }

    for b_num, (pkey, tint, acc) in photo_map.items():
        base_img = create_photographic_base(pkey, tint_color=tint, brightness=0.45)
        add_glow_orb(base_img, 540, 850, 450, acc, 0.4)
        
        # Read existing graphic overlay if already made or draw fresh
        prev_file = VISUALS_DIR / f"beat_{b_num:02d}.jpg"
        if prev_file.exists():
            prev_im = Image.open(prev_file).convert("RGBA")
            # Alpha composite previous HUD cards over photographic plate
            # Blend 50% photo with 50% existing cards
            base_rgba = base_img.convert("RGBA")
            blended = Image.blend(base_rgba, prev_im, 0.65).convert("RGB")
            blended = add_scanlines(blended)
            blended.save(prev_file, quality=95)
            print(f"  ✓ Composited real photo into beat_{b_num:02d}.jpg")

    print("🎉 All 30 visual beats successfully upgraded with real photographic backgrounds!")

if __name__ == "__main__":
    download_source_photos()
    build_all_composites()
