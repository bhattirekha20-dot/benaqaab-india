"""Create the staged dashboard animation requested by the user.

Sequence:
1. The headline panel enters in the centre with a LIVE label.
2. It travels to the top of the screen.
3. The blue demographic-status card enters from the left with LIVE.
4. The orange demographic clock draws itself in real time.
5. The red middle-income card enters from the right with LIVE.
6. All four settle into a balanced, live dashboard.

Run: python3 make_sequence_animation.py
Then convert the temporary MP4 to H.264 with the command in the companion note.
"""
from pathlib import Path
from math import sin, cos, pi
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = Path(__file__).parent
ASSETS = ROOT / "uploads"
HEADER = ASSETS / "image-1.png"
BLUE = ASSETS / "image-2.png"
CLOCK = ASSETS / "image-3.png"
RED = ASSETS / "image-4.png"
OUTPUT = ROOT / "demographic-clock-staged-raw.mp4"

W, H = 1280, 720
FPS, DURATION = 30, 14.5
DARK = (4, 9, 17, 255)
ORANGE = (255, 132, 39)
GOLD = (255, 190, 72)
CYAN = (42, 202, 255)
PINK = (255, 74, 112)
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def clamp(v, lo=0.0, hi=1.0):
    return max(lo, min(hi, v))


def ease(start, end, t):
    """Cubic smoothstep over an exact time range."""
    p = clamp((t - start) / (end - start))
    return p * p * (3 - 2 * p)


def overshoot(start, end, t):
    """Friendly pop-in easing for cards."""
    p = clamp((t - start) / (end - start))
    c1, c3 = 1.70158, 2.70158
    return 1 + c3 * (p - 1) ** 3 + c1 * (p - 1) ** 2


def lerp(a, b, p):
    return a + (b - a) * p


def rgba(color, alpha):
    return (color[0], color[1], color[2], int(clamp(alpha, 0, 255)))


def apply_alpha(img, opacity):
    if opacity >= .999:
        return img
    out = img.copy()
    alpha = out.getchannel("A").point(lambda a: int(a * opacity))
    out.putalpha(alpha)
    return out


def composite_scaled(canvas, asset, x, y, scale, opacity=1.0):
    w, h = max(1, round(asset.width * scale)), max(1, round(asset.height * scale))
    resized = asset.resize((w, h), Image.Resampling.LANCZOS)
    resized = apply_alpha(resized, opacity)
    canvas.alpha_composite(resized, (round(x), round(y)))


def glow_dot(canvas, xy, color, r=5, alpha=1.0):
    x, y = xy
    halo = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    hd = ImageDraw.Draw(halo)
    hd.ellipse((x-r*5, y-r*5, x+r*5, y+r*5), fill=rgba(color, 52 * alpha))
    halo = halo.filter(ImageFilter.GaussianBlur(r * 3))
    canvas.alpha_composite(halo)
    d = ImageDraw.Draw(canvas)
    d.ellipse((x-r, y-r, x+r, y+r), fill=rgba(color, 255 * alpha))
    d.ellipse((x-r*.38, y-r*.38, x+r*.38, y+r*.38), fill=rgba((255, 239, 190), 255 * alpha))


def draw_live_badge(canvas, x, y, color, alpha=1.0, label="LIVE"):
    """A small on-screen LIVE tag for every entered module."""
    if alpha <= .01:
        return
    d = ImageDraw.Draw(canvas)
    font = ImageFont.truetype(MONO, 15)
    tw = int(d.textlength(label, font=font))
    width, height = tw + 48, 29
    # glow and badge shell
    glow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.rounded_rectangle((x-3, y-3, x+width+3, y+height+3), radius=15, outline=rgba(color, 95 * alpha), width=3)
    glow = glow.filter(ImageFilter.GaussianBlur(7))
    canvas.alpha_composite(glow)
    d = ImageDraw.Draw(canvas)
    d.rounded_rectangle((x, y, x+width, y+height), radius=14, fill=rgba((5, 15, 25), 235 * alpha), outline=rgba(color, 180 * alpha), width=1)
    glow_dot(canvas, (x+15, y+height/2), color, 3, alpha * (.75 + .25 * sin(pi * 2 * .8)))
    d.text((x+25, y+7), label, font=font, fill=rgba(color, 255 * alpha))


