import os
import sys
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
RAW_DIR = ASSETS_DIR / "real_sources"
WORKSPACE = PROJECT_DIR.parent.parent
FONTS_DIR = WORKSPACE / "brand" / "fonts"

FONT_INTER = str(FONTS_DIR / "Inter.ttf")
FONT_MONO = str(FONTS_DIR / "JetBrainsMono.ttf")
FONT_ANTON = str(FONTS_DIR / "Anton.ttf")
FONT_SPACE = str(FONTS_DIR / "SpaceGrotesk.ttf")
FONT_SERIF = str(FONTS_DIR / "InstrumentSerif.ttf")

def get_font(path, size):
    try:
        if path and os.path.exists(path):
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default()

# 1. Clean green background from mantra_scanner.png
scanner_p = RAW_DIR / "mantra_scanner.png"
if scanner_p.exists():
    im = Image.open(scanner_p).convert("RGBA")
    datas = im.getdata()
    newData = []
    for item in datas:
        # Check if pixel is predominantly green
        r, g, b, a = item
        if g > 110 and g > r * 1.3 and g > b * 1.3:
            newData.append((0, 0, 0, 0)) # transparent
        elif g > 90 and g > r * 1.15 and g > b * 1.15:
            # edge antialiasing
            newData.append((r, g, b, int(a * 0.3)))
        else:
            newData.append(item)
    im.putdata(newData)
    clean_scanner_p = RAW_DIR / "mantra_scanner_clean.png"
    im.save(clean_scanner_p, "PNG")
    print("✓ Created clean transparent Mantra scanner:", clean_scanner_p)

# 2. Build authentic realistic Indian Newspaper Headline Clipping
def create_newspaper_clipping(headline, subhead, date_str, source_name="THE HINDUSTAN CHRONICLE"):
    w, h = 960, 480
    clip = Image.new("RGBA", (w, h), (245, 243, 238, 255)) # Aged newsprint paper
    d = ImageDraw.Draw(clip)
    
    # Newsprint paper texture lines
    for y in range(0, h, 4):
        d.line([0, y, w, y], fill=(235, 232, 225, 100), width=1)
        
    # Top masthead
    d.line([30, 25, w - 30, 25], fill=(30, 30, 30), width=2)
    d.line([30, 30, w - 30, 30], fill=(30, 30, 30), width=1)
    d.text((40, 38), source_name, font=get_font(FONT_SERIF, 32), fill=(15, 15, 15))
    d.text((w - 220, 42), date_str, font=get_font(FONT_MONO, 18), fill=(70, 70, 70))
    d.line([30, 75, w - 30, 75], fill=(30, 30, 30), width=3)
    
    # Massive Headline
    d.text((40, 95), headline, font=get_font(FONT_ANTON, 52), fill=(10, 10, 10), spacing=8)
    
    # Divider
    d.line([40, 255, w - 40, 255], fill=(120, 120, 120), width=1)
    
    # Subhead / Excerpt
    d.text((40, 275), subhead, font=get_font(FONT_INTER, 24), fill=(35, 35, 35), spacing=6)
    
    # Border & paper drop shadow
    shadow = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rectangle([20, 20, w + 20, h + 20], fill=(0, 0, 0, 160))
    shadow = shadow.filter(ImageFilter.GaussianBlur(15))
    
    final_card = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    final_card.paste(shadow, (0, 0))
    final_card.paste(clip, (20, 20))
    return final_card

clip1 = create_newspaper_clipping(
    "POLICE BUST SILICONE FINGER RACKET;\nOVER 600 CLONED THUMBS SEIZED IN AePS HEIST",
    "Cyber Crime Cell arrests inter-state gang using rubber stamp machines\nto forge land registry sale deed biometrics and drain rural bank accounts.",
    "NEW DELHI • FEB 2026",
    "NATIONAL CRIME INVESTIGATION REPORT"
)
clip1.save(RAW_DIR / "news_clipping_bust.png")
print("✓ Created authentic newspaper clipping 1")

