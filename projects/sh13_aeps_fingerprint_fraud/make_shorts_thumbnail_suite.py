#!/usr/bin/env python3
"""
make_shorts_thumbnail_suite.py — Broadcast Master AI Thumbnail Suite (9:16 & 16:9)
Episode SH-13: AePS Aadhaar Fingerprint Fraud (Silicone Ungli Scam)
Channel: Benaqaab India (बेनाक़ाब इंडिया) • Sach · Saboot · Bebak

Generates 3 Distinct High-CTR YouTube Shorts (9:16) Master Thumbnails + 1 Widescreen (16:9) Cover:
1. Option 1: The Silicone Finger Shock Hook (Hero Clone Thumb + ₹10,000 SAAF!)
2. Option 2: The Land Registry Data Leak (Official Stamp Paper + Unmasked Thumbprint + Scanner)
3. Option 3: The 60-Second Citizen Shield (mAadhaar Lock + Error 330 Immune Badge)
"""

import os
import sys
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PROJECT_DIR = Path(__file__).resolve().parent
WORKSPACE = PROJECT_DIR.parent.parent

# Brand Fonts
FONT_ANTON = WORKSPACE / "brand" / "fonts" / "Anton.ttf"
FONT_INTER = WORKSPACE / "brand" / "fonts" / "Inter.ttf"
FONT_MONO = WORKSPACE / "brand" / "fonts" / "JetBrainsMono.ttf"
FONT_SPACE = WORKSPACE / "brand" / "fonts" / "SpaceGrotesk.ttf"
FONT_DEVANAGARI = WORKSPACE / "brand" / "fonts" / "NotoSansDevanagari.ttf"
LOGO_PATH = WORKSPACE / "brand" / "logo.png"

# Visual Assets
BEAT_01 = PROJECT_DIR / "assets" / "visuals" / "beat_01.jpg" # Debit alert
BEAT_05 = PROJECT_DIR / "assets" / "visuals" / "beat_05.jpg" # Silicone fake thumb
BEAT_12 = PROJECT_DIR / "assets" / "visuals" / "beat_12.jpg" # Registry deed thumbprint
BEAT_19 = PROJECT_DIR / "assets" / "visuals" / "beat_19.jpg" # Mantra L0 scanner station
BEAT_21 = PROJECT_DIR / "assets" / "visuals" / "beat_21.jpg" # ₹10,000 odometer debit
BEAT_27 = PROJECT_DIR / "assets" / "visuals" / "beat_27.jpg" # Error 330 Locked

REAL_MANTRA = PROJECT_DIR / "assets" / "real_sources" / "mantra_indiamart.png"
REAL_STAMP = PROJECT_DIR / "assets" / "real_sources" / "stamped_paper_india.jpg"

OUT_OPT1 = PROJECT_DIR / "Shorts_Thumb_01_Silicone_Ungli.jpg"
OUT_OPT2 = PROJECT_DIR / "Shorts_Thumb_02_Registry_Leak.jpg"
OUT_OPT3 = PROJECT_DIR / "Shorts_Thumb_03_Citizen_Shield.jpg"
OUT_PRIMARY = PROJECT_DIR / "SH13_Thumbnail_9x16.jpg"
OUT_16X9 = PROJECT_DIR / "SH13_Thumbnail_16x9.jpg"

def get_font(path, size):
    try:
        return ImageFont.truetype(str(path), size)
    except Exception:
        return ImageFont.load_default()

def draw_top_left_brand(canvas, scale=1.3):
    draw = ImageDraw.Draw(canvas)
    pw = int(320 * scale)
    ph = int(62 * scale)
    x, y = int(50 * scale), int(50 * scale)
    
    # Frosted glass background
    draw.rounded_rectangle([x, y, x + pw, y + ph], radius=int(31 * scale), fill=(10, 14, 23, 245), outline=(251, 191, 36), width=int(2.5 * scale))
    
    # Red circle avatar
    cx = x + int(32 * scale)
    cy = y + int(31 * scale)
    r = int(18 * scale)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(239, 68, 68))
    
    # White Benaqaab text
    font_bold = get_font(FONT_ANTON, int(23 * scale))
    draw.text((x + int(60 * scale), y + int(10 * scale)), "BENAQAAB INDIA", font=font_bold, fill=(255, 255, 255))
    font_sub = get_font(FONT_MONO, int(11 * scale))
    draw.text((x + int(62 * scale), y + int(35 * scale)), "SACH · SABOOT · BEBAK", font=font_sub, fill=(251, 191, 36))

