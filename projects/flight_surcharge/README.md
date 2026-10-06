# फ्लाइट क्यों महँगी — ₹10,000 तक सरचार्ज (IndiGo, 6 Oct 2026)

A 2:56 Hindi news-explainer Short on the IndiGo fuel surcharge that went live at 00:01 on
6 October 2026: the five domestic tiers (₹375–₹1,300), the international table (₹1,000–₹10,000),
the ATF ladder behind it (₹115 → ₹110 → ₹115 → ₹121 → ₹137 per litre), the West Asia war and
Brent back over $100 — and the honest layer (this is the second round since February, crude is
cooling again, the other carriers had not announced, and it applies only to new bookings).

**Deliverable:** `Flight_Surcharge_Short.mp4` — 1080×1920 · 30 fps · 5285 frames · 176.167 s ·
H.264 CRF 18 + AAC 192 kbps, loudness-passed audio.

| File | What it is |
|---|---|
| `Flight_Surcharge_Short.html` | the whole film, one deterministic HTML (every frame a pure function of t) |
| `Flight_Surcharge_Short.mp4` | the delivery render (audio muxed, gates run on this file) |
| `TIMELINE.json` | measured narration times that drive the scene windows |
| `SCRIPT.md` | narration, on-screen facts with source tags, transition map, visual plan |
| `SOURCES.md` | N1–N7, the disagreement table, the film rules for this story |
| `PLAN.json` | 7 shots, 14 claims, asset list — structural gate PASS (`_qa/PLAN_GATE.json`) |
| `build_audio.py` | the audio master recipe (numpy beds + 6 distinct cut SFX + duck + two-pass loudnorm) |
| `AUDIO_NOTES.md` | every level and SFX measured on the master |
| `MOTION_PASS.md` | scene windows, ambient-motion inventory, the fixes applied |
| `captions_hi.srt` · `description.txt` · `pinned_comment.txt` · `titles.txt` | upload pack (no brackets) |
| `thumbnail_1280x720.jpg` · `thumbnail_1080x1920.jpg` | thumbnails, cut from the plane hero with a scrim |
| `audio/` | raw VO clips + the trimmed 48 kHz clips + `master.wav` + `master_loud.wav` |
| `_qa/` | pre-render stills + contact sheet, fix-probe contact sheet, PLAN gate report, render log |

## Rebuild
```bash
cd projects/flight_surcharge
python3 build_audio.py
python3 ../../viz/hrender.py Flight_Surcharge_Short.html Flight_Surcharge_Short.mp4 \
        --audio audio/master_loud.wav --crf 18 --max-samples 8 --check
```
Narration can be re-made from `SCRIPT.md` (voice-03) if the audio folder is ever lost; the film HTML
and the engine live in this repo, so the video is fully reproducible.

## Facts and framing
Every number on screen carries its tier and a source tag; the surcharge is framed as **IndiGo's**
decision, not a government or industry move; `सिर्फ़ नई बुकिंग पर लागू` is spoken and on screen;
Africa's ₹6,000 is omitted because sources describe it differently; the ₹425 line in one report is
treated as a typo against three sources saying ₹375. Sources: IndiGo statement via ANI and Business
Standard, New Indian Express, AsiaNet, Economic Times, Indian Express explainer, Trading Economics.
