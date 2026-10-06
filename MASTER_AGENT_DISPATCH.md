# 🎬 MASTER AGENT DISPATCH — Benaqaab India
### The Complete Single-File Operating Dossier: Video Portfolio, Topic Registry & Production Standards

> **Channel:** Benaqaab India (बेनाक़ाब इंडिया)  
> **Motto:** `SACH · SABOOT · BEBAK` (Truth · Evidence · Uncompromising)  
> **Version:** 2.0 (Reconciled Production Standard) • **Date:** 07 October 2026  
> **Repository:** `https://github.com/bhattirekha20-dot/benaqaab-india`  
> **Audience:** Any AI Agent (Claude, Gemini, GPT, Grok, DeepSeek, Cursor, Codex) or Human Producer taking over video production.

---

## 📌 HOW AN AI AGENT USES THIS FILE

If you are an AI assistant opening this repository, **reading this single document gives you 100% of the operational context**:
1. **Section 1**: Channel Brand DNA, Voice & Graphic Standards.
2. **Section 2**: Complete Portfolio of all 28 topics with existing videos and workspaces.
3. **Section 3**: Central Topic Registry — What is Covered (Never Repeat), Live Cycles, and Ready-to-Build Backlog.
4. **Section 4**: The 10 Non-Negotiables & 20 Absolute Production Laws (L1–L20).
5. **Section 5**: The Three Codified Colour Grading Profiles (Profile A, B, and C).
6. **Section 6**: Technical Toolchain, Rendering Engine & Audio Standards.
7. **Section 7**: Mandatory Unpacked Deliverables Standard (Thumbnails, Covers & Upload Copy).
8. **Section 8**: Step-by-Step AI Action Playbook (From Topic Selection to Published Video).

---

## 🏛️ SECTION 1: CHANNEL BRAND DNA, VOICE & GRAPHIC IDENTITY

### 1.1 Editorial Mission
Benaqaab India is an independent investigative documentary and explainer channel modeled on the investigative rigor of **Dhruv Rathee**, the visual explainers of **Vox**, and the forensic map/motion journalism of **Johnny Harris**.
- We never do generic AI summaries or hollow listicles.
- Every claim must be backed by official documents, court orders, gazette notifications, or multi-source verified data.
- **Presenter Screen Time:** Less than 20% of total video runtime. The visual mechanism, documents, data counters, and evidence take center stage.
- **Mandatory Closing:** Every video ends with the Benaqaab India logo, the closing tagline (*"Sach, Saboot, Bebak"*), and a clear call-to-action.

### 1.2 Voiceover Cadence & Master Clock Law
- **Language:** Conversational, intelligent **Hinglish** (smooth Hindi sentence structure with universally understood English technical/financial terms).
- **Tone:** Calm, investigative, objective, and urgent without screechy sensationalism.
- **The Master Clock Law:** Voiceover timing is the absolute master clock of the video. Visual scene cuts, animated highlights, and data counters are keyed directly to measured narration audio duration (`read_time()` or TTS stem output). Picture never drags after audio finishes.

### 1.3 Brand Identity & Logo Placement Standard
- **Wordmark:** `BENAQAAB INDIA` (बेनाक़ाब इंडिया)
- **Brand Logo Asset:** `brand/benaqaab_os_logo.png` (or embedded SVG logo component).
- **Official Placement:** **Top-Left Safe Area** across ALL 16:9 and 9:16 videos.
  - *9:16 Shorts/Reels (1080×1920):* `top: 36px; left: 32px;`
  - *16:9 Landscape (1920×1080):* `top: 28px; left: 36px;`
  - *Styling:* Translucent dark pill background (`rgba(10, 15, 20, 0.72)`), subtle gold edge glow (`rgba(251, 191, 36, 0.35)`), and 1px border (`rgba(255, 255, 255, 0.12)`).
  - *Superseded Note:* Older mentions of "top-right" logo placement are strictly superseded by this Top-Left standard.

