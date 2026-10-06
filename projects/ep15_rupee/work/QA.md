# EP15 "Rupee 96" — QA (3 Oct 2026)

## Deliverable
- EP15_Rupee_1920x1080.mp4 · 1920×1080 · 30 fps · H.264 + AAC 48 kHz · target ≈ 190.68 s (3:11)
- captions.srt (116 cues, word-timed) · thumbnail_1280x720.jpg · description.txt · title_pinned.txt

## Audio
- VO 9 clips (voice-00), Hinglish; prep master −14.62 LUFS / TP −1.84 dBTP (alimiter 0.80 ceiling att).
- Align: whisper small, per-clip cost ≤ 0.25 (clean); timeline total 184.279 s / 512 words.
- No music/SFX (§36). No third-party audio (EXT empty) → no source_style pass needed.

## Checks done
- Stills QA @0.6/15/30/55/75/100/125/148/170/186 s — all scenes render, presenter in S1/S6/S8 only.
- Sources card auto-fit (lay9) verified at 190 s: 10 lines fit within safe area; disclaimer top-right.
- Determinism check passed at build time.

## Full render
- 5720 frames · 190.667 s (3:11) · 15.6 MB · blurred frames 0 · captures 5724 · avg samples 1.00.
- motion_report: pops=[] · still_ratio 0.614 (slow amber ticker + static sources card) · freezes/spikes all ≤1.6 s,
  every one inside a VO line (no dead air), longest at 185.5–190.3 s = end card (SOURCES), by design.
- Determinism check: passed ([ok] determinism check passed — no state-carry warning this time).

## Honesty
- Title/thumbnail: typographic only (₹96 + oil line + chips); no news frames, no third-party footage anywhere (EXT empty),
  so no viz/source_style pass needed this episode.
- "Not investment advice" stated in the outro VO, on the end card, and in description.txt. BofA/SBI expectations labelled as
  expectations (reported), not facts. Revised/uncertain numbers (₹2 lakh cr for Ep14) not used here.
