import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR = Path(__file__).parent
THUMB_PATH = DIR / "thumbnail_master.jpg"

w, h = 1920, 1080
img = Image.new("RGB", (w, h), "#06090F")
draw = ImageDraw.Draw(img)

# Fonts
font_anton = Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/fonts/Anton.ttf")
font_inter = Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/fonts/Inter.ttf")
font_mono = Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/fonts/JetBrainsMono.ttf")
font_dev = Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/fonts/NotoSansDevanagari.ttf")

def get_f(p, sz):
    try:
        return ImageFont.truetype(str(p), sz)
    except Exception:
        return ImageFont.load_default()

f_giant = get_f(font_anton, 160)
f_huge = get_f(font_anton, 110)
f_sub = get_f(font_anton, 64)
f_badge = get_f(font_mono, 34)
f_mono_sub = get_f(font_mono, 26)

# Background Composite: Split Atmosphere
# Left 50%: Glowing Emerald Green (The 7.8% Headline Bull)
# Right 50%: Ominous Deep Crimson (The Household Savings & Debt Reality)
for x in range(0, w // 2):
    intensity = (1.0 - abs(x - 480) / 600) * 0.45
    cr = int(6 + 8 * intensity)
    cg = int(9 + 130 * intensity)
    cb = int(15 + 60 * intensity)
    draw.line([(x, 0), (x, h)], fill=(cr, cg, cb), width=1)

for x in range(w // 2, w):
    intensity = (1.0 - abs(x - 1440) / 600) * 0.48
    cr = int(6 + 155 * intensity)
    cg = int(9 + 10 * intensity)
    cb = int(15 + 20 * intensity)
    draw.line([(x, 0), (x, h)], fill=(cr, cg, cb), width=1)

# Subtle perspective grid
for y in range(0, h, 60):
    draw.line([(0, y), (w, y)], fill=(20, 30, 45, 60), width=1)
for x in range(0, w, 100):
    draw.line([(x, 0), (x, h)], fill=(20, 30, 45, 60), width=1)

# Diagonal neon division line
draw.line([(w // 2 - 25, 0), (w // 2 + 25, h)], fill="#FBBF24", width=6)
draw.line([(w // 2 - 25, 0), (w // 2 + 25, h)], fill="#FFFFFF", width=2)

# Left Side Graphics: Green Bull Trend
trend_pts = [(80, 750), (240, 680), (450, 520), (640, 470), (840, 220)]
for i in range(len(trend_pts)-1):
    draw.line([trend_pts[i], trend_pts[i+1]], fill="#34D399", width=12)
for px, py in trend_pts:
    draw.ellipse([(px-14, py-14), (px+14, py+14)], fill="#FFFFFF", outline="#10B981", width=5)

draw.rounded_rectangle([(80, 150), (520, 230)], radius=14, fill="#064E3B", outline="#34D399", width=3)
draw.text((300, 190), "HEADLINE GDP", fill="#A7F3D0", font=f_badge, anchor="mm")

draw.text((80, 260), "7.8%", fill="#34D399", font=f_giant)
draw.text((80, 470), "FASTEST IN WORLD?", fill="#FFFFFF", font=f_sub)
draw.text((80, 560), "$3.94T (RS. 330 LAKH CR)", fill="#FBBF24", font=f_mono_sub)

# Right Side Graphics: Red Savings & Debt Spike
draw.rounded_rectangle([(w - 560, 150), (w - 80, 230)], radius=14, fill="#450A0A", outline="#EF4444", width=3)
draw.text((w - 320, 190), "GROUND REALITY", fill="#FECACA", font=f_badge, anchor="mm")

draw.text((w - 840, 260), "5.3%", fill="#F43F5E", font=f_giant)
draw.text((w - 840, 470), "SAVINGS AT 50-YR LOW!", fill="#FFFFFF", font=f_sub)
draw.text((w - 840, 560), "PER-CAPITA RANK: #136 ($2,730)", fill="#F87171", font=f_mono_sub)

# Bottom Massive Yellow Headline Banner
banner_y = h - 260
draw.rectangle([(0, banner_y), (w, h)], fill="#0B0F19", outline="#FBBF24", width=4)
draw.rectangle([(0, banner_y), (w, banner_y + 14)], fill="#FACC15")

draw.text((w // 2, banner_y + 80), "7.8% GDP KA ASLI SACH BEBAK", fill="#FACC15", font=f_huge, anchor="mm")
draw.text((w // 2, banner_y + 165), "OFFICIAL MoSPI & RBI DATA EXPOSED · DHRUV RATHEE STYLE FORENSIC INVESTIGATION", fill="#FFFFFF", font=f_mono_sub, anchor="mm")

# Top Left Channel Logo Brand Pill
logo_pill_x, logo_pill_y = 60, 45
draw.rounded_rectangle([(logo_pill_x, logo_pill_y), (logo_pill_x + 380, logo_pill_y + 68)], radius=34, fill="#0F172A", outline="#FBBF24", width=2)
# Load logo if available
logo_path = Path("c:/Users/dell/Desktop/my ai bot skills ok/brand/logo.png")
if logo_path.exists():
    try:
        limg = Image.open(logo_path).resize((46, 46)).convert("RGBA")
        img.paste(limg, (logo_pill_x + 12, logo_pill_y + 11), limg)
    except Exception:
        pass
draw.text((logo_pill_x + 220, logo_pill_y + 34), "BENAQAAB INDIA", fill="#FFFFFF", font=get_f(font_anton, 32), anchor="mm")

# Top Right Verified Evidence Badge
draw.rounded_rectangle([(w - 480, 45), (w - 60, 113)], radius=34, fill="#1E1B4B", outline="#818CF8", width=2)
draw.text((w - 270, 79), "[VERIFIED EVIDENCE PROOF]", fill="#C7D2FE", font=get_f(font_mono, 24), anchor="mm")

img.save(THUMB_PATH, quality=95)
print(f"✅ Generated Master 4K Thumbnail: {THUMB_PATH}")
