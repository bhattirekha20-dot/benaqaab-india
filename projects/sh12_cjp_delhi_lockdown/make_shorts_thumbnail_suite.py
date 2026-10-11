#!/usr/bin/env python3
"""
make_shorts_thumbnail_suite.py — Master YouTube Shorts (9:16) Thumbnail Suite
Project: SH-12 Delhi Lockdown & CJP Youth Protest
Adheres strictly to Mobile Shorts Feed High-CTR Standards:
- 1080x1920 Full HD Vertical
- Upper 35% Curiosity Safe Zone (100% visible on Shorts shelf and search)
- Giant Anton Typography (readable from 2 meters away on a phone)
- High-contrast color psychology: White + Crimson (#E11D48) + Signal Amber (#FBBF24)
- 3 Distinct High-Impact Creative Options
"""

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
BEAT_03 = PROJECT_DIR / "assets" / "visuals" / "beat_03.jpg" # Police Barricades
BEAT_06 = PROJECT_DIR / "assets" / "visuals" / "beat_06.jpg" # CJP Amber Cockroach Emblem
BEAT_08 = PROJECT_DIR / "assets" / "visuals" / "beat_08.jpg" # Supreme Court Gavel

OUT_PRIMARY = PROJECT_DIR / "SH12_Thumbnail_9x16.jpg"
OUT_PRIMARY_ALT = PROJECT_DIR / "thumbnail_1080x1920.jpg"
OUT_OPT1 = PROJECT_DIR / "Shorts_Thumb_01_Lockdown.jpg"
OUT_OPT2 = PROJECT_DIR / "Shorts_Thumb_02_Hammer.jpg"
OUT_OPT3 = PROJECT_DIR / "Shorts_Thumb_03_Police_CJP.jpg"

def get_font(path, size):
    try:
        return ImageFont.truetype(str(path), size)
    except Exception:
        return ImageFont.load_default()

def draw_badge(draw, text, xy, font, bg_color, text_color, pad_x=28, pad_y=14, radius=16, border_color=None, border_width=2, icon_type=None):
    x, y = xy
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    
    icon_w = 0
    if icon_type == "alert":
        icon_w = th + 16
    elif icon_type == "dot":
        icon_w = 24
        
    w = tw + pad_x * 2 + icon_w
    h = th + pad_y * 2
    
    draw.rounded_rectangle([x, y, x + w, y + h], radius=int(radius), fill=bg_color, outline=border_color, width=int(border_width))
    
    curr_x = x + pad_x
    if icon_type == "alert":
        cx = curr_x + (th // 2)
        cy = y + (h // 2)
        r = th // 2
        draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, 240))
        draw.line([(cx, cy - r + 4), (cx, cy + 2)], fill=(225, 29, 72, 255), width=int(math.ceil(th / 10.0)))
        draw.point([(cx, cy + r - 4), (cx, cy + r - 3)], fill=(225, 29, 72, 255))
        curr_x += th + 14
    elif icon_type == "dot":
        cx = curr_x + 10
        cy = y + (h // 2)
        draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=(244, 63, 94, 255))
        curr_x += 24
        
    ty = y + pad_y - bbox[1]
    draw.text((curr_x, ty), text, font=font, fill=text_color)
    return w, h

def draw_rubber_stamp(text, font, text_color=(244, 63, 94, 250), border_color=(244, 63, 94, 240), angle=-8):
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    pad_x, pad_y = 30, 14
    w = tw + pad_x * 2
    h = th + pad_y * 2
    
    stamp = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    sdraw = ImageDraw.Draw(stamp)
    sdraw.rounded_rectangle([2, 2, w - 2, h - 2], radius=10, outline=border_color, width=5)
    sdraw.rounded_rectangle([8, 8, w - 8, h - 8], radius=6, outline=border_color, width=2)
    
    tx = pad_x - bbox[0]
    ty = pad_y - bbox[1]
    sdraw.text((tx, ty), text, font=font, fill=text_color)
    
    return stamp.rotate(angle, resample=Image.BICUBIC, expand=True)

