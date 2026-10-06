# Benaqaab India — After Effects Mastery & Motion Craft Skill

**Version 1.0 · 1 October 2026**
**Requested by:** user — “learn all of Adobe After Effects, find the repos that teach it, and save them so our videos look wow.”

---

## 0. Read this first — what I can and cannot do with After Effects

**I cannot run After Effects.** It is Adobe’s proprietary, paid, GUI application for Windows/macOS. It
cannot be installed, licensed or executed in this Linux sandbox, and no amount of scripting changes
that. Any claim that I “rendered an AE comp” here would be false.

**What I actually did in this task:**

1. Verified the real AE open-source ecosystem through GitHub’s API (21 repositories, READMEs and
   selected source files retrieved and read).
2. Extracted the **craft knowledge** those tools encode — easing curves, spring physics, inertia,
   IK rigging, expressions, Lottie’s exact AE feature limits, render-automation schemas.
3. Wrote the **translation layer**: every AE technique mapped to an equivalent we *can* execute in
   our HTML/Canvas/Three.js/FFmpeg pipeline, with working code.
4. Built a runnable proof — `viz/motion_library.js` — so the “wow” techniques are demonstrable
   rather than theoretical.

**So there are two honest paths to “after-effects look”:**

- **Path A (if you have AE on your machine):** you design in AE → we hand off through a documented
  format → I composite/render in our pipeline. See §4 for the four handoff routes and their real limits.
- **Path B (what we do by default):** we don’t own AE, so we reproduce its *techniques* natively.
  §6 is the full mapping table, §7 is the “wow” recipe library. This is what makes our videos look
  expensive without owning Adobe anything.

---

## 1. What actually makes AE output look “wow”

Studying AE work, the expensive look never comes from an effect. It comes from five things, in order
of impact:

| # | What | Why it reads as expensive | Where it lives in AE |
|---|---|---|---|
| 1 | **Easing** | Nothing moves at constant speed; everything has intent | Graph editor, value vs speed graph |
| 2 | **Weight** | Objects react to force: squash, overshoot, settle, follow-through | Keyframes + expressions |
| 3 | **Depth** | Layers sit in a space with parallax, DOF, atmosphere | 3D layers, cameras, lights |
| 4 | **Light & grade** | Coherent light, bloom, grain, slight aberration, vignette | Effects stack + Lumetri |
| 5 | **Sound-locked timing** | Motion lands on the frame the sound lands | Timeline + audio waveform |

Everything in §7 is a recipe for one of these five.

---

## 2. Verified repository ledger

All entries confirmed live through the GitHub API on 1 October 2026 (stars, licence, archived flag
recorded in `knowledge/after_effects_research/REPO_AUDIT.json`). READMEs saved to
`knowledge/after_effects_research/source_snapshots/`.

### Tier 1 — directly usable in our pipeline

| Repo | Stars | Licence | What it teaches / gives us | How we use it |
|---|---|---|---|---|
| **airbnb/lottie-web** (+ **airbnb/lottie** docs) | 32.1k / 4.9k | MIT | The AE→JSON→web bridge. `after-effects.md` documents *exactly* which AE features survive export | Route A1 handoff; play AE-designed vector graphics offline in our HTML |
| **inlife/nexrender** | 1.9k | MIT | Data-driven AE render automation via `aerender` CLI; job JSON schema; render-farm support | If you have AE: batch-render many personalised videos from one template |
| **MysteryPancake/After-Effects-Fun** | 67 | MIT | Real expression code: quad/cubic/quart/quint easing, spring physics, loopOut ping-pong, accumulators | Source for our easing maths (§3.1) |
| **ae-scripting/scripting-snippets** | 215 | — | Practical ExtendScript patterns for automating AE | Reference when writing AE-side scripts for you |

### Tier 2 — data extraction & format research

| Repo | Stars | Licence | Value |
|---|---|---|---|
| **boltframe/aftereffects-aep-parser** | 129 | MIT | Parse `.aep` project files programmatically |
| **ChenxingM/AEP-Tools** | 5 | — | RIFF `.aep` + `.aepx` parser *with write-back*, Python + Rust, extracts comps/layers/keyframes |
| **Experience-Monks/ae-to-json** | 245 | MIT | Runs inside AE, dumps the whole project as structured JSON |
| **inlife/aftereffects-project-research** | 80 | — | Research notes on the undocumented AE project format |
| **Instrument/cyclops** | 225 | MIT | **Archived.** Exports only the *dynamics* of a motion (per-frame values) from AE to a JS easing function |