### 1.4 Typography & Font Pairing
- **Display Headlines:** *Outfit*, *Syne*, or *Playfair Display* (bold, authoritative).
- **Body & Data:** *Inter* or *Plus Jakarta Sans* (maximum legibility on mobile screens).
- **Metrics & Code Counters:** *JetBrains Mono* or *Fira Code* (tabular figures for rolling counters).
- **Hindi Text Rule:** Hindi typography expands wider than Latin at equal point sizes. Always apply `.fit` auto-shrinking or explicit line-wrapping logic to prevent layout clipping.

---

## 🎥 SECTION 2: PORTFOLIO OF ALL TOPICS WITH EXISTING VIDEOS

Here is the master catalogue of all delivered videos and production workspaces in the repository:

### 2.1 Flagship Documentaries & Explainers (16:9 Landscape)

| Code | Title & Subject | Duration | Video MP4 Path | Workspace Path | Key Data & Story Mechanism |
|---|---|---|---|---|---|
| **EP-12** | **NavIC — India Ka Apna GPS** | 3m 21s | `VIDEOS/01_NavIC_3m21s.mp4` | `projects/ep12_navic/` | 7-satellite constellation, L5/S dual frequency, 1500 km strategic border buffer, civilian smartphone mandate. |
| **EP-13** | **Monsoon 2026 & El Niño** | 3m 26s | `VIDEOS/02_Monsoon_ElNino_3m26s.mp4` | `projects/ep13_monsoon/` | 12.6% rainfall deficit, El Niño equatorial Pacific warming vs positive Indian Ocean Dipole, crop price ledger. |
| **EP-14** | **Bullet Train 2027 (Mumbai–Ahmedabad)** | 2m 57s | `VIDEOS/03_Bullet_Train_2m57s.mp4` | `projects/ep14_bullet/` | 508 km corridor, Shinkansen E10 tech, 21 km Thane Creek undersea tunnel, 320 km/h operational speeds. |
| **EP-15** | **Rupee 96 vs USD — Aapki Jeb Par Asar** | 3m 11s | `VIDEOS/04_Rupee_96_3m11s.mp4` | `projects/ep15_rupee/` | Currency depreciation, forex reserve defense, Brent crude >$100 impact on fuel and import inflation. |
| **EP-16** | **Made-in-India Chips — Dholera & Sanand** | 3m 47s | `VIDEOS/05_Made_in_India_Chips_3m47s.mp4` | `projects/ep16_chips/` | Tata-PSMC Dholera 28nm fab, Micron Sanand assembly, Assam OSAT facility, semiconductor supply chain. |
| **FL-05** | **Kagaz Ki Machine: Teen Scams, Ek Hi Model** | 12m 40s | Built in Workspace | `projects/kagaz_ki_machine/` | ₹734 Cr GST fake ITC racket, 135 shell entities, scrap bill recycling, ED investigation anatomy. |
| **FL-06** | **Hugging Face AI Model Supply Chain Hack** | 4m 12s | Built in Workspace | `projects/ai_hf_hack/` | Python pickle deserialization vulnerability, 100+ hijacked model weights, remote arbitrary code execution. |

### 2.2 YouTube Shorts & High-Retention Vertical Videos (9:16 Vertical)

