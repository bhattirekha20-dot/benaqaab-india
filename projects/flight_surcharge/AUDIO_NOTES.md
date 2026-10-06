# AUDIO_NOTES.md — फ्लाइट क्यों महँगी (film 3)

Rebuild: `python3 build_audio.py` (writes `audio/master.wav`, then `audio/master_loud.wav`).
Renderer input: `--audio audio/master_loud.wav`.

## Narration
| # | Clip | Placed at | Length |
|---|---|---|---|
| 1 | `audio/vo_1_48.wav` | 0.550 s | 20.550 s |
| 2 | `vo_2_48.wav` | 21.750 | 23.922 |
| 3 | `vo_3_48.wav` | 46.322 | 27.542 |
| 4 | `vo_4_48.wav` | 74.514 | 25.549 |
| 5 | `vo_5_48.wav` | 100.713 | 19.243 |
| 6 | `vo_6_48.wav` | 120.606 | 33.425 |
| 7 | `vo_7_48.wav` | 154.681 | 19.850 |

Clips are 48 kHz mono 16-bit; they were trimmed at −45 dB with a 0.12 s pad and played at
uniform `atempo 1.10` (see TIMELINE history: raw 209.0 s → 176.167 s).

## Beds (all synthesised in numpy)
- **Pad** — 110 / 164.81 / 220 / 329.63 / 82.41 Hz sines with slow LFOs, band 60–1400 Hz, gain 0.055,
  4 s fade-in / 5 s fade-out. Gain reduces up to **75 %** under speech.
- **Air** — band 900–5200 Hz noise at 0.010 (cabin atmosphere), same duck.
- **Heart** — 55 Hz pulse every 1.25 s with a 4-beat accent pattern, gain 0.10 (level drop under speech).
- **Tick beds** — 2100 Hz ticks every 0.5 s through the tier scene, 1750 Hz through the ATF ladder,
  gain 0.035. Scale moments only; never on top of a spoken number.

## Six distinct cut SFX (one per official transition)
| Cut | Character | Peak | Centroid |
|---|---|---|---|
| Zoom to Change 0.80 s @ 20.650 | riser 260→1500 Hz + band noise, bell + 70 Hz snap at the change | −2.8 dBFS | 3157 Hz |
| Signal Glitch 2 0.67 s @ 45.222 | gated 3 kHz square-noise stutter, zip down, 58 Hz sub | −1.5 | 5916 |
| White Flash 0.40 s @ 73.414 | reversed whoosh, 54 Hz thump + bright bell | −2.3 | 3375 |
| Dissolve 0.50 s @ 99.613 | soft airy band-noise swell + low hand-off tone | −2.0 | 4727 |
| Fold Over 1.00 s @ 119.506 | 1900→320 Hz flutter sweep, paper flap tick, sub | −1.5 | 3031 |
| Light Leaks 1.00 s @ 153.581 | 2200–5500 Hz shimmer rise + airy tail + sub | −1.5 | 7503 |

Measured on the loud master inside each cut window. Speech peaks sit at −1.5 dBFS, so no cut SFX
rides above the voice; SFX duck up to **55 %** under speech.

## Scene accents
S1 entry whoosh 5.6 s + five fuel-drip blips 8.2–12.6 s · S4 war rumble 73.9–82.9 s, two distant
horns 76.6/80.8 s, Brent rise sweep 81.2 s, small ding at the 100-dollar crossing 83.4 s · S5 four
card swooshes + festive bell at the season chip · S6 four UI ticks, toggle click, cooling sweep ·
S7 two-note question motif + Like/Subscribe sparkle.

## Master and loudness
- Mix: `speech rms 0.1160 · bed 0.0142 · sfx 0.0065` (pre-duck), tanh glue, dither, 0.35 s fade,
  sample-peak normalised to **−2.0 dBFS**.
- Two-pass **linear** `loudnorm` (I −14 / TP −2.0 / LRA 6): measured input **−15.19 LUFS / TP −2.00**.
  The TP target was tightened from −1.5 to **−2.0** after the first mux: AAC encoding overshot to
  −1.1 dBFS true peak on the delivered file, above the ≤ −1.5 dBFS spec.
- Re-muxed with `-c:v copy` (video stream bit-identical — MD5 match before and after) from the
  tightened master. Verified on the **muxed** `Flight_Surcharge_Short.mp4` with `ebur128=peak=true`:
  **I −14.0 LUFS · LRA 2.4 LU · true peak −1.6 dBFS**.
- Narration RMS after loudness: −16.5 dBFS, i.e. the voice sits well clear of beds and accents.
- `audio/master.wav` and `audio/master_loud.wav` are **not kept** in the workspace (they were ~170 MB);
  `build_audio.py` regenerates both in ~20 s from the `vo_*_48.wav` clips.

Traps avoided (compact §12.5): no bare `alimiter`; peaks normalised in numpy before the loudness
pass; loudness measured on the file that actually gets muxed.