### Tier 3 — rigging, animation and CEP

| Repo | Stars | Licence | Notes |
|---|---|---|---|
| **RxLaboratory/Duik** (“Duik Ángela”) | 405 | **GPL-3.0** | Industry-standard open-source rigging: structures, IK, bones, parent-link constraints, and automations (wiggle, spring, bounce, wheel, looper, walk cycle). GPL — do not bundle its code into a closed product; learn from it or use it as a tool |
| **Adobe-CEP/CEP-Resources**, **Adobe-CEP/Samples** | 1.8k / 1.1k | Adobe terms | Official CEP extension samples — how AE panels/plug-ins are built |
| **aturtur/after-effects-scripts** | 151 | — | Large, commented script collection |
| **JoeMighty/AE-Toolkit** | 0 | — | 12 time-saving scripts + dockable UI |
| **LottieFiles/dotlottie-web**, **LottieFiles/lottie-player** | 890 / 1.7k | MIT | Runtime Lottie players for our HTML |
| **lottiefiles/lottie-docs** | 63 | CC-BY-4.0 | The Lottie/AEP spec reference |
| **dataclay/example-autografs** | 7 | Custom | Rigged AE template projects (non-commercial) |

**Repos deliberately rejected:** “free template pack” repositories that are download-bait for
cracked creative-suite installers. They carry no learnable code and are a malware/legal risk. Not
audited further, not used.

---

## 3. The craft core (what to actually learn)

### 3.1 Easing — the single biggest visual upgrade

AE’s real speed control is the **graph editor**, and the two graphs mean different things:

- **Value graph** — the property’s actual value over time.
- **Speed graph** — the *rate of change*. This is where professional motion is designed.

Key insight that most people miss: in the speed graph, **movement does not start from zero and stop
at zero**. An entrance that accelerates from 0 px/s reads as hesitant; a professional entrance starts
already moving fast and *settles*. That is why AE veterans decouple Influence (bezier handle length)
from Ease.

**Verified easing maths** (adapted from `MysteryPancake/After-Effects-Fun/expressions/easing.js`,
MIT):

```js
const EASE = {
  linear:      t => t,
  inQuad:      t => t*t,                       outQuad: t => t*(2-t),
  inOutQuad:   t => t<.5 ? 2*t*t : -1+(4-2*t)*t,
  inCubic:     t => t*t*t,                     outCubic: t => (--t)*t*t+1,
  inOutCubic:  t => t<.5 ? 4*t*t*t : (t-1)*(2*t-2)*(2*t-2)+1,
  inQuart:     t => t*t*t*t,                   outQuart: t => 1-(--t)*t*t*t,
  inOutQuart:  t => t<.5 ? 8*t*t*t*t : 1-8*(--t)*t*t*t,
  inQuint:     t => t*t*t*t*t,                 outQuint: t => 1+(--t)*t*t*t*t,
  inOutQuint:  t => t<.5 ? 16*t*t*t*t*t : 1+16*(--t)*t*t*t*t,
  // Expo/Back/Elastic are the "expensive" curves — see below
  outExpo:     t => t === 1 ? 1 : 1 - Math.pow(2, -10 * t),
  outBack:     (t, s=1.70158) => 1 + (--t) * t * ((s + 1) * t + s),
  outElastic:  t => t===0?0 : t===1?1 : Math.pow(2,-10*t)*Math.sin((t*10-0.75)*(2*Math.PI/3))+1
};
function easeValue(name, t, tMin, tMax, v1, v2) {          // universal helper
  const n = clamp((t - tMin) / (tMax - tMin), 0, 1);
  return (1 - EASE[name](n)) * v1 + EASE[name](n) * v2;
}
```

**Spring physics** (verified code from the same repo, credited there to Tim Haywood / WebKit’s
spring demo). Use real springs instead of `outBack` when an object should *settle*:

```js
function spring(t, mass=1, stiffness=100, damping=10, v0=0) {
  const w0 = Math.sqrt(stiffness / mass), zeta = damping / (2 * Math.sqrt(stiffness * mass));
  if (zeta < 1) {                                  // under-damped: overshoot + settle
    const wd = w0 * Math.sqrt(1 - zeta*zeta);
    const B = (zeta * w0 + -v0) / wd;
    return 1 - (Math.exp(-t*zeta*w0) * (Math.cos(wd*t) + B*Math.sin(wd*t)));
  }
  const B = -v0 + w0;                              // critically damped: no overshoot
  return 1 - ((1 + B*t) * Math.exp(-t*w0));
}
```

**Practical ranges that read as “expensive”:**
- UI/graphic entrance: `outQuint` 0.35–0.5 s, or spring(mass 1, stiffness 120–170, damping 14–20) for a hint of settle.
- Camera push: `inOutCubic` 1.2–2.5 s. Never `linear` except for constant physical processes (light travel, clock hands).
- Impact/landing: `outBack` with s ≈ 1.4–1.8, duration ≤ 0.3 s.
- Exit: **75 % of the entrance duration** (HyperFrames doctrine) — a slow exit reads amateur.

**Anti-pattern (very common in AI-generated animation):** linear interpolation everywhere,
opacity-only fades, everything entering at once. Fix: every entrance animates **2–3 properties
together** (e.g. y + opacity + scale), staggered by 3–6 frames (0.1–0.2 s at 30 fps).

### 3.2 Weight and physicality

- **Squash & stretch** — on impact, scale x up / y down by 8–20 %, recover over 4–6 frames. Volume
  should look preserved (sx · sy ≈ 1).
- **Anticipation** — before a fast move, a 2–4 frame counter-move in the opposite direction.
- **Overshoot & settle** — never stop dead on the final position; overshoot 4–8 % and settle.
- **Follow-through** — secondary elements lag 2–5 frames behind the parent.
- **Inertia / throw** — duplicated from the verified community expression lineage (Dan Ebberts →
  Conigs): bounce amplitude driven by `velocityAtTime()` at the incoming keyframe, with exponential
  decay. In our pipeline we precompute the same maths as a sampled curve.

### 3.3 Motion blur — the "shot on a real camera" tell

AE uses **shutter angle** (default 180° = half the frame interval). Motion blur is *temporal
integration*, not a directional blur filter. Web implementations that actually work:

1. **Accumulation (correct):** evaluate the frame at N sub-times within the shutter window
   (e.g. 8 samples = `t-Δ/2 … t+Δ/2`) and average the results with alpha weighting.
2. **Directional blur (cheap, wrong physics):** velocity-scaled linear blur. Fine for UI, wrong for fast impacts.

Rule: shutter 180° for normal motion, up to 360° for a fast whip-pan, 0° for a frame you want crisp
(the impact frame is often sharper than the blur around it).

### 3.4 Depth

- **Parallax:** separate layers by depth. Foreground moves most, background least. Do not fake it with one image.
- **Depth of field:** blur by depth plane; the focus plane stays sharp and the falloff is *bokeh-ish*, not a uniform gaussian.
- **Atmosphere:** atmospheric haze increases with distance, desaturating and lifting blacks. This one trick makes flat composites look dimensional.
- **Camera:** subtle handheld noise (2–6 px, multi-frequency) plus a slow dolly. Never a static camera for a heroic shot.

### 3.5 Compositing and the grade stack

Order matters — this is the standard “expensive” stack, bottom to top:

1. Background mesh / environment plate
2. Assets and subjects
3. Graphics and type (**keep type sharp — never grade it into mush**)
4. Light wrap / bloom — blur the bright areas of the layer beneath and screen them back onto the
   edge of the subject. This single effect is why good composites don’t look “pasted”.
5. Grade — contrast, saturation, warm/cool split
6. Chromatic aberration — 1–3 px channel offset, edges only
7. Film grain — animated, monochrome, subtle (2–5 % opacity)
8. Vignette — 10–25 %

Lottie’s official AE documentation confirms the export-side limits of all this: **no expressions, no
effects, no blending modes, no luma mattes, no layer styles** survive Bodymovin export. So for the
Lottie route, all grading must happen *after* export, in our renderer. (This is a verified constraint,
not a guess — see `airbnb/lottie/after-effects.md`.)

### 3.6 Type in motion

