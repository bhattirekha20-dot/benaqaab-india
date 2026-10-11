#!/usr/bin/env python3
"""
build_master_ai_composite_thumbnails.py
Constructs Broadcast-Master High-CTR Composite Thumbnails (9:16 & 16:9)
Utilizing authentic 4K+ forensic assets:
- Real Stamp Paper Legal Deed (stamped_paper_india.jpg)
- Real Finger Ridge Micro-Texture (real_finger_macro.jpg)
- Real Biometric Scanner in Action (real_scanner_action.jpg)
- Real Mantra MFS100 Retail Hardware (mantra_clean_transparent.png)
- Real 500-Rupee Notes (indian_currency_fan.jpg)
- Real Specimen Aadhaar Card (aadhaar_specimen.png)
- Official Benaqaab India Typography & Seals
"""

import sys
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter, ImageOps

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PROJECT_DIR = Path(__file__).resolve().parent
WORKSPACE = PROJECT_DIR.parent.parent
SOURCES = PROJECT_DIR / "assets" / "real_sources"

# Fonts
FONT_ANTON = WORKSPACE / "brand" / "fonts" / "Anton.ttf"
FONT_INTER = WORKSPACE / "brand" / "fonts" / "Inter.ttf"
FONT_MONO = WORKSPACE / "brand" / "fonts" / "JetBrainsMono.ttf"
FONT_SPACE = WORKSPACE / "brand" / "fonts" / "SpaceGrotesk.ttf"

# Outputs
OUT_9X16_MASTER = PROJECT_DIR / "SH13_Thumbnail_9x16.jpg"
OUT_9X16_ALT = PROJECT_DIR / "thumbnail_1080x1920.jpg"
OUT_16X9_MASTER = PROJECT_DIR / "SH13_Thumbnail_16x9.jpg"
OUT_16X9_ALT = PROJECT_DIR / "thumbnail_1280x720.jpg"
PREVIEW_DIR = PROJECT_DIR / "previews"

def get_font(path, size):
    try:
        return ImageFont.truetype(str(path), size)
    except Exception:
        return ImageFont.load_default()

def draw_3d_text(draw, text, xy, font, fill_color, shadow_color=(0, 0, 0), depth=8):
    x, y = xy
    for d in range(depth, 0, -1):
        draw.text((x + d, y + d), text, font=font, fill=shadow_color)
    draw.text((x, y), text, font=font, fill=fill_color)

def draw_top_left_brand(canvas, scale=1.35):
    draw = ImageDraw.Draw(canvas)
    pw = int(320 * scale)
    ph = int(62 * scale)
    x, y = int(50 * scale), int(50 * scale)
    
    # Dark obsidian glass pill
    draw.rounded_rectangle([x, y, x + pw, y + ph], radius=int(31 * scale), fill=(10, 14, 23, 245), outline=(251, 191, 36), width=int(2.5 * scale))
    
    # Red circular avatar
    cx = x + int(32 * scale)
    cy = y + int(31 * scale)
    r = int(18 * scale)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(239, 68, 68))
    
    # Benaqaab text
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

