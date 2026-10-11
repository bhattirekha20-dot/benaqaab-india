---
name: Progressive Infographic Motion Editor
description: Convert a static dashboard, poster, data card design, or screenshot into a staged motion graphic and a semantic, motion-controlled HTML reference. The final video duration, frame rate, and exact pacing are chosen by the calling AI or video editor.
version: 1.0
---

# Central Motion Editing Skill

## Purpose
Use this skill whenever a user provides a static design and asks for it to become a motion graphic, video sequence, animated dashboard, or editable HTML animation reference.

The output must **not** assume a fixed duration. Use a relative **0–100 phase scale** so a video AI can choose timing, pacing, frame rate, and final export length.

## Required Inputs

1. **Reference design** — full screenshot, poster, dashboard, or individual panel assets.
2. **Panel list** — identify the main visual modules, for example:
   - headline / title panel
   - left information card
   - central clock, chart, or hero graphic
   - right risk / information card
3. **Desired final layout** — usually the source layout unless the user requests a new arrangement.
4. **Copy/text** — preserve all user-provided wording exactly unless asked to rewrite it.
5. **Optional brand palette** — otherwise derive colors from the reference.

## Required Outputs

Create both outputs when possible:

- **Motion reference HTML**: semantic HTML, editable CSS, JavaScript motion controller, play/pause, restart, phase scrubber, and embedded machine-readable motion specification.
- **Motion brief / skill specification**: an AI-readable plan describing element order, entrance style, visual hierarchy, final layout, color rules, and relative phases.

Optional:

- Browser-compatible MP4 preview.
- Individual transparent panel assets.
- JSON motion specification for another editor or automation system.

## Core Rule: Progressive Reveal

Do **not** show every panel at once at the beginning.

Reveal one meaningful visual unit at a time so the viewer understands the story:

1. Bring in the primary message first.
2. Move it into its final anchor position.
3. Bring in supporting information in reading order.
4. Animate the hero graphic as a live construction or draw-on action.
5. Bring in the final risk/callout module.
6. Hold the final composition with subtle ongoing live motion.

## Default Phase Timeline

Use phases, never fixed seconds. The video AI decides how long every phase lasts.

| Phase | Element | Motion instruction |
|---|---|---|
| 01 | Headline / dialog | Fade in and scale up in the screen centre. Attach a small `LIVE` tag if requested. |
| 02 | Headline / dialog | Move smoothly to its final anchor, normally the top centre. |
| 03 | Left supporting card | Enter from a staged central position or from the left; use a single gentle scale settle. |
| 04 | Central hero graphic | Draw, build, count, trace, or reveal the central graphic live. Do not simply fade it in unless requested. |
| 04b | Hero text | Reveal numbers and labels only after the main hero graphic is mostly built. |
| 05 | Right supporting card | Enter from the right with a color-coded `LIVE` tag if appropriate. |
| 06 | Final composition | Hold all modules in a balanced layout. Add low-intensity live signals: pulsing dots, moving data packets, breathing glow, or a slow scan line. |

## Motion Rules

### Entrance behavior
- Use **one clean entrance per module**.
- Use a fast but smooth ease-out; avoid repetitive bouncing.
- Allow a small 2–4% settle/overshoot only for information cards.
- Keep headline movement clean and premium: scale/fade, then reposition.
- Avoid camera shake, aggressive spinning, or random motion.

### Hero-graphic behavior
Choose an animation that explains the graphic:

- **Clock / ring**: draw clockwise from 12 o’clock; use a glowing travelling node.
- **Chart**: grow from baseline; animate data line or bars in reading order.
- **Map**: reveal boundaries or markers progressively.
- **Counter**: count only once the related visual container is visible.
- **Icon / orbit**: use a path trace, rotating marker, or controlled glow pulse.

### Final hold behavior
- Keep the composition readable and mostly stable.
- Use only small ambient movement:
  - `LIVE` dot pulse
  - slow data packet on connector line
  - 1–2 px vertical float
  - soft glow breathing
  - subtle scan sweep
- Respect `prefers-reduced-motion` in HTML previews.

## Layout Rules

- Maintain a clear reading hierarchy: **headline → left context → centre insight → right consequence**.
- Use final layout anchors in normalized coordinates or a 1280×720 reference grid.
- Keep safe margins around all elements.
- Do not cover text with `LIVE` badges or animation effects.
- Align card heights/visual weight when the design calls for symmetry.
- Use a dark, unobtrusive background when panels are extracted from a dark screenshot.

## Color Mapping

Derive roles from the source design:

```json
{
  "information": "cyan / blue",
  "hero": "orange / gold",
  "risk": "pink / red",
  "copy": "off-white",
  "secondaryCopy": "muted blue-grey",
  "background": "deep navy / charcoal"
}
```

Apply the same role color to:
- card border
- card label
- `LIVE` indicator
- connector line / data packet
- glow and accent animation

## Semantic HTML Requirement

For HTML references, all copy must be real text inside semantic HTML elements. Do not make the full design one background screenshot.

Use this structure:

```html
<header class="headline">...</header>
<article class="card card--info">...</article>
<section class="hero-graphic">...</section>
<article class="card card--risk">...</article>
<script id="motion-spec" type="application/json">...</script>
```

The HTML reference must include:

- real editable text
- CSS variables for colors
- JavaScript render function tied to a normalized 0–100 phase value
- play/pause and restart control
- phase scrubber (not fixed duration)
- machine-readable object exposed as `window.MOTION_REFERENCE`
- a written AI/editor instruction block

## Standard Machine-Readable Motion Spec

Embed this schema in the output HTML:

```json
{
  "name": "Short descriptive title",
  "format": {
    "width": 1280,
    "height": 720,
    "aspectRatio": "16:9",
    "duration": "decided by AI/video editor",
    "fps": "decided by AI/video editor"
  },
  "style": {
    "background": "description",
    "information": "#32ccff",
    "hero": "#ff862e",
    "risk": "#ff5274"
  },
  "timeline": [
    {"phase": "01", "element": "headline", "action": "centre fade/scale in"},
    {"phase": "02", "element": "headline", "action": "move to final top position"},
    {"phase": "03", "element": "left card", "action": "enter and settle"},
    {"phase": "04", "element": "hero graphic", "action": "draw/build live"},
    {"phase": "05", "element": "right card", "action": "enter and settle"},
    {"phase": "06", "element": "complete composition", "action": "hold with subtle live motion"}
  ],
  "finalLayout": {
    "headline": [0.5, 0.1],
    "leftCard": [0.18, 0.58],
    "hero": [0.5, 0.58],
    "rightCard": [0.82, 0.58]
  }
}
```

## Quality Checklist

Before delivering, verify:

- [ ] The first thing shown is the main title/dialog, not all panels.
- [ ] Every requested `LIVE` label appears at the correct reveal stage.
- [ ] Hero graphic is visibly constructed/drawn, not only faded in.
- [ ] All final elements align in a balanced composition.
- [ ] Final hold includes restrained ambient motion.
- [ ] Text is legible at the target display size.
- [ ] HTML uses phases/percentages—not a prescribed video duration.
- [ ] No external CSS, fonts, or scripts are required for the HTML preview.
- [ ] Machine-readable motion specification is embedded and accessible.

## Current Project Reference

Apply this skill to `demographic-clock-motion-reference.html` using this narrative order:

**Headline first → headline moves to top → blue demographic card → orange 2045 clock drawn live → red middle-income card → final connected dashboard.**
