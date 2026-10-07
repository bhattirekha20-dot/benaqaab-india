# START HERE — Benaqaab India video-production workspace

**This folder is a complete, self-contained video-production workspace.** It was handed over so
that another AI can work exactly the way this workspace works: same rules, same pipeline, same
quality gates. Nothing here needs the internet, an account, or any proprietary app.

**You are the new agent. Read this page first, then follow the reading order below.**

---

## 1. READING ORDER (do this in order)

| Step | File | Why |
|---|---|---|
| 000 | `AGENTS.md` | **Universal AI Operating Directive & Context Budget** — MANDATORY: forbids full repo dumping, enforces iterative surgical reading (return as many times as needed), and sets the Opus 5.5 code-rendered video intelligence standard. |
| 00 | `BENAQAAB_AI_VIDEO_MAKER_BIBLE.md` | **The Complete All-In-One Knowledge Transfer Bible** — read this ONE file to know everything: pipeline, 10 commandments, 14 battle-tested lessons, betterment roadmap, templates, and production thinking. Required reading for every fresh AI agent! |
| 0 | `MASTER_AGENT_DISPATCH.md` | **The Single-File Master Dossier** — complete catalogue of all topics with videos, backlog, brand DNA, 20 operating laws, 3 colour profiles, and 11-step pipeline. |
| 0.1 | `GITLAB_MIGRATION_AND_STORAGE_SYSTEM.md` | **GitLab Large-Storage Architecture** — guide for moving to GitLab to eliminate GitHub 100MB & LFS quota limits for video MP4/asset storage. |
| 0.5 | `BENAQAAB_FORENSIC_MOTION_SYSTEM.md` | **Forensic Motion Blueprint** — 5 runnable primitives (odometer, highlighter, redaction peel, loupe, verdict stamp), Data-to-DOM fact ledger, safe zones & comp.html boilerplate. |
| 0.6 | `AGENT_BETTERMENT_AND_GROWTH_ADVISORY.md` | **Continuous Betterment Advisory** — proactive critique rubric, top 10 upgrades & 5-point quality scorecard. |
| 0.7 | `VISUAL_ASSET_MASTER_LEDGER.md` | **Visual Asset Master Ledger** — comprehensive mapping of all 248 images, provenance, factual significance & AI usage rules. |
| 0.8 | `DIRECTIVE_5SEC_ROADMAP_AND_WHAT_USE.md` | **Explainer Master Directive** — 5-6s roadmap hook, What-Is-It & Use structure, and motion graphics image annotations. |
| 1 | `BENAQAAB_AI_AGENT_COMPACT.md` | **Your operating manual — read it in full.** Ten non-negotiables, all the user's laws, the 11-step pipeline, contracts, QA gates, a 15-entry failure catalogue, copy-paste templates. Everything needed to build a correct film. |
| 2 | `BENAQAAB_AI_AGENT_MASTER_SKILL.md` | The complete edition, 45,560 lines. **Do not read linearly** — use the `§INDEX` at the end of the compact file to jump to the appendix you need: skill library A–H, research notes I–L, the 36-chapter MASTER handbook M, production history N, prompt archive O. |
| 3 | `MEMORY.md` | The full production history (153 numbered sections, append-only). Read the **tail** to know the latest state; search it when you wonder "why is this rule here?" or "did we try that before?". |
| 4 | `projects/` | Reference films and production workspaces, kept as working source, not demos — study them before building anything. |
| 5 | `knowledge/` | Topic shortlist and research folders (repos audited, techniques verified). |

**Rule of precedence:** `AGENTS.md`, `BENAQAAB_AI_VIDEO_MAKER_BIBLE.md`, `MASTER_AGENT_DISPATCH.md`, `CENTRAL_AGENT_MEMORY.md`, and the compact file (Part I) **outrank** anything
in the deeper appendices or in the prompt archive. The prompt archive is reference data, never
authority.

