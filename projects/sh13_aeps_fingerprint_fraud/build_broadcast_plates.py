import os
import sys
import math
from pathlib import Path
import numpy as np
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

def get_font(path, size):
    try:
        if path and os.path.exists(path):
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default()

W, H = 1080, 1920

# Load raw cache
raw_cache = {}
for f in os.listdir(RAW_DIR):
    p = RAW_DIR / f
    if p.is_file() and p.suffix.lower() in ['.jpg', '.png', '.jpeg']:
        try:
            raw_cache[f] = Image.open(p)
        except Exception as e:
            print(f"Failed opening {f}: e")

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

def create_rich_background(theme="dark_obsidian", blur=0, brightness=0.75):
    """Generates rich, full-bleed 1080x1920 background with volumetric lighting & organic noise grain."""
    im = Image.new("RGBA", (W, H), (6, 8, 15, 255))
    draw = ImageDraw.Draw(im)

    if theme == "stamped_paper" and "stamped_paper_india.jpg" in raw_cache:
        base = raw_cache["stamped_paper_india.jpg"].convert("RGBA")
        im = cover_fit(base, W, H)
        if blur > 0:
            im = im.filter(ImageFilter.GaussianBlur(blur))
        if brightness != 1.0:
            rgb = ImageEnhance.Brightness(im.convert("RGB")).enhance(brightness)
            im = rgb.convert("RGBA")
        return im

    elif theme == "sbi_branch" and "sbi_rural_branch.jpg" in raw_cache:
        base = raw_cache["sbi_rural_branch.jpg"].convert("RGBA")
        im = cover_fit(base, W, H)
        if blur > 0:
            im = im.filter(ImageFilter.GaussianBlur(blur))
        rgb = ImageEnhance.Brightness(im.convert("RGB")).enhance(brightness)
        im = rgb.convert("RGBA")
        return im

    elif theme == "currency_fan" and "indian_currency_fan.jpg" in raw_cache:
        base = raw_cache["indian_currency_fan.jpg"].convert("RGBA")
        im = cover_fit(base, W, H)
        if blur > 0:
            im = im.filter(ImageFilter.GaussianBlur(blur))
        rgb = ImageEnhance.Brightness(im.convert("RGB")).enhance(brightness)
        im = rgb.convert("RGBA")
        return im

    elif theme == "server_rack" and "server_rack.jpg" in raw_cache:
        base = raw_cache["server_rack.jpg"].convert("RGBA")
        im = cover_fit(base, W, H)
        if blur > 0:
            im = im.filter(ImageFilter.GaussianBlur(blur))
        rgb = ImageEnhance.Brightness(im.convert("RGB")).enhance(brightness)
        im = rgb.convert("RGBA")
        return im

    # Default: Deep Chromatic Obsidian with Volumetric Atmospheric Blooms (NO GRAPH PAPER GRID!)
    # Base dark chromatic gradient
    for y in range(H):
        t = y / H
        r = int(6 + t * 6)
        g = int(8 + t * 9)
        b = int(15 + t * 15)
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    # Ambient volumetric glow orbs
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    # Electric Sky cyan glow upper-right
    gd.ellipse([W - 400, 200, W + 300, 950], fill=(56, 189, 248, 28))
    # Crimson signal glow lower-left
    gd.ellipse([-250, H - 950, 450, H - 250], fill=(239, 68, 68, 24))
    # Ambient warm gold/indigo center bloom
    gd.ellipse([200, 700, 880, 1380], fill=(99, 102, 241, 16))
    glow = glow.filter(ImageFilter.GaussianBlur(140))
    im = Image.alpha_composite(im, glow)

    # Add subtle organic 35mm film grain (±4 intensity) to eliminate banding
    np_im = np.array(im, dtype=np.int16)
    noise = np.random.randint(-4, 5, (H, W, 4), dtype=np.int16)
    noise[:, :, 3] = 0 # keep alpha intact
    np_im = np.clip(np_im + noise, 0, 255).astype(np.uint8)
    im = Image.fromarray(np_im, mode="RGBA")

    return im

def add_cinematic_vignette(im, top_fade=220, bottom_fade=360):
    """Darkens top safe zone (for logo) and bottom safe zone (for caption pill)."""
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vd = ImageDraw.Draw(vignette)
    
    # Top gradient
    for y in range(top_fade):
        alpha = int(190 * (1.0 - y / top_fade))
        vd.line([(0, y), (W, y)], fill=(4, 6, 10, alpha))
        
    # Bottom gradient
    for y in range(H - bottom_fade, H):
        p = (y - (H - bottom_fade)) / bottom_fade
        alpha = int(220 * p)
        vd.line([(0, y), (W, y)], fill=(4, 6, 10, alpha))
        
    return Image.alpha_composite(im.convert("RGBA"), vignette)