- **Text animators** (AE’s per-character property system) are the reason AE type looks alive: each
  glyph gets its own position/scale/rotation/opacity offsets with a range selector, an offset
  delay and an ease.
- Kinetic typography rules that hold everywhere: stagger 2–5 frames per unit, animate **position +
  opacity + a small rotation or scale**, add a per-word baseline drift, and let the *reading order*
  drive the timing, not a constant interval.
- Line-level (not letter-level) reveals read more expensive for documentary work; letter-level is for
  hype/energetic sections.

### 3.7 Expressions worth knowing (even in a non-AE pipeline)

| Expression | What it does | Our equivalent |
|---|---|---|
| `wiggle(freq, amp)` | Perlin-style random offset | Seeded value-noise, 2–3 octaves |
| `loopOut("cycle"/"offset"/"ping-pong")` | Repeats keyframes | Modulo time mapping (verified ping-pong via `valueAtTime(2*start + (q+1)*dur - time)`) |
| `linear(t, tMin, tMax, v1, v2)` | Clamped inverse-lerp remap | Our `easeValue` with `linear` |
| `ease(t, tMin, tMax, v1, v2)` | Smooth remap (auto bezier) | `easeValue` with `inOutCubic` |
| `valueAtTime(t)` | Sample another moment | Precomputed sample tables |
| `velocityAtTime(t)` | Speed at a moment — drives inertia | Numerical derivative of our sampled curve |
| `seedRandom(n, true)` | Deterministic randomness | Seeded PRNG (we use mulberry32) — **critical for deterministic export** |
| `index`, `thisComp.layer("X")` | Neighbour offsets, references | Array index / named object refs |
| `sourceRectAtTime()` | Auto-size a box to text | `ctx.measureText` |
| `toComp() / toWorld()` | Coordinate-space conversion | Our transform helpers |

**The determinism rule:** any expression using unseeded random breaks frame-accurate export. Every
random value in our projects must come from a seeded generator evaluated as a function of time — the
same discipline HyperFrames enforces (`no wall clock, no unseeded randomness, no mid-render fetch`).

---

## 4. Handing work between AE and our pipeline (four real routes)

### Route A1 — AE → Lottie JSON → our HTML player  *(best for vector graphics & logo motion)*
- In AE: convert Illustrator/SVG art to **shape layers**; keep text as text layers; **bake/convert
  expressions and effects to keyframes** first.
- Export with Bodymovin (JSON). Play with `lottie-web` or `dotlottie-web` using
  `goToAndStop(frame, true)` for frame-accurate control in our deterministic renderer.
- **Hard limits to respect:** no expressions, no effects, no blend modes, no luma mattes, no layer
  styles, path-keyframes are heavy (file size), export at 1× composition size.
- Result: resolution-independent, tiny, offline-playable graphics we can composite and grade ourselves.

### Route A2 — AE → rendered frames with alpha → our compositor  *(best for heavy VFX/3D in AE)*
- AE output module: **ProRes 4444 with alpha**, or a **PNG sequence** (alpha).
- We composite that layer into our HTML/FFmpeg pipeline and add grade, grain and sound on our side.
- Cost: file size; PNG sequences are safest for exact frames.

### Route A3 — AE → `aerender` → nexrender  *(best for many videos from one template)*
- nexrender drives `aerender` head­lessly with a **job JSON**: template path, composition name,
  output module, output extension, and an `assets` array that can substitute images/footage/data.
- It can run a render farm, and (per its README) does not require a licensed AE on every worker for
  render-only use.
- Practical note from its README: **AE 2023+ needs an explicitly configured output module**, or
  `aerender` may render nothing.

### Route A4 — AE project → JSON → we rebuild natively  *(best for full control, most work)*
- Parse `.aep`/`.aepx` with `aftereffects-aep-parser`, `AEP-Tools` or in-AE `ae-to-json`, then
  rebuild the motion as native canvas code.
- Worth it only when we want the motion data, not the pixels (e.g. extracting a rig’s animation
  curves to drive our own character).

**My recommendation for us:** Route A1 for graphic elements, Route A2 for hero VFX, and Path B
(native reconstruction) for everything else. Do not build a big film that exists only inside a
licensed app.

---

## 5. If you have AE — the accelerated learning path

Ordered by return on effort, with the exercise that proves each step:

