# 🎴 MASTER TITLE CARDS PROMPT — CODE-RENDERED MOTION ENGINE

> **AUTHORITY:** Permanent Master Prompt Directive  
> **ORIGIN:** Direct User Master Prompt  
> **MANDATE:** Verbatim Preservation — Do NOT edit anything in this prompt text.

---

## 📜 The Verbatim Master Prompt

```text
You are a motion designer who builds video from code. Make a silent 15 to 20 second title-card video: a sequence of short lines, rendered frame by frame in headless Chrome and encoded to MP4 with ffmpeg. No footage, no image or video generation, no audio. Every frame is drawn with Canvas2D in a web page.

INPUTS (replace these, or use the defaults):
- LINES: 4 to 6 short statements, 1 to 6 words each. Default: "Every frame is code" / "Nothing is filmed" / "Same input" / "Same pixels" / "Render it free".
- PALETTE: background, ink, one accent. Default #0b0b0f, #f4f2ec, #c8ff3d.
- FONT: one display family, downloaded as .woff2 into fonts/. Default Space Grotesk 700 (SIL Open Font License).
- SIZE: 1920×1080 at 30 fps.

PROJECT FILES:
- index.html: a canvas with id "c", @font-face for the local font, and one module script.
- tokens.js: W, H, FPS, colours, font and sizes.
- render.mjs: the puppeteer frame capture.
- package.json with "type": "module" and puppeteer installed (npm install puppeteer).

THE RULE THAT MAKES IT WORK:
Expose window.renderFrame(t), where t is seconds. It must clear and redraw the entire canvas using only t and constants. Never use Math.random, Date.now, performance.now, setTimeout, CSS animations or requestAnimationFrame inside it. Also expose window.DURATION and window.FPS, and set window.READY = true only after document.fonts.load('700 168px "Space Grotesk"') and document.fonts.ready have resolved.

THE CARDS:
One card per line, centred on a flat background. Each card fades in while rising 40 px over 0.5 s, holds for max(1.2, 0.35 + words/3.2) seconds, then fades out over 0.25 s. Exactly one word per card uses the accent colour. Keep all text inside a 144 px margin.

RENDER HARNESS (render.mjs):
Serve the folder on a free port so the font loads over http://. Launch puppeteer headless with a 1920×1080 viewport, open index.html, wait for window.READY, and for each frame i call window.renderFrame(i / FPS) and save canvas.toDataURL('image/png') as frames/f%05d.png.

ENCODE:
ffmpeg -y -framerate 30 -i frames/f%05d.png -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart out/title_cards.mp4

Render one still per card first and check it, then render the full video. If your tool can't run commands, write the files and give me the exact commands to run.
```

---

## 🏛️ Implementation Blueprint & Contract Rules

1. **Deterministic Function of Time (`RULE-RENDERFRAME-DETERMINISM`):**
   - `window.renderFrame(t)` must be 100% mathematical and reproducible.
   - Prohibited inside `renderFrame`: `Math.random()`, `Date.now()`, `performance.now()`, `setTimeout()`, CSS keyframes, `requestAnimationFrame()`.
   - Dual-compatible: Expose both `window.renderFrame(t)` and `window.seek(t)`.

2. **Font Readiness Contract (`RULE-FONT-READY-GATE`):**
   - `window.READY = true` and `window.ready = true` are only set after `document.fonts.load('700 168px "Space Grotesk"')` and `document.fonts.ready` resolve.

3. **Card Motion Kinetics (`RULE-TITLE-CARD-KINETICS`):**
   - In: Fade in + rise 40px over 0.5s via cubic ease-out (`1 - (1-p)^3`).
   - Hold: Hold centered for $\max(1.2, 0.35 + \text{words}/3.2)$ seconds (scaled to achieve 15–20s video).
   - Out: Fade out over 0.25s.
   - Accent Rule: Exactly one word per card rendered with `PALETTE.accent` (`#c8ff3d`).
   - Margin Rule: All text constrained inside 144px safe margin (1632px max width).

4. **Reference Implementation:**
   - Production folder: `projects/title_cards/`
   - Reusable template: `viz/templates/title_cards_boilerplate.html`
