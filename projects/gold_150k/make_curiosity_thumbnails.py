#!/usr/bin/env python3
"""
make_curiosity_thumbnails.py — High-CTR Curiosity Thumbnail Generator for Benaqaab India
Project: Sona ₹1.5 Lakh: The Real Showroom Bill (SH-08)
Outputs both clean base plates (for manual editing in Photoshop/Canva) and 
final typography-first high-contrast curiosity thumbnails (ready for direct upload).
"""

import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

ROOT = Path(__file__).resolve().parent
WORKSPACE = ROOT.parent.parent
FONT_ANTON = WORKSPACE / "brand" / "fonts" / "Anton.ttf"
FONT_INTER = WORKSPACE / "brand" / "fonts" / "Inter.ttf"

def draw_badge(draw, text, xy, font, bg_color, text_color, pad_x=24, pad_y=12, radius=12, border_color=None, border_width=2):
    x, y = xy
    bbox = font.getbbox(text)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    w = tw + pad_x * 2
    h = th + pad_y * 2
    
    # Draw background box with rounded corners
    draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=bg_color, outline=border_color, width=border_width)
    
    # Text centered
    tx = x + pad_x - bbox[0]
    ty = y + pad_y - bbox[1]
    draw.text((tx, ty), text, font=font, fill=text_color)
    return w, h

def create_vertical_curiosity():
    src_path = ROOT / "thumbnail_1080x1920.jpg"
    clean_out = ROOT / "thumbnail_clean_base_1080x1920.jpg"
    final_out = ROOT / "thumbnail_curiosity_text_1080x1920.jpg"
    
    im = Image.open(src_path).convert("RGBA")
    # Save clean base
    im.convert("RGB").save(clean_out, quality=95)
    print(f"✅ Saved clean vertical base: {clean_out.name}")

    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Top dark vignette gradient for typography legibility
    for y in range(550):
        alpha = int(220 * (1.0 - (y / 550.0) ** 1.3))
        draw.line([(0, y), (1080, y)], fill=(5, 7, 12, alpha))

    # Fonts
    font_hero = ImageFont.truetype(str(FONT_ANTON), 116)
    font_badge = ImageFont.truetype(str(FONT_ANTON), 72)
    font_sub = ImageFont.truetype(str(FONT_INTER), 42)
    font_disc = ImageFont.truetype(str(FONT_INTER), 26)

    # 1. Main Curiosity Hook: "SONA ₹1.5 LAKH?"
    hero_text = "SONA ₹1.5 LAKH?"
    bbox = font_hero.getbbox(hero_text)
    tw = bbox[2] - bbox[0]
    hx = (1080 - tw) // 2
    hy = 80

    # Glow shadow
    for off in [(-4, 0), (4, 0), (0, -4), (0, 4), (-3, -3), (3, 3), (0, 6)]:
        draw.text((hx + off[0], hy + off[1]), hero_text, font=font_hero, fill=(0, 0, 0, 240))
    # Fill in bright gold / white
    draw.text((hx, hy), hero_text, font=font_hero, fill=(255, 255, 255, 255))

    # 2. Red Warning Badge: "ASLI BILL = ₹1.82 LAKH!"
    badge_text = "ASLI BILL = ₹1.82 LAKH!"
    bw_box = font_badge.getbbox(badge_text)
    bw = bw_box[2] - bw_box[0] + 60
    bx = (1080 - bw) // 2
    by = 225
    draw_badge(draw, badge_text, (bx, by), font_badge, 
               bg_color=(225, 29, 72, 245), text_color=(255, 255, 255, 255),
               pad_x=30, pad_y=16, radius=18, border_color=(254, 205, 211, 255), border_width=3)

    # 3. Yellow Callout: "₹31,000 EXTRA KAHAN GAYA?"
    callout_text = "₹31,000 EXTRA KAHAN GAYA?"
    cw_box = font_sub.getbbox(callout_text)
    cw = cw_box[2] - cw_box[0] + 50
    cx = (1080 - cw) // 2
    cy = 360
    draw_badge(draw, callout_text, (cx, cy), font_sub,
               bg_color=(251, 191, 36, 240), text_color=(15, 23, 42, 255),
               pad_x=25, pad_y=12, radius=14, border_color=(255, 255, 255, 200), border_width=2)

    # 4. Discreet Disclosure: "AI ILLUSTRATIVE · BENAQAAB INDIA"
    draw_badge(draw, "AI ILLUSTRATIVE · BENAQAAB INDIA", (36, 1850), font_disc,
               bg_color=(0, 0, 0, 180), text_color=(203, 213, 225, 255),
               pad_x=16, pad_y=8, radius=8, border_color=(255, 255, 255, 60), border_width=1)

    combined = Image.alpha_composite(im, overlay)
    combined.convert("RGB").save(final_out, quality=95)
    print(f"🔥 Saved finished curiosity vertical thumbnail: {final_out.name}")

