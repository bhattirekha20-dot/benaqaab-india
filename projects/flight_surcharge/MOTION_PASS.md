# MOTION_PASS.md — फ्लाइट क्यों महँगी (film 3)

**Format:** 1080×1920 · 30 fps · 5285 frames · **176.167 s (2:56.2)** · deterministic single HTML.
**Renderer:** `python3 ../../viz/hrender.py Flight_Surcharge_Short.html Flight_Surcharge_Short.mp4 --audio audio/master_loud.wav --crf 18 --max-samples 8 --check`

## Scene windows (from TIMELINE.json — measured narration)
| # | Scene | In | Out | Transition out |
|---|---|---|---|---|
| 1 | HOOK | 0.000 | 21.200 | Zoom to Change 0.80 |
| 2 | THE TIERS | 21.200 | 45.772 | Signal Glitch 2 0.67 |
| 3 | THE FUEL LADDER | 45.772 | 73.964 | White Flash 0.40 |
| 4 | THE ROOT | 73.964 | 100.163 | Dissolve · 叠化 0.50 |
| 5 | WHAT IT MEANS | 100.163 | 120.056 | Fold Over 1.00 |
| 6 | THE HONEST PART | 120.056 | 154.131 | Light Leaks 1.00 |
| 7 | CTA | 154.131 | 176.167 | — |

## Ambient motion inventory (the anti-freeze layer)
Global: two orbiting glow fields, drifting 96 px grid, 70 cabin motes moving right-to-left, 34 faster
fuel sparks, a 700 px light sweep crossing every ~4.7 s, camera breathing zoom 1.006→1.012 with a
16–21 s orbit, plus seeded grain and a 0.40 vignette.
Per scene: S1 plane climb + blinking beacon + falling droplets · S2 bars wiping and rupee labels
counting · S3 bars springing, +14 % stamp spring, gauge needle · S4 tanker traverse, Brent line
drawing, spark drift · S5 cards sliding with a plane glyph travelling each route · S6 toggle
switching state, motifs pulsing · S7 pill sheen sweeping, plane crossing the bottom.

## Two fixes applied after the first stills pass
1. **S1 plane entrance** — the climb was finishing at 17.5 s with the droplets starting at 2.2 s, so
   the fuel fell while the plane was still off-frame. Now `clamp(t/11.0)` with droplets from 8.2 s,
   each fading out over its fall.
2. **S7 bottom plane** — moved from y 1480 to 1516 at scale 0.36 so it clears both the third recall
   chip and the caption plate while it crosses.

## Engine-level fixes carried in from films 1–2 (library untouched)
- `Signal Glitch 2` wrapped so the glitch never fully replaces the two shots mid-transition.
- `White Flash` crossfades A→B with the white veil capped at **72 %** and reaching zero at both ends.
- Captions suppressed during transition windows; `dominantIndex()` prevents the snap-back frame.
- Background drawn 1:1 (never inside the camera transform) so text cannot shear.