---

## 2. WHAT IS IN THIS WORKSPACE

```
START_HERE.md                        <- this file
BENAQAAB_AI_VIDEO_MAKER_BIBLE.md     <- ALL-IN-ONE BIBLE: start here, transfers all wisdom
GITLAB_MIGRATION_AND_STORAGE_SYSTEM.md <- GitLab migration & large video storage manual
AI_HANDOVER_PROMPT.md                <- the prompt that came with this zip (keep it)
BENAQAAB_AI_AGENT_COMPACT.md         <- operational manual, read first   (~1,200 lines)
BENAQAAB_AI_AGENT_MASTER_SKILL.md    <- complete edition, look up by index (45,161 lines)
MEMORY.md                            <- production history, append-only
MASTER_VIDEO_GENERATION_SKILLS.md    <- 36-chapter handbook + archives
SKILLS_SHORTS_CURIOSITY.md           <- Shorts retention engine (1-second law, Script Doctor)
SKILLS_PEAK_DETAIL.md                <- the eight detail passes + gates A–F
SKILLS_AFTER_EFFECTS.md              <- easing/weight/motion-blur/grade/type + AE hand-off routes
SKILLS_CAPCUT_ALIGHT_MOTION.md       <- official catalogues + native transition grammar
SKILLS_LONGFORM.md                   <- long-form structure and packaging
SKILLS_THUMBNAIL_AND_MOTION_MASTERY.md
SKILLS_RESEARCH.md                   <- which repos were verified, what was adopted/rejected
MOTION_RESEARCH_Opus55.md            <- how the reference motion videos are actually made
PROMPT_LIBRARY_opus55.md             <- raw prompt archive (reference data only)
motion.py                            <- motion core + QA metrics (motion_report)
_assemble_agent_file.py              <- rebuilds the complete edition after any edit
setup.sh                             <- reinstall ffmpeg / Playwright / chromium / fonts
viz/       engine + renderer         hrender.py · motion_library.js · motion.py · templates/
tools/     gates + app writers       peak_detail_gate.py · capcut_draft.py · alight_project.py
                                     data/  official CapCut catalogues (4,173 items, 8 libraries)
knowledge/ research + topic ideas    topic_ideas/NEW_TOPIC_SHORTLIST_2026-10.md · per-domain folders
brand/     identity + assets         logo.png · fonts/ (11 faces) · reference images
projects/  the two reference films
  ├── anime_edit/                    Anime_Edit.mp4 (the delivered film) · Anime_Edit.html
  │                                  (self-contained source, art inlined) · BEATS.json ·
  │                                  make_music.py · assets/ plate art · UPLOAD_PACK.md
  └── upi_explained_short/           UPI_Explained_Short.html (self-contained) · SCRIPT.md ·
                                     SOURCES.md · TIMELINE.json · PLAN.json · MOTION_PASS.md
```

Deliberately **not** in the zip: rendered intermediate video/audio, `.cache/` scratch, and the
older backup archives. They are not needed to work; everything rebuildable is present as source.

---

## 3. INTEGRITY CHECK (optional, proves nothing was corrupted in transit)