| Code | Title & Subject | Duration | Video MP4 Path | Workspace Path | Key Data & Story Mechanism |
|---|---|---|---|---|---|
| **SH-01** | **Neon Blade** | 47s | `VIDEOS/06_Neon_Blade_SHORT_47s.mp4` | `projects/anime_edit_01/` | Dynamic cyberpunk katana, neon rain reflections, fast-paced kinetic cut sequence. |
| **SH-02** | **Laal Chaand** | 48s | `VIDEOS/07_Laal_Chaand_SHORT_48s.mp4` | `projects/anime_edit_02/` | Crimson moon lunar mystery, cherry blossom drift, atmospheric samurai visual rhythm. |
| **SH-03** | **Safed Raat** | 53s | `VIDEOS/08_Safed_Raat_SHORT_53s.mp4` | `projects/anime_edit_03/` | Blizzard ice aesthetic, Arctic Northern Sea trade route geopolitics and icebreaker transit. |
| **SH-08** | **Sona ₹1.5 Lakh: Asli Showroom Bill** | 54s | `VIDEOS/09_Sona_150k_Bill_SHORT_54s.mp4` | `projects/gold_150k/` | ₹1,50,280 spot gold vs ₹1,85,000+ final showroom bill (+3% GST, 12-18% making charges, wastage, hallmarking) vs Gold ETF. |
| **SH-09** | **India Last 24 Hours: 4 Badi Khabrein** | 1m 58s (118s) | `VIDEOS/10_India_Last_24H_SHORT_118s.mp4` | `projects/india_last_24h/` | IAF Chief AP Singh on indigenous weapons, SEBI SME IPO crackdown, Women's T20 World Cup, Rahul Gandhi Kolhapur. Profile A neutral grade. |
| **SH-10** | **India–Japan JCM: Carbon Credits** | 1m 47s (107s) | `VIDEOS/11_India_Japan_JCM_SHORT_107s.mp4` | `projects/india_japan_jcm/` | Article 6.2 Paris Agreement bilateral carbon credits, corresponding adjustments, avoided double counting. |
| **FL-04** | **Flight Surcharge: IndiGo ATF Hike** | 2m 56s (176s) | `projects/flight_surcharge/...mp4` | `projects/flight_surcharge/` | ATF fuel price +14% surge, distance tiers ₹1,375 to ₹11,300, Brent crude $100+ surcharge mechanism. |
| **SH-07** | **Voter List Mein Naam Missing? (SIR)** | 1m 41s (101s) | Built in Workspace | `projects/voter_list_sir/` | 2026 Special Intensive Revision, Form 6/7/8 voter deletions, Supreme Court hearing, checking electoral rolls. |

### 2.3 Early Productions & Experimental Pilots (Documented in Memory)

| Code | Title | Format | Runtime | Workspace Reference |
|---|---|---|---|---|
| **EP-01** | The 10,000mAh Battery War | 16:9 | ~40s | `MEMORY.md` §32 |
| **EP-02** | Master Video Pipeline Pilot | 16:9 | ~45s | `MEMORY.md` §41 |
| **EP-03** | 1 in 4 AI Users on Earth is Indian | 16:9 | ~45s | `MEMORY.md` §45 |
| **EP-04** | Digital Arrest Exposed | 16:9 | 5m 21s | `Digital_Arrest_Exposed.html` |
| **EP-05** | NEET Gen Z Protest & Paper Leak | 16:9 | ~4m 10s | `MEMORY.md` §9 |
| **EP-06** | Air Pollution & The Toxic Smog | 16:9 | ~3m 50s | `MEMORY.md` §9 |
| **EP-07** | News Desk & Presenter Stage Pilot | 16:9 | ~2m 30s | `viz/recipes/ep7_comp.html` |
| **EP-08** | Kal Se Badle Ye Niyam (1 Oct Rules) | 16:9 | ~3m 15s | `viz/recipes/ep8_comp.html` |
| **EP-09** | Chenab Bridge Engineering | 16:9 | ~3m 20s | `MEMORY.md` §80 |
| **EP-10** | India's Last 24 Hours News Desk | 16:9 | ~3m 10s | `viz/recipes/ep10_comp_wiredesk.html` |
| **EP-11** | Market & Economic Tickerboard | 16:9 | ~3m 05s | `viz/recipes/ep11_comp_tickerboard.html` |
| **SH-04** | Lightning: Physics of the Bolt | 9:16 | 45s | `MEMORY.md` §121 |
| **SH-05** | Deeper Than Everest (Challenger Deep) | 9:16 | 52s | `MEMORY.md` §123 |
| **SH-06** | UPI: How India Moves ₹314 Lakh Cr | 9:16 | 55s | `projects/upi_explained_short/` |
| **FL-01** | RBI Rate Decision & EMI Short | 9:16 | ~170s | `MEMORY.md` §143 |
| **FL-02** | Nobel Prize 2026: Optogenetics | 16:9 | ~165s | `MEMORY.md` §145 |
| **FL-03** | Plan Bee — 255 Elephants, One AI | 9:16 | ~170s | `MEMORY.md` §147 |