# ==============================================================================
# 9:16 VERTICAL SHORTS MASTER THUMBNAIL (1080x1920)
# ==============================================================================
def build_master_9x16():
    print("🎨 Compositing 9:16 Master YouTube Shorts Thumbnail (1080x1920)...")
    W, H = 1080, 1920
    canvas = Image.new("RGB", (W, H), (7, 9, 14))
    
    # 1. LAYER 1: Authentic Indian Stamp Paper Legal Deed Background
    stamp_path = SOURCES / "stamped_paper_india.jpg"
    if stamp_path.exists():
        im_stamp = Image.open(stamp_path).convert("RGB")
        # Crop the official stamp paper section with revenue seal and blue thumbprint
        crop_stamp = im_stamp.crop((500, 300, 7500, 7500)).resize((W, H), Image.Resampling.LANCZOS)
        # Tone down to dark moody cyber slate
        crop_stamp = ImageEnhance.Brightness(crop_stamp).enhance(0.42)
        crop_stamp = ImageEnhance.Contrast(crop_stamp).enhance(1.35)
        crop_stamp = crop_stamp.filter(ImageFilter.GaussianBlur(1.5))
        canvas.paste(crop_stamp, (0, 0))
        
    # 2. LAYER 2: Hero Scanner in Action (real_scanner_action.jpg)
    action_path = SOURCES / "real_scanner_action.jpg"
    if action_path.exists():
        im_action = Image.open(action_path).convert("RGB")
        # Crop finger pressing on glowing red sensor prism
        action_crop = im_action.crop((350, 150, 1250, 950)).resize((820, 640), Image.Resampling.LANCZOS)
        action_crop = ImageEnhance.Contrast(action_crop).enhance(1.25)
        
        # Soft feathered oval mask
        mask = Image.new("L", (820, 640), 0)
        mdraw = ImageDraw.Draw(mask)
        mdraw.ellipse([20, 20, 800, 620], fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(25))
        
        # Place in center stage: y = 720
        cx = (W - 820) // 2
        cy = 720
        
        # Specular crimson back-glow
        glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        gdraw = ImageDraw.Draw(glow)
        gdraw.ellipse([cx - 50, cy - 50, cx + 870, cy + 690], fill=(239, 68, 68, 140))
        glow = glow.filter(ImageFilter.GaussianBlur(55))
        canvas.paste(glow, (0, 0), glow)
        
        canvas.paste(action_crop, (cx, cy), mask)
        
    # 3. LAYER 3: Macro Skin Ridge Texture Callout (real_finger_macro.jpg)
    macro_path = SOURCES / "real_finger_macro.jpg"
    if macro_path.exists():
        im_macro = Image.open(macro_path).convert("RGB")
        # Center crop the microscopic friction ridges
        mw, mh = 420, 420
        mcrop = im_macro.crop((1200, 600, 2600, 2000)).resize((mw, mh), Image.Resampling.LANCZOS)
        mcrop = ImageEnhance.Color(mcrop).enhance(1.4)
        mcrop = ImageEnhance.Contrast(mcrop).enhance(1.3)
        
        # Circular lens bezel
        mmask = Image.new("L", (mw, mh), 0)
        ImageDraw.Draw(mmask).ellipse([10, 10, mw - 10, mh - 10], fill=255)
        mmask = mmask.filter(ImageFilter.GaussianBlur(3))
        
        # Place circular loupe at lower-right: x = 600, y = 1000
        lx, ly = 600, 980
        
        # Specular glass border
        bezel = Image.new("RGBA", (mw, mh), (0, 0, 0, 0))
        bdraw = ImageDraw.Draw(bezel)
        bdraw.ellipse([10, 10, mw - 10, mh - 10], outline=(56, 189, 248, 255), width=6)
        bdraw.ellipse([16, 16, mw - 16, mh - 16], outline=(255, 255, 255, 180), width=2)
        # Crosshair
        bdraw.line([(mw//2, 0), (mw//2, mh)], fill=(56, 189, 248, 140), width=2)
        bdraw.line([(0, mh//2), (mw, mh//2)], fill=(56, 189, 248, 140), width=2)
        
        canvas.paste(mcrop, (lx, ly), mmask)
        canvas.paste(bezel, (lx, ly), bezel)
        
        # Loupe Label
        draw_l = ImageDraw.Draw(canvas)
        font_pill = get_font(FONT_MONO, 20)
        draw_badge(draw_l, "300+ DPI RIDGE CLONE", (lx + 30, ly + mh - 35), font_pill, (10, 14, 23), (56, 189, 248), pad_x=16, pad_y=8, radius=10, border_color=(56, 189, 248), border_width=2)

    # 4. LAYER 4: Real Stacks of Cash (indian_currency_fan.jpg) at lower left
    cash_path = SOURCES / "indian_currency_fan.jpg"
    if cash_path.exists():
        im_cash = Image.open(cash_path).convert("RGB")
        # Crop fan of 500-rupee notes
        cw, ch = 520, 360
        ccrop = im_cash.crop((50, 680, 1020, 1380)).resize((cw, ch), Image.Resampling.LANCZOS)
        
        cmask = Image.new("L", (cw, ch), 0)
        ImageDraw.Draw(cmask).rounded_rectangle([10, 10, cw - 10, ch - 10], radius=24, fill=255)
        cmask = cmask.filter(ImageFilter.GaussianBlur(12))
        
        # Paste at bottom left (y = 1380)
        canvas.paste(ccrop, (50, 1420), cmask)
        
    # 5. LAYER 5: Real-World Banking Debit SMS Notification Card
    # Floating frosted card at y = 1430
    sms_card = Image.new("RGBA", (W - 140, 180), (10, 14, 23, 245))
    sdraw = ImageDraw.Draw(sms_card)
    sdraw.rounded_rectangle([0, 0, W - 140, 180], radius=24, fill=(10, 14, 23, 245), outline=(239, 68, 68), width=3)
    
    # Red Alert Dot & Title
    sdraw.ellipse([26, 26, 44, 44], fill=(239, 68, 68))
    font_sms_title = get_font(FONT_MONO, 22)
    sdraw.text((54, 22), "BANK ALERT: CASH WITHDRAWAL (AePS)", font=font_sms_title, fill=(239, 68, 68))
    
    font_sms_amt = get_font(FONT_ANTON, 52)
    sdraw.text((26, 58), "- ₹ 10,000.00 DEBITED", font=font_sms_amt, fill=(255, 255, 255))
    
    font_sms_detail = get_font(FONT_INTER, 20)
    sdraw.text((26, 128), "Auth: Biometric (Rogue Mitra POS) · Zero OTP Req.", font=font_sms_detail, fill=(148, 163, 184))
    
    canvas.paste(sms_card, (70, 1480), sms_card)

    # 6. LAYER 6: Upper & Lower Dramatic Gradient Vignette for Text Safe Zones
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    for y in range(0, 720):
        t = 1.0 - (y / 720.0)
        odraw.line([(0, y), (W, y)], fill=(7, 9, 14, int(250 * t)))
    for y in range(1650, H):
        t = (y - 1650) / (H - 1650.0)
        odraw.line([(0, y), (W, y)], fill=(7, 9, 14, int(250 * t)))
    canvas.paste(overlay, (0, 0), overlay)

    # 7. LAYER 7: Top Brand & High-CTR Typography
    draw = ImageDraw.Draw(canvas)
    draw_top_left_brand(canvas, scale=1.35)
    
    # Critical Alert Badge (Upper Right)
    font_alert = get_font(FONT_MONO, 24)
    draw_badge(draw, "CRITICAL BANKING ALERT", (68, 220), font_alert, (225, 29, 72), (255, 255, 255), pad_x=24, pad_y=12, radius=14, icon_type="alert")
    
    # Curiosity Hook Pill
    font_curiosity = get_font(FONT_ANTON, 40)
    draw_badge(draw, "ZERO OTP · ZERO ATM CARD", (68, 320), font_curiosity, (251, 191, 36), (10, 14, 23), pad_x=30, pad_y=12, radius=16)
    
    # Giant High-CTR Typography in Upper Safe Zone (Readable across mobile screens)
    font_headline_1 = get_font(FONT_ANTON, 130)
    font_headline_2 = get_font(FONT_ANTON, 106)
    
    draw_3d_text(draw, "₹10,000 SAAF!", (68, 440), font_headline_1, fill_color=(255, 255, 255), depth=12)
    draw_3d_text(draw, "NAKLI UNGLI SCAM!", (68, 580), font_headline_2, fill_color=(239, 68, 68), depth=10)

    # Angled Forensic Police Stamp
    draw_rubber_stamp(canvas, "689+ CLONES SEIZED", (80, 1340), font_size=58, angle=-8, color=(239, 68, 68))

    # Bottom Citizen Shield Bar
    font_shield = get_font(FONT_MONO, 26)
    draw_badge(draw, "CITIZEN SHIELD: LOCK BIOMETRICS IN mAadhaar", (68, 1720), font_shield, (15, 23, 42), (56, 189, 248), pad_x=28, pad_y=16, radius=18, border_color=(56, 189, 248), border_width=3)

    canvas.save(OUT_9X16_MASTER, quality=98)
    canvas.save(OUT_9X16_ALT, quality=98)
    print(f"✅ 9:16 Master Thumbnail Saved: {OUT_9X16_MASTER}")
    return canvas

# ==============================================================================
# 16:9 WIDESCREEN MASTER THUMBNAIL (1280x720 FOR DESKTOP & SEARCH FEEDS)
# ==============================================================================
def build_master_16x9():
    print("🎨 Compositing 16:9 Master Widescreen Thumbnail (1280x720)...")
    W, H = 1280, 720
    canvas = Image.new("RGB", (W, H), (7, 9, 14))
    
    # Left Half: Real Indian Stamp Paper Deed with genuine stamp seal
    stamp_path = SOURCES / "stamped_paper_india.jpg"
    if stamp_path.exists():
        im_stamp = Image.open(stamp_path).convert("RGB")
        left_crop = im_stamp.crop((500, 200, 5500, 4200)).resize((760, 720), Image.Resampling.LANCZOS)
        left_crop = ImageEnhance.Brightness(left_crop).enhance(0.44)
        left_crop = ImageEnhance.Contrast(left_crop).enhance(1.35)
        canvas.paste(left_crop, (0, 0))
        
    # Right Half: Real Biometric Scanner in Action (real_scanner_action.jpg)
    action_path = SOURCES / "real_scanner_action.jpg"
    if action_path.exists():
        im_action = Image.open(action_path).convert("RGB")
        # Crop precisely where the finger presses on the glowing red optical sensor
        right_crop = im_action.crop((120, 120, 880, 880)).resize((660, 720), Image.Resampling.LANCZOS)
        right_crop = ImageEnhance.Contrast(right_crop).enhance(1.25)
        right_crop = ImageEnhance.Brightness(right_crop).enhance(1.10)
        
        # Smooth horizontal blend mask
        mask = Image.new("L", (660, 720), 0)
        mdraw = ImageDraw.Draw(mask)
        for x in range(660):
            val = int(255 * (x / 660.0) ** 1.6)
            mdraw.line([(x, 0), (x, 720)], fill=val)
        canvas.paste(right_crop, (W - 660, 0), mask)
        
    # Loupe inspecting finger ridges in the upper right
    macro_path = SOURCES / "real_finger_macro.jpg"
    if macro_path.exists():
        im_macro = Image.open(macro_path).convert("RGB")
        mw, mh = 260, 260
        mcrop = im_macro.crop((1200, 600, 2600, 2000)).resize((mw, mh), Image.Resampling.LANCZOS)
        mcrop = ImageEnhance.Color(mcrop).enhance(1.4)
        mcrop = ImageEnhance.Contrast(mcrop).enhance(1.3)
        
        mmask = Image.new("L", (mw, mh), 0)
        ImageDraw.Draw(mmask).ellipse([5, 5, mw - 5, mh - 5], fill=255)
        mmask = mmask.filter(ImageFilter.GaussianBlur(2))
        
        lx, ly = W - 320, 140
        canvas.paste(mcrop, (lx, ly), mmask)
        
        # Glass border
        bezel = Image.new("RGBA", (mw, mh), (0, 0, 0, 0))
        bdraw = ImageDraw.Draw(bezel)
        bdraw.ellipse([5, 5, mw - 5, mh - 5], outline=(56, 189, 248, 255), width=5)
        bdraw.ellipse([9, 9, mw - 9, mh - 9], outline=(255, 255, 255, 180), width=2)
        bdraw.line([(mw//2, 0), (mw//2, mh)], fill=(56, 189, 248, 140), width=2)
        bdraw.line([(0, mh//2), (mw, mh//2)], fill=(56, 189, 248, 140), width=2)
        canvas.paste(bezel, (lx, ly), bezel)
        
        # Badge on loupe
        draw_b = ImageDraw.Draw(canvas)
        font_pill = get_font(FONT_MONO, 15)
        draw_badge(draw_b, "300+ DPI CLONE", (lx + 20, ly + mh - 26), font_pill, (10, 14, 23), (56, 189, 248), pad_x=12, pad_y=6, radius=8, border_color=(56, 189, 248), border_width=2)

    # Ambient red glow on right side scanner
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gdraw = ImageDraw.Draw(glow)
    gdraw.ellipse([W - 650, 150, W - 150, 650], fill=(239, 68, 68, 130))
    glow = glow.filter(ImageFilter.GaussianBlur(65))
    canvas.paste(glow, (0, 0), glow)

    # Dark cinematic glass overlay & edge vignette for typography legibility
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    for y in range(H):
        t = y / float(H)
        alpha = int(140 + t * 95)
        vdraw.line([(0, y), (W, y)], fill=(7, 9, 14, alpha))
    canvas.paste(vignette, (0, 0), vignette)

    draw = ImageDraw.Draw(canvas)
    draw_top_left_brand(canvas, scale=0.92)
    
    # Top Right Warning Badge
    font_badge = get_font(FONT_MONO, 17)
    draw_badge(draw, "CRITICAL BANKING ALERT", (W - 360, 45), font_badge, (225, 29, 72), (255, 255, 255), pad_x=18, pad_y=8, radius=10, icon_type="alert")
    
    # Curiosity Hook Pill
    font_curiosity = get_font(FONT_ANTON, 26)
    draw_badge(draw, "ZERO OTP · ZERO ATM CARD SWIPED", (60, 140), font_curiosity, (251, 191, 36), (10, 14, 23), pad_x=24, pad_y=10, radius=14)
    
    # Giant Anton Headline
    font_headline = get_font(FONT_ANTON, 102)
    draw_3d_text(draw, "NAKLI UNGLI SCAM!", (60, 235), font_headline, fill_color=(255, 255, 255), depth=7)
    
    # Sub-headline in Crimson
    font_sub = get_font(FONT_ANTON, 58)
    draw_3d_text(draw, "₹10,000 SAAF IN SECONDS!", (60, 355), font_sub, fill_color=(239, 68, 68), depth=6)
    
    # Tilted Forensic Stamp
    draw_rubber_stamp(canvas, "689+ CLONES SEIZED", (60, 475), font_size=40, angle=-8, color=(239, 68, 68))
    
    # Banking Debit SMS Card (floating at bottom right)
    sms_card = Image.new("RGBA", (480, 130), (10, 14, 23, 245))
    sdraw = ImageDraw.Draw(sms_card)
    sdraw.rounded_rectangle([0, 0, 480, 130], radius=18, fill=(10, 14, 23, 245), outline=(239, 68, 68), width=2)
    sdraw.ellipse([18, 18, 32, 32], fill=(239, 68, 68))
    font_sms_t = get_font(FONT_MONO, 15)
    sdraw.text((38, 16), "BANK ALERT: CASH WDL (AePS)", font=font_sms_t, fill=(239, 68, 68))
    font_sms_a = get_font(FONT_ANTON, 38)
    sdraw.text((18, 44), "- ₹ 10,000.00 DEBITED", font=font_sms_a, fill=(255, 255, 255))
    font_sms_d = get_font(FONT_INTER, 14)
    sdraw.text((18, 95), "Auth: Biometric · Zero OTP Required", font=font_sms_d, fill=(148, 163, 184))
    canvas.paste(sms_card, (W - 520, H - 160), sms_card)
    
    # Remedy pill (Bottom Left)
    font_remedy = get_font(FONT_MONO, 18)
    draw_badge(draw, "CITIZEN SHIELD: LOCK BIOMETRICS IN mAadhaar", (60, 590), font_remedy, (15, 23, 42), (56, 189, 248), pad_x=18, pad_y=10, radius=10, border_color=(56, 189, 248), border_width=2)

    canvas.save(OUT_16X9_MASTER, quality=98)
    canvas.save(OUT_16X9_ALT, quality=98)
    print(f"✅ 16:9 Master Thumbnail Saved: {OUT_16X9_MASTER}")
    return canvas

if __name__ == '__main__':
    print("=" * 80)
    print("🚀 BENAQAAB INDIA — 4K BROADCAST COMPOSITE THUMBNAIL ENGINE")
    print("=" * 80)
    build_master_9x16()
    build_master_16x9()
    print("=" * 80)
    print("🎉 MASTER 9:16 AND 16:9 THUMBNAILS BUILT WITH AUTHENTIC REAL ASSETS!")
    print("=" * 80)
