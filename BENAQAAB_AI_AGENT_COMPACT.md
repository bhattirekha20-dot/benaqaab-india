# BENAQAAB INDIA — AI AGENT SKILL FILE (compact, single file)

**Version 1.0 · 4 October 2026 · what to hand to any AI agent**
**Read top to bottom.** Part I is the operating manual (laws, pipeline, contracts, gates, failure
catalogue — everything needed to build a film correctly). Part II digests all fifteen deeper skill
documents into their operative rules. §INDEX at the end points into the complete edition
(`BENAQAAB_AI_AGENT_MASTER_SKILL.md`, 2.90 MB) where every appendix sits in full.

**THE TEN NON-NEGOTIABLES**
1. The 1-Gate Approval Pipeline — topic in, interactive preview (`comp.html`) out; wait for user approval before rendering final MP4.
2. Frame = pure function of t — deterministic, seeded, re-renderable one second at a time.
3. No dead frames — motion at three scales; `motion_report` freezes = none.
4. Real Source Media & AI Images — never diagrams alone; anchor every beat in authentic source media and photorealistic AI art.
5. Facts or nothing — sourced + dated; disagreements shown, never averaged; claims labelled.
6. Sound is measured — VO is the master clock; loudness measured on the muxed file (-14 LUFS).
7. Text must fit — Hindi is wider than Latin; measure, shrink, wrap; no overflow, no collisions.
8. Cuts are a craft — official transition names/durations; captions above the composite; no snap-back.
9. Verification before claims — encoded frames inspected, gates run, real numbers, unknowns stated.
10. Protect the record & Unpack Deliverables — protected files never deleted; deliverables always unpacked and visible, never buried in ZIPs.

---

# PART I — OPERATIONAL CORE

*This part is the v2.0 master skill file, verbatim. It is the file an agent should read first.*

# BENAQAAB INDIA — AI AGENT MASTER SKILL (single file)

**Version 2.0 · 4 October 2026 · owner: the user ("Benaqaab India" channel)**
**Purpose:** hand this ONE file to any capable AI agent and it must be able to work the way
this workspace works — same rules, same pipeline, same quality gates, same traps avoided.
**Companions in the repo (deeper reference, not required to start):** `MEMORY.md` (full history,
130+ sections), `MASTER_VIDEO_GENERATION_SKILLS.md` (36-chapter handbook + archives),
`SKILLS_*.md` (topic skills), `knowledge/`, `tools/`, `viz/`, `brand/`.

> **Reading order for a new agent:** §1 → §2 (the laws) → §3 (workspace) → §4 (pipeline) →
> then whatever the task needs (§6–§13) → §14 QA before delivery → §16 when something breaks.

### THE TEN NON-NEGOTIABLES
1. **The 1-Gate Approval Pipeline.** Topic in → preview out (`comp.html`) → user gate → final MP4. Work autonomously through research, script, audio, and visual assets to build the interactive HTML preview. STOP at the gate. Never render final MP4 until the user explicitly approves or says *"render the video"*.
2. **Frame = pure function of t.** Deterministic, seeded, re-renderable one second at a time.
3. **No dead frames.** Every frame has motion at three scales; `motion_report` freezes = none.
4. **Real Source Media & AI Images — Never Diagrams Alone.** Animate real mechanisms; anchor every beat in authentic source media (PIB, press, official data cards, document scans) paired with photorealistic AI illustrations. No sterile diagrams or bare slideshows.
5. **Facts or nothing.** Every number sourced + dated; disagreements shown, not averaged; labels on claims.
6. **Sound is measured, not guessed.** VO is the master clock; loudness is measured on the muxed file (-14 LUFS).
7. **Text must fit.** Hindi is wider than Latin — measure, shrink, wrap; nothing overflows, nothing collides.
8. **Cuts are a craft.** Official transition names/durations, captions above the composite, no snap-back.
9. **Verification before claims.** Encoded-file frames inspected; gates run; real numbers reported; unknowns said plainly.
10. **Protect the record & Unpack Deliverables.** Never delete protected files; `MEMORY.md` grows, superseded rules get `[OLD vX]`. All deliverables (thumbnails, titles, descriptions, SRT) must be presented unpacked and immediately visible—never buried exclusively in ZIPs.

### CONTENTS
| § | Section |
|---|---|
| 1 | The job, the channel, the user |
| 2 | The user's laws (standing directives) |
| 3 | Workspace map & file discipline |
| 4 | The standard pipeline, step by step |
| 5 | Research & fact rules |
| 6 | Script craft — Shorts |
| 7 | Script craft — long form |
| 8 | Visual system (composition, HUD, type, thumbnails) |
| 9 | Motion craft (curves, camera, ambient motion, impact frames) |
| 10 | Transitions (CapCut + Alight, natively) |
| 11 | Technical contracts (renderer, HTML, engine, grade) |
| 12 | Audio pipeline (voice, master, loudness) |
| 13 | Edit-style films (anime-edit recipe) |
| 14 | QA gates |
| 15 | Delivery & packaging |
| 16 | Failure catalogue (symptom → cause → fix) |
| 17 | Copy-paste templates |
| 18 | Quickstart run sheet |
| 19 | Honesty rules |
| 20 | Reference index + definition of done |

---

## 1. THE JOB, THE CHANNEL, THE USER

**Channel:** *Benaqaab India* — tagline **"SACH · SABOOT · BEBAK"** (truth · proof · outspoken).
A general India explainer channel, **not** a scam-only channel. Scope covers science & space,
tech & AI, money & rules that affect people, health myths, environment & climate, civic /
government / infrastructure, India engineering, sourced history, and scams & cyber-safety as
*one* category among many.

**Formats in active use**

| Format | Spec | Notes |
|---|---|---|
| YouTube Short (default) | 1080×1920, 30 fps, **≤ 2:00** (our cap), H.264 High + AAC | measured narration sets the length, never a preset |
| Long-form (rare, Ep12+) | 1920×1080, 30 fps, target 3:30–4:30, max 5:00 | see §7 |
| Edit-style film (on request) | 1080×1920 vertical, 10–30 s, beat-driven | see §13 — e.g. "anime edit" |

**Language rules**
- Narration is **Hindi / Hinglish**. For TTS, write Hindi in **Devanagari** and spell numbers,
  abbreviations and English words phonetically (`रवि, एट, ओके एच डी एफ सी बैंक` to force an
  `@`-style handle). Hinglish spoken shorthand is the house voice; the user writes in Hinglish
  shorthand and expects it to be understood without asking for spelling clarification.
- On-screen text: English for labels/numbers/sources; **Hindi summary captions** for the short
  films (they are *summaries*, never word-aligned subtitles — say so in the file header).

**The user**
- Communicates in short Hinglish. Assume intent, don't interrogate.
- Wants finished work, not drafts: *"from now I only give you topic and you, using everything,
  make best videos."* Make every call yourself and **report the decisions at delivery**.
- **Mandatory Pauses / User Gates:**
  1. **Gate 0 (`RULE-FORMAT-DURATION-GATE`):** Whenever a topic is chosen, **always ask the user**: (a) Long video (16:9), short video, or YouTube Short (9:16)? and (b) What target duration? Never guess or assume format/duration!
  2. **Gate 1 (`RULE-GATE-1`):** Interactive `comp.html` preview approval before full MP4 render.
- Wants honest reporting: what was verified, what wasn't, what failed and why.

---

## 2. THE USER'S LAWS (standing directives — verbatim where quoted, with current status)

**L0 · Format & Duration Confirmation Gate (`RULE-FORMAT-DURATION-GATE`).** *"make sure when ever a video topic is choose the ai ask me tht long video or short video or yt short and duartion too ok"*
Whenever a video topic is chosen (provided by user, proposed by agent, or selected from topic registry), the agent MUST STOP and explicitly ask: (1) Long-form (16:9), short explainer, or YouTube Short (9:16)? and (2) What target duration? Only after user confirmation does scriptwriting and production begin.

**L1 · Autonomy & The 1-Gate Approval Protocol.** *"from now I only give you topic and you, using everything, make best videos."*
The agent executes autonomously through research, script, voiceover generation, visual asset creation, and building the interactive HTML preview (`comp.html`). However, the **1-Gate Approval Protocol** is mandatory: the agent must STOP at the preview gate and never render a final MP4 until the user explicitly approves or gives the command: *"render the video"*. (Older automatic rendering without preview gate is superseded).

**L2 · Topic research first, then build.** When asked to find topics, research properly, save a
shortlist file with verified numbers + sources + hook lines + risk notes, and let the user pick.
It already exists: `knowledge/topic_ideas/NEW_TOPIC_SHORTLIST_2026-10.md`.

**L3 · Delete what the user calls demo data — but never these files.**
*"ok now delet all the demo data ok and find new tipics to make the video ok."*
- Delete: throwaway labs, demos, scratch projects, test artifacts, `.cache/` content.
- **NEVER delete, hide, move or pack:** `MEMORY.md`, `MOTION_RESEARCH_Opus55.md`,
  `SKILLS_RESEARCH.md`, `SKILLS_LONGFORM.md`, `SKILLS_SHORTS_CURIOSITY.md`,
  `SKILLS_THUMBNAIL_AND_MOTION_MASTERY.md`, `PROMPT_LIBRARY_opus55.md`, `motion.py`
  (both `viz/` and root copies), `setup.sh`, `knowledge/`, `brand/`, `viz/`.
- Update living documents **in place**; mark superseded entries `[OLD vX]`; never silently drop
  history. Heavy intermediates go to `.cache/`.
- A "delete full workspace" request means **video projects only** (`projects/` + rendered MP4s);
  make a text/skills backup first and verify protected files afterwards by hash.

**L4 · Peak detail is the standard, not an extra.** *"far more detailing and better execution…
research repositories… strengthen the skills further."* Research verified repos, adopt what is
provable, reject link-dump advice, and **never claim** that repo research permanently upgrades a
model or guarantees cinematic results.

**L5 · Use the official apps' language.** CapCut + Alight Motion — official versions, with **all**
their transitions/effects/features. The apps cannot run in this Linux workspace (proprietary,
login + VIP), so: (a) extract the **official catalogues** from open metadata and reimplement the
grammar natively (`viz/motion_library.js`, 24 transitions, official names + durations), and
(b) ship CapCut draft / Alight `.xml` writers (`tools/capcut_draft.py`, `tools/alight_project.py`)
when the user wants to finish in the app. **Never claim an app rendered anything here.**

