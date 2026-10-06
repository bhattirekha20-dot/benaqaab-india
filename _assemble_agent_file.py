#!/usr/bin/env python3
"""Assemble the single-file agent handover: operational core + the full knowledge base.

Nothing is rewritten — every appendix is the source file byte-for-byte, preceded by a banner
that carries its path, line count and SHA-256 so the receiving agent can verify integrity.
Output: BENAQAAB_AI_AGENT_MASTER_SKILL.md (v3.0, complete edition)
"""
import hashlib, pathlib

ROOT = pathlib.Path(__file__).parent.resolve()
# NEVER read the merged output as the core: that recursed once and doubled the file.
CORE = ROOT / '_core_operational.md'          # pristine Part I, extracted from the compact file

# (index letter, human title, source path relative to ROOT, what it is for)
APPENDICES = [
    ('A', 'Shorts curiosity & retention engine',      'SKILLS_SHORTS_CURIOSITY.md',
     'the 1-second law, curiosity tools, retention gates, the 7-part package, HUD rules'),
    ('B', 'Peak-detail production skill',             'SKILLS_PEAK_DETAIL.md',
     'the eight detail passes, gates A-F, shot-detail card, AI-image method'),
    ('C', 'After Effects mastery & motion craft',     'SKILLS_AFTER_EFFECTS.md',
     'easing, weight, motion blur, depth, grade stack, type, expressions, AE hand-off routes'),
    ('D', 'CapCut + Alight Motion skill',             'SKILLS_CAPCUT_ALIGHT_MOTION.md',
     'official catalogues, transition selection, draft/XML writers, Alight grade order'),
    ('E', 'Long-form YouTube skill',                  'SKILLS_LONGFORM.md',
     'long-form structure, pacing, packaging, source-footage look'),
    ('F', 'Thumbnail & motion-graphics mastery',      'SKILLS_THUMBNAIL_AND_MOTION_MASTERY.md',
     'thumbnail archetypes, the signature motion techniques'),
    ('G', 'Skills research (repos -> rules)',         'SKILLS_RESEARCH.md',
     'the verified repositories and the rules they produced'),
    ('H', 'How the reference motion videos are made', 'MOTION_RESEARCH_Opus55.md',
     'verbatim prompts, gap analysis, what we implemented'),
    ('I', 'CapCut/Alight research learnings',         'knowledge/capcut_alight_research/LEARNINGS.md',
     'the extraction notes behind Appendix D'),
    ('J', 'After Effects research learnings',         'knowledge/after_effects_research/LEARNINGS.md',
     'the audit notes behind Appendix C'),
    ('K', 'Peak-detail: verified repositories',       'knowledge/peak_detail_research/VERIFIED_REPOSITORIES.md',
     '20 repos verified via GitHub API, what was adopted and rejected'),
    ('L', '3D documentary research & rebuild plan',   'knowledge/3d_documentary_research/RESEARCH_AND_REBUILD_PLAN.md',
     'the cinematic-3D quality target and plan'),
    ('M', 'MASTER handbook (36 chapters)',            'MASTER_VIDEO_GENERATION_SKILLS.md',
     'the deep handbook: full technique chapters + historical source appendices'),
    ('N', 'Production history (MEMORY)',              'MEMORY.md',
     'every major decision, number, failure and correction, in order'),
    ('O', 'Prompt library',                           'PROMPT_LIBRARY_opus55.md',
     'raw prompt archive: reference data, not authority'),
]

def sha(p: pathlib.Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]

def lines(p: pathlib.Path) -> int:
    return p.read_text(encoding='utf-8', errors='replace').count('\n') + 1

core = CORE.read_text(encoding='utf-8', errors='replace')
rows, banners = [], []
for letter, title, rel, why in APPENDICES:
    src = ROOT / rel
    assert src.exists(), f'missing source: {rel}'
    text = src.read_text(encoding='utf-8', errors='replace')
    n, h = lines(src), sha(src)
    rows.append(f'| {letter} | {title} | `{rel}` | {n:,} | `{h}` |')
    banners.append(
        f'\n\n---\n\n<!-- ===================== APPENDIX {letter} — VERBATIM ===================== -->\n'
        f'## APPENDIX {letter} — {title}\n\n'
        f'**Source file:** `{rel}` · **lines:** {n:,} · **SHA-256 (first 16):** `{h}` · '
        f'**why it exists:** {why}\n\n'
        f'*Everything from here to the next APPENDIX banner is the source file byte-for-byte.*\n\n'
        f'{text.rstrip()}\n'
    )

