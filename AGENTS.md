# 🛡️ AGENTS.md — Benaqaab India Universal AI Operating Directive

> **AUTHORITY:** This directive is the supreme operational governance document for ALL AI models, agents, and IDEs (including Claude, Gemini, GPT, DeepSeek, Cursor, Codex, Devin, and Antigravity) operating in this workspace.  
> **CHANNEL:** Benaqaab India (बेनाक़ाब इंडिया) • **TAGLINE:** `SACH · SABOOT · BEBAK` (Truth · Evidence · Uncompromising)  
> **STATUS:** Mandatory & Non-Negotiable.

---

## 🚨 ARTICLE 1: THE ANTI-DUMP LAW (STRICT CONTEXT BUDGET)

### 1.1 Never Copy Or Ingest The Full Repository
- **DO NOT attempt to copy, clone, download, or dump the entire repository into your workspace, active prompt, or subagent context.**
- **DO NOT attempt to read multi-megabyte files in full all at once.**
- Ingesting giant files causes immediate context window exhaustion, token truncation, catastrophic forgetting of system instructions, hallucinated APIs, and degraded "AI-slop" outputs.

### 1.2 Multi-Megabyte Files — Strict Access Rules
The following files must **NEVER** be ingested in bulk:
1. `BENAQAAB_AI_AGENT_MASTER_SKILL.md` (3.16 MB / 45,560 lines): **NEVER read in full.** It is an archive. Use the `§INDEX` at the end of `BENAQAAB_AI_AGENT_COMPACT.md` to look up specific appendices only when needed.
2. `MASTER_VIDEO_GENERATION_SKILLS.md` (1.69 MB / 36 chapters): **NEVER read in full.** Query specific chapters on demand using targeted search.
3. `PROMPT_LIBRARY_opus55.md` (650 KB): Historical prompt archive. Consult specific reference prompts only when targeted.
4. `MEMORY.md` (516 KB): Production history. **Read only the tail (last 100–200 lines)** for recent state, or use `grep_search` for specific case IDs.

---

## 🔄 ARTICLE 2: THE ITERATIVE ON-DEMAND READING PROTOCOL

### 2.1 The "Come Back Again And Again" Mandate
- You are **explicitly authorized and commanded** to come back repeatedly as many times as needed to read, inspect, and deeply understand specific sections before taking any action.
- There is **zero penalty** for making 5, 10, 15, or 20 targeted read operations. Quality requires deep comprehension.
- Never guess, extrapolate, or hallucinate a rule when you can inspect the exact code or documentation.

### 2.2 Surgical Inspection Tools
Always use precision tools rather than bulk dumps:
- **`view_file` with Line Ranges:** Specify `StartLine` and `EndLine` to read 100–300 lines at a time.
- **`grep_search`:** Search for exact rule identifiers (e.g., `RULE-MASTER-CLOCK`, `RULE-LOGO-TOPLEFT`), function names (`seek(t)`, `motion_report`), or topic IDs.
- **Surgical Reading Order for Any Task:**
  1. Check topic status in `CENTRAL_TOPICS_MASTER.md` or `MASTER_AGENT_DISPATCH.md`.
  2. Read operational guidelines in `BENAQAAB_AI_AGENT_COMPACT.md` (§1–§4).
  3. Inspect forensic motion primitives in `BENAQAAB_FORENSIC_MOTION_SYSTEM.md`.
  4. Inspect reference compositions in `projects/` (e.g., `projects/upi_explained_short/`).

---

## 🎬 ARTICLE 3: THE OPUS 5.5 INTELLIGENCE LEVEL VIDEO ENGINE STANDARD

All video productions in this workspace must meet the intelligence and visual craftsmanship standard demonstrated by Claude Opus 5.5 code-rendered motion graphics (`MOTION_RESEARCH_Opus55.md`).