**L6 · After Effects knowledge is required.** Learn AE craft (easing, weight, motion blur, depth,
grade stack, type in motion, expressions) and encode it in the pipeline. AE cannot be installed
here; the four real hand-off routes (Lottie, alpha frames, aerender/nexrender, project→JSON→
rebuild) are documented in `SKILLS_AFTER_EFFECTS.md`.

**L7 · Never slideshow-ify.** Never limit motion graphics to text cards over zooming JPEGs.
Animate real mechanisms: pipelines, packets, dials, counters, bars, splitters, stamps, maps.

**L8 · Theme freedom.** Dark-only or light-only is not a rule; choose what serves the subject and
readability. (Older "bright daylight" guidance is superseded.)

**L9 · Like ★ / Subscribe ▶ always.** A floating chip during the film (spec in §8) and a spoken
ask in the final beat (~2 s), plus the on-screen CTA in the last scene. End **Like ★ / Subscribe ▶**.

**L10 · Audio defaults.** Narration + discrete SFX is the default bed. Music only when the format
demands it (edits, montages) and then it must be **original or licensed** — never a copyrighted
track. Mix targets in §12.

**L11 · Visual style contract (Shorts).** Full-screen visuals that breathe; a compact glass card
top zone (`rgba(10,14,20,0.78)`, thin accent bar) with a 3–4 word title and 2–4 tiny stat cells;
a small bottom-left caption pill with a thin accent underline; official Benaqaab OS logo in the
**top-left safe area** (`x: 55px, y: 30–40px`, gold-glow border; older top-right guidance is `[SUPERSEDED]`).
**No dashboard clutter** — no fake timecode, no frame counter, no REC dot, no viewfinder brackets, no
`SOURCE //` watermarks, no stacked box walls: it reads as an unfinished render and costs
retention. Never put the speaker continuously on screen — if a presenter is ever used, 1–2 s
maximum in full screen, then back to full-screen visuals.

**L12 · Honesty about disagreements.** When two credible sources disagree, **show both on screen
with dates** and say so in the narration. Never average them into a fake number.

**L13 · Never use brackets in `description.txt` or pinned comments:** no `( ) [ ] < > { }`.

**L14 · Category variety.** Shortlists must mix categories; don't propose scams only.

**L15 · Edits on request.** *"make me a anime edit ok"* → build **original** anime-style art and
original music (nothing ripped, no existing characters/IP, no copyrighted songs), then apply
real edit grammar (beat cuts, impact frames, speed-ramp echoes). If the user supplies their own
licensed clips, cut *those* on the same beat map.

**L16 · New video = clean slate (declare it every time).** *"whenever i ask you to make a new video
always delete last video all the files and start research for new topic"* — before starting any new
film: delete the previous film's project folder (`projects/<name>/`), its rendered MP4 and its audio
master, and any of its QA/scratch caches; then begin with **fresh topic research** — never reuse the
last topic's material unless the user explicitly asks for a sequel or a new version. If the user
names a topic, use that topic, but the wipe still happens first. Record the wipe in `MEMORY.md`
(what was deleted, and which backup can restore it).

**L17 · Three Dedicated Color Grading Profiles.**
- **Profile A (Daily News & Global Roundups):** Neutral documentary grade. Natural color temperature, realistic skin tones, clean whites, balanced saturation, crisp contrast, zero orange/sepia tint (used in `projects/india_last_24h/`).
- **Profile B (Benaqaab Forensic Dossier):** High-contrast B&W / desaturated stills with bold horizontal Red censor/classification band (`#ef4444` / `#dc2626`).
- **Profile C (Historical / Archival Public Footage):** Warm sepia/orange base with dark-green horizontal band (`#22764e`) and 3% grain (`apply_public_video_grade.py`).

**L18 · Media Sourcing & Multi-Story Rigor.**
- Real source media & AI images — never diagrams alone.
- In multi-topic roundups, independently find and curate suitable media for *every story* in the lineup, not just the headliner (Rahul Gandhi).

**L19 · Autonomous Permission Handling.**
- Do not re-prompt for permission once confirmed by the user. User confirmation is permanent for that workflow.
- If a clip cannot be downloaded (403/captcha/bot blocks), autonomously fall back to verified public stills and official data cards without stalling.

**L20 · Mandatory Unpacked Deliverables Standard.**
- All deliverables (`thumbnail_1280x720.jpg`, `cover_vertical_1080x1920.jpg` / `thumbnail_1080x1920.png`, `title.txt`, `description.txt`, `hashtags_and_tags.txt`, `headline_captions.srt`) must be placed unpacked at the project root / `delivery/` folder.
- In completion reports, the AI must explicitly display the thumbnail and quote the title and description directly. Never bury deliverables solely inside ZIP archives.

**L21 · Universal 10-Visuals-Per-Minute Law (`RULE-10-VISUALS-PER-MINUTE`).**
- **Mandatory Visual Cadence:** Across ANY topic and format, every 60 seconds of video must feature **at least 10 distinct visual assets/beats** (average shot length ≤ 5.5 to 6.0 seconds). Holding a static visual for >6 seconds is strictly banned.
- **Longform Scaling:** For longform documentaries (such as the 10m 29s PFBR film), 10 beats/min scales to **roughly 105 distinct visuals** across the timeline.
- **The 8-Part Mixed-Media Portfolio:** Never rely on a single visual style. The 10 visuals per minute must weave together: (1) Photorealistic Forensic AI Macro Photography, (2) Primary-Source Official Gazettes/Court Documents with highlighter sweeps, (3) Engineering Schematics/CAD Cutaways with callout pins, (4) Live Rolling Data Odometers & Tickers, (5) Geopolitical & Maritime Supply Chain Maps, (6) 2X Optical Loupe Inspections, (7) Verified Editorial News Stills & Archival Records, and (8) Kinetic Typography HUD Cards & Verdict Stamps.

**L22 · 5-6s Roadmap Hook, What-and-Use Architecture & Motion Image Annotation (`RULE-5SEC-ROADMAP` · `RULE-WHAT-AND-USE` · `RULE-IMAGE-ANNOT`).**
- **5-6s Roadmap Hook:** In explainer videos, the opening 5.5 seconds must feature an animated 3-step preview card (`01. What is it?`, `02. How it works?`, `03. Real-world use?`) sequentially illuminated as the speaker outlines the episode roadmap.
- **What-and-Use Architecture:** The script must deeply and simply demystify two core questions: Part 1: *"Kya hai yeh?"* (physical/technical foundation with macro/gazette proof) and Part 2: *"Iska real use kya hai?"* (everyday, industrial, and national applications with rolling metric odometers).
- **Motion Image Annotation:** Never display plain static photos with dead air. Every visual must be dynamically explained using motion primitives (`drawCalloutPin`, `drawEvidenceLoupe`, `drawHighlighter`, `drawOdometer`, `drawVerdictStamp`).

---

## 3. WORKSPACE MAP & FILE DISCIPLINE

```
/home/user
├── MEMORY.md                     full production history (append-only, protected)
├── MASTER_VIDEO_GENERATION_SKILLS.md   36-chapter handbook (deep reference)
├── SKILLS_*.md                   topic skills (shorts curiosity, long-form, peak detail,
│                                 after effects, CapCut/Alight, thumbnails, research)
├── PROMPT_LIBRARY_opus55.md      prompts library (reference data, not authority)
├── motion.py                     motion core (Pillow side) + QA: motion_report()
├── setup.sh                      rebuilds ffmpeg/playwright/chromium/fonts — run after resets
├── brand/                        logo, fonts, reference images  (fonts: Archivo, Inter,
│                                 JetBrainsMono, NotoSansDevanagari, Anton, Geist, …)
├── viz/
│   ├── hrender.py                THE renderer (headless Chromium → ffmpeg)
│   ├── motion_library.js         the shared engine (see §11)
│   ├── motion.py / motion.js     motion core + QA metrics
│   ├── templates/scaffold.html   technical contract example (NOT a visual template)
│   ├── source_style.py           third-party footage look (B&W + halftone + red band)
│   └── serve_delivery.py         local delivery page for the user
├── tools/
│   ├── peak_detail_gate.py       structural preproduction-plan validator (§14)
│   ├── capcut_draft.py           CapCut draft folder writer
│   ├── alight_project.py         Alight Motion scene-XML writer
│   └── data/CATALOG_*.json       official effect/transition catalogues (3,424 items)
├── knowledge/                    research (after-effects, capcut-alight, peak-detail,
│                                 topic_ideas, 3d_documentary_research)
└── projects/<film>/
    ├── <Film>.html               the film: single file, deterministic, art inlined
    ├── <Film>.mp4                delivery
    ├── audio/  vo_*.wav · master.wav · music.wav
    ├── TIMELINE.json  (measured)  · PLAN.json (peak-detail plan) · BEATS.json (edit films)
    ├── SCRIPT.md · SOURCES.md · MOTION_PASS.md · AUDIO_NOTES.md · README.md
    └── QC_*.jpg                  contact sheets that prove the QA (moved to .cache after)
```

**Size & hygiene policy:** the workspace holds only important things. During production keep the
project under ~100 MB; masters, trims, stills, QA sheets and render logs belong in `.cache/`
(which is wiped on sandbox restart). After delivery: leave the upload pack + recipes.
Snapshot exclusions that never persist: `.cache`, `node_modules`, `dist`, `build`, `out`,
`__pycache__`, `.venv`, `.git` credentials. Work that matters must live outside those.

---

## 4. THE STANDARD PIPELINE (topic in → finished video out)

**Step 0 — setup (once per sandbox, mandatory).**
```bash
bash /home/user/setup.sh     # run via start_process; expect [setup] OK
which ffmpeg ffprobe && python3 -c "import playwright, numpy, PIL; print('ok')"
```
If ffmpeg/Playwright are missing after a sandbox reset, this rebuilds them. Never start a render
before this passes.

**Step 1 — research → `SOURCES.md`.** Every number from a primary source or two independent
secondaries, with date + URL. Mark non-claims explicitly. Derived figures (e.g. 66 crore ÷ 86,400
= 7,639/s) must be labelled as **our derivation** and shown as an average.