def paste_asset(base_img, asset, cx, cy, max_w, max_h, shadow=True, border_color=None, border_w=3):
    if asset is None:
        return
    if isinstance(asset, str):
        if asset not in raw_cache:
            return
        asset = raw_cache[asset]

    asset_fitted = contain_fit(asset, max_w, max_h)
    aw, ah = asset_fitted.size
    px = cx - aw // 2
    py = cy - ah // 2

    if shadow:
        sh_w, sh_h = aw + 60, ah + 60
        sh = Image.new("RGBA", (sh_w, sh_h), (0, 0, 0, 0))
        sd = ImageDraw.Draw(sh)
        sd.rectangle([30, 30, aw + 30, ah + 30], fill=(0, 0, 0, 210))
        sh = sh.filter(ImageFilter.GaussianBlur(26))
        base_img.paste(sh, (px - 30, py - 30), sh)

    if border_color:
        card = Image.new("RGBA", (aw + border_w * 2, ah + border_w * 2), (0, 0, 0, 0))
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

# Helper to create simulated Land Registry Browser window (Jamabandi portal)
def draw_jamabandi_portal():
    card = Image.new("RGBA", (960, 940), (15, 23, 42, 248))
    d = ImageDraw.Draw(card)
    
    # Outer border
    d.rounded_rectangle([0, 0, 960, 940], radius=18, outline="#FBBF24", width=3)
    
    # Browser chrome bar
    d.rounded_rectangle([0, 0, 960, 70], radius=18, fill="#0F172A")
    d.rectangle([0, 50, 960, 70], fill="#0F172A")
    # Window dots
    d.ellipse([25, 25, 45, 45], fill="#EF4444")
    d.ellipse([55, 25, 75, 45], fill="#FBBF24")
    d.ellipse([85, 25, 105, 45], fill="#10B981")
    
    # URL bar
    d.rounded_rectangle([130, 16, 820, 54], radius=8, fill="#1E293B", outline="#475569", width=1)
    font_mono = get_font(FONT_MONO, 18)
    d.text((150, 24), "🔒 https://jamabandi.nic.in/PropertyDeed/SearchPublic", fill="#38BDF8", font=font_mono)
    
    # Portal Header
    font_space_bold = get_font(FONT_SPACE, 26)
    font_inter = get_font(FONT_INTER, 20)
    font_inter_bold = get_font(FONT_INTER, 22)
    
    d.text((40, 96), "GOVERNMENT LAND RECORDS PORTAL", fill="#F8FAFC", font=font_space_bold)
    d.text((40, 132), "Public Registry & Registered Sale Deeds (Kewala) Repository", fill="#94A3B8", font=font_inter)
    d.line([(40, 170), (920, 170)], fill="#334155", width=2)
    
    # Form filters
    fields = [
        ("SELECT DISTRICT:", "FARIDABAD (HARYANA)"),
        ("SELECT TEHSIL:", "BALLABGARH"),
        ("REGISTRATION YEAR:", "2022 - 2023"),
        ("DEED TYPE:", "REGISTERED SALE DEED (KEWALA)")
    ]
    y_pos = 195
    for label, val in fields:
        d.text((40, y_pos), label, fill="#FBBF24", font=get_font(FONT_SPACE, 18))
        d.rounded_rectangle([270, y_pos - 6, 920, y_pos + 36], radius=6, fill="#1E293B", outline="#475569", width=1)
        d.text((290, y_pos + 2), val, fill="#F8FAFC", font=font_mono)
        y_pos += 54
        
    d.line([(40, y_pos + 10), (920, y_pos + 10)], fill="#334155", width=2)
    y_pos += 26
    
    # Search Results Table
    d.text((40, y_pos), "SEARCH RESULTS: (PUBLIC UNMASKED BIOMETRICS DETECTED)", fill="#EF4444", font=font_space_bold)
    y_pos += 42
    
    # Table header
    d.rectangle([40, y_pos, 920, y_pos + 38], fill="#334155")
    d.text((55, y_pos + 8), "DEED #", fill="#FFFFFF", font=font_inter_bold)
    d.text((180, y_pos + 8), "EXECUTION DATE", fill="#FFFFFF", font=font_inter_bold)
    d.text((420, y_pos + 8), "AADHAAR LINKED", fill="#FFFFFF", font=font_inter_bold)
    d.text((680, y_pos + 8), "ACTION / DEED", fill="#FFFFFF", font=font_inter_bold)
    y_pos += 38
    
    # Row 1
    d.rectangle([40, y_pos, 920, y_pos + 72], fill="#1E293B")
    d.text((55, y_pos + 20), "4892/22", fill="#F8FAFC", font=font_mono)
    d.text((180, y_pos + 20), "12-OCT-2022", fill="#94A3B8", font=font_mono)
    d.text((420, y_pos + 20), "XXXX-XXXX-9120", fill="#EF4444", font=font_mono)
    # Download Button
    d.rounded_rectangle([680, y_pos + 12, 900, y_pos + 60], radius=8, fill="#EF4444")
    d.text((700, y_pos + 22), "DOWNLOAD PDF [PDF]", fill="#FFFFFF", font=get_font(FONT_SPACE, 16))
    y_pos += 76
    
    # Row 2
    d.rectangle([40, y_pos, 920, y_pos + 72], fill="#0F172A")
    d.text((55, y_pos + 20), "4893/22", fill="#F8FAFC", font=font_mono)
    d.text((180, y_pos + 20), "12-OCT-2022", fill="#94A3B8", font=font_mono)
    d.text((420, y_pos + 20), "XXXX-XXXX-3411", fill="#EF4444", font=font_mono)
    d.rounded_rectangle([680, y_pos + 12, 900, y_pos + 60], radius=8, fill="#EF4444")
    d.text((700, y_pos + 22), "DOWNLOAD PDF [PDF]", fill="#FFFFFF", font=get_font(FONT_SPACE, 16))
    y_pos += 96
    
    # Red Warning Tag Banner
    d.rounded_rectangle([40, y_pos, 920, y_pos + 72], radius=10, fill=(239, 68, 68, 55), outline="#EF4444", width=2)
    d.text((60, y_pos + 22), "SECURITY FLAW: CONTAINS UNMASKED HIGH-RES THUMBPRINT SCAN (NO 2FA)", fill="#EF4444", font=get_font(FONT_SPACE, 19))
    
    return card