---

## 🎯 SECTION 3: CENTRAL TOPIC REGISTRY & ROADMAP

Any agent picking or proposing a topic must strictly follow this registry:

### 3.1 🔴 Covered Topics (Strictly NEVER Repeat)
All 28 titles listed in Section 2 above are delivered and published. Under **Rule L16**, an agent must **never** create a video on these topics again unless the user explicitly provides a radically new angle.

### 3.2 🚫 Permanent Blacklist (Never Touch)
1. **Shootspace / GIFT City Cloud-Storage Ponzi**
2. **Task-Based / Part-Time Telegram Job Scam**
3. **Generic AI Voice-Cloning Deepfake Scam**
4. **Generic Delhi Smog Overview** (without new scientific inversion data)

### 3.3 ⏳ Time-Critical Topics (October 2026 Live Cycles)

#### Topic A: RBI Rate Decision & Your EMI
- **Angle:** Weak monsoon (12.6% deficit) ➔ Food mandi inflation ➔ CPI at 4.82% ➔ Brent crude >$100 ➔ RBI pulls the repo rate lever (5.25% ➔ 5.50%) ➔ Home loan EMI vs FD savings returns.
- **Hook:** *"Kal aapki EMI badh sakti hai — aur iska bada kaaran hai: baarish."*
- **Key Stats:** Repo rate 5.25%, expected +25 bps hike to 5.50%; ₹50 lakh loan EMI increases by ₹775–₹820/mo.

#### Topic B: Census 2027 — The World's First Fully Digital Census
- **Angle:** 15-year gap since 2011; 100% digital rollout with mobile self-enumeration (`se.census.gov.in`), 3.4M enumerators, and the return of caste enumeration after 95 years (since 1931).
- **Hook:** *"15 saal se ginti nahi hui thi — ab India pehli baar poori tarah digital tareeke se khud ko gin raha hai."*
- **Key Stats:** ₹11,718.24 crore approved budget; 16-digit Self-Enumeration ID; National Census Moment 1 March 2027.

#### Topic C: Gaganyaan — India's First Robot Astronaut Goes First
- **Angle:** 3-step qualification ladder before crewed spaceflight in 2028; humanoid Vyommitra flying in late 2026 uncrewed test; CE-20 cryogenic hot fire 8,810 seconds.
- **Hook:** *"Insaan se pehle robot jaayega — India ka pehla crewed space mission aise test hota hai."*
- **Key Stats:** ₹20,193 crore budget; TV-D1 abort flight validated; Arabian Sea splashdown with 48 international backup sites.

#### Topic D: October Sky — Halley's Dust at 66 km/s
- **Angle:** Earth crossing the orbital debris stream of Halley's Comet; Draconids (8–9 Oct) and Orionids (21–22 Oct); meteor atmospheric entry speed physics.
- **Hook:** *"Is mahine aasman me Halley's comet ki dhool — 66 kilometre per second ki speed se."*
- **Key Stats:** Entry velocity 66 km/s (237,600 km/h); 200× faster than a rifle bullet.

### 3.4 🟢 High-Priority Researched Backlog (Ready to Build)

