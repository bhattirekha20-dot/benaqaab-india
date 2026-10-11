# 🎬 MASTER IMAGE ASSETS, COMPOSITING & CHAI PROMPTS SPECIFICATION
### SH-12: Delhi Lockdown & The Cockroach Janta Party (CJP) Protest (9:16 YouTube Short)

> **Channel:** Benaqaab India (बेनाक़ाब इंडिया) • `SACH · SABOOT · BEBAK`  
> **Format:** 9:16 Vertical (1080×1920) • **Duration:** 47.30 Seconds  
> **Visual Cadence:** 30 Visual Cuts (1 cut every 1.57s)  
> **Frameworks:** OpenMontage CHAI Framework + Benaqaab Forensic Motion Stack

---

## 📑 TABLE OF CONTENTS
1. [Visual Architecture: Real Source Media vs. Photorealistic AI Scenes](#1-visual-architecture)
2. [Advanced Image Compositing Techniques (Cropping, Floating & Parallax)](#2-advanced-compositing-techniques)
3. [Master CHAI Image Generation Prompts (Beats 01–30)](#3-master-chai-prompts)
4. [Official Source Documents & Internet Media Ingestion List](#4-official-source-media-list)

---

## 1. VISUAL ARCHITECTURE: REAL SOURCE MEDIA VS. AI SCENES

To strictly satisfy `RULE-REAL-SOURCE-PROOF` and `RULE-AUDIO-VISUAL-CAUSAL-LOCKSTEP`:
* **Real Official Source Media (50%):** Actual government gazettes, DMRC metro notices, scanned Form 7 voter deletion objection forms, Supreme Court order transcripts, real satellite maps, and press wire photography of police barricades.
* **Photorealistic AI Stills (50%):** High-tension cinematic reconstructions of moments where direct camera crews were absent (e.g. inside the commercial flight cabin during police boarding, nighttime Delhi border cordons, macro gavel impacts, dramatic youth silhouettes).

---

## 2. ADVANCED COMPOSITING TECHNIQUES (CROPPING, FLOATING & MOTION FX)

### A. Full-Bleed 9:16 Base Layer (Zero Black Pillarboxes)
* Every hero asset is cropped or generated to native **1080×1920 (9:16)**.
* **Virtual Camera Motion:** Slow cinematic push (`scale: 1.0 ➔ 1.06`) or subtle vertical drift (`panY: -15px`) over 1.57 seconds to eliminate static dead frames (`motion_report` freezes = 0).

### B. Floating Glass Evidence Cards & 3D Tilt
* Primary evidence (newspaper headlines, tweets, police circulars) is treated as a **floating obsidian card**:
  - Background: `rgba(15, 23, 42, 0.88)` with `backdrop-filter: blur(16px) saturate(180%)`.
  - Border: `1px solid rgba(255, 255, 255, 0.12)` with high-energy accent stroke (Signal Amber `#FBBF24` or Electric Sky `#38BDF8`).
  - Drop Shadow: `box-shadow: 0 20px 45px rgba(0, 0, 0, 0.8)`.
  - Parallax Float: Subtle sine-wave vertical oscillation (`y = y + 8 * sin(t * 3)`).

### C. The Forensic Loupe 2.5X Crop (Magnifying Glass)
* Used on **Beat 14** (CEC Photo) and **Beat 16** (Form 7 Deletion Checkbox):
  - A circular aperture (`radius = 140px`) crops into the high-resolution source document at **2.5× scale**.
  - Enclosed in an Electric Sky `#38BDF8` specular glass bezel with drop shadow and crosshair reticle lines (`Motion.drawLoupe`).

### D. Dynamic Yellow Highlighter Multiply Overlay
* Used on **Beat 09** (Court Transcript) and **Beat 15** (SIR Gazette):
  - Document text is presented in clean monochrome.
  - As the voiceover speaks the key phrase, an authentic yellow highlighter bar (`#FACC15`) draws horizontally from left to right using `ctx.globalCompositeOperation = 'multiply'` with procedural ink fiber bleed.

### E. Alpha Subject Cutouts & Multi-Layer Depth
* Extract foreground subjects (e.g. activist silhouette, police officer, Supreme Court gavel) using SAM 2 or alpha masks:
  - **Background Layer (Z = 0):** Blurred documentary backdrop (Jantar Mantar / Airport tarmac).
  - **Middle Layer (Z = 1):** Floating evidence document or rolling counter.
  - **Foreground Layer (Z = 2):** Cutout subject with subtle rim glow (`drop-shadow(0 0 16px rgba(...))`), creating an illusion of 3D spatial depth.

### F. Slamming Forensic Rubber Stamp
* Used on **Beat 27** (`DISPROPORTIONATE FORCE!`):
  - Enters at `scale: 1.6`, slams down to `1.0` with a **120ms spring settle** and camera trauma shake (`intensity = 0.04`).
  - Angled at `-7°`, colored in Crimson Flame `#EF4444` with distressed rubber ink texture.

---

## 3. MASTER CHAI IMAGE GENERATION PROMPTS (9:16 VERTICAL)

Below are the detailed, production-grade CHAI prompts (Camera, Hyper-detail, Aesthetics, Illumination) for key scenes:

---

### Beat 01 | `00:00 – 01.57s`
* **Filename:** `ai_01_locked_delhi_metro_gate.jpg`
* **Scene Context:** The opening hook. Shuttered Delhi Metro station entrance locked with heavy steel chains and yellow caution tape as confused commuters look on.
* **Aspect Ratio:** `9:16`
* **CHAI Prompt:**
  > **[Camera]:** Eye-level medium-wide vertical shot, 35mm f/2.0 anamorphic cinema lens, shallow depth of field focusing sharply on the locked turnstile gates.  
  > **[Hyper-Detail]:** Modern Delhi Metro station entrance sealed shut. Heavy industrial stainless steel shutter pulled down with yellow barricade tape reading "ENTRY RESTRICTED - DMRC ADVISORY". Commuters in business and student attire stranded outside in soft morning haze. Polished granite station floor reflecting red overhead warning signals.  
  > **[Aesthetics]:** Gritty investigative documentary aesthetic, high-contrast chromatic palette, deep obsidian shadows, realistic architectural metal textures, zero AI cartoonishness.  
  > **[Illumination]:** Cold morning blue ambient daylight contrasted against harsh red station beacon emergency glow, dramatic rim light on steel shutter slats.  
  > **[Negative Prompt]:** Cartoon, 3D render, flat, blurry, low resolution, warped hands, unrealistic metro signs, oversaturated purple colors.

---

### Beat 03 | `03.15 – 04.72s`
* **Filename:** `ai_03_delhi_police_border_barricade.jpg`
* **Scene Context:** 25,000 security personnel mobilization. Multi-tier steel barricades and Rapid Action Force personnel deployed at Delhi borders.
* **Aspect Ratio:** `9:16`
* **CHAI Prompt:**
  > **[Camera]:** Low-angle vertical shot, 50mm f/1.8 lens, cinematic perspective emphasizing the sheer depth of multi-tier police barricades stretching along the highway.  
  > **[Hyper-Detail]:** Delhi Police and Rapid Action Force (RAF) officers in protective riot gear, ballistic vests, and helmets standing in formation. Heavy yellow iron barricades with concertina razor wire coiled along the top. Armored water cannon vehicle visible in the foggy background. Paved road with painted lane markers.  
  > **[Aesthetics]:** Serious news journalism photography, photorealistic documentary realism, desaturated slate and asphalt tones with punchy yellow barricade accents.  
  > **[Illumination]:** Misty morning light diffused through Delhi winter haze, flashing blue and red emergency police LED lights casting sharp specular reflections on riot shields and wet tarmac.  
  > **[Negative Prompt]:** Fantasy soldiers, video game look, plastic textures, exaggerated faces, oversaturation, text watermarks.

---

### Beat 04 | `04.72 – 06.30s`
* **Filename:** `ai_04_inflight_police_cabin_arrest.jpg`
* **Scene Context:** Police boarding a passenger aircraft cabin at Delhi Airport to detain the CJP convenor straight off the flight.
* **Aspect Ratio:** `9:16`
* **CHAI Prompt:**
  > **[Camera]:** Over-the-shoulder vertical interior shot inside a narrow aircraft cabin aisle, 28mm f/2.8 lens, cinematic high-tension framing.  
  > **[Hyper-Detail]:** Interior of a commercial narrowbody passenger airplane. Two uniformed Delhi Police officers with radio badges standing in the narrow carpeted aisle speaking calmly to a young seated passenger. Overhead luggage bins closed, reading lights illuminating anxious passenger faces turning around in their seats.  
  > **[Aesthetics]:** High-stakes investigative thriller realism, claustrophobic spatial tension, authentic aircraft cabin interior details (seat fabric, seatbelt buckles, aisle carpeting).  
  > **[Illumination]:** Warm interior aircraft cabin downlights contrasted with bright white daylight flooding through small airplane window portals.  
  > **[Negative Prompt]:** Flying plane exterior, cartoon passengers, distorted aircraft interior, blurry faces, surreal lighting.

---

### Beat 06 | `07.88 – 09.45s`
* **Filename:** `ai_06_cjp_emblem_neon_cockroach.jpg`
* **Scene Context:** The official symbol of the Cockroach Janta Party (CJP) emerging from dark shadows.
* **Aspect Ratio:** `9:16`
* **CHAI Prompt:**
  > **[Camera]:** Macro frontal vertical studio shot, 85mm f/1.4 portrait lens, centered symmetrical composition.  
  > **[Hyper-Detail]:** High-tech stylized metallic emblem of a resilient cockroach holding a glowing protest torch. Brushed titanium and obsidian carbon fiber texture, precision laser-etched antennae and chitin plates. Subtle gold and amber circuit lines etched across the exoskeleton.  
  > **[Aesthetics]:** Cyber-investigative branding, dark chromatic slate `#0A0D14` background with volumetric smoke particles, ultra-premium emblem craftsmanship.  
  > **[Illumination]:** Vibrant Signal Amber `#FBBF24` backlight bloom, edge specular highlights glinting off polished metallic surfaces, volumetric rim lighting.  
  > **[Negative Prompt]:** Disgusting insect photo, messy drawing, cartoon mascot, low poly, cheap clip art.

---

### Beat 10 | `14.18 – 15.76s`
* **Filename:** `ai_10_gen_z_student_march_delhi.jpg`
* **Scene Context:** Thousands of university students and exam aspirants marching peacefully with placards.
* **Aspect Ratio:** `9:16`
* **CHAI Prompt:**
  > **[Camera]:** Ground-level dynamic vertical tracking shot, 35mm f/2.0, walking forward with the crowd.  
  > **[Hyper-Detail]:** Sea of Indian college students and young professionals marching in peaceful unison along a wide New Delhi boulevard. Diverse young people carrying cardboard protest signs, smartphones recording video, and college backpacks. Iconic tree-lined Lutyens Delhi avenue in the background.  
  > **[Aesthetics]:** Authentic photojournalism style, raw energy of youth democracy, natural skin tones, high dynamic range clothing details.  
  > **[Illumination]:** Natural overcast daylight filtering through tree canopies, subtle volumetric sun shafts cutting through Delhi air.  
  > **[Negative Prompt]:** Violence, riots, fire, cartoon students, duplicate identical faces, fake CGI look.

---

### Beat 14 | `20.48 – 22.06s`
* **Filename:** `ai_14_cec_gyanesh_kumar_press_room.jpg`
* **Scene Context:** Chief Election Commissioner Gyanesh Kumar at a formal Election Commission press conference.
* **Aspect Ratio:** `9:16`
* **CHAI Prompt:**
  > **[Camera]:** Telephoto portrait shot, 135mm f/2.8 lens, focused sharply on the official briefing desk with shallow depth of field.  
  > **[Hyper-Detail]:** Formal press conference setting at Nirvachan Sadan. Senior bureaucratic dignitary seated behind a wooden desk lined with press microphones carrying prominent news channel tags. Official green and gold emblem of India backdrop. Document folder and glasses on the desk.  
  > **[Aesthetics]:** High-end editorial political photography, authentic institutional gravitas, razor-sharp suit fabric and microphone foam textures.  
  > **[Illumination]:** Bright multi-angle television broadcast studio key lights, soft fill lighting, crisp specular reflections on microphone metal grilles.  
  > **[Negative Prompt]:** Caricature, comedic face, distorted hands, blurry logos, fantasy courtroom.

---

### Beat 22 | `33.08 – 34.66s`
* **Filename:** `ai_22_smartphone_internet_suspension.jpg`
* **Scene Context:** Modern smartphone held in hand showing government network suspension notice.
* **Aspect Ratio:** `9:16`
* **CHAI Prompt:**
  > **[Camera]:** Extreme close-up first-person POV shot, 50mm f/1.8 macro lens, phone screen filling 70% of the vertical frame.  
  > **[Hyper-Detail]:** Hand holding a sleek smartphone in central Delhi. Screen displaying a real-looking system push alert: "Mobile Internet & Data Suspended by Department of Telecommunications under BNSS Section 163". Zero signal bars on status bar. Blurred Delhi street and police vehicle siren lights visible in the bokeh background.  
  > **[Aesthetics]:** Photorealistic modern tech editorial, crisp OLED screen glass reflections, subtle fingerprint smudges on glass for realism.  
  > **[Illumination]:** Glowing screen OLED backlight illuminating fingers and palm, contrasted with moody twilight ambient lighting outside.  
  > **[Negative Prompt]:** Broken phone screen, cartoon UI, generic stock photo hand, blurry text.

---

### Beat 26 | `39.38 – 40.96s`
* **Filename:** `ai_26_supreme_court_bench_gavel_impact.jpg`
* **Scene Context:** The historic judicial rebuke: *"A hammer should not be used to kill a fly!"*
* **Aspect Ratio:** `9:16`
* **CHAI Prompt:**
  > **[Camera]:** Low-angle dramatic vertical shot, 50mm f/1.4 lens, freezing the moment of judicial authority.  
  > **[Hyper-Detail]:** Heavy polished mahogany judge's gavel striking a brass sounding block on the bench of the Supreme Court of India. Minute dust particles frozen in mid-air above the strike point. Stacks of bound legal petitions, law ledgers, and Ashoka lion brass emblem blurred in the dignified wood-paneled courtroom background.  
  > **[Aesthetics]:** Regal constitutional documentary authority, deep rich walnut wood tones, golden brass highlights, ultra-fine polished lacquer reflections.  
  > **[Illumination]:** Dramatic directional beam of golden courtroom light illuminating the gavel head, deep cinematic chiaroscuro shadows across the bench.  
  > **[Negative Prompt]:** Cartoon mallet, courtroom fire, fantasy courtroom, oversaturated colors, flat lighting.

---

## 4. OFFICIAL SOURCE DOCUMENTS & INTERNET MEDIA INGESTION LIST

For maximum journalistic credibility (`RULE-REAL-SOURCE-PROOF`), gather the following 7 real primary source assets from verified internet archives:

1. **DMRC Official Passenger Advisory:** Scanned notice/tweet announcing temporary closure of 45 metro stations on 10 Oct 2026.
2. **Delhi Police Section 163 BNSS Order:** Official prohibitory order notification issued for New Delhi District / Jantar Mantar.
3. **ECI Special Intensive Revision (SIR) 2026 Gazette:** Scanned title page of the Election Commission directive on electoral roll cleanup.
4. **Election Commission Form 7 Application:** Clean official scan of the "Application for Objection to Proposed Inclusion / Deletion of Name in Existing Electoral Roll".
5. **Nirvachan Sadan Exterior:** High-resolution architectural photo of the Election Commission of India headquarters on Ashoka Road.
6. **Supreme Court of India Courtroom Facade:** Official archival photograph of the Chief Justice courtroom and apex dome.
7. **Northern Railway Advisory:** Official cancellation notice of Mail/Express trains into New Delhi & Hazrat Nizamuddin stations.