# Helper to create Realistic 3D Silicone Cloned Thumb Macro Plate
def draw_silicone_thumb_plate():
    card = Image.new("RGBA", (960, 980), (10, 14, 23, 245))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, 960, 980], radius=24, outline="#A855F7", width=3)
    
    font_space_bold = get_font(FONT_SPACE, 26)
    font_mono = get_font(FONT_MONO, 20)
    d.text((45, 45), "FORENSIC EVIDENCE • EXHIBIT B-12", fill="#A855F7", font=font_space_bold)
    d.text((45, 85), "SEIZED ARTIFICIAL SILICONE THUMB REPLICA (POLYMER CLONE)", fill="#F8FAFC", font=get_font(FONT_INTER, 20))
    d.line([(45, 125), (915, 125)], fill="#334155", width=2)
    
    # Dark examination petri dish / specimen glass
    cx, cy = 480, 520
    d.ellipse([cx - 320, cy - 320, cx + 320, cy + 320], fill="#0A0F1D", outline="#475569", width=4)
    d.ellipse([cx - 280, cy - 280, cx + 280, cy + 280], outline=(56, 189, 248, 110), width=2)
    
    # Realistic flesh-tinted silicone thumb shape
    thumb_col = (235, 170, 145, 235)
    thumb_shad = (180, 120, 100, 245)
    d.ellipse([cx - 160, cy - 210, cx + 160, cy + 210], fill=thumb_col, outline=thumb_shad, width=8)
    
    # Biometric ridges (concentric wavy whorls)
    for r in range(25, 150, 14):
        d.ellipse([cx - 30 - r, cy - 30 - r, cx - 30 + r, cy - 30 + r], outline=(170, 100, 80, 180), width=3)
        
    # Specular rim highlight on silicone curve
    d.arc([cx - 150, cy - 200, cx + 150, cy + 200], start=180, end=270, fill=(255, 230, 220, 255), width=6)
    
    # Metal Tweezers holding edge
    d.line([(cx + 140, cy), (cx + 380, cy - 80)], fill="#94A3B8", width=16)
    d.line([(cx + 140, cy + 30), (cx + 380, cy + 40)], fill="#64748B", width=14)
    
    # Forensic Scale Ruler at bottom
    rx, ry = 160, 860
    d.line([(rx, ry), (rx + 640, ry)], fill="#FFFFFF", width=4)
    for i in range(9):
        x = rx + i * 80
        d.line([(x, ry - 15), (x, ry + 15)], fill="#FFFFFF", width=3)
        d.text((x - 12, ry + 22), f"{i} CM", fill="#94A3B8", font=font_mono)
        
    # Technical Tag
    d.rounded_rectangle([600, 750, 915, 830], radius=8, fill=(168, 85, 247, 51), outline="#A855F7", width=2)
    d.text((615, 770), "RIDGE DEPTH: 0.35 mm", fill="#FFFFFF", font=font_mono)
    d.text((615, 796), "MATERIAL: RTV SILICONE", fill="#A855F7", font=font_mono)
    
    return card