**Step 2 — concept.** ONE formal idea (one element that transforms through everything / before-
after split / chain reaction), ONE running example for the whole film, ONE memorable line.

**Step 3 — script (`SCRIPT.md`).** For Shorts: 7-part ShortsCraft package (§6). Narration
paragraph = one scene. Numbers phonetic in VO, exact numerals on screen. Word count checked
against ~2.4 words/s *before* synthesis. Scene ↔ transition map included.

**Step 4 — voice.** `add_voice` audition (the one mandatory pause) → `generate_speech` per
paragraph → convert to 48 kHz mono WAV → **measure durations with python `wave`** → write
`TIMELINE.json` (`narration_at`, `start`, `dur`, `vo`, `total`). VO is the master clock; scene
boundaries are computed from measured audio, never guessed. Keep total = whole frames at 30 fps
(e.g. `125 + 26/30 = 125.86666666666666`).

**Step 5 — build the film HTML.** Single file, deterministic, new look per film. Inline art as
data URIs when the film must survive as one file (`bake_film.py` pattern). Inject `T` (timeline)
and the cut windows. Follow the contract in §11.

**Step 6 — QA loop before the full render.**
```bash
# page-error probe first (hrender waits forever on a broken page — §16 F2)
python3 - <<'PY'  # playwright: goto file://…, wait_for_function('window.ready===true'), print pageerror list
PY
python3 viz/hrender.py <Film>.html _qa --stills 1.2,7.5,18.0,33.5,55.0,74.0,95.0,118.0
python3 viz/hrender.py <Film>.html _qa --beats 1.0        # contact sheet every second
```
Read the sheets at full size. Fix text overflow, collisions, dead stretches. Re-check.

**Step 7 — audio master.** numpy: narration at measured times + per-cut SFX + optional bed +
sidechain duck under speech → `audio/master.wav` (peak-normalise in numpy) → **two-pass
`loudnorm`** to the delivery target (§12). Mux with `-c:v copy` so the loudness pass never
touches a pixel.

**Step 8 — full render.**
```bash
python3 viz/hrender.py <Film>.html <Film>.mp4 --audio audio/master.wav --crf 18 --max-samples 8 --check
```
Run it through `start_process` (it can take 10–25+ minutes), watch the log, then read the
`[check]` JSON (§14). Freezes must be none, or explained and deliberate. Pops must be only inside
the declared cut windows.

**Step 9 — verify the encoded file.** Extract 6–12 frames **from the MP4** (`ffmpeg -ss … -frames:v 1`)
and look at them; `ffprobe` the streams; `ebur128` measure the muxed audio. `ffmpeg -v error
-i out.mp4 -f null -` to prove it decodes clean.

**Step 10 — deliver.** Present the MP4; state specs (duration, frames, size, LUFS, peak);
list files; report **decisions made** and what was *not* verified. Keep upload pack + QC sheets;
push intermediates to `.cache/`.

**Step 11 — update `MEMORY.md`** with a new numbered section: what was built, measured numbers,
the traps found, the fixes. Never delete old sections; mark superseded ones `[OLD vX]`.

---

## 5. RESEARCH & FACT RULES

- Two independent sources for any number that goes on screen; prefer the primary (government,
  company release, paper). Record date *and* window ("Apr 2026", "FY2025-26").
- **Disagreement is content, not noise:** show both values side by side with their dates and
  scale definitions (this is the honesty scene pattern: e.g. 49 % IMF/PIB Jun 2025 vs 46 %
  reported Sep 2025, both labelled).
- Claims that are claims get labelled: "reported", "as of March 2026", "99.99 % uptime — a
  reported average, not a guarantee".
- If it isn't verified, it does not go on screen and does not enter the VO.
- Schematics/diagrams are labelled *schematic* when not to scale.
- Never hide a conflict to make a cleaner story. When unsure, say what is unknown — in the
  narration if it matters to the claim.
- Repo research method (the one that has worked): query the GitHub API for metadata, verify the
  repo exists, fetch the README/source of the specific file, inspect only the relevant parts,
  record what was adopted and what was rejected *and why*. Never adopt link-dump advice. Never
  claim a repo was installed/benchmarked when it was only read.

---

## 6. SCRIPT CRAFT — SHORTS (the retention engine)

**6.1 The 1-second law.** On a swipeable feed the decision happens in ~1 second. Frame 0 must
stack: visual + on-screen text + first spoken words. Within 1–2 s the viewer must feel one of:
**(a)** "I need to know the answer", **(b)** "this affects me" (wallet/health/phone/daily life),
**(c)** "that's surprising / I don't believe it".

**6.2 Use 2–3 of the 7 curiosity tools every film:** open loop · information gap · pattern
interrupt · stakes · specificity (exact numbers/names/dates) · promise + proof (flash evidence at
2–7 s) · loop ending (last line flows back into the first frame).

**6.3 Two retention gates.** *Gate 1 (2.5–3.0 s):* the strongest visual proof or twist must land
here. *Gate 2 (14–15 s, then every ~10–12 s in longer Shorts):* fire a secondary mini-hook
("par asli twist abhi baaki hai…").

**6.4 The 5-beat suspension bridge** (short films): hook → spine → contrast/mechanism → payoff →
loop + ask. Cut rhythm uneven (2.5–5.5 s beats, never metronomic, no dead air > 2.2 s).

**6.5 7-part pre-production package (produce and log it):**
1. **Topic + angle** — one line: why viewers care within 1 second.
2. **3 hook options** (question / bold counterintuitive claim / specific number or callout) +
   which one is recommended and why.
3. **Full script table** — | Time | Voiceover (≤10 words/sentence) | On-screen text (≤6 words) |
   Visual cue (visual₁ → visual₂, i.e. two visual states per sentence) | Sound/SFX |.
4. **Fact-check list** — every stat/date/name + source; anything unconfirmed is marked `[VERIFY]`
   and replaced before TTS.
5. **Metadata** — 3 titles (<60 chars, honest, curiosity-driven), description (2 punchy lines +
   a debate question), 5 hashtags.
6. **Frame 0 design** — exact layout + a 3–6 word sharpener + any badge.
7. **Retention check** — score Hook, Pacing, Payoff, Loop 1–10 (rewrite <8), and Script Doctor
   0–100 (ship ≥85): first-2s hook, curiosity gaps, pacing, specificity, payoff, accuracy risk.

**6.6 Visual↔sentence rule.** Every spoken sentence gets **two** visual states (start and
end/twist). Never illustrate abstractions with generic mood images — use concrete, literal
visuals (a chart, a mechanism, a real screen capture).

**6.7 Narration length.** ~2.4 words/s; 25–35 s ≈ 60–85 words; our Shorts cap is 2:00 — pick what
the story needs. Hook in the first 2 s; re-hook every ~20–25 s; new visual beat every 3–6 s.

---

## 7. SCRIPT CRAFT — LONG FORM (when the user asks for a full video)

- **First 30 s is a ranking input.** Cold open on the most surprising fact/visual (no logo sting,
  no "welcome back"); promise stated by 15–30 s; visual change every 3–7 s; first deliberate
  pattern interrupt at 25–35 s.
- **Structure (≤5 min):** 0:00–0:20 cold open + promise · 0:20–0:40 context (dated) ·
  3–4 chapters of 45–75 s (mini-hook → explanation → PROOF → mini-payoff) · re-hook at ~50 % ·
  last 30–40 s final payoff that circles the opening question (never "in summary") → CTA ≤10 s.
- **Open loops** teased early and paid late; **chapters** in the description (first must be 0:00,
  ≥3 chapters each ≥10 s, descriptive names).
- **Scene types to build in HTML:** animated charts (one scale per comparison), schematic maps
  (city dots/routes; no national borders unless Survey-of-India compliant), timelines, orbit/
  process diagrams, kinetic type, real photos/footage with purposeful punch-ins, split screens,
  document zooms, ≤1.5 s chapter cards, and one recurring anchor motif.
- **Cutting:** progressive rhythm (cuts accelerate toward the payoff), contrast of fast/slow,
  narrative loop returning to the core question. **J/L-cuts:** next scene's visual leads the VO by
  ~0.3 s. No dead air between sections.
- **Third-party footage/photo look:** every external clip/photo goes through `viz/source_style.py`
  (high-contrast B&W + halftone screen + translucent red band on the eye line + vignette) so
  evidence and our own graphics are distinguishable at a glance. Our charts/maps stay in colour.
  Keep clips short, credited, used for commentary; prefer official/free sources.
- **Benchmarks:** <5 min videos: 50–70 % average percentage viewed; ≥60 % still watching at 30 s;
  average view duration ≥50 % roughly triples recommendation odds.
- **Packaging:** thumbnail 1280×720 with 3–4 words + one big number/graphic, matching the hook;
  title ≤60 chars; SRT captions uploaded; end screen in the last 5–20 s.

---

## 8. VISUAL SYSTEM (design laws)

**8.1 Composition.** One idea per frame. ≤3 subject groups, one protagonist per beat, accent
colour reserved for the current key point. Full-screen visuals that breathe (keep ~65–75 % of the
frame open). Letterboxing and empty decoration are banned; every pixel earns its place.

**8.2 The Shorts HUD (minimal full-screen style).**
- Top zone: ONE translucent glass card `rgba(10,14,20,0.78)` with a thin accent bar, a bold 3–4
  word title, and 2–4 compact stat cells (2–3 words each — no sentences).
- Bottom-left: a small caption pill, 2–3 words visible at a time, thin accent underline.
- Top-left: official Benaqaab OS logo with gold glow border (`x: 55px, y: 30–40px`, from `source_images/benaqaab_os_logo.png` or `brand/logo.png`; older top-right placement is `[SUPERSEDED]`).
- Safe zones: keep text inside x ≥ 70 px, and clear of the bottom ~300 px where platform UI sits.
  Caption band in the films we shipped: y ≈ 1592, height 148.
- **Banned:** timecode, frame counters, REC dots, scene strips, viewfinder brackets, watermarks,
  multi-box dashes, presenter corners, end cards on Shorts.

