# Demographic Clock — Conversation and Project Map

This file maps the user-visible requests, decisions, visual assets, and resulting deliverables for the Demographic Clock project. It is designed so another AI or video editor can understand the project without rereading the complete chat.

## A. User requests mapped to implementation

| Order | User request / intention | Implementation decision |
|---|---|---|
| 01 | Make the text and orange/orbit graphics in the reference image dynamic. | Created an editable HTML dashboard with semantic text, cards, a live orange clock ring, ticker, and configurable values. |
| 02 | Make it a video and add motion. | Produced a motion-graphic preview with orbit glow, moving node, data signals, card highlights, and scanner sweep. |
| 03 | Do not use one static dashboard reveal; show each supplied panel in sequence. | Defined a staged storyboard: title first, title moves top, blue card, live-drawn circular clock, red card, final layout. |
| 04 | Make the central circular graphic draw live. | Defined clock ring drawing clockwise from 12 o’clock; show inner `2045` copy only after the ring is mostly built. |
| 05 | Provide HTML so an AI/video editor can understand and reuse the motion. | Created a semantic motion-reference HTML file with CSS, JavaScript phase controller, editable text, and a JSON motion object. |
| 06 | Do not mark a fixed video duration; the user’s AI chooses it. | Removed fixed duration, fixed timecodes, and fixed FPS from the current HTML/skill. Replaced them with relative Phase 01–06 instructions and a 0–100 phase scrubber. |
| 07 | Make the workflow a central reusable skill. | Created `skills/progressive-infographic-motion/SKILL.md`. |
| 08 | Expand support and map all conversation decisions. | Added extended editing capabilities, templates, asset map, and this conversation map. |

## B. Final narrative / reveal order

```text
Phase 01  Headline/dialog appears in the centre with LIVE.
Phase 02  Headline smoothly moves to top centre.
Phase 03  Blue demographic-status card enters and settles at left with LIVE.
Phase 04  Orange 2045 ring is drawn live clockwise from 12 o’clock.
Phase 04b  2045 / WINDOW CLOSES / remaining-time text fades in late in ring draw.
Phase 05  Red middle-income-trap card enters from right with LIVE.
Phase 06  All modules form the final dashboard; add restrained connector/data-packet movement and LIVE pulses.
```

## C. Current panel asset map

These are the current source attachments in `/home/user/uploads/`.

| Source file | Visual module | Final role | Accent | Final position | Reveal phase |
|---|---|---|---|---|---|
| `image-1.png` | Demographic Clock headline / subtitle | Primary message | Gold | Top centre | 01 → 02 |
| `image-2.png` | `TODAY (2026 STATUS)` / Median age card | Context / supporting evidence | Cyan | Left | 03 |
| `image-3.png` | `2045` circular ring / Window closes | Hero insight | Orange / gold | Centre | 04 / 04b |
| `image-4.png` | `THE MIDDLE-INCOME TRAP` card | Risk / consequence | Pink / red | Right | 05 |

## D. Locked display copy

### Header

- `ACTUARIAL DEMOGRAPHIC RISK · INDIA PROJECTION`
- `THE 2045 DEMOGRAPHIC CLOCK: RACE AGAINST TIME`
- `India has only 19 years before its demographic dividend window permanently shuts.`

### Blue information card

- `TODAY (2026 STATUS)`
- `Median age: 28.4 yrs`
- `1 crore youth enter jobs each year`
- `Youngest workforce on Earth`
- `Fertility rate: 2.0 (NFHS-5)`
- `Replacement level broken`
- `South states already aging`

### Orange hero clock

- `2045`
- `WINDOW CLOSES`
- `19 years 81 days remaining`

### Red risk card

- `THE MIDDLE-INCOME TRAP`
- `Target: $10,000 / cap`
- `Must reach $10,000 before 2045`
- `Current: $2,730 (need 4× leap)`
- `Without mass formal pensions`
- `Without universal healthcare`
- `Brazil/Thailand stagnation risk`

## E. Visual and motion rules

### Colors

```json
{
  "information": "#32ccff",
  "hero": "#ff862e",
  "heroHighlight": "#ffbe55",
  "risk": "#ff5274",
  "copy": "#edf5ff",
  "secondaryCopy": "#93a7bd",
  "background": "deep navy / dark charcoal"
}
```

### Do

- Use dark navy background, low-opacity grid, and vignette.
- Use separate `LIVE` badges for header, blue card, hero ring, and red card.
- Add a glowing travelling node to the orange ring.
- Use thin connector lines only after the full layout has formed.
- Keep background/ambient movement quiet and premium.
- Preserve text as editable semantic content in HTML references.

### Do not

- Do not reveal all panels at the first frame.
- Do not prescribe a final duration or FPS.
- Do not hide cards behind badges or effects.
- Do not use aggressive bounce, random glitching, or fast flash effects.
- Do not turn the final HTML reference into only a static screenshot.

## F. Deliverable map

| Path | Purpose | Current use |
|---|---|---|
| `/home/user/demographic-clock.html` | First dynamic dashboard prototype | Visual / data prototype |
| `/home/user/demographic-clock-animation.mp4` | Earlier moving-dashboard video preview | Optional legacy preview only; not timing authority |
| `/home/user/demographic-clock-staged.mp4` | Earlier staged MP4 preview | Optional legacy preview only; not timing authority |
| `/home/user/demographic-clock-motion-reference.html` | Current semantic HTML reference | Primary reference for AI/video editor |
| `/home/user/CENTRAL_MOTION_EDITING_SKILL.md` | Earlier standalone central-skill document | Background/reference document |
| `/home/user/skills/progressive-infographic-motion/SKILL.md` | Reusable packaged agent skill | Primary reusable skill |
| `/home/user/skills/progressive-infographic-motion/references/editing-capabilities.md` | Extended capability library | Use for advanced editing |
| `/home/user/skills/progressive-infographic-motion/templates/motion-manifest-template.json` | Generic machine-readable template | Use for new projects |
| `/home/user/skills/progressive-infographic-motion/templates/editor-handoff-template.md` | Editor/video-AI handoff template | Use for new projects |
| `/home/user/skills/progressive-infographic-motion/references/demographic-clock-conversation-map.md` | This mapped project history | Primary project memory |

## G. How the next AI should continue

1. Load `skills/progressive-infographic-motion/SKILL.md`.
2. Read this conversation map.
3. Load `demographic-clock-motion-reference.html` and inspect `window.MOTION_REFERENCE`.
4. Use the four assets listed in the panel asset map if visual reference is needed.
5. Keep the exact narrative phase order.
6. Let the requested AI/video editor choose total duration, pacing, and FPS.
7. If copy/data changes, update the semantic HTML and motion manifest—not only screenshots.
