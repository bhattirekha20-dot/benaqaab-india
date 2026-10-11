import os
import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets" / "visuals"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)
FONTS_DIR = Path(r"c:\Users\dell\Desktop\my ai bot skills ok\brand\fonts")

FONT_INTER = str(FONTS_DIR / "Inter.ttf") if (FONTS_DIR / "Inter.ttf").exists() else None
FONT_MONO = str(FONTS_DIR / "JetBrainsMono.ttf") if (FONTS_DIR / "JetBrainsMono.ttf").exists() else None
FONT_ANTON = str(FONTS_DIR / "Anton.ttf") if (FONTS_DIR / "Anton.ttf").exists() else None
FONT_SPACE = str(FONTS_DIR / "SpaceGrotesk.ttf") if (FONTS_DIR / "SpaceGrotesk.ttf").exists() else None

def get_font(path, size):
    try:
        if path and os.path.exists(path):
            return ImageFont.truetype(path, size)
    except Exception:
        pass
    return ImageFont.load_default()

W, H = 1080, 1920

PROTECTED_AI_BEATS = {
    "beat_01.jpg", "beat_03.jpg", "beat_04.jpg", "beat_06.jpg", "beat_08.jpg",
    "beat_10.jpg", "beat_11.jpg", "beat_12.jpg", "beat_14.jpg", "beat_18.jpg",
    "beat_21.jpg", "beat_24.jpg", "beat_25.jpg"
}

def safe_save(img, filename):
    out_path = ASSETS_DIR / filename
    if filename in PROTECTED_AI_BEATS and out_path.exists():
        return
    img.save(out_path, quality=95)

def create_base(bg_color1, bg_color2):
    img = Image.new("RGB", (W, H), bg_color1)
    draw = ImageDraw.Draw(img)
    # Smooth vertical chromatic gradient
    r1, g1, b1 = bg_color1
    r2, g2, b2 = bg_color2
    for y in range(0, H, 4):
        t = y / H
        r = int(r1 + (r2 - r1) * t)
        g = int(g1 + (g2 - g1) * t)
        b = int(b1 + (b2 - b1) * t)
        draw.rectangle([0, y, W, y+4], fill=(r, g, b))
    return img

def add_scanlines(img, opacity=14):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for y in range(0, H, 6):
        d.line([(0, y), (W, y)], fill=(0, 0, 0, opacity))
    img.paste(overlay, (0, 0), overlay)
    return img

def add_glow_orb(img, cx, cy, radius, color_rgb, intensity=0.45):
    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(overlay)
    for r in range(radius, 0, -15):
        alpha = int((1.0 - (r / radius)) * intensity * 255)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(color_rgb[0], color_rgb[1], color_rgb[2], alpha))
    overlay = overlay.filter(ImageFilter.GaussianBlur(16))
    img.paste(overlay, (0, 0), overlay)
    return img

def draw_header_tag(draw, text, y=240, accent_color=(251, 191, 36)):
    font = get_font(FONT_MONO, 28)
    draw.rounded_rectangle([60, y, W - 60, y + 54], radius=12, fill=(15, 23, 42), outline=accent_color, width=2)
    draw.text((80, y + 12), text, font=font, fill=accent_color)

def draw_main_headline(draw, text_lines, y=340, font_size=64, text_color=(248, 250, 252)):
    font = get_font(FONT_ANTON, font_size)
    curr_y = y
    for line in text_lines:
        bbox = font.getbbox(line)
        w = bbox[2] - bbox[0]
        x = (W - w) // 2
        # drop shadow
        draw.text((x + 3, curr_y + 3), line, font=font, fill=(0, 0, 0))
        draw.text((x, curr_y), line, font=font, fill=text_color)
        curr_y += font_size + 14
    return curr_y

