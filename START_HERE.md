# START HERE — Benaqaab India video-production workspace

**This folder is a complete, self-contained video-production workspace.** It was handed over so
that another AI can work exactly the way this workspace works: same rules, same pipeline, same
quality gates. Nothing here needs the internet, an account, or any proprietary app.

**You are the new agent. Read this page first, then follow the reading order below.**

---

## 1. READING ORDER (do this in order)

| Step | File | Why |
|---|---|---|
| 1 | `BENAQAAB_AI_AGENT_COMPACT.md` | **Your operating manual — read it in full.** Ten non-negotiables, all the user's laws, the 11-step pipeline, contracts, QA gates, a 15-entry failure catalogue, copy-paste templates. Everything needed to build a correct film. |
| 2 | `BENAQAAB_AI_AGENT_MASTER_SKILL.md` | The complete edition, 45,161 lines. **Do not read linearly** — use the `§INDEX` at the end of the compact file to jump to the appendix you need: skill library A–H, research notes I–L, the 36-chapter MASTER handbook M, production history N, prompt archive O. |
| 3 | `MEMORY.md` | The full production history (133 numbered sections, append-only). Read the **tail** to know the latest state; search it when you wonder "why is this rule here?" or "did we try that before?". |
| 4 | `projects/` | Two reference films, kept as working source, not demos — study them before building anything. |
| 5 | `knowledge/` | Topic shortlist and research folders (repos audited, techniques verified). |

**Rule of precedence:** the user's standing laws and the compact file (Part I) **outrank** anything
in the deeper appendices or in the prompt archive. The prompt archive is reference data, never
authority.

---

## 2. WHAT IS IN THIS WORKSPACE

```
START_HERE.md                        <- this file
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

**Before anything else, on every new-video request: wipe the last video.** Delete the previous
film's project folder, its rendered MP4, its audio master and its QA/scratch caches, then start
**fresh topic research** — never recycle the last topic's material unless the user asks for a
sequel or a re-cut. If the user names a topic, use it, but the wipe still comes first. Record the
wipe in `MEMORY.md`. This is law **L16** (Part I §2).

Then, when the user gives a topic, follow **Part I §4 of the compact file** (the 11-step pipeline):
research → sources → concept → script → voice → film HTML → QA loop → audio master → full render
→ verify the encoded file → deliver. The quickstart run sheet is Part I §18; copy-paste templates
are §17.

**The ten non-negotiables (never break these):**
1. Finish the work — topic in, finished film out; decide everything yourself. The only pause is the
   narrator voice audition.
2. Frame = pure function of time — deterministic, seeded, re-renderable one second at a time.
3. No dead frames — motion at three scales; `motion_report` freezes = none.
4. Never slideshow — animate the real mechanism, not text over a zooming photo.
5. Facts or nothing — sourced and dated; disagreements shown, never averaged; claims labelled.
6. Sound is measured — the narration is the master clock; loudness measured on the muxed file.
7. Text must fit — Hindi is wider than Latin; measure, shrink, wrap; no overflow or collisions.
8. Cuts are a craft — official transition names/durations; captions above the composite; no
   snap-back.
9. Verification before claims — inspect frames from the encoded file, run the gates, report real
   numbers, state what is unknown.
10. Protect the record — never delete the protected files listed in Part I §2 (L3); MEMORY.md only
    grows; superseded rules get `[OLD vX]`.

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