def draw_top_brand_pill(canvas, W):
    if LOGO_PATH.exists():
        logo = Image.open(LOGO_PATH).convert("RGBA").resize((44, 44), Image.Resampling.LANCZOS)
        pill_w, pill_h = 300, 58
        pill_x = (W - pill_w) // 2
        pill_y = 48
        draw = ImageDraw.Draw(canvas)
        draw.rounded_rectangle([pill_x, pill_y, pill_x + pill_w, pill_y + pill_h], radius=29,
                               fill=(11, 16, 26, 245), outline=(251, 191, 36, 230), width=2)
        canvas.paste(logo, (pill_x + 12, pill_y + 7), logo)
        draw.text((pill_x + 68, pill_y + 14), "BENAQAAB INDIA", font=get_font(FONT_INTER, 22), fill=(255, 255, 255, 255))

# =========================================================================
# OPTION 1: THE GROUND ZERO EMERGENCY (DELHI LOCKDOWN? / 45 STATIONS BAND!)
# =========================================================================
def generate_option_1():
    W, H = 1080, 1920
    canvas = Image.new("RGBA", (W, H), (7, 10, 18, 255))
    
    # Hero: beat_01 (Locked Metro Shutter & Police Tape)
    hero = Image.open(BEAT_01).convert("RGBA")
    hero = ImageEnhance.Contrast(hero).enhance(1.26)
    hero = ImageEnhance.Color(hero).enhance(1.15)
    hero = hero.resize((W, H), Image.Resampling.LANCZOS)
    canvas.paste(hero, (0, 0))
    
    # Smooth Top Vignette (0..680px)
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    for y in range(680):
        alpha = int(245 * (1.0 - (y / 680.0) ** 1.35))
        vdraw.line([(0, y), (W, y)], fill=(6, 10, 18, alpha))
    canvas = Image.alpha_composite(canvas, vignette)
    
    # Rubber Stamp over shutter: "[45 STATIONS LOCKED]"
    font_stamp = get_font(FONT_ANTON, 54)
    stamp_img = draw_rubber_stamp("45 STATIONS LOCKED", font_stamp, angle=-8)
    canvas.paste(stamp_img, (510, 710), stamp_img)
    
    # Top Brand Pill
    draw_top_brand_pill(canvas, W)
    
    # Top Typography
    draw = ImageDraw.Draw(canvas)
    font_hero = get_font(FONT_ANTON, 134)
    font_badge = get_font(FONT_ANTON, 76)
    font_callout = get_font(FONT_INTER, 44)
    
    # 1. Main Hook: "DELHI LOCKDOWN?"
    hero_text = "DELHI LOCKDOWN?"
    bbox = font_hero.getbbox(hero_text)
    tw = bbox[2] - bbox[0]
    hx = (W - tw) // 2
    hy = 145
    for off in [(-5, 0), (5, 0), (0, -5), (0, 5), (-4, -4), (4, 4), (0, 8), (0, 13)]:
        draw.text((hx + off[0], hy + off[1]), hero_text, font=font_hero, fill=(0, 0, 0, 255))
    draw.text((hx, hy), hero_text, font=font_hero, fill=(255, 255, 255, 255))
    
    # 2. Red Warning Badge: "45 METRO STATIONS BAND!"
    badge_text = "45 METRO STATIONS BAND!"
    bw_box = font_badge.getbbox(badge_text)
    bw = bw_box[2] - bw_box[0] + 64 + 52
    bx = (W - bw) // 2
    by = 315
    draw_badge(draw, badge_text, (bx, by), font_badge,
               bg_color=(225, 29, 72, 250), text_color=(255, 255, 255, 255),
               pad_x=32, pad_y=16, radius=20, border_color=(254, 205, 211, 255), border_width=3, icon_type="alert")
               
    # 3. Amber Callout: "CJP YOUTH PROTEST EXPOSED"
    callout_text = "CJP YOUTH PROTEST EXPOSED"
    cw_box = font_callout.getbbox(callout_text)
    cw = cw_box[2] - cw_box[0] + 56
    cx = (W - cw) // 2
    cy = 475
    draw_badge(draw, callout_text, (cx, cy), font_callout,
               bg_color=(251, 191, 36, 245), text_color=(15, 23, 42, 255),
               pad_x=28, pad_y=14, radius=16, border_color=(255, 255, 255, 220), border_width=2)
               
    final_rgb = canvas.convert("RGB")
    final_rgb.save(OUT_OPT1, quality=98)
    final_rgb.save(OUT_PRIMARY, quality=98)
    final_rgb.save(OUT_PRIMARY_ALT, quality=98)
    print(f"✅ Option 1 Saved: {OUT_OPT1.name} (Primary Master)")

