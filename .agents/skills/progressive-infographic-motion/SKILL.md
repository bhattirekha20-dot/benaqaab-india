---
name: progressive-infographic-motion
description: Turn a static dashboard, poster, data card design, or supplied image panels into a staged animated motion graphic and an editable, semantic HTML motion reference. Use this skill whenever the user asks to animate graphics, make a dashboard live, create a motion reference, or prepare assets for an AI video editor.
version: 1.0.0
---

# Progressive Infographic Motion

## Objective

Transform static visual information into a clean, premium sequence where the viewer sees the message being built step by step.

**Important:** Never prescribe a fixed total duration, fixed seconds, or fixed FPS unless the user explicitly asks for them. Use relative phases instead. The calling AI or video editor decides the final pacing.

## When to use

Use this skill for requests such as:

- “Make this dashboard animated.”
- “Turn this graphic into a video.”
- “Make a live clock / chart / infographic.”
- “Create HTML reference for my video AI.”
- “Animate these cards one by one.”
- “Add motion to this screenshot.”

## Input handling

1. Inspect all supplied images and identify individual modules.
2. Extract the visible text, colors, panel types, and intended final layout.
3. Preserve source wording unless the user requests copy changes.
4. If individual panel screenshots are provided, treat them as a storyboard and use their visual order or the user’s stated order.
5. Ask a clarification only when the requested sequence or final layout cannot be inferred.

## Mandatory motion strategy

Do not reveal the whole screen at once.

Use this progressive order by default:

| Phase | What appears | Required motion |
|---|---|---|
| 01 | Main title / dialog | Fade and scale into the centre. Show a `LIVE` tag if requested. |
| 02 | Main title / dialog | Move it to its final anchor, normally top centre. |
| 03 | Left context card | Enter and settle at the left. Use the information color. |
| 04 | Central hero graphic | Draw/build the graphic live, rather than only fading it in. |
| 04b | Hero labels / number | Reveal after the graphic is mostly complete. |
| 05 | Right consequence/risk card | Enter and settle at the right. Use its accent color. |
| 06 | Final dashboard | Hold the complete composition with subtle ongoing live motion. |

## Motion rules

### Entrance and easing

- One clean entrance per element.
- Use smooth ease-out motion.
- Allow only a small settle/overshoot for cards.
- Avoid unnecessary shakes, spins, large bounces, or random movement.
- Keep reading order obvious: headline → context → hero insight → consequence.

### Hero graphics

Animate the graphic in a way that explains it:

- **Clock / ring:** draw clockwise from 12 o’clock with a glowing travelling node.
- **Graph / chart:** grow from baseline, then reveal labels.
- **Counter:** show after its container exists; count once, not repeatedly.
- **Map:** reveal regions/markers in a meaningful order.
- **Icon/orbit:** trace a path or use controlled orbit light.

### Final composition

Use subtle ambient motion only:

- pulsing `LIVE` dots
- slow data packet on connector lines
- 1–2 px breathing float
- restrained glow pulse
- occasional soft scan line

Do not obscure text or reduce legibility.

## Design rules

- Preserve visual hierarchy and source meaning.
- Make final arrangement balanced and readable.
- Use semantic role colors consistently:
  - information/context → cyan or blue
  - hero/active graphic → orange or gold
  - danger/risk → pink or red
  - copy → off-white / muted blue-grey
  - background → dark navy / charcoal
- Place `LIVE` badges near an element but never over its key text.
- Keep safe margins and make the final layout work at 16:9 by default.

## HTML reference deliverable

When producing an HTML reference, it must be self-contained and contain:

1. Real selectable HTML text — do not make all text part of a single screenshot.
2. Inline CSS only; no required external scripts, fonts, or CDN files.
3. A responsive 16:9 preview canvas.
4. Play/pause, restart, loop, and **phase** (0–100) scrubber controls.
5. JavaScript render function driven by a normalized phase value.
6. A machine-readable JSON specification embedded in:

```html
<script id="motion-spec" type="application/json">...</script>
```

7. The same object exposed in JavaScript as:

```js
window.MOTION_REFERENCE
```

The HTML must use **phase labels**, such as `PHASE 01`–`PHASE 06`, not fixed video timecodes.

## Required machine-readable format

```json
{
  "name": "Descriptive motion sequence title",
  "format": {
    "width": 1280,
    "height": 720,
    "aspectRatio": "16:9",
    "duration": "decided by AI/video editor",
    "fps": "decided by AI/video editor"
  },
  "style": {
    "background": "dark navy with subtle grid and vignette",
    "information": "#32ccff",
    "hero": "#ff862e",
    "risk": "#ff5274"
  },
  "timeline": [
    {"phase": "01", "element": "headline", "action": "centre fade and scale in"},
    {"phase": "02", "element": "headline", "action": "move to top"},
    {"phase": "03", "element": "left card", "action": "enter and settle"},
    {"phase": "04", "element": "hero", "action": "draw or build live"},
    {"phase": "05", "element": "right card", "action": "enter and settle"},
    {"phase": "06", "element": "complete dashboard", "action": "hold with subtle live motion"}
  ],
  "finalLayout": {
    "headline": [0.5, 0.1],
    "leftCard": [0.18, 0.58],
    "hero": [0.5, 0.58],
    "rightCard": [0.82, 0.58]
  }
}
```

## Video-rendering deliverable

If a video is also requested:

- Make it browser compatible (H.264 MP4 if available).
- Do not add music, narration, duration, or a frame rate unless requested.
- Keep the final frame readable as a hold frame.
- The video must faithfully follow the phase order above.

## Validation checklist

Before delivery, confirm:

- [ ] Main message appears first.
- [ ] Header moves to its final top position before supporting cards arrive.
- [ ] Hero graphic is visibly drawn/built, not merely faded in.
- [ ] Individual `LIVE` tags appear alongside their related modules.
- [ ] Final screen contains all modules in a clear, balanced layout.
- [ ] Ambient motion is gentle and does not block text.
- [ ] HTML reference uses phase values only; it does not dictate duration, timecodes, or FPS.
- [ ] `window.MOTION_REFERENCE` is available to a consuming AI.

## Current project example

For the 2045 Demographic Clock project, use:

**Headline → headline moves top → blue demographic card → orange 2045 ring drawn live → red middle-income card → final connected dashboard.**

## Extended resources in this skill package

Load these files when the request needs more support:

- `references/editing-capabilities.md` — asset analysis, graph/chart/ticker patterns, localization, data binding, accessibility, video-editor handoff, and advanced editing modes.
- `templates/motion-manifest-template.json` — reusable machine-readable project manifest with relative phases only.
- `templates/editor-handoff-template.md` — layer naming, locked-copy, layout, and motion handoff for a video AI/editor.
- `references/demographic-clock-conversation-map.md` — full mapped project history, current asset map, locked copy, design decisions, and deliverable map for this project.
