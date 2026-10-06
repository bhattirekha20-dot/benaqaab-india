# EP13 QA — "Baarish 13% Kam: Kya Aapki Thali Mehengi Hogi?"
_2026-10-02 · 1920×1080 · 30 fps · 206.5 s (3:26) · H.264 + AAC 48 kHz stereo_

- Durations: 6195 frames = 206.5 s = VO 199.901 s + 6.6 s sources card ✔ (cap 5:00)
- motion_report: `pops: []`, `freezes: []`, still_ratio 0.168 (the rain layer keeps every frame moving)
- Determinism: the comp was audited by the renderer; the only cross-frame value is the rain's `t`-derived y (stable under the repeat check)
- Audio: baked from the same timeline (no drift possible); −14.2 LUFS, TP −4.5 dBTP
- Captions: 122 cues, word-timed from forced alignment (whisper + DP), ≤26 chars
- Sources: on-screen line per scene + 9-item sources card; all items dated Sept–Oct 2026
- Look: RAIN LEDGER — rain motif, gauge dial, regional bars (one scale), rabi month strip, 4-item watchlist
- Presenter: scenes 1, 6, 8 only (≈35 s of 206 s ≈ 17%)
- No third-party footage (all graphics) → no `source_style.py` pass needed
- Standing rules: no music, no HUD, no `will-change`, Hinglish VO + English on-screen text

## Rubric (1–5)
Hook 5 · focal clarity 5 · colour discipline 4 (red only for deficits, gold for money) · rhythm 4 ·
easing 4 · transitions 4 · narration 4 · neutrality 5 · restraint 5 · **weakest: colour discipline (semantic red/gold reuse)**

## Honesty
- Ran: prep, align, 6195-frame render, ffprobe, loudness, contact sheets.
- Unsure: some figures are outlet-reported (reservoir %, onion ×2) and may be revised by IMD/CWC.
- Verify: watch once end-to-end; the SRT is optional (upload or keep as a file).
- Next improvement: when IMD's Oct–Dec outlook updates, cut a 60 s Short from scene 6 (rabi test).
