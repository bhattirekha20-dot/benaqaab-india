#!/usr/bin/env python3
"""
🖼️ BENAQAAB THUMBNAIL & COVER GENERATOR
Automates creation of uncropped 16:9 YouTube thumbnails (1280x720)
and 9:16 Shorts covers (1080x1920) directly from project assets.
"""

import argparse
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

def get_font(font_path, size):
    try:
        return ImageFont.truetype(str(font_path), size)
    except Exception:
        return ImageFont.load_default()

def generate_landscape_thumbnail(hero_img_path, headline_en, headline_hi, out_path, date_str="2026"):
    w, h = 1280, 720
    img = Image.new('RGB', (w, h), (10, 15, 20))

    if hero_img_path and Path(hero_img_path).exists():
        try:
            hero = Image.open(hero_img_path).convert('RGB')
            # Fit and fill center
            hero_ratio = hero.width / hero.height
            target_ratio = w / h
            if hero_ratio > target_ratio:
                new_h = h
                new_w = int(h * hero_ratio)
            else:
                new_w = w
                new_h = int(w / hero_ratio)
            hero = hero.resize((new_w, new_h), Image.Resampling.LANCZOS)
            crop_x = (new_w - w) // 2
            crop_y = (new_h - h) // 2
            hero = hero.crop((crop_x, crop_y, crop_x + w, crop_y + h))
            img.paste(hero, (0, 0))
        except Exception as e:
            print(f"Warning: could not process hero image: {e}")

    # Gradient Vignette Overlays
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw_ov = ImageDraw.Draw(overlay)
    for y in range(h):
        if y < 140:
            alpha = int(220 * (1 - y / 140))
            draw_ov.line([(0, y), (w, y)], fill=(8, 12, 18, alpha))
        elif y > 280:
            alpha = int(245 * ((y - 280) / (h - 280)))
            draw_ov.line([(0, y), (w, y)], fill=(6, 9, 14, alpha))

    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)

    font_bold = Path("brand/fonts/Outfit-Bold.ttf")
    font_sans = Path("brand/fonts/Inter-Bold.ttf")

    f_badge = get_font(font_bold, 24)
    f_title = get_font(font_bold, 64)
    f_sub = get_font(font_bold, 40)

    # Top-Left Logo Bug Pill
    draw.rounded_rectangle([48, 36, 320, 84], radius=10, fill=(10, 15, 22), outline=(251, 191, 36), width=2)
    draw.text((64, 46), "BENAQAAB INDIA", fill=(255, 255, 255), font=f_badge)

    # Top-Right Date Tag
    draw.rounded_rectangle([w - 240, 36, w - 48, 84], radius=10, fill=(10, 15, 22), outline=(56, 189, 248), width=2)
    draw.text((w - 218, 46), date_str, fill=(56, 189, 248), font=f_badge)

    # Main Headline (3-4 words)
    draw.text((50, 430), headline_en.upper(), fill=(255, 255, 255), font=f_title)
    if headline_hi:
        draw.text((50, 515), headline_hi, fill=(251, 191, 36), font=f_title)

    # Gold Bottom Border
    draw.line([(0, h - 6), (w, h - 6)], fill=(251, 191, 36), width=6)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, 'JPEG', quality=95)
    print(f"✅ Generated 16:9 Thumbnail: {out_path}")

def generate_vertical_cover(hero_img_path, headline_en, headline_hi, out_path):
    w, h = 1080, 1920
    img = Image.new('RGB', (w, h), (10, 15, 20))

    if hero_img_path and Path(hero_img_path).exists():
        try:
            hero = Image.open(hero_img_path).convert('RGB')
            hero_ratio = hero.width / hero.height
            target_ratio = w / h
            if hero_ratio > target_ratio:
                new_h = h
                new_w = int(h * hero_ratio)
            else:
                new_w = w
                new_h = int(w / hero_ratio)
            hero = hero.resize((new_w, new_h), Image.Resampling.LANCZOS)
            crop_x = (new_w - w) // 2
            crop_y = (new_h - h) // 2
            hero = hero.crop((crop_x, crop_y, crop_x + w, crop_y + h))
            img.paste(hero, (0, 0))
        except Exception as e:
            print(f"Warning: could not process hero image: {e}")

    # Gradient Overlays respecting Mobile Safe Zones (Top 0-230, Bottom 1497-1920)
    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw_ov = ImageDraw.Draw(overlay)
    for y in range(h):
        if y < 320:
            alpha = int(220 * (1 - y / 320))
            draw_ov.line([(0, y), (w, y)], fill=(8, 12, 18, alpha))
        elif y > 1000:
            alpha = int(245 * ((y - 1000) / (h - 1000)))
            draw_ov.line([(0, y), (w, y)], fill=(6, 9, 14, alpha))

    img = Image.alpha_composite(img.convert('RGBA'), overlay).convert('RGB')
    draw = ImageDraw.Draw(img)

    font_bold = Path("brand/fonts/Outfit-Bold.ttf")
    f_badge = get_font(font_bold, 28)
    f_title = get_font(font_bold, 76)
    f_sub = get_font(font_bold, 48)

    # Top-Left Logo Bug inside Safe Zone
    draw.rounded_rectangle([80, 80, 380, 140], radius=12, fill=(10, 15, 22), outline=(251, 191, 36), width=2)
    draw.text((105, 94), "BENAQAAB INDIA", fill=(255, 255, 255), font=f_badge)

    # Center-Bottom Headline in Safe Workspace (Y: 240 to 1480)
    draw.text((80, 1140), headline_en.upper(), fill=(255, 255, 255), font=f_title)
    if headline_hi:
        draw.text((80, 1240), headline_hi, fill=(251, 191, 36), font=f_title)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    img.save(out_path, 'JPEG', quality=95)
    print(f"✅ Generated 9:16 Vertical Cover: {out_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate Benaqaab India Thumbnail Pack")
    parser.add_argument("--hero", required=True, help="Path to hero background image")
    parser.add_argument("--en", required=True, help="English Headline (3-4 words)")
    parser.add_argument("--hi", default="", help="Hindi Subtitle or callout")
    parser.add_argument("--outdir", default=".", help="Output directory")
    parser.add_argument("--date", default="OCT 2026", help="Date badge string")
    args = parser.parse_args()

    out_dir = Path(args.outdir)
    generate_landscape_thumbnail(args.hero, args.en, args.hi, out_dir / "thumbnail_1280x720.jpg", args.date)
    generate_vertical_cover(args.hero, args.en, args.hi, out_dir / "cover_vertical_1080x1920.jpg")

if __name__ == "__main__":
    main()
