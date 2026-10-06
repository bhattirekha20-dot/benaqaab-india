# 🚀 BENAQAAB OS — Channel Intelligence & Production SaaS Studio

**BENAQAAB OS** is a publishable, production-grade SaaS operations studio engineered for investigative video journalism channels. It tracks every stage of video production, from Frame-0 retention hooks and research ledgers to deterministic video playback, thumbnail CTR testing, and 10-point forensic quality compliance.

---

## 🌟 Key Architecture & Features

### 1. 📊 Command Operations HUD
- **Bento Grid Executive Telemetry:** Total output runtime, vetted topic pipeline, master cut delivery count, broadcast compliance score.
- **Time-Critical News Radar:** Live October 2026 alerts (RBI Repo Rate decision, monsoon deficit, crude/rupee swings).
- **Recent Deliveries Shelf:** Instant status checks and 1-click video player.

### 2. 🎬 Episode & Short Production Tracker
- Complete serial index of all channel explainers, flagship documentaries, vertical shorts, and anime motion benchmarks (`EP-01` through `EP-16`, `SH-01` through `SH-08`, `FL-01` through `FL-04`).
- Real-time search by keyword, category, or serial number.
- Instant format filtering: All, 📱 Shorts (9:16), 🎬 Documentaries (16:9), and Delivered.

### 3. 🎯 Master Topic Intelligence Radar
- Pre-researched topic vault citing primary ledgers (RBI, PIB, NPCI, ISRO, GSI, CBIC, BIS).
- **3-Layer Retention Hook breakdown:** Spoken words, visual stimuli, and sharpener text.
- 1-Click State Advancer: Move topics from *Ideation* ➔ *Research Completed* ➔ *Ready to Build* ➔ *In Scripting* ➔ *Ready for Preview*.
- Propose and add custom topics directly with auto-saving to browser `localStorage`.

### 4. 📼 Broadcast Media Vault & Cinema Theater
- Full-screen in-browser player with automatic aspect ratio adaptation (16:9 widescreen vs 9:16 vertical shorts).
- HTTP 206 Partial Content (Byte Range) support for smooth timeline scrubbing and instantaneous seeking.
- Instant MP4 direct download buttons.

### 5. 🖼️ Thumbnail Studio & Real-World CTR Simulator
- **Mobile YouTube Shorts Simulator:** Test 9:16 vertical thumbnails in a realistic smartphone frame with engagement overlays.
- **Desktop Search Simulator:** Test 16:9 landscape thumbnails against dark feed themes to verify contrast and clickability.
- Side-by-side toggles for **Finished Curiosity Typography** vs **Clean Photographic Plates**.

### 6. 🛡️ Forensic QA Matrix & Quality Auditor
- 10-point production audit matrix checking:
  1. Audio Loudness Calibration (-14 LUFS, LRA <= 5 LU).
  2. Frame-0 Retention Hook (concrete conflict in <1.0s).
  3. Full-Screen Visual Staging (65-75% screen open, zero permanent bottom reels).
  4. Two-Source Fact Verification (primary regulatory sources).
  5. Typography & On-Screen Legibility (high contrast, zero mobile clipping).
  6. GPU Compositor Motion (60fps transform/opacity only).
  7. AI Disclosure Labels (disclaimer pills).
  8. 1-Gate Approval Protocol (HTML preview validated before render).
  9. Thumbnail Curiosity & Visual Hook (high-contrast, readable text).
  10. Loopable Ending & Concise CTA (comments question triggering >5 words).

---

## ⚡ How to Run Locally

### Zero-Dependency Python Streaming Server (Recommended):
```bash
python saas/serve.py
```
Open your browser and navigate to:  
👉 **`http://localhost:8080/saas/index.html`**

---

## 🌐 How to Publish Online (1-Click Deployment)

BENAQAAB OS is built with pure Vanilla HTML5, CSS3, and JavaScript with localStorage persistence. It can be hosted on any static or serverless platform with zero configuration:

### Option A: Vercel / Netlify
1. Point your project to the repository root or set root directory to `saas`.
2. Build command: None (Static SPA).
3. Publish directory: `saas`.

### Option B: GitHub Pages
1. Push the repository to GitHub.
2. In Repository Settings ➔ **Pages**, select branch `main` and folder `/saas` (or `/docs`).
3. Your live studio URL will be active immediately.

---

## 💾 Data Backup & Portability
- Click **"💾 Export Database"** in the sidebar to export your full channel production ledger and custom topics to a structured `JSON` file.
- State is automatically preserved in your browser's `localStorage` across page reloads.
