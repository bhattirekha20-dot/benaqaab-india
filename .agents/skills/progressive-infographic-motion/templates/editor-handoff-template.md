# Motion Editor Handoff — [PROJECT NAME]

## Important delivery rule

Use the phases below as order and relative pacing only. **The AI/video editor chooses final duration and FPS.**

## Source assets

| Asset | Module | Role | Final anchor | Accent | Motion |
|---|---|---|---|---|---|
| `[path]` | Header | Primary message | Top centre | Gold | Centre reveal → move to top |
| `[path]` | Left card | Context | Left | Cyan | Enter → settle |
| `[path]` | Hero | Key insight | Centre | Orange | Draw/build live |
| `[path]` | Right card | Risk/consequence | Right | Pink | Enter → settle |

## Locked copy

- Headline: `[text]`
- Subheadline: `[text]`
- Left card: `[label, title, bullets]`
- Hero labels: `[text]`
- Right card: `[label, title, bullets]`
- CTA/ticker: `[text]`

## Layer order

```text
01_Header
02_Header_Live
03_Left_Context_Card
04_Left_Live
05_Central_Hero_Graphic
06_Central_Hero_Text
07_Central_Live
08_Right_Risk_Card
09_Right_Live
10_Connection_Left
11_Connection_Right
12_Final_Ambience
```

## Relative phase order

1. **Phase 01:** Headline appears in the centre with `LIVE`.
2. **Phase 02:** Headline moves to its final top position.
3. **Phase 03:** Left information card enters and settles.
4. **Phase 04:** Central graphic draws/builds live; hero text appears late in this phase.
5. **Phase 05:** Right risk/consequence card enters and settles.
6. **Phase 06:** All elements hold. Add only subtle ambient motion.

## Hero graphic direction

- Graphic type: `[clock / ring / chart / counter / map / custom]`
- Build direction: `[clockwise from 12 o’clock / baseline up / left-to-right / custom]`
- Text reveal rule: `[reveal after hero is mostly built]`

## Final-layout map

Use normalized anchors so the editor can adapt to 16:9, 9:16, or 1:1:

```json
{
  "headline": [0.5, 0.1],
  "leftCard": [0.18, 0.58],
  "hero": [0.5, 0.58],
  "rightCard": [0.82, 0.58]
}
```

## Ambient motion limits

- LIVE dots: soft pulse only.
- Connector packets: slow, clear data travel.
- Glow: gentle breathing, no harsh flash.
- Floating panels: maximum 1–2 px equivalent drift.
- Text: stable after it enters.