# Helper to create Dedicated Mantra MFS100 Biometric Terminal Station (Beats 19 & 26)
def draw_scanner_terminal_plate(mode="active"):
    card = Image.new("RGBA", (960, 960), (10, 14, 23, 248))
    d = ImageDraw.Draw(card)
    
    border_col = "#22C55E" if mode == "active" else "#EF4444"
    d.rounded_rectangle([0, 0, 960, 960], radius=24, outline=border_col, width=3)
    
    font_space_bold = get_font(FONT_SPACE, 26)
    font_mono = get_font(FONT_MONO, 20)
    font_inter = get_font(FONT_INTER, 20)
    
    if mode == "active":
        d.text((45, 45), "FORENSIC HARDWARE AUDIT • STEP 3", fill="#22C55E", font=font_space_bold)
        d.text((45, 85), "MANTRA MFS100 OPTICAL SENSOR (500 DPI RESOLUTION)", fill="#F8FAFC", font=font_inter)
    else:
        d.text((45, 45), "TRANSACTION SECURITY PROTOCOL • REJECTED", fill="#EF4444", font=font_space_bold)
        d.text((45, 85), "MANTRA MFS100 • RESPONSE CODE: ERROR 330 (LOCKED)", fill="#F8FAFC", font=font_inter)
    d.line([(45, 125), (915, 125)], fill="#334155", width=2)
    
    # Examination Tray Stage
    tray_w, tray_h = 760, 560
    tx = (960 - tray_w) // 2
    ty = 175
    
    # Tray drop shadow
    sh = Image.new("RGBA", (tray_w + 40, tray_h + 40), (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([20, 20, tray_w + 20, tray_h + 20], radius=20, fill=(0, 0, 0, 230))
    sh = sh.filter(ImageFilter.GaussianBlur(24))
    card.paste(sh, (tx - 20, ty - 20), sh)
    
    # Pure studio examination tray
    tray = Image.new("RGBA", (tray_w, tray_h), (255, 255, 255, 255))
    td = ImageDraw.Draw(tray)
    
    # Centered Mantra photo (box + scanner)
    if "mantra_indiamart.png" in raw_cache:
        mantra_img = raw_cache["mantra_indiamart.png"]
        mantra_fit = mantra_img.resize((520, 520), Image.Resampling.LANCZOS)
        tray.paste(mantra_fit, ((tray_w - 520) // 2, 20))
        
    # Metric scale tick marks on top & bottom borders
    for x in range(0, tray_w, 40):
        td.line([(x, 0), (x, 10)], fill=(180, 180, 180), width=2)
        td.line([(x, tray_h - 10), (x, tray_h)], fill=(180, 180, 180), width=2)
        
    tray_outline = "#22C55E" if mode == "active" else "#EF4444"
    td.rounded_rectangle([0, 0, tray_w, tray_h], radius=16, outline=tray_outline, width=3)
    card.paste(tray, (tx, ty))
    d = ImageDraw.Draw(card)
    
    # Scanner prism coordinate on card
    px, py = tx + 465, ty + 195
    
    if mode == "active":
        # Laser reticle on scanner glass
        d.ellipse([px - 50, py - 40, px + 50, py + 40], outline="#22C55E", width=4)
        d.line([(px - 80, py), (px + 80, py)], fill="#34D399", width=4)
        
        # Technical Readout Badge
        d.rounded_rectangle([80, 770, 880, 890], radius=12, fill=(34, 197, 94, 40), outline="#22C55E", width=2)
        d.text((105, 800), "WARNING: OLDER L0 OPTICAL SENSOR HAS ZERO LIVENESS DETECTION", fill="#34D399", font=get_font(FONT_SPACE, 22))
        d.text((105, 842), "STQC L0 • PRISM SENSES SURFACE RIDGES WITHOUT BLOOD PULSE CHECK", fill="#FFFFFF", font=font_mono)
    else:
        # Red X on scanner glass
        d.ellipse([px - 50, py - 40, px + 50, py + 40], outline="#EF4444", width=6)
        d.line([(px - 35, py - 25), (px + 35, py + 25)], fill="#EF4444", width=6)
        d.line([(px + 35, py - 25), (px - 35, py + 25)], fill="#EF4444", width=6)
        
        # Rejection badge
        d.rounded_rectangle([80, 770, 880, 890], radius=12, fill=(239, 68, 68, 50), outline="#EF4444", width=2)
        d.text((105, 800), "DECLINED: UIDAI CIDR RESPONSE ERROR 330 (BIOMETRICS LOCKED)", fill="#EF4444", font=get_font(FONT_SPACE, 22))
        d.text((105, 842), "BIOMETRIC LOCKED BY CITIZEN • SERVER BLOCKS 100% DISBURSEMENT", fill="#FFFFFF", font=font_mono)
        
    return card

# Helper to create UV Light Poly-Stamper Curing Machine Plate
def draw_uv_machine_plate():
    card = Image.new("RGBA", (960, 940), (10, 14, 23, 245))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, 960, 940], radius=24, outline="#EC4899", width=3)
    
    font_space_bold = get_font(FONT_SPACE, 26)
    font_mono = get_font(FONT_MONO, 22)
    
    d.text((45, 45), "BIOMETRIC FORGERY LAB • STEP 2", fill="#EC4899", font=font_space_bold)
    d.text((45, 85), "UV POLY-STAMPER EXPOSURE & CURING MACHINE", fill="#F8FAFC", font=get_font(FONT_INTER, 20))
    d.line([(45, 125), (915, 125)], fill="#334155", width=2)
    
    # Machine Chassis Box
    d.rounded_rectangle([100, 160, 860, 760], radius=20, fill="#1E1B4B", outline="#4338CA", width=4)
    
    # Glowing UV Curing Chamber
    d.rounded_rectangle([150, 220, 810, 640], radius=12, fill="#3B0764", outline="#EC4899", width=4)
    
    # 3 Glowing Violet UV Tubes
    for ty in [280, 420, 560]:
        d.rounded_rectangle([180, ty, 780, ty + 50], radius=25, fill="#F472B6")
        d.line([(200, ty + 25), (760, ty + 25)], fill="#FFFFFF", width=8)
        
    # UV Glow diffusion
    glow = Image.new("RGBA", (960, 940), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([200, 240, 760, 620], fill=(236, 72, 153, 90))
    glow = glow.filter(ImageFilter.GaussianBlur(40))
    card = Image.alpha_composite(card, glow)
    d = ImageDraw.Draw(card)
    
    # Machine Control Deck
    d.rounded_rectangle([150, 670, 810, 740], radius=8, fill="#0F172A", outline="#475569", width=2)
    d.text((180, 690), "EXPOSURE TIMER: 03:30 MIN", fill="#34D399", font=font_mono)
    d.text((580, 690), "UV WAVE: 365 nm ACTIVE", fill="#EC4899", font=font_mono)
    
    # Status Alert at bottom
    d.rounded_rectangle([100, 800, 860, 880], radius=12, fill=(236, 72, 153, 38), outline="#EC4899", width=2)
    d.text((140, 828), "PHOTO-POLYMER GEL HARDENS INTO 3D RIGID STAMP MOULD", fill="#F8FAFC", font=get_font(FONT_SPACE, 20))
    
    return card

# Helper to create Tracing Butter Paper on Light Box Plate
def draw_butter_paper_plate():
    card = Image.new("RGBA", (960, 940), (12, 16, 26, 245))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, 960, 940], radius=24, outline="#FBBF24", width=3)
    
    font_space_bold = get_font(FONT_SPACE, 26)
    font_mono = get_font(FONT_MONO, 20)
    
    d.text((45, 45), "BIOMETRIC FORGERY LAB • STEP 1", fill="#FBBF24", font=font_space_bold)
    d.text((45, 85), "TRACING THUMBPRINT RIDGES ONTO BUTTER PAPER", fill="#F8FAFC", font=get_font(FONT_INTER, 20))
    d.line([(45, 125), (915, 125)], fill="#334155", width=2)
    
    # Lightbox Stage
    d.rounded_rectangle([80, 160, 880, 780], radius=16, fill="#FFFBEB", outline="#F59E0B", width=4)
    
    # Stamped deed page underneath at 50% opacity
    d.rectangle([130, 200, 830, 740], fill="#FDE68A")
    d.text((160, 230), "GOVERNMENT OF HARYANA • REVENUE STAMP", fill="#78350F", font=get_font(FONT_SPACE, 20))
    d.text((160, 270), "REGISTRATION ACT 1908 • SALE DEED # 4892", fill="#92400E", font=font_mono)
    
    # Official Ink Thumbprint on document
    d.ellipse([400, 360, 600, 580], fill="#1E3A8A", outline="#172554", width=4)
    for r in range(15, 95, 12):
        d.ellipse([470 - r, 460 - r, 470 + r, 460 + r], outline="#93C5FD", width=2)
        
    # Semi-translucent Butter Paper Sheet over thumbprint
    bp = Image.new("RGBA", (500, 420), (255, 255, 255, 190))
    bpd = ImageDraw.Draw(bp)
    bpd.rectangle([0, 0, 500, 420], outline="#D97706", width=3)
    for r in range(15, 80, 12):
        bpd.ellipse([250 - r, 210 - r, 250 + r, 210 + r], outline="#000000", width=4)
    card.paste(bp, (250, 300), bp)
    
    # Drafting Pen pointing at paper
    d = ImageDraw.Draw(card)
    d.line([(480, 480), (680, 300)], fill="#000000", width=14)
    d.polygon([(480, 480), (510, 450), (450, 510)], fill="#94A3B8")
    d.ellipse([475, 475, 485, 485], fill="#EF4444")
    
    # Status pill at bottom
    d.rounded_rectangle([80, 810, 880, 890], radius=12, fill=(251, 191, 36, 51), outline="#FBBF24", width=2)
    d.text((110, 840), "HIGH-RES BIOMETRIC RIDGES TRANSFERRED WITH BLACK GEL INK", fill="#FFFFFF", font=get_font(FONT_SPACE, 20))
    
    return card

# Helper to create Emergency Helpline 1930 Plate
def draw_helpline_plate():
    card = Image.new("RGBA", (960, 940), (10, 14, 23, 245))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, 960, 940], radius=24, outline="#FBBF24", width=4)
    
    font_space_bold = get_font(FONT_SPACE, 28)
    font_mono = get_font(FONT_MONO, 22)
    
    d.text((45, 45), "MINISTRY OF HOME AFFAIRS (MHA) • I4C", fill="#FBBF24", font=font_space_bold)
    d.text((45, 90), "CITIZEN FINANCIAL CYBER FRAUD REPORTING SYSTEM", fill="#F8FAFC", font=get_font(FONT_INTER, 20))
    d.line([(45, 135), (915, 135)], fill="#334155", width=2)
    
    # Giant Glowing Speed Dial 1930
    d.rounded_rectangle([120, 180, 840, 520], radius=24, fill="#1E293B", outline="#FBBF24", width=4)
    
    font_anton = get_font(FONT_ANTON, 140)
    d.text((480, 230), "1930", fill="#FBBF24", font=font_anton, anchor="mt")
    
    font_space = get_font(FONT_SPACE, 26)
    d.text((480, 410), "NATIONAL CYBER CRIME HELPLINE (TOLL-FREE)", fill="#FFFFFF", font=font_space, anchor="mt")
    d.text((480, 455), "DIAL WITHIN 2 HOURS ('GOLDEN HOUR') TO FREEZE MONEY", fill="#34D399", font=font_mono, anchor="mt")
    
    # Web Portal Card below
    d.rounded_rectangle([120, 560, 840, 740], radius=16, fill="#0F172A", outline="#38BDF8", width=3)
    d.text((150, 595), "OFFICIAL REPORTING PORTAL:", fill="#94A3B8", font=font_mono)
    d.text((150, 635), "cybercrime.gov.in", fill="#38BDF8", font=get_font(FONT_SPACE, 34))
    d.text((150, 685), "Directly integrates with RBI, NPCI, & 250+ Banks for auto-freeze", fill="#FFFFFF", font=get_font(FONT_INTER, 18))
    
    # Warning footer
    d.rounded_rectangle([120, 770, 840, 870], radius=16, fill=(239, 68, 68, 51), outline="#EF4444", width=2)
    d.text((480, 815), "REPORT IMMEDIATELY BEFORE CASH IS WITHDRAWN AT ATM", fill="#FFFFFF", font=font_space_bold, anchor="mt")
    
    return card