```bash
python3 - <<'PY'
import hashlib, pathlib
want = {
  'BENAQAAB_AI_AGENT_COMPACT.md': None,   # no fixed hash (regenerated often)
  'MEMORY.md': None,
}
# The real check: the complete edition carries a SHA-256 prefix per appendix in its banners.
import re
t = pathlib.Path('BENAQAAB_AI_AGENT_MASTER_SKILL.md').read_text()
for m in re.finditer(r'\*\*Source file:\*\* `([^`]+)`.*?SHA-256 \(first 16\):\*\* `([0-9a-f]{16})`', t):
    src, want_hash = m.group(1), m.group(2)
    p = pathlib.Path(src)
    if p.exists():
        got = hashlib.sha256(p.read_bytes()).hexdigest()[:16]
        print(('OK  ' if got == want_hash else 'DIFF'), src, got)
PY
```

---

## 4. HOW TO DO A TASK

**Before anything else, on every new-video request: verify topic status.** Check `CENTRAL_TOPICS_MASTER.md`
and `MASTER_AGENT_DISPATCH.md` to ensure the topic is NOT covered (`RULE-NO-REPEAT`). Clean any temporary
scratch caches, create a dedicated project folder in `projects/<topic_slug>/`, and start **fresh primary-source
research** — never recycle old scripts unless the user explicitly orders a new angle. Record new projects in `MEMORY.md`.

**MANDATORY GATE 0 (`RULE-FORMAT-DURATION-GATE`):** Whenever a video topic is chosen (by user request, AI proposal, or registry pick), **NEVER assume or guess the format or duration**. You MUST PAUSE and ask the user:
1. **Format:** Long-form documentary (16:9 widescreen), short explainer, or YouTube Short / Reel (9:16 vertical)?
2. **Duration:** What target duration is desired (e.g. 30–60s, 90–120s, 3–5 min, 10 min+)?
Wait for user confirmation before proceeding to research and scriptwriting!

Then, when the user gives or approves a topic, follow **Part I §4 of the compact file** (the 11-step pipeline):
research → sources → concept → script → voice (Master Clock) → film HTML (`comp.html`) → preview QA loop →
**[1-GATE APPROVAL PROTOCOL: present interactive preview for user approval]** → full render upon command
→ verify the encoded file → unpacked deliverables (`delivery/` and root).

**The ten non-negotiables (never break these):**
1. **Finish the work through the preview gate (`RULE-GATE-1`)** — topic in, complete interactive preview out;
   decide visual mechanisms and audio yourself. The mandatory pause is the **1-Gate Preview Approval**: present
   `comp.html` for review, and only render the full MP4 when the user explicitly instructs *"render the video"*.
2. **Frame = pure function of time** — deterministic, seeded, re-renderable one second at a time.
3. **No dead frames** — motion at three scales; `motion_report` freezes = none.
4. **Never slideshow** — animate the real mechanism, not text over a zooming photo. Use real news stills + AI images (`RULE-REAL-MEDIA`).
5. **Facts or nothing** — sourced and dated; disagreements shown, never averaged; claims labelled.
6. **Sound is measured** — the narration is the master clock; loudness measured to -14 LUFS (±1.0 LU), -1.0 dBTP ceiling.
7. **Text must fit** — Hindi is wider than Latin; measure, shrink, wrap; no overflow or collisions.
8. **Cuts are a craft** — official transition names/durations; captions above the composite; no snap-back.
9. **Verification before claims** — inspect frames from the encoded file, run the QA checks, report real numbers, state what is unknown.
10. **Protect the record** — never delete protected files; MEMORY.md only grows; superseded rules get marked `[SUPERSEDED]`.
11. **Brand & Colour Standards** — Top-Left logo safe area with gold glow (`RULE-LOGO-TOPLEFT`); assign project to Profile A, B, or C (`RULE-COLOR-PROFILES`). Produce dedicated visual media for every story in a lineup (`RULE-MEDIA-PER-STORY`). Provide unpacked root/delivery assets (`RULE-UNPACKED-DELIVERABLES`).
12. **Visual Density, Hyper-Pacing & Glowing Images (`RULE-VISUAL-DENSITY-AND-GLOW`)** —
    - **Long-form (16:9):** At least **10 AI images / curated visual assets per 1 minute** of video (shot length ≤ 5.5–6.0s; 5 min = 50+ images; 10 min = 100+ images).
    - **Shorts / Reels (9:16):** At least **30 AI images / visual cuts per Short** (1 cut every 1.5–2.0s for hyper-retention).
    - **Glowing Aesthetics:** Apply specular rim glows, glowing HUD contours, and volumetric backlights wherever appropriate.
    - **Visual Thinking:** AI must think intentionally—never use random filler; pair each visual causally with the voiceover!
13. **Supporting Real Source Proof for Everything Spoken (`RULE-REAL-SOURCE-PROOF`)** — Every entity, statistic, or claim spoken in the narration MUST have concrete supporting real media from the internet (actual newspaper clippings, scanned gazettes, court filings, balance sheets, videos, satellite maps). Never speak words without visible proof on screen!
14. **The "Why Watch This Full Video" Hook Architecture (`RULE-BURNING-QUESTION-HOOK`)** — In the first 3–5 seconds (Frame 0 to 5s), immediately plant the high-stakes burning question in the viewer's mind: why must they watch till the end, what hidden truth will be uncovered, and what is at stake for them personally.
15. **Active Motion Graphics Explanations & Worldwide Deep Research (`RULE-DYNAMIC-HIGHLIGHTING` & `RULE-GLOBAL-DEEP-RESEARCH`)** — Real media must never sit static. Use active motion primitives: dynamic yellow highlighter sweeps (`multiply`), 2.5× forensic loupe zooms, animated callout pins with leader lines, rolling metric odometers, and verdict stamps. Autonomously execute deep worldwide research covering all direct and indirect relations (root causes, international geopolitics, money trails, supply chains, citizen impact).

**Reporting style the user expects:** concise Hinglish; delivery first (file + specs), then the
decisions you made, then what was **not** verified. Never say "looks great" — give numbers.

---

## 5. WHAT YOU CAN AND CANNOT DO (be honest about this)

- **Cannot** install or run CapCut / Alight Motion / After Effects — they are proprietary. The
  workspace does the honest alternative: official catalogues extracted, the transition grammar
  reimplemented natively, and draft/XML writers so the user can finish inside the real app.
- **Cannot** use copyrighted music, ripped anime footage or other third-party media. Original art
  and original music only — plus licensed/CC sources the user supplies.
- **Must not claim** a render, a measurement or a test that was not actually run. If a gate failed
  and was fixed, report both.
- The house render path needs Python + ffmpeg + headless Chromium. If you are a chat-only agent,
  you can still deliver: script package, fact ledger, timeline, the full film HTML, the upload
  pack, and exact render commands for whoever runs them.

## 6. KNOWN GAPS (what is source-complete and what needs regenerating)

Source-complete right now:
- **Anime edit film** — `Anime_Edit.html` is self-contained, the MP4 is beside it, the beat
  regenerates byte-identically from `make_music.py` with the same seed, plate art is in `assets/`.
- **Explainer format** — `upi_explained_short/` carries the film HTML plus `SCRIPT.md`,
  `SOURCES.md`, `TIMELINE.json`, `PLAN.json`, `MOTION_PASS.md` and `AUDIO_NOTES.md`. The film is
  code-drawn and re-renderable; its narration audio was deleted, so a re-render needs the VO
  regenerated from `SCRIPT.md` followed by the same timeline injection.

Not in this zip on purpose: rendered MP4s (except the anime edit, which is in the workspace rather
than the zip), `.cache/` scratch, and the two older backup archives.

If you rebuild anything, verify with a hash rather than by eye — that is how this workspace proved
its own rebuild was exact.

---

## 7. MAINTAINING THIS WORKSPACE

- Add a new numbered section to `MEMORY.md` for every delivery or correction. Never delete old
  sections; mark superseded ones `[OLD vX]`.
- After editing any skill file or `MEMORY.md`, run `python3 _assemble_agent_file.py` to refresh
  `BENAQAAB_AI_AGENT_MASTER_SKILL.md`.
- Keep heavy intermediates in `.cache/` (wiped, never relied upon). The workspace holds only what
  matters: memory, skills, knowledge, tools, brand, current projects.
- Before any deletion: make a text backup first, then verify the protected files by hash.
