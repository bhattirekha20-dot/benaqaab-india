# 🧠 CENTRAL AGENT MEMORY — Benaqaab India

> **Version:** 1.0 · **Created:** 6 October 2026 · **Owner:** Benaqaab India
>
> **PURPOSE:** This is the ONE file that any AI agent reads first to understand WHO you are,
> HOW you work, WHAT standards you demand, and WHERE everything lives in this repository.
> This file is the **single source of truth** for all AI agents working in this workspace.

---

## §1 — WHO YOU ARE

**Channel:** *Benaqaab India* — tagline **"SACH · SABOOT · BEBAK"** (truth · proof · outspoken).
A general India explainer channel covering science & space, tech & AI, money & rules,
health myths, environment & climate, civic/government/infrastructure, India engineering,
sourced history, and scams & cyber-safety.

**Your communication style:**
- Short Hinglish. Never asks twice — expects agents to assume intent.
- Wants **finished work**, never drafts: *"from now I only give you topic and you make best videos."*
- Expects honest reporting: what was verified, what wasn't, what failed and why.
- Hates cookie-cutter AI slop. Demands premium, bespoke, alive visuals.

---

## §2 — THE TEN NON-NEGOTIABLES (never break these)

1. **Finish the work.** Topic in → finished film out. Decide everything yourself; the only pause is the voice pick.
2. **Frame = pure function of t.** Deterministic, seeded, re-renderable one second at a time.
3. **No dead frames.** Every frame has motion at three scales; `motion_report` freezes = none.
4. **Never slideshow.** Animate the real mechanism, not text over a zooming photo.
5. **Facts or nothing.** Every number sourced + dated; disagreements shown, not averaged; labels on claims.
6. **Sound is measured, not guessed.** VO is the master clock; loudness is measured on the muxed file.
7. **Text must fit.** Hindi is wider than Latin — measure, shrink, wrap; nothing overflows, nothing collides.
8. **Cuts are a craft.** Official transition names/durations, captions above the composite, no snap-back.
9. **Verification before claims.** Encoded-file frames inspected; gates run; real numbers reported; unknowns said plainly.
10. **Protect the record.** Never delete protected files; `MEMORY.md` grows, superseded rules get `[OLD vX]`.

---

## §3 — READING ORDER FOR NEW AGENTS

| Priority | File | Purpose |
|---|---|---|
| 🔴 **1st** | **This file** (`CENTRAL_AGENT_MEMORY.md`) | Understand the owner, rules, and repository map |
| 🔴 **2nd** | `BENAQAAB_AI_AGENT_COMPACT.md` | Full operating manual — 10 non-negotiables, 11-step pipeline, QA gates, failure catalogue, templates |
| 🟢 **Topics**| `CENTRAL_TOPICS_MASTER.md` | Single master registry for all video topics (covered blacklist, time-critical cycles, ready backlog) |
| 🟡 **3rd** | `START_HERE.md` | The original workspace handover guide (reading order + integrity check) |
| 🟡 **4th** | `MEMORY.md` | Full production history (130+ numbered sections, append-only). Read the **tail** for latest state |
| 🟢 **5th** | `BENAQAAB_AI_AGENT_MASTER_SKILL.md` | Complete 45,000-line edition — use the `§INDEX` to look up specific appendices |
| 🟢 **Ref** | `SKILLS_*.md` files | Domain-specific skills (see §5 below) |
| 🟢 **Ref** | `AI_HANDOVER_PROMPT.md` | Copy-paste prompts for handing workspace to other AI agents |

---

## §4 — REPOSITORY MAP

