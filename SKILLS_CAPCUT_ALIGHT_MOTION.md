# Benaqaab India — CapCut + Alight Motion Skill

**Version 1.0 · 1 October 2026**
**Companions:** `knowledge/capcut_alight_research/LEARNINGS.md` · `viz/motion_library.js` ·
`tools/capcut_draft.py` · `tools/alight_project.py`

---

## 0. The boundary, stated once

CapCut and Alight Motion are **proprietary apps**. They cannot be installed or run in this Linux
workspace, and no app export can be produced here. What we *do* is deliverable and tested:

| Path | Deliverable | Status |
|---|---|---|
| **A — for the app** | A CapCut draft folder or an Alight Motion `.xml` you import and export yourself | Writers built and structurally tested |
| **B — for our renderer** | The official transitions reimplemented in our canvas engine and rendered to MP4 here | Built, phase-audited, rendered |

Never claim an app rendered anything. Never claim our reimplementation is the app's exact shader.

---

## 1. The official catalogues (saved, with ids and durations)

**3,424 CapCut items** parsed from open-source metadata tables that mirror the app's own ids —
saved in `knowledge/capcut_alight_research/CATALOG_*.json` and `tools/data/capcut_*.json`:

| Library | Items | Free | VIP | Use it for |
|---|---|---|---|---|
| Transitions | 1,130 | 147 | 983 | cuts between shots |
| Video intros | 250 | 43 | 207 | shot entrances |
| Video outros | 217 | 22 | 195 | shot exits |
| Group animations | 107 | 71 | 36 | whole-scene motion |
| Text intros | 182 | 62 | 120 | title entrances |
| Scene effects | 1,582 | 314 | 1,268 | atmosphere, light, texture |
| Character effects | 251 | 120 | 131 | subject treatment |
| Filters | 454 | 112 | 342 | the base grade |

**Default durations are real CapCut values and they cluster hard:** 2.0 s (×475), 1.0 s (×168),
0.5 s (×161), 0.8 s (×41). Use the catalogue's own duration unless the edit needs otherwise.

**VIP discipline:** 87 % of transitions are VIP. When we build a draft for a free account, filter
`free == true` first. Reliable free staples: **White Flash 0.40 s**, **Fold Over 1.00 s**,
**Cutout Flip 0.80 s**, **叠化 dissolve 0.50 s**.

**Alight Motion:** 196 documented effects across 12 categories (from the decompiled-APK docs), 24
blend modes, 7 layer types, 20 parametric shape templates. Effect ids are canonical, e.g.
`com.alightcreative.effects.gaussianblur`.

---

## 2. Adding a transition to one of our films (Path B — the normal case)

Every film we render is a seekable HTML composition. A transition is just a function of normalised
progress `u`, drawn between two visual states. The standard library lives in
`viz/motion_library.js`; lift the function you need, or write a new one in the same shape:

```js
// u: 0 -> 1 across the transition. A = outgoing, B = incoming (both are drawable).
T['White Flash'] = (c,u,w,h)=>{                 // official CapCut 0.40 s
  c.drawImage(A,0,0,w,h);
  if(u<.5){ c.fillStyle='#ffffff'; c.globalAlpha=E.inQuad(u*2); c.fillRect(0,0,w,h); }
  else { c.drawImage(B,0,0,w,h); c.fillStyle='#ffffff'; c.globalAlpha=1-E.outCubic((u-.5)*2);
         c.fillRect(0,0,w,h); }
  c.globalAlpha=1;
};
```

Rules that keep it professional:
- **Duration from the catalogue**, not from taste — then adjust only if the beat demands it.
- **One transition per cut.** Two competing effects read as an accident.
- **Half-out, half-in.** Every transition should be honestly reversible: if it looks wrong played
  backwards, it is wrong.
- **Land on the sound.** The transition's end frame should be the audio transient's frame.
- **Motion blur is free** — the house renderer samples sub-frames when `window.speed(t)` reports a
  fast frame. Give it a real number; don't leave it at 0.
- **Deterministic only.** Seeded noise, never `Math.random()` at draw time.

### Which transition for which cut
| Cut type | Use | Avoid |
|---|---|---|
| Same scene, time passing | Dissolve · 叠化 | glitch families |
| Beat hit / impact | White Flash, Neon, Snap Zoom | long dissolves |
| Location change | Swipe Left, Corner Slide, Fold Over | nothing |
| Reveal / subject change | Cube Rotate, Fold Over, Flip Page | Film Burn |
| Chaos / signal / warning | Signal Glitch 2, Jerky Camera | soft families |
| Emotional close | Wide Ripple, Shrink | glitch families |

