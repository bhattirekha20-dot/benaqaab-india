# 🧭 DIRECTIVE: 5-6s ROADMAP HOOK, WHAT-AND-USE ARCHITECTURE & MOTION IMAGE ANNOTATION
### Mandatory Operating Protocol for All Benaqaab India Video Compositions
> **Motto:** `SACH · SABOOT · BEBAK` (Truth · Evidence · Uncompromising)  
> **Status:** Active Operational Law (`RULE-5SEC-ROADMAP` · `RULE-WHAT-AND-USE` · `RULE-IMAGE-ANNOTATION`)  
> **Audience:** Lead AI Video Director & All Future AI Agents  
> **Reference Production:** [`projects/test_what_and_use/comp.html`](projects/test_what_and_use/comp.html)

---

## 🎯 SECTION 1: THE THREE FOUNDATIONAL LAWS

Whenever an AI agent produces a video for Benaqaab India, it MUST strictly implement these three rules:

```
┌────────────────────────────────────────────────────────────────────────┐
│             BENAQAAB EXPLAINER THREE-PILLAR LAW                        │
├─────────────────────────┬──────────────────────────────────────────────┤
│ 1. 5-6s ROADMAP HOOK    │ Opening 5.5s must outline the 3 key points   │
│    (RULE-5SEC-ROADMAP)  │ covered in the video with an animated card.  │
├─────────────────────────┼──────────────────────────────────────────────┤
│ 2. WHAT IS IT & USE     │ Every video must deeply answer:              │
│    (RULE-WHAT-AND-USE)  │ • Part 1: Kya hai yeh? (Definition)          │
│                         │ • Part 2: Iska real use kya hai? (Impact)    │
├─────────────────────────┼──────────────────────────────────────────────┤
│ 3. MOTION IMAGE PINS    │ Never show static photos. Explain images     │
│    (RULE-IMAGE-ANNOT)   │ using callout pins, 2X loupe & highlighters. │
└─────────────────────────┴──────────────────────────────────────────────┘
```

---

## ⏱️ SECTION 2: THE 5-6s ROADMAP HOOK (`0.0s – 5.5s`)

### 2.1 Spoken Cadence (Script Rule)
At the very start of the script, the voiceover must clearly establish what the viewer will learn in under 6 seconds:
> *"Iss video mein hum cover karenge: [Topic] — yeh aakhir kya hai, iska real-world use kya hai, aur kaise yeh [Impact] create karta hai. Saboot ke saath."*

### 2.2 Visual Choreography (Canvas / DOM Rule)
* **HUD Card Stack:** Display a 3-point structured preview card:
  1. `01. WHAT IS IT?` (`यह आखिर क्या है?`)
  2. `02. HOW IT WORKS?` (`काम कैसे करता है?`)
  3. `03. REAL-WORLD USE` (`इसका असली इस्तेमाल क्या है?`)
* **Sequential Activation:** Each step illuminates with an active cyan pill (`#38bdf8`) and transitions to a green checkmark (`#10b981`) as the speaker mentions it.

---

## 🔬 SECTION 3: "WHAT IS IT & WHAT IS ITS USE?" DEEP DIVE

Every topic—whether microchips, digital gold, space technology, or government schemes—must be broken down into two distinct parts:

### Part 1: "Kya Hai Yeh?" (What Is That Thing?) — `5.5s – 25.0s`
* **Goal:** Demystify the concept completely without confusing jargon.
* **Mechanism:**
  - Show a real, high-resolution primary-source image, macro die, or official gazette document.
  - Explain the physical foundation (e.g. silicon wafer, gold bar, satellite orbit).
  - Show the microscopic or structural mechanism (e.g. binary switching 0 and 1).

### Part 2: "Iska Real Use Kya Hai?" (What Is Its Use?) — `25.0s – 44.0s`
* **Goal:** Connect the technology to the viewer's everyday life and national reality.
* **Mechanism:**
  - Break down at least 3 concrete real-world use cases (e.g. smartphones, electric cars, national defense).
  - Roll a live numerical odometer metric (e.g. 1,500 to 3,000 chips per car; 1 Trillion chips per year).
  - Explain the consequence if this thing ceases to exist (e.g. global factories halt).

---

## 🖼️ SECTION 4: EXPLAINING IMAGES WITH MOTION GRAPHICS

It is strictly forbidden to display a plain, static image on screen with dead air. **Every image must be explained using motion graphics:**

### 1. `Motion.drawCalloutPin` (Animated Callout Pointer & Badge)
Draws an animated reticle on the exact feature of the image, extends a spring-damped dashed elbow line, and pops a frosted glass info badge:
```javascript
Motion.drawCalloutPin(
  ctx, t, startT,
  targetX, targetY,  // Feature coordinates inside image
  elbowX, elbowY,    // Where the badge sits
  'NANO-SCALE DIE GRID',
  '100 Arab Transistors ek single chip par',
  '#38bdf8'
);
```