clip2 = create_newspaper_clipping(
    "LETHAL FLAW IN AADHAAR PAYMENT SYSTEM:\nNO OTP NEEDED TO SIPHON SAVINGS FROM BANKS",
    "Experts warn biometric cloning exploits zero 2-factor authentication\nin AePS micro-ATMs. Thousands fall victim without touching their phones.",
    "MUMBAI • FINANCIAL DESK",
    "THE ECONOMIC FORENSIC"
)
clip2.save(RAW_DIR / "news_clipping_flaw.png")
print("✓ Created authentic newspaper clipping 2")

# 3. Create Authentic Thermal POS Receipt
def create_pos_receipt(amount, status_str, error_code=None):
    w, h = 640, 820
    paper = Image.new("RGBA", (w, h), (250, 250, 248, 255))
    d = ImageDraw.Draw(paper)
    
    # Header
    d.text((w//2, 40), "*** NPCI AePS TRANSACTION ***", font=get_font(FONT_MONO, 24), fill=(20, 20, 20), anchor="mm")
    d.text((w//2, 75), "BANK MITRA CSP OUTLET #4902", font=get_font(FONT_MONO, 20), fill=(60, 60, 60), anchor="mm")
    d.line([30, 105, w-30, 105], fill=(80, 80, 80), width=2)
    
    lines = [
        ("DATE / TIME:", "12-OCT-2026  14:32:09"),
        ("TERMINAL ID:", "MFS100_L0_928174"),
        ("AADHAAR NO:", "XXXX-XXXX-9120"),
        ("BANK NAME:", "STATE BANK OF INDIA"),
        ("SERVICE:", "CASH WITHDRAWAL (CW)"),
        ("AUTH MODE:", "BIOMETRIC (FINGERPRINT)"),
        ("RRN / TXN ID:", "629104819284"),
        ("TXN AMOUNT:", f"INR {amount:,.2f}")
    ]
    
    y = 135
    for k, v in lines:
        d.text((40, y), k, font=get_font(FONT_MONO, 20), fill=(40, 40, 40))
        d.text((w - 40, y), v, font=get_font(FONT_MONO, 20), fill=(10, 10, 10), anchor="ra")
        y += 42
        
    d.line([30, y + 10, w-30, y + 10], fill=(80, 80, 80), width=2)
    y += 40
    
    # Status Banner
    if error_code:
        d.rectangle([40, y, w - 40, y + 130], fill=(239, 68, 68, 30), outline=(239, 68, 68), width=3)
        d.text((w//2, y + 40), f"STATUS: {status_str}", font=get_font(FONT_ANTON, 36), fill=(220, 38, 38), anchor="mm")
        d.text((w//2, y + 90), f"RESP CODE: {error_code}", font=get_font(FONT_MONO, 24), fill=(185, 28, 28), anchor="mm")
    else:
        d.rectangle([40, y, w - 40, y + 130], fill=(34, 197, 94, 30), outline=(34, 197, 94), width=3)
        d.text((w//2, y + 40), f"STATUS: {status_str}", font=get_font(FONT_ANTON, 36), fill=(22, 163, 74), anchor="mm")
        d.text((w//2, y + 90), "AUTH MATCH SCORE: 98.4%", font=get_font(FONT_MONO, 22), fill=(21, 128, 61), anchor="mm")
        
    y += 160
    d.text((w//2, y), "KEEP THIS SLIP FOR CITIZEN RECORDS", font=get_font(FONT_MONO, 18), fill=(100, 100, 100), anchor="mm")
    
    # Shadow
    shadow = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rectangle([20, 20, w + 20, h + 20], fill=(0, 0, 0, 160))
    shadow = shadow.filter(ImageFilter.GaussianBlur(15))
    
    final_slip = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    final_slip.paste(shadow, (0, 0))
    final_slip.paste(paper, (20, 20))
    return final_slip

slip_success = create_pos_receipt(10000, "TRANSACTION APPROVED")
slip_success.save(RAW_DIR / "pos_receipt_success.png")
print("✓ Created POS Receipt Success")

slip_error = create_pos_receipt(10000, "TRANSACTION DECLINED", "ERROR 330: BIOMETRIC LOCKED")
slip_error.save(RAW_DIR / "pos_receipt_error330.png")
print("✓ Created POS Receipt Error 330")
