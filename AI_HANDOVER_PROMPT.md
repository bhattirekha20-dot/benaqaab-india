# AI HANDOVER PROMPT — copy, paste, attach the zip

Give your AI **the zip file** plus **one of the prompts below**. The prompt is written so the agent
knows what it received, what to read first, which rules are absolute, and what to deliver.

---

## PROMPT 1 — THE MAIN ONE (for any capable AI: ChatGPT, Claude, Gemini, Grok, etc.)

> Copy everything inside the box and paste it into your AI. Then attach the zip.

```
I am giving you a zip of my complete video-production workspace. It is the full knowledge base
behind my channel "Benaqaab India" — every rule, skill, tool and reference film I have built up.
I want you to work inside it exactly the way the workspace works.

FIRST, DO THIS IN ORDER:
1. Unzip it. Read MASTER_AGENT_DISPATCH.md and START_HERE.md completely — MASTER_AGENT_DISPATCH.md
   is your single-file master dossier containing every covered video, topic status, laws, 3 colour profiles,
   and production rules.
2. Read BENAQAAB_AI_AGENT_COMPACT.md completely. It is your operating manual: my standing rules,
   the 11-step production pipeline, technical contracts, quality gates, a failure catalogue and
   copy-paste templates.
3. Do not read BENAQAAB_AI_AGENT_MASTER_SKILL.md linearly — it is 45,560 lines. Use the §INDEX at
   the end of the compact file to jump to the appendix you need for the task at hand. Same for
   MEMORY.md: read its tail for the latest state, search it when you need to know why a rule exists
   or whether something was already tried.
4. Study the two reference films in projects/ before building anything of your own:
   projects/anime_edit/ is an edit-style film, projects/upi_explained_short/ is an explainer.

THEN WORK BY THESE TEN NON-NEGOTIABLES (never break them):
1. Finish the work. I give you a topic; you produce the finished film. Make every call yourself and
   report your decisions at the end. The only thing you may pause for is the narrator voice pick.
2. Every frame is a pure function of time — deterministic, seeded, re-renderable one second at a time.
3. No dead frames. Motion must exist at three scales in every frame; the freeze check must come back
   clean. A film that animates and then holds still is a failure.
4. Never make a slideshow. Animate the real mechanism — pipelines, counters, bars, packets, dials —
   never text cards over a zooming photo.
5. Facts or nothing. Every number sourced and dated; when sources disagree, show both on screen,
   never average them; label anything that is a claim rather than a fact.
6. Sound is measured, never guessed. Narration timing is the master clock; loudness is measured on
   the final muxed file and reported.
7. Text must fit. Hindi is wider than Latin at the same size — measure, shrink, wrap; nothing
   overflows its box, nothing collides.
8. Cuts are a craft. Use the official transition names and durations, keep captions above the
   transition composite, and make sure no scene snaps back for a frame after a cut.
9. Verification before claims. Inspect frames from the encoded file, run the gates, report real
   numbers, and state plainly what you did not verify.
10. Protect the record. Never delete the protected files listed in Part I §2 of the compact file.
    MEMORY.md only grows; superseded rules get marked, not removed.

WHEN I GIVE YOU A TOPIC, THE DELIVERABLE IS:
- a script with a fact ledger where every number carries its source and date,
- the film as a single self-contained deterministic HTML file,
- the directable assets it needs, drawn or generated (original work only),
- an audio master with the narration as the master clock,
- the rendered MP4, verified from the encoded file, and
- an upload pack: titles, description, hashtags, pinned comment and a thumbnail brief.
Then add a new section to MEMORY.md describing what you built and the numbers you measured.

BE HONEST ABOUT LIMITS: you cannot install CapCut, Alight Motion or After Effects, and you cannot
use copyrighted music or ripped footage. Say so, and do the honest alternative the manual describes.
Never claim a render, measurement or test you did not actually run.

TASK FOR NOW: <write your topic or instruction here. Example: "make a 90-second Short explaining
how monsoon onset is declared in India" or "make another edit film like the anime one, same
quality, different vibe: neon cyberpunk rain">
```

---

## PROMPT 2 — SHORT VERSION (when you just want it to start reading)

