# 🎯 FIRST-SECOND CURIOSITY & SHORTS RETENTION ENGINE (2026-10-01)

> **Permanent Benaqaab India skill file — NEVER DELETE.**
> Distilled from 7 cloned & verified GitHub repositories (studied 1 Oct 2026) so every YouTube Short answers **"Why am I watching this?"** in the **very first second** and holds curiosity until the final frame.

---

## 1. VERIFIED GITHUB REPOSITORIES STUDIED (1 Oct 2026)

| Repository | What It Contains | Core Technique Adopted |
|---|---|---|
| **`vyralcontent/content-skills`** | Distilled patterns from **200,000+ viral Shorts, Reels & TikToks** (`viral-hooks`, `viral-youtube-shorts`, `viral-short-form`, `three-layer-hook.md`, `hook-archetypes.md`, `hook-tactics.md`, `shorts-retention.md`) | **The 3-Layer Frame-0 Hook** (Visual + Verbal + Sharpener Text), Kallaway's 6 archetypes, **Shaped Curiosity Gaps**, VVSA diagnostics |
| **`nateherkai/hyperframes-student-kit`** | `short-form-edit/references/curiosity-and-entertainment.md`, `quality-gates.md`, `STORYTELLING-WORKBOOK.md`, `style-library/02-kallaway/DESIGN.md` | **Priority-1 Gate** (*"In the first 3 seconds is someone convinced they need to watch until the end?"*), **`OPEN-LOOPS.json` ledger**, **Unresolved Visual State (Empty Sockets / Wall-of-Slots)** |
| **`sergebulaev/youtube-skills`** | `yt-hook-scripter`, `references/hook-formulas.md` (Y1–Y11), `algorithm-heuristics.md` | **Y10 Frame-One Shorts Hook**, odd-precision numbers, Restate-and-Raise, zero-intro law |
| **`AgriciDaniel/claude-youtube`** | `references/shorts-playbook.md`, `references/retention-scripting-guide.md` | **Suspension-Bridge (Open-Loop) Scripting (+68% completion)**, Sawtooth pattern interrupts (+43% completion), Explore→Exploit VVSA gates |
| **`iart-ai/tiktok-video-skills`** | `skills/short-form-video/SKILL.md`, `references/retention-pacing.md` | **Uneven cut cadence** (metronome = boredom; uneven = momentum), frame-0 hook pop without fade-in, 9:16 universal safe box |
| **`poyrazemun/youtube-shorts-generator`** | Automated Claude Shorts pipeline (`script_generator.py`) | **5-Beat Spine:** `Hook → Context → Rehook → Twist → Loopable Ending Fact` + hard-banned openers |
| **`BenAttanasio/shortsmith`** | Programmatic 9:16 vertical explainer engine | **VO-as-master-clock** architecture where every visual beat re-times to spoken words |

---

## 2. THE 1-SECOND LAW: HOW VIEWERS DECIDE "WHY AM I WATCHING THIS?"

1. **You have ~1.0 to 2.1 seconds, not 5 seconds.**
   - On the YouTube Shorts feed, swiping is reflexive. Pre-attentive visual processing fires in **< 0.5 seconds** — before the narrator finishes the first word.
   - **VVSA (Viewed vs. Swiped Away)** is the #1 gate: **< 60% = distribution dies; 75–90% = algorithm pushes wide.**
2. **Priority-1 Gate (`hyperframes-student-kit/curiosity-and-entertainment.md`):**
   - *"First and highest-priority test: In the first 3 seconds, is someone convinced they need to watch until the end? If the opening only earns 'that looked cool' and cannot answer 'WHY should I stay?', revise it before rendering."*
3. **The Three-Layer Hook at `t = 0.0s` (`vyralcontent/three-layer-hook.md`):**
   Every Short MUST fire three aligned signals on **Frame 0**:
   - **Layer 1 — VISUAL (t = 0.0s, zero fade-in):**
     Show the **conflict, anomaly, or an unresolved visual state** immediately (e.g., 3 lit satellites + 1 red blinking `[MISSING]` slot; a ₹10 note submerged in water; a WhatsApp screen with a red warning stamp). Compose as **"click-to-unpause"** (mid-action) + presenter face visible from Frame 0.
   - **Layer 2 — ON-SCREEN TEXT (t = 0.0s, 3–6 words max):**
     **Sharpens, NEVER repeats** the spoken sentence (`three-layer-hook.md`). Drop verbs and articles; keep the **number, contrast (`vs`, `→`), or stake**.
     - *Bad (repeats voice):* `"India has built its own GPS system"`
     - *Good (sharpens stake):* `"INDIA'S GPS: 3 OF 4 SATS"` or `"1 SATELLITE SHORT"`
     - **Pressure test:** Mute the audio — does Frame 0 alone make a scroller stop and ask *"Wait, why?"*
   - **Layer 3 — VERBAL (0.0s–1.8s, 5–10 words):**
     First spoken clause lands the **personal stake, contradiction, or shocking number** immediately.
     - **Hard-banned in Shorts:** `"Namaskar doston"`, `"Aaj hum baat karenge"`, `"Kya aapko pata hai"` (generic "Did you know"), slow setups, or channel intros. Start inside the tension on Word 1.