1. **Semaglutide 90% Price Crash:** Novo Nordisk patent expired in India on 20 March 2026; price crashed from ₹10,000/mo to ₹1,290/mo across 40+ domestic generic pharma pens (Natco, Glenmark, Eris) vs $1,349 in USA.
2. **Artemis II Lunar Mission:** 4 humans flying around the Moon for the first time in 50 years since Apollo 17; free-return trajectory, SLS Block 1, $93 Billion program.
3. **India's GDP 7.8% vs Per-Capita Income:** Fastest growing major economy (India 7.8% vs China 4.3% vs US 1.5%), 6th nominal ($4.15T), 3rd PPP ($18.9T), but rank 149 in per-capita income (~$2,813).
4. **Olympics 2036 in Ahmedabad:** India's formal Letter of Intent to IOC; SVP Sports Enclave hub model, western corridor venues, bidding against Doha & Riyadh.
5. **3,682 Tigers Census Technology:** India holds 75% of world's wild tigers; M-STrIPES app, camera-trap AI stripe biometrics, scat DNA sequencing.

### 3.5 🔬 Pure Science & Mechanism Explainers

1. **Why Bay of Bengal Gets 4× More Cyclones Than Arabian Sea:** 28–30°C Sea Surface Temperature, three-sided basin heat trapping, freshwater surface lid from Ganga-Brahmaputra.
2. **UPI Switch Architecture:** The 4-party model (Payer App ➔ PSP Bank ➔ NPCI IMPS Switch ➔ Beneficiary Bank) moving ₹314 Lakh Crore annually at zero MDR.
3. **Delhi Winter Smog Inversion:** Atmospheric mixing height collapse from 2,000m to 200m; warm air lid trapping PM2.5 in the bowl between Himalayas and Aravallis.
4. **Jet Stream Flight Time Myth:** Earth's rotation vs 120 mph tropospheric winds; why return flights take 2 hours longer.
5. **Moon's Soil Gradient (ISRO ChaSTE):** +50°C surface dropping to -10°C just 8 cm below the regolith.

---

## ⚖️ SECTION 4: THE 10 NON-NEGOTIABLES & 20 OPERATING LAWS

### The 10 Core Non-Negotiables
1. **Finish the Work:** When given a topic, produce the complete package. Never stop halfway.
2. **Determinism:** Every frame is a pure function of time `f(t)`. No unseeded `Math.random()` during draw loops.
3. **60FPS Motion at 3 Scales:** Micro-jitter/drift, primary layout movements, and background ambient depth. No dead or static frames.
4. **Real Mechanisms, Never Slideshows:** Show pipelines, counters, flowcharts, and genuine evidence cards—never just text over a zooming stock photo.
5. **Fact Integrity:** Every single number must be sourced and dated. When sources disagree, show both numbers on screen.
6. **Master Audio Clock:** Narration timing governs the visual edits. Audio master is normalized to EBU R128 (-14 LUFS).
7. **Text Safety:** Measure before rendering. Hindi is wider than English. Never allow text collisions or viewport overflow.
8. **Editorial Cuts:** Transitions must be clean (whip pans, masked wipes, camera dollys). Captions stay above transition composites.
9. **Verification Before Claims:** Inspect real rendered frames, run the QA gates, and report true numbers.
10. **Preserve the Record:** Never delete protected files. `MEMORY.md` is append-only.