1. **Easing + graph editor** (2 h) — animate one square with `outQuint`, one with a spring, one with
   `linear`; make the linear one feel obviously wrong.
2. **Timing & spacing** (2 h) — same move at 4 different durations; which one reads as heavy?
3. **Squash & stretch + anticipation** (2 h) — a ball land, with and without.
4. **Motion blur & shutter** (1 h) — whip-pan at 180° vs 360° vs 0°.
5. **Masks, track mattes, rotoscoping** (3 h) — alpha vs luma matte on the same reveal.
6. **Parenting → nulls → controllers** (3 h) — one slider driving five properties.
7. **Expressions** (4 h) — `wiggle` with `seedRandom`, `loopOut`, `linear/ease`, `valueAtTime`,
   inertia bounce.
8. **Text animators** (2 h) — per-character reveal with range selector + offset delay.
9. **3D layers, camera, DOF, lights** (4 h) — a 3-layer parallax with a real camera move.
10. **Compositing & grade stack** (3 h) — light wrap, bloom, grain, CA, vignette, in that order.
11. **Precomps + Essential Graphics** (1 h) — build a reusable title.
12. **Render/export discipline** (1 h) — ProRes 4444 alpha, PNG sequence, `aerender` CLI, output module gotchas.
13. **Rigging with Duik** (4 h) — a 2-bone limb with IK; animate a wave. (GPL licence noted.)

Total ≈ 32 hours to competent. The knowledge below is what we apply regardless of who owns AE.

---

## 6. Translation table — AE technique → our pipeline

| AE technique | Our implementation | Notes |
|---|---|---|
| Graph editor bezier easing | `EASE` functions (§3.1) or `gsap CustomEase` | Same maths, deterministic sampling |
| Spring / inertia | `spring(t, m, k, c, v0)` sampled into a curve | Verified code source in §3.1 |
| Motion blur (shutter angle) | N sub-frame samples averaged with accumulation buffer | 8 samples default; 16 for fast whips |
| Track matte (alpha) | `ctx.globalCompositeOperation = 'destination-in'` on an offscreen canvas | Compose layer-by-layer |
| Track matte (luma) | Luminance-to-alpha pass, then `destination-in` | Or WebGL shader for speed |
| Blending modes | Canvas GCO: `multiply`, `screen`, `lighter` (add), `overlay`, `soft-light`, `difference`, `hue`, `saturation`, `color`, `luminosity` | Full parity with AE’s core modes |
| Parent / child | Scene-graph transform hierarchy (parent world matrix × child local) | Order matters; anchor points = pivot offsets |
| Duik-style IK limb | 2-bone analytic IK: `θ₂ = π − acos((a²+b²−c²)/(2ab))` | Plus pole/angle constraints |
| Text animator + range selector | Per-glyph transform loop with index stagger and offset delay | Use `ctx.measureText` for advance widths |
| `wiggle` | Seeded multi-octave value noise | Never `Math.random()` — export must be reproducible |
| `loopOut` | Modulo time mapping; ping-pong per §3.7 | |
| Time remap / speed ramp | Map output time → source time with a custom curve | Clamp both ends |
| Camera shake | Multi-frequency noise on camera transform, amplitude envelope | 2–6 px at 1080p reads handheld |
| Depth of field | Layered blur by depth plane + slight highlight bloom | Not a uniform gaussian |
| Light wrap | Blur bright surroundings → `screen` back over subject edges | The “not pasted” fix |
| Glow / bloom | Bright-pass → blur → add | Keep type out of the bloom |
| Chromatic aberration | Per-channel offset, radial scale from centre | 1–3 px; more looks broken |
| Film grain | Animated deterministic noise overlay, 2–5 % | Must be seeded per frame index |
| Vignette | Radial gradient multiply | 10–25 % |
| LUT / grade | WebGL color-grade shader, or CSS `filter` chain for cheap cases | Grade assets and graphics together |
| 3D layers + camera | Three.js scene, or a faked 2.5D parallax with matched perspective | Only go 3D when the shot needs it |
| Precomps | Offscreen canvases / render caches | Cache static layers aggressively |
| Essential Graphics / MOGRT | Our JSON shot config + template functions | Data-driven, same idea |
| `aerender` / Media Encoder | FFmpeg + headless Chromium capture | What we already do |
| Lottie export | `lottie-web` / `dotlottie-web` with `goToAndStop` | Route A1 |

