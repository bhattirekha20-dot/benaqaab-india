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
VISUALS_DIR = ASSETS_DIR / "visuals"
VISUALS_DIR.mkdir(parents=True, exist_ok=True)

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

W, H = 1080, 1920

# Load raw image cache
raw_cache = {}
for f in os.listdir(RAW_DIR):
    p = RAW_DIR / f
    if p.is_file() and p.suffix.lower() in ['.jpg', '.png', '.jpeg']:
        try:
            raw_cache[f] = Image.open(p)
        except Exception as e:
            print(f"Failed opening {f}: {e}")

print(f"Loaded {len(raw_cache)} raw web assets from {RAW_DIR}")

def cover_fit(im, tw, th):
    iw, ih = im.size
    scale = max(tw / iw, th / ih)
    nw, nh = int(iw * scale), int(ih * scale)
    im_resized = im.resize((nw, nh), Image.Resampling.LANCZOS)
    left = (nw - tw) // 2
    top = (nh - th) // 2
    return im_resized.crop((left, top, left + tw, top + th))

def contain_fit(im, max_w, max_h):
    iw, ih = im.size
    scale = min(max_w / iw, max_h / ih)
    nw, nh = max(1, int(iw * scale)), max(1, int(ih * scale))
    return im.resize((nw, nh), Image.Resampling.LANCZOS)

def create_base_canvas(bg_asset_name=None, bg_color=(7, 9, 14), brightness=0.75, blur=0):
    if bg_asset_name and bg_asset_name in raw_cache:
        im = raw_cache[bg_asset_name].convert("RGB")
        im = cover_fit(im, W, H)
        if blur > 0:
            im = im.filter(ImageFilter.GaussianBlur(blur))
        if brightness != 1.0:
            im = ImageEnhance.Brightness(im).enhance(brightness)
    else:
        im = Image.new("RGB", (W, H), bg_color)
        
    # Cinematic Vignette (Subtle top & bottom darkening for clean HUD readability)
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(vignette)
    d.rectangle([0, 0, W, 240], fill=(7, 9, 14, 150))
    d.rectangle([0, H - 360, W, H], fill=(7, 9, 14, 180))
    im.paste(vignette, (0, 0), vignette)
    return im

def paste_asset(base_img, asset_name, cx, cy, max_w, max_h, shadow=True, border_color=None, border_w=3):
    if asset_name not in raw_cache:
        return
    asset = raw_cache[asset_name]
    asset_fitted = contain_fit(asset, max_w, max_h)
    aw, ah = asset_fitted.size
    
    px = cx - aw // 2
    py = cy - ah // 2
    
    if shadow:
        sh_w, sh_h = aw + 40, ah + 40
        sh = Image.new("RGBA", (sh_w, sh_h), (0, 0, 0, 0))
        sd = ImageDraw.Draw(sh)
        sd.rectangle([20, 20, aw + 20, ah + 20], fill=(0, 0, 0, 180))
        sh = sh.filter(ImageFilter.GaussianBlur(16))
        base_img.paste(sh, (px - 20, py - 20), sh)
        
    if border_color:
        card = Image.new("RGBA", (aw + border_w*2, ah + border_w*2), (0, 0, 0, 0))
        cd = ImageDraw.Draw(card)
        cd.rectangle([0, 0, card.width, card.height], fill=border_color)
        if asset_fitted.mode == "RGBA":
            card.paste(asset_fitted, (border_w, border_w), asset_fitted)
        else:
            card.paste(asset_fitted, (border_w, border_w))
        base_img.paste(card, (px - border_w, py - border_w), card)
    else:
        if asset_fitted.mode == "RGBA":
            base_img.paste(asset_fitted, (px, py), asset_fitted)
        else:
            base_img.paste(asset_fitted, (px, py))

# Generate All 30 Visual Plates
print("Generating 30 Full-Bleed Authentic Evidence Plates...")