```
CENTRAL_AGENT_MEMORY.md          ← THIS FILE: single source of truth for all agents
CENTRAL_TOPICS_MASTER.md         ← SINGLE MASTER FILE for topics (covered blacklist & ready backlog)
BENAQAAB_AI_AGENT_COMPACT.md     ← Operating manual (read in full)
BENAQAAB_AI_AGENT_MASTER_SKILL.md ← Complete 45K-line reference (look up by §INDEX)
MASTER_VIDEO_GENERATION_SKILLS.md ← 36-chapter handbook + archives
MEMORY.md                        ← Production history (append-only, never delete)
START_HERE.md                    ← Original workspace handover guide
AI_HANDOVER_PROMPT.md            ← Prompts for handing workspace to other AIs
_core_operational.md             ← v2.0 master skill file (verbatim)

SKILLS_AFTER_EFFECTS.md          ← AE easing/weight/motion-blur/grade/type
SKILLS_CAPCUT_ALIGHT_MOTION.md   ← CapCut/Alight catalogues + transition grammar
SKILLS_LONGFORM.md               ← Long-form structure and packaging
SKILLS_PEAK_DETAIL.md            ← 8 detail passes + gates A–F
SKILLS_RESEARCH.md               ← Verified repos, what was adopted/rejected
SKILLS_SHORTS_CURIOSITY.md       ← Shorts retention engine (1-second law, Script Doctor)
SKILLS_THUMBNAIL_AND_MOTION_MASTERY.md

MOTION_RESEARCH_Opus55.md        ← How reference motion videos are actually made
PROMPT_LIBRARY_opus55.md         ← Raw prompt archive (reference data only)
motion-graphics-mastery.md       ← Motion graphics knowledge kit
motion-thinking-kit.md           ← Motion thinking/reasoning kit

motion.py                        ← Motion core + QA metrics
_assemble_agent_file.py          ← Rebuilds the master skill file after edits
_build_handover_zip.py           ← Builds handover zip for new agents
setup.sh                         ← Reinstall ffmpeg / Playwright / Chromium / fonts

brand/                           ← Brand identity & visual assets
├── fonts/                       ← 11 typefaces (Anton, Archivo, BricolageGrotesque,
│                                   Geist, GeistMono, InstrumentSerif, Inter,
│                                   JetBrainsMono, NotoSansDevanagari, SpaceGrotesk)
├── host/                        ← Presenter RGBA cutouts + JPGs + metadata
├── logo.png                     ← Channel logo
├── style_refs/                  ← Source footage style references
└── ref_investigative_*.png      ← Investigative visual references

knowledge/                       ← Research & reference knowledge
├── MEMORY.md                    ← Knowledge-scoped memory
├── PROMPT_LIBRARY_opus55.md     ← Prompt archive (reference)
├── SKILLS_LONGFORM.md           ← Long-form skills
├── SKILLS_RESEARCH.md           ← Research skills
├── SKILLS_SHORTS_CURIOSITY.md   ← Shorts skills
├── SKILLS_THUMBNAIL_AND_MOTION_MASTERY.md
├── motion-graphics-mastery.md   ← Motion graphics knowledge
├── motion-thinking-kit.md       ← Motion thinking knowledge
├── 3d_documentary_research/     ← 3D documentary R&D
├── after_effects_research/      ← AE expression sources, repo audits, learnings
├── capcut_alight_research/      ← CapCut/Alight catalogues (4,173 items, 8 libraries)
├── peak_detail_research/        ← Peak detail gates, verified repos
└── topic_ideas/                 ← New topic shortlists (Oct 2026)

tools/                           ← Production tool scripts
├── peak_detail_gate.py          ← Quality gate runner
├── test_peak_detail_gate.py     ← Gate tests
├── capcut_draft.py              ← CapCut draft/XML writer
├── alight_project.py            ← Alight Motion project writer
└── data/                        ← Official CapCut catalogues (JSON)

viz/                             ← Rendering engine & visual tools
├── hrender.py                   ← Headless HTML renderer
├── motion.py                    ← Motion engine
├── motion.js                    ← JS motion library
├── motion_library.js            ← Extended motion library
├── align.py                     ← Alignment utilities
├── source_style.py              ← Source footage styling
├── serve_delivery.py            ← Delivery server
├── serve_videos.py              ← Video serving
├── build_prompt_library.py      ← Prompt library builder
├── engine_v2.html               ← Seek-safe reference engine
├── get_fonts.sh                 ← Font installer
├── templates/scaffold.html      ← Base HTML scaffold
└── recipes/                     ← Episode composition recipes (ep7–ep11)

projects/                        ← Production projects (source files)
├── voter_list_sir/              ← SIR voter list controversy (101s Short, preview + script + audit)
├── flight_surcharge/            ← Flight surcharge Short (full pipeline)
├── ep12_navic/                  ← EP12 NavIC explainer
├── ep13_monsoon/                ← EP13 Monsoon El Niño
├── ep14_bullet/                 ← EP14 Bullet Train 2027
├── ep15_rupee/                  ← EP15 Rupee 96
├── ep16_chips/                  ← EP16 Made-in-India Chips
├── anime_edit_01/               ← Neon Blade (anime edit Short)
├── anime_edit_02/               ← Laal Chaand (anime edit Short)
└── anime_edit_03/               ← Safed Raat (anime edit Short)

VIDEOS/                          ← Rendered & delivered videos (MP4s)
│   01_NavIC · 02_Monsoon · 03_Bullet_Train
│   04_Rupee_96 · 05_Made_in_India_Chips
│   06_Neon_Blade_SHORT · 07_Laal_Chaand_SHORT · 08_Safed_Raat_SHORT
│   index.html (video gallery)

uploads/                         ← Uploaded reference images
docs/                            ← Plans & documentation
└── EP12_NavIC_PLAN.md           ← NavIC episode production plan
```