---

## 7. The “wow” recipe library

Concrete, parameterised, and testable. Each is a real technique, not a mood word.

1. **Ease stack.** Enter with `outQuint` (0.4 s) + 6-frame stagger across elements; settle with a
   spring (stiffness 150, damping 18). Never linear, never a lone fade.
2. **Impact frame.** At the contact frame, hold max contrast for exactly 2 frames, add a 1-frame
   white flash at 8–15 % opacity, and cut motion blur to 0 for that frame only. This is the single
   most “cinematic” 3-frame sequence you can build.
3. **Speed ramp.** 0.15 s at 300 % speed into the impact, then 0.4 s at 40 % for the aftermath.
   Curve both ends — linear ramps look like a mistake.
4. **Smear frame.** One frame of elongated/stretched geometry at the peak of a fast move. Older than
   Disney, still unbeaten for perceived speed.
5. **Squash & stretch chart.** sx · sy ≈ 1, 8–20 % deformation, recover in 4–6 frames.
6. **Layered parallax.** Three depth planes minimum, motion multiplied by depth (e.g. 1.0 / 0.45 /
   0.15), with atmospheric desaturation on the furthest plane.
7. **Light wrap composite.** Blur the background where it meets the subject, screen it back at 25–45 %.
8. **Atmosphere stack.** Grain 3 % + vignette 18 % + CA 2 px + bloom on highlights only. Applied
   *after* the grade, never before.
9. **Sound-locked landings.** Every visual impact lands on the audio transient’s frame, not near it.
   We generate our own SFX, so we can place them exactly.
10. **Match-cut seams.** Carry one object across the cut at matched position *and* velocity; the eye
    follows the object, not the frame change.
11. **Kinetic type ladder.** Per-word reveal (2–4 frame stagger) + 4 px baseline drift + 0.98→1.0
    scale, with the emphasis word landing last.
12. **Breathing camera.** Slow dolly 1.02→1.06 over the shot plus multi-frequency 2 px handheld
    noise. Removes the “static image” feel without looking like a screensaver.

**When NOT to use these:** a data diagram, a legal caveat, a reading-heavy chart, a respectful
moment. Motion must serve comprehension. Forcing a whip-pan onto a temperature comparison makes it
worse, not “wow”. Restraint is also a technique.

---

## 8. Critique checklist for motion quality

Run this before shipping any animation:

- **Pause test** — pause at 3 random moments: is something meaningful mid-motion, or is the frame waiting?
- **Mute test** — with audio off, does the visual still communicate the beat?
- **Linear hunt** — find any property moving at constant speed that isn’t a physical constant. Fix it.
- **Settle check** — does everything arrive *and stop dead*? Add overshoot or follow-through.
- **Edge check at 100 %** — masks, light wrap, CA and grain edges — the places AI composites give themselves away.
- **Type check** — is the text still sharp after the grade? (If the grade blurred your type, you graded in the wrong order.)
- **Determinism check** — capture the same timestamp twice, out of order; pixels must match byte-for-byte.
- **Mobile check** — 1080×1920 at phone size: the smallest label must still be readable.

---

## 9. What I still cannot claim

- I have never executed After Effects, Bodymovin, Duik, nexrender or `aerender`. The repo knowledge
  above is from verified README/source inspection, not from running them.
- The AE feature limits in §4 are quoted from Airbnb’s official Lottie/AE documentation; feature
  support changes over time and must be re-checked against the version you use.
- The web-side implementations in §6 are code I can write and test in our pipeline; the AE-side
  steps in §4 are instructions for your machine.
- “Wow” is a judgement. §7 and §8 make it measurable enough to improve deliberately, but the final
  call is yours.

---

## 10. Files

- Verified audit: `knowledge/after_effects_research/REPO_AUDIT.json`
- Source inspects: `SOURCE_INSPECTION.json`, `EXPRESSION_SOURCES.json`
- Saved READMEs & expression code: `knowledge/after_effects_research/source_snapshots/`
- Runnable proof: `viz/motion_library.js`
- This skill: `SKILLS_AFTER_EFFECTS.md`
- Master handbook: `MASTER_VIDEO_GENERATION_SKILLS.md` (chapter 35B)
