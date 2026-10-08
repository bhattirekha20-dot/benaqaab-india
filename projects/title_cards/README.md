# 🎬 Code-Rendered Title Card Video Engine

A deterministic, silent title-card video generator built purely from code. Every single frame is rendered with Canvas2D in headless Chrome and encoded to broadcast MP4 with FFmpeg.

- **Zero Stock Footage**
- **Zero AI Video Hallucination (No Runway / Kling / Veo artifacts)**
- **Pure Deterministic Mathematics:** Same input $t$ $\to$ exact same pixels every single time.

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
cd projects/title_cards
npm install
```

### 2. Verify Stills First (Inspect Cards & Alignment)
Before rendering hundreds of frames, generate one crisp still image per card:
```bash
node render.mjs --stills
```
Inspect the output in `stills/`:
- `stills/card_1.png` — "Every frame is **code**"
- `stills/card_2.png` — "Nothing is **filmed**"
- `stills/card_3.png` — "Same **input**"
- `stills/card_4.png` — "Same **pixels**"
- `stills/card_5.png` — "Render it **free**"

### 3. Render Full Video & Encode Master MP4
```bash
node render.mjs
```
This will:
1. Spin up an internal static HTTP server so `@font-face` loads over `http://`.
2. Launch headless Chrome at 1920×1080.
3. Wait for `window.READY === true` (`document.fonts.load` + `document.fonts.ready`).
4. Seek through time $t = i / 30$ and capture frames into `frames/f%05d.png`.
5. Encode the frame sequence with FFmpeg:
   ```bash
   ffmpeg -y -framerate 30 -i frames/f%05d.png -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart out/title_cards.mp4
   ```
6. Produce `out/title_cards.mp4`.

---

## ⚙️ Core Architecture & Contract

### The Rule That Makes It Work
The web composition exposes `window.renderFrame(t)` where $t$ is seconds:
- Clears the canvas with `PALETTE.background`.
- Calculates card phase:
  - **Fade In + Rise:** rises 40px while fading from $\alpha = 0 \to 1$ over 0.5s with cubic ease-out.
  - **Hold:** holds at screen center for $\max(1.2, 0.35 + \text{words}/3.2) \times \text{holdScale}$ seconds.
  - **Fade Out:** fades from $\alpha = 1 \to 0$ over 0.25s.
- Formats words: exactly one word per card receives the accent colour (`#c8ff3d`).
- Auto-scales text if total line width exceeds $1920 - 2 \times 144 = 1632\text{px}$.
- Dual-exposes `window.seek(t) = window.renderFrame(t)` for full interoperability with Benaqaab's `viz/hrender.py`.

---

## 🎨 Customizing Design Tokens (`tokens.js`)

Edit `tokens.js` to change lines, colours, and fonts:
```javascript
export const PALETTE = {
  background: '#0b0b0f', // deep slate obsidian
  ink: '#f4f2ec',        // warm paper text
  accent: '#c8ff3d'      // electric chartreuse accent
};

export const LINES = [
  { text: "Every frame is code", accent: "code" },
  { text: "Nothing is filmed", accent: "filmed" },
  { text: "Same input", accent: "input" },
  { text: "Same pixels", accent: "pixels" },
  { text: "Render it free", accent: "free" }
];
```