---

## §5 — SKILL FILES CATALOGUE

Each skill file is a self-contained domain manual. **Never alter their code or logic** — they are battle-tested.

| Skill File | Domain | Key Concepts |
|---|---|---|
| `SKILLS_AFTER_EFFECTS.md` | After Effects workflows | Easing, weight, motion blur, grade, type, AE hand-off routes |
| `SKILLS_CAPCUT_ALIGHT_MOTION.md` | CapCut & Alight Motion | Official catalogues, native transition grammar, XML/JSON writers |
| `SKILLS_LONGFORM.md` | Long-form episodes | Structure, pacing, packaging for 3–5 min explainers |
| `SKILLS_PEAK_DETAIL.md` | Peak detail production | 8 detail passes, gates A–F, 3-worst-problems fix loop |
| `SKILLS_RESEARCH.md` | Research methodology | Verified repos, adopted/rejected techniques, audit results |
| `SKILLS_SHORTS_CURIOSITY.md` | Shorts retention | 1-second law, Script Doctor, curiosity gaps, hook archetypes |
| `SKILLS_THUMBNAIL_AND_MOTION_MASTERY.md` | Thumbnails & motion | Thumb composition, motion mastery techniques |
| `motion-graphics-mastery.md` | Motion graphics | Complete motion graphics knowledge kit |
| `motion-thinking-kit.md` | Motion reasoning | Thinking/reasoning framework for motion design |
| `MOTION_RESEARCH_Opus55.md` | Motion research | How the reference motion videos are actually made |
| `PROMPT_LIBRARY_opus55.md` | Prompt archive | Raw prompts used across production (reference only) |

---

## §6 — PRODUCTION FORMATS

| Format | Spec | Notes |
|---|---|---|
| YouTube Short (default) | 1080×1920, 30 fps, **≤ 2:00** | Measured narration sets the length |
| Long-form (Ep12+) | 1920×1080, 30 fps, target 3:30–4:30, max 5:00 | See `SKILLS_LONGFORM.md` |
| Edit-style film | 1080×1920 vertical, 10–30 s, beat-driven | e.g. anime edits |

---

## §7 — LANGUAGE RULES

- **Narration:** Hindi / Hinglish. For TTS, write Hindi in **Devanagari** and spell numbers, abbreviations and English words phonetically.
- **On-screen text:** English for labels/numbers/sources; Hindi summary captions for short films (summaries, never word-aligned subtitles).
- **User communication:** Short Hinglish. Assume intent, don't interrogate.

---

## §8 — THE 11-STEP PIPELINE (summary)

1. **Wipe** previous project (L16)
2. **Research** the topic (verified facts, dated sources)
3. **Sources** — build fact ledger
4. **Concept** — scene-by-scene plan with timings
5. **Script** — Hinglish narration with phonetic TTS marks
6. **Voice** — narrator voice audition (the one pause)
7. **Film HTML** — self-contained, deterministic, code-drawn
8. **QA loop** — motion_report, peak detail gates, text overflow check
9. **Audio master** — VO as master clock, measured loudness
10. **Full render** — ffmpeg, verified from encoded file
11. **Deliver** — MP4 + SRT + thumbnail + title + description + pinned comment