```
I am sending you a zip of my complete video-production workspace for the channel Benaqaab India.
Unzip it and read MASTER_AGENT_DISPATCH.md and START_HERE.md first — MASTER_AGENT_DISPATCH.md gives you
the complete catalogue of all topics with videos, current roadmap, brand DNA, 20 operating laws,
and the 3 colour grading profiles. Then read BENAQAAB_AI_AGENT_COMPACT.md in full. The bigger file,
BENAQAAB_AI_AGENT_MASTER_SKILL.md, is a look-up library: use the §INDEX at the end of the compact
file to reach the appendix you need.

Then tell me in your own words: what the workspace contains, the ten non-negotiables, and how you
will produce a film when I give you a topic. After that I will give you the topic.
```

---

## PROMPT 3 — CODING AGENT VERSION (Claude Code, Cursor, Codex, an agentic CLI…)

```
This zip is a video-production workspace. Set it up and take it over.

1. Unzip into a working directory. Put it under /home/user if you are on Linux.
2. Run: bash setup.sh      # installs ffmpeg, Playwright, headless Chromium, fonts
   Expect [setup] OK. Do not skip this — a fresh machine has none of it.
3. Read MASTER_AGENT_DISPATCH.md and START_HERE.md, then BENAQAAB_AI_AGENT_COMPACT.md in full (your operating manual).
4. Prove the environment works before building anything:
   - the renderer: python3 viz/hrender.py --help
   - the gate:     python3 tools/peak_detail_gate.py --help
   - the reference film: re-render a few seconds of projects/upi_explained_short/UPI_Explained_Short.html
     and confirm no page errors and a clean motion check.
5. Then build what I ask for, following the 11-step pipeline in Part I §4 of the compact file,
   including the QA gates in §14 before you hand anything over.
   Render long jobs through a background process, never a blocking foreground call.

Rules that are absolute: the ten non-negotiables in START_HERE.md section 4, and the protected-file
list in Part I §2 L3 of the compact file. Report real numbers, not opinions.
```

---

## PROMPT 4 — WHAT TO SEND WITH A SINGLE TASK (fill-in template)

```
Workspace attached. Read START_HERE.md and BENAQAAB_AI_AGENT_COMPACT.md first, then follow the
pipeline in Part I §4.

TASK:        <one sentence — what the film is about>
FORMAT:      <Shorts explainer / edit film / long-form>  (default: Shorts explainer, under 2 minutes)
LENGTH:      <let the measured narration decide, or give a target>
LANGUAGE:    Hindi / Hinglish narration, English labels on screen
STYLE:       <reference: projects/upi_explained_short for explainers, projects/anime_edit for edits>
MUST INCLUDE: <any fact, number or scene you want in>
MUST AVOID:   <anything you do not want>

Deliver the film plus the upload pack. Report your decisions and anything you could not verify.
```

---

## 5. IF YOUR AI SAYS IT CANNOT OPEN THE ZIP

Some chat interfaces cannot read zips. In that case send files one at a time, in this order:

1. `START_HERE.md`
2. `BENAQAAB_AI_AGENT_COMPACT.md`
3. the reference project files you want it to match (`projects/.../README.md`, `SCRIPT.md`,
   `SOURCES.md`, and the film HTML)
4. the relevant appendix text copied out of `BENAQAAB_AI_AGENT_MASTER_SKILL.md`

…and use **Prompt 1 with this replacement line**:

```
Files are being sent one at a time instead of as a zip. Read them in the order I send them and tell
me when you have understood the workspace; then wait for my topic.
```

---

## 6. WHAT TO EXPECT BACK (so you can check the agent is doing it right)

A correct agent will, before it builds anything:
- summarise the workspace and the ten non-negotiables in its own words,
- ask only for the topic (or for the voice pick, if it can generate speech),
- state what it cannot do here — no CapCut/Alight/AE, no copyrighted media,
- and show you a fact ledger with dated sources before any rendering.

A wrong agent will: start writing a script with invented numbers, promise CapCut or After Effects
effects, describe a film without timings, or claim results from tests it never ran. If you see that,
reply: *"re-read Part I of BENAQAAB_AI_AGENT_COMPACT.md and start again from the pipeline."*