# Helper to create Cyber Defense Shield Plate
def draw_cyber_shield_plate():
    card = Image.new("RGBA", (960, 940), (10, 14, 23, 245))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, 960, 940], radius=24, outline="#38BDF8", width=3)
    
    font_space_bold = get_font(FONT_SPACE, 28)
    font_mono = get_font(FONT_MONO, 22)
    
    d.text((45, 45), "CITIZEN PROTECTION PROTOCOL", fill="#38BDF8", font=font_space_bold)
    d.text((45, 90), "BIOMETRIC LOCKING VIA mAadhaar APP", fill="#F8FAFC", font=get_font(FONT_INTER, 20))
    d.line([(45, 135), (915, 135)], fill="#334155", width=2)
    
    # Hexagonal Security Shield in center
    cx, cy = 480, 480
    r = 240
    points = []
    for i in range(6):
        angle = math.radians(60 * i - 30)
        px = cx + r * math.cos(angle)
        py = cy + r * math.sin(angle)
        points.append((px, py))
        
    d.polygon(points, fill="#0F172A", outline="#38BDF8")
    d.line(points + [points[0]], fill="#38BDF8", width=8)
    
    # Internal Padlock Icon
    d.rectangle([cx - 70, cy - 20, cx + 70, cy + 100], fill="#10B981")
    d.ellipse([cx - 50, cy - 90, cx + 50, cy + 10], outline="#10B981", width=16)
    
    # UIDAI Text
    d.text((cx, cy + 160), "UIDAI CIDR IMMUNITY ACTIVE", fill="#38BDF8", font=font_space_bold, anchor="mt")
    d.text((cx, cy + 205), "All AePS Fingerprint Requests Auto-Rejected", fill="#FFFFFF", font=font_mono, anchor="mt")
    
    # Info Pill at bottom
    d.rounded_rectangle([100, 770, 860, 870], radius=16, fill=(52, 211, 153, 51), outline="#34D399", width=2)
    d.text((480, 815), "100% IMMUNIZED AGAINST SILICONE CLONES", fill="#34D399", font=font_space_bold, anchor="mt")
    
    return card