for beat_id in range(1, 31):
    pad = f"{beat_id:02d}"
    out_path = VISUALS_DIR / f"beat_{pad}.jpg"
    
    if beat_id == 1:
        # Authentic 500 Rupee currency fan with floating SMS debit alert
        im = create_base_canvas("indian_currency_fan.jpg", brightness=0.7)
        # SMS Notification card at y = 420
        paste_asset(im, "news_clipping_flaw.png", 540, 1140, 880, 440, shadow=True)
        
    elif beat_id == 2:
        # Authentic ATM card with cancellation ring
        im = create_base_canvas("atm_card.jpg", brightness=0.85)
        d = ImageDraw.Draw(im)
        d.ellipse([340, 760, 740, 1160], outline="#EF4444", width=14)
        d.line([410, 830, 670, 1090], fill="#EF4444", width=14)
        
    elif beat_id == 3:
        # State Bank of India rural branch
        im = create_base_canvas("sbi_rural_branch.jpg", brightness=0.75)
        paste_asset(im, "indian_currency_fan.jpg", 540, 1100, 840, 480, shadow=True, border_color="#EF4444", border_w=4)
        
    elif beat_id == 4:
        # Cyber dark lab workstation
        im = create_base_canvas("hacker_setup.jpg", brightness=0.8)
        paste_asset(im, "news_clipping_flaw.png", 540, 960, 920, 460, shadow=True, border_color="#38BDF8", border_w=3)
        
    elif beat_id == 5:
        # Silicone artificial thumb replica
        im = create_base_canvas("cyber_dark.jpg", brightness=0.75)
        paste_asset(im, "fingerprint_whorl.jpg", 540, 940, 580, 580, shadow=True, border_color="#A855F7", border_w=5)
        
    elif beat_id == 6:
        # Authentic Police Seizure Newspaper Clipping: 600+ Cloned Thumbs Seized
        im = create_base_canvas("delhi_police_board.jpg", brightness=0.7)
        paste_asset(im, "news_clipping_bust.png", 540, 960, 940, 480, shadow=True, border_color="#EF4444", border_w=4)
        
    elif beat_id == 7:
        # Official NPCI AePS Architecture Diagram
        im = create_base_canvas("server_rack.jpg", brightness=0.65)
        paste_asset(im, "aeps_diagram.png", 540, 960, 980, 720, shadow=True, border_color="#38BDF8", border_w=4)
        
    elif beat_id == 8:
        # State Bank of India rural branch & Micro-ATM
        im = create_base_canvas("sbi_rural_branch.jpg", brightness=0.85)
        
    elif beat_id == 9:
        # Authentic Newspaper Clipping: AePS Zero OTP Flaw
        im = create_base_canvas("server_rack.jpg", brightness=0.7)
        paste_asset(im, "news_clipping_flaw.png", 540, 960, 940, 480, shadow=True, border_color="#EF4444", border_w=4)
        
    elif beat_id == 10:
        # Official Land Registry Portal
        im = create_base_canvas("legal_document.jpg", brightness=0.75)
        paste_asset(im, "news_clipping_bust.png", 540, 960, 920, 460, shadow=True, border_color="#FBBF24", border_w=3)
        
    elif beat_id == 11:
        # Full-Bleed Ultra HD Indian Stamped Paper Scan
        im = create_base_canvas("stamped_paper_india.jpg", brightness=0.9)
        
    elif beat_id == 12:
        # Zoom-in on the authentic thumb impression on stamped paper
        im = create_base_canvas("stamped_paper_india.jpg", brightness=0.85)
        paste_asset(im, "fingerprint_whorl.jpg", 540, 960, 560, 560, shadow=True, border_color="#FBBF24", border_w=5)
        
    elif beat_id == 13:
        # Stamped paper with Official Aadhaar Card Specimen
        im = create_base_canvas("stamped_paper_india.jpg", brightness=0.8)
        paste_asset(im, "aadhaar_specimen.png", 540, 960, 940, 360, shadow=True, border_color="#EF4444", border_w=4)
        
    elif beat_id == 14:
        # Digital download portal
        im = create_base_canvas("cyber_dark.jpg", brightness=0.8)
        paste_asset(im, "aadhaar_specimen.png", 540, 840, 900, 340, shadow=True, border_color="#38BDF8", border_w=3)
        paste_asset(im, "news_clipping_flaw.png", 540, 1200, 900, 420, shadow=True)
        
    elif beat_id == 15:
        # Laboratory tracing butter paper
        im = create_base_canvas("hacker_setup.jpg", brightness=0.8)
        paste_asset(im, "fingerprint_whorl.jpg", 540, 960, 540, 540, shadow=True, border_color="#A855F7", border_w=4)
        
    elif beat_id == 16:
        # UV polymer curing machine with ultraviolet glow
        im = create_base_canvas("cyber_dark.jpg", brightness=0.85)
        paste_asset(im, "fingerprint_whorl.jpg", 540, 960, 540, 540, shadow=True, border_color="#EC4899", border_w=5)
        
    elif beat_id == 17:
        # 3D Rubber thumb clone macro
        im = create_base_canvas("cyber_dark.jpg", brightness=0.8)
        paste_asset(im, "fingerprint_whorl.jpg", 540, 960, 600, 600, shadow=True, border_color="#FBBF24", border_w=6)
        
    elif beat_id == 18:
        # Scammer POS micro-ATM counter
        im = create_base_canvas("sbi_rural_branch.jpg", brightness=0.7)
        paste_asset(im, "pos_receipt_success.png", 540, 960, 680, 820, shadow=True)
        
    elif beat_id == 19:
        # CLEAN TRANSPARENT MANTRA MFS100 OPTICAL SCANNER!
        im = create_base_canvas("cyber_dark.jpg", brightness=0.85)
        paste_asset(im, "mantra_scanner_clean.png", 540, 940, 720, 540, shadow=True)
        
    elif beat_id == 20:
        # Authentic POS Receipt Approved Slip
        im = create_base_canvas("server_rack.jpg", brightness=0.7)
        paste_asset(im, "pos_receipt_success.png", 540, 960, 720, 880, shadow=True)
        
    elif beat_id == 21:
        # ₹10,000 Heist Currency Fan
        im = create_base_canvas("indian_currency_fan.jpg", brightness=0.7)
        
    elif beat_id == 22:
        # Cyber defense shield
        im = create_base_canvas("forensic_dark_slate.jpg", brightness=0.85)
        paste_asset(im, "aadhaar_logo_clean.png", 540, 940, 680, 440, shadow=True)
        
    elif beat_id == 23:
        # Official Android phone with mAadhaar App
        im = create_base_canvas("forensic_dark_slate.jpg", brightness=0.85)
        paste_asset(im, "maadhaar_phone_screen.png", 540, 960, 820, 1300, shadow=True)
        
    elif beat_id == 24:
        # mAadhaar App Biometrics Settings Lock
        im = create_base_canvas("forensic_dark_slate.jpg", brightness=0.85)
        paste_asset(im, "maadhaar_phone_screen.png", 540, 960, 820, 1300, shadow=True)
        
    elif beat_id == 25:
        # UIDAI CIDR Server Immunity
        im = create_base_canvas("server_rack.jpg", brightness=0.75)
        paste_asset(im, "aeps_diagram.png", 540, 960, 940, 660, shadow=True, border_color="#34D399", border_w=4)
        
    elif beat_id == 26:
        # Scammer tries with clone on Mantra scanner again
        im = create_base_canvas("cyber_dark.jpg", brightness=0.85)
        paste_asset(im, "mantra_scanner_clean.png", 540, 940, 720, 540, shadow=True)
        
    elif beat_id == 27:
        # Authentic POS Receipt: ERROR 330 BIOMETRIC LOCKED!
        im = create_base_canvas("hacker_setup.jpg", brightness=0.7)
        paste_asset(im, "pos_receipt_error330.png", 540, 960, 740, 900, shadow=True)
        
    elif beat_id == 28:
        # National Cybercrime Helpline 1930
        im = create_base_canvas("delhi_police_board.jpg", brightness=0.75)
        paste_asset(im, "news_clipping_bust.png", 540, 960, 920, 460, shadow=True, border_color="#FBBF24", border_w=4)
        
    elif beat_id == 29:
        # Complete evidence board
        im = create_base_canvas("delhi_police_board.jpg", brightness=0.7)
        paste_asset(im, "news_clipping_bust.png", 540, 820, 900, 440, shadow=True)
        paste_asset(im, "pos_receipt_error330.png", 540, 1260, 560, 680, shadow=True)
        
    elif beat_id == 30:
        # Benaqaab India closing stage - clean dark background
        im = create_base_canvas("cyber_dark.jpg", brightness=0.5)

    im.save(out_path, quality=94)
    print(f"  ✓ Saved clean plate: beat_{pad}.jpg")

print("All 30 clean evidence plates successfully generated!")
