#!/usr/bin/env python3
"""
make_broadcast_thumbnails.py — Flagship Broadcast-Grade Investigative Thumbnail Engine
Project: SH-12 Delhi Lockdown & CJP Youth Protest
Channel: Benaqaab India (बेनाक़ाब इंडिया) • Sach · Saboot · Bebak

Generates:
1. 16:9 Landscape Thumbnail (1280x720) — Full-bleed dual-image composite blending Delhi Police riot barricades
   on the left with Shivaji Stadium locked metro gates on the right, dark glass vignette, Anton typography,
   CJP amber emblem, and forensic rubber stamp.
2. 9:16 Vertical Shorts Cover (1080x1920) — Full-bleed photojournalistic vertical cover with clean typography
   hierarchy in the upper safe zone, zero emoji tofu artifacts, and maximum retention curiosity.
"""

import os
import sys
import math
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PROJECT_DIR = Path(__file__).resolve().parent
WORKSPACE = PROJECT_DIR.parent.parent

# Fonts
FONT_ANTON = WORKSPACE / "brand" / "fonts" / "Anton.ttf"
FONT_INTER = WORKSPACE / "brand" / "fonts" / "Inter.ttf"
FONT_MONO = WORKSPACE / "brand" / "fonts" / "JetBrainsMono.ttf"
LOGO_PATH = WORKSPACE / "brand" / "logo.png"

# Assets
BEAT_01 = PROJECT_DIR / "assets" / "visuals" / "beat_01.jpg" # Locked Metro Gate
BEAT_03 = PROJECT_DIR / "assets" / "visuals" / "beat_03.jpg" # Police Riot Deployment
BEAT_06 = PROJECT_DIR / "assets" / "visuals" / "beat_06.jpg" # CJP Amber Cockroach Emblem

OUT_16X9 = PROJECT_DIR / "SH12_Thumbnail_16x9.jpg"
OUT_16X9_ALT = PROJECT_DIR / "thumbnail_1280x720.jpg"
OUT_9X16 = PROJECT_DIR / "SH12_Thumbnail_9x16.jpg"
OUT_9X16_ALT = PROJECT_DIR / "thumbnail_1080x1920.jpg"

def get_font(path, size):
    try:
        return ImageFont.truetype(str(path), size)
    except Exception:
        return ImageFont.load_default()

def draw_badge(draw, text, xy, font, bg_color, text_color, pad_x=24, pad_y=12, radius=12, border_color=None, border_width=2, icon_type=None):
    """Draws a rounded badge pill with optional procedural icon (warning, alert, dot)"""
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
    
    # Rounded badge box
    draw.rounded_rectangle([x, y, x + w, y + h], radius=int(radius), fill=bg_color, outline=border_color, width=int(border_width))
    
    # Draw icon if requested
    curr_x = x + pad_x
    if icon_type == "alert":
        # Draw red warning circle with white '!'
        cx = curr_x + (th // 2)
        cy = y + (h // 2)
        r = th // 2
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, 240))
        # Exclamation point
        draw.line([(cx, cy - r + 3), (cx, cy + 1)], fill=(225, 29, 72, 255), width=3)
        draw.point([(cx, cy + r - 3), (cx, cy + r - 2)], fill=(225, 29, 72, 255))
        curr_x += th + 12
    elif icon_type == "dot":
        cx = curr_x + 8
        cy = y + (h // 2)
        draw.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(244, 63, 94, 255))
        curr_x += 20
        
    # Text
    ty = y + pad_y - bbox[1]
    draw.text((curr_x, ty), text, font=font, fill=text_color)
    return w, h