**8.3 Typography.**
- Fonts from `brand/fonts/`: Archivo (numbers/titles, tabular figures for counters), Inter (UI),
  JetBrains Mono (labels/source tags), NotoSansDevanagari (Hindi), Anton/Geist/Bricolage/
  InstrumentSerif/SpaceGrotesk for variety. CJK: system `NotoSerifCJK-Bold.ttc` (copy into the
  project when the film needs kanji — a film must never depend on a missing font).
- **Hindi strings are wider than Latin at the same px.** Every fixed-width box gets
  `fitText()` (measure → shrink until it fits, ≥ a legibility floor) and `wrapText()` (wrap to
  ≤2 lines, shrink to fit). This is not optional — overflow was the #1 defect in the first UPI
  render pass.
- ≤6 words per line, one line at a time. Numbers exactly as sourced, with units, tabular figures,
  counting up. Text entrances ≤600 ms, exits faster (~250 ms) and at exactly 0 before a cut.

**8.4 Adaptive contrast over imagery.** Sample the luminance (mean **and** std) behind a text box
and fade in a feathered dark plate only if needed: `need = clamp01((mean-0.15)*2.3 + std*1.25)` —
std catches busy photo areas where mean alone says "fine".

**8.5 Thumbnails (1280×720 and 1080×1920).** Never a flat text-bar screenshot. Signature
archetypes: (1) dramatic AI/3D hero with one giant number, (2) split before/after or India-vs-world
comparison, (3) evidence wall with red thread/callouts, (4) minimal full-screen with 3–4 words,
(5) character-led (channel host) reaction frame. Two-stage pipeline: AI/3D base → programmatic
type + badge from `brand/logo.png`. Keep 3–4 words, one big graphic, high contrast, and the
thumbnail must match the hook.

**8.6 Motion-graphics techniques in the house style** (use more than one per film):
2.5D evidence wall with red-thread camera flight · physical slam-down rubber stamps
(`[EXPOSED]` is banned-in-text only for descriptions; on screen stamps are fine) · kinetic
multiplier equations (₹5 Cr → ₹4,000 Cr = 800×) · glowing India map with corridor/hotspot pulses ·
live highlighter sweep over official documents · HUD discipline (never clutter) · segment-reticle
callouts with leader lines onto real objects · code-drawn flags/chakras and live waveform graphs.

---

## 9. MOTION CRAFT (what makes it look "wow")

**9.1 Easing — the biggest single upgrade.** Four named curves, nothing else:
ARRIVE (outQuint/outExpo for entrances) · SETTLE (spring for physical things) · SWEEP (inOutCubic
for camera/A→B moves) · CUT (instant, for hits). Entrances ≤600 ms; exits ~250 ms. Linear is for
progress bars and belt motion only. `outQuart` does **not** exist in `viz/motion_library.js`
(available: linear, outQuad, inQuad, outCubic, inCubic, inOutCubic, outQuint, outExpo, outBack,
outElastic).

**9.2 Frame = pure function of t.** No `Math.random`, no `Date`, no state carried between
`seek()` calls (seed everything: `mulberry(seed)`). This is what makes parallel capture, re-render
of a single second, and deterministic QA possible.

**9.3 Camera.** ONE transform for the whole film: slow push-in, log-space zoom, ≤1 move per shot,
never in-then-out back-to-back. Camera drift must be a function of **absolute** film time and
applied *inside* the scene renderer, so transition buffers and the direct path stay
pixel-identical (otherwise a 1-frame jump appears at every cut boundary).

**9.4 Weight and physicality.** Springs are closed-form damped step responses; a value whose
target changes over time is the SUM of one spring per change. Use `spring()` for anything that
should feel physical (stamps slamming, packets landing, cards settling).

**9.5 Motion blur.** The renderer samples sub-frames across a 180° shutter and blends in linear
light. `window.speed(t)` (fastest on-screen speed, px/s) drives adaptive sampling: 1 sample when
the smear is sub-pixel, up to `--max-samples` on fast moves. 6–8 sub-frames for fast motion;
4 or fewer causes ghosting. Because the render is deterministic, "reuse the previous frame" is
only safe when `window.state(t)` matches.

**9.6 Text handoff.** Masked word rise, 55–70 ms stagger. Outgoing text is gone before incoming
text arrives. **Captions live ABOVE the video layers** and must be skipped while a transition
composites (`window.__capSkip`), otherwise the text ghosts into the wipe. At a cut, overlap the
two captions (out fades by ~50 %, in arrives from ~40 %) so the caption band is never empty —
and `capAlpha()` must not drop an incoming caption back to zero after the cut has already passed
its midpoint.

**9.7 Ambient motion is mandatory (the peak-detail law learned the hard way).** A film that
animates in and then holds still reads as dead. Every frame must have motion at three scales:
- **Global:** absolute-time glow orbit, grid drift (≈26/17 px·s⁻¹), 50–70 dust motes
  (26–84 px·s⁻¹), a light sweep crossing on a 5.6 s loop, and the continuous camera drift.
- **Per-scene micro-motion:** LED pulses, marching dashes, dial ticks, queue slots, shimmer
  inside bars, chip bobs, breathing outlines — 3–6 px / low-alpha, never distracting.
