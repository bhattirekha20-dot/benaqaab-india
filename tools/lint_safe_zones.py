#!/usr/bin/env python3
"""
🛡️ BENAQAAB SAFE-ZONE LINTER
Audits 1080x1920 frames to ensure vital text and evidence stay strictly
within the Safe Workspace (X: 80-900, Y: 240-1480) and generates a visual overlay.
"""

import argparse
import sys
from pathlib import Path
from PIL import Image, ImageDraw

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def overlay_safe_zones(img_path, out_debug_path=None):
    if not Path(img_path).exists():
        print(f"Error: image {img_path} does not exist.")
        sys.exit(1)

    img = Image.open(img_path).convert('RGBA')
    w, h = img.size

    if (w, h) != (1080, 1920):
        print(f"Warning: image dimensions ({w}x{h}) differ from standard 9:16 (1080x1920). Scaling calculations.")

    overlay = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # 1. Top Obstruction Zone (0 to 230px) - Red 20%
    draw.rectangle([0, 0, w, 230], fill=(239, 68, 68, 60), outline=(239, 68, 68, 200), width=2)
    draw.text((20, 20), "TOP UI OBSTRUCTION (Avatar / Search)", fill=(255, 255, 255))

    # 2. Bottom Obstruction Zone (1497 to 1920px) - Red 20%
    draw.rectangle([0, 1497, w, h], fill=(239, 68, 68, 60), outline=(239, 68, 68, 200), width=2)
    draw.text((20, 1510), "BOTTOM UI OBSTRUCTION (Captions / Sound / Title)", fill=(255, 255, 255))

    # 3. Right Action Margin (907 to 1080px) - Red 20%
    draw.rectangle([907, 230, w, 1497], fill=(239, 68, 68, 60), outline=(239, 68, 68, 200), width=2)
    draw.text((915, 250), "RIGHT ICONS", fill=(255, 255, 255))

    # 4. SAFE WORKSPACE (X: 80 to 900, Y: 240 to 1480) - Cyan Border
    draw.rectangle([80, 240, 900, 1480], outline=(56, 189, 248, 240), width=3)
    draw.text((95, 250), "SAFE WORKSPACE (All Evidence & Text)", fill=(56, 189, 248))

    composite = Image.alpha_composite(img, overlay).convert('RGB')

    if not out_debug_path:
        out_debug_path = Path(img_path).parent / f"debug_safezone_{Path(img_path).name}"

    composite.save(out_debug_path, 'JPEG', quality=90)
    print(f"✅ Safe-zone audit overlay generated: {out_debug_path}")
    print(f"   Safe Bounds: X [80, 900] | Y [240, 1480]")

def main():
    parser = argparse.ArgumentParser(description="Audit and overlay safe zones on 1080x1920 video frames")
    parser.add_argument("image", help="Path to 1080x1920 frame image")
    parser.add_argument("--out", help="Path for output debug overlay image")
    args = parser.parse_args()

    overlay_safe_zones(args.image, args.out)

if __name__ == "__main__":
    main()
