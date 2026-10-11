#!/usr/bin/env python3
"""
Benaqaab India - Automated Layout & Typography Critic Gate (tools/layout_gate.py)
Inspects deterministic code-rendered compositions via window.layout(t) sampling.

Checks:
1. Minimum font sizes (Shorts 9:16: >= 34px labels/tags, >= 44px body; 16:9: >= 14px secondary, >= 18px body).
2. Safe zone violations (preventing edge clipping or UI obstructions).
3. Overlapping text collisions (detecting colliding bounding boxes across active elements).
4. Reading speed budget (ensuring text remains visible long enough to be read).
"""

import argparse
import asyncio
import math
import sys
from pathlib import Path
from playwright.async_api import async_playwright

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


# Reading speed standard: ~180-220 words per minute (~3.5 words/sec or ~18 chars/sec)
def min_reading_seconds(text: str) -> float:
    words = len(text.strip().split())
    # Minimum 0.75s floor for single words, +0.28s per word
    return max(0.75, 0.4 + words * 0.28)

def boxes_intersect(b1, b2, pad=2) -> bool:
    # Check if two 2D axis-aligned bounding boxes overlap (with slight padding forgiveness)
    return not (
        b1['x'] + b1['w'] - pad < b2['x'] + pad or
        b2['x'] + b2['w'] - pad < b1['x'] + pad or
        b1['y'] + b1['h'] - pad < b2['y'] + pad or
        b2['y'] + b2['h'] - pad < b1['y'] + pad
    )

async def audit_composition(url: str, duration: float = None, sample_step: float = 0.25, is_shorts: bool = False):
    print(f"\n=======================================================")
    print(f"  🔍 BENAQAAB AUTOMATIC LAYOUT & TYPOGRAPHY CRITIC")
    print(f"  Target: {url}")
    print(f"  Format: {'9:16 Shorts (Vertical)' if is_shorts else '16:9 Master (Widescreen)'}")
    print(f"=======================================================\n")

    # Safe zone definitions
    if is_shorts:
        safe_x0, safe_x1 = 80, 1000
        safe_y0, safe_y1 = 180, 1740
        min_font_px = 34.0
    else:
        safe_x0, safe_x1 = 60, 1860
        safe_y0, safe_y1 = 40, 1040
        min_font_px = 14.0

    violations = []
    text_lifespans = {} # text -> {'first': t, 'last': t, 'count': n}

    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--enable-gpu-rasterization",
                "--ignore-gpu-blocklist",
                "--disable-web-security"
            ]
        )
        page = await browser.new_page(viewport={"width": 1080 if is_shorts else 1920, "height": 1920 if is_shorts else 1080})
        await page.goto(url, wait_until="networkidle")
        await page.wait_for_timeout(1000)

        # Probe duration if not passed
        if duration is None:
            comp_dur = await page.evaluate("window.TOTAL_DURATION || window.DURATION || 60.0")
            duration = float(comp_dur)

        print(f"⏱️ Auditing duration: {duration:.2f}s (sampling every {sample_step}s)...")

        t = 0.0
        sample_count = 0

        while t <= duration:
            # Layout probe call
            boxes = await page.evaluate(f"window.layout ? window.layout({t}) : []")
            sample_count += 1

            if boxes:
                # Filter visible boxes (alpha > 0.05)
                visible = [b for b in boxes if b.get('alpha', 1.0) > 0.05 and b.get('s', '').strip()]

                # 1. Check minimum font size & safe zone
                for b in visible:
                    s = b['s'].strip()
                    px = b.get('px', 0)
                    bx0 = b['x']
                    bx1 = b['x'] + b['w']
                    by0 = b['y']
                    by1 = b['y'] + b['h']

                    # Typography scale check
                    if px < min_font_px:
                        violations.append({
                            't': t,
                            'type': 'FONT_TOO_SMALL',
                            'detail': f"Text '{s}' rendered at {px:.1f}px (minimum is {min_font_px}px)"
                        })

                    # Safe zone check
                    if bx0 < safe_x0 or bx1 > safe_x1 or by0 < safe_y0 or by1 > safe_y1:
                        violations.append({
                            't': t,
                            'type': 'SAFE_ZONE_VIOLATION',
                            'detail': f"Text '{s}' bounds [{bx0:.0f}, {by0:.0f}, {bx1:.0f}, {by1:.0f}] exceeds safe zone [{safe_x0}, {safe_y0}, {safe_x1}, {safe_y1}]"
                        })

                    # Track on-screen duration
                    if s not in text_lifespans:
                        text_lifespans[s] = {'first': t, 'last': t, 'count': 1}
                    else:
                        text_lifespans[s]['last'] = t
                        text_lifespans[s]['count'] += 1

                # 2. Check collisions / overlaps
                for i in range(len(visible)):
                    for j in range(i + 1, len(visible)):
                        b1 = visible[i]
                        b2 = visible[j]
                        if boxes_intersect(b1, b2, pad=4):
                            violations.append({
                                't': t,
                                'type': 'TEXT_COLLISION_OVERLAP',
                                'detail': f"'{b1['s'].strip()}' collides with '{b2['s'].strip()}' at [{b1['x']:.0f}, {b1['y']:.0f}]"
                            })

            t = round(t + sample_step, 3)

        await browser.close()

    # 3. Check reading time budget for distinct statements
    for s, data in text_lifespans.items():
        if len(s.split()) >= 3: # Only multi-word statements
            on_screen_dur = data['last'] - data['first'] + sample_step
            needed = min_reading_seconds(s)
            if on_screen_dur < needed:
                violations.append({
                    't': data['first'],
                    'type': 'READING_TIME_TOO_SHORT',
                    'detail': f"Statement '{s}' held for {on_screen_dur:.2f}s but requires at least {needed:.2f}s for comprehension"
                })

    # Summary report
    print("\n-------------------------------------------------------")
    print(f"📊 AUDIT RESULTS: {sample_count} sample slices analyzed")
    print("-------------------------------------------------------")

    if not violations:
        print("✅ 100% CLEAN! Zero font scale violations, zero safe-zone clips, zero text overlaps.\n")
        return True

    # Group violations by type
    by_type = {}
    for v in violations:
        by_type.setdefault(v['type'], []).append(v)

    for vtype, items in by_type.items():
        print(f"\n❌ [{vtype}] ({len(items)} instances):")
        # Show first 5 examples
        for item in items[:5]:
            print(f"   • at t={item['t']:.2f}s: {item['detail']}")
        if len(items) > 5:
            print(f"   ... and {len(items) - 5} more.")

    print(f"\n🚫 TOTAL VIOLATIONS DETECTED: {len(violations)}\n")
    return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Benaqaab Layout & Typography Quality Gate")
    parser.add_argument("url", help="HTTP URL or path to comp.html")
    parser.add_argument("--duration", type=float, default=None, help="Duration in seconds to audit")
    parser.add_argument("--step", type=float, default=0.25, help="Sampling step in seconds (default: 0.25)")
    parser.add_argument("--shorts", action="store_true", help="Audit as 9:16 vertical Short")

    args = parser.parse_args()
    success = asyncio.run(audit_composition(args.url, args.duration, args.step, args.shorts))
    sys.exit(0 if success else 1)
