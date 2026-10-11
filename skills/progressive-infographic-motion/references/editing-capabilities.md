# Extended Editing Capabilities

Use this reference alongside `../SKILL.md` when a project needs more than the basic staged dashboard sequence.

## 1. Reference Analysis and Asset Preparation

### Supported input styles

- One complete screenshot / poster
- Multiple cropped panel screenshots
- Logo plus separate text / icon assets
- A design mockup plus written animation request
- A video frame that needs a reconstructed HTML layout
- Mixed-language text, including Hindi + English dashboards

### Required analysis

For each source image, identify:

1. **Module type** — header, card, chart, clock, ticker, button, badge, logo, background, CTA.
2. **Role** — primary message, context, hero, risk, proof, CTA, ambient decoration.
3. **Reading order** — what should be understood first, second, third.
4. **Color role** — information, active/live signal, danger/risk, secondary copy.
5. **Animation potential** — entrance, draw-on, counter, scan, glow, pulse, data travel, hold state.
6. **Text safety** — text that must never be hidden, clipped, or replaced.

### Asset map format

```json
{
  "asset": "panel-blue.png",
  "module": "context card",
  "role": "information",
  "finalAnchor": "left",
  "entrance": "slide/settle",
  "accent": "cyan",
  "liveLabel": true,
  "sourceTextLocked": true
}
```

## 2. Supported Motion Patterns

### Editorial / dashboard patterns

| Pattern | Best for | Motion rule |
|---|---|---|
| Centre-to-anchor title | headline/dialog | Reveal large at centre, then park in its final header position. |
| Context-card reveal | information cards | Slide or scale in once, then settle. |
| Live ring / clock | countdowns, circular KPIs | Trace clockwise with node and glow; reveal numeric label late. |
| Graph draw | lines, bars, charts | Build from baseline or first data point. |
| Data packet | related panels | Small bright point travels along a slim connector. |
| Signal scan | technology/data feel | Low-opacity sweep across the composition; use sparingly. |
| Counter | figures/KPIs | Count during hero reveal only; stop when final value is reached. |
| Ticker | alerts / bilingual message | Fade or horizontal flow after core information is visible. |
| CTA reveal | final action | Appear last, after viewers have understood the evidence. |

### Transition patterns

- Clean fade + scale
- Directional slide + soft settle
- Mask reveal
- Draw-on SVG/path reveal
- Radial reveal for clocks and circles
- Section reflow / rearrangement
- Crossfade between chart states
- Data-linked connector animation

Avoid random glitching, excessive zooms, or more than one major effect per element.

## 3. Text and Data Support

### Dynamic text

Support these values as editable data rather than image pixels:

- headline and subheadline
- status label / date label
- KPI number and units
- bullet lists
- chart labels
- ticker / alert text
- `LIVE` labels
- CTA copy
- brand / campaign name

### Data-driven content model

Use a central config object in HTML/JS:

```js
const CONTENT = {
  headline: "...",
  labels: { information: "TODAY", risk: "RISK" },
  figures: { current: 2730, target: 10000 },
  bullets: { left: [], right: [] },
  ticker: []
};
```

When data changes, preserve the motion order and final visual hierarchy.

### Localization

- Keep original script, punctuation, and numbers where required.
- Use font fallbacks that support the user’s language.
- Never animate text by splitting characters if it could break Indic scripts, Arabic, or other shaped text.
- For bilingual panels, animate whole phrases/lines rather than individual glyphs.

## 4. Video-Editor Handoff Support

Every motion project should include an editor handoff manifest containing:

- canvas / aspect-ratio recommendation
- final layout map in normalized coordinates
- layer names
- phase order
- entrance type per layer
- color tokens
- text copy and locked text fields
- hero graphic draw direction
- ambient motion rules
- asset paths / source panels

Use `../templates/editor-handoff-template.md`.

### Layer naming convention

```text
01_Header
02_Header_Live
03_Left_Context_Card
04_Left_Live
05_Central_Hero_Ring
06_Central_Hero_Text
07_Central_Live
08_Right_Risk_Card
09_Right_Live
10_Connection_Left
11_Connection_Right
12_Final_Ambience
```

## 5. HTML Preview Support

An editable HTML motion reference should support:

- responsive 16:9 preview
- phase scrubber from 0–100
- play/pause/restart/loop
- `prefers-reduced-motion`
- semantic text elements
- CSS color tokens
- a JSON motion manifest
- `window.MOTION_REFERENCE`
- no dependency on external resources for the preview

The preview is an instruction/reference tool, not a declaration of final render length.

## 6. Quality and Accessibility Support

- Maintain readable contrast for text and labels.
- Do not communicate meaning with color alone; labels/icons should also carry meaning.
- Make `LIVE` labels decorative only if they are repeated; otherwise use accessible text.
- Avoid rapid flash effects.
- Respect reduced-motion preferences in browser references.
- Check that final frame can hold on screen without looking unfinished.

## 7. Optional Advanced Modes

Use only if the user asks:

- voice-over / caption synchronization
- audio-reactive data pulse
- vertical 9:16 and square 1:1 re-layout
- multi-scene explainer sequences
- branded lower thirds
- interactive hover/click states for web
- exported SVG animation / Lottie-ready vector plan
- multi-language content variants
- dynamic API/CMS data binding

For all advanced modes, retain the primary sequence: **main message → evidence/context → hero insight → risk/impact → final composition**.