---

## 3. ENGINEERING A "SHAPED CURIOSITY GAP" (NOT CLICKBAIT)

From `vyralcontent/hook-tactics.md` and `hyperframes-student-kit/curiosity-and-entertainment.md`:

- **Why vague teases fail:** *"Aaj ek badi khabar aayi hai jo aapko chaukayegi"* fails because the viewer's brain has **no shape** to attach curiosity to — they swipe away.
- **The Shaped Curiosity Gap Formula:**
  $$\text{Concrete Subject/Number (Given at 0–1s)} + \text{Specific Stake to Viewer (Given at 1–3s)} - \text{The Mechanism/Twist (Withheld until Payoff)}$$
  - *Example (NavIC):* **Given at 0–2s:** "India ka apna GPS — NavIC — aaj aapko location nahi de sakta, kyunki 4 mein se sirf 3 satellite kaam kar रहे hain." **Open Loop Question:** *Why does 1 missing satellite break positioning, and what happens on 15 October?*
  - *Example (Plastic Notes):* **Given at 0–2s:** "Aapki jeb ka ₹10 aur ₹20 ka note ab plastic ka banne ja raha hai — Sarkar ne 200 crore notes ke trial ko manzoori de di hai." **Open Loop Question:** *Will old paper notes stop working, and why only ₹10 and ₹20?*

### Visual Open-Loop Device ("Wall of Slots" / Unresolved State)
From `hyperframes-student-kit/STORYTELLING-WORKBOOK.md` & `curiosity-and-entertainment.md`:
- Show an **incomplete visual structure** in the opening 2 seconds (e.g., a 4-slot status bar with 1 slot locked/red, a 3-step chain with step 3 masked `[?]`, or a split comparison with the right side hidden).
- Track it explicitly in the episode's `work/OPEN-LOOPS.json`:
  - `setup` (0.0–2.5s): plant the unresolved question visually and verbally.
  - `updates` (body beats): fill slots 1 and 2; raise the stakes at ~50% (the **Re-Hook**).
  - `closure` (75–90% mark): reveal the final slot / twist with sourced proof.

---

## 4. THE 6 PROVEN SHORTS HOOK ARCHETYPES (FOR BENAQAAB INDIA)

Always draft 3 opening candidates across these archetypes and pick the sharpest one before generating VO:

| # | Archetype | Hinglish Spoken Skeleton (0.0–2.0s) | Frame-0 On-Screen Sharpener |
|---|---|---|---|
| **1** | **Contrarian / Myth-Break** *(Kallaway #6)* | *"Aapko lagta hai [Common Belief] — par asli sach bilkul ulta hai."* | `MYTH vs REAL DATA` |
| **2** | **Direct Viewer Stake** *(Dan Koe / Hormozi)* | *"Agar aapke paas [ ₹10 note / FASTag / WhatsApp ] hai, toh ye naya badlav aapke liye hai."* | `CHECK YOUR WALLET` / `₹3,075 PASS` |
| **3** | **Odd-Precision Number** *(Dickie Bush / Poyrazemun)* | *"200 crore naye plastic notes…"* / *"4 mein se sirf 3 satellite…"* | `200 CRORE NOTES` / `3 OF 4 ACTIVE` |
| **4** | **Consequence-First** *(Poyrazemun)* | *"Sirf ek satellite kam hone ki wajah se Bharat ka apna GPS abhi location nahi de sakta."* | `1 MISSING = NO GPS` |
| **5** | **Investigator / Proof-First** *(Kallaway #5)* | *"Parliament mein Sarkar ne khud maana hai ki…"* (show official doc on Frame 0) | `PARLIAMENT RECORD` |
| **6** | **Danger / Red-Flag Callout** *(Negation)* | *"WhatsApp par aayi is traffic challan file ko galti se bhi touch mat karna…"* | `DO NOT TAP .APK` |

---

## 5. THE 5-BEAT "SUSPENSION BRIDGE" TIMELINE FOR SHORTS

Whether a Short is **35 seconds** or **75–90 seconds** (up to our 2:00 cap, §71), scale the body beats — **never slow down the 2-second hook**:

| Beat | Window | Job | Visual & Motion Rule |
|---|---|---|---|
| **1. Frame-0 Hook** | `0.0 – 2.2s` | Answer *"Why am I watching?"* + open the main curiosity loop (`L1`) | Strongest visual + presenter at `t=0.0s` (no fade-up). 3–6 word sharpener text. Hold shot ~2s so the eye reads it (§51). |
| **2. Promise Proof** | `2.2 – 7.0s` | Validate the hook with the first sourced number/document (MrBeast rule) | Morph card expands into the first proof visual (official doc / diagram / counter). |
| **3. Mechanism Beats** | `7.0s – 50%` | Explain *how/why* in 4–6s visual beats; fill slots 1 & 2 of the open loop | Uneven cut intervals (e.g., 3.2s, 4.8s, 3.6s) + one slow log-space camera push per shot. |
| **4. Mid-Video Re-Hook** | `~45% – 55%` | Prevent the mid-video bleed! Open a second micro-loop (`L2`) | *"Par asli twist ye nahi hai…"* + visual pattern interrupt (contrast colour switch / split-screen / presenter return). |
| **5. Twist Payoff + Loop Seam** | `75% – 100%` | Close `L1` + `L2` with the biggest reveal → open comment question → loop to Frame 0 | Final visual state morphs back into Frame 0's exact geometry (`loop_seam < 2.0`), and the final sentence feeds back into Word 1. |

---

## 6. MANDATORY PRE-RENDER CURIOSITY CHECKLIST (ADD TO QA_REPORT.md)

Before rendering any Short, verify all 7 gates:
1. **Frame-0 Mute Test:** Looking ONLY at `frame_0000.png` with sound off, is the topic + curiosity tension 100% clear in < 1 second?
2. **Non-Redundant Hook Text:** Does the Frame-0 headline **sharpen** (3–6 words, numbers/contrast) rather than copy the spoken Hinglish line?
3. **Zero Throat-Clearing:** Does Word 1 of the VO jump straight into the stake/number/contradiction (no "Namaskar doston" in Shorts)?
4. **Unresolved Visual State:** Is there a visible open loop on screen by `t = 2.0s` (missing slot, comparison gap, mystery number) that only resolves in the final third?
5. **Mid-Video Re-Hook:** Is there an explicit curiosity reset ("Par asli sawaal ye hai…" / "Lekin iska sabse bada asar…") near the 50% mark?
6. **Uneven Cut Rhythm:** Are beat transitions spaced unevenly (2.5–5.5s, never a robotic metronome) with zero dead air > 2.2s?
7. **Loop Seam (< 2.0/255):** Does the final frame visually match Frame 0 and does the closing line invite a rewatch?

---

## 7. "SHORTSCRAFT" MASTER RULES (MEMORY FILE v2 — SECTIONS F, G, H, I)

### 7.1 The 1-Second Rule & Core 3 Feelings (Never Break)
- **Jenny Hoyos 1-Second Rule:** On a swipeable Shorts feed, viewers decide in **~1 second** (not 3 seconds) whether to stay or swipe. Optimize **Frame 0** so the visual + on-screen text + first spoken words stack together before the first syllable finishes.
- **Core Feeling Rule:** Within the first **1–2 seconds**, the viewer must feel at least one of these three things:
  1. **(a) *"I need to know the answer to this."*** (Information gap / open loop)
  2. **(b) *"This affects me."*** (Personal stake — wallet, safety, health, phone, daily life)
  3. **(c) *"That's surprising, I don't believe it."*** (Counterintuitive claim / paradox / proof anomaly)

### 7.2 The 7 Curiosity Tools (Use 2–3 in Every Short)
1. **Open Loop:** Ask or imply something in seconds `0–2s`, and delay the final answer until the last 5 seconds.
2. **Information Gap:** Make clear the viewer is missing a specific piece of knowledge (e.g., *19 digits vs 14 digits*, *3 of 4 satellites*).
3. **Pattern Interrupt:** Odd first frame, mid-action start, sudden zoom, or visual contradiction.
4. **Stakes:** Explicitly state what the viewer loses or gains.
5. **Specificity:** Exact numbers, names, dates, and laws — never vague adjectives.
6. **Promise + Proof:** Show what they will learn and flash verifiable evidence immediately in seconds `2–7s`.
7. **Loop Ending:** Write the last spoken line so it flows grammatically and visually back into the first line (`Frame N-1 → Frame 0`).

### 7.3 Two Algorithmic Retention Gates
- **Gate 1 (`2.5s – 3.0s` — Initial Distribution Gate):** Determines swipe-away vs viewed rate (`VVSA`). Your strongest visual proof or twist of the hook must hit right at `2.5–3.0s`.
- **Gate 2 (`14.0s – 15.0s` — Sustained Distribution Gate):** Determines whether YouTube pushes the Short wider. Fire a secondary mini-hook / cliffhanger (`"Par asli khatra yahan hai..."` / `"Lekin iska sabse ajeeb hissa..."`) right at `14–15s` (and every ~10–12s in longer Shorts).

### 7.4 Mandatory 7-Part "ShortsCraft" Script & Pre-Production Package
Before rendering any Short, produce and log this 7-part package:
1. **TOPIC + ANGLE:** One line explaining what makes this version special and why viewers care in 1 second.
2. **3 HOOK OPTIONS + RECOMMENDATION:** Write 3 distinct hooks:
   - *Option A — Question / Visual Question*
   - *Option B — Bold Counterintuitive Claim*
   - *Option C — Specific Number / Story / Direct Callout*
   - Plus which hook is recommended and why.
3. **FULL SCRIPT TABLE (with Dual-Visual Sentence Switch):**
   | Time | Voiceover (≤10 words/sentence) | On-Screen Text (≤6 words) | Visual / Motion Cue (`visual_1` start → `visual_2` end) | Sound / SFX |
   |---|---|---|---|---|
4. **FACT-CHECK LIST (Mandatory Fact Integrity):**
   - Every statistic, date, name, or rule listed with its verified primary/news source.
   - Never invent stats; if anything is unconfirmed, mark `[VERIFY]` and replace with a verified fact before TTS.
5. **METADATA:**
   - **3 Title Options** (< 60 characters, curiosity-driven, honest, no quotes)
   - **Description** (2 punchy lines + 1 debate question to drive comments)
   - **5 Hashtags** (mixing `#shorts` + niche tags)
6. **FIRST-FRAME (`frame_0000.png`) DESIGN:** Exact visual layout + 3–6 word sharpener text + presenter badge.
7. **RETENTION CHECK & SCRIPT DOCTOR SCORE:**
   - Rate **1–10** on **Hook, Pacing, Payoff, Loop** (rewrite anything `< 8/10`).
   - Run the **Script Doctor (0–100)** rubric (target `≥ 85/100`).

### 7.5 Per-Video Request Template (Section G) & Post-Upload Feedback Loop (Section H)
- **Request Template (Section G):** `Topic | Language (Hinglish/Hindi/English) | Length (30–45s fast or up to 90s deep) | Style | Audience | Tone | Extra`
- **Post-Upload Feedback Loop (Section H):** Whenever the user shares analytics (`Views`, `Avg. view duration %`, `Swipe-away in first 3 sec %`, `Hook used`, `Worked/Failed`), analyze the 3-second swipe-away rate and append the lesson to `MEMORY.md` without ever deleting older entries (mark superseded rules `[OLD vX]` if updated).

---

## 8. 5 ADDITIONAL GITHUB PIPELINE REPOS CLONED & DISTILLED (TOTAL 12 REPOS)

In addition to the 7 skill repositories in §1–§6, we cloned and inspected these 5 open-source YouTube Shorts automation & retention codebases:

1. **`Leo0186/ai-youtube-shorts-generator` (`modules/brain.py` — AutoShorts AI):**
   - **Dual-Visual Sentence Switch (`visual_1` + `visual_2`):** Every single spoken sentence is paired with **two** visual states — `visual_1` matching the *start* of the sentence and `visual_2` matching the *end/twist* of the sentence.
   - **Strictly Concrete Visuals:** Never illustrate "The economy crashed" with an abstract "sad man"; always show a concrete, literal object/data visual ("stock market red chart plunging").
   - **5-Stage Edutainment Flow:** `Hook → Context → Mechanism (How it works) → Twist → Outro`.

2. **`Chamanrajragu/purffle-shorts` (`purffle_shorts/script.py` & `doctor.py`):**
   - **2-Pass "Script Doctor" Architecture (`review_script`):** Pass 1 writes the structured JSON script (`WORDS_PER_SECOND = 2.6`, `hook_text` ≤ 6 words, `title` ≤ 60 chars). Pass 2 runs a ruthless retention editor that scores the draft **0–100** (`85+` is required) across *first-2s hook strength, curiosity gaps, pacing, specificity, payoff, and accuracy risk*, lists up to 5 concrete issues, and rewrites weak lines before TTS/render.
   - **11 Proven Short Formats:** `facts`, `story`, `listicle`, `myth` (myth vs fact), `quiz`, `news`, `explainer`, `dialogue` (2-speaker A/B), `chat`, `reddit`, `motivational`.

3. **`gopanihitansh5-collab/youtube-automation` (`src/providers/prompt_builder.py` & `src/quality_gate.py`):**
   - **Scene Energy Map & Emotional Arc:** Every scene is assigned an explicit energy and purpose along a psychological arc (e.g., `mystery → tension → revelation → satisfaction` or `concern → worry → relief → action`).
   - **10-Second Mini-Hook Rule:** Enforces a pattern interrupt in the first 2 words and a mini-hook every 10 seconds to prevent mid-video drop-off, plus a debate-starting pinned comment question.
   - **Automated Narration & Visual Diversity Gate (`_validate_narration_diversity` & `quality_gate.py`):** Blocks any script where `repeated_sentence_ratio > 0.10`, where consecutive scenes start with the same word, or where two scenes share the same visual subject/camera angle/color palette.

4. **`Dark2C/Viral-Faceless-Shorts-Generator` (`trendscraper` + `speechalign` + `piper`):**
   - **Human Script-Approval Gate:** Separates trend research + script generation from TTS + FFmpeg rendering with an explicit script-approval checkpoint so the hook is perfected before rendering frames.
   - **Word-Level Speech Alignment (`speechalign`):** Aligns every word timestamp from TTS audio before drawing captions or cutting visuals.

5. **`Anil-matcha/AI-Youtube-Shorts-Generator` (`shorts_generator/highlights.py`):**
   - **LLM Highlight & Hook Scoring:** Scores candidate segments by immediate hook tension, self-contained payoff, and Whisper word-level timestamps (`faster-whisper`) for 9:16 vertical framing.

---

## 9. 🔴 STANDING USER RULES — CHENAB-BRIDGE FULL-SCREEN MINIMAL STYLE (`brand/reference_minimal_fullscreen.png`), 1–2s MAX SPEAKER & HTML-FIRST APPROVAL GATE (2026-10-01)

1. **NO Multi-Box Dashboard Clutter ("Poor Things"):**
   - ❌ Never stack multiple boxes on screen (no top status bar, no `[01]..[05]` slot strip, no bottom-left `BENAKAB INDIA` card, no `VERIFIED DISPATCH // SOURCE` strip, no `SOURCE //` watermarks on full-screen visuals, no giant full-width caption box).
2. **Gold-Standard Layout (`brand/reference_minimal_fullscreen.png`):**
   - **Full-Screen `1080×1920` Visuals / Video:** Every B-roll clip, photo plate, and motion graphic fills the entire `1080×1920` frame edge-to-edge (`max view`), leaving **65–75% of the screen open** so the visual and motion graphics breathe.
   - **Minimal Translucent Glass Card (Top Zone):** One clean dark glass card (`rgba(10, 14, 20, 0.78)`, thin top accent bar) with a bold 3–4 word title (`BUILT FOR THE WORST`) and 2–4 compact stat cells (`266 km/h`, `Zone V (max)` — 2 to 3 words per cell max, zero long sentences).
   - **Compact Bottom-Left Caption Pill:** Small tight dark pill at bottom-left (`chal sakti`) showing 2–3 words at a time with a thin orange/gold underline.
   - **Tiny Top-Right Logo Only:** Small circular logo in top-right (`56×56px`).
3. **Speaker Visibility — 1 to 2 Seconds MAX in Full Screen:**
   - Do **NOT** keep the speaker continuously in the corner. Show the speaker **only for 1 to 2 seconds max** in full screen, and keep the rest of the Short 100% full-screen visuals & motion graphics.
4. **HTML-First Approval Gate (`comp.html` BEFORE Final MP4 Render):**
   - **Always build and show `comp.html` to the user FIRST** and **wait for explicit user approval** before rendering the final `.mp4` video.