# Helper to create Crime Investigation Board Plate (Beat 29)
def draw_evidence_board_plate():
    card = Image.new("RGBA", (W, H), (10, 14, 22, 255))
    d = ImageDraw.Draw(card)
    
    # Ambient background glows
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.ellipse([100, 300, 980, 1200], fill=(239, 68, 68, 25))
    glow = glow.filter(ImageFilter.GaussianBlur(100))
    card = Image.alpha_composite(card, glow)
    d = ImageDraw.Draw(card)
    
    # Upper Evidence: Newspaper Clipping Bust
    paste_asset(card, "news_clipping_bust.png", 540, 780, 940, 480, shadow=True, border_color="#EF4444", border_w=3)
    # Lower Evidence: Error 330 Thermal Slip
    paste_asset(card, "pos_receipt_error330.png", 540, 1260, 620, 700, shadow=True, border_color="#38BDF8", border_w=3)
    
    # Red Evidence Thread connecting the two items
    d.line([(280, 860), (420, 1080)], fill="#EF4444", width=6)
    # Push pins
    for px, py in [(280, 860), (420, 1080)]:
        d.ellipse([px - 14, py - 14, px + 14, py + 14], fill="#DC2626", outline="#FFFFFF", width=3)
        
    return card

# --- MAIN GENERATION PIPELINE FOR ALL 30 PLATES ---
print("Generating 30 Full-Bleed Broadcast Evidence Plates (No Slop, No Grid)...")