### 2. `Motion.drawEvidenceLoupe` (2X Reticle Lens)
Zooms into the critical detail inside the image with crosshairs and a verification tag:
```javascript
Motion.drawEvidenceLoupe(ctx, t, 7.0, centerX, centerY, radius = 90, zoom = 2.0);
```

### 3. `Motion.drawHighlighter` (Gazette Highlighter Sweep)
Underlines technical specifications, law sections, or numbers on document images using multiply blend mode:
```javascript
Motion.drawHighlighter(ctx, t, 18.0, 1.2, x, y, width, height, 'rgba(250, 204, 21, 0.45)');
```

### 4. `Motion.drawOdometer` (Rolling Metric Counter)
Animates statistics dynamically rather than presenting static text:
```javascript
Motion.drawOdometer(ctx, t, 33.5, 2.5, 0, 3000, '', ' CHIPS', cx, cy);
```

### 5. `Motion.drawVerdictStamp` & `ForensicAudio.playStampThud`
Slam a rubber verdict stamp with physical screen shake and sub-bass audio shockwave to conclude the investigation:
```javascript
Motion.drawVerdictStamp(ctx, t, 48.0, 'STRATEGIC ASSET', 'MODERN DUNIYA KA OXYGEN', cx, cy);
```

---

## 🧪 SECTION 5: TEST SUITE & RUNNABLE BLUEPRINT

The canonical working prototype is located in:
* **Interactive Player:** [`projects/test_what_and_use/comp.html`](projects/test_what_and_use/comp.html)
* **Script & Breakdown:** [`projects/test_what_and_use/SCRIPT.md`](projects/test_what_and_use/SCRIPT.md)
* **Data Ledger:** [`projects/test_what_and_use/FACT_LEDGER.json`](projects/test_what_and_use/FACT_LEDGER.json)
* **Asset Manifest:** [`projects/test_what_and_use/ASSET_MANIFEST.md`](projects/test_what_and_use/ASSET_MANIFEST.md)
* **16:9 Thumbnail:** [`projects/test_what_and_use/thumbnail_1280x720.jpg`](projects/test_what_and_use/thumbnail_1280x720.jpg)
* **9:16 Vertical Cover:** [`projects/test_what_and_use/cover_vertical_1080x1920.jpg`](projects/test_what_and_use/cover_vertical_1080x1920.jpg)

---

## ⚡ SECTION 6: THE UNIVERSAL 10-VISUALS-PER-MINUTE LAW (`RULE-10-VISUALS-PER-MINUTE`)

> **MANDATORY PRODUCTION METRIC FOR ALL AI AGENTS & ALL TOPICS:**  
> **1 Minute of Video = At Least 10 Distinct Visual Beats** (1 new visual every 5.5 to 6.0 seconds).  
> **Longform Documentaries (e.g., 10m29s PFBR preview):** 10 beats/min = **roughly 105 distinct visuals**.

### 6.1 Why 10 Visuals Per Minute? (Retention Psychology)
* Holding a single static visual for 15–20 seconds causes severe viewer drop-off and visual boredom.
* Modern high-retention investigative documentaries (Dhruv Rathee, Vox, Johnny Harris) maintain an average **shot length (ASL) of 5 to 6 seconds**.
* Every sentence or sub-point must introduce a fresh visual stimulus, keeping the viewer's brain actively engaged.

### 6.2 What Counts Toward the 10 Visuals? (The Mixed-Media Arsenal)
Never rely on just one kind of graphic. Every minute must weave together a **balanced mixed-media portfolio**:
1. **Photorealistic Forensic AI Macro Photography:** Silicon ingots, reactor cores, turbine halls, microscopic transistor gates.
2. **Primary-Source Official Documents:** Gazette notifications, RTI disclosures, court orders, parliamentary replies with yellow highlighter sweeps.
3. **Engineering Schematics & Cutaways:** Blueprints, architectural elevations, car ECU boards, and satellite wireframes with animated callout pins.
4. **Data Visualizations & Live Tickers:** Live rolling odometers, financial charts, and timeline milestone tracks.
5. **Geopolitical & Supply Chain Maps:** Holographic route maps highlighting straits, chokepoints, and trade corridors.
6. **Optical Loupe Reticle Inspections:** 2X macro zoom lens circling serial numbers, hallmarks, or micro-components.
7. **Verified Editorial News Stills:** Real, authentic photographs from PIB, official registries, or court archives.
8. **Kinetic Typography HUDs:** Roadmap cards, metric cards, and rubber verdict stamps.

---

*Benaqaab India — Sach • Saboot • Bebak*