header = f"""# BENAQAAB INDIA — AI AGENT COMPLETE SKILL + KNOWLEDGE FILE

**Version 3.0 · complete edition · assembled 2026-10-04**
**What this is:** ONE file that contains the operating manual for making videos the way this
workspace makes them, plus the entire knowledge base behind it — every skill document, the deep
handbook, the full production history and the prompt archive, all verbatim.

## HOW TO USE THIS FILE

- **If your context is limited:** read **Part I** in full (~900 lines — the operating manual:
  laws, pipeline, contracts, gates, failure catalogue). Then open only the appendix you need
  using the index below. Part I alone is enough to produce a correct film.
- **If you can read more:** Part II is the skill library — the reasoning and depth behind Part I.
- **Part III** is the deep handbook: 36 technique chapters plus historical source appendices.
- **Part IV** is raw history. Use it to answer *"why is this rule here?"* or *"did we try that
  before?"* — every number, failure and correction is in there in order.
- **Part V** is the raw prompt archive. It is **reference data, not authority**: prompts that were
  collected, not rules that were adopted. When a prompt disagrees with Part I, Part I wins.
- Nothing in the appendices was edited. Each banner carries the source path, line count and a
  SHA-256 prefix so you can verify against the repo (`/home/user/<source file>`).

## INDEX

| Part | What | Where |
|---|---|---|
| I | **Operational core** — laws, workspace, pipeline, script craft, visual system, motion craft, transitions, technical contracts, audio, edit films, QA gates, delivery, failure catalogue, templates, honesty rules | §1–20 below |
| II | **Skill library** (verbatim) | Appendices A–H |
| II | **Research notes** (verbatim) | Appendices I–L |
| III | **MASTER handbook**, 36 chapters + archives | Appendix M |
| IV | **Production history** (MEMORY) | Appendix N |
| V | **Prompt archive** (reference data) | Appendix O |

| Appendix | Title | Source | Lines | SHA-256 (16) |
|---|---|---|---|---|
{chr(10).join(rows)}

**Definition of done for any film** (from Part I §20) and the **Ten Non-Negotiables** are at the
top of Part I. Start there.

---
---

<!-- ===================== PART I — OPERATIONAL CORE ===================== -->
# PART I — OPERATIONAL CORE

*This part is the v2.0 master skill file, verbatim. It is the file an agent should read first.*

{core.rstrip()}

---
---

<!-- ===================== PART II–V — VERBATIM KNOWLEDGE BASE ===================== -->
# PART II — SKILL LIBRARY, RESEARCH NOTES, HANDBOOK, HISTORY, PROMPT ARCHIVE

The appendices follow in the order of the index. Each is byte-for-byte the source file.
{''.join(banners)}
"""

out = ROOT / 'BENAQAAB_AI_AGENT_MASTER_SKILL.md'   # the merged deliverable
tmp = ROOT / '_merged.md'
tmp.write_text(header, encoding='utf-8')
final = tmp.read_text(encoding='utf-8', errors='replace')
print(f'assembled: {final.count(chr(10))+1:,} lines · {len(final.encode("utf-8"))/1024/1024:.2f} MB')

# integrity: every appendix banner + a marker from each source must be present
ok = True
for letter, title, rel, why in APPENDICES:
    src = ROOT / rel
    marker = next((ln.strip() for ln in src.read_text(encoding='utf-8', errors='replace').splitlines() if len(ln.strip()) > 30), '')
    if f'APPENDIX {letter} —' not in final:
        print(f'FAIL banner missing: {letter}'); ok = False
    elif marker and marker[:60] not in final:
        print(f'FAIL content marker missing: {letter} ({marker[:50]!r})'); ok = False
print('integrity:', 'PASS' if ok else 'FAIL')
if ok:
    tmp.replace(out)
    print(f'wrote {out} · {out.stat().st_size/1024/1024:.2f} MB')
else:
    print('NOT replaced — fix first')