for beat_id in range(1, 31):
    pad = f"{beat_id:02d}"
    out_path = VISUALS_DIR / f"beat_{pad}.jpg"

    if beat_id == 1:
        # Full bleed 500 Rupee banknote fan + news clipping flaw
        im = create_rich_background("currency_fan", brightness=0.7)
        paste_asset(im, "news_clipping_flaw.png", 540, 1140, 920, 460, shadow=True, border_color="#EF4444", border_w=3)

    elif beat_id == 2:
        # REAL AUTHENTIC RuPay DEBIT CARD with high-contrast cancellation stamp
        im = create_rich_background("dark_obsidian", brightness=0.85)
        paste_asset(im, "rupay_debit_card.jpg", 540, 960, 940, 620, shadow=True, border_color="#38BDF8", border_w=4)
        # Red strike ring
        d = ImageDraw.Draw(im)
        d.ellipse([340, 760, 740, 1160], outline="#EF4444", width=14)
        d.line([410, 830, 670, 1090], fill="#EF4444", width=14)

    elif beat_id == 3:
        # Real State Bank of India rural branch full-bleed + currency fan
        im = create_rich_background("sbi_branch", brightness=0.75)
        paste_asset(im, "indian_currency_fan.jpg", 540, 1120, 880, 500, shadow=True, border_color="#EF4444", border_w=4)

    elif beat_id == 4:
        # Cyber dark workstation + AePS flaw clipping
        im = create_rich_background("dark_obsidian", brightness=0.8)
        paste_asset(im, "news_clipping_flaw.png", 540, 960, 940, 480, shadow=True, border_color="#38BDF8", border_w=3)

    elif beat_id == 5:
        # REALISTIC 3D SILICONE THUMB EXHIBIT PLATE!
        im = create_rich_background("dark_obsidian", brightness=0.8)
        silicone_card = draw_silicone_thumb_plate()
        im.paste(silicone_card, (60, 420), silicone_card)

    elif beat_id == 6:
        # Real Police Seizure Newspaper Clipping: 600+ Cloned Thumbs Seized
        im = create_rich_background("dark_obsidian", brightness=0.8)
        paste_asset(im, "news_clipping_bust.png", 540, 960, 960, 520, shadow=True, border_color="#EF4444", border_w=4)

    elif beat_id == 7:
        # Official NPCI AePS Architecture Diagram
        im = create_rich_background("server_rack", brightness=0.65)
        paste_asset(im, "aeps_diagram.png", 540, 960, 980, 720, shadow=True, border_color="#38BDF8", border_w=4)

    elif beat_id == 8:
        # State Bank of India rural branch (Full Bleed)
        im = create_rich_background("sbi_branch", brightness=0.85)

    elif beat_id == 9:
        # Authentic Newspaper Clipping: AePS Zero OTP Flaw
        im = create_rich_background("server_rack", brightness=0.7)
        paste_asset(im, "news_clipping_flaw.png", 540, 960, 960, 500, shadow=True, border_color="#EF4444", border_w=4)

    elif beat_id == 10:
        # SIMULATED JAMABANDI / LAND REGISTRY PORTAL!
        im = create_rich_background("dark_obsidian", brightness=0.8)
        portal_card = draw_jamabandi_portal()
        im.paste(portal_card, (60, 390), portal_card)

    elif beat_id == 11:
        # Full-Bleed Ultra HD Indian Stamped Paper Scan
        im = create_rich_background("stamped_paper", brightness=0.92)

    elif beat_id == 12:
        # Zoomed stamped paper scan where authentic thumbprints exist
        im = create_rich_background("stamped_paper", brightness=0.88)

    elif beat_id == 13:
        # Stamped paper with Official Aadhaar Card Specimen
        im = create_rich_background("stamped_paper", brightness=0.82)
        paste_asset(im, "aadhaar_specimen.png", 540, 960, 960, 380, shadow=True, border_color="#EF4444", border_w=4)

    elif beat_id == 14:
        # Portal deed download screen
        im = create_rich_background("dark_obsidian", brightness=0.8)
        portal_card = draw_jamabandi_portal()
        im.paste(portal_card, (60, 390), portal_card)

    elif beat_id == 15:
        # BUTTER PAPER TRACING ON LIGHT BOX!
        im = create_rich_background("dark_obsidian", brightness=0.8)
        bp_card = draw_butter_paper_plate()
        im.paste(bp_card, (60, 420), bp_card)

    elif beat_id == 16:
        # UV POLY-STAMPER CURING MACHINE PLATE!
        im = create_rich_background("dark_obsidian", brightness=0.8)
        uv_card = draw_uv_machine_plate()
        im.paste(uv_card, (60, 420), uv_card)

    elif beat_id == 17:
        # 3D SILICONE THUMB CLONE MACRO!
        im = create_rich_background("dark_obsidian", brightness=0.8)
        silicone_card = draw_silicone_thumb_plate()
        im.paste(silicone_card, (60, 420), silicone_card)

    elif beat_id == 18:
        # Scammer POS counter at rural SBI CSP
        im = create_rich_background("sbi_branch", brightness=0.7)
        paste_asset(im, "pos_receipt_success.png", 540, 960, 720, 880, shadow=True)

    elif beat_id == 19:
        # DEDICATED MANTRA MFS100 TERMINAL (ACTIVE SCANNING MODE)
        im = create_rich_background("dark_obsidian", brightness=0.85)
        station_card = draw_scanner_terminal_plate(mode="active")
        im.paste(station_card, (60, 420), station_card)

    elif beat_id == 20:
        # Authentic POS Receipt Approved Slip
        im = create_rich_background("server_rack", brightness=0.7)
        paste_asset(im, "pos_receipt_success.png", 540, 960, 740, 900, shadow=True)

    elif beat_id == 21:
        # Full-Bleed Currency Fan (₹10,000 Heist)
        im = create_rich_background("currency_fan", brightness=0.75)

    elif beat_id == 22:
        # CYBER DEFENSE SHIELD FOR CITIZENS!
        im = create_rich_background("dark_obsidian", brightness=0.85)
        shield_card = draw_cyber_shield_plate()
        im.paste(shield_card, (60, 420), shield_card)

    elif beat_id == 23:
        # Official Android phone with mAadhaar App
        im = create_rich_background("dark_obsidian", brightness=0.85)
        paste_asset(im, "maadhaar_phone_screen.png", 540, 960, 840, 1340, shadow=True)

    elif beat_id == 24:
        # mAadhaar App Biometrics Settings Lock
        im = create_rich_background("dark_obsidian", brightness=0.85)
        paste_asset(im, "maadhaar_phone_screen.png", 540, 960, 840, 1340, shadow=True)

    elif beat_id == 25:
        # UIDAI CIDR Server Immunity
        im = create_rich_background("server_rack", brightness=0.75)
        paste_asset(im, "aeps_diagram.png", 540, 960, 960, 680, shadow=True, border_color="#34D399", border_w=4)

    elif beat_id == 26:
        # DEDICATED MANTRA MFS100 TERMINAL (REJECTED ERROR 330 MODE)
        im = create_rich_background("dark_obsidian", brightness=0.85)
        station_card = draw_scanner_terminal_plate(mode="rejected")
        im.paste(station_card, (60, 420), station_card)

    elif beat_id == 27:
        # Authentic POS Receipt: ERROR 330 BIOMETRIC LOCKED!
        im = create_rich_background("dark_obsidian", brightness=0.75)
        paste_asset(im, "pos_receipt_error330.png", 540, 960, 760, 920, shadow=True)

    elif beat_id == 28:
        # NATIONAL CYBER HELPLINE 1930 CARD!
        im = create_rich_background("dark_obsidian", brightness=0.85)
        helpline_card = draw_helpline_plate()
        im.paste(helpline_card, (60, 420), helpline_card)

    elif beat_id == 29:
        # Complete evidence board (Police Bust + Error 330 Receipt + Connecting Pins)
        im = draw_evidence_board_plate()

    elif beat_id == 30:
        # Benaqaab India closing stage - rich obsidian with glowing background
        im = create_rich_background("dark_obsidian", brightness=0.6)

    # Apply cinematic vignette to guarantee pristine top logo & bottom caption readability
    im = add_cinematic_vignette(im)
    im = im.convert("RGB")
    im.save(out_path, quality=94)
    print(f"  ✓ Saved broadcast plate: beat_{pad}.jpg")

print("All 30 broadcast evidence plates successfully regenerated!")