---

## 3. Generating a draft for the real app (Path A)

```python
from tools.capcut_draft import Draft, Material, Clip, Transition
import json
cat = {t['display_name']: t for t in json.load(open('tools/data/capcut_transitions.json'))}
d = Draft(1080, 1920, 30, 'My video')
a, b = Material('shot_a.mp4'), Material('shot_b.mp4')
t = cat['White Flash']                      # official id, duration and VIP flag
d.add(Clip(a, 0, 6_000_000, transition=Transition(
        t['display_name'], t['resource_id'], t['effect_id'], md5, int(t['duration_s']*1e6), t['paid'])))
d.add(Clip(b, 6_000_000, 6_000_000))
print(d.write('drafts/My Video', copy_media=True))
```

That writes `draft_content.json` + `draft_meta_info.json` (+ a `media/` folder). Open it in CapCut
(import-draft or copy into the draft root). The app resolves the effect resources; VIP ones stay VIP.

For Alight Motion, build the scene and validate before exporting:

```python
from tools.alight_project import Scene, Element, Effect, Property, Keyframe, adjustment_layer, FX
sc = Scene(title='My video', width=1080, height=1920, total_time_ms=6000, fps=30)
sc.add(Element.text_layer(540, 820, 'BENAQAAB', size=120, id=2))
title = sc.elements[-1]
title.props.append(Property('size','float', keyframes=[
    Keyframe(0.0, 0.40, 'cubicBezier 0.480224 0.0 1.0 1.0'), Keyframe(0.5, 1.0)]))
sc.add(adjustment_layer(1080, 1920, [Effect(FX+'exposure', {'exposure': 0.06}),
                                     Effect(FX+'vignette', {'radius': 0.62, 'strength': 0.35})],
                        label='Grade', eid=3, start=0, end=6.0))
sc.write('scene.xml')
from tools.alight_project import validate; print(validate('scene.xml')['problems'])   # must be []
```

The documented rule that matters most: an **adjustment layer** grades everything beneath it, but
only if its first effect is **Copy Background** (`com.alightcreative.effects.lift`, `fill = 0`) and
its plate covers the frame — `.rect` is 100×100 units, so `scale = canvas / 100` (1080 → 10.8).

---

## 4. The grade stack (Alight Motion's own documented order, adopted for us)

1. Content (background + subject)
2. **Duotone core** — split-tone: cool shadows, warm highlights
3. **Exposure lift** — exposure + contrast
4. **Glow / bloom** — blurred copy of the composite, screened back
5. **Finishing** — sharpen, vignette, grain (seeded)

Type always goes **above** the grade so it stays crisp. This matches what we already do, and it now
has independent confirmation from a second tool's documentation.

---

## 5. Quality gates before any film ships

1. **Determinism** — capture 8+ timestamps, re-capture them shuffled; SHA-256 must match.
2. **Phase audit** — every transition sampled at u = 0.12/0.35/0.50/0.70/0.90 must change the frame;
   a transition whose numbers are flat is a bug, not a style.
3. **No dead frames** — check min/max brightness across the transition, not just the midpoint.
4. **Zero page errors** in the browser console at every stage.
5. **Motion blur present** — `window.speed(t)` must return a real magnitude on fast cuts.
6. **Sound on the frame** — every transition onset has an SFX onset within one frame.
7. **Readable at 1080×1920 on a phone** — cell labels, captions, type.

---

## 6. Files

- Knowledge base: `knowledge/capcut_alight_research/LEARNINGS.md`
- Evidence: `REPO_AUDIT.json`, `CATALOG_*.json`, `CATALOG_SUMMARY.json`, `ALIGHT_SOURCES.json`,
  `ALIGHT_ASSET_COUNTS.json`, `source_snapshots/`
- Engine: `viz/motion_library.js` (24 transitions, official names/durations)
- Tools: `tools/capcut_draft.py`, `tools/alight_project.py`, `tools/data/capcut_*.json`
- Demo render: `demos/Transition_Demo_CapCut_Alight_1080x1920.mp4`
- Test evidence: `.cache/ae_research/TRANSITION_TEST.json`, `PHASE2.json`, `LAB_TEST.json`
