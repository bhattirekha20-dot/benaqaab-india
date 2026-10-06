# Long-form YouTube skills (researched 30 Sep 2026): apply from Ep12 onward

## Format (user directive §90)
- 16:9, 1920×1080, 30 fps. **Max 5:00**; target 3:30–4:30.
- **Presenter NOT permanent.** Use her for:
  - the intro hook (≤8 s);
  - 1–2 key moments (a reveal, a verdict);
  - the outro CTA.
- Keep her face on screen under ~20% of the runtime (research: under 20% in the first 30 s). Everything else is full-screen visuals.

## First 30 seconds (in 2026 YouTube treats it as a ranking input)
- Cold open: go straight into the most surprising fact or visual. No logo sting, no "welcome back".
- State the promise by 15–30 s ("is video ke end tak aap jaanoge…").
- Change the visual every 3–7 s in the first 30 s. Strong hooks pack about 15–19 visual changes into 30 s.
- Place the first deliberate pattern interrupt at 25–35 s (the first big drop-off zone).
- Within the first 5 s, visually confirm what the title and thumbnail promised. A mismatch means an instant drop-off.

## Structure of a ≤5-min "mini-documentary"
| Time | Beat |
|---|---|
| 0:00–0:20 | Cold open (presenter or a striking visual) + the promise |
| 0:20–0:40 | Context: why this matters now (dated facts) |
| 0:40–3:40 | 3–4 chapters of 45–75 s each: mini-hook → explanation → PROOF (data / real media) → mini-payoff |
| ~50% mark | Re-hook: tease the best part ("sabse badi baat abhi baaki hai…") |
| last 30–40 s | Final payoff that circles back to the opening question (never say "in summary") → CTA ≤10 s |

- **Open loops:** tease a reveal early and pay it off later.
- **Chapters:** timestamps in the description. The first must be 0:00, you need ≥3 chapters, each ≥10 s. Use descriptive names ("NavIC kaise kaam karta hai", not "Part 2").

## Pacing and visual variety
- Change the visual every 10–20 s in the first 3 min, then every 25–40 s.
- Make a BIG pattern interrupt every 60–90 s by switching scene type: map → chart → real photo/footage → kinetic type → presenter.
- **Scene types we can build in HTML:**
  - animated line/bar charts (ALWAYS one scale per comparison);
  - schematic maps (no national borders unless they are Survey-of-India compliant; use city dots and routes);
  - timelines; orbit/process diagrams; kinetic typography;
  - real photos/footage with purposeful punch-ins; split screens;
  - "document zoom" on a sourced quote;
  - chapter title cards (≤1.5 s); a recurring anchor motif.
- **Cutting patterns:**
  - progressive rhythm (cuts speed up toward the payoff);
  - contrast (fast and slow sections);
  - narrative loop (keep returning to the core question);
  - anchor (a recurring visual motif).
- **J-cut / L-cut:** the next scene's visual leads the VO by about 0.3 s. No "flat landings": no dead air between sections.
- Trim filler: watch at 1.5× and cut anything where attention wanders.

## Audio
- VO at −14 LUFS.
- If the user approves music (standing rule §36 = no music/SFX by default):
  - use a bed at about −24 to −28 LUFS, ducked under the VO, and change the track per chapter;
  - add subtle SFX on motion beats (whoosh/pop/click).
  - Licensed only: YouTube Audio Library (the user downloads it) or CC0 / CC BY tracks, credited.

## Styles to borrow (faceless documentary channels)
- Wendover Productions: maps + clean motion graphics; "how does this system work?".
- PolyMatter: custom graphics, explainer journalism.
- RealLifeLore: custom maps, data visualisation.
- Vox: halftone / paper-collage texture, animated maps and stats, beat-synced.
- Economics Explained / How Money Works: charts + narration; finance told as story.
- ColdFusion: calm narration, cinematic B-roll.

## Benchmarks
- Videos under 5 min: aim for 50–70% average percentage viewed, and 60–65%+ still watching at 30 s.
- Average view duration ≥50% makes a video about 3× more likely to be recommended.

## Packaging
- Thumbnail 1280×720: 3–4 words, one big number or graphic, high contrast, and it must match the hook.
- Title ≤60 characters: curiosity plus clarity, no bait-and-switch.
- End screen in the last 5–20 s: subscribe + next video.
- Upload the SRT captions.

## Sources
- rivereditor.com (2026 scripting guide)
- longstories.ai (May 2026)
- pixflow.net (Aug 2026)
- johnisaacson.co.uk (Mar 2026)
- lenostube.com (Jun 2026)
- fluxnote.io (Mar 2026)
- vidiq.com (Jun 2026)
- gyre.pro (Sep 2026)
- tubebuddy.com (Sep 2026)
- faceless.my (Aug 2026)
- cliptude.com (Vox style)

## Source-footage look (user rule §97, 30 Sep 2026)
- EVERY third-party clip or photo goes through `viz/source_style.py`: high-contrast B&W + halftone dot screen + translucent red band on the eye line (auto face placement) + subtle red/olive glows + vignette.
- Reference: `brand/style_refs/source_footage_ref.png`; demo: `brand/style_refs/source_footage_style_demo.jpg`.
- Our own charts, maps and graphics stay in full colour, so viewers can tell "evidence" from "our explanation" at a glance.
- The look is a design choice, not copyright protection: still keep clips short, credited, muted, used for commentary, and prefer official/free sources.