### The 20 Absolute Laws (L1–L20)
- **L1 (Protected Files):** Never delete core skill docs, logs, or reference directories.
- **L2 (Deterministic Time):** `render(t)` takes seconds as input and outputs the identical frame every time.
- **L3 (Motion Scale Hierarchy):** Foreground kinetic typography, midground data/diagrams, background ambient mesh.
- **L4 (Mechanism-First):** Illustrate how things work (e.g., money flow, packet transit, thermal gradient).
- **L5 (Source Ledger):** Every script must contain an attached fact ledger with primary source URLs and dates.
- **L6 (Audio Mix Standards):** Voiceover at 0 dB reference; background music ducked to -18 dB to -24 dB; loudness -14 LUFS.
- **L7 (Typographic Hierarchy):** Max 2 font families; Display for titles, Sans for reading; auto-shrink `.fit` on headlines.
- **L8 (Clean Editorial Handoffs):** Use eased transitions; outgoing text fades to 0 before incoming text enters (`handoff()`).
- **L9 (Factual Integrity):** Never hallucinate stats. State what could not be retrieved.
- **L10 (Append-Only Logging):** Record all changes and project milestones in `MEMORY.md`.
- **L11 (1-Gate Approval Protocol):** Always create and test the interactive `comp.html` first. Do NOT start long MP4 renders until the user approves the preview with *"render the video"*.
- **L12 (Hinglish Narrative Flow):** Keep speech natural, energetic, and free of archaic formal Hindi jargon.
- **L13 (Anti-AI-Slop Visuals):** Use custom Bento grids, multi-stop mesh gradients, and rich glassmorphism. Never use generic purple gradients or 3 identical cards.
- **L14 (Top-Left Logo Safe Area):** The Benaqaab India logo is always placed at the **Top-Left** with subtle gold glow.
- **L15 (Three Colour Profiles):** Always classify the project into Profile A, B, or C (see Section 5).
- **L16 (No Topic Repetition):** Check Section 2 and 3 before proposing or starting any video. Never repeat covered topics.
- **L17 (Autonomous Media Per Story):** In multi-story roundups, the agent must autonomously retrieve or generate dedicated visual assets for *every single story*, not just one subject.
- **L18 (Real Media & AI Imagery):** Use real news stills, official documents, and high-res AI photojournalism composites. Never rely on barren SVG wireframes or plain diagrams alone.
- **L19 (Unpacked Deliverables Standard):** Never bury thumbnails or text files inside a ZIP. Deliverables must exist unpacked at project root and be displayed directly in chat.
- **L20 (Autonomous Technical Fallback):** Once permission is confirmed, never re-ask for permission. If a video clip is blocked by HTTP 403 or captchas, autonomously fall back to verified high-res stills and official data cards without stalling.

---

## 🎨 SECTION 5: THE THREE CODIFIED COLOUR GRADING PROFILES

Never apply a conflicting global grade. Every project belongs to one specific profile:

### Profile A: Daily News & Current Affairs Roundup
- **Projects:** `projects/india_last_24h/`, daily news tickers, wire desks.
- **Look:** Clean neutral documentary grade, balanced crisp whites, natural skin tones.
- **Rule:** **Zero artificial sepia, orange cast, or vintage grading.** Backgrounds are deep slate/obsidian (`#0a0f14`), cards are frosted neutral glass (`rgba(255, 255, 255, 0.05)`), and borders are crisp white (`rgba(255, 255, 255, 0.12)`).

### Profile B: Benaqaab Forensic Dossier / Investigation
- **Projects:** Scam exposés, corruption investigations (`projects/kagaz_ki_machine/`, `Digital_Arrest_Exposed.html`).
- **Look:** High-contrast desaturated/monochrome stills with bold red censor bands (`#ef4444`) and white investigative text.
- **Style:** Evidence corkboards, red string connections, document highlighter strokes (`mix-blend-mode: multiply`), classified dossier stamps.

### Profile C: Archival / Historical Public Video Footage
- **Projects:** Historical documentaries, archival retrospectives (`apply_public_video_grade.py`).
- **Look:** Warm sepia/orange photographic foundation, dark-green horizontal brand bands (`#22764e`), and subtle 3% organic film grain overlay to eliminate digital gradient banding.

---

## 🛠️ SECTION 6: TECHNICAL TOOLCHAIN & RENDERING ENGINE

### 6.1 Deterministic HTML5 Canvas Engine
All Benaqaab India motion graphics are code-rendered using deterministic web standards:
- **Renderer Script:** `viz/hrender.py`
- **Engine:** Playwright controlling headless Chromium.
- **Mechanism:** Captures frames sequentially at exact timestamps (`t = frame / fps`). Frame rate is locked at **24 fps** or **30 fps**.
- **Run Command:**
  ```bash
  python3 viz/hrender.py projects/<project_name>/comp.html --fps 24 --out output.mp4
  ```