# COLLISION-PROOF INFORMATION BOX (Prevents all text overlapping!)
def draw_info_box(draw, x, y, w, h, title, items, border_color=(56, 189, 248)):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=20, fill=(11, 16, 27), outline=border_color, width=2)
    
    # Title badge
    f_title = get_font(FONT_MONO, 26)
    draw.text((x + 32, y + 22), title, font=f_title, fill=border_color)
    draw.line([(x + 32, y + 62), (x + w - 32, y + 62)], fill=(255, 255, 255, 30), width=1)
    
    curr_y = y + 74
    num_items = len(items)
    row_h = (h - 90) / max(num_items, 1)
    
    for k, v in items:
        f_k = get_font(FONT_INTER, 24)
        f_v = get_font(FONT_MONO, 24)
        
        k_bbox = f_k.getbbox(k)
        v_bbox = f_v.getbbox(v)
        kw = k_bbox[2] - k_bbox[0]
        vw = v_bbox[2] - v_bbox[0]
        
        # Safe horizontal check
        if kw + vw + 36 <= (w - 64):
            # Single line layout: Left label, Right value
            draw.text((x + 32, curr_y + (row_h - 28) // 2), k, font=f_k, fill=(148, 163, 184))
            draw.text((x + w - 32 - vw, curr_y + (row_h - 28) // 2), v, font=f_v, fill=(248, 250, 252))
        else:
            # 2-line stacked layout: Label above, Value below! Zero collision!
            draw.text((x + 32, curr_y + 4), k.upper(), font=get_font(FONT_MONO, 18), fill=(148, 163, 184))
            draw.text((x + 32, curr_y + 30), v, font=get_font(FONT_MONO, 24), fill=(254, 240, 138))
            
        curr_y += row_h
        draw.line([(x + 32, curr_y), (x + w - 32, curr_y)], fill=(255, 255, 255, 18), width=1)

# HIGH-CONTRAST STATUS BADGE (Dark base, glowing outline, crisp text)
def draw_status_badge(draw, text, y, font_size=46, border_color=(251, 191, 36), text_color=(254, 240, 138), sub_text=None):
    x = 100
    w = W - 200
    h = 136 if sub_text else 100
    draw.rounded_rectangle([x, y, x + w, y + h], radius=18, fill=(15, 23, 42), outline=border_color, width=3)
    
    f_main = get_font(FONT_ANTON, font_size)
    bbox = f_main.getbbox(text)
    tw = bbox[2] - bbox[0]
    tx = (W - tw) // 2
    
    if sub_text:
        draw.text((tx, y + 16), text, font=f_main, fill=text_color)
        f_sub = get_font(FONT_MONO, 24)
        s_bbox = f_sub.getbbox(sub_text)
        sw = s_bbox[2] - s_bbox[0]
        draw.text(((W - sw) // 2, y + 78), sub_text, font=f_sub, fill=(148, 163, 184))
    else:
        th = bbox[3] - bbox[1]
        ty = y + (h - th) // 2 - 4
        draw.text((tx, ty), text, font=f_main, fill=text_color)

print("🎨 Rendering 30 visual beats with ZERO text overlapping & peak detail...")

# BEAT 01: Locked Delhi Metro Gate
b01 = create_base((12, 14, 20), (5, 6, 9))
b01 = add_glow_orb(b01, 540, 750, 420, (239, 68, 68), 0.4)
d = ImageDraw.Draw(b01)
draw_header_tag(d, "🚨 BREAKING REPORT • NEW DELHI 10 OCT 2026", 220, (239, 68, 68))
draw_main_headline(d, ["DELHI METRO", "GATES SHUTTERED!"], 310, 78, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1260], radius=24, fill=(15, 20, 32), outline=(239, 68, 68), width=3)
for sy in range(560, 1220, 48):
    d.line([(100, sy), (W-100, sy)], fill=(30, 41, 59), width=3)
# Crime / barricade tape overlay
tape = Image.new("RGBA", (W, 140), (251, 191, 36, 240))
td = ImageDraw.Draw(tape)
f_tape = get_font(FONT_ANTON, 56)
for tx in range(-200, W+400, 380):
    td.text((tx, 35), "⚠ STATION CLOSED • ENTRY RESTRICTED ⚠", font=f_tape, fill=(0, 0, 0))
tape = tape.rotate(-8, expand=True)
b01.paste(tape, (-60, 840), tape)
draw_status_badge(d, "45 STATIONS LOCKED DOWN", 1290, 46, (239, 68, 68), (255, 255, 255), "DMRC OFFICIAL CITIZEN ADVISORY")
b01.save(ASSETS_DIR / "beat_01.jpg", quality=95)

# BEAT 02: 45 Metro Stations Network Map
b02 = create_base((8, 12, 22), (4, 6, 12))
b02 = add_glow_orb(b02, 540, 800, 450, (239, 68, 68), 0.5)
d = ImageDraw.Draw(b02)
draw_header_tag(d, "🔴 DMRC TRANSIT LOCKDOWN ALERT", 220, (239, 68, 68))
draw_main_headline(d, ["45 STATIONS SEALED", "YELLOW · BLUE · VIOLET"], 310, 68, (251, 191, 36))
draw_info_box(d, 80, 520, W-160, 680, "METRO NETWORK IMPACT LEDGER", [
    ("Total Stations Closed", "45 STATIONS"),
    ("Closure Window", "9:00 PM - 6:00 PM"),
    ("Interchange Restricted", "NEW DELHI / CENTRAL"),
    ("Passenger Disruption", "EST. 1.8M COMMUTERS"),
    ("Order Authority", "DELHI POLICE DIRECTIVE")
], (239, 68, 68))
draw_status_badge(d, "DMRC ADVISORY: GATES LOCKED", 1260, 46, (239, 68, 68), (255, 255, 255), "PASSENGER ACCESS SUSPENDED")
b02.save(ASSETS_DIR / "beat_02.jpg", quality=95)

# BEAT 03: 25,000 Police Deployment
b03 = create_base((10, 14, 20), (5, 7, 10))
b03 = add_glow_orb(b03, 540, 720, 400, (56, 189, 248), 0.4)
d = ImageDraw.Draw(b03)
draw_header_tag(d, "🛡️ SECURITY FORCES DEPLOYMENT", 220, (56, 189, 248))
draw_main_headline(d, ["25,000 POLICE & CAPF", "ON THE STREETS!"], 310, 72, (255, 255, 255))
draw_info_box(d, 80, 520, W-160, 660, "SECURITY MOBILIZATION MATRIX", [
    ("Delhi Police Strength", "18,000 BOOTS"),
    ("Paramilitary (RAF/CRPF)", "7,000 TROOPS"),
    ("Border Checkpoints", "SINGHU · TIKRI · GHAZIPUR"),
    ("Prohibitory Order", "SECTION 163 BNSS"),
    ("Water Cannons Deployed", "24 MOBILE UNITS")
], (56, 189, 248))
draw_status_badge(d, "MULTI-TIER STEEL BARRICADES", 1240, 48, (251, 191, 36), (254, 240, 138), "JANTAR MANTAR PERIMETER SEALED")
b03.save(ASSETS_DIR / "beat_03.jpg", quality=95)

# BEAT 04: In-Flight Boarding Arrest
b04 = create_base((14, 10, 20), (7, 4, 10))
b04 = add_glow_orb(b04, 540, 780, 420, (239, 68, 68), 0.45)
d = ImageDraw.Draw(b04)
draw_header_tag(d, "✈️ AIRPORT INTERCEPTION • IGI AIRPORT T3", 220, (239, 68, 68))
draw_main_headline(d, ["ARREST INSIDE FLIGHT!", "POLICE BOARD PASSENGER PLANE"], 310, 62, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1260], radius=24, fill=(12, 17, 28), outline=(239, 68, 68), width=3)
d.text((120, 570), "FLIGHT TOUCHDOWN INTERCEPTION", font=get_font(FONT_ANTON, 52), fill=(239, 68, 68))
# Target locked graphic
d.rectangle([140, 680, W-140, 1080], fill=(20, 28, 44), outline=(56, 189, 248), width=2)
d.line([(540, 700), (540, 1060)], fill=(239, 68, 68), width=2)
d.line([(160, 880), (W-160, 880)], fill=(239, 68, 68), width=2)
d.ellipse([460, 800, 620, 960], outline=(239, 68, 68), width=4)
d.text((320, 990), "TARGET: ABHIJEET DIPKE", font=get_font(FONT_MONO, 32), fill=(251, 191, 36))
d.text((120, 1140), "Police boarded immediately after aircraft reached taxiway.", font=get_font(FONT_INTER, 30), fill=(203, 213, 225))
draw_status_badge(d, "INTERCEPTED ON RUNWAY", 1290, 46, (239, 68, 68), (255, 255, 255), "DETAINED BEFORE REACHING TERMINAL")
b04.save(ASSETS_DIR / "beat_04.jpg", quality=95)

# BEAT 05: Dark Silhouette & The CJP Phenomenon
b05 = create_base((7, 9, 14), (3, 4, 7))
b05 = add_glow_orb(b05, 540, 800, 500, (251, 191, 36), 0.35)
d = ImageDraw.Draw(b05)
draw_header_tag(d, "🕵️ INVESTIGATIVE DOSSIER • WHO ARE THEY?", 220, (251, 191, 36))
draw_main_headline(d, ["BEHIND THE PANIC:", "WHO IS CJP?"], 310, 78, (255, 255, 255))
d.rounded_rectangle([100, 520, W-100, 1260], radius=24, fill=(15, 20, 32), outline=(251, 191, 36), width=2)
d.ellipse([420, 660, 660, 900], fill=(30, 41, 59), outline=(251, 191, 36), width=3)
d.text((450, 740), "🪳", font=get_font(FONT_INTER, 100), fill=(251, 191, 36))
d.text((220, 960), "COCKROACH JANTA PARTY", font=get_font(FONT_ANTON, 56), fill=(251, 191, 36))
d.text((320, 1040), "GEN Z YOUTH MOVEMENT", font=get_font(FONT_MONO, 32), fill=(148, 163, 184))
d.text((160, 1140), "Why is the entire capital in lockdown mode?", font=get_font(FONT_INTER, 34), fill=(248, 250, 252))
draw_status_badge(d, "YOUTH DEMOCRACY MOVEMENT", 1290, 46, (251, 191, 36), (254, 240, 138))
b05.save(ASSETS_DIR / "beat_05.jpg", quality=95)

# BEAT 06: Official CJP Emblem
b06 = create_base((12, 10, 18), (5, 4, 8))
b06 = add_glow_orb(b06, 540, 750, 450, (251, 191, 36), 0.5)
d = ImageDraw.Draw(b06)
draw_header_tag(d, "🪳 POLITICAL PROFILE • MOVEMENT ORIGIN", 220, (251, 191, 36))
draw_main_headline(d, ["COCKROACH JANTA PARTY", "FOUNDED 16 MAY 2026"], 310, 66, (251, 191, 36))
draw_info_box(d, 80, 520, W-160, 680, "CJP IDENTITY SHEET", [
    ("Founder", "ABHIJEET DIPKE"),
    ("Demographics", "GEN Z / STUDENTS / ASPIRANTS"),
    ("Core Issues", "UNEMPLOYMENT & VOTER RIGHTS"),
    ("Network Channels", "VIRAL TELEGRAM / REELS"),
    ("Official Symbol", "RESILIENT COCKROACH & TORCH")
], (251, 191, 36))
draw_status_badge(d, "\"WE CANNOT BE CRUSHED\"", 1260, 52, (251, 191, 36), (254, 240, 138))
b06.save(ASSETS_DIR / "beat_06.jpg", quality=95)

# BEAT 07: Name Origin Question
b07 = create_base((10, 12, 18), (4, 5, 8))
b07 = add_glow_orb(b07, 540, 750, 420, (56, 189, 248), 0.45)
d = ImageDraw.Draw(b07)
draw_header_tag(d, "❓ THE ORIGIN STORY • WHY THIS NAME?", 220, (56, 189, 248))
draw_main_headline(d, ["WHY CALL YOURSELF", "'COCKROACH'?!"], 310, 74, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(15, 23, 42), outline=(56, 189, 248), width=2)
d.text((120, 580), "FROM AN INSULT TO A WEAPON", font=get_font(FONT_MONO, 32), fill=(56, 189, 248))
d.text((120, 680), "When an apex judge called", font=get_font(FONT_INTER, 42), fill=(203, 213, 225))
d.text((120, 740), "jobless youth 'cockroaches'...", font=get_font(FONT_INTER, 42), fill=(251, 191, 36))
d.text((120, 840), "Instead of feeling defeated,", font=get_font(FONT_INTER, 42), fill=(203, 213, 225))
d.text((120, 900), "they adopted it with pride:", font=get_font(FONT_INTER, 42), fill=(56, 189, 248))
d.rectangle([120, 1000, W-120, 1160], fill=(24, 34, 56), outline=(251, 191, 36), width=2)
d.text((180, 1045), "\"SURVIVES ANY BLAST\"", font=get_font(FONT_ANTON, 60), fill=(251, 191, 36))
draw_status_badge(d, "TURNING THE SLUR INTO POWER", 1280, 46, (56, 189, 248), (255, 255, 255))
b07.save(ASSETS_DIR / "beat_07.jpg", quality=95)

# BEAT 08: Supreme Court Judge Remark Archive
b08 = create_base((14, 12, 10), (6, 5, 4))
b08 = add_glow_orb(b08, 540, 750, 420, (251, 191, 36), 0.4)
d = ImageDraw.Draw(b08)
draw_header_tag(d, "🏛️ JUDICIAL PROCEEDINGS TRANSCRIPT", 220, (251, 191, 36))
draw_main_headline(d, ["THE CONTROVERSIAL", "REMARK IN COURT"], 310, 72, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(18, 16, 22), outline=(251, 191, 36), width=2)
d.text((120, 580), "TRANSCRIPT ARCHIVE EXCERPT:", font=get_font(FONT_MONO, 30), fill=(251, 191, 36))
d.text((120, 680), "\"...these unemployed agitators", font=get_font(FONT_INTER, 40), fill=(248, 250, 252))
d.text((120, 740), "acting like cockroaches everywhere...\"", font=get_font(FONT_INTER, 40), fill=(239, 68, 68))
d.rectangle([100, 860, W-100, 1160], fill=(28, 24, 32), outline=(239, 68, 68), width=2)
d.text((140, 900), "IMPACT ON MILLIONS OF YOUTH:", font=get_font(FONT_MONO, 28), fill=(239, 68, 68))
d.text((140, 960), "Triggered a nationwide student backlash", font=get_font(FONT_INTER, 34), fill=(203, 213, 225))
d.text((140, 1020), "across colleges and coaching hubs.", font=get_font(FONT_INTER, 34), fill=(251, 191, 36))
draw_status_badge(d, "SPARKED NATIONWIDE OUTRAGE", 1280, 46, (239, 68, 68), (255, 255, 255))
b08.save(ASSETS_DIR / "beat_08.jpg", quality=95)

# BEAT 09: Yellow Highlighter Sweep on Legal Quote
b09 = create_base((12, 12, 16), (5, 5, 7))
b09 = add_glow_orb(b09, 540, 800, 420, (250, 204, 21), 0.5)
d = ImageDraw.Draw(b09)
draw_header_tag(d, "🖋️ FORENSIC DOCUMENT EVIDENCE", 220, (250, 204, 21))
draw_main_headline(d, ["FROM SLUR TO", "REVOLUTION!"], 310, 78, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(245, 245, 240), outline=(200, 200, 200), width=3)
d.text((120, 570), "COURT TRANSCRIPT RECORD", font=get_font(FONT_MONO, 32), fill=(70, 70, 70))
d.line([(120, 620), (W-120, 620)], fill=(180, 180, 180), width=2)
# Clean text to be highlighted dynamically in canvas
d.text((130, 745), "\"REFERRED AS COCKROACHES\"", font=get_font(FONT_ANTON, 56), fill=(30, 41, 59))
d.text((130, 920), "Youth Response: We exist, we vote,", font=get_font(FONT_INTER, 36), fill=(30, 41, 59))
d.text((130, 980), "and we will hold institutions accountable.", font=get_font(FONT_INTER, 36), fill=(30, 41, 59))
draw_status_badge(d, "ADOPTED BY 1.2M STUDENTS", 1280, 48, (251, 191, 36), (254, 240, 138))
b09.save(ASSETS_DIR / "beat_09.jpg", quality=95)

# BEAT 10: Youth Marching with Placards
b10 = create_base((10, 15, 22), (4, 7, 12))
b10 = add_glow_orb(b10, 540, 750, 440, (56, 189, 248), 0.4)
d = ImageDraw.Draw(b10)
draw_header_tag(d, "📢 NATIONWIDE STUDENT MOBILIZATION", 220, (56, 189, 248))
draw_main_headline(d, ["YOUTH TAKES TO", "THE STREETS!"], 310, 76, (255, 255, 255))
draw_info_box(d, 80, 520, W-160, 660, "PROTEST SPREAD ACROSS INDIA", [
    ("Delhi Central Hub", "JANTAR MANTAR"),
    ("University Support", "DU · JNU · JAMIA · IIT"),
    ("State Chapters", "BIHAR · UP · MAHARASHTRA"),
    ("Aspirants Joined", "NEET / UPSC CANDIDATES"),
    ("Core Strategy", "PEACEFUL CITIZEN VIGIL")
], (56, 189, 248))
draw_status_badge(d, "\"DEMOCRACY IS OURS\"", 1240, 52, (56, 189, 248), (255, 255, 255))
b10.save(ASSETS_DIR / "beat_10.jpg", quality=95)

# BEAT 11: Jantar Mantar Iconic Landmark
b11 = create_base((16, 10, 10), (7, 4, 4))
b11 = add_glow_orb(b11, 540, 750, 420, (239, 68, 68), 0.45)
d = ImageDraw.Draw(b11)
draw_header_tag(d, "📍 PROTEST VENUE • JANTAR MANTAR", 220, (239, 68, 68))
draw_main_headline(d, ["THE BATTLEGROUND:", "JANTAR MANTAR"], 310, 72, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(20, 16, 18), outline=(239, 68, 68), width=2)
d.text((120, 580), "HISTORIC PROTEST SITE FORTIFIED", font=get_font(FONT_MONO, 32), fill=(239, 68, 68))
d.text((120, 680), "• Multi-layer barricades installed", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
d.text((120, 760), "• Water cannons positioned at gate", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
d.text((120, 840), "• Drones deployed overhead", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
d.text((120, 920), "• Prohibitory Section 163 BNSS", font=get_font(FONT_INTER, 38), fill=(251, 191, 36))
draw_status_badge(d, "POLICE DENIED ASSEMBLY PERMIT", 1280, 46, (239, 68, 68), (255, 255, 255))
b11.save(ASSETS_DIR / "beat_11.jpg", quality=95)

# BEAT 12: Banner CEC Resign Now
b12 = create_base((18, 8, 12), (8, 3, 5))
b12 = add_glow_orb(b12, 540, 750, 450, (239, 68, 68), 0.5)
d = ImageDraw.Draw(b12)
draw_header_tag(d, "🔥 THE CORE DEMAND OF CJP", 220, (239, 68, 68))
draw_main_headline(d, ["\"CEC RESIGN NOW!\"", "UNCOMPROMISING STANCE"], 310, 68, (251, 191, 36))
d.rounded_rectangle([60, 540, W-60, 1180], radius=24, fill=(239, 68, 68), outline=(255, 255, 255), width=4)
d.text((160, 640), "DEMAND NUMBER ONE:", font=get_font(FONT_MONO, 36), fill=(255, 255, 255))
d.text((100, 740), "CHIEF ELECTION COMMISSIONER", font=get_font(FONT_ANTON, 62), fill=(255, 255, 255))
d.text((200, 840), "MUST RESIGN IMMEDIATELY!", font=get_font(FONT_ANTON, 56), fill=(254, 240, 138))
d.text((140, 980), "Accountability for Voter List Deletions", font=get_font(FONT_INTER, 38), fill=(255, 255, 255))
draw_status_badge(d, "CJP ULTRA-MANDATE: STEP DOWN", 1260, 48, (251, 191, 36), (254, 240, 138))
b12.save(ASSETS_DIR / "beat_12.jpg", quality=95)

# BEAT 13: Nirvachan Sadan (ECI Headquarters)
b13 = create_base((10, 14, 20), (4, 6, 9))
b13 = add_glow_orb(b13, 540, 750, 420, (56, 189, 248), 0.4)
d = ImageDraw.Draw(b13)
draw_header_tag(d, "🏛️ ELECTION COMMISSION OF INDIA", 220, (56, 189, 248))
draw_main_headline(d, ["NIRVACHAN SADAN", "UNDER THE SPOTLIGHT"], 310, 68, (255, 255, 255))
draw_info_box(d, 80, 520, W-160, 680, "INSTITUTIONAL DOSSIER", [
    ("Institution", "ELECTION COMMISSION (ECI)"),
    ("Headquarters", "ASHOKA ROAD, NEW DELHI"),
    ("Chief Commissioner", "GYANESH KUMAR"),
    ("Constitutional Mandate", "ARTICLE 324"),
    ("Current Focus", "SPECIAL INTENSIVE REVISION")
], (56, 189, 248))
draw_status_badge(d, "ALLEGED MASS VOTER PURGE", 1260, 48, (56, 189, 248), (255, 255, 255))
b13.save(ASSETS_DIR / "beat_13.jpg", quality=95)

# BEAT 14: CEC Gyanesh Kumar File Card
b14 = create_base((12, 12, 18), (5, 5, 8))
b14 = add_glow_orb(b14, 540, 750, 440, (251, 191, 36), 0.45)
d = ImageDraw.Draw(b14)
draw_header_tag(d, "🎯 HERO INVESTIGATION TARGET", 220, (251, 191, 36))
draw_main_headline(d, ["CEC GYANESH KUMAR", "FACING RESIGNATION CALLS"], 310, 64, (251, 191, 36))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(15, 20, 32), outline=(251, 191, 36), width=2)
d.ellipse([400, 620, 680, 900], fill=(24, 32, 48), outline=(56, 189, 248), width=4)
d.text((430, 720), "CEC", font=get_font(FONT_ANTON, 72), fill=(255, 255, 255))
d.text((260, 960), "CHIEF ELECTION COMMISSIONER", font=get_font(FONT_MONO, 28), fill=(148, 163, 184))
d.text((140, 1050), "Under fire over 2026 Special Intensive", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
d.text((140, 1110), "Revision (SIR) electoral roll process.", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
draw_status_badge(d, "PRESSURE BUILDS ON APEX BODY", 1280, 46, (251, 191, 36), (254, 240, 138))
b14.save(ASSETS_DIR / "beat_14.jpg", quality=95)

# BEAT 15: Scanned SIR Gazette Document
b15 = create_base((14, 14, 18), (6, 6, 8))
b15 = add_glow_orb(b15, 540, 750, 420, (250, 204, 21), 0.4)
d = ImageDraw.Draw(b15)
draw_header_tag(d, "📜 OFFICIAL GAZETTE NOTIFICATION", 220, (250, 204, 21))
draw_main_headline(d, ["SPECIAL INTENSIVE", "REVISION (SIR) 2026"], 310, 72, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(248, 248, 242), outline=(210, 210, 210), width=3)
d.text((120, 560), "THE GAZETTE OF INDIA • ECI NOTIFICATION", font=get_font(FONT_MONO, 28), fill=(80, 80, 80))
d.line([(120, 610), (W-120, 610)], fill=(180, 180, 180), width=2)
d.text((120, 660), "SUBJECT: SPECIAL INTENSIVE REVISION OF ROLLS", font=get_font(FONT_ANTON, 38), fill=(20, 20, 20))
d.text((120, 740), "Algorithmic audit initiated across all states.", font=get_font(FONT_INTER, 34), fill=(60, 60, 60))
d.rectangle([110, 820, W-110, 940], fill=(254, 240, 138))
d.text((130, 850), "FORM 7 DELETION PROCEDURE INVOKED", font=get_font(FONT_ANTON, 48), fill=(0, 0, 0))
d.text((120, 1000), "Mass removal of 'unverified' entries triggered", font=get_font(FONT_INTER, 34), fill=(60, 60, 60))
d.text((120, 1060), "concerns over youth voter disenfranchisement.", font=get_font(FONT_INTER, 34), fill=(60, 60, 60))
draw_status_badge(d, "PRIMARY SOURCE GAZETTE RECORD", 1280, 46, (250, 204, 21), (254, 240, 138))
b15.save(ASSETS_DIR / "beat_15.jpg", quality=95)

# BEAT 16: Form 7 Deletion Evidence
b16 = create_base((18, 10, 12), (8, 4, 5))
b16 = add_glow_orb(b16, 540, 750, 440, (239, 68, 68), 0.45)
d = ImageDraw.Draw(b16)
draw_header_tag(d, "🗳️ VOTER ROLL FORENSICS • FORM 7", 220, (239, 68, 68))
draw_main_headline(d, ["HOW VOTERS WERE", "SILENTLY REMOVED!"], 310, 68, (251, 191, 36))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(15, 20, 32), outline=(239, 68, 68), width=2)
d.text((120, 580), "THE DELETION MECHANISM:", font=get_font(FONT_MONO, 32), fill=(239, 68, 68))
d.rectangle([110, 660, W-110, 800], fill=(239, 68, 68, 40), outline=(239, 68, 68), width=2)
d.text((140, 700), "FORM 7 BULK OBJECTIONS", font=get_font(FONT_ANTON, 56), fill=(255, 255, 255))
d.text((120, 860), "1. Automated anomaly detection flagged youth.", font=get_font(FONT_INTER, 36), fill=(203, 213, 225))
d.text((120, 940), "2. Notices sent to outdated postal addresses.", font=get_font(FONT_INTER, 36), fill=(203, 213, 225))
d.text((120, 1020), "3. Summary deletion upon non-response.", font=get_font(FONT_INTER, 36), fill=(239, 68, 68))
draw_status_badge(d, "THOUSANDS OF ENTRIES PURGED", 1280, 46, (239, 68, 68), (255, 255, 255))
b16.save(ASSETS_DIR / "beat_16.jpg", quality=95)

# BEAT 17: Algorithmic Disenfranchisement Board (Clean Counter Frame)
b17 = create_base((12, 10, 16), (5, 4, 7))
b17 = add_glow_orb(b17, 540, 750, 480, (239, 68, 68), 0.5)
d = ImageDraw.Draw(b17)
draw_header_tag(d, "📊 DATA-TO-DOM FACT LEDGER", 220, (239, 68, 68))
draw_main_headline(d, ["NAMES PURGED FROM", "ELECTORAL ROLLS!"], 310, 72, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(12, 17, 28), outline=(239, 68, 68), width=3)
d.text((140, 580), "CUMULATIVE ESTIMATED DELETIONS", font=get_font(FONT_MONO, 30), fill=(148, 163, 184))
d.rectangle([120, 680, W-120, 880], fill=(22, 12, 18), outline=(239, 68, 68), width=3)
d.text((120, 940), "Targeting young first-time voters and", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
d.text((120, 1000), "migrant workers without digital verification.", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
draw_status_badge(d, "STATUS: UNRESOLVED BEFORE SC", 1280, 46, (251, 191, 36), (254, 240, 138))
b17.save(ASSETS_DIR / "beat_17.jpg", quality=95)

# BEAT 18: Abhijeet Dipke Activist Profile
b18 = create_base((10, 14, 20), (4, 6, 9))
b18 = add_glow_orb(b18, 540, 750, 440, (56, 189, 248), 0.45)
d = ImageDraw.Draw(b18)
draw_header_tag(d, "👤 KEY PROTAGONIST PROFILE", 220, (56, 189, 248))
draw_main_headline(d, ["ABHIJEET DIPKE", "CJP CONVENOR & ACTIVIST"], 310, 68, (251, 191, 36))
draw_info_box(d, 80, 520, W-160, 680, "ACTIVIST IDENTITY PROFILE", [
    ("Legal Name", "ABHIJEET DIPKE"),
    ("Leadership Role", "FOUNDER & NATIONAL CONVENOR"),
    ("Political Body", "COCKROACH JANTA PARTY"),
    ("Present Status", "INTERCEPTED AT IGI AIRPORT"),
    ("Legal Notice", "SECTION 163 BNSS")
], (56, 189, 248))
draw_status_badge(d, "DIGITAL CAMPAIGN ARCHITECT", 1260, 48, (56, 189, 248), (255, 255, 255))
b18.save(ASSETS_DIR / "beat_18.jpg", quality=95)

# BEAT 19: Aircraft Tarmac Interception
b19 = create_base((14, 10, 18), (6, 4, 8))
b19 = add_glow_orb(b19, 540, 750, 440, (239, 68, 68), 0.45)
d = ImageDraw.Draw(b19)
draw_header_tag(d, "🛫 DRAMATIC AIRPORT ARREST SCENE", 220, (239, 68, 68))
draw_main_headline(d, ["TAKEN STRAIGHT OFF", "THE RUNWAY!"], 310, 72, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(15, 20, 32), outline=(239, 68, 68), width=2)
d.text((120, 580), "PRE-EMPTIVE POLICE CRACKDOWN", font=get_font(FONT_MONO, 32), fill=(239, 68, 68))
d.text((120, 680), "As flight touched down at Terminal 3,", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
d.text((120, 740), "Delhi Police personnel were waiting", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
d.text((120, 800), "at the aerobridge doors.", font=get_font(FONT_INTER, 38), fill=(251, 191, 36))
d.rectangle([110, 900, W-110, 1140], fill=(24, 16, 22), outline=(239, 68, 68), width=2)
d.text((140, 940), "WITNESS REPORT:", font=get_font(FONT_MONO, 28), fill=(239, 68, 68))
d.text((140, 1000), "\"He was escorted away before", font=get_font(FONT_INTER, 36), fill=(203, 213, 225))
d.text((140, 1060), "stepping into the baggage hall.\"", font=get_font(FONT_INTER, 36), fill=(203, 213, 225))
draw_status_badge(d, "HIGH-LEVEL AIRPORT DETENTION", 1280, 46, (239, 68, 68), (255, 255, 255))
b19.save(ASSETS_DIR / "beat_19.jpg", quality=95)

# BEAT 20: Police Siren Flashing Lights
b20 = create_base((18, 6, 12), (7, 2, 5))
b20 = add_glow_orb(b20, 540, 750, 480, (239, 68, 68), 0.55)
d = ImageDraw.Draw(b20)
draw_header_tag(d, "🚨 EMERGENCY ENFORCEMENT PROTOCOL", 220, (239, 68, 68))
draw_main_headline(d, ["POLICE CONVOY &", "DETAINED IN CUSTODY"], 310, 68, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(18, 14, 20), outline=(239, 68, 68), width=3)
d.text((120, 580), "CAPITAL-WIDE ARREST SWEEP", font=get_font(FONT_MONO, 32), fill=(239, 68, 68))
d.rectangle([110, 680, W-110, 880], fill=(30, 15, 22), outline=(239, 68, 68), width=2)
d.text((160, 730), "3,000+ DETAINED", font=get_font(FONT_ANTON, 90), fill=(239, 68, 68))
d.text((120, 940), "Activists, youth organizers, and student", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
d.text((120, 1000), "leaders placed under preventive custody.", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
draw_status_badge(d, "HELD AT UNDISCLOSED LOCATIONS", 1280, 46, (251, 191, 36), (254, 240, 138))
b20.save(ASSETS_DIR / "beat_20.jpg", quality=95)

# BEAT 21: Deserted Railway Station Platform (FIXED COLLISION & HIGH-CONTRAST BADGE!)
b21 = create_base((12, 14, 18), (5, 6, 8))
b21 = add_glow_orb(b21, 540, 750, 420, (251, 191, 36), 0.4)
d = ImageDraw.Draw(b21)
draw_header_tag(d, "🚆 NORTHERN RAILWAY DISRUPTION", 220, (251, 191, 36))
draw_main_headline(d, ["TRAINS STOPPED OUTSIDE", "NEW DELHI STATION!"], 310, 66, (255, 255, 255))
draw_info_box(d, 80, 520, W-160, 680, "RAILWAY CLOSURE NOTICE", [
    ("Terminus Affected", "NEW DELHI & NIZAMUDDIN"),
    ("Suspension Duration", "10-HOUR WINDOW"),
    ("Trains Cancelled", "MAIL & EXPRESS SERVICES"),
    ("Stated Reason", "PRECAUTIONARY SECURITY"),
    ("Passenger Impact", "STRANDED AT OUTER STATIONS")
], (251, 191, 36))
draw_status_badge(d, "PLATFORMS LEFT EMPTY", 1260, 50, (251, 191, 36), (254, 240, 138), "10-HOUR SUSPENSION ENFORCED")
b21.save(ASSETS_DIR / "beat_21.jpg", quality=95)

# BEAT 22: Smartphone Internet Suspended Screen
b22 = create_base((10, 12, 18), (4, 5, 8))
b22 = add_glow_orb(b22, 540, 750, 440, (239, 68, 68), 0.45)
d = ImageDraw.Draw(b22)
draw_header_tag(d, "📵 TELECOM RESTRICTIONS IMPOSED", 220, (239, 68, 68))
draw_main_headline(d, ["24-HOUR INTERNET SHUTDOWN", "IN CENTRAL DELHI!"], 310, 66, (239, 68, 68))
d.rounded_rectangle([180, 520, W-180, 1240], radius=32, fill=(15, 20, 32), outline=(56, 189, 248), width=3)
d.rectangle([210, 550, W-210, 600], fill=(25, 33, 50))
d.text((440, 560), "12:45 PM", font=get_font(FONT_MONO, 24), fill=(148, 163, 184))
d.text((450, 700), "📵", font=get_font(FONT_INTER, 80), fill=(239, 68, 68))
d.text((280, 840), "NO INTERNET CONNECTION", font=get_font(FONT_ANTON, 48), fill=(239, 68, 68))
d.text((240, 930), "Mobile data suspended as per", font=get_font(FONT_INTER, 34), fill=(203, 213, 225))
d.text((240, 980), "Ministry of Home Affairs order.", font=get_font(FONT_INTER, 34), fill=(203, 213, 225))
draw_status_badge(d, "BNSS SECTION 163 ENFORCED", 1280, 46, (239, 68, 68), (255, 255, 255))
b22.save(ASSETS_DIR / "beat_22.jpg", quality=95)

# BEAT 23: Fortress Delhi Satellite Map
b23 = create_base((10, 14, 20), (4, 6, 9))
b23 = add_glow_orb(b23, 540, 750, 450, (56, 189, 248), 0.45)
d = ImageDraw.Draw(b23)
draw_header_tag(d, "🗺️ GEOGRAPHIC INTELLIGENCE • NCR", 220, (56, 189, 248))
draw_main_headline(d, ["FORTRESS DELHI:", "4 CORDONS OF CONTROL"], 310, 72, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(15, 23, 42), outline=(56, 189, 248), width=2)
for cr in [120, 220, 320]:
    d.ellipse([540 - cr, 800 - cr, 540 + cr, 800 + cr], outline=(56, 189, 248, 120), width=2)
d.ellipse([510, 770, 570, 830], fill=(239, 68, 68))
d.text((430, 850), "JANTAR MANTAR", font=get_font(FONT_MONO, 28), fill=(251, 191, 36))
d.text((120, 1080), "• Outer Ring: State borders sealed", font=get_font(FONT_INTER, 34), fill=(203, 213, 225))
d.text((120, 1140), "• Inner Ring: Lutyens Delhi locked", font=get_font(FONT_INTER, 34), fill=(203, 213, 225))
draw_status_badge(d, "4 RINGS OF SECURITY CORDON", 1280, 46, (56, 189, 248), (255, 255, 255))
b23.save(ASSETS_DIR / "beat_23.jpg", quality=95)

# BEAT 24: Supreme Court of India Grand Facade
b24 = create_base((12, 12, 18), (5, 5, 8))
b24 = add_glow_orb(b24, 540, 750, 440, (251, 191, 36), 0.45)
d = ImageDraw.Draw(b24)
draw_header_tag(d, "🏛️ SUPREME COURT OF INDIA", 220, (251, 191, 36))
draw_main_headline(d, ["THE APEX COURT", "STEPS IN TODAY!"], 310, 74, (255, 255, 255))
draw_info_box(d, 80, 520, W-160, 680, "JUDICIAL INTERVENTION DOSSIER", [
    ("Apex Court", "SUPREME COURT OF INDIA"),
    ("Plea Heard", "URGENT CONTEMPT PETITION"),
    ("Public Grievance", "ENTIRE CAPITAL PARALYZED"),
    ("Transit Service", "METRO & TRAINS RESUMPTION"),
    ("Bench Mandate", "AVOID COMPLETE SHUTDOWN")
], (251, 191, 36))
draw_status_badge(d, "PARTIAL RELIEF ORDERED", 1260, 50, (251, 191, 36), (254, 240, 138), "SUPREME COURT FULL BENCH INTERVENES")
b24.save(ASSETS_DIR / "beat_24.jpg", quality=95)

# BEAT 25: Apex Court Emergency Bench Hearing
b25 = create_base((14, 10, 14), (6, 4, 6))
b25 = add_glow_orb(b25, 540, 750, 450, (239, 68, 68), 0.45)
d = ImageDraw.Draw(b25)
draw_header_tag(d, "⚖️ EMERGENCY COURTROOM HEARING", 220, (239, 68, 68))
draw_main_headline(d, ["GOVERNMENT GRILLED OVER", "DISPROPORTIONATE FORCE"], 310, 62, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(18, 14, 20), outline=(239, 68, 68), width=2)
d.text((120, 580), "QUESTION POSED TO SOLICITOR GENERAL:", font=get_font(FONT_MONO, 28), fill=(239, 68, 68))
d.text((120, 680), "\"Why must millions of ordinary", font=get_font(FONT_INTER, 42), fill=(248, 250, 252))
d.text((120, 740), "citizens suffer when a small", font=get_font(FONT_INTER, 42), fill=(248, 250, 252))
d.text((120, 800), "group exercises peaceful protest?\"", font=get_font(FONT_INTER, 42), fill=(251, 191, 36))
d.rectangle([110, 920, W-110, 1140], fill=(28, 18, 24), outline=(239, 68, 68), width=2)
d.text((160, 960), "BENCH OBSERVATION:", font=get_font(FONT_MONO, 30), fill=(239, 68, 68))
d.text((140, 1030), "\"Security must be proportionate.\"", font=get_font(FONT_ANTON, 48), fill=(255, 255, 255))
draw_status_badge(d, "BENCH CHALLENGES POLICE OVERREACH", 1280, 46, (239, 68, 68), (255, 255, 255))
b25.save(ASSETS_DIR / "beat_25.jpg", quality=95)

# BEAT 26: The Historic Judicial Rebuke Quote Plaque
b26 = create_base((18, 8, 12), (7, 3, 5))
b26 = add_glow_orb(b26, 540, 750, 500, (251, 191, 36), 0.6)
d = ImageDraw.Draw(b26)
draw_header_tag(d, "🔥 THE SUPREME COURT REBUKE", 220, (251, 191, 36))
draw_main_headline(d, ["HISTORIC VERBAL STRIKE", "AGAINST OVERREACH"], 310, 66, (255, 255, 255))
d.rounded_rectangle([60, 520, W-60, 1220], radius=28, fill=(15, 20, 32), outline=(251, 191, 36), width=4)
d.text((120, 580), "SUPREME COURT OF INDIA DECLARES:", font=get_font(FONT_MONO, 32), fill=(251, 191, 36))
d.text((100, 680), "\"A HAMMER", font=get_font(FONT_ANTON, 90), fill=(254, 240, 138))
d.text((100, 780), "SHOULD NOT BE USED", font=get_font(FONT_ANTON, 72), fill=(255, 255, 255))
d.text((100, 870), "TO KILL A FLY!\"", font=get_font(FONT_ANTON, 84), fill=(239, 68, 68))
d.text((120, 1020), "Questioning the shutdown of Delhi Metro", font=get_font(FONT_INTER, 36), fill=(203, 213, 225))
d.text((120, 1080), "and blanket detention of youth leadership.", font=get_font(FONT_INTER, 36), fill=(203, 213, 225))
draw_status_badge(d, "JUDICIAL VERDICT OF EXCESS", 1260, 48, (239, 68, 68), (255, 255, 255))
b26.save(ASSETS_DIR / "beat_26.jpg", quality=95)

# BEAT 27: Clean Card for Animated Slamming Verdict Stamp
b27 = create_base((16, 6, 10), (6, 2, 4))
b27 = add_glow_orb(b27, 540, 750, 480, (239, 68, 68), 0.6)
d = ImageDraw.Draw(b27)
draw_header_tag(d, "⚖️ FORENSIC VERDICT STAMP", 220, (239, 68, 68))
draw_main_headline(d, ["FINAL ASSESSMENT", "DELHI 10 OCT 2026"], 310, 72, (255, 255, 255))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(18, 14, 20), outline=(239, 68, 68), width=2)
d.text((120, 580), "CONSTITUTIONAL BENCH RULING:", font=get_font(FONT_MONO, 28), fill=(239, 68, 68))
d.text((120, 1060), "A peaceful student protest cannot be met", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
d.text((120, 1120), "with total transit lockdown of 20M citizens.", font=get_font(FONT_INTER, 38), fill=(248, 250, 252))
draw_status_badge(d, "DISPROPORTIONATE STATE ACTION", 1280, 46, (239, 68, 68), (255, 255, 255))
b27.save(ASSETS_DIR / "beat_27.jpg", quality=95)

# BEAT 28: Dual Evidence Ledger
b28 = create_base((10, 14, 20), (4, 6, 9))
b28 = add_glow_orb(b28, 540, 750, 440, (56, 189, 248), 0.45)
d = ImageDraw.Draw(b28)
draw_header_tag(d, "📑 DUAL EVIDENCE LEDGER", 220, (56, 189, 248))
draw_main_headline(d, ["FACTS ESTABLISHED:", "VOTER PURGE & OVERREACH"], 310, 66, (251, 191, 36))
draw_info_box(d, 80, 520, W-160, 680, "TWO PROVEN REALITIES", [
    ("Youth Grievance", "SIR FORM 7 BULK DELETIONS"),
    ("Citizen Impact", "45 METRO STATIONS SHUT"),
    ("Police Mobilization", "25,000 BOOTS DEPLOYED"),
    ("Judicial Finding", "\"HAMMER ON A FLY\""),
    ("Apex Court Status", "FULL BENCH MONITORING")
], (56, 189, 248))
draw_status_badge(d, "SOURCE-BACKED JOURNALISM", 1260, 48, (56, 189, 248), (255, 255, 255))
b28.save(ASSETS_DIR / "beat_28.jpg", quality=95)

# BEAT 29: Benaqaab India Forensic Credo
b29 = create_base((8, 10, 16), (3, 4, 7))
b29 = add_glow_orb(b29, 540, 750, 500, (251, 191, 36), 0.5)
d = ImageDraw.Draw(b29)
draw_header_tag(d, "🛡️ BENAQAAB INDIA • INVESTIGATIVE JOURNALISM", 220, (251, 191, 36))
draw_main_headline(d, ["SACH · SABOOT · BEBAK", "TRUTH · EVIDENCE · UNCOMPROMISING"], 310, 60, (251, 191, 36))
d.rounded_rectangle([80, 520, W-80, 1240], radius=24, fill=(15, 20, 32), outline=(251, 191, 36), width=2)
d.ellipse([420, 620, 660, 860], fill=(24, 32, 48), outline=(251, 191, 36), width=3)
d.text((460, 710), "BI", font=get_font(FONT_ANTON, 90), fill=(251, 191, 36))
d.text((180, 940), "NO SENSATIONALISM. NO RUMORS.", font=get_font(FONT_MONO, 32), fill=(148, 163, 184))
d.text((220, 1030), "ONLY HARD EVIDENCE.", font=get_font(FONT_ANTON, 68), fill=(255, 255, 255))
d.text((180, 1140), "Every claim backed by official source.", font=get_font(FONT_INTER, 34), fill=(203, 213, 225))
draw_status_badge(d, "100% EVIDENCE-BACKED REPORTING", 1280, 46, (251, 191, 36), (254, 240, 138))
b29.save(ASSETS_DIR / "beat_29.jpg", quality=95)

# BEAT 30: Viral Mobile Subscribe CTA Stage
b30 = create_base((10, 12, 20), (4, 5, 9))
b30 = add_glow_orb(b30, 540, 850, 550, (239, 68, 68), 0.4)
b30 = add_glow_orb(b30, 540, 500, 400, (251, 191, 36), 0.3)
d = ImageDraw.Draw(b30)
draw_header_tag(d, "🔔 SUPPORT INDEPENDENT TRUTH", 220, (251, 191, 36))
draw_main_headline(d, ["JOIN 500,000+ CITIZENS", "STANDING FOR TRUTH"], 310, 68, (255, 255, 255))
b30.save(ASSETS_DIR / "beat_30.jpg", quality=95)

print("✅ All 30 visual beats regenerated successfully with ZERO overlapping!")
