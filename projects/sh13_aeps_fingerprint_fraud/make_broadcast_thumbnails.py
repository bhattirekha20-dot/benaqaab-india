#!/usr/bin/env python3
"""
make_broadcast_thumbnails.py — High-CTR Broadcast Thumbnail Suite
Episode SH-13: AePS Aadhaar Fingerprint Fraud (Silicone Ungli Scam)
Channel: Benaqaab India (बेनाक़ाब इंडिया) • Sach · Saboot · Bebak
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

FONT_ANTON = WORKSPACE / "brand" / "fonts" / "Anton.ttf"
FONT_INTER = WORKSPACE / "brand" / "fonts" / "Inter.ttf"
FONT_MONO = WORKSPACE / "brand" / "fonts" / "JetBrainsMono.ttf"
FONT_SPACE = WORKSPACE / "brand" / "fonts" / "SpaceGrotesk.ttf"
LOGO_PATH = WORKSPACE / "brand" / "logo.png"

BEAT_01 = PROJECT_DIR / "assets" / "visuals" / "beat_01.jpg" # Debit alert
BEAT_05 = PROJECT_DIR / "assets" / "visuals" / "beat_05.jpg" # Silicone thumb
BEAT_21 = PROJECT_DIR / "assets" / "visuals" / "beat_21.jpg" # ₹10,000 odometer
BEAT_27 = PROJECT_DIR / "assets" / "visuals" / "beat_27.jpg" # Error 330

OUT_16X9 = PROJECT_DIR / "thumbnail_1280x720.jpg"
OUT_9X16 = PROJECT_DIR / "thumbnail_1080x1920.jpg"

def get_font(path, size):
    try:
        return ImageFont.truetype(str(path), size)
    except Exception:
        return ImageFont.load_default()

def draw_badge(draw, text, xy, font, bg_color, text_color, pad_x=24, pad_y=10, radius=12, border_color=None, border_width=2, icon_type=None):
    x, y = xy
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    icon_w = 0
    if icon_type == "alert":
        icon_w = th + 14
    elif icon_type == "dot":
        icon_w = 20
        
    w = tw + pad_x * 2 + icon_w
    h = th + pad_y * 2
    
    draw.rounded_rectangle([x, y, x + w, y + h], radius=int(radius), fill=bg_color, outline=border_color, width=int(border_width))
    
    curr_x = x + pad_x
    if icon_type == "alert":
        cx = curr_x + (th // 2)
        cy = y + (h // 2)
        r = th // 2
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, 240))
        draw.line([(cx, cy - r + 3), (cx, cy + 1)], fill=(225, 29, 72, 255), width=3)
        draw.ellipse([cx - 2, cy + 4, cx + 2, cy + 8], fill=(225, 29, 72, 255))
        curr_x += th + 14
    elif icon_type == "dot":
        cx = curr_x + 8
        cy = y + (h // 2)
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(244, 63, 94))
        curr_x += 20
        
    draw.text((curr_x, y + pad_y - 2), text, font=font, fill=text_color)
    return w, h

def draw_tilted_stamp(base_img, text, xy, font_size=42, angle=-8, color=(239, 68, 68)):
    font = get_font(FONT_ANTON, font_size)
    dummy_draw = ImageDraw.Draw(base_img)
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    pad_x, pad_y = 30, 14
    sw = tw + pad_x * 2
    sh = th + pad_y * 2
    
    stamp = Image.new("RGBA", (sw + 40, sh + 40), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(stamp)
    
    sdraw.rounded_rectangle([10, 10, sw + 10, sh + 10], radius=14, outline=color, width=5)
    sdraw.rounded_rectangle([16, 16, sw + 4, sh + 4], radius=10, outline=color, width=2)
    sdraw.text((pad_x + 10, pad_y + 6), text, font=font, fill=color)
    
    rotated = stamp.rotate(angle, resample=Image.BICUBIC, expand=True)
    base_img.paste(rotated, xy, rotated)

def draw_top_left_brand(draw, scale=1.0):
    pill_w = int(320 * scale)
    pill_h = int(60 * scale)
    x, y = int(50 * scale), int(50 * scale)
    draw.rounded_rectangle([x, y, x + pill_w, y + pill_h], radius=int(30 * scale), fill=(10, 14, 23, 230), outline=(251, 191, 36), width=2)
    
    # Red circle dot
    cx = x + int(32 * scale)
    cy = y + int(30 * scale)
    r = int(18 * scale)
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(244, 63, 94))
    
    font_bold = get_font(FONT_ANTON, int(22 * scale))
    draw.text((x + int(60 * scale), y + int(10 * scale)), "BENAQAAB INDIA", font=font_bold, fill=(255, 255, 255))
    font_sub = get_font(FONT_MONO, int(11 * scale))
    draw.text((x + int(62 * scale), y + int(34 * scale)), "SACH · SABOOT · BEBAK", font=font_sub, fill=(251, 191, 36))

def build_16x9_thumbnail():
    print("🎨 Building 16:9 Landscape Master Thumbnail (1280x720)...")
    W, H = 1280, 720
    canvas = Image.new("RGB", (W, H), (7, 9, 14))
    
    # Left image: Debit alert / Odometer (crop & fit)
    if BEAT_01.exists():
        im_left = Image.open(BEAT_01).convert("RGB")
        im_left = im_left.crop((0, 300, 1080, 1500)).resize((700, 720), Image.Resampling.LANCZOS)
        canvas.paste(im_left, (0, 0))
    
    # Right image: Silicone fake thumb (crop & fit)
    if BEAT_05.exists():
        im_right = Image.open(BEAT_05).convert("RGB")
        im_right = im_right.crop((0, 300, 1080, 1500)).resize((700, 720), Image.Resampling.LANCZOS)
        # Create gradient mask for smooth cinematic dual-blend
        mask = Image.new("L", (700, 720), 0)
        mdraw = ImageDraw.Draw(mask)
        for x in range(700):
            val = int(255 * (x / 700.0) ** 1.5)
            mdraw.line([(x, 0), (x, 720)], fill=val)
        canvas.paste(im_right, (W - 700, 0), mask)
        
    # Dark cinematic glass overlay & edge vignette
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    for y in range(H):
        t = y / H
        alpha = int(140 + t * 90)
        vdraw.line([(0, y), (W, y)], fill=(7, 9, 14, alpha))
    canvas.paste(vignette, (0, 0), vignette)
    
    draw = ImageDraw.Draw(canvas)
    draw_top_left_brand(draw, scale=0.9)
    
    # Emergency Warning Badge (Top Right)
    font_badge = get_font(FONT_MONO, 16)
    draw_badge(draw, "CRITICAL BANKING ALERT", (W - 350, 45), font_badge, (225, 29, 72), (255, 255, 255), pad_x=16, pad_y=8, radius=10, icon_type="alert")
    
    # Signal Amber Curiosity Pill
    font_curiosity = get_font(FONT_SPACE or FONT_ANTON, 24)
    draw_badge(draw, "ZERO OTP · ZERO ATM CARD SWIPED", (60, 140), font_curiosity, (251, 191, 36), (15, 23, 42), pad_x=24, pad_y=10, radius=14)
    
    # Giant Anton Headline with multi-layer 3D drop shadow
    font_headline = get_font(FONT_ANTON, 96)
    headline_text = "NAKLI UNGLI SCAM!"
    hx, hy = 60, 240
    
    # 3D Black Drop Shadow
    for off in range(6, 0, -1):
        draw.text((hx + off, hy + off), headline_text, font=font_headline, fill=(0, 0, 0))
    draw.text((hx, hy), headline_text, font=font_headline, fill=(255, 255, 255))
    
    # Sub-headline
    font_sub = get_font(FONT_ANTON, 54)
    sub_text = "₹10,000 SAAF IN SECONDS!"
    for off in range(4, 0, -1):
        draw.text((hx + off, hy + 115 + off), sub_text, font=font_sub, fill=(0, 0, 0))
    draw.text((hx, hy + 115), sub_text, font=font_sub, fill=(244, 63, 94))
    
    # Tilted Forensic Stamp
    draw_tilted_stamp(canvas, "1,000+ CLONES SEIZED", (60, 480), font_size=38, angle=-8, color=(239, 68, 68))
    
    # Remedy pill (Bottom Left)
    font_remedy = get_font(FONT_MONO, 18)
    draw_badge(draw, "SHIELD: LOCK BIOMETRICS IN mAadhaar", (60, 590), font_remedy, (15, 23, 42), (56, 189, 248), pad_x=18, pad_y=10, radius=10, border_color=(56, 189, 248), border_width=2)
    
    canvas.save(OUT_16X9, quality=95)
    print(f"✅ Saved: {OUT_16X9}")

def build_9x16_thumbnail():
    print("🎨 Building 9:16 Vertical Shorts Master Cover (1080x1920)...")
    W, H = 1080, 1920
    canvas = Image.new("RGB", (W, H), (7, 9, 14))
    
    # Base background: Beat 05 (Silicone thumb)
    if BEAT_05.exists():
        im = Image.open(BEAT_05).convert("RGB").resize((W, H), Image.Resampling.LANCZOS)
        canvas.paste(im, (0, 0))
        
    # Dark gradient overlays for upper and lower text contrast
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    for y in range(0, 650):
        t = 1.0 - (y / 650.0)
        odraw.line([(0, y), (W, y)], fill=(7, 9, 14, int(220 * t)))
    for y in range(1200, H):
        t = (y - 1200) / (H - 1200.0)
        odraw.line([(0, y), (W, y)], fill=(7, 9, 14, int(230 * t)))
    canvas.paste(overlay, (0, 0), overlay)
    
    draw = ImageDraw.Draw(canvas)
    draw_top_left_brand(draw, scale=1.4)
    
    # Emergency Warning Badge (Upper Center)
    font_badge = get_font(FONT_MONO, 24)
    draw_badge(draw, "CRITICAL BANKING ALERT", (70, 240), font_badge, (225, 29, 72), (255, 255, 255), pad_x=22, pad_y=10, radius=12, icon_type="alert")
    
    # Signal Amber Curiosity Pill
    font_curiosity = get_font(FONT_ANTON, 40)
    draw_badge(draw, "NO OTP · NO ATM CARD", (70, 340), font_curiosity, (251, 191, 36), (15, 23, 42), pad_x=28, pad_y=12, radius=16)
    
    # Giant Headline in Upper Safe Zone
    font_giant = get_font(FONT_ANTON, 120)
    headline_text = "₹10,000 SAAF!"
    hx, hy = 70, 480
    for off in range(8, 0, -1):
        draw.text((hx + off, hy + off), headline_text, font=font_giant, fill=(0, 0, 0))
    draw.text((hx, hy), headline_text, font=font_giant, fill=(255, 255, 255))
    
    font_sub = get_font(FONT_ANTON, 76)
    sub_text = "NAKLI SILICONE UNGLI"
    for off in range(6, 0, -1):
        draw.text((hx + off, hy + 140 + off), sub_text, font=font_sub, fill=(0, 0, 0))
    draw.text((hx, hy + 140), sub_text, font=font_sub, fill=(244, 63, 94))
    
    # Center-Lower: Tilted Forensic Stamp
    draw_tilted_stamp(canvas, "AePS SCAM EXPOSED", (120, 1280), font_size=58, angle=-8, color=(239, 68, 68))
    
    # Lower Shield Pill
    font_bottom = get_font(FONT_MONO, 28)
    draw_badge(draw, "IMMUNIZE YOUR ACCOUNT: LOCK BIOMETRICS IN mAadhaar", (70, 1500), font_bottom, (15, 23, 42), (56, 189, 248), pad_x=26, pad_y=14, radius=16, border_color=(56, 189, 248), border_width=3)
    
    canvas.save(OUT_9X16, quality=95)
    print(f"✅ Saved: {OUT_9X16}")

if __name__ == "__main__":
    build_16x9_thumbnail()
    build_9x16_thumbnail()