### 6.2 Audio & Loudness Pipeline
- **Narration Audio:** Generated via TTS or recorded stems, placed in project directory as `narration_01.mp3`, etc.
- **Master Audio Muxing & Normalization:**
  ```bash
  ffmpeg -y -i raw_video.mp4 -i narration_master.wav -filter_complex "[1:a]loudnorm=I=-14:LRA=7:tp=-1[aout]" -map 0:v -map "[aout]" -c:v copy -c:a aac -b:a 192k final_video.mp4
  ```
- **Loudness Standard:** Integrated Loudness **-14 LUFS (±1.0)**, True Peak **-1.0 dBFS**.

### 6.3 Quality Assurance Gates (`tools/peak_detail_gate.py`)
Before declaring a render complete, run the automated verification checks:
1. **Freeze Check:** Zero consecutive identical frames during active scenes.
2. **Contrast Ratio:** Text on background must exceed **4.5:1** (WCAG AA).
3. **Decode Test:** FFmpeg full stream decode test with zero corrupt frame errors (`ffmpeg -v error -i video.mp4 -f null -`).

---

## 📦 SECTION 7: UNPACKED DELIVERABLES STANDARD

Whenever a project is completed, the agent must output the following files **unpacked** at the project root and in `delivery/`:

1. `thumbnail_1280x720.jpg` — 16:9 YouTube video thumbnail (bold contrast, high-CTR headline text, <4 words).
2. `cover_vertical_1080x1920.jpg` — 9:16 Shorts/Reels cover frame (centered hero subject, punchy curiosity gap).
3. `title.txt` — Primary click-worthy title + 2 alternative A/B test titles.
4. `description.txt` — Full description with timecoded chapter markers, verified source ledger, and Benaqaab India social links.
5. `hashtags_and_tags.txt` — Search-optimized tags and YouTube hashtags.
6. `headline_captions.srt` — Timecoded subtitle file synchronized to narration audio stems.
7. **Direct Chat Presentation:** In the conversational reply, the AI must explicitly display the thumbnail image and quote the title, description, and key metrics. Never tell the user to unpack a ZIP just to read the title or inspect the thumbnail.

---

## 🚀 SECTION 8: STEP-BY-STEP AI AGENT ACTION PLAYBOOK

When the user asks you to produce a video, follow this exact 11-step execution flow:

```
[User Request / Topic Pick]
         │
         ▼
[Step 1: Check Registry] ──► Verify topic is NOT in Section 3.1 (Covered).
         │
         ▼
[Step 2: Fact Research]  ──► Validate at least 2 primary sources. Build Fact Ledger.
         │
         ▼
[Step 3: Scriptwriting]  ──► Conversational Hinglish. Frame-0 Hook. <20% host time.
         │
         ▼
[Step 4: Voiceover Stem] ──► Generate or measure narration audio. This is MASTER CLOCK.
         │
         ▼
[Step 5: Visual Sourcing]──► Fetch high-res stills & generate AI scene assets.
         │
         ▼
[Step 6: Build comp.html]──► Deterministic HTML5 Canvas/DOM scene with Top-Left logo.
         │
         ▼
[Step 7: 1-GATE PREVIEW] ──► Test comp.html locally. Present preview to USER for approval!
         │                   (DO NOT render MP4 until user says "render the video")
         ▼
[Step 8: Render MP4]     ──► Run hrender.py or FFmpeg. Mux audio at -14 LUFS.
         │
         ▼
[Step 9: QA Audit Gate]  ──► Run peak_detail_gate.py. Inspect decoded frames.
         │
         ▼
[Step 10: Deliverables]  ──► Output unpacked thumbnails, covers, title, description, SRT.
         │
         ▼
[Step 11: Update Record] ──► Append entry to MEMORY.md and move topic to Covered.
```

---

*Benaqaab India — Sach • Saboot • Bebak*  
*Repository: https://github.com/bhattirekha20-dot/benaqaab-india*
