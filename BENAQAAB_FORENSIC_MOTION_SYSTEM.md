# 🔍 BENAQAAB INDIA — ALL-IN-ONE AI MASTER DIRECTIVE & MOTION SYSTEM
### SACH · SABOOT · BEBAK (Truth · Proof · Outspoken)
> **Target Audience:** Any AI Agent generating or updating Benaqaab India video compositions (`comp.html`)  
> **Status:** Single Source of Truth · Definitive Autonomous Blueprint  
> **Repository:** `https://github.com/bhattirekha20-dot/benaqaab-india`

---

## 1. THE FOUNDATIONAL LAW: CODE IS THE VIDEO EDITOR
You are the **Lead Forensic Motion Director for Benaqaab India**. Your job is to produce high-impact, factually bulletproof investigative journalism videos.

### 🚫 The Proprietary App Trap (What NEVER to do)
- **Never dump raw catalogues of thousands of CapCut, Photoshop, or Premiere Pro effect names** (e.g. *"Photoshop Liquify"*, *"CapCut 3D Zoom Pro"*, *"Premiere Warp Stabilizer"*).
- Proprietary desktop GUIs cannot run in this headless Linux environment.
- Dumping thousands of closed-source effect IDs bloats the prompt token window, induces severe instruction drift, causes hallucinations of non-existent APIs, and degrades visual output.

### ✅ The Deterministic Engine Reality (What ALWAYS to do)
- Video in this workspace is generated as a pure function of time $t$ inside a single, self-contained HTML file (`comp.html`).
- The composition is rendered frame-by-frame by headless Chromium using `viz/hrender.py` into broadcast-grade MP4 at **1080×1920 (9:16 vertical, 30 FPS)**.
- Instead of proprietary filters, every visual effect is executed natively using **mathematical easing, spring physics, canvas composite operations, and procedural SVG/DOM layers**.

---

## 2. THE 1-GATE PRODUCTION PIPELINE
Every production follows this strict, unskippable 6-step cycle:

```
[Step 1: Primary Research] ➔ [Step 2: Fact Ledger JSON] ➔ [Step 3: VO & Timestamps]
                                                                    │
[Step 6: Master MP4 Render] 🠄 [Step 5: 1-Gate User Approval] 🠄 [Step 4: comp.html]
```

1. **Primary Research:** Source government gazettes, PIB, RBI, DGCA, Supreme Court orders, or official balance sheets. No uncited claims.
2. **Fact Ledger Manifest:** Formulate a structured `FACT_LEDGER` JavaScript object containing all metrics, dates, and citations.
3. **Audio Voiceover Lock:** Synthesize or record voiceover; measure integrated loudness to **-14 LUFS (±1.0 LUFS)** with True Peak **≤ -1.0 dBFS / dBTP**. Extract word-level timestamps.
4. **HTML Composition (`comp.html`):** Build the standalone HTML file implementing `window.seek(t)`, embedding the 5 forensic motion primitives.
5. **The 1-Gate Approval:** **STOP.** Present the interactive preview (`comp.html`) to the human director. The user scrubs the timeline and inspects safe zones.
6. **Master Render:** Only upon explicit approval (*"render the video"*), execute:
   ```bash
   python3 viz/hrender.py comp.html out.mp4 --fps 30 --audio vo.mp3
   ```

---

## 3. THE "DATA-TO-DOM" FACT LEDGER ARCHITECTURE
**Rule:** Every single statistic, date, percentage, or currency figure drawn on screen MUST be dynamically bound to `FACT_LEDGER`. Hardcoding magic numbers in canvas `fillText` is strictly forbidden.

### Standard Schema
```javascript
const FACT_LEDGER = {
  caseId: "CASE #IND-402-26",
  topic: "AIRLINE FARE SURCHARGE SPIKE",
  headlineHi: "फ्लाइट टिकट पर ₹10,000 का 'सीक्रेट' सरचार्ज?",
  baseFare: 4200,
  surchargeAmount: 10000,
  spikePercentage: 238,
  sourceAgency: "DGCA NOTIFICATION REF-2026/09",
  sourceDocumentDate: "2026-10-06",
  verdict: "UNJUSTIFIED EXTRACTION",
  verdictHi: "सबूत: मनमाना सरचार्ज"
};
```

