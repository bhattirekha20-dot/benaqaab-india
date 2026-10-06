# EP12 QA — NavIC: India ka apna GPS kyun band pada hai?
_Rendered 2026-10-02 · 1920×1080 · 30 fps · 201.5 s (3:21) · 13.4 MB · H.264 + AAC 48 kHz stereo_

## Kit checklist (what applies to rendered MP4s)
- [x] Durations sum to target: 6044 frames = 201.467 s, composition DURATION = VO 194.277 + 7.2 s sources card
- [x] Seek-safe comp: `render(t)` is pure; audited with the renderer's own determinism check
- [x] No leftover state after backward seek (single-scene display, rebuilt every seek)
- [x] Audio in sync (audio cut from the same timeline; drift impossible — baked mux, not live)
- [x] No pops or glitches — `motion_report`: `"pops": []`
- [x] Motion blur: every frame sharp by design (`speed()` returns 0; no blurred frames) — no smear on text
- [x] Audio loudness −14.2 LUFS, true peak −4.3 dBTP (YouTube target −14)
- [x] No console errors, no network requests (fonts + presenter are local files; no CDN)
- [x] Only transform / opacity / stroke-dashoffset animated
- [x] 16:9 only — no 9:16 overflow case
- [x] Captions are word-timed from the forced alignment (whisper + DP), max 26 chars per cue, min 1 s visible
- [x] Sources card present (5 s) + per-scene source line on screen
- [x] Every gap marked — no `[FILL IN]` left; all facts attributed
- [x] No HUD, no `will-change`, banned-effect list clear

## Freeze report (from motion_report still_ratio 0.656)
Long holds > 1 s: 22 — all intentional (node reads on the timeline, the two panels on "what broke",
the source card hold, the presenter beats). Longest: 195.4–201.1 s = the sources card (5.7 s, under the 6 s dead-air limit).

## Creative rubric (1–5, fixed below 4)
- Hook strength 5 — "India ka GPS aaj akela location nahi bata sakta", government's own words
- Focal point clarity 5 — one saffron focal per scene
- Colour discipline 4 — navy base + saffron focal + cyan data (green/red only for status)
- Rhythm variety 4 — map → timeline → diagram → slot board → split → card → outro; no two adjacent scenes share a form
- Easing quality 4 — SETTLE on arrivals, SWEEP on wipes, no bounce anywhere
- Transition intent 4 — dip between scenes; wipe used only for "what broke" panels
- Narration naturalness 4 — Hinglish, one idea per sentence, no editorialising
- Factual neutrality 5 — every claim attributed; government position stated in its own words
- Emotional restraint 5 — numbers and official statements carry the weight
- **Weakest item: colour discipline** — the red/green status colours appear in two scenes; kept because
  they are semantic (working / failed), not decorative.

## Honesty statement
- **Ran:** prep.py, whisper forced alignment, the full 6044-frame render, ffprobe, loudness analysis,
  frame QA sheet, contact sheets for every scene.
- **Traced only:** the JS `seek()` behaviour on the *delivered* MP4 doesn't apply (the MP4 is baked);
  the comp's seek-safety was verified by the renderer's determinism check.
- **Unsure about:** NVS-03's launch window is *reported* (15–20 Oct), not officially announced —
  labelled "reported" on screen; officials have said it could slip to November, also on screen.
- **User must verify:** nothing before upload. Optional: watch once end-to-end for pacing taste.
- **Next improvement:** add the real ISRO launch clip (styled with `viz/source_style.py`) at 4:30 on
  the launch day, as a pinned follow-up update.

## Assumptions
- A1: Hinglish VO with English on-screen text (standing rule).
- A2: No music (standing rule §36).
- A3: Presenter is AI-generated; labelled "AI PRESENTER" on screen.
- A4: 3:21 length — inside the ≤5 min cap; no source video clips were used (all graphics), so
  `source_style.py` was not needed for this episode.
