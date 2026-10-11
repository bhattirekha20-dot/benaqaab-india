"""Create a short motion-graphics MP4 from the supplied demographic clock artwork.

Run: python3 make_demographic_motion.py
Output: demographic-clock-motion.mp4

It intentionally has no music, so it can be used as a background motion graphic
or paired with a voice-over/music track later.
"""
from pathlib import Path
from math import cos, sin, pi
from datetime import datetime
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

ROOT = Path(__file__).parent
SOURCE = ROOT / "uploads" / "image-1.png"
OUTPUT = ROOT / "demographic-clock-motion.mp4"
FPS = 30
SECONDS = 12
W, H = 977, 485

# Artwork coordinates in the supplied 977 × 485 dashboard image.
CX, CY, RING_R = 477, 300, 91
LEFT_CARD = (25, 150, 321, 450)
RIGHT_CARD = (631, 150, 927, 450)
ORANGE = (255, 135, 43, 255)
GOLD = (255, 188, 69, 255)
CYAN = (40, 199, 255, 255)
PINK = (255, 73, 112, 255)

FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def smoothstep(a, b, x):
    x = max(0.0, min(1.0, (x - a) / (b - a)))
    return x * x * (3 - 2 * x)


def additive(base: Image.Image, overlay: Image.Image) -> Image.Image:
    """Screen-like alpha compositing used for neon light."""
    return Image.alpha_composite(base, overlay)


def colour_with_alpha(rgb, alpha):
    return (rgb[0], rgb[1], rgb[2], max(0, min(255, int(alpha))))


def rounded_outline(draw, box, colour, width=1, radius=17):
    draw.rounded_rectangle(box, radius=radius, outline=colour, width=width)


def glow_dot(layer, x, y, color, radius=4, strength=1.0):
    # Blurred halo is painted to a temporary layer so it stays soft.
    halo = Image.new("RGBA", layer.size, (0, 0, 0, 0))
    h = ImageDraw.Draw(halo)
    h.ellipse((x - radius * 4, y - radius * 4, x + radius * 4, y + radius * 4), fill=colour_with_alpha(color, 30 * strength))
    halo = halo.filter(ImageFilter.GaussianBlur(radius * 3))
    layer.alpha_composite(halo)
    d = ImageDraw.Draw(layer)
    d.ellipse((x - radius, y - radius, x + radius, y + radius), fill=colour_with_alpha(color, 245))
    d.ellipse((x - radius / 2, y - radius / 2, x + radius / 2, y + radius / 2), fill=(255, 232, 167, 255))


def arc_segment(draw, box, start, end, color, width):
    # PIL uses degrees, begins at 3 o'clock, and proceeds clockwise.
    draw.arc(box, start=start, end=end, fill=color, width=width)