---

## 4. THE 5 FORENSIC MOTION PRIMITIVES (RUNNABLE CODE)
Every Benaqaab video achieves its signature high-end investigative feel through these 5 modular visual primitives:

### Primitive 1: Rolling Numeric Odometer (Retention Hook)
- **Purpose:** Dynamically roll up numbers (prices, scam figures, percentages) with exponential deceleration, settling on the exact ledger figure with a sound-locked bounce.

```javascript
function drawOdometer(ctx, t, startT, duration, startVal, targetVal, x, y) {
  const p = Math.max(0, Math.min(1, (t - startT) / duration));
  const eased = p === 1 ? 1 : 1 - Math.pow(2, -10 * p); // outExpo
  const current = Math.round(startVal + (targetVal - startVal) * eased);
  
  ctx.save();
  ctx.font = '900 110px monospace';
  ctx.fillStyle = '#ef4444';
  ctx.shadowColor = 'rgba(239, 68, 68, 0.6)';
  ctx.shadowBlur = 25;
  ctx.textAlign = 'center';
  ctx.fillText(`+ ₹${current.toLocaleString('en-IN')}`, x, y);
  ctx.restore();
}
```

### Primitive 2: Yellow Forensic Highlighter Sweep
- **Purpose:** Emulates an authentic legal highlighter pen sweeping across key clauses of an official gazette or contract.
- **Key Technique:** Uses `globalCompositeOperation = 'multiply'` so the document text underneath remains completely crisp and visible.

```javascript
function drawHighlighter(ctx, t, startT, duration, x, y, width, height) {
  if (t < startT) return;
  const p = Math.max(0, Math.min(1, (t - startT) / duration));
  const easedWidth = width * (1 - Math.pow(1 - p, 3)); // outCubic
  
  ctx.save();
  ctx.globalCompositeOperation = 'multiply';
  ctx.fillStyle = 'rgba(250, 204, 21, 0.65)'; // Fluorescent Marker Yellow
  ctx.fillRect(x, y, easedWidth, height);
  ctx.restore();
}
```

### Primitive 3: Classified Redaction Tape Peel
- **Purpose:** A matte black classified tape bar that slides or peels off on the beat, exposing hidden evidence.

```javascript
function drawRedactionPeel(ctx, t, startT, duration, x, y, width, height) {
  let offset = 0;
  if (t >= startT) {
    const p = Math.max(0, Math.min(1, (t - startT) / duration));
    offset = (p * (2 - p)) * (width + 40); // outQuad slide
  }
  const remainingW = Math.max(0, width - offset);
  if (remainingW <= 0) return;

  ctx.save();
  ctx.fillStyle = '#09090b'; // Heavy matte black
  ctx.shadowColor = 'rgba(0,0,0,0.5)';
  ctx.shadowBlur = 10;
  ctx.fillRect(x + offset, y, remainingW, height);
  
  // Watermark text if not fully peeled
  if (offset < width * 0.4) {
    ctx.fillStyle = '#71717a';
    ctx.font = '700 18px monospace';
    ctx.fillText('TOP SECRET · PENDING VERIFICATION', x + 20 + offset, y + height * 0.65);
  }
  ctx.restore();
}
```

### Primitive 4: Evidence Loupe / Zoom Lens
- **Purpose:** High-tech circular magnifying glass with crosshairs and 2X zoom hovering over a signature, stamp, or clause.