# =========================================================================
# OPTION 2: THE JUDICIAL SHOWDOWN (MAKKHI PAR HATHOUDA? / SC SLAMS GOVT!)
# =========================================================================
def generate_option_2():
    W, H = 1080, 1920
    canvas = Image.new("RGBA", (W, H), (7, 10, 18, 255))
    
    # Hero: beat_08 (Supreme Court Gavel) blended with beat_01 (Metro Shutter) in bottom half
    gavel = Image.open(BEAT_08).convert("RGBA")
    gavel = ImageEnhance.Contrast(gavel).enhance(1.24)
    gavel = ImageEnhance.Color(gavel).enhance(1.15)
    gavel = gavel.resize((W, H), Image.Resampling.LANCZOS)
    canvas.paste(gavel, (0, 0))
    
    # Top dark vignette
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    for y in range(650):
        alpha = int(245 * (1.0 - (y / 650.0) ** 1.35))
        vdraw.line([(0, y), (W, y)], fill=(6, 10, 18, alpha))
    canvas = Image.alpha_composite(canvas, vignette)
    
    # Stamp: "CONTEMPT NOTICE"
    font_stamp = get_font(FONT_ANTON, 56)
    stamp_img = draw_rubber_stamp("CONTEMPT NOTICE", font_stamp, angle=-9)
    canvas.paste(stamp_img, (500, 720), stamp_img)
    
    # Brand Pill
    draw_top_brand_pill(canvas, W)
    
    draw = ImageDraw.Draw(canvas)
    font_hero = get_font(FONT_ANTON, 108)
    font_badge = get_font(FONT_ANTON, 72)
    font_sub = get_font(FONT_INTER, 42)
    
    # 1. Main Hook: "MAKKHI PAR HATHOUDA?"
    hero_text = "MAKKHI PAR HATHOUDA?"
    bbox = font_hero.getbbox(hero_text)
    tw = bbox[2] - bbox[0]
    hx = (W - tw) // 2
    hy = 145
    for off in [(-5, 0), (5, 0), (0, -5), (0, 5), (-4, -4), (4, 4), (0, 8), (0, 12)]:
        draw.text((hx + off[0], hy + off[1]), hero_text, font=font_hero, fill=(0, 0, 0, 255))
    draw.text((hx, hy), hero_text, font=font_hero, fill=(251, 191, 36, 255)) # Glowing Gold
    
    # 2. Red Badge: "SUPREME COURT SLAMS GOVT!"
    badge_text = "SUPREME COURT SLAMS!"
    bw_box = font_badge.getbbox(badge_text)
    bw = bw_box[2] - bw_box[0] + 64 + 48
    bx = (W - bw) // 2
    by = 310
    draw_badge(draw, badge_text, (bx, by), font_badge,
               bg_color=(225, 29, 72, 250), text_color=(255, 255, 255, 255),
               pad_x=32, pad_y=16, radius=20, border_color=(254, 205, 211, 255), border_width=3, icon_type="alert")
               
    # 3. White Pill: "45 METRO KYUN BAND KIYE?"
    sub_text = "45 METRO STATIONS KYUN BAND?"
    sw_box = font_sub.getbbox(sub_text)
    sw = sw_box[2] - sw_box[0] + 56
    sx = (W - sw) // 2
    sy = 470
    draw_badge(draw, sub_text, (sx, sy), font_sub,
               bg_color=(15, 23, 42, 245), text_color=(255, 255, 255, 255),
               pad_x=28, pad_y=14, radius=16, border_color=(56, 189, 248, 220), border_width=2)
               
    final_rgb = canvas.convert("RGB")
    final_rgb.save(OUT_OPT2, quality=98)
    print(f"✅ Option 2 Saved: {OUT_OPT2.name}")