def main():
    if not SOURCE.exists():
        raise FileNotFoundError(f"Could not find {SOURCE}")

    image = Image.open(SOURCE).convert("RGBA")
    image = image.resize((W, H), Image.Resampling.LANCZOS)
    base_array = np.array(image)

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(OUTPUT), fourcc, FPS, (W, H))
    if not writer.isOpened():
        raise RuntimeError("Could not open MP4 writer in this environment.")

    year_font = ImageFont.truetype(FONT_BOLD, 30)
    small_font = ImageFont.truetype(FONT_MONO, 8)
    live_font = ImageFont.truetype(FONT_MONO, 9)

    for frame in range(FPS * SECONDS):
        t = frame / FPS
        # A very subtle push-in makes the complete dashboard feel like a scene,
        # rather than a frozen screenshot.
        zoom = 1.0 + 0.012 * smoothstep(0, SECONDS, t) + 0.002 * sin(t * 0.9)
        zw, zh = int(W * zoom), int(H * zoom)
        enlarged = Image.fromarray(base_array).resize((zw, zh), Image.Resampling.LANCZOS)
        left, top = (zw - W) // 2, (zh - H) // 2
        canvas = enlarged.crop((left, top, left + W, top + H)).convert("RGBA")

        # Scene starts in darkness, then the UI blooms in.
        reveal = smoothstep(0.0, 1.05, t)
        if reveal < 1:
            dark = Image.new("RGBA", (W, H), (0, 0, 0, int((1 - reveal) * 225)))
            canvas = Image.alpha_composite(canvas, dark)

        # Soft breathing light behind the central orbit.
        pulse = 0.5 + 0.5 * sin(2 * pi * t / 2.6)
        halo = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        hd = ImageDraw.Draw(halo)
        halo_r = 116 + int(4 * pulse)
        hd.ellipse((CX - halo_r, CY - halo_r, CX + halo_r, CY + halo_r), fill=colour_with_alpha(ORANGE, 16 + 10 * pulse))
        halo = halo.filter(ImageFilter.GaussianBlur(30))
        canvas = Image.alpha_composite(canvas, halo)

        neon = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        nd = ImageDraw.Draw(neon)

        # Gentle card-edge pulse suggests that the data panels are live.
        edge_alpha = 24 + int(22 * pulse)
        rounded_outline(nd, LEFT_CARD, colour_with_alpha(CYAN, edge_alpha), width=1)
        rounded_outline(nd, RIGHT_CARD, colour_with_alpha(PINK, edge_alpha), width=1)

        # Data packets move between the two panels and the clock.
        y = 300
        left_phase = (t * 0.48) % 1
        right_phase = (t * 0.48 + .46) % 1
        lx = 322 + (373 - 322) * left_phase
        rx = 581 + (630 - 581) * right_phase
        nd.line((323, y, 373, y), fill=colour_with_alpha(CYAN, 30), width=1)
        nd.line((581, y, 629, y), fill=colour_with_alpha(PINK, 30), width=1)
        glow_dot(neon, lx, y, CYAN, radius=2, strength=.8)
        glow_dot(neon, rx, y, ORANGE, radius=2, strength=.8)

        # Orange orbital head: a moving, brightly lit arc and a travelling node.
        # The original ring remains visible behind it, while this layer gives it motion.
        head = -94 + (t * 78) % 360
        trail_degrees = 72
        ring_box = (CX - RING_R, CY - RING_R, CX + RING_R, CY + RING_R)
        for part in range(12):
            p = part / 12
            start = head - trail_degrees + p * trail_degrees
            end = start + trail_degrees / 12 + .9
            alpha = int(10 + 85 * p)
            arc_segment(nd, ring_box, start, end, colour_with_alpha(ORANGE, alpha), 6)
        # A fine golden sweep runs around the outer edge.
        arc_segment(nd, (CX - RING_R - 5, CY - RING_R - 5, CX + RING_R + 5, CY + RING_R + 5), head - 18, head + 5, colour_with_alpha(GOLD, 115), 1)

        rad = head * pi / 180
        node_x = CX + RING_R * cos(rad)
        node_y = CY + RING_R * sin(rad)
        glow_dot(neon, node_x, node_y, GOLD, radius=4, strength=1.1)

        # Three minimal rotating orbit ticks.
        for offset in (128, 248, 8):
            a = (head + offset) * pi / 180
            r1, r2 = 106, 112
            x1, y1 = CX + r1 * cos(a), CY + r1 * sin(a)
            x2, y2 = CX + r2 * cos(a), CY + r2 * sin(a)
            nd.line((x1, y1, x2, y2), fill=colour_with_alpha(ORANGE, 95), width=1)

        # Select one fact in each panel and briefly illuminate its bullet.
        fact_idx = int(t * 1.35) % 5
        left_y = 256 + fact_idx * 29
        right_y = 256 + fact_idx * 29
        glow_dot(neon, 52, left_y, CYAN, radius=1.7, strength=.35)
        glow_dot(neon, 657, right_y, PINK, radius=1.7, strength=.35)

        # Tiny live badge makes the motion state explicit without changing the artwork layout.
        badge_opacity = int(125 + 95 * (0.5 + 0.5 * sin(t * 2 * pi)))
        nd.rounded_rectangle((442, 372, 532, 387), radius=7, fill=(4, 15, 23, 150), outline=colour_with_alpha(ORANGE, 90), width=1)
        glow_dot(neon, 452, 379, ORANGE, radius=1.4, strength=.45)
        nd.text((458, 375), "LIVE  CLOCK", font=live_font, fill=colour_with_alpha(GOLD, badge_opacity))

        # Light scanner travels across the dashboard about once every four seconds.
        scan_x = int(((t % 4.2) / 4.2) * (W + 240) - 120)
        scan = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        sd = ImageDraw.Draw(scan)
        for dx in range(-34, 35):
            a = int(16 * (1 - abs(dx) / 35) ** 2)
            sd.line((scan_x + dx, 52, scan_x + dx, 448), fill=(94, 208, 255, a), width=1)
        scan = scan.filter(ImageFilter.GaussianBlur(2))
        neon.alpha_composite(scan)

        # Bloom the bright layer very lightly, then retain a crisp light layer above it.
        bloom = neon.filter(ImageFilter.GaussianBlur(6))
        bloom.putalpha(bloom.getchannel("A").point(lambda a: int(a * .55)))
        canvas = Image.alpha_composite(canvas, bloom)
        canvas = Image.alpha_composite(canvas, neon)

        # Closing fade is intentionally gentle so the last frame works as a hold frame.
        ending = smoothstep(SECONDS - .75, SECONDS, t)
        if ending > 0:
            canvas = Image.alpha_composite(canvas, Image.new("RGBA", (W, H), (0, 0, 0, int(ending * 55))))

        bgr = cv2.cvtColor(np.array(canvas.convert("RGB")), cv2.COLOR_RGB2BGR)
        writer.write(bgr)

    writer.release()
    print(f"Created {OUTPUT} ({SECONDS}s at {FPS} fps)")


if __name__ == "__main__":
    main()