*Full details in `BENAQAAB_AI_AGENT_COMPACT.md` §4.*

---

## §9 — VISUAL IDENTITY STANDARDS

- **Typography pairing:** Space Grotesk / Outfit / Syne (headlines) + Inter (body) + JetBrains Mono (code/data)
- **Hindi text:** NotoSansDevanagari
- **Color philosophy:** Deep chromatic slate/obsidian base (`#07090E`), frosted glass surfaces, vibrant accent per episode (each episode gets a unique "look")
- **Motion:** GPU compositor-only (`transform`, `opacity`), 60fps target, spring deceleration, 3-scale ambient motion in every frame
- **Frosted glass:** `backdrop-filter: blur(16px) saturate(180%)` with specular borders
- **Organic grain:** SVG noise at 3–4% opacity across viewports
- **Source footage style:** B&W with red-band accent (see `brand/style_refs/`)

---

## §10 — DELIVERED EPISODES REGISTRY

| # | Title | Format | Duration | Look | Status |
|---|---|---|---|---|---|
| EP12 | NavIC: India ka apna GPS | Long-form 16:9 | 3:21 | ORBIT LEDGER | ✅ Delivered |
| EP13 | Monsoon El Niño | Long-form 16:9 | 3:26 | RAIN LEDGER | ✅ Delivered |
| EP14 | Bullet Train 2027 | Long-form 16:9 | 2:57 | — | ✅ Delivered |
| EP15 | Rupee 96 | Long-form 16:9 | 3:11 | EXCHANGE BOARD | ✅ Delivered |
| EP16 | Made-in-India Chips | Long-form 16:9 | 3:47 | SILICON WAFER | ✅ Delivered |
| S01 | Neon Blade (anime edit) | Short 9:16 | 0:47 | Neon anime | ✅ Delivered |
| S02 | Laal Chaand (anime edit) | Short 9:16 | 0:48 | Sakura / oni | ✅ Delivered |
| S03 | Safed Raat (anime edit) | Short 9:16 | 0:53 | Snow / yuki-onna | ✅ Delivered |
| — | Flight Surcharge | Short 9:16 | — | — | Source complete |

---

## §11 — PROTECTED FILES (never delete, hide, move or pack)

These files are **inviolable**. Breaking this rule is an automatic failure:

- `MEMORY.md` (production history — append only, never truncate)
- `CENTRAL_AGENT_MEMORY.md` (this file)
- `MOTION_RESEARCH_Opus55.md`
- `brand/fonts/*` (all 11 typefaces)
- `brand/host/*` (presenter cutouts)
- `brand/logo.png`
- `knowledge/PROMPT_LIBRARY_opus55.md`
- `knowledge/SKILLS_*.md`
- `setup.sh`
- `viz/` (entire rendering engine)
- All `SKILLS_*.md` root files

---

## §12 — HOW TO MAINTAIN THIS REPOSITORY

1. **After every delivery or correction:** Add a new numbered section to `MEMORY.md`. Never delete old sections; mark superseded ones `[OLD vX]`.
2. **After editing any skill file:** Run `python3 _assemble_agent_file.py` to refresh `BENAQAAB_AI_AGENT_MASTER_SKILL.md`.
3. **Heavy intermediates:** Keep in `.cache/` (always wipeable, never relied upon).
4. **Before any deletion:** Make a text backup first, verify protected files by hash.
5. **New agents:** Give them `AI_HANDOVER_PROMPT.md` + this repository ZIP.

---

## §13 — REPORTING STYLE

- **Concise Hinglish** — delivery first (file + specs), then decisions, then what was NOT verified.
- **Never say "looks great"** — give numbers.
- **Honest limits:** Cannot install CapCut/Alight/AE. Cannot use copyrighted music/footage. Say so.
- **Never claim** a render, measurement or test that was not actually run.

---

*This file is the centralized memory for all AI agents. When in doubt, this file + `BENAQAAB_AI_AGENT_COMPACT.md` are the authority. Everything else is reference.*