def create_landscape_curiosity():
    src_path = ROOT / "thumbnail_1280x720.jpg"
    clean_out = ROOT / "thumbnail_clean_base_1280x720.jpg"
    final_out = ROOT / "thumbnail_curiosity_text_1280x720.jpg"

    im = Image.open(src_path).convert("RGBA")
    # Save clean base
    im.convert("RGB").save(clean_out, quality=95)
    print(f"✅ Saved clean landscape base: {clean_out.name}")

    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Left gradient underlay
    for x in range(650):
        alpha = int(210 * (1.0 - (x / 650.0) ** 1.4))
        draw.line([(x, 0), (x, 720)], fill=(5, 7, 12, alpha))

    # Fonts
    font_hero = ImageFont.truetype(str(FONT_ANTON), 88)
    font_badge = ImageFont.truetype(str(FONT_ANTON), 54)
    font_sub = ImageFont.truetype(str(FONT_INTER), 28)
    font_disc = ImageFont.truetype(str(FONT_INTER), 18)

    # 1. Main Curiosity Hook: "SONA ₹1.5 LAKH?"
    hero_text = "SONA ₹1.5 LAKH?"
    hx = 50
    hy = 50
    for off in [(-3, 0), (3, 0), (0, -3), (0, 3), (-2, -2), (2, 2), (0, 5)]:
        draw.text((hx + off[0], hy + off[1]), hero_text, font=font_hero, fill=(0, 0, 0, 240))
    draw.text((hx, hy), hero_text, font=font_hero, fill=(255, 255, 255, 255))

    # 2. Red Warning Badge: "ASLI BILL = ₹1.82 LAKH!"
    badge_text = "ASLI BILL = ₹1.82 LAKH!"
    by = 175
    draw_badge(draw, badge_text, (hx, by), font_badge,
               bg_color=(225, 29, 72, 245), text_color=(255, 255, 255, 255),
               pad_x=24, pad_y=12, radius=14, border_color=(254, 205, 211, 255), border_width=3)

    # 3. Yellow Highlight Strip: "MAKING CHARGES EXPOSED: +₹31,000"
    sub_text = "MAKING CHARGES EXPOSED: +₹31,000"
    sy = 275
    draw_badge(draw, sub_text, (hx, sy), font_sub,
               bg_color=(251, 191, 36, 240), text_color=(15, 23, 42, 255),
               pad_x=20, pad_y=10, radius=10, border_color=(255, 255, 255, 220), border_width=2)

    # 4. Small Disclosure
    draw_badge(draw, "AI ILLUSTRATIVE · BENAQAAB INDIA", (50, 665), font_disc,
               bg_color=(0, 0, 0, 180), text_color=(203, 213, 225, 255),
               pad_x=12, pad_y=6, radius=6, border_color=(255, 255, 255, 60), border_width=1)

    combined = Image.alpha_composite(im, overlay)
    combined.convert("RGB").save(final_out, quality=95)
    print(f"🔥 Saved finished curiosity landscape thumbnail: {final_out.name}")

if __name__ == "__main__":
    create_vertical_curiosity()
    create_landscape_curiosity()
    print("✨ All thumbnail variants generated successfully!")