def draw_ring(canvas, cx, cy, progress, alpha):
    """Draw the centre ring as an actual live stroke, not a static fade."""
    if progress <= 0 or alpha <= 0:
        return
    radius = 111
    bbox = (cx-radius, cy-radius, cx+radius, cy+radius)
    # Bloom under the arc.
    glow = Image.new("RGBA", canvas.size, (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    start, end = -90, -90 + 360 * progress
    gd.arc(bbox, start, end, fill=rgba(ORANGE, 165 * alpha), width=14)
    glow = glow.filter(ImageFilter.GaussianBlur(15))
    canvas.alpha_composite(glow)
    d = ImageDraw.Draw(canvas)
    # Rich two-band orange stroke.
    d.arc(bbox, start, end, fill=rgba((255, 105, 34), 255 * alpha), width=13)
    d.arc((cx-radius+2, cy-radius+2, cx+radius-2, cy+radius-2), start, end, fill=rgba(GOLD, 220 * alpha), width=4)
    # Travelling head with a little orbit sparkle.
    a = end * pi / 180
    hx, hy = cx + radius * cos(a), cy + radius * sin(a)
    glow_dot(canvas, (hx, hy), GOLD, 5, alpha)
    for offset in (95, 210):
        ta = (end + offset) * pi / 180
        x1, y1 = cx + 126 * cos(ta), cy + 126 * sin(ta)
        x2, y2 = cx + 133 * cos(ta), cy + 133 * sin(ta)
        d.line((x1, y1, x2, y2), fill=rgba(ORANGE, 160 * alpha), width=2)


def draw_connection(canvas, x1, x2, y, color, phase, alpha):
    if alpha <= 0:
        return
    d = ImageDraw.Draw(canvas)
    d.line((x1, y, x2, y), fill=rgba(color, 35 * alpha), width=2)
    dotx = lerp(x1, x2, phase)
    glow_dot(canvas, (dotx, y), color, 2.6, alpha)


def make_background(t):
    # Dark navy gradient with a central low-key blue/orange atmosphere.
    yy, xx = np.mgrid[0:H, 0:W]
    base = np.zeros((H, W, 4), dtype=np.uint8)
    vignette = ((xx-W/2)/(W*.7))**2 + ((yy-H/2)/(H*.72))**2
    blue = np.exp(-(((xx-W*.5)/(W*.42))**2 + ((yy-H*.49)/(H*.5))**2))
    orange = np.exp(-(((xx-W*.5)/(W*.19))**2 + ((yy-H*.57)/(H*.25))**2))
    base[...,0] = np.clip(3 + blue*3 + orange*5 - vignette*3, 0, 255)
    base[...,1] = np.clip(8 + blue*7 + orange*2 - vignette*5, 0, 255)
    base[...,2] = np.clip(17 + blue*15 + orange*1 - vignette*8, 0, 255)
    base[...,3] = 255
    img = Image.fromarray(base, "RGBA")
    # Tiny muted grid lines make the opening look intentional rather than empty.
    grid = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(grid)
    grid_alpha = int(8 + 4 * sin(t*.7))
    for x in range(40, W, 80):
        gd.line((x, 0, x, H), fill=(70, 126, 170, grid_alpha), width=1)
    for y in range(40, H, 80):
        gd.line((0, y, W, y), fill=(70, 126, 170, grid_alpha), width=1)
    return Image.alpha_composite(img, grid)


def main():
    for p in (HEADER, CLOCK, RED, BLUE):
        if not p.exists():
            raise FileNotFoundError(p)
    header = Image.open(HEADER).convert("RGBA")
    clock_asset = Image.open(CLOCK).convert("RGBA")
    red = Image.open(RED).convert("RGBA")
    blue = Image.open(BLUE).convert("RGBA")

    writer = cv2.VideoWriter(str(OUTPUT), cv2.VideoWriter_fourcc(*"mp4v"), FPS, (W, H))
    if not writer.isOpened():
        raise RuntimeError("Video writer did not open")

    # Final layout values.  They form the balanced end screen.
    header_final = (190, 45, 1.31)
    blue_final = (67, 270, 1.05)
    clock_final = (510, 284, 1.10)  # 236x250 asset, centred at about 640×421.
    red_final = (900, 275, .97)

    for f in range(int(FPS * DURATION)):
        t = f / FPS
        canvas = make_background(t)

        # --- 1. Headline lands in the centre, then travels up to become the header. ---
        header_in = ease(.15, 1.15, t)
        header_move = ease(2.0, 2.95, t)
        h_scale = lerp(1.10, header_final[2], ease(.2, 2.95, t))
        h_x_start = (W - header.width*1.10) / 2
        h_y_start = 275
        h_x = lerp(h_x_start, header_final[0], header_move)
        h_y = lerp(h_y_start, header_final[1], header_move)
        # A subtle open-scale before the upward move.
        h_scale *= .92 + .08 * header_in
        composite_scaled(canvas, header, h_x, h_y, h_scale, header_in)
        if t < 2.5:
            draw_live_badge(canvas, W/2 - 40, h_y + header.height*h_scale + 20, GOLD, header_in)
        else:
            draw_live_badge(canvas, h_x + header.width*h_scale - 91, h_y + 15, GOLD, .8)

        # Baseline header guide appears after the title has parked at the top.
        guide_alpha = ease(2.8, 3.3, t)
        d = ImageDraw.Draw(canvas)
        d.line((115, 195, 1165, 195), fill=rgba((73, 116, 147), 54 * guide_alpha), width=1)

        # --- 2. Blue age card enters and settles left. ---
        blue_in = ease(3.25, 4.5, t)
        bp = overshoot(3.25, 4.65, t)
        blue_scale = blue_final[2] * (.72 + .28 * min(1, bp))
        blue_x = lerp(430, blue_final[0], bp)
        blue_y = lerp(285, blue_final[1], bp) + (sin(t*1.8)*2 if t > 4.6 else 0)
        composite_scaled(canvas, blue, blue_x, blue_y, blue_scale, blue_in)
        draw_live_badge(canvas, blue_x + 9, blue_y - 35, CYAN, blue_in)

        # --- 3. Clock draws itself as an actual stroke, then its information fades in. ---
        ring_p = ease(5.10, 7.18, t)
        ring_alpha = ease(4.95, 5.28, t)
        cx, cy = 640, 421
        draw_ring(canvas, cx, cy, ring_p, ring_alpha)
        clock_info = ease(6.62, 7.48, t)
        # The supplied clock screenshot gives the finished digits and type a polished look.
        composite_scaled(canvas, clock_asset, clock_final[0], clock_final[1] + sin(t*1.5)*1.8, clock_final[2], clock_info)
        draw_live_badge(canvas, cx-44, 570, ORANGE, max(0, clock_info-.08))

        # --- 4. Red card arrives last from the right. ---
        red_in = ease(7.82, 9.15, t)
        rp = overshoot(7.82, 9.28, t)
        red_scale = red_final[2] * (.70 + .30 * min(1, rp))
        red_x = lerp(1145, red_final[0], rp)
        red_y = lerp(309, red_final[1], rp) + (sin(t*1.7 + 1.2)*2 if t > 9.3 else 0)
        composite_scaled(canvas, red, red_x, red_y, red_scale, red_in)
        draw_live_badge(canvas, red_x + red.width*red_scale - 88, red_y - 35, PINK, red_in)

        # --- 5. Finished composition: active data lines and a quiet bottom status. ---
        final = ease(9.4, 10.2, t)
        draw_connection(canvas, 384, 524, 421, CYAN, (t*.53) % 1, final)
        draw_connection(canvas, 756, 891, 421, PINK, (t*.53+.5) % 1, final)
        if final > 0:
            d = ImageDraw.Draw(canvas)
            font = ImageFont.truetype(MONO, 14)
            footer = "SYSTEM LIVE  •  DEMOGRAPHIC WINDOW TRACKING"
            tw = d.textlength(footer, font=font)
            d.text(((W-tw)/2, 673), footer, font=font, fill=rgba((121, 167, 192), 160*final))
            glow_dot(canvas, ((W-tw)/2-13, 681), CYAN, 2.3, final)

        # Fade from black at the very beginning and a short final resting fade.
        opening = 1 - ease(0, .22, t)
        if opening > 0:
            canvas = Image.alpha_composite(canvas, Image.new("RGBA", (W, H), (0, 0, 0, int(255*opening))))
        ending = ease(DURATION-.35, DURATION, t)
        if ending > 0:
            canvas = Image.alpha_composite(canvas, Image.new("RGBA", (W, H), (0, 0, 0, int(ending*28))))

        writer.write(cv2.cvtColor(np.asarray(canvas.convert("RGB")), cv2.COLOR_RGB2BGR))

    writer.release()
    print(f"Created {OUTPUT} — {DURATION}s at {FPS} fps")


if __name__ == "__main__":
    main()