def draw_rubber_stamp(text, font, text_color=(239, 68, 68, 250), border_color=(239, 68, 68, 240), angle=-8):
    """Draws a distressed forensic rubber stamp with double border"""
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pad_x, pad_y = 28, 14
    w = tw + pad_x * 2
    h = th + pad_y * 2
    
    stamp = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(stamp)
    
    # Outer double border
    sdraw.rounded_rectangle([2, 2, w - 2, h - 2], radius=10, outline=border_color, width=4)
    sdraw.rounded_rectangle([7, 7, w - 7, h - 7], radius=7, outline=border_color, width=2)
    
    # Text
    tx = pad_x - bbox[0]
    ty = pad_y - bbox[1]
    sdraw.text((tx, ty), text, font=font, fill=text_color)
    
    # Rotate with smooth antialiasing
    rotated = stamp.rotate(angle, resample=Image.BICUBIC, expand=True)
    return rotated

def generate_landscape_16x9():
    W, H = 1280, 720
    
    # 1. Full-bleed widescreen dual-image composite
    # Left: beat_03 (Police riot barricades & tactical deployment)
    # Right: beat_01 (Shivaji Stadium locked metro gates & caution tape)
    left_img = Image.open(BEAT_03).convert("RGBA")
    right_img = Image.open(BEAT_01).convert("RGBA")
    
    # Enhance punch and contrast
    left_img = ImageEnhance.Contrast(left_img).enhance(1.25)
    left_img = ImageEnhance.Color(left_img).enhance(1.15)
    right_img = ImageEnhance.Contrast(right_img).enhance(1.22)
    right_img = ImageEnhance.Color(right_img).enhance(1.15)
    
    # Scale left image to cover width ~750
    s_l = 750.0 / left_img.width
    left_scaled = left_img.resize((750, int(left_img.height * s_l)), Image.Resampling.LANCZOS)
    crop_y_l = max(0, (left_scaled.height - H) // 2)
    left_cropped = left_scaled.crop((0, crop_y_l, 750, crop_y_l + H))
    
    # Scale right image to cover width ~800
    s_r = 800.0 / right_img.width
    right_scaled = right_img.resize((800, int(right_img.height * s_r)), Image.Resampling.LANCZOS)
    crop_y_r = max(0, (right_scaled.height - H) // 2)
    right_cropped = right_scaled.crop((0, crop_y_r, 800, crop_y_r + H))
    
    # Composite base
    canvas = Image.new("RGBA", (W, H), (7, 10, 18, 255))
    canvas.paste(left_cropped, (0, 0))
    
    # Smooth horizontal feather blend for the right image
    mask_r = Image.new("L", (800, H), 255)
    mdraw = ImageDraw.Draw(mask_r)
    for x in range(260):
        alpha = int(255 * (x / 260.0))
        mdraw.line([(x, 0), (x, H)], fill=alpha)
    canvas.paste(right_cropped, (W - 800, 0), mask_r)
    
    # 2. Layer dark gradient vignette on left side (0..680px) to ensure 100% typography contrast
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    
    for x in range(W):
        if x < 440:
            alpha = 235
        elif x < 720:
            # Cosine decay
            t = (x - 440) / 280.0
            alpha = int(235 * (0.5 + 0.5 * math.cos(math.pi * t)))
        else:
            alpha = 0
        vdraw.line([(x, 0), (x, H)], fill=(6, 10, 18, alpha))
        
    # Top and bottom subtle edge vignette
    for y in range(100):
        alpha = int(180 * (1.0 - y / 100.0))
        vdraw.line([(0, y), (W, y)], fill=(4, 7, 12, alpha))
    for y in range(H - 100, H):
        alpha = int(180 * ((y - (H - 100)) / 100.0))
        vdraw.line([(0, y), (W, y)], fill=(4, 7, 12, alpha))
        
    canvas = Image.alpha_composite(canvas, vignette)
    
    # 3. Add secondary evidence thumbnail inset: CJP Cockroach emblem (upper right)
    if BEAT_06.exists():
        emblem = Image.open(BEAT_06).convert("RGBA")
        ew, eh = 190, 190
        emblem = emblem.resize((ew, eh), Image.Resampling.LANCZOS)
        
        mask = Image.new("L", (ew, eh), 0)
        md = ImageDraw.Draw(mask)
        md.ellipse([4, 4, ew - 4, eh - 4], fill=255)
        
        plate = Image.new("RGBA", (ew, eh), (0, 0, 0, 0))
        pd = ImageDraw.Draw(plate)
        pd.ellipse([2, 2, ew - 2, eh - 2], fill=(12, 18, 30, 240), outline=(251, 191, 36, 255), width=3)
        
        emblem_x = W - ew - 42
        emblem_y = 48
        canvas.paste(plate, (emblem_x, emblem_y), plate)
        canvas.paste(emblem, (emblem_x, emblem_y), mask)
        
        font_tag = get_font(FONT_MONO, 15)
        draw_ov = ImageDraw.Draw(canvas)
        draw_badge(draw_ov, "CJP YOUTH EMBLEM", (emblem_x + 8, emblem_y + eh - 20), font_tag,
                   bg_color=(10, 15, 25, 240), text_color=(251, 191, 36, 255),
                   pad_x=12, pad_y=5, radius=6, border_color=(251, 191, 36, 200), border_width=1)

    # 4. Tilted distressed rubber stamp "[45 STATIONS LOCKED]" over metro shutter
    font_stamp = get_font(FONT_ANTON, 38)
    stamp_img = draw_rubber_stamp("45 STATIONS LOCKED", font_stamp,
                                  text_color=(244, 63, 94, 250), border_color=(244, 63, 94, 240), angle=-8)
    canvas.paste(stamp_img, (670, 370), stamp_img)
    
    # 5. Left Typography Hierarchy (Anton + Inter + JetBrains Mono)
    draw = ImageDraw.Draw(canvas)
    
    font_hero = get_font(FONT_ANTON, 94)
    font_badge = get_font(FONT_ANTON, 52)
    font_callout = get_font(FONT_INTER, 27)
    font_mono = get_font(FONT_MONO, 18)
    font_brand = get_font(FONT_INTER, 20)
    
    # A. Top-Left Brand Pill
    if LOGO_PATH.exists():
        logo = Image.open(LOGO_PATH).convert("RGBA").resize((38, 38), Image.Resampling.LANCZOS)
        pill_w, pill_h = 240, 50
        draw.rounded_rectangle([48, 36, 48 + pill_w, 36 + pill_h], radius=25,
                               fill=(11, 16, 26, 245), outline=(251, 191, 36, 220), width=2)
        canvas.paste(logo, (56, 42), logo)
        draw.text((102, 48), "BENAQAAB INDIA", font=font_brand, fill=(255, 255, 255, 255))
        
    # B. Live Breaking News Tag
    draw_badge(draw, "GROUND ZERO EXPOSÉ", (310, 42), font_mono,
               bg_color=(225, 29, 72, 240), text_color=(255, 255, 255, 255),
               pad_x=16, pad_y=6, radius=8, border_color=(254, 205, 211, 200), border_width=1, icon_type="dot")

    # C. Main Shock Hook: "DELHI LOCKDOWN!"
    hero_text = "DELHI LOCKDOWN!"
    hx = 48
    hy = 135
    # Heavy 3D drop-shadow
    for off in [(-4, 0), (4, 0), (0, -4), (0, 4), (-3, -3), (3, 3), (-4, 4), (4, 4), (0, 7), (0, 10)]:
        draw.text((hx + off[0], hy + off[1]), hero_text, font=font_hero, fill=(0, 0, 0, 255))
    draw.text((hx, hy), hero_text, font=font_hero, fill=(255, 255, 255, 255))
    
    # D. Red Warning Badge: "45 METRO STATIONS BAND!"
    badge_text = "45 METRO STATIONS BAND!"
    by = 265
    draw_badge(draw, badge_text, (hx, by), font_badge,
               bg_color=(225, 29, 72, 250), text_color=(255, 255, 255, 255),
               pad_x=26, pad_y=14, radius=16, border_color=(254, 205, 211, 255), border_width=3, icon_type="alert")
               
    # E. Amber Callout Pill: "CJP PROTEST: \"MAKKHI PAR HATHOUDA?\""
    callout_text = 'CJP PROTEST: "MAKKHI PAR HATHOUDA?"'
    cy = 385
    draw_badge(draw, callout_text, (hx, cy), font_callout,
               bg_color=(251, 191, 36, 245), text_color=(15, 23, 42, 255),
               pad_x=22, pad_y=12, radius=12, border_color=(255, 255, 255, 220), border_width=2)
               
    # F. Sub-fact Pill: "25,000 POLICE DEPLOYED · BNSS 163 · TRAINS CANCELLED"
    fact_text = "25,000 POLICE DEPLOYED · BNSS 163 · TRAINS CANCELLED"
    fy = 465
    draw_badge(draw, fact_text, (hx, fy), font_mono,
               bg_color=(15, 23, 42, 235), text_color=(147, 197, 253, 255),
               pad_x=18, pad_y=10, radius=10, border_color=(56, 189, 248, 180), border_width=1)
               
    # G. Channel Credential Footer
    draw.text((52, 665), "SACH · SABOOT · BEBAK | PRIMARY EVIDENCE VERIFIED",
              font=get_font(FONT_INTER, 16), fill=(148, 163, 184, 220))
              
    final_rgb = canvas.convert("RGB")
    final_rgb.save(OUT_16X9, quality=98)
    final_rgb.save(OUT_16X9_ALT, quality=98)
    print(f"✅ Generated Widescreen 16:9 Thumbnail: {OUT_16X9}")

def generate_vertical_9x16():
    W, H = 1080, 1920
    canvas = Image.new("RGBA", (W, H), (7, 11, 18, 255))
    
    # 1. Full-bleed vertical hero image (Locked Metro Gate & stranded students)
    if BEAT_01.exists():
        hero = Image.open(BEAT_01).convert("RGBA")
        hero = ImageEnhance.Contrast(hero).enhance(1.25)
        hero = ImageEnhance.Color(hero).enhance(1.15)
        hero = hero.resize((W, H), Image.Resampling.LANCZOS)
        canvas.paste(hero, (0, 0))
        
    # 2. Gradient Vignettes
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    odraw = ImageDraw.Draw(overlay)
    
    # Top dark vignette (0..680px)
    for y in range(680):
        alpha = int(245 * (1.0 - (y / 680.0) ** 1.3))
        odraw.line([(0, y), (W, y)], fill=(6, 10, 18, alpha))
        
    # Bottom vignette (1550..1920px)
    for y in range(1550, H):
        alpha = int(235 * ((y - 1550) / 370.0))
        odraw.line([(0, y), (W, y)], fill=(6, 10, 18, alpha))
        
    canvas = Image.alpha_composite(canvas, overlay)
    
    # 3. Stamp in upper center right
    font_stamp = get_font(FONT_ANTON, 52)
    stamp_img = draw_rubber_stamp("45 STATIONS LOCKED", font_stamp,
                                  text_color=(244, 63, 94, 250), border_color=(244, 63, 94, 240), angle=-8)
    canvas.paste(stamp_img, (520, 690), stamp_img)
    
    # 4. Top Typography Hierarchy
    draw = ImageDraw.Draw(canvas)
    
    font_hero = get_font(FONT_ANTON, 124)
    font_badge = get_font(FONT_ANTON, 72)
    font_callout = get_font(FONT_INTER, 42)
    font_mono = get_font(FONT_MONO, 28)
    
    # A. Top Brand Capsule
    if LOGO_PATH.exists():
        logo = Image.open(LOGO_PATH).convert("RGBA").resize((48, 48), Image.Resampling.LANCZOS)
        pill_w, pill_h = 320, 64
        pill_x = (W - pill_w) // 2
        pill_y = 50
        draw.rounded_rectangle([pill_x, pill_y, pill_x + pill_w, pill_y + pill_h], radius=32,
                               fill=(11, 16, 26, 245), outline=(251, 191, 36, 230), width=2)
        canvas.paste(logo, (pill_x + 12, pill_y + 8), logo)
        draw.text((pill_x + 70, pill_y + 16), "BENAQAAB INDIA", font=get_font(FONT_INTER, 24), fill=(255, 255, 255, 255))

    # B. Main Shock Hook: "DELHI LOCKDOWN?"
    hero_text = "DELHI LOCKDOWN?"
    bbox = font_hero.getbbox(hero_text)
    tw = bbox[2] - bbox[0]
    hx = (W - tw) // 2
    hy = 150
    
    for off in [(-5, 0), (5, 0), (0, -5), (0, 5), (-4, -4), (4, 4), (0, 8), (0, 12)]:
        draw.text((hx + off[0], hy + off[1]), hero_text, font=font_hero, fill=(0, 0, 0, 255))
    draw.text((hx, hy), hero_text, font=font_hero, fill=(255, 255, 255, 255))
    
    # C. Red Warning Badge: "45 METRO STATIONS BAND!"
    badge_text = "45 METRO STATIONS BAND!"
    bw_box = font_badge.getbbox(badge_text)
    bw = bw_box[2] - bw_box[0] + 64 + 48 # including alert icon
    bx = (W - bw) // 2
    by = 310
    draw_badge(draw, badge_text, (bx, by), font_badge,
               bg_color=(225, 29, 72, 250), text_color=(255, 255, 255, 255),
               pad_x=32, pad_y=16, radius=20, border_color=(254, 205, 211, 255), border_width=3, icon_type="alert")
               
    # D. Amber Callout: "CJP YOUTH PROTEST EXPOSED"
    callout_text = "CJP YOUTH PROTEST EXPOSED"
    cw_box = font_callout.getbbox(callout_text)
    cw = cw_box[2] - cw_box[0] + 56
    cx = (W - cw) // 2
    cy = 460
    draw_badge(draw, callout_text, (cx, cy), font_callout,
               bg_color=(251, 191, 36, 245), text_color=(15, 23, 42, 255),
               pad_x=28, pad_y=14, radius=16, border_color=(255, 255, 255, 220), border_width=2)

    # E. Bottom Fact Tag: "25,000 POLICE · BNSS 163 · TRAINS CANCELLED"
    draw_badge(draw, "25,000 POLICE · BNSS 163 · TRAINS CANCELLED", ((W - 740) // 2, 1750), font_mono,
               bg_color=(15, 23, 42, 240), text_color=(147, 197, 253, 255),
               pad_x=24, pad_y=12, radius=12, border_color=(56, 189, 248, 200), border_width=2)
               
    # F. Bottom Credential Line
    cred_text = "SACH · SABOOT · BEBAK | PRIMARY EVIDENCE VERIFIED"
    cb = get_font(FONT_INTER, 20).getbbox(cred_text)
    draw.text(((W - (cb[2] - cb[0])) // 2, 1850), cred_text,
              font=get_font(FONT_INTER, 20), fill=(203, 213, 225, 230))
              
    final_rgb = canvas.convert("RGB")
    final_rgb.save(OUT_9X16, quality=98)
    final_rgb.save(OUT_9X16_ALT, quality=98)
    print(f"✅ Generated Mobile 9:16 Thumbnail: {OUT_9X16}")

if __name__ == '__main__':
    print("🚀 Running Broadcast-Grade Thumbnail Engine...")
    generate_landscape_16x9()
    generate_vertical_9x16()
    print("🎉 High-CTR Thumbnails generated successfully!")