### 3.1 Every Frame Is Rendered From Code
- **No Stock Footage & No AI Video Hallucinations:** Videos are NOT generated via text-to-video generators (Kling, Runway, Veo) where text garbles and logic fails.
- Every single frame is rendered from deterministic code (HTML5 Canvas 2D, WebGL, procedural SVG, and CSS) through headless Chromium via `viz/hrender.py`.
- **The Absolute Time Contract:** The composition must implement `window.seek(t)`. Every transform, opacity, mask, loupe, and counter must be reproducible when seeking to any arbitrary timestamp $t$. Never rely on uncontrolled CSS timers, `setInterval`, or accumulated physics drift.

### 3.2 The Opus 5.5 Vector Law & Kinetic Choreography
1. **Continuous Acceleration & Deceleration:**
   - Use premium physics easing: `cubic-bezier(0.16, 1, 0.3, 1)` or critically damped spring physics.
   - Strictly avoid amateur linear transitions, repeated rubber-band bounces, or elastic overshoots.
2. **Motion at Three Scales Simultaneously (Zero Dead Frames):**
   - **Macro Scale:** Dynamic Virtual Camera (continuous cinematic pan, zoom/dolly, subtle tilt, and trauma-decay camera shake on impact).
   - **Meso Scale:** Structural mechanism transforms (odometer digits rolling, highlighter drawing, loupe lens floating, match-cut morphs).
   - **Micro Scale:** Ambient living texture (subtle particle drift, glowing scanlines, procedural SVG noise grain at 3–4% opacity to eliminate gradient banding).
   - A video that animates and then holds completely still is an automatic failure (`motion_report` freezes = 0).
3. **Opus 5.5 Continuity Law:**
   - Match-position transitions: hero elements retain identity and positional continuity across scene cuts.
   - Outgoing typography and graphics must clear before incoming elements occupy the space. Never overlap competing headlines.

### 3.3 The Benaqaab Forensic Journalism Stack (Dhruv Rathee / Vox / Johnny Harris Style)
Every explainer and documentary must implement the 5 Forensic Motion Primitives defined in `BENAQAAB_FORENSIC_MOTION_SYSTEM.md`:
1. **Data-to-DOM Fact Ledger:** Every metric, rupee figure, percentage, or date drawn on screen MUST be dynamically bound to a structured `FACT_LEDGER` object. Magic numbers in canvas text are forbidden.
2. **Authentic Yellow Highlighter:** Document and newspaper inspection using `ctx.globalCompositeOperation = 'multiply'` (hex `#FFE600` or `#FACC15`) with procedural ink bleed and fiber edges.
3. **Forensic Loupe (Magnifying Glass):** 2.2× to 3.0× circular magnification with specular glass bezel (`rgba(255, 255, 255, 0.25)`), drop shadow, and crosshair reticle inspecting primary evidence.
4. **Redaction Peel & Reveal:** Black government redaction bars peeling back with paper tear sound design cues to reveal covered truths.
5. **Verdict Stamp & Odometer:**
   - Tabular monospace metric counters (`JetBrains Mono`) rolling smoothly with ease-out deceleration.
   - High-impact angled forensic stamp (*"CONFIRMED"*, *"BOGUS"*, *"DEBUNKED"*) with 120ms spring settle and camera trauma shake.
6. **Real Source Media + Photorealistic AI Art:**
   - Anchor every beat in authentic source media: gazettes, PIB releases, balance sheets, RTI replies, press clippings, and maps.
   - Pair with curated, photorealistic AI illustrations. Never produce sterile, empty geometric diagrams.

### 3.4 Visual Density, Hyper-Pacing & Glowing Images Law (`RULE-VISUAL-DENSITY-AND-GLOW`)
1. **Mandatory Visual Density Ratios:**
   - 🎬 **Long-Form Videos (16:9 Documentary/Explainer):** **At least 10 AI images / visual assets per 1 minute of video** (shot length ≤ 5.5–6.0s).
     - *3-minute video:* Minimum **30 visual assets**.
     - *5-minute video:* Minimum **50 visual assets**.
     - *10-minute documentary (like EP-17 PFBR):* Minimum **100–105 distinct visual beats**.
   - 📱 **Short-Form Videos / YouTube Shorts / Reels (9:16):** **At least 30 AI images / visual cuts per Short** (hyper-retention cadence: 1 image cut every 1.5 to 2.0 seconds). A static Short that holds 1 image for 5+ seconds is an automatic retention failure.