```javascript
function drawEvidenceLoupe(ctx, t, startT, x, y, radius, zoomScale = 2.0) {
  if (t < startT) return;
  const p = Math.max(0, Math.min(1, (t - startT) / 0.8));
  // Spring entry
  const scale = 0.3 + 0.7 * (1 - Math.exp(-p * 8) * Math.cos(p * 12));

  ctx.save();
  ctx.translate(x, y);
  ctx.scale(scale, scale);

  // Outer Lens Housing
  ctx.shadowColor = 'rgba(0,0,0,0.6)';
  ctx.shadowBlur = 25;
  ctx.strokeStyle = '#38bdf8';
  ctx.lineWidth = 8;
  ctx.beginPath();
  ctx.arc(0, 0, radius, 0, Math.PI * 2);
  ctx.stroke();

  // Glass reflection tint
  ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
  ctx.fill();
  ctx.shadowBlur = 0;

  // Crosshair reticle
  ctx.strokeStyle = 'rgba(56, 189, 248, 0.5)';
  ctx.lineWidth = 1.5;
  ctx.beginPath();
  ctx.moveTo(-radius + 15, 0); ctx.lineTo(radius - 15, 0);
  ctx.moveTo(0, -radius + 15); ctx.lineTo(0, radius - 15);
  ctx.stroke();

  // Callout Tag
  ctx.fillStyle = '#0f172a';
  ctx.beginPath();
  ctx.roundRect(40, -radius, 140, 38, 8);
  ctx.fill();
  ctx.strokeStyle = '#38bdf8';
  ctx.lineWidth = 1;
  ctx.stroke();
  ctx.fillStyle = '#38bdf8';
  ctx.font = '700 14px monospace';
  ctx.fillText('VERIFIED 2X', 60, -radius + 24);

  ctx.restore();
}
```

### Primitive 5: Slamming Rubber Verdict Stamp (Spring Shockwave)
- **Purpose:** Punctuate the investigative conclusion with an authoritative red stamp (`SABOOT: UNJUSTIFIED`) slamming onto the canvas with spring overshoot and physical screen shake.

```javascript
function drawVerdictStamp(ctx, t, hitT, textEn, textHi, cx, cy) {
  if (t < hitT) return;
  const p = t - hitT;
  
  // Real spring physics: overshoot and bounce back
  const w0 = 14, z = 0.65;
  const springP = 1 - Math.exp(-p * z * w0) * (Math.cos(p * w0 * Math.sqrt(1 - z * z)));
  const scale = 2.8 - (2.8 - 1.0) * Math.min(1.2, springP);

  // Screen shake vibration on impact (lasts 0.25s)
  const impact = Math.max(0, 1 - (p * 4));
  const shakeX = Math.sin(t * 80) * 8 * impact;
  const shakeY = Math.cos(t * 70) * 8 * impact;

  ctx.save();
  ctx.translate(cx + shakeX, cy + shakeY);
  ctx.rotate(-0.08); // Authentic rubber stamp angle
  ctx.scale(scale, scale);

  // Heavy Outer Border
  ctx.strokeStyle = '#dc2626';
  ctx.lineWidth = 10;
  ctx.beginPath();
  ctx.roundRect(-360, -90, 720, 180, 20);
  ctx.stroke();

  // Inner Double Border
  ctx.strokeStyle = '#ef4444';
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.roundRect(-345, -75, 690, 150, 12);
  ctx.stroke();

  // Text Inks
  ctx.fillStyle = '#ef4444';
  ctx.textAlign = 'center';
  ctx.font = '900 56px -apple-system, sans-serif';
  ctx.fillText(textEn, 0, -10);

  ctx.fillStyle = '#fca5a5';
  ctx.font = '800 36px "Noto Sans Devanagari", sans-serif';
  ctx.fillText(textHi, 0, 48);

  ctx.restore();
}
```

---

## 5. MOBILE SAFE ZONE SPECIFICATIONS (9:16 VERTICAL)
When composing for YouTube Shorts and Instagram Reels, never place crucial text or proof inside the UI obstruction zones:

| Screen Region | Viewport Coverage | What Lives Here (Do NOT place evidence here) |
|---|---|---|
| **Top Zone** | `0px` to `230px` (Top 12%) | Channel avatar, subscribe pill, search icon. |
| **Bottom Zone** | `1497px` to `1920px` (Bottom 22%) | Captions, sound track pill, channel title. |
| **Right Margin** | `907px` to `1080px` (Right 16%) | Like, Dislike, Comment, Share, Remix icons. |
| **SAFE WORKSPACE** | **X: 80 to 900 \| Y: 240 to 1480** | **All titles, counters, documents, and stamps MUST live here.** |

---

## 6. THE DETERMINISTIC `window.seek(t)` CONTRACT
Chromium renders frame-by-frame. The HTML file must export this exact contract:

```javascript
window.ready = true;        // Set to true once fonts/assets load
window.DURATION = 15.0;     // Exact runtime in seconds (matched to audio file)
window.FPS = 30;            // House framerate
window.WIDTH = 1080;
window.HEIGHT = 1920;

// The single render method called by hrender.py on every frame
window.seek = function(t) {
  // Clear canvas
  // Render Layer 1: Background grid & deterministic dust particles
  // Render Layer 2: UI Badges & Case ID
  // Render Layer 3: Scene active at time t
  // Render Layer 4: Forensic vignette & grain
};
```

- **No `Math.random()` during draw:** Randomness must be a pure function of $t$ using deterministic PRNG (`seededRandom(s)`).
- **No `setInterval` or `setTimeout`:** Animations are driven exclusively by the variable $t$.

---

## 7. FULL REUSABLE BOILERPLATE (`comp.html`)
Copy and adapt this complete boilerplate for any upcoming episode or short:

```html
<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<title>Benaqaab Production Comp</title>
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { background: #070b14; display: flex; justify-content: center; align-items: center; min-height: 100vh; }
  canvas { display: block; max-height: 96vh; aspect-ratio: 9/16; }
</style>
</head>
<body>
<canvas id="stage" width="1080" height="1920"></canvas>
<script>
(() => {
  'use strict';
  const W = 1080, H = 1920, FPS = 30, DURATION = 15.0;
  window.DURATION = DURATION; window.FPS = FPS; window.WIDTH = W; window.HEIGHT = H; window.ready = true;

  const FACT_LEDGER = {
    caseId: "CASE #IND-402-26",
    title: "AIRLINE FARE HIKE SCAM",
    headlineHi: "फ्लाइट टिकट पर ₹10,000 की नई लूट?",
    baseFare: 4200,
    surcharge: 10000,
    verdict: "SABOOT: UNJUSTIFIED"
  };

  const cvs = document.getElementById('stage');
  const ctx = cvs.getContext('2d');

  window.seek = function(t) {
    ctx.clearRect(0, 0, W, H);
    
    // 1. Blueprint Grid Background
    const bg = ctx.createLinearGradient(0, 0, 0, H);
    bg.addColorStop(0, '#060a12'); bg.addColorStop(1, '#0b1324');
    ctx.fillStyle = bg; ctx.fillRect(0, 0, W, H);
    
    // 2. Persistent Top Badge
    ctx.fillStyle = '#f8fafc';
    ctx.font = '700 24px -apple-system, sans-serif';
    ctx.fillText('BENAQAAB FORENSICS', 100, 120);

    // 3. Scene Branching based on t
    if (t < 4.5) {
      // Scene 1: Hook & Odometer Counter
    } else if (t < 9.5) {
      // Scene 2: Forensic Document, Highlighter & Redaction Peel
    } else {
      // Scene 3: Data Comparison & Slamming Verdict Stamp
    }
  };

  // Browser scrub preview helper
  let curT = 0;
  function loop() {
    curT = (curT + 1/30) % DURATION;
    window.seek(curT);
    requestAnimationFrame(loop);
  }
  window.seek(0);
  requestAnimationFrame(loop);
})();
</script>
</body>
</html>
```

---
*Benaqaab India — Sach • Saboot • Bebak*  
*Repository: https://github.com/bhattirekha20-dot/benaqaab-india*