def draw_badge(draw, text, xy, font, bg_color, text_color, pad_x=28, pad_y=14, radius=16, border_color=None, border_width=2, icon_type=None):
    x, y = xy
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    icon_w = 0
    if icon_type == "alert":
        icon_w = th + 18
    elif icon_type == "dot":
        icon_w = 26
        
    w = tw + pad_x * 2 + icon_w
    h = th + pad_y * 2
    
    draw.rounded_rectangle([x, y, x + w, y + h], radius=int(radius), fill=bg_color, outline=border_color, width=int(border_width))
    
    curr_x = x + pad_x
    if icon_type == "alert":
        cx = curr_x + (th // 2)
        cy = y + (h // 2)
        r = th // 2
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, 240))
        draw.line([(cx, cy - r + 4), (cx, cy + 2)], fill=(225, 29, 72, 255), width=3)
        draw.ellipse([cx - 2, cy + 4, cx + 2, cy + 8], fill=(225, 29, 72, 255))
        curr_x += th + 16
    elif icon_type == "dot":
        cx = curr_x + 10
        cy = y + (h // 2)
        draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(244, 63, 94, 255))
        curr_x += 26
        
    draw.text((curr_x, y + pad_y - 2), text, font=font, fill=text_color)
    return w, h

def draw_rubber_stamp(canvas, text, xy, font_size=52, angle=-9, color=(239, 68, 68)):
    font = get_font(FONT_ANTON, font_size)
    dummy_draw = ImageDraw.Draw(canvas)
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    pad_x, pad_y = 32, 16
    sw = tw + pad_x * 2
    sh = th + pad_y * 2
    
    stamp = Image.new("RGBA", (sw + 60, sh + 60), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(stamp)
    sdraw.rounded_rectangle([15, 15, sw + 15, sh + 15], radius=16, outline=color, width=6)
    sdraw.rounded_rectangle([23, 23, sw + 7, sh + 7], radius=10, outline=color, width=2)
    sdraw.text((pad_x + 15, pad_y + 9), text, font=font, fill=color)
    
    rotated = stamp.rotate(angle, resample=Image.BICUBIC, expand=True)
    canvas.paste(rotated, xy, rotated)

def draw_3d_text(draw, text, xy, font, fill_color, shadow_color=(0, 0, 0), depth=8):
    x, y = xy
    for d in range(depth, 0, -1):
        draw.text((x + d, y + d), text, font=font, fill=shadow_color)
    draw.text((x, y), text, font=font, fill=fill_color)

# ==============================================================================
# OPTION 1: THE SILICONE FINGER SHOCK HOOK (HERO MACRO THUMB + ₹10,000 SAAF!)
# ==============================================================================
def create_thumb_option_1():
    print("🎨 Creating Option 1: Silicone Clone Shock Hook (9:16)...")
    W, H = 1080, 1920
    canvas = Image.new("RGB", (W, H), (7, 9, 14))
    
    # Hero visual: Macro silicone clone thumb (beat_05)
    if BEAT_05.exists():
        im = Image.open(BEAT_05).convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(im).enhance(1.18)
        enh = ImageEnhance.Color(enh).enhance(1.15)
        canvas.paste(enh, (0, 0))
        
    # Top and Bottom cinematic gradient darkeners for pristine readability
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    for y in range(0, 750):
        t = 1.0 - (y / 750.0)
        odraw.line([(0, y), (W, y)], fill=(7, 9, 14, int(240 * t)))
    for y in range(1150, H):
        t = (y - 1150) / (H - 1150.0)
        odraw.line([(0, y), (W, y)], fill=(7, 9, 14, int(235 * t)))
    canvas.paste(overlay, (0, 0), overlay)
    
    draw = ImageDraw.Draw(canvas)
    draw_top_left_brand(canvas, scale=1.35)
    
    # Critical Alert Badge (Upper Right Safe Zone)
    font_alert = get_font(FONT_MONO, 24)
    draw_badge(draw, "CRITICAL BANKING ALERT", (68, 220), font_alert, (225, 29, 72), (255, 255, 255), pad_x=24, pad_y=12, radius=14, icon_type="alert")
    
    # Curiosity Hook Pill
    font_curiosity = get_font(FONT_ANTON, 38)
    draw_badge(draw, "ZERO OTP · ZERO ATM CARD", (68, 320), font_curiosity, (251, 191, 36), (10, 14, 23), pad_x=30, pad_y=12, radius=16)
    
    # Giant High-CTR Typography in Upper Safe Zone (Readable on phone screens)
    font_headline_1 = get_font(FONT_ANTON, 126)
    font_headline_2 = get_font(FONT_ANTON, 108)
    
    draw_3d_text(draw, "₹10,000 SAAF!", (68, 440), font_headline_1, fill_color=(255, 255, 255), depth=10)
    draw_3d_text(draw, "NAKLI UNGLI SE?!", (68, 580), font_headline_2, fill_color=(239, 68, 68), depth=8)
    
    # High-impact angled forensic stamp
    draw_rubber_stamp(canvas, "689+ CLONES SEIZED", (80, 1260), font_size=56, angle=-8, color=(239, 68, 68))
    
    # Lower Remedy Pill
    font_shield = get_font(FONT_MONO, 26)
    draw_badge(draw, "CITIZEN SHIELD: LOCK BIOMETRICS IN mAadhaar", (68, 1480), font_shield, (15, 23, 42), (56, 189, 248), pad_x=28, pad_y=16, radius=18, border_color=(56, 189, 248), border_width=3)
    
    canvas.save(OUT_OPT1, quality=96)
    print(f"✅ Option 1 Saved: {OUT_OPT1}")
    return canvas

# ==============================================================================
# OPTION 2: THE LAND REGISTRY DATA LEAK (DEED STAMP PAPER + SCANNER EVIDENCE)
# ==============================================================================
def create_thumb_option_2():
    print("🎨 Creating Option 2: Land Registry Data Leak (9:16)...")
    W, H = 1080, 1920
    canvas = Image.new("RGB", (W, H), (7, 9, 14))
    
    # Background: Authentic stamped registry deed (beat_12)
    if BEAT_12.exists():
        im = Image.open(BEAT_12).convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(im).enhance(1.15)
        canvas.paste(enh, (0, 0))
        
    # Overlay real Mantra MFS100 device in the middle/lower hero zone
    if REAL_MANTRA.exists():
        mantra = Image.open(REAL_MANTRA).convert("RGBA")
        mw = 720
        mh = int(mantra.height * (mw / mantra.width))
        mantra_resized = mantra.resize((mw, mh), Image.Resampling.LANCZOS)
        
        # Center horizontally, place at y = 880
        mx = (W - mw) // 2
        my = 880
        
        # Ambient cyan/emerald backlight behind scanner
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.ellipse([mx - 60, my - 60, mx + mw + 60, my + mh + 60], fill=(56, 189, 248, 120))
        glow = glow.filter(ImageFilter.GaussianBlur(50))
        canvas.paste(glow, (0, 0), glow)
        canvas.paste(mantra_resized, (mx, my), mantra_resized)
        
    # Top and Bottom dark vignettes
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    for y in range(0, 720):
        t = 1.0 - (y / 720.0)
        odraw.line([(0, y), (W, y)], fill=(7, 9, 14, int(245 * t)))
    for y in range(1250, H):
        t = (y - 1250) / (H - 1250.0)
        odraw.line([(0, y), (W, y)], fill=(7, 9, 14, int(240 * t)))
    canvas.paste(overlay, (0, 0), overlay)
    
    draw = ImageDraw.Draw(canvas)
    draw_top_left_brand(canvas, scale=1.35)
    
    # Warning Pill
    font_alert = get_font(FONT_MONO, 24)
    draw_badge(draw, "AADHAAR DATA LEAK EXPOSED", (68, 220), font_alert, (225, 29, 72), (255, 255, 255), pad_x=24, pad_y=12, radius=14, icon_type="alert")
    
    # Curiosity Badge
    font_curiosity = get_font(FONT_ANTON, 38)
    draw_badge(draw, "ZAMEEN REGISTRY SE CHORI!", (68, 320), font_curiosity, (251, 191, 36), (10, 14, 23), pad_x=30, pad_y=12, radius=16)
    
    # Giant Typography
    font_headline_1 = get_font(FONT_ANTON, 118)
    font_headline_2 = get_font(FONT_ANTON, 102)
    
    draw_3d_text(draw, "AAPKA THUMBPRINT", (68, 440), font_headline_1, fill_color=(255, 255, 255), depth=10)
    draw_3d_text(draw, "PUBLICLY LEAKED?!", (68, 570), font_headline_2, fill_color=(251, 191, 36), depth=8)
    
    # Rubber Stamp
    draw_rubber_stamp(canvas, "ZERO 2FA LOOPHOLE", (80, 1300), font_size=54, angle=-8, color=(239, 68, 68))
    
    # Bottom callout
    font_bottom = get_font(FONT_MONO, 26)
    draw_badge(draw, "HOW 300+ DPI THUMBPRINTS ARE CLONED", (68, 1500), font_bottom, (15, 23, 42), (52, 211, 153), pad_x=28, pad_y=16, radius=18, border_color=(52, 211, 153), border_width=3)
    
    canvas.save(OUT_OPT2, quality=96)
    print(f"✅ Option 2 Saved: {OUT_OPT2}")
    return canvas

# ==============================================================================
# OPTION 3: THE 60-SECOND CITIZEN SHIELD (MAADHAAR LOCK + ERROR 330)
# ==============================================================================
def create_thumb_option_3():
    print("🎨 Creating Option 3: Citizen Shield (9:16)...")
    W, H = 1080, 1920
    canvas = Image.new("RGB", (W, H), (7, 9, 14))
    
    # Background: Error 330 plate (beat_27)
    if BEAT_27.exists():
        im = Image.open(BEAT_27).convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
        enh = ImageEnhance.Contrast(im).enhance(1.20)
        canvas.paste(enh, (0, 0))
        
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    for y in range(0, 720):
        t = 1.0 - (y / 720.0)
        odraw.line([(0, y), (W, y)], fill=(7, 9, 14, int(245 * t)))
    for y in range(1200, H):
        t = (y - 1200) / (H - 1200.0)
        odraw.line([(0, y), (W, y)], fill=(7, 9, 14, int(240 * t)))
    canvas.paste(overlay, (0, 0), overlay)
    
    draw = ImageDraw.Draw(canvas)
    draw_top_left_brand(canvas, scale=1.35)
    
    # Shield Alert Badge
    font_alert = get_font(FONT_MONO, 24)
    draw_badge(draw, "OFFICIAL CYBER DEFENSE", (68, 220), font_alert, (16, 185, 129), (255, 255, 255), pad_x=24, pad_y=12, radius=14, icon_type="alert")
    
    # Shield Curiosity Pill
    font_curiosity = get_font(FONT_ANTON, 38)
    draw_badge(draw, "60-SECOND CITIZEN SHIELD", (68, 320), font_curiosity, (56, 189, 248), (10, 14, 23), pad_x=30, pad_y=12, radius=16)
    
    # Giant Typography
    font_headline_1 = get_font(FONT_ANTON, 120)
    font_headline_2 = get_font(FONT_ANTON, 102)
    
    draw_3d_text(draw, "APNA AADHAAR", (68, 440), font_headline_1, fill_color=(255, 255, 255), depth=10)
    draw_3d_text(draw, "TURANT LOCK KAREIN!", (68, 570), font_headline_2, fill_color=(52, 211, 153), depth=8)
    
    # Rubber Stamp
    draw_rubber_stamp(canvas, "ERROR 330: IMMUNE", (80, 1260), font_size=56, angle=-8, color=(52, 211, 153))
    
    # Bottom callout
    font_bottom = get_font(FONT_MONO, 26)
    draw_badge(draw, "HOW TO BLOCK SILICONE FINGER FRAUD NOW", (68, 1480), font_bottom, (15, 23, 42), (251, 191, 36), pad_x=28, pad_y=16, radius=18, border_color=(251, 191, 36), border_width=3)
    
    canvas.save(OUT_OPT3, quality=96)
    print(f"✅ Option 3 Saved: {OUT_OPT3}")
    return canvas

# ==============================================================================
# WIDESCREEN 16:9 MASTER THUMBNAIL (1280x720 FOR DESKTOP / SEARCH / BROWSE)
# ==============================================================================
def create_thumb_16x9():
    print("🎨 Creating 16:9 Widescreen Master Thumbnail (1280x720)...")
    W, H = 1280, 720
    canvas = Image.new("RGB", (W, H), (7, 9, 14))
    
    # Dual-Pane Forensic Composition:
    # Left pane: Real Stamped Registry Paper & Debit alert
    # Right pane: Fake Silicone Finger under scanner
    if BEAT_01.exists() and BEAT_05.exists():
        im_left = Image.open(BEAT_01).convert("RGB").crop((0, 200, 1080, 1600)).resize((720, 720), Image.Resampling.LANCZOS)
        im_right = Image.open(BEAT_05).convert("RGB").crop((0, 200, 1080, 1600)).resize((720, 720), Image.Resampling.LANCZOS)
        
        canvas.paste(im_left, (0, 0))
        
        # Soft gradient blend mask
        mask = Image.new("L", (720, 720), 0)
        mdraw = ImageDraw.Draw(mask)
        for x in range(720):
            val = int(255 * (x / 720.0) ** 1.6)
            mdraw.line([(x, 0), (x, 720)], fill=val)
        canvas.paste(im_right, (W - 720, 0), mask)
        
    # Dark cinematic glass overlay & edge vignette
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    for y in range(H):
        t = y / float(H)
        alpha = int(145 + t * 95)
        vdraw.line([(0, y), (W, y)], fill=(7, 9, 14, alpha))
    canvas.paste(vignette, (0, 0), vignette)
    
    draw = ImageDraw.Draw(canvas)
    draw_top_left_brand(canvas, scale=0.92)
    
    # Top Right Warning Badge
    font_badge = get_font(FONT_MONO, 17)
    draw_badge(draw, "CRITICAL BANKING ALERT", (W - 360, 45), font_badge, (225, 29, 72), (255, 255, 255), pad_x=18, pad_y=8, radius=10, icon_type="alert")
    
    # Curiosity Hook Pill
    font_curiosity = get_font(FONT_SPACE or FONT_ANTON, 25)
    draw_badge(draw, "ZERO OTP · ZERO ATM CARD SWIPED", (60, 140), font_curiosity, (251, 191, 36), (10, 14, 23), pad_x=24, pad_y=10, radius=14)
    
    # Giant Anton Headline
    font_headline = get_font(FONT_ANTON, 98)
    draw_3d_text(draw, "NAKLI UNGLI SCAM!", (60, 235), font_headline, fill_color=(255, 255, 255), depth=6)
    
    # Sub-headline in Crimson
    font_sub = get_font(FONT_ANTON, 56)
    draw_3d_text(draw, "₹10,000 SAAF IN SECONDS!", (60, 350), font_sub, fill_color=(239, 68, 68), depth=5)
    
    # Tilted Forensic Stamp
    draw_rubber_stamp(canvas, "689+ CLONES SEIZED", (60, 470), font_size=38, angle=-8, color=(239, 68, 68))
    
    # Remedy pill (Bottom Left)
    font_remedy = get_font(FONT_MONO, 18)
    draw_badge(draw, "CITIZEN SHIELD: LOCK BIOMETRICS IN mAadhaar", (60, 580), font_remedy, (15, 23, 42), (56, 189, 248), pad_x=18, pad_y=10, radius=10, border_color=(56, 189, 248), border_width=2)
    
    canvas.save(OUT_16X9, quality=96)
    print(f"✅ 16:9 Widescreen Saved: {OUT_16X9}")
    return canvas

def main():
    print("=" * 80)
    print("🚀 BENAQAAB INDIA — HIGH-CTR THUMBNAIL MASTER SUITE")
    print("=" * 80)
    
    opt1 = create_thumb_option_1()
    create_thumb_option_2()
    create_thumb_option_3()
    create_thumb_16x9()
    
    # Copy Option 1 as primary SH13_Thumbnail_9x16.jpg
    opt1.save(OUT_PRIMARY, quality=96)
    alt_out = PROJECT_DIR / "thumbnail_1080x1920.jpg"
    opt1.save(alt_out, quality=96)
    
    print("=" * 80)
    print("🎉 ALL 3 HIGH-CTR SHORTS THUMBNAILS & 16:9 WIDESCREEN GENERATED SUCCESSFULLY!")
    print(f"1️⃣ Option 1 (Silicone Ungli Shock): {OUT_OPT1}")
    print(f"2️⃣ Option 2 (Registry Data Leak):   {OUT_OPT2}")
    print(f"3️⃣ Option 3 (Citizen Shield):       {OUT_OPT3}")
    print(f"📺 16:9 Master Landscape Cover:     {OUT_16X9}")
    print("=" * 80)

if __name__ == "__main__":
    main()