2. **Volumetric Glowing Aesthetics ("Glowing Images Standard"):**
   - Enable and encourage **glowing visual effects wherever appropriate**:
     - **Specular Rim Glows:** High-contrast edge rim light on hero subjects (`filter: drop-shadow(0 0 18px rgba(...))` or canvas `shadowBlur`).
     - **Volumetric Ambient Bloom:** Backlight diffusion, glowing volumetric orbs, and lens highlight blooms.
     - **Forensic Energy Accents:** Electric Sky `#38BDF8` (space/tech/AI), Signal Amber `#FBBF24` (money/gold/economy), Crimson Flame `#F43F5E` (crime/scams/exposés), Neon Mint `#34D399` (energy/infra).
3. **Deep Visual Reasoning ("Think Yourself" Mandate):**
   - Never generate arbitrary or decorative filler. Every visual asset must have **causal narrative purpose** directly matched to the voiceover word-clock.
   - The AI must think intentionally: plan camera angles, micro-contrast, depth of field, and storytelling impact.

### 3.5 Audio Master Clock Law
- Voiceover narration (Hindi/Hinglish) is the **absolute master clock** of the entire film.
- Visual scenes, cuts, counters, and highlights must be timed to word-level audio timestamps.
- Audio master must measure **-14 LUFS (±1.0 LUFS)** integrated loudness with True Peak **≤ -1.0 dBFS**.

---

## 💎 ARTICLE 4: THE "BEST THING DONE" LAW (ZERO AI SLOP)

Every output produced by an AI agent must be production-ready, fully resolved, and visually stunning.

### 4.1 Zero AI Slop Directive
- **NO Generic Purple Gradients on Flat Black:** Use deep chromatic slate/obsidian (`#07090E`, `#0A0D14`) paired with frosted glass surfaces (`rgba(15, 20, 32, 0.7)`), 1px specular borders, and high-energy accents (Electric Sky `#38BDF8`, Crimson Flame `#F43F5E`, Signal Amber `#FBBF24`).
- **NO Unstyled Placeholder Divs or "Lorem Ipsum":** Every asset, headline, fact, source attribution, and label must be real, sourced, and dated.
- **NO Half-Baked MVPs:** When asked to create or update a video, produce the complete, working, interactive `comp.html` file with all assets, logic, and audio synchronizers.

### 4.2 Typography & Language Standards
- **Font Hierarchy:**
  - Display Headlines: *Outfit*, *Syne*, or *Playfair Display* (bold, authoritative).
  - Body & Explanations: *Inter* or *Plus Jakarta Sans* (maximum legibility).
  - Metrics & Data: *JetBrains Mono* (tabular figures for rolling counters).
- **Hindi Text Fit Rule:** Devanagari text expands wider than Latin at identical font sizes. Always compute bounding boxes and apply auto-fit scaling (`.fit`) or explicit wrapping so text NEVER clips or overflows safe zones.

### 4.3 Brand Placement Standard
- **Logo Asset:** `brand/logo.png`.
- **Placement:** **Top-Left Safe Area (`RULE-LOGO-TOPLEFT`)** inside a frosted dark pill with subtle gold border glow. (Top-right placement is strictly obsolete).

### 4.4 Gate 0: Format & Duration Confirmation Law (`RULE-FORMAT-DURATION-GATE`)
**Whenever a video topic is chosen** (whether provided by the user, selected from `CENTRAL_TOPICS_MASTER.md`, or proposed by the AI):
- **NEVER assume or guess the format or duration.**
- **The AI MUST PAUSE and explicitly ask the user two questions before proceeding to scriptwriting:**
  1. **Video Format:**
     - 🎬 **Long Video / Documentary** (16:9 Landscape widescreen)
     - 📽️ **Short Explainer Film** (16:9 or 9:16)
     - 📱 **YouTube Short / Reel** (9:16 Vertical mobile)
  2. **Target Duration:**
     - What exact target duration is desired? (e.g., 30s–60s micro-short, 60s–120s extended short, 3m–5m explainer, 10m+ documentary).