- **Mechanism motion:** even in a "hold" beat, have the actual system tick (a verification ping
  running the rail, a counter's trailing digits, a travelling highlight).
Motion must mean something; do not add noise to satisfy a metric.

**9.8 Impact frames (anime/edit grammar).** A hit is a designed 3-frame sequence, not a big
flash: frame 1 pure white → frame 2 the plate **inverted** (difference blend) darkened back down
+ halftone → frame 3 RGB split + speed lines. Amplitude-driven flashes wash the frame out for
6+ frames and must be avoided. Pair with camera shake and a zoom punch, all decaying from one
impulse envelope per kick.

**9.9 Speed ramps.** Echo trails: draw the previous 2–3 frames behind the current one at −33 ms
steps, alpha ~0.3/k, with their own camera values. Three frames of echo reads as a real ramp.

**9.10 Beat grid.** For music-driven films: `BPM → BEAT = 60/BPM`, cut times snapped to the real
kick/clap list (write `BEATS.json`), and a structural map (intro / build / drop / outro). Builds
accelerate: 0.4 s cuts → 0.2 s cuts → 0.1 s cuts into the drop; the drop holds longer shots so
the action is readable. Music and picture must share one clock.

**9.11 Everything else** (colour: one accent per film; depth: parallax between layers rather
than "3D"; grade stack, §11.6).

---

## 10. TRANSITIONS (CapCut + Alight Motion, natively implemented)

**10.1 The library.** `viz/motion_library.js` ships **24 transitions** behind
`makeTransitions(bufA, bufB)` — official CapCut names with their real default durations, e.g.
Signal Glitch 2 (0.67) · Fold Over (1.00) · Push Away 2 (1.00) · Zoom to Change (0.80) ·
Dissolve 叠化 (0.50) · White Flash (0.40) · Cutout Flip (0.80). Signature:
`TRANS[name](ctx, u, w, h)` where `u: 0→1` is the transition progress.

**10.2 Choosing for a cut (from the official catalogue).** `tools/data/capcut_*.json` holds
**4,173 items across 8 libraries** (transitions 1,130 · scene effects 1,582 · filters 454 ·
character effects 251 · video intros 250 · video outros 217 · text intros 182 · group animations
107), of which **891 are free** (`paid === false`) and 3,282 VIP. Record fields are
`api_name, display_name, duration_s, effect_id, resource_id, paid, is_overlap`. Real durations
cluster hard (2.0 s, 1.0 s, 0.5 s, 0.8 s) — use the catalogue's own `duration_s` unless the edit
needs otherwise. Free staples: **White Flash 0.40 · Fold Over 1.00 · Cutout Flip 0.80 ·
叠化 0.50**. 87 % of transitions are VIP (147 of 1,130 free): filter `paid === false` when building
drafts for a free account, and never strip VIP tags — that is the app's store, not ours to change.

**10.3 Cut placement rule.** A cut starts when the **outgoing narration line ends** and lasts its
catalogue duration; the incoming narration must begin on a clean frame. In practice:
`cutStart = sceneStart − 0.55` (the 0.55 s is the lead-in constant from measured timelines).

**10.4 The caption rule at cuts.** Captions are a separate layer: skip them inside the transition
composite; cross-fade them outside with overlap (§9.6).

**10.5 The snap-back bug (must not recur).** If a cut finishes *before* the incoming scene's
nominal start (short transitions do), a naive "last scene whose start has passed" rule draws the
**outgoing** scene for the last 1–4 frames. Fix: `dominantIndex(t)` — after a cut's midpoint the
incoming scene owns the frame even before its start; plus `capAlpha()` continuity so the caption
does not flicker.

**10.6 Path A (finish in the app).** `tools/capcut_draft.py` writes `draft_content.json` +
`draft_meta_info.json` + local media (transitions attach to the **preceding** segment; newer
CapCut builds may write non-plaintext draft files); `tools/alight_project.py` writes scene XML
(media before elements, unique ascending ids, `<transform>`, typed properties, keyframes as
`<kf t v e>` with cubic bezier easing, canonical effect ids like
`com.alightcreative.effects.gaussianblur`). Alight's adjustment-layer grade order is adopted for
us: copy background → duotone → exposure → glow → finishing (sharpen/vignette/noise).

---

## 11. TECHNICAL CONTRACTS

**11.1 `viz/hrender.py` — the only renderer.**
```
python3 viz/hrender.py <film.html> <out.mp4>
    [--audio audio/master.wav] [--crf 18] [--preset medium]
    [--start S] [--end S]                 # re-render a range
    [--max-samples 8] [--samples N]       # adaptive vs fixed sub-frames
    [--jpeg]                              # faster stills; avoid on dark gradients (banding)
    [--stills "1.2,7.5,18.0"]             # PNG stills + contact sheet -> dir
    [--beats 1.0]                         # one still every N s -> contact sheet
    [--check]                             # run motion_report on the result (prints JSON)
```
Always run it through `start_process` (long jobs), never a foreground `bash` call. It waits on
`window.ready === true` with a long timeout — one page error means a silent 120 s+ timeout, so
run a page-error probe first (§16 F2).

**11.2 The film HTML contract.**
- Stage: `#root` or `<canvas>` at exactly **1080×1920**, opaque background (no white flash).
- `window.seek(t)` — **required**, draws the frame at t; pure function of t; may be async.
- `window.ready` — **required**, `true` after fonts *and* images are loaded (await
  `document.fonts.ready` and every `img.onload` before setting it).
- `window.DURATION` — required (seconds); `window.FPS` / `WIDTH` / `HEIGHT` optional (30/1080/1920).
- `window.speed(t)` — fastest on-screen speed in px/s (drives motion blur); `window.state(t)` —
  signature of everything visible (safe frame reuse).
- CSS: `@font-face` pointing at `../../brand/fonts/*.ttf`; engine via
  `<script src="../../viz/motion_library.js">`.
- Determinism: no `Math.random`, no `Date`, no cross-frame state. Every random value is seeded.

**11.3 `viz/motion_library.js` exports** (global `window.MotionEngine`):
`Ease` (linear, outQuad, inQuad, outCubic, inCubic, inOutCubic, outQuint, outExpo, outBack,
outElastic) · `spring(t, mass, stiffness, damping, v0)` · `clamp` · `lerp` · `mulberry(seed)` ·
`hash` · `vnoise` · `noise1` · `wobble` · `mk(w,h)` (offscreen canvas) · `tint(src,color,keepAlpha)`
· `blurCanvas(src,k)` · `bloom(c,src,w,h,strength,radius)` · `chromatic(c,src,w,h,px)` ·
`lightWrap(c,bg,x,y,w,h,amount)` · `vignette(c,w,h,amount)` · `grain(c,w,h,frameIndex,amount)` ·
`makeTransitions(A,B)`.

**11.4 Transition-buffer pattern.** If a film uses cuts: keep two offscreen buffers
`bufA/bufB`; on a cut frame, render the outgoing and incoming scenes into them (with captions
skipped), composite through `TRANS[name]`, then draw captions + overlays on top. Outside the cut
window, render the dominant scene directly to the stage — with the *same* camera function so
there is no visual jump at the boundary.

**11.5 Composition helpers worth rebuilding in every project** (they paid for themselves):
`bg()` (gradient + drifting grid + orbiting glows) · `atmos()` (dust + sweep) · `txt()` (letter
spacing support) · `fitText()` / `wrapText()` · `roundRect()` · `chip()` · `caption()` ·
`sourceTag()` (mono, dim, bottom-left) · `brand()` (top-left wordmark + INDIA) · `qrBlock()` ·
`impulses(t)` (decaying shake/punch/rgb/flash/lines per hit) · `shakeOf(t)` (seeded) ·
`speedLines()` · `impactFrame(t)`.

**11.6 The grade stack — house order, every frame:**
composite → **bloom** (blur of the stage, `lighter`, α≈0.10–0.28) → **vignette** (darken the
corners, never ring the subject) → **grain** (seeded, α≈0.04–0.06). Optional per-scene: chromatic
aberration on hits, halftone on impact frames, additive light wrap on bright subjects.
Alight's documented order agrees: exposure → glow → finishing.

**11.7 Data-URI baking.** For a single-file film: cover-fit each plate to exactly 1080×1920
(avoids runtime upscaling), save JPEG q≈92, base64 into the HTML, then assert no placeholder
token survives. Keep the template + baker (`bake_film.py`) so the film can be rebuilt without
regenerating art.

**11.8 Render cost budgeting.** Expect roughly: 125 s film @8-pass ≈ 22–25 min; 15 s edit film ≈
10 min; ambient layers add ~40 % time and can double file size at the same CRF. Budget for it,
and note that a full-quality ambient pass is *the* thing that removes dead frames — never trade it
away for speed on a delivery render.

---

## 12. AUDIO PIPELINE (exact recipe)

**12.1 Voice.** `add_voice` audition (hi) → user picks → `generate_speech` per narration block
(≤1500 chars per call; batch parallel calls at sentence boundaries for long text). Devanagari for
Hindi, phonetics for tricky English/handles. Keep one `voice_id` for the whole film.

**12.2 Measure, never assume.** Convert clips to 48 kHz mono WAV; measure with python `wave`;
`TIMELINE.json` holds `narration_at`, `start`, `dur`, `vo`, `total`. Scene duration = narration +
lead-in (0.55) + gap (1.15) + tail (2.90) as the house constants (tune per film, but derive them
from measurements, not from a target runtime).

**12.3 Build the master in numpy** (not in the video tool): place each VO at its measured time;
add one **distinct** SFX per cut (different character each — glitch burst, whoosh, thud, click);
optional tick bed under a "scale" scene at a true-rate ÷ 200; optional low bed (55/82.5 Hz); apply
a sidechain duck (≈0.25) under speech; 0.35 s fades; **peak-normalise in numpy first** (sample
peak, e.g. −2.0 dBFS).

**12.4 Loudness — two passes, linear, then mux with video copied.**
```bash
ffmpeg -nostats -i audio/master.wav -af loudnorm=I=-14:TP=-1.5:LRA=6:print_format=json -f null -   # pass 1: read measured_*
ffmpeg -v error -y -i audio/master.wav -af "loudnorm=I=-14:TP=-1.5:LRA=6:measured_I=…:measured_LRA=…:measured_TP=…:measured_thresh=…:offset=…:linear=true" audio/master_loud.wav
ffmpeg -v error -y -i film.mp4 -i audio/master_loud.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 192k -ar 48000 -shortest final.mp4
```
Targets: **−14 LUFS integrated** for Shorts (a −20 LUFS mix plays quiet next to other Shorts),
true peak ≤ −1.5 dBFS, LRA 3–5 LU for narration, higher only for wall-of-SFX edits.
Measure the *muxed* file with `-filter:a ebur128=peak=true` and report the numbers.

**12.5 Verified traps.**
- `alimiter` lets transients through **4–6 dB over its own limit** — do not try to hit a loudness
  target with a bare limiter; use `loudnorm`.
- `ebur128`'s reported peak is not true-peak safe by itself; normalise in numpy, then `loudnorm`.
- Music beds: −24 to −28 LUFS under narration, ducked. For edit films: music *is* the bed,
  target −14 LUFS with the hits exposed.

**12.6 SFX spec.** Distinct and audible without masking speech: cut whooshes 0.3–0.5 s, impact
thuds 0.2–0.4 s with a HF transient, tick trains at the true event rate for "scale" moments.
Never place an SFX where it competes with a spoken number.

---

## 13. EDIT-STYLE FILMS (the "anime edit" recipe, generalised)

**Copyright boundary (non-negotiable).** No ripped anime footage, no existing characters/IP, no
copyrighted songs. Build **original art + original music**, then apply real edit grammar. If the
user supplies their own licensed clips, cut those on the same beat map.

**13.1 Structure** (15 s example, 150 BPM, drop at 6.4 s):
intro (0–3.2, title slams) → build (3.2–6.4, cuts 0.4 s → 0.2 s → 0.1 s with echo trails) →
**drop** (impact frame 1 white → 2 negative+halftone → 3 RGB split) → drop section (held shots,
shake per kick) → outro (second lift, reprise title, CTA).

**13.2 Recipe.**
1. `generate_image` — 4–6 original plates, 9:16, consistent character/lighting (hero, close-up
   eye, action slash, silhouette/moon, …). Prompt for anime key-visual look; no text in images.
2. `make_music.py` in numpy: kick/808 (tanh-saturated sine sweep), clap (multi-burst noise +
   tone), hats (differentiated noise), cowbell melody, sub line, riser, impact — arranged in bars
   with a real intro/build/drop/outro → `audio/beat.wav` → `BEATS.json` (kicks, claps, hats,
   sections, drop time).
3. Loudness the music to −14 LUFS / TP −1.5.
4. Shot list: each shot = plate + z0/z1 zoom + x/y drift + rotation + easing + echo amount.
   Cut times land on kicks/claps. Build section cuts fast; drop holds longer.
5. Impulse engine: one decaying envelope per hit → shake + zoom punch + RGB split + flash + speed
   lines. Impact-frame sequence for the section boundaries.
6. Typography: CJK glyphs slammed on the beat (scale 3.0→1.0 in 0.12 s, shadow, outline echo),
   vertical side text, optional subtitle line under a title.
7. Grade: bloom + vignette + grain; end fade.
8. `bake_film.py`: inline plates as JPEG data URIs + inject `BEATS.json` + assert no placeholders
   remain → render → QA.

**13.3 QA specifics for edits.** `motion_report` will list pops at every intentional hit — that is
correct; pass the cut times as `cuts=` to `motion_report` to confirm only intended discontinuities
remain. still_ratio should be ~0.0. Check the 3 impact frames of each boundary at 1/30 s spacing
from the **encoded** file, not the HTML.

---

## 14. QA GATES (nothing ships before these)

**14.1 Structural plan gate.**
```bash
python3 tools/peak_detail_gate.py PLAN.json --root . --report _qa/peak_detail_report.json
```
`PLAN.json` requires: `duration` (with `duration × fps` = whole frames), `fps`, `width`, `height`,
`assets{}` (path/role/rights_note, files must exist inside the root), `claims{}`
(statement/unit/qualification/source_url http(s)), and `shots[]` — each with `id, purpose, hero,
start_state, end_state, primary_motion, secondary_motion, camera, audio, transition, acceptance`
plus `asset_roles[]`, `detail_choices[]`, `claims[]`, `assets[]`; shot ranges contiguous from 0 to
duration. Output states honestly: `visual_quality` / `factual_accuracy` / `licence_validity`
are **NOT ASSESSED** by this tool.

**14.2 Motion gate (`hrender --check` → `motion_report`).**
- **freezes:** windows ≥0.8 s where <0.2 % of pixels change by >2 % (on a 90×160 gray probe —
  it is a *local* metric, so one small moving element counts). Target: **none**. A deliberate
  end-of-beat hold ≤1.5 s is acceptable if you say so.
- **pops:** frames whose mean difference > 3× their neighbours and not inside a declared cut.
  Any pop outside a cut window is a bug (usually a scene snap-back or a mis-timed flash).
- **still_ratio:** overall share of still frames. House bar: **≤0.20** after the ambient pass;
  a film at 0.78 is dead and must not ship.
- Query it directly when needed: `python3 -c "import viz.motion as M; …"` with `cuts=[…]`.

**14.3 Frame craft pass (human eyes, full size).**
- Text: nothing overflows its box, nothing collides, Hindi legible at 25 % scale on a phone,
  numerals exact with units and sources present where facts appear.
- Composition: one idea per frame, ≤3 subject groups, safe zones respected.
- Motion: every frame alive (compare two stills 1 s apart), no accidental stillness, no jitter.
- Continuity: camera consistent, no jump at cut boundaries, caption band continuous.
- Loop seam: last frames match frame 0 if the film is a Short that loops.
- Blind-read check: the thesis must be recoverable from stills + on-screen text alone.

**14.4 Harsh-director pass.** Write the 3 worst problems with timestamps, fix them, re-render
just those seconds (`--start/--end`), and confirm.

**14.5 Delivery gates.** MP4 verified with `ffprobe` (codec/res/fps/duration) and
`ffmpeg -v error -i out.mp4 -f null -` (clean decode); audio measured on the muxed file
(LUFS/TP/LRA); 6–12 frames extracted from the encoded file and inspected; file size sane
(<60 MB for a 2-min Short at CRF 18–19).

**14.6 Peak-detail eight passes** (for anything ambitious): 1 editorial truth · 2 composition &
hierarchy · 3 asset & image craft · 4 meaningful primary motion · 5 secondary motion & physical
coherence · 6 transition & continuity · 7 sound & speech · 8 finish & performance. Each pass has a
question; if the answer is weak, fix it before the next pass.

---

## 15. DELIVERY & PACKAGING

**15.1 Files per film.** `<Film>.mp4` (delivery) · `<Film>.html` (the editable film) ·
`audio/` · `TIMELINE.json` · `PLAN.json` · `SOURCES.md` · `SCRIPT.md` · `MOTION_PASS.md` ·
`AUDIO_NOTES.md` · `README.md` · `QC_*.jpg`. Present the MP4 with `present_file` and state specs
+ decisions + what was not verified.

**15.2 Upload pack (every delivery — MANDATORY UNPACKED STANDARD).**
- **Unpacked Delivery Rule:** All deliverable files MUST exist as standalone, unpacked files at the project root / `delivery/` directory. In the final report to the user, the AI MUST explicitly display the thumbnail (via markdown image embed) and paste the title, description, and hashtags directly into the chat response. Never bury deliverables solely inside a ZIP archive.
- **Titles:** 3 options, <60 characters, curiosity + clarity, no bait-and-switch, no quotes (`title.txt`).
- **Description:** 2 punchy lines + 1 debate question. **No brackets of any kind** — `( ) [ ] < > { }`
  are banned in `description.txt` and pinned comments. Check length with `wc -c` (≤5,000).
- **Hashtags:** 5–15, mix of `#shorts` + niche (`hashtags_and_tags.txt`).
- **Pinned comment:** the open question that drives comments (no brackets).
- **Chapters** (long-form): first 0:00, ≥3, each ≥10 s, descriptive.
- **Thumbnails:** 1280×720 (`thumbnail_1280x720.jpg`) + 1080×1920 (`cover_vertical_1080x1920.jpg`), 3–4 words, one big graphic, official Benaqaab logo badge.
- **Captions:** Clean timestamped SRT file (`headline_captions.srt`).

**15.3 Reporting style.** Concise Hinglish; lead with what is delivered and where; give measured
numbers (duration, frames, size, LUFS, peak) — never "looks great"; list decisions; list what was
NOT verified or what failed; offer the next concrete step.

---

## 16. FAILURE CATALOGUE (symptom → cause → fix)

**F1 · "Syntax error somewhere in the film."** → `node --check` on the extracted `<script>`
content. Note: a single bad token (`size=96` instead of `size:96` in an options object) kills the
whole page. Fix, re-check, then probe.

**F2 · Render hangs then times out.** → `hrender` waits on `window.ready`; a page error means it
never fires. Always run a Playwright probe first: `goto file://…`, capture `pageerror`, then
`wait_for_function('window.ready===true')`, and print DURATION/errors.

**F3 · Silent patch failures.** → `python str.replace()` returns the string unchanged when the
pattern doesn't match — it does not raise. After any multi-edit patch, **grep for the new
identifiers** ("ok" printed is not proof). This has cost multiple builds.

**F4 · Caption ghosting / empty caption band.** → text was composited inside the transition, and
the two caption fades did not overlap. Fix: `__capSkip` inside the composite; out
`1−(u−0.15)/0.35`, in `(u−0.40)/0.35`.

**F5 · Old scene flashes for 1–4 frames after a short cut.** → cut finished before the incoming
scene's nominal start. Fix: `dominantIndex(t)` + `capAlpha(i,t)` (§10.5).

**F6 · 77 % of frames "frozen" but every still looks fine.** → the metric is local and long holds
kill it. Fix: the ambient motion pass (§9.7). Verify with a local probe on 3 s windows before the
full re-render, and expect the file size / render time to rise.

**F7 · Impact frames are a white/cream mush.** → amplitude-driven flash for many frames, and a
difference blend followed by a black fill that does nothing (difference with black is identity).
Fix: designed 3-frame sequence; black fill AFTER resetting to `source-over`; halftone at ~0.2 α.

**F8 · Loudness pass overshoots.** → `alimiter` transients. Fix: two-pass `loudnorm` (§12.4), and
mux with `-c:v copy`.

**F9 · ffmpeg/Playwright/chromium missing after a sandbox reset.** → `bash setup.sh` via
`start_process`; wait for `[setup] OK`.

**F10 · Light "flash" frames in a `--stills` contact sheet that look like blown highlights.** →
that's the impact frame; don't "fix" it. Verify the sequence at 1/30 s spacing.

**F11 · Render is far slower than the estimate.** → adaptive sampling is doing its job (fast
motion = more sub-frames); ambient layers also slow capture. Watch `captures` and `avg samples`
in the log; don't lower `--max-samples` below 6 for fast films (ghosting).

**F12 · Determinism check fails ("frame differs").** → `Math.random`/`Date`/cross-frame state.
Seed every random (mulberry), key reuse off `window.state(t)`.

**F13 · Fonts missing on a CJK/diacritic film.** → the film must carry its own font (copy the
`.ttc`/`.ttf` into the project and `@font-face` it) — never rely on a system font being present
after a reset.

**F14 · A number on screen no longer matches its source.** → re-verify every figure at build time
against `SOURCES.md`; if the source window has changed, update the on-screen date and the VO.

**F15 · User repeats a request.** → identical requests arrive when the previous response wasn't
seen. Re-verify the workspace state and re-present the deliverable; do not rebuild from scratch.

---

## 17. COPY-PASTE TEMPLATES

**17.1 New-film brief (what a good request looks like / what to generate for yourself).**
```
TOPIC:            <one line>
WHY NOW:          <timeliness or evergreen reason>
ANGLE (1 line):   <the sneaky-simple truth>
RUNNING EXAMPLE:  <one concrete case the whole film follows>
MEMORABLE LINE:   <one sentence, repeatable>
HOOK (rec):       <type A/B/C + the actual line>
PAYOFF:           <what the viewer gets at the end>
OPEN QUESTION:    <the loop + pinned-comment question>
LENGTH TARGET:    derived from measured VO, cap 2:00
CLAIMS:           <numbers + sources + dates>
NON-CLAIMS:       <what we will NOT assert>
```

**17.2 Script table (Shorts).**
```
| Time | Voiceover (Hindi/Hinglish, ≤10 words) | On-screen text (≤6 words) | Visual₁ → Visual₂ | SFX | Source tag |
```

**17.3 Shot-detail card (peak detail).**
```
SHOT <n> <start–end>: purpose | hero element | start state | end state |
primary motion | secondary motion | camera | audio | transition | acceptance test
```

**17.4 `PLAN.json` skeleton.**
```json
{ "duration": 125.86666666666666, "fps": 30, "width": 1080, "height": 1920,
  "assets": { "film": { "path": "Film.html", "role": "…", "rights_note": "…" } },
  "claims": { "c1": { "statement": "…", "unit": "…", "qualification": "…",
                      "source_url": "https://…" } },
  "shots": [ { "id":"S1","purpose":"…","hero":"…","start_state":"…","end_state":"…",
               "primary_motion":"…","secondary_motion":"…","camera":"…","audio":"…",
               "transition":"…","acceptance":"…","asset_roles":["…"],
               "detail_choices":["…"],"claims":["c1"],"assets":["film"],
               "start":0,"end":11.471 } ] }
```

**17.5 Decision log (delivered with the film).**
```
DECIDED: palette/type/transition family; why; the numbers I derived; the timing constants used;
what I cut for time; what I'd change if the user wants a different vibe.
NOT VERIFIED: <list>.
```

**17.6 Upload pack.**
```
TITLE (pick 1 of 3, <60 chars): …
DESCRIPTION (2 lines + question, NO brackets): …
HASHTAGS (5–15): …
PINNED COMMENT (question, NO brackets): …
THUMBNAIL: 1280×720 + 1080×1920, 3–4 words
```

---

## 18. QUICKSTART (copy-paste run sheet)

```bash
# 0. environment
start_process: bash /home/user/setup.sh > setup.log 2>&1        # expect [setup] OK
# 1. read the mission
cat MEMORY.md | tail -200 ; cat knowledge/topic_ideas/NEW_TOPIC_SHORTLIST_2026-10.md
# 2. script + sources in the project folder
mkdir -p projects/<film>/audio
# 3. VO: add_voice (audition, one pause) -> generate_speech xN -> convert + measure
ffmpeg -v error -y -i vo_1.mp3 -ar 48000 -ac 1 audio/vo_1.wav
python3 -c "import wave;w=wave.open('audio/vo_1.wav');print(w.getnframes()/w.getframerate())"
# 4. timeline -> film HTML (single file, deterministic) -> page-error probe -> stills
python3 viz/hrender.py Film.html _qa --stills 1.2,7.5,18.0,33.5,55.0
# 5. audio master (numpy) -> loudnorm two-pass -> mux
# 6. full render + check
start_process: python3 viz/hrender.py Film.html Film.mp4 --audio audio/master.wav \
               --crf 18 --max-samples 8 --check
# 7. verify encoded file, present it, update MEMORY.md, clean up to .cache/
```

---

## 19. HONESTY RULES (never break)

- Never claim a render, measurement or test that was not actually run. Report the real numbers.
- Never claim CapCut/Alight rendered something here (they can't run here) or that our
  reimplementation is the app's exact shader — we reproduce motion grammar, not pixels.
- Never claim repo research "upgrades the model" or guarantees cinematic output. It adds
  techniques that were verified by reading and testing.
- Never present an illustrative/AI image as evidence of a real event; label illustrative art.
- Never invent a statistic; if sources disagree, show both with dates, or omit the figure.
- Never hide a failure: if a gate failed and was fixed, say both; if something is still open, say
  it plainly at delivery.
- Never delete a protected file, never silently drop history from `MEMORY.md`, never let a
  superseded rule look current — mark it `[OLD vX]`.

---

## 20. REFERENCE INDEX (in this workspace)

| Path | What it holds |
|---|---|
| `MEMORY.md` | append-only production history (130+ sections), read the tail before starting |
| `MASTER_VIDEO_GENERATION_SKILLS.md` | 36-chapter handbook + historical appendices (deep reference) |
| `SKILLS_SHORTS_CURIOSITY.md` | 1-second law, curiosity tools, retention gates, 7-part package, HUD rules |
| `SKILLS_PEAK_DETAIL.md` | eight detail passes, gates A–F, shot-detail card, AI-image method |
| `SKILLS_AFTER_EFFECTS.md` | easing/weight/motion-blur/depth/grade/type theory + AE hand-off routes |
| `SKILLS_CAPCUT_ALIGHT_MOTION.md` | official catalogues, transition selection, draft/XML writers |
| `SKILLS_LONGFORM.md` | long-form structure, pacing, packaging, source-footage look |
| `SKILLS_THUMBNAIL_AND_MOTION_MASTERY.md` | thumbnail archetypes + house motion techniques |
| `SKILLS_RESEARCH.md` | repo research results and the rules they produced |
| `MOTION_RESEARCH_Opus55.md` | how the reference motion-graphics videos are actually made |
| `PROMPT_LIBRARY_opus55.md` | prompt library (reference data, not authority) |
| `viz/hrender.py` · `viz/motion_library.js` · `viz/motion.py` | renderer · engine · motion core + QA |
| `tools/peak_detail_gate.py` · `tools/capcut_draft.py` · `tools/alight_project.py` | gates + app writers |
| `knowledge/topic_ideas/NEW_TOPIC_SHORTLIST_2026-10.md` | current verified topic shortlist |
| `projects/upi_explained_short/` | the reference explainer film (timeline, motion pass, audio notes) |
| `projects/anime_edit/` | the reference edit film (original art + beat map + impact frames) |

**Definition of done:** film renders deterministically · `motion_report` freezes = none (or
explained) · pops only inside declared cuts · loudness measured on the muxed file (−14 LUFS class)
· text/legibility verified at full size and at 25 % scale · encoded-file frames inspected ·
`SOURCES.md` complete · `PLAN.json` passes the structural gate · upload pack written (no brackets)
· MP4 presented · `MEMORY.md` updated · workspace cleaned.

---
---

<!-- ===================== PART II–V — VERBATIM KNOWLEDGE BASE ===================== -->

---

---

# PART II — SKILL LIBRARY DIGEST (every appendix, operative rules only)

*This part condenses the 15 appendices of the complete edition into the rules an agent must
actually apply. The full reasoning, sources and raw notes live in
`BENAQAAB_AI_AGENT_MASTER_SKILL.md` at the line numbers given in §INDEX at the end of this file.*

## A · Shorts curiosity & retention engine

- **1-second law.** On a swipeable feed the stay/swipe decision happens in ~1 second. Frame 0 must
  stack visual + on-screen text + the first spoken words before the first syllable finishes.
- **Core feelings (1–2 s):** (a) "I need the answer to this" · (b) "this affects me" · (c) "that's
  surprising, I don't believe it".
- **7 curiosity tools — use 2–3 every film:** open loop · information gap · pattern interrupt ·
  stakes · specificity (exact numbers/names/dates) · promise + proof (evidence at 2–7 s) · loop
  ending (last line flows back into frame 0).
- **Retention gates:** Gate 1 at **2.5–3.0 s** (strongest proof/twist lands here — decides
  swipe-away) · Gate 2 at **14–15 s**, then a mini-hook every ~10–12 s ("par asli twist abhi
  baaki hai…").
- **5-beat suspension bridge:** hook → spine → contrast/mechanism → payoff → loop + ask. Cut
  rhythm uneven (2.5–5.5 s), never a metronome; **zero dead air > 2.2 s**.
- **Dual-visual sentence switch:** every spoken sentence gets TWO visual states (start → end/twist).
  Concrete/literal visuals only — never an abstract mood image for a concrete claim.
- **7-part pre-production package** (Part I §6.5): topic+angle · 3 hooks + recommendation · full
  script table · fact-check list · metadata · frame-0 design · retention score + Script Doctor.
- **Script Doctor:** 2-pass architecture; pass 1 writes the structured script
  (`WORDS_PER_SECOND = 2.6`, `hook_text` ≤ 6 words, `title` ≤ 60 chars), pass 2 scores it 0–100
  across first-2s hook, curiosity gaps, pacing, specificity, payoff, accuracy risk — **ship ≥ 85**,
  rewrite anything under 8/10 on Hook / Pacing / Payoff / Loop.
- **11 proven short formats:** facts · story · listicle · myth (myth vs fact) · quiz · news ·
  explainer · dialogue (2-speaker A/B) · chat · reddit · motivational.
- **Scene energy map:** give every scene an explicit energy + purpose along an arc
  (mystery → tension → revelation → satisfaction, etc.).
- **Diversity gate:** block a script where `repeated_sentence_ratio > 0.10`, where consecutive
  scenes open with the same word, or where two scenes share the same visual subject / camera
  angle / palette.
- **Packaging from this skill:** 3 title options < 60 chars · description = 2 lines + 1 debate
  question · 5 hashtags · pinned comment = the open question · frame 0 = layout + 3–6 word
  sharpener + badge.
- **Post-upload loop:** when the user shares analytics (views, avg view duration %, swipe-away in
  first 3 s, which hook), analyse the 3-second swipe-away rate and append the lesson to MEMORY.
- **HUD discipline** (also in Part I §8.2): one glass card, minimal cells, tiny logo, no dashboard
  clutter, speaker ≤ 2 s in full screen if at all.

## B · Peak detail — the eight passes and the gates

Run these passes in order for anything ambitious; each has one question — if the answer is weak,
fix it before advancing.

1. **Editorial truth** — is every claim sourced, dated, and is the disagreement shown?
2. **Composition & hierarchy** — one idea per frame, ≤3 subject groups, safe zones held?
3. **Asset & image craft** — is each asset the right kind and quality (code-drawn vs photo vs 3D)?
4. **Meaningful primary motion** — does the hero motion explain the mechanism?
5. **Secondary motion & physical coherence** — do weight, springs and timing feel physical?
6. **Transition & continuity** — do cuts carry an element, and does nothing snap back?
7. **Sound & speech** — VO timing, ducking, SFX meaning, loudness measured?
8. **Finish & performance** — bloom/vignette/grain, determinism, render cost, delivery gates?

- **Minimal stack:** choose the smallest tool set that does the job (house default: HTML canvas +
  `viz/motion_library.js` + `viz/hrender.py`; Python/Pillow only for the motion core and stills).
- **AI image prep method:** generate at the right aspect, cover-fit before render (never runtime
  upscale), keep plates in the project, inline as data URIs when the film must be one file.
- **Rejected third-party absolutes (do not adopt):** no-linear-interpolation absolutism, Ken Burns
  on every still, idle per-element breathing, a mandatory mesh-gradient layer stack, a ban on hard
  cuts or intentional stillness, universal stagger.
- **Also enforced:** `PLAN.json` + `tools/peak_detail_gate.py` before rendering, and the six quality
  gates A–F (preproduction, frame craft, moving result, sound, determinism & delivery, harsh
  director pass).

## C · After Effects mastery (theory that ports to any pipeline)

- **0 — boundary:** AE cannot be installed here; learn the craft and encode it. Never claim AE
  rendered anything in this workspace.
- **What makes AE output look "wow" (in order of impact):** easing discipline → weight/physicality
  → motion blur → depth → the grade stack → type in motion. Not plugins.
- **Easing:** four named curves only (ARRIVE/SETTLE/SWEEP/CUT — Part I §9.1); entrances ≤ 600 ms,
  exits ~250 ms; the single biggest visual upgrade available.
- **Weight:** closed-form springs; anything physical settles, nothing floats in linearly.
- **Motion blur:** a real 180° shutter (temporal integration) — our renderer implements it; the
  "velocity blur" filter is not the same thing.
- **Depth:** parallax between layers > fake 3D; atmosphere (haze, bloom, grain) at different depths.
- **Grade stack order (adopted):** composite → bloom → vignette → grain, plus optional chromatic
  aberration / halftone on hits (Part I §11.6).
- **Type in motion:** masked word rise, 55–70 ms stagger, ≤6 words per line, outgoing text gone
  before incoming arrives; kinetic numbers with tabular figures.
- **Expressions worth knowing (portable ideas):** accumulators (a value that keeps what you add),
  camera snap, counters, and easing-by-expression — these are the behaviours the engine's
  `spring()`, `Track` patterns and `counter` helpers reproduce.
- **Four real AE hand-off routes:** (1) AE → Lottie JSON → web player (vector/logo motion);
  (2) AE → alpha-rendered frames → our compositor (heavy VFX); (3) AE → aerender → nexrender
  (many videos from one template); (4) AE project → JSON → rebuild natively (max control,
  most work).
- **Critique checklist:** real motion vs decoration; one dominant direction per film; continuity
  across cuts; nothing appearing before its word; legible at 25 % scale.

## D · CapCut + Alight Motion (and how we implement their language natively)

- **Boundary:** neither app runs here. Two honest deliverables: Path A = draft/XML files the user
  imports into the real app; Path B = the official transition grammar reimplemented in our engine
  (`viz/motion_library.js`, 24 transitions) and rendered here. Never claim app-rendered output or
  exact shader parity.
- **Official catalogue (corrected figures):** `tools/data/capcut_*.json` — **4,173 items across 8
  libraries** (transitions 1,130 · scene effects 1,582 · filters 454 · character effects 251 ·
  video intros 250 · video outros 217 · text intros 182 · group animations 107); **891 free**,
  3,282 VIP. Fields: `api_name, display_name, duration_s, effect_id, resource_id, paid,
  is_overlap`. Filter `paid === false` for free-account drafts; never strip VIP tags.
- **Free staples + real durations:** White Flash 0.40 · Fold Over 1.00 · Cutout Flip 0.80 ·
  叠化 0.50. Cardinal durations cluster at 2.0 s / 1.0 s / 0.5 s / 0.8 s — use the catalogue's
  own `duration_s` unless the edit demands otherwise.
- **Selection guidance:** match the cut's emotional job — flash for impact beats, fold/roll for
  scene-to-scene continuity, dissolve for time passing, push/pull for escalation, glitch for
  error/reversal. Cuts start when the outgoing narration line ends (Part I §10.3).
- **Path A rules (must not break):** CapCut drafts = `draft_content.json` + `draft_meta_info.json`
  + local media; a transition attaches to the **preceding** segment; newer builds may write
  non-plaintext drafts. Alight = scene XML: `media` before elements, unique ascending ids,
  `<transform>`, typed properties (float/int/color/vec2-4/quat/bool/uri/string), keyframes
  `<kf t v e>` with cubic-bezier easing, canonical effect ids (`com.alightcreative.effects.*`).
  Unspecified end times default to the scene `totalTime` (a zero-length element is a bug).
- **Alight's documented grade order, adopted for us:** adjustment layer with Copy Background
  (`com.alightcreative.effects.lift`, fill 0, canvas/100 scale) → duotone → exposure → glow →
  finishing (sharpen / vignette / noise).
- **Honest limits:** 196 documented effects across 12 categories, 24 blend modes, 7 layer types,
  20 parametric shapes; looks are still the app's shaders — we rebuild motion grammar, not pixels.

## E · Long-form (when the film is not a Short)

- **Format:** 1920×1080, 30 fps, max 5:00, target 3:30–4:30. Presenter not permanent — intro hook
  ≤ 8 s, 1–2 key moments, outro; keep the face under ~20 % of runtime.
- **First 30 s (a ranking input):** cold open on the most surprising fact/visual; promise by
  15–30 s; visual change every 3–7 s; first deliberate pattern interrupt at 25–35 s; within 5 s the
  picture must confirm what the title and thumbnail promised.
- **Structure:** 0:00–0:20 cold open + promise · 0:20–0:40 dated context · 3–4 chapters of 45–75 s
  (mini-hook → explanation → PROOF → mini-payoff) · re-hook at ~50 % · final payoff circles the
  opening question (never "in summary") → CTA ≤ 10 s.
- **Pacing:** visual change every 10–20 s early, 25–40 s later; a BIG pattern interrupt every
  60–90 s by switching scene type; J/L cuts (next visual leads VO by ~0.3 s); no dead air.
- **Scene vocabulary:** animated charts (one scale per comparison), schematic maps (no national
  borders unless Survey-of-India compliant — use city dots and routes), timelines, orbit/process
  diagrams, kinetic type, purposeful punch-ins on real photos/footage, split screens, document
  zooms, ≤1.5 s chapter cards, one recurring anchor motif.
- **Audio:** VO −14 LUFS; if music is approved, bed −24 to −28 LUFS ducked under the VO, change per
  chapter; SFX on motion beats; licensed/CC only.
- **Benchmarks:** 50–70 % average percentage viewed for < 5 min; ≥ 60 % still watching at 30 s;
  average view duration ≥ 50 % roughly triples recommendation odds.
- **Packaging:** thumbnail 1280×720 (3–4 words + one big number, matching the hook) · title ≤ 60
  chars · SRT captions uploaded · end screen in the last 5–20 s · chapters (first 0:00, ≥3, ≥10 s
  each, descriptive).
- **Source-footage look:** every third-party clip/photo through `viz/source_style.py` (high-contrast
  B&W + halftone + translucent red band on the eye line + vignette) so evidence is distinguishable
  from our own colourful explanation; keep clips short, credited, commentary-only.

## F · Thumbnails & the signature motion techniques

- **Never a flat text-bar screenshot.** Five archetypes: (1) dramatic AI/3D hero + one giant
  number; (2) split comparison (before/after, India-vs-world); (3) evidence wall with red-thread
  callouts onto documents; (4) minimal full-screen with 3–4 words; (5) character-led reaction
  frame. Two-stage pipeline: strong base image → programmatic type + badge from `brand/logo.png`.
  Deliver 1280×720 + 1080×1920 and keep it consistent with the hook.
- **Signature motion techniques (use several per film):** 2.5D evidence wall with red-thread camera
  flight · physical slam-down rubber stamps · kinetic multiplier equations (e.g. ₹5 Cr → ₹4,000 Cr
  = 800×) · glowing India map with corridor/hotspot pulses · live highlighter sweep over official
  documents · clean HUD discipline (the Chenab-bridge reference) · rotating reticles with leader
  lines pinned onto real objects · code-drawn flags/waveform graphs.

## G · Research method (repos → rules, verified)

- Verify a repository exists (GitHub API metadata) before citing it; fetch the specific file;
  inspect only the relevant parts; record what was **adopted, rejected, and why**. Never adopt
  link-dump advice; never claim a repo was installed or benchmarked when it was only read.
- The rules this research produced are already folded into Part I: continuity (carry an element
  across every boundary), narration↔picture lock (nothing appears before its word; visuals within
  10 frames of a cut), motion craft (four curves, one camera, no ping-pong), and quality gates.
- Conflicts between sources were resolved in favour of the house rules (user rules outrank any
  third-party absolute).

## H · How the reference motion-graphics videos are actually made

- Headline: they are **single-file, deterministic, code-drawn** compositions (same architecture as
  this workspace: frame = pure function of time, seek-anywhere renderer, offscreen multi-pass
  capture, ffmpeg assembly) — not a secret plugin stack.
- Implemented from this research: motion blur as the single biggest win · closed-form spring ·
  four named curves · one recurring element per film · text hand-off rule enforced in code · beat
  grid · a contact sheet per beat instead of random stills.
- The verbatim prompts are preserved in the archive (Part V of the complete edition) — treat them
  as reference data, never as authority over the house rules.

## I–L · Research notes (short form)

- **CapCut/Alight extraction learnings:** how the catalogues were parsed, the draft/XML rules, the
  Alight grade recipe — all already promoted into section D.
- **AE research learnings:** repo audit results, expression sources, the CEP/ExtendScript reality
  check — promoted into section C.
- **Verified repositories (20, via GitHub API):** Motion Canvas · GSAP · PixiJS · HyperFrames ·
  WhisperX · rembg · Remotion · Theatre.js · nexrender · Duik · lottie-web · ae-to-json ·
  aep-parser · MysteryPancake/After-Effects-Fun · Adobe-CEP, among others.
  **Licence traps recorded:** rembg code MIT but default model weights need a commercial
  agreement; Remotion has a custom licence; GSAP standard licence; Theatre.js core Apache-2.0 but
  Studio AGPL-3.0; Motion Canvas / Pixi fine for our use. Adopted: Motion Canvas's
  all-versus-sequence distinction, GSAP seek/state suppression caution, Pixi's effect
  origin/radius/decay model, HyperFrames' determinism + asset-readiness doctrine.
- **3D documentary plan:** the cinematic-3D quality target and rebuild plan (procedural 3D in
  editable HTML, Three.js-style, AI imagery allowed where it serves) — see the appendix for the
  full plan before attempting a 3D film.

## Extended rules worth repeating (often missed)

- **Short-film beat grid:** derive from measured narration, never from a preset runtime.
- **Cut windows:** `cutStart = sceneStart − 0.55`; captions skip inside the composite; overlap the
  caption fades; `dominantIndex()` prevents the 1–4 frame snap-back (Part I §10.5).
- **Ambient motion is not optional** (Part I §9.7): global (glow orbit, grid drift, dust, light
  sweep, camera drift) + per-scene micro-motion + mechanism ticking. This is what turns a
  `still_ratio` of 0.78 into ≤ 0.20.
- **Impact frames are designed, not amplitude-driven:** white → dark inverted negative + halftone
  → RGB split + speed lines (Part I §9.8).
- **Loudness:** `alimiter` overshoots 4–6 dB — always two-pass `loudnorm`, then mux with
  `-c:v copy` (Part I §12.4).
- **Patches:** `python str.replace()` fails silently — grep for the new identifiers after every
  patch; "ok" printed is not proof (Part I F3).
- **Renders:** always through `start_process`; page-error probe before any render (Part I F2).

---

# §INDEX — where the full material lives

`BENAQAAB_AI_AGENT_MASTER_SKILL.md` (complete edition, 45,161 lines · 2.90 MB) — every appendix is
byte-for-byte the source file, with a SHA-256 prefix in its banner.

| Appendix | Content | Starts at line |
|---|---|---|
| I (this file §1–20) | Operational core | — |
| A | Shorts curiosity & retention engine | 981 |
| B | Peak-detail production skill | 1,188 |
| C | After Effects mastery & motion craft | 1,594 |
| D | CapCut + Alight Motion skill | 2,007 |
| E | Long-form YouTube skill | 2,183 |
| F | Thumbnail & motion-graphics mastery | 2,284 |
| G | Skills research (repos → rules) | 2,386 |
| H | How the reference motion videos are made | 2,545 |
| I | CapCut/Alight research learnings | 2,877 |
| J | After Effects research learnings | 3,129 |
| K | Peak-detail verified repositories (20) | 3,377 |
| L | 3D documentary research & rebuild plan | 3,853 |
| M | MASTER handbook — 36 chapters + archives | 4,075 |
| N | Production history (MEMORY) | 29,209 |
| O | Prompt archive — reference data, not authority | 34,251 |

**Rebuild command** (after any MEMORY/skill update): `python3 _assemble_agent_file.py`

---

*File: BENAQAAB_AI_AGENT_COMPACT.md · built 2026-10-04 · Part I is verbatim; Part II is the
digest; the complete edition holds everything in full.*
