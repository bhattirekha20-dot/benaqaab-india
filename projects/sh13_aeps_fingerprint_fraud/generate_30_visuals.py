import os
import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets" / "visuals"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)
FONTS_DIR = Path(r"c:\Users\dell\Desktop\my ai bot skills ok\brand\fonts")
LOGO_PATH = Path(r"c:\Users\dell\Desktop\my ai bot skills ok\brand\logo.png")

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

def create_base(bg_color1, bg_color2):
    img = Image.new("RGB", (W, H), bg_color1)
    draw = ImageDraw.Draw(img)
    r1, g1, b1 = bg_color1
    r2, g2, b2 = bg_color2
    for y in range(0, H, 4):
        t = y / H
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        draw.rectangle([0, y, W, y+4], fill=(r, g, b))
    return img

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
    # Circle avatar placeholder or paste logo if available
    draw.ellipse([70, 100, 120, 150], fill=(244, 63, 94))
    font_bold = get_font(FONT_ANTON, 26)
    draw.text((135, 104), "BENAQAAB INDIA", font=font_bold, fill=(255, 255, 255))
    font_sub = get_font(FONT_MONO, 14)
    draw.text((135, 134), "SACH · SABOOT · BEBAK", font=font_sub, fill=(251, 191, 36))

def draw_verdict_stamp(draw, text, cx=540, cy=1400, angle=-10, border_color=(244, 63, 94)):
    # Draw a rotated forensic rubber stamp onto an overlay
    stamp_w, stamp_h = 750, 140
    stamp = Image.new("RGBA", (stamp_w, stamp_h), (0, 0, 0, 0))
    sd = ImageDraw.Draw(stamp)
    sd.rounded_rectangle([10, 10, stamp_w - 10, stamp_h - 10], radius=18, outline=border_color, width=6)
    sd.rounded_rectangle([20, 20, stamp_w - 20, stamp_h - 20], radius=12, outline=border_color, width=2)
    font_stamp = get_font(FONT_ANTON, 68)
    bbox = sd.textbbox((0, 0), text, font=font_stamp)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    sd.text(((stamp_w - tw)//2, (stamp_h - th)//2 - 10), text, font=font_stamp, fill=border_color)
    
    rotated = stamp.rotate(angle, resample=Image.BICUBIC, expand=True)
    return rotated

def generate_all_30_visuals():
    print("🎨 Generating 30 hyper-retention visual beats for Episode SH-13...")
    
    # Common color palettes
    OBSIDIAN = (7, 9, 14)
    SLATE_DARK = (15, 23, 42)
    CRIMSON = (244, 63, 94)
    AMBER = (251, 191, 36)
    SKY = (56, 189, 248)
    EMERALD = (52, 211, 153)
    WHITE = (255, 255, 255)
    MUTED = (148, 163, 184)

    # BEAT 01: Frame 0 Hook - Account Debited Alert
    b1 = create_base(OBSIDIAN, (28, 10, 16))
    add_glow_orb(b1, 540, 960, 480, CRIMSON, 0.35)
    d1 = ImageDraw.Draw(b1)
    draw_top_left_brand(d1)
    draw_header_tag(d1, "CRITICAL BANKING ALERT", 260, CRIMSON)
    d1.rounded_rectangle([60, 360, W-60, 1080], radius=28, fill=(15, 20, 32), outline=(244, 63, 94), width=3)
    d1.text((100, 420), "A/C DEBITED: ₹10,000.00", font=get_font(FONT_ANTON, 72), fill=CRIMSON)
    d1.text((100, 520), "AePS CASH WITHDRAWAL SUCCESSFUL", font=get_font(FONT_SPACE, 36), fill=WHITE)
    d1.line([(100, 590), (W-100, 590)], fill=(244, 63, 94), width=2)
    d1.text((100, 640), "TIME: 03:14 AM (MIDNIGHT)", font=get_font(FONT_MONO, 32), fill=MUTED)
    d1.text((100, 710), "LOCATION: MICRO-ATM #9412 (BIHAR)", font=get_font(FONT_MONO, 32), fill=MUTED)
    d1.text((100, 780), "AUTHENTICATION: BIOMETRIC THUMBPRINT", font=get_font(FONT_MONO, 32), fill=AMBER)
    d1.rounded_rectangle([100, 890, W-100, 1010], radius=16, fill=(244, 63, 94), outline=WHITE, width=2)
    d1.text((140, 925), "ZERO OTP SENT · VICTIM WAS ASLEEP", font=get_font(FONT_ANTON, 40), fill=WHITE)
    b1 = add_scanlines(b1)
    b1.save(ASSETS_DIR / "beat_01.jpg", quality=95)

    # BEAT 02: Zero OTP · Zero ATM Card · Zero Bank Visit
    b2 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b2, 540, 800, 400, AMBER, 0.25)
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
        d2.rounded_rectangle([60, cy, W-60, cy+180], radius=20, fill=(15, 23, 42), outline=col, width=2)
        d2.text((100, cy+30), title, font=get_font(FONT_ANTON, 46), fill=col)
        d2.text((100, cy+100), desc, font=get_font(FONT_INTER, 28), fill=MUTED)
    b2 = add_scanlines(b2)
    b2.save(ASSETS_DIR / "beat_02.jpg", quality=95)

    # BEAT 03: The Disappearance of ₹10,000
    b3 = create_base(OBSIDIAN, (35, 12, 18))
    add_glow_orb(b3, 540, 900, 450, CRIMSON, 0.4)
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
    b3.save(ASSETS_DIR / "beat_03.jpg", quality=95)

    # BEAT 04: The Weapon Clue
    b4 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b4, 540, 850, 420, SKY, 0.3)
    d4 = ImageDraw.Draw(b4)
    draw_top_left_brand(d4)
    draw_header_tag(d4, "THE FORENSIC EVIDENCE", 260, SKY)
    d4.text((80, 380), "CHOR KA ASLI HATHYAR?", font=get_font(FONT_ANTON, 72), fill=WHITE)
    d4.text((80, 480), "NOT A GUN. NOT MALWARE. NOT A PASSWORD.", font=get_font(FONT_SPACE, 32), fill=AMBER)
    d4.rounded_rectangle([80, 580, W-80, 1400], radius=24, fill=(12, 18, 30), outline=SKY, width=2)
    # Draw geometric magnifying reticle
    d4.ellipse([340, 750, 740, 1150], outline=SKY, width=4)
    d4.ellipse([420, 830, 660, 1070], outline=(251, 191, 36), width=2)
    d4.line([(540, 700), (540, 1200)], fill=SKY, width=2)
    d4.line([(290, 950), (790, 950)], fill=SKY, width=2)
    d4.text((360, 1220), "[ FORENSIC RETICLE ]", font=get_font(FONT_MONO, 28), fill=MUTED)
    d4.text((140, 1300), "A SYNTHETIC PHYSICAL BIOMETRIC CLONE", font=get_font(FONT_ANTON, 40), fill=AMBER)
    b4 = add_scanlines(b4)
    b4.save(ASSETS_DIR / "beat_04.jpg", quality=95)

    # BEAT 05: The Silicone Ungli (Cloned Thumb)
    b5 = create_base(OBSIDIAN, (20, 15, 30))
    add_glow_orb(b5, 540, 900, 460, (168, 85, 247), 0.35)
    d5 = ImageDraw.Draw(b5)
    draw_top_left_brand(d5)
    draw_header_tag(d5, "EXHIBIT A: SYNTHETIC BIOMETRIC", 260, (168, 85, 247))
    d5.text((80, 380), "NAKLI SILICONE UNGLI!", font=get_font(FONT_ANTON, 80), fill=(168, 85, 247))
    d5.text((80, 490), "TRANSLUCENT POLYMER ARTIFICIAL THUMB", font=get_font(FONT_SPACE, 34), fill=WHITE)
    d5.rounded_rectangle([80, 580, W-80, 1420], radius=24, fill=(10, 12, 20), outline=(168, 85, 247), width=3)
    # Simulate fingerprint ridges inside glass box
    for r in range(40, 240, 20):
        d5.ellipse([540-r, 920-r, 540+r, 920+r], outline=(251, 191, 36), width=3)
    d5.text((120, 1220), "DERMAL RIDGE MATCH: 99.4%", font=get_font(FONT_MONO, 36), fill=EMERALD)
    d5.text((120, 1280), "MATERIAL: MEDICAL GRADE SILICONE GEL", font=get_font(FONT_MONO, 32), fill=MUTED)
    d5.text((120, 1340), "THICKNESS: 1.8mm FLEXIBLE SHELL", font=get_font(FONT_MONO, 32), fill=MUTED)
    b5 = add_scanlines(b5)
    b5.save(ASSETS_DIR / "beat_05.jpg", quality=95)

    # BEAT 06: Police Evidence - 1,000+ Clones Seized
    b6 = create_base(OBSIDIAN, (30, 10, 15))
    add_glow_orb(b6, 540, 850, 420, CRIMSON, 0.4)
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
    b6.save(ASSETS_DIR / "beat_06.jpg", quality=95)

    # BEAT 07: AePS System Architecture
    b7 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b7, 540, 850, 420, SKY, 0.35)
    d7 = ImageDraw.Draw(b7)
    draw_top_left_brand(d7)
    draw_header_tag(d7, "NPCI SYSTEM ARCHITECTURE", 260, SKY)
    d7.text((80, 380), "WHAT IS AePS?", font=get_font(FONT_ANTON, 84), fill=WHITE)
    d7.text((80, 480), "AADHAAR ENABLED PAYMENT SYSTEM", font=get_font(FONT_SPACE, 34), fill=SKY)
    d7.rounded_rectangle([60, 580, W-60, 1400], radius=24, fill=(10, 16, 28), outline=SKY, width=2)
    # Flow diagram
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
    b7.save(ASSETS_DIR / "beat_07.jpg", quality=95)

    # BEAT 08: Financial Inclusion Dream
    b8 = create_base(OBSIDIAN, (10, 25, 20))
    add_glow_orb(b8, 540, 900, 420, EMERALD, 0.35)
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
    b8.save(ASSETS_DIR / "beat_08.jpg", quality=95)

    # BEAT 09: The Lethal Flaw (Zero 2FA)
    b9 = create_base(OBSIDIAN, (32, 10, 15))
    add_glow_orb(b9, 540, 850, 450, CRIMSON, 0.45)
    d9 = ImageDraw.Draw(b9)
    draw_top_left_brand(d9)
    draw_header_tag(d9, "SYSTEM VULNERABILITY AUDIT", 260, CRIMSON)
    d9.text((80, 380), "THE LETHAL FLAW: ZERO 2FA", font=get_font(FONT_ANTON, 72), fill=CRIMSON)
    d9.text((80, 480), "NO SECOND-FACTOR AUTHENTICATION REQUIRED", font=get_font(FONT_SPACE, 30), fill=WHITE)
    d9.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(16, 12, 20), outline=CRIMSON, width=3)
    d9.text((100, 660), "AUTHENTICATION COMPARISON:", font=get_font(FONT_MONO, 30), fill=MUTED)
    # Netbanking
    d9.rounded_rectangle([100, 740, W-100, 900], radius=14, fill=(15, 23, 42), outline=MUTED, width=1)
    d9.text((120, 765), "UPI / NETBANKING:", font=get_font(FONT_ANTON, 32), fill=WHITE)
    d9.text((120, 820), "Password + OTP + Device ID (3 Factors)", font=get_font(FONT_MONO, 26), fill=EMERALD)
    # AePS
    d9.rounded_rectangle([100, 950, W-100, 1150], radius=14, fill=(35, 12, 18), outline=CRIMSON, width=2)
    d9.text((120, 985), "AePS SYSTEM:", font=get_font(FONT_ANTON, 36), fill=CRIMSON)
    d9.text((120, 1050), "Only Aadhaar # + Thumbprint (1 Factor)", font=get_font(FONT_MONO, 28), fill=(251, 191, 36))
    d9.rounded_rectangle([100, 1220, W-100, 1320], radius=12, fill=CRIMSON, outline=WHITE, width=2)
    d9.text((140, 1245), "IF THUMBPRINT LEAKS = FULL ACCOUNT ACCESS!", font=get_font(FONT_ANTON, 34), fill=WHITE)
    b9 = add_scanlines(b9)
    b9.save(ASSETS_DIR / "beat_09.jpg", quality=95)

    # BEAT 10: Where do they get your thumb? The Land Registry Trail
    b10 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b10, 540, 850, 420, AMBER, 0.3)
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
    b10.save(ASSETS_DIR / "beat_10.jpg", quality=95)

    # BEAT 11: The Scanned Property Sale Deed (Kewala)
    b11 = create_base(OBSIDIAN, (20, 24, 30))
    add_glow_orb(b11, 540, 850, 400, (226, 232, 240), 0.2)
    d11 = ImageDraw.Draw(b11)
    draw_top_left_brand(d11)
    draw_header_tag(d11, "PRIMARY EVIDENCE DOCUMENT", 260, MUTED)
    d11.text((80, 380), "THE REGISTERED SALE DEED", font=get_font(FONT_ANTON, 68), fill=WHITE)
    d11.text((80, 480), "WHENEVER YOU BUY A FLAT OR PLOT...", font=get_font(FONT_SPACE, 32), fill=AMBER)
    # Scanned paper simulation
    d11.rounded_rectangle([80, 580, W-80, 1420], radius=16, fill=(248, 250, 252), outline=(148, 163, 184), width=3)
    d11.text((120, 630), "GOVERNMENT OF INDIA - REGISTRATION DEPARTMENT", font=get_font(FONT_MONO, 24), fill=(15, 23, 42))
    d11.text((120, 680), "DEED OF CONVEYANCE / SALE DEED #8491/2024", font=get_font(FONT_ANTON, 36), fill=(15, 23, 42))
    d11.line([(120, 740), (W-120, 740)], fill=(203, 213, 225), width=2)
    d11.text((120, 780), "BUYER NAME: RAMESH SHARMA", font=get_font(FONT_MONO, 28), fill=(51, 65, 85))
    d11.text((120, 840), "FATHER: LATE SHRI K.L. SHARMA", font=get_font(FONT_MONO, 28), fill=(51, 65, 85))
    d11.text((120, 900), "PROPERTY: PLOT NO. 42, SECTOR 8", font=get_font(FONT_MONO, 28), fill=(51, 65, 85))
    # Simulated thumbprint box
    d11.rectangle([120, 980, 420, 1380], fill=(241, 245, 249), outline=(15, 23, 42), width=3)
    d11.text((140, 1000), "THUMBPRINT OF BUYER", font=get_font(FONT_MONO, 20), fill=(15, 23, 42))
    # Draw ink thumbprint simulation
    for r in range(20, 140, 12):
        d11.ellipse([270-r, 1200-r*1.2, 270+r, 1200+r*1.2], outline=(30, 41, 59), width=2)
    # Text next to thumb
    d11.text((450, 1040), "HIGH RESOLUTION", font=get_font(FONT_ANTON, 36), fill=CRIMSON)
    d11.text((450, 1100), "300+ DPI SCAN", font=get_font(FONT_MONO, 28), fill=(51, 65, 85))
    d11.text((450, 1160), "UNMASKED BIOMETRIC", font=get_font(FONT_SPACE, 26), fill=CRIMSON)
    b11 = add_scanlines(b11)
    b11.save(ASSETS_DIR / "beat_11.jpg", quality=95)

    # BEAT 12: Highlighter Sweep on Thumbprint
    b12 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b12, 540, 850, 420, AMBER, 0.4)
    d12 = ImageDraw.Draw(b12)
    draw_top_left_brand(d12)
    draw_header_tag(d12, "FORENSIC HIGHLIGHTER SWEEP", 260, AMBER)
    d12.text((80, 380), "CLEAR UNMASKED THUMBPRINT", font=get_font(FONT_ANTON, 68), fill=AMBER)
    d12.text((80, 480), "FREE DOWNLOAD FOR ANYONE ON THE INTERNET", font=get_font(FONT_SPACE, 30), fill=WHITE)
    d12.rounded_rectangle([80, 580, W-80, 1400], radius=24, fill=(10, 15, 25), outline=AMBER, width=3)
    # Magnified thumb box with yellow highlighter multiply simulation
    d12.rectangle([200, 680, 880, 1250], fill=(248, 250, 252), outline=AMBER, width=4)
    for r in range(25, 200, 15):
        d12.ellipse([540-r, 965-r*1.1, 540+r, 965+r*1.1], outline=(15, 23, 42), width=3)
    # Yellow highlighter rectangle
    d12.rectangle([220, 720, 860, 1210], fill=(255, 230, 0, 120), outline=(251, 191, 36), width=2)
    d12.text((240, 1290), "RIDGES & CORE LOOPS FULLY INTACT", font=get_font(FONT_MONO, 32), fill=AMBER)
    b12 = add_scanlines(b12)
    b12.save(ASSETS_DIR / "beat_12.jpg", quality=95)

    # BEAT 13: The Aadhaar Number Leak
    b13 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b13, 540, 850, 420, CRIMSON, 0.35)
    d13 = ImageDraw.Draw(b13)
    draw_top_left_brand(d13)
    draw_header_tag(d13, "UNMASKED IDENTITY RECORD", 260, CRIMSON)
    d13.text((80, 380), "AADHAAR NUMBER LEAKED", font=get_font(FONT_ANTON, 72), fill=CRIMSON)
    d13.text((80, 480), "12 DIGITS UNMASKED RIGHT BESIDE THE THUMB", font=get_font(FONT_SPACE, 30), fill=WHITE)
    d13.rounded_rectangle([60, 580, W-60, 1360], radius=24, fill=(15, 20, 30), outline=CRIMSON, width=3)
    # Simulated Aadhaar card section
    d13.text((100, 660), "GOVERNMENT OF INDIA - AADHAAR CARD ATTACHED", font=get_font(FONT_MONO, 28), fill=MUTED)
    d13.rounded_rectangle([100, 740, W-100, 960], radius=16, fill=(10, 14, 22), outline=(244, 63, 94), width=2)
    d13.text((140, 810), "7412  8956  9012", font=get_font(FONT_MONO, 64), fill=WHITE)
    d13.text((140, 900), "ZERO DIGITS MASKED (SHOULD BE XXXX XXXX 9012)", font=get_font(FONT_MONO, 24), fill=CRIMSON)
    d13.text((100, 1040), "EVERYTHING REQUIRED FOR AePS IS NOW EXPOSED:", font=get_font(FONT_SPACE, 30), fill=AMBER)
    d13.text((100, 1120), "✔ 12-Digit Aadhaar Number", font=get_font(FONT_INTER, 34), fill=WHITE)
    d13.text((100, 1180), "✔ Primary Bank Account Name", font=get_font(FONT_INTER, 34), fill=WHITE)
    d13.text((100, 1240), "✔ 300+ DPI Clean Fingerprint Image", font=get_font(FONT_INTER, 34), fill=WHITE)
    b13 = add_scanlines(b13)
    b13.save(ASSETS_DIR / "beat_13.jpg", quality=95)

    # BEAT 14: The 1-Click Download Exploit
    b14 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b14, 540, 850, 400, SKY, 0.3)
    d14 = ImageDraw.Draw(b14)
    draw_top_left_brand(d14)
    draw_header_tag(d14, "PUBLIC EXPLOIT PIPELINE", 260, SKY)
    d14.text((80, 380), "ZERO LOGIN NEEDED", font=get_font(FONT_ANTON, 80), fill=WHITE)
    d14.text((80, 480), "ANYONE CAN DOWNLOAD YOUR COMPLETE DEED", font=get_font(FONT_SPACE, 32), fill=SKY)
    d14.rounded_rectangle([60, 580, W-60, 1360], radius=24, fill=(10, 15, 26), outline=SKY, width=2)
    # UI button simulation
    d14.rounded_rectangle([140, 780, W-140, 940], radius=20, fill=(37, 99, 235), outline=WHITE, width=2)
    d14.text((240, 830), "📥 DOWNLOAD DEED (PDF)", font=get_font(FONT_ANTON, 48), fill=WHITE)
    d14.text((140, 1020), "STATUS: 20-PAGE SCAN FETCHED IN 1.2s", font=get_font(FONT_MONO, 32), fill=EMERALD)
    d14.text((140, 1100), "NO CAPTCHA · NO OTP · NO IDENTITY CHECK", font=get_font(FONT_MONO, 28), fill=CRIMSON)
    b14 = add_scanlines(b14)
    b14.save(ASSETS_DIR / "beat_14.jpg", quality=95)

    # BEAT 15: The Digital Inversion & Tracing Paper
    b15 = create_base(OBSIDIAN, (20, 18, 28))
    add_glow_orb(b15, 540, 850, 420, (168, 85, 247), 0.3)
    d15 = ImageDraw.Draw(b15)
    draw_top_left_brand(d15)
    draw_header_tag(d15, "CLONING STAGE 1: INVERSION", 260, (168, 85, 247))
    d15.text((80, 380), "BUTTER PAPER PRINT", font=get_font(FONT_ANTON, 72), fill=WHITE)
    d15.text((80, 480), "CONVERTING PIXELS TO NEGATIVE STAMP TEMPLATE", font=get_font(FONT_SPACE, 28), fill=(168, 85, 247))
    d15.rounded_rectangle([80, 580, W-80, 1400], radius=24, fill=(8, 10, 18), outline=(168, 85, 247), width=3)
    # Inverted negative box
    d15.rectangle([240, 680, 840, 1180], fill=(0, 0, 0), outline=WHITE, width=2)
    for r in range(20, 180, 14):
        d15.ellipse([540-r, 930-r*1.1, 540+r, 930+r*1.1], outline=(255, 255, 255), width=2)
    d15.text((140, 1240), "SOFTWARE: PHOTOSHOP / COREL DRAW", font=get_font(FONT_MONO, 30), fill=MUTED)
    d15.text((140, 1300), "SUBSTRATE: HIGH-CONTRAST TRACING PAPER", font=get_font(FONT_MONO, 30), fill=AMBER)
    b15 = add_scanlines(b15)
    b15.save(ASSETS_DIR / "beat_15.jpg", quality=95)

    # BEAT 16: The Poly-Stamper Machine & UV Curing
    b16 = create_base(OBSIDIAN, (25, 12, 35))
    add_glow_orb(b16, 540, 850, 450, (236, 72, 153), 0.35)
    d16 = ImageDraw.Draw(b16)
    draw_top_left_brand(d16)
    draw_header_tag(d16, "CLONING STAGE 2: UV CURING", 260, (236, 72, 153))
    d16.text((80, 380), "THE POLY-STAMPER MACHINE", font=get_font(FONT_ANTON, 68), fill=WHITE)
    d16.text((80, 480), "ORDINARY RUBBER STAMP MAKER USED FOR CRIME", font=get_font(FONT_SPACE, 30), fill=(236, 72, 153))
    d16.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(12, 10, 20), outline=(236, 72, 153), width=3)
    # Machine schematic
    d16.rounded_rectangle([140, 680, W-140, 1100], radius=20, fill=(20, 15, 30), outline=(236, 72, 153), width=2)
    d16.text((180, 740), "[ UV CURING CHAMBER ]", font=get_font(FONT_MONO, 32), fill=(251, 191, 36))
    d16.text((180, 820), "LIGHT INTENSITY: 365nm ULTRAVIOLET", font=get_font(FONT_MONO, 28), fill=WHITE)
    d16.text((180, 890), "MEDIUM: LIQUID PHOTOPOLYMER RESIN", font=get_font(FONT_MONO, 28), fill=WHITE)
    d16.text((180, 960), "CURING DURATION: 15 MINUTES", font=get_font(FONT_MONO, 28), fill=EMERALD)
    d16.text((120, 1180), "COST OF EQUIPMENT: UNDER ₹8,000 ON INDIAMART", font=get_font(FONT_ANTON, 38), fill=AMBER)
    d16.text((120, 1260), "ACCESSIBLE TO ANY LOCAL DTP OPERATOR", font=get_font(FONT_SPACE, 30), fill=MUTED)
    b16 = add_scanlines(b16)
    b16.save(ASSETS_DIR / "beat_16.jpg", quality=95)

    # BEAT 17: The 3D Rubber Finger Created
    b17 = create_base(OBSIDIAN, (20, 15, 30))
    add_glow_orb(b17, 540, 850, 420, AMBER, 0.35)
    d17 = ImageDraw.Draw(b17)
    draw_top_left_brand(d17)
    draw_header_tag(d17, "CLONING STAGE 3: THE PHYSICAL CLONE", 260, AMBER)
    d17.text((80, 380), "THE CLONE IS BORN", font=get_font(FONT_ANTON, 84), fill=WHITE)
    d17.text((80, 480), "PERFECT 3D REPLICA OF VICTIM'S RIGHT THUMB", font=get_font(FONT_SPACE, 30), fill=AMBER)
    d17.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(14, 16, 26), outline=AMBER, width=3)
    d17.text((100, 660), "FORENSIC CHARACTERISTICS:", font=get_font(FONT_MONO, 32), fill=MUTED)
    d17.text((100, 750), "✔ Exact Papillary Ridge Spacing", font=get_font(FONT_INTER, 36), fill=WHITE)
    d17.text((100, 830), "✔ Sweat Pore Indentations Duplicated", font=get_font(FONT_INTER, 36), fill=WHITE)
    d17.text((100, 910), "✔ Flexible Curvature Fits Scammer's Finger", font=get_font(FONT_INTER, 36), fill=WHITE)
    d17.text((100, 990), "✔ Reusable Across Hundreds of Transactions", font=get_font(FONT_INTER, 36), fill=WHITE)
    d17.rounded_rectangle([100, 1140, W-100, 1300], radius=16, fill=(244, 63, 94), outline=WHITE, width=2)
    d17.text((140, 1190), "READY FOR THE CASH EXTRACTION", font=get_font(FONT_ANTON, 48), fill=WHITE)
    b17 = add_scanlines(b17)
    b17.save(ASSETS_DIR / "beat_17.jpg", quality=95)

    # BEAT 18: The Rogue Micro-ATM Merchant
    b18 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b18, 540, 850, 420, CRIMSON, 0.35)
    d18 = ImageDraw.Draw(b18)
    draw_top_left_brand(d18)
    draw_header_tag(d18, "THE ROGUE OPERATOR", 260, CRIMSON)
    d18.text((80, 380), "ROGUE BANK MITRA", font=get_font(FONT_ANTON, 76), fill=CRIMSON)
    d18.text((80, 480), "HOW SCAMMERS ACCESS THE AePS NETWORK", font=get_font(FONT_SPACE, 32), fill=WHITE)
    d18.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(12, 16, 26), outline=CRIMSON, width=2)
    d18.text((100, 660), "OPERATOR PROFILE:", font=get_font(FONT_MONO, 32), fill=MUTED)
    d18.text((100, 750), "• Fake business correspondent (BC) IDs bought on Telegram", font=get_font(FONT_INTER, 32), fill=WHITE)
    d18.text((100, 840), "• Third-party fintech merchant login accounts", font=get_font(FONT_INTER, 32), fill=WHITE)
    d18.text((100, 930), "• Micro-ATM machine operates from secluded hotel room", font=get_font(FONT_INTER, 32), fill=WHITE)
    d18.rounded_rectangle([100, 1080, W-100, 1280], radius=16, fill=(15, 23, 42), outline=AMBER, width=2)
    d18.text((130, 1120), "RESULT: UNTRACEABLE CASH DRAINS", font=get_font(FONT_ANTON, 40), fill=AMBER)
    d18.text((130, 1190), "No CCTV. No Bank Branch. No Guards.", font=get_font(FONT_SPACE, 30), fill=MUTED)
    b18 = add_scanlines(b18)
    b18.save(ASSETS_DIR / "beat_18.jpg", quality=95)

    # BEAT 19: The Older L0 Optical Scanner Flaw
    b19 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b19, 540, 850, 440, (34, 197, 94), 0.3)
    d19 = ImageDraw.Draw(b19)
    draw_top_left_brand(d19)
    draw_header_tag(d19, "HARDWARE VULNERABILITY", 260, (34, 197, 94))
    d19 = ImageDraw.Draw(b19)
    d19.text((80, 380), "THE L0 SCANNER FLAW", font=get_font(FONT_ANTON, 76), fill=WHITE)
    d19.text((80, 480), "LEGACY OPTICAL SCANNERS CANNOT DETECT LIFE", font=get_font(FONT_SPACE, 30), fill=(34, 197, 94))
    d19.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(10, 18, 20), outline=(34, 197, 94), width=3)
    d19.text((100, 660), "OPTICAL SENSOR AUDIT (MANTRA / MORPHO L0):", font=get_font(FONT_MONO, 28), fill=MUTED)
    d19.text((100, 750), "❌ ZERO LIVENESS DETECTION", font=get_font(FONT_ANTON, 42), fill=CRIMSON)
    d19.text((100, 820), "Does not measure blood pulse or skin warmth", font=get_font(FONT_MONO, 26), fill=MUTED)
    d19.text((100, 920), "❌ ZERO SUBCUTANEOUS CHECK", font=get_font(FONT_ANTON, 42), fill=CRIMSON)
    d19.text((100, 990), "Treats rubber silicone like living human tissue", font=get_font(FONT_MONO, 26), fill=MUTED)
    d19.rounded_rectangle([100, 1120, W-100, 1280], radius=16, fill=(34, 197, 94), outline=WHITE, width=2)
    d19.text((140, 1160), "GREEN LIGHT BLINKS: PRINT ACCEPTED!", font=get_font(FONT_ANTON, 38), fill=OBSIDIAN)
    b19 = add_scanlines(b19)
    b19.save(ASSETS_DIR / "beat_19.jpg", quality=95)

    # BEAT 20: The Biometric Match: 98% Match
    b20 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b20, 540, 850, 420, EMERALD, 0.4)
    d20 = ImageDraw.Draw(b20)
    draw_top_left_brand(d20)
    draw_header_tag(d20, "SYSTEM AUTHENTICATION LOG", 260, EMERALD)
    d20.text((80, 380), "98% MATCH CONFIRMED", font=get_font(FONT_ANTON, 76), fill=EMERALD)
    d20.text((80, 480), "CENTRAL UIDAI SERVER VERIFIES THE RUBBER THUMB", font=get_font(FONT_SPACE, 28), fill=WHITE)
    d20.rounded_rectangle([60, 580, W-60, 1360], radius=24, fill=(10, 20, 18), outline=EMERALD, width=3)
    d20.text((100, 660), "AUTHENTICATION RESPONSE:", font=get_font(FONT_MONO, 32), fill=MUTED)
    d20.text((100, 750), "STATUS: SUCCESS (AUTH-CODE: 200)", font=get_font(FONT_ANTON, 48), fill=WHITE)
    d20.text((100, 840), "MATCH SCORE: 98.2 / 100", font=get_font(FONT_MONO, 36), fill=EMERALD)
    d20.text((100, 920), "ALGORITHM: MINUTIAE POINT ALIGNMENT", font=get_font(FONT_MONO, 30), fill=MUTED)
    d20.text((100, 1000), "VERDICT: VALID CITIZEN PRESENT", font=get_font(FONT_MONO, 30), fill=CRIMSON)
    d20.rounded_rectangle([100, 1120, W-100, 1260], radius=16, fill=(16, 185, 129), outline=WHITE, width=2)
    d20.text((150, 1160), "AUTHORIZATION GRANTED TO WITHDRAW CASH", font=get_font(FONT_ANTON, 34), fill=OBSIDIAN)
    b20 = add_scanlines(b20)
    b20.save(ASSETS_DIR / "beat_20.jpg", quality=95)

    # BEAT 21: Rolling Odometer Hits ₹10,000 (Cash Out)
    b21 = create_base(OBSIDIAN, (35, 12, 16))
    add_glow_orb(b21, 540, 850, 480, CRIMSON, 0.45)
    d21 = ImageDraw.Draw(b21)
    draw_top_left_brand(d21)
    draw_header_tag(d21, "LIVE ROLLING CASH ODOMETER", 260, CRIMSON)
    d21.text((80, 380), "POORE ₹10,000 GAYAB!", font=get_font(FONT_ANTON, 84), fill=CRIMSON)
    d21.text((80, 500), "CASH DISPENSED TO FRAUDSTER IN SECONDS", font=get_font(FONT_SPACE, 32), fill=WHITE)
    d21.rounded_rectangle([60, 600, W-60, 1350], radius=24, fill=(12, 14, 24), outline=CRIMSON, width=3)
    # Giant rolling odometer display
    d21.rounded_rectangle([100, 720, W-100, 940], radius=16, fill=(0, 0, 0), outline=AMBER, width=3)
    d21.text((140, 780), "₹ 1 0 , 0 0 0 . 0 0", font=get_font(FONT_MONO, 72), fill=AMBER)
    d21.text((100, 1020), "VICTIM PHONE: ZERO ALERT UNTIL MORNING", font=get_font(FONT_MONO, 32), fill=MUTED)
    d21.text((100, 1100), "SAVINGS ACCOUNT DRAINED TO PENNIES", font=get_font(FONT_SPACE, 34), fill=CRIMSON)
    d21.rounded_rectangle([100, 1190, W-100, 1280], radius=12, fill=CRIMSON, outline=WHITE, width=2)
    d21.text((150, 1215), "HARD-EARNED MONEY GONE FOREVER?", font=get_font(FONT_ANTON, 40), fill=WHITE)
    b21 = add_scanlines(b21)
    b21.save(ASSETS_DIR / "beat_21.jpg", quality=95)

    # BEAT 22: THE PIVOT - The 60-Second Citizen Shield (Color Inversion to Cyan/Gold)
    b22 = create_base(OBSIDIAN, (10, 20, 35))
    add_glow_orb(b22, 540, 850, 480, SKY, 0.45)
    d22 = ImageDraw.Draw(b22)
    draw_top_left_brand(d22)
    draw_header_tag(d22, "THE FOOLPROOF CITIZEN SHIELD", 260, SKY)
    d22.text((80, 380), "LEKIN BACHNE KA EK RASTA!", font=get_font(FONT_ANTON, 72), fill=WHITE)
    d22.text((80, 480), "60 SECONDS TO IMMUNIZE YOUR BANK ACCOUNT", font=get_font(FONT_SPACE, 32), fill=SKY)
    d22.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(10, 18, 30), outline=SKY, width=3)
    d22.text((100, 660), "UIDAI CITIZEN ARMOR FEATURE:", font=get_font(FONT_MONO, 32), fill=MUTED)
    d22.text((100, 750), "🛡️ BIOMETRIC LOCKING FACILITY", font=get_font(FONT_ANTON, 54), fill=AMBER)
    d22.text((100, 850), "Completely freezes all fingerprint & iris authentication.", font=get_font(FONT_INTER, 34), fill=WHITE)
    d22.text((100, 930), "Zero bank withdrawals possible until you unlock.", font=get_font(FONT_INTER, 34), fill=WHITE)
    d22.rounded_rectangle([100, 1080, W-100, 1280], radius=16, fill=(14, 165, 233), outline=WHITE, width=2)
    d22.text((160, 1120), "OFFICIAL GOVERNMENT SECURITY SHIELD", font=get_font(FONT_ANTON, 38), fill=OBSIDIAN)
    d22.text((160, 1180), "Available to all 1.4 Billion Aadhaar holders.", font=get_font(FONT_SPACE, 28), fill=(15, 23, 42))
    b22 = add_scanlines(b22)
    b22.save(ASSETS_DIR / "beat_22.jpg", quality=95)

    # BEAT 23: Step 1 - Open mAadhaar App
    b23 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b23, 540, 850, 420, SKY, 0.35)
    d23 = ImageDraw.Draw(b23)
    draw_top_left_brand(d23)
    draw_header_tag(d23, "STEP 1: ACCESS THE SHIELD", 260, SKY)
    d23.text((80, 380), "OPEN mAadhaar APP", font=get_font(FONT_ANTON, 84), fill=WHITE)
    d23.text((80, 480), "OR GO TO: myaadhaar.uidai.gov.in", font=get_font(FONT_SPACE, 34), fill=AMBER)
    d23.rounded_rectangle([80, 580, W-80, 1380], radius=24, fill=(10, 16, 28), outline=SKY, width=2)
    # Simulated mobile phone frame
    d23.rounded_rectangle([200, 660, 880, 1300], radius=32, fill=(15, 23, 42), outline=MUTED, width=3)
    d23.ellipse([510, 680, 570, 710], fill=(51, 65, 85)) # Speaker notch
    d23.rounded_rectangle([240, 760, 840, 880], radius=16, fill=(37, 99, 235), outline=WHITE, width=2)
    d23.text((320, 800), "LOGIN WITH OTP", font=get_font(FONT_ANTON, 48), fill=WHITE)
    d23.text((240, 940), "OFFICIAL UIDAI PORTAL", font=get_font(FONT_MONO, 28), fill=MUTED)
    d23.text((240, 1010), "ENTER 12-DIGIT AADHAAR", font=get_font(FONT_INTER, 32), fill=WHITE)
    d23.text((240, 1080), "ENTER 6-DIGIT SMS OTP", font=get_font(FONT_INTER, 32), fill=WHITE)
    b23 = add_scanlines(b23)
    b23.save(ASSETS_DIR / "beat_23.jpg", quality=95)

    # BEAT 24: Step 2 - Toggle Biometric Lock to ON
    b24 = create_base(OBSIDIAN, (10, 25, 20))
    add_glow_orb(b24, 540, 850, 440, EMERALD, 0.4)
    d24 = ImageDraw.Draw(b24)
    draw_top_left_brand(d24)
    draw_header_tag(d24, "STEP 2: ACTIVATE THE LOCK", 260, EMERALD)
    d24.text((80, 380), "TOGGLE: BIOMETRICS LOCKED", font=get_font(FONT_ANTON, 68), fill=EMERALD)
    d24.text((80, 480), "SLIDE THE SWITCH TO PROTECT YOUR PRINTS", font=get_font(FONT_SPACE, 30), fill=WHITE)
    d24.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(12, 22, 20), outline=EMERALD, width=3)
    # Simulated toggle switch
    d24.rounded_rectangle([200, 760, 880, 960], radius=40, fill=(16, 185, 129), outline=WHITE, width=3)
    d24.ellipse([680, 780, 860, 940], fill=WHITE) # Toggle handle to ON
    d24.text((260, 835), "🔒 LOCKED", font=get_font(FONT_ANTON, 64), fill=OBSIDIAN)
    d24.text((100, 1060), "CURRENT STATUS: 100% PROTECTED", font=get_font(FONT_MONO, 36), fill=EMERALD)
    d24.text((100, 1140), "AePS Cash Withdrawal: BLOCKED", font=get_font(FONT_INTER, 34), fill=WHITE)
    d24.text((100, 1210), "Micro-ATM Verification: BLOCKED", font=get_font(FONT_INTER, 34), fill=WHITE)
    b24 = add_scanlines(b24)
    b24.save(ASSETS_DIR / "beat_24.jpg", quality=95)

    # BEAT 25: The Digital Vault (Aadhaar Protected)
    b25 = create_base(OBSIDIAN, (12, 20, 35))
    add_glow_orb(b25, 540, 850, 450, SKY, 0.4)
    d25 = ImageDraw.Draw(b25)
    draw_top_left_brand(d25)
    draw_header_tag(d25, "THE IMPENETRABLE VAULT", 260, SKY)
    d25.text((80, 380), "IMMUNIZED AGAINST CLONES", font=get_font(FONT_ANTON, 72), fill=WHITE)
    d25.text((80, 480), "EVEN IF SOMEONE COPIES YOUR PHYSICAL THUMB", font=get_font(FONT_SPACE, 28), fill=SKY)
    d25.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(10, 16, 28), outline=SKY, width=3)
    # Vault graphic representation
    d25.ellipse([340, 720, 740, 1120], outline=SKY, width=6)
    d25.ellipse([400, 780, 680, 1060], outline=AMBER, width=4)
    d25.text((450, 890), "🔒", font=get_font(FONT_ANTON, 96), fill=WHITE)
    d25.text((120, 1200), "CENTRAL UIDAI SERVERS REJECT ALL ATTEMPTS", font=get_font(FONT_MONO, 32), fill=EMERALD)
    d25.text((120, 1270), "Your bank account balance remains untouched.", font=get_font(FONT_INTER, 32), fill=MUTED)
    b25 = add_scanlines(b25)
    b25.save(ASSETS_DIR / "beat_25.jpg", quality=95)

    # BEAT 26: The Scammer Tries Again with Clone
    b26 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b26, 540, 850, 420, CRIMSON, 0.3)
    d26 = ImageDraw.Draw(b26)
    draw_top_left_brand(d26)
    draw_header_tag(d26, "THE FRAUD ATTEMPT IN PROGRESS", 260, CRIMSON)
    d26.text((80, 380), "SCAMMER PRESSES CLONE...", font=get_font(FONT_ANTON, 72), fill=WHITE)
    d26.text((80, 480), "TRYING TO EXTRACT ANOTHER ₹10,000", font=get_font(FONT_SPACE, 32), fill=CRIMSON)
    d26.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(12, 14, 22), outline=CRIMSON, width=2)
    d26.text((100, 680), "ATTEMPT LOG #8921", font=get_font(FONT_MONO, 32), fill=MUTED)
    d26.text((100, 760), "DEVICE: Micro-ATM POS L0 Scanner", font=get_font(FONT_INTER, 34), fill=WHITE)
    d26.text((100, 840), "PAYLOAD: Cloned Silicone Thumb (98% Ridge Match)", font=get_font(FONT_INTER, 34), fill=WHITE)
    d26.text((100, 920), "REQUEST: Cash Withdrawal ₹10,000", font=get_font(FONT_INTER, 34), fill=AMBER)
    d26.rounded_rectangle([100, 1080, W-100, 1260], radius=16, fill=(15, 23, 42), outline=MUTED, width=2)
    d26.text((160, 1120), "WAITING FOR SERVER RESPONSE...", font=get_font(FONT_MONO, 36), fill=MUTED)
    d26.text((160, 1180), "Connecting to UIDAI CIDR Gateways...", font=get_font(FONT_MONO, 24), fill=MUTED)
    b26 = add_scanlines(b26)
    b26.save(ASSETS_DIR / "beat_26.jpg", quality=95)

    # BEAT 27: The Brutal System Block: ERROR 330
    b27 = create_base(OBSIDIAN, (35, 10, 18))
    add_glow_orb(b27, 540, 850, 480, CRIMSON, 0.5)
    d27 = ImageDraw.Draw(b27)
    draw_top_left_brand(d27)
    draw_header_tag(d27, "CRITICAL ERROR RESPONSE", 260, CRIMSON)
    d27.text((80, 380), "ERROR 330: LOCKED!", font=get_font(FONT_ANTON, 88), fill=CRIMSON)
    d27.text((80, 500), "TRANSACTION ABORTED BY UIDAI GATEWAY", font=get_font(FONT_SPACE, 32), fill=WHITE)
    d27.rounded_rectangle([60, 600, W-60, 1380], radius=24, fill=(15, 12, 22), outline=CRIMSON, width=4)
    # Giant error screen
    d27.rounded_rectangle([100, 700, W-100, 960], radius=16, fill=(244, 63, 94), outline=WHITE, width=3)
    d27.text((140, 750), "ERROR CODE: 330", font=get_font(FONT_ANTON, 64), fill=WHITE)
    d27.text((140, 840), "BIOMETRICS ARE LOCKED BY AADHAAR HOLDER", font=get_font(FONT_MONO, 28), fill=(255, 255, 255))
    d27.text((100, 1040), "AUTHENTICATION DENIED", font=get_font(FONT_ANTON, 46), fill=AMBER)
    d27.text((100, 1120), "ZERO RUPEES DEBITED · FRAUDSTER THWARTED", font=get_font(FONT_MONO, 30), fill=EMERALD)
    d27.text((100, 1200), "INCIDENT LOGGED TO CYBER POLICE", font=get_font(FONT_MONO, 30), fill=MUTED)
    b27 = add_scanlines(b27)
    b27.save(ASSETS_DIR / "beat_27.jpg", quality=95)

    # BEAT 28: National Helpline 1930 Card
    b28 = create_base(OBSIDIAN, SLATE_DARK)
    add_glow_orb(b28, 540, 850, 440, AMBER, 0.35)
    d28 = ImageDraw.Draw(b28)
    draw_top_left_brand(d28)
    draw_header_tag(d28, "EMERGENCY CYBERCRIME HOTLINE", 260, AMBER)
    d28.text((80, 380), "DIAL 1930 IMMEDIATELY", font=get_font(FONT_ANTON, 76), fill=AMBER)
    d28.text((80, 480), "NATIONAL CYBER CRIME REPORTING PORTAL", font=get_font(FONT_SPACE, 30), fill=WHITE)
    d28.rounded_rectangle([60, 580, W-60, 1380], radius=24, fill=(12, 16, 28), outline=AMBER, width=2)
    d28.text((100, 680), "GOLDEN HOUR MANDATE:", font=get_font(FONT_MONO, 32), fill=MUTED)
    d28.text((100, 760), "Report within 2 hours of unauthorized debit.", font=get_font(FONT_INTER, 34), fill=WHITE)
    d28.text((100, 840), "Cyber cell freezes the mule bank account in real-time.", font=get_font(FONT_INTER, 34), fill=WHITE)
    d28.rounded_rectangle([100, 960, W-100, 1140], radius=16, fill=(15, 23, 42), outline=SKY, width=2)
    d28.text((140, 1000), "🌐 cybercrime.gov.in", font=get_font(FONT_ANTON, 54), fill=SKY)
    d28.text((140, 1080), "Indian Cyber Crime Coordination Centre (I4C)", font=get_font(FONT_MONO, 24), fill=MUTED)
    b28 = add_scanlines(b28)
    b28.save(ASSETS_DIR / "beat_28.jpg", quality=95)

    # BEAT 29: Dynamic Verdict Stamp: [CLONED FINGERPRINT EXPOSED]
    b29 = create_base(OBSIDIAN, (35, 12, 18))
    add_glow_orb(b29, 540, 850, 480, CRIMSON, 0.45)
    d29 = ImageDraw.Draw(b29)
    draw_top_left_brand(d29)
    draw_header_tag(d29, "FINAL FORENSIC VERDICT", 260, CRIMSON)
    d29.text((80, 380), "THE TRUTH UNMASKED", font=get_font(FONT_ANTON, 84), fill=WHITE)
    d29.text((80, 500), "AePS BIOMETRIC VULNERABILITY REVEALED", font=get_font(FONT_SPACE, 32), fill=AMBER)
    d29.rounded_rectangle([60, 600, W-60, 1350], radius=24, fill=(12, 15, 25), outline=CRIMSON, width=3)
    d29.text((100, 680), "CHANNEL VERDICT:", font=get_font(FONT_MONO, 32), fill=MUTED)
    d29.text((100, 770), "• Biometric theft happens through public land portals.", font=get_font(FONT_INTER, 34), fill=WHITE)
    d29.text((100, 860), "• Silicone thumbs bypass older L0 optical scanners.", font=get_font(FONT_INTER, 34), fill=WHITE)
    d29.text((100, 950), "• Locking biometrics in mAadhaar eliminates 100% risk.", font=get_font(FONT_INTER, 34), fill=EMERALD)
    # Paste stamp
    stamp_img = draw_verdict_stamp(d29, "CLONED SCAM EXPOSED", angle=-9, border_color=CRIMSON)
    b29.paste(stamp_img, (160, 1080), stamp_img)
    b29 = add_scanlines(b29)
    b29.save(ASSETS_DIR / "beat_29.jpg", quality=95)

    # BEAT 30: Channel Identity Card & Subscribe/Like CTA
    b30 = create_base(OBSIDIAN, (15, 18, 30))
    add_glow_orb(b30, 540, 850, 480, AMBER, 0.4)
    d30 = ImageDraw.Draw(b30)
    draw_header_tag(d30, "OFFICIAL CHANNEL IDENTITY", 260, AMBER)
    d30.rounded_rectangle([60, 380, W-60, 1500], radius=32, fill=(10, 14, 24), outline=AMBER, width=3)
    # Large glowing avatar
    d30.ellipse([420, 480, 660, 720], fill=(244, 63, 94), outline=(251, 191, 36), width=4)
    d30.text((490, 560), "BI", font=get_font(FONT_ANTON, 96), fill=WHITE)
    d30.text((280, 770), "BENAQAAB INDIA", font=get_font(FONT_ANTON, 72), fill=WHITE)
    d30.text((310, 860), "SACH · SABOOT · BEBAK", font=get_font(FONT_MONO, 36), fill=AMBER)
    # Interactive-style Like button
    d30.rounded_rectangle([140, 960, W-140, 1080], radius=20, fill=(15, 23, 42), outline=SKY, width=2)
    d30.text((240, 995), "👍 LIKED & SAVED", font=get_font(FONT_ANTON, 48), fill=SKY)
    # Interactive-style Subscribe button
    d30.rounded_rectangle([140, 1140, W-140, 1280], radius=20, fill=CRIMSON, outline=WHITE, width=2)
    d30.text((200, 1180), "🔔 SUBSCRIBED ▶", font=get_font(FONT_ANTON, 56), fill=WHITE)
    d30.text((220, 1360), "SHARE TO PROTECT YOUR PARENTS", font=get_font(FONT_SPACE, 34), fill=MUTED)
    b30 = add_scanlines(b30)
    b30.save(ASSETS_DIR / "beat_30.jpg", quality=95)

    print("✅ All 30 visual beats generated successfully in assets/visuals/!")

if __name__ == "__main__":
    generate_all_30_visuals()