# =========================================================================
# OPTION 3: THE 25,000 POLICE CLASH (25,000 POLICE! / KAUN HAI CJP?)
# =========================================================================
def generate_option_3():
    W, H = 1080, 1920
    canvas = Image.new("RGBA", (W, H), (7, 10, 18, 255))
    
    # Hero: beat_03 (Police riot barricades) + beat_06 (CJP Cockroach Emblem)
    police = Image.open(BEAT_03).convert("RGBA")
    police = ImageEnhance.Contrast(police).enhance(1.25)
    police = ImageEnhance.Color(police).enhance(1.15)
    police = police.resize((W, H), Image.Resampling.LANCZOS)
    canvas.paste(police, (0, 0))
    
    # Inset large glowing CJP Cockroach emblem in center
    if BEAT_06.exists():
        emblem = Image.open(BEAT_06).convert("RGBA")
        ew, eh = 420, 420
        emblem = emblem.resize((ew, eh), Image.Resampling.LANCZOS)
        
        mask = Image.new("L", (ew, eh), 0)
        md = ImageDraw.Draw(mask)
        md.ellipse([8, 8, ew - 8, eh - 8], fill=255)
        
        plate = Image.new("RGBA", (ew, eh), (0, 0, 0, 0))
        pd = ImageDraw.Draw(plate)
        pd.ellipse([4, 4, ew - 4, eh - 4], fill=(12, 18, 30, 245), outline=(251, 191, 36, 255), width=5)
        
        em_x = (W - ew) // 2
        em_y = 750
        canvas.paste(plate, (em_x, em_y), plate)
        canvas.paste(emblem, (em_x, em_y), mask)
    
    # Top dark vignette
    vignette = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    vdraw = ImageDraw.Draw(vignette)
    for y in range(650):
        alpha = int(245 * (1.0 - (y / 650.0) ** 1.35))
        vdraw.line([(0, y), (W, y)], fill=(6, 10, 18, alpha))
    canvas = Image.alpha_composite(canvas, vignette)
    
    # Stamp: "BNSS SECTION 163"
    font_stamp = get_font(FONT_ANTON, 52)
    stamp_img = draw_rubber_stamp("BNSS SECTION 163", font_stamp, angle=-8)
    canvas.paste(stamp_img, (520, 1220), stamp_img)
    
    # Brand Pill
    draw_top_brand_pill(canvas, W)
    
    draw = ImageDraw.Draw(canvas)
    font_hero = get_font(FONT_ANTON, 136)
    font_badge = get_font(FONT_ANTON, 72)
    font_sub = get_font(FONT_INTER, 42)
    
    # 1. Main Hook: "25,000 POLICE!"
    hero_text = "25,000 POLICE!"
    bbox = font_hero.getbbox(hero_text)
    tw = bbox[2] - bbox[0]
    hx = (W - tw) // 2
    hy = 145
    for off in [(-5, 0), (5, 0), (0, -5), (0, 5), (-4, -4), (4, 4), (0, 8), (0, 12)]:
        draw.text((hx + off[0], hy + off[1]), hero_text, font=font_hero, fill=(0, 0, 0, 255))
    draw.text((hx, hy), hero_text, font=font_hero, fill=(255, 255, 255, 255))
    
    # 2. Red Badge: "DELHI HIGH ALERT!"
    badge_text = "DELHI HIGH ALERT!"
    bw_box = font_badge.getbbox(badge_text)
    bw = bw_box[2] - bw_box[0] + 64 + 48
    bx = (W - bw) // 2
    by = 310
    draw_badge(draw, badge_text, (bx, by), font_badge,
               bg_color=(225, 29, 72, 250), text_color=(255, 255, 255, 255),
               pad_x=32, pad_y=16, radius=20, border_color=(254, 205, 211, 255), border_width=3, icon_type="alert")
               
    # 3. Amber Callout: "KAUN HAI CJP YOUTH?"
    sub_text = "KAUN HAI YE COCKROACH PARTY?"
    sw_box = font_sub.getbbox(sub_text)
    sw = sw_box[2] - sw_box[0] + 56
    sx = (W - sw) // 2
    sy = 470
    draw_badge(draw, sub_text, (sx, sy), font_sub,
               bg_color=(251, 191, 36, 245), text_color=(15, 23, 42, 255),
               pad_x=28, pad_y=14, radius=16, border_color=(255, 255, 255, 220), border_width=2)
               
    final_rgb = canvas.convert("RGB")
    final_rgb.save(OUT_OPT3, quality=98)
    print(f"✅ Option 3 Saved: {OUT_OPT3.name}")

if __name__ == '__main__':
    print("🚀 Generating YouTube Shorts (9:16) Thumbnail Suite...")
    generate_option_1()
    generate_option_2()
    generate_option_3()
    print("🎉 All 3 YouTube Shorts Thumbnails successfully generated!")