- **Only AFTER the user confirms their preferred format and duration** may the agent proceed to Step 1 (Research & Fact Ledger) and Step 2 (Script & Audio).

### 4.5 The Production & 1-Gate Approval Pipeline
Follow this unskippable pipeline:
```
[0. Topic Pick ➔ ASK Format & Duration] ➔ [1. Research & Fact Ledger] ➔ [2. Script & Audio Lock]
                                                                                │
[6. Master MP4 Render] 🠄 [5. Human Approval Gate] 🠄 [4. Browser QA] 🠄 [3. comp.html Preview]
```
- **STOP at Step 0:** Ask and confirm format + duration before drafting.
- **STOP at Step 5:** Present the interactive `comp.html` preview to the user. Never render the final broadcast MP4 until the user explicitly says *"render"* or approves the composition.
- **Unpacked Deliverables:** Deliver all title options, description copy, hashtags, pinned comments, and thumbnail briefs directly in the response—never hide them inside ZIP archives.

---

## 🗺️ ARTICLE 5: SURGICAL FILE NAVIGATION MAP

Use this map to locate exact operational rules without loading whole files:

| Task / Topic | Target File | What to Inspect |
|---|---|---|
| **Pipeline & Standing Rules** | `BENAQAAB_AI_AGENT_COMPACT.md` | §1 (Overview), §2 (Laws), §4 (11-Step Pipeline), §14 (QA Gates) |
| **Forensic Primitives & Boilerplate** | `BENAQAAB_FORENSIC_MOTION_SYSTEM.md` | §2 (Pipeline), §3 (Fact Ledger), §4 (5 Primitives), §7 (`comp.html` boilerplate) |
| **Opus 5.5 Motion Techniques** | `MOTION_RESEARCH_Opus55.md` | §0 (Core Finding), §1.4 (Spotify Prompt Rules), §2 (Timeline math) |
| **Topic Status & Registry** | `CENTRAL_TOPICS_MASTER.md` | Check before picking any topic (never repeat covered topics) |
| **Brand DNA & Colour Profiles** | `MASTER_AGENT_DISPATCH.md` | §1 (Brand), §4 (20 Laws), §5 (Colour Profiles A, B, C) |
| **Visual Asset Ledger** | `VISUAL_ASSET_MASTER_LEDGER.md` | Mapping of 248 visual assets, provenance, and usage rules |
| **Shorts Retention & Hooks** | `SKILLS_SHORTS_CURIOSITY.md` | 1-Second Frame-0 Law, Kallaway hook archetypes, caption pills |
| **Recent Production Lessons** | `MEMORY.md` | Inspect tail (last 100–200 lines) for latest state and learnings |
| **Reference Explainer Film** | `projects/upi_explained_short/` | `UPI_Explained_Short.html`, `SCRIPT.md`, `SOURCES.md` |
| **Reference Edit Film** | `projects/anime_edit/` | `Anime_Edit.html`, `BEATS.json` |

---

## ⚖️ SUMMARY FOR EVERY AGENT INVOCATION

1. **Context Discipline:** Do not dump the repository. Read surgically.
2. **Iterative Visits:** Return as many times as necessary to understand the exact requirements.
3. **Opus 5.5 Motion:** Render every frame from code (`seek(t)`), apply continuous acceleration, and layer 3-scale motion.
4. **Forensic Integrity:** Ground every figure in the `FACT_LEDGER`, use authentic source documents with yellow highlighter overlays, and keep VO as the master clock.
5. **Best Thing Done:** Never output AI slop. Deliver fully finished, verified, broadcast-grade work.
