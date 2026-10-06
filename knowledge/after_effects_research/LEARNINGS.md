# After Effects — Saved Knowledge Base

**Location:** `knowledge/after_effects_research/` · **Compiled:** 1 October 2026
**Companion skill:** `/home/user/SKILLS_AFTER_EFFECTS.md` · **Runnable proof:** `viz/motion_library.js`

---

## Why this file exists

The user asked to "learn all of After Effects" so that our videos look outstanding. After Effects is
proprietary, paid, Windows/macOS-only software; it cannot be installed or executed in this Linux
workspace. So this knowledge base does the two things that *are* possible and useful:

1. It records what the real AE ecosystem actually contains, **verified repo by repo**, so the claim
   "I know AE" rests on inspectable evidence rather than assertion.
2. It converts every AE technique into a form our pipeline can execute — with the maths, the
   parameter ranges, and a tested implementation.

**Hard boundary, stated once and never blurred:** nothing here was produced by running After
Effects, Bodymovin, Duik, `aerender` or nexrender. Every repo claim is README/source/documentation
inspection. Every *implementation* claim (the lab, the easing curves, the determinism test) is code
that was actually run in this workspace and is reported with its measured result.

---

## Part 1 — Verified repository ledger

Method: GitHub REST API via `urllib`, `Accept: application/vnd.github+json`, user-agent
`Benaqaab-Research`, checked 1 October 2026. Raw JSON in `REPO_AUDIT.json`; saved README/source
snapshots in `source_snapshots/`; SHA-256 recorded in `SOURCE_INSPECTION.json` and
`EXPRESSION_SOURCES.json`.

### Verified live (18 repos + 4 Adobe/Lottie extras)

| Repo | Stars | Licence | Archived | What it is |
|---|---|---|---|---|
| airbnb/lottie-web | 32,138 | MIT | no | AE→JSON exporter (Bodymovin) + web player |
| airbnb/lottie | 4,953 | MIT | no | Official docs incl. `after-effects.md` feature limits |
| inlife/nexrender | 1,858 | MIT | no | Data-driven, headless `aerender` automation |
| LottieFiles/lottie-player | 1,657 | MIT | no | `<lottie-player>` web component |
| Adobe-CEP/CEP-Resources | 1,842 | Adobe terms | no | Official CEP extension/panel dev resources |
| Adobe-CEP/Samples | 1,087 | Adobe terms | no | Official sample panels |
| LottieFiles/dotlottie-web | 890 | MIT | no | `.lottie` player (smaller, zipped format) |
| RxLaboratory/Duik | 405 | GPL-3.0 | no | Industry-standard open-source rigging |
| Experience-Monks/ae-to-json | 245 | MIT | no | In-AE project → JSON dump |
| Instrument/cyclops | 225 | MIT | **yes** | Per-frame dynamics export → JS easing |
| ae-scripting/scripting-snippets | 215 | — | no | ExtendScript automation patterns |
| lottiefiles/lottie-js | 170 | MIT | no | Programmatic Lottie JSON construction |
| aturtur/after-effects-scripts | 151 | — | no | Large commented script collection |
| boltframe/aftereffects-aep-parser | 129 | MIT | no | `.aep` parser (successor to `aepx.js`) |
| inlife/aftereffects-project-research | 80 | — | no | Reverse-engineering notes on the `.aep` format |
| MysteryPancake/After-Effects-Fun | 67 | MIT | no | Expression library with source |
| lottiefiles/lottie-docs | 63 | CC-BY-4.0 | no | Lottie/AEP format specification |
| ae-scripting/Expressions | 16 | MIT | no | Expression snippet collection |
| dataclay/example-autografs | 7 | Custom (non-commercial) | no | Rigged AE templates |
| ChenxingM/AEP-Tools | 5 | none stated | no | `.aep` + `.aepx` parse *and write-back*, Rust-accelerated |
| JoeMighty/AE-Toolkit | 0 | none stated | no | 12-script panel toolkit |

**Not found:** `adobe/CEP-Resources` — 404. The correct org is **Adobe-CEP**. Recorded so nobody
repeats the dead lookup.

### Explicitly rejected

Link-dump repositories that advertise "free AE template packs" and redirect to Google Drive
archives of cracked Creative Suite installers. No learnable code, real malware and licence risk.
Not audited, not used, not linked.

**Licence caution carried forward:** Duik and its siblings are **GPL-3.0**. GPL is a copyleft
licence — learn from it or run it as a tool, do not paste its code into a closed product. nexrender
and the Lottie repos are MIT (attribution only). `dataclay/example-autografs` is non-commercial.
`ChenxingM/AEP-Tools`, `aturtur/after-effects-scripts`, `ae-scripting/scripting-snippets` and
`JoeMighty/AE-Toolkit` state **no licence** — treat as all-rights-reserved: read for understanding,
do not redistribute their code.

---

## Part 2 — The craft knowledge (what "AE quality" actually is)

### 2.1 Timing is read from the graph editor, not the keyframes

AE exposes two graphs and they are not interchangeable:

- **Value graph** — the property value over time. What the audience sees.
- **Speed graph** — the derivative. What the audience *feels*.

The professional tell: **an entrance that starts from zero velocity reads hesitant.** Real objects
entering frame are already moving. Practically: pull the first bezier handle so the curve leaves the
origin steeply, and pull the last handle so it flattens into the landing. In code that is
`outQuint` / `outExpo` (fast out, long settle) rather than `inOutQuad` (slow out, slow in).

**Empirical curve choice, by intent:**

| Intent | Curve | Duration |
|---|---|---|
| UI / graphic entrance | outQuint | 0.35–0.50 s |
| Physical settle (object lands) | spring, mass 1, stiffness 120–170, damping 14–20 | 0.5–0.9 s to rest |
| Camera move | inOutCubic | 1.2–2.5 s |
| Impact / recoil | outBack, s ≈ 1.4–1.8 | ≤ 0.30 s |
| Exit | — | **75 % of the entrance** |
| Constant physical process | linear | — |

### 2.2 Expressions — verified source, and what each one is for

Retrieved from `MysteryPancake/After-Effects-Fun` (MIT). Full files in
`source_snapshots/MysteryPancake__After-Effects-Fun__expressions__*.js`.

- `easing.js` — quad/cubic/quart/quint in+out functions plus a universal
  `customEasing(name, t, tMin, tMax, v1, v2)` that clamps, inverse-lerps, applies the curve and
  lerps. This is exactly the shape our renderer uses.
- `easing4.js` — a real **spring**: `spring(t, mass, stiffness, damping, initialVelocity)` with the
  under-damped and critically-damped branches written out, credited there to Tim Haywood via WebKit's
  spring demo. This is the single most valuable file in the collection: springs read as physical in
  a way tuned beziers never quite do.
- `loopOut.js` — ping-pong looping implemented with `valueAtTime(2*timeStart + (quant+1)*duration - time)`
  and a `quant = floor((time - timeStart)/duration)` guard against divide-by-zero when `numKeys < 2`.
- `accumulator.js` — integrates another property's value across every frame so far
  (`for t = 0; t < time; t += thisComp.frameDuration`). Useful pattern for "distance travelled"
  readouts.
- `counter.js` — the classic rolling-digit number: `[0, (b - a) * offset]` where `a` is the current
  value and `b` is the previous frame's value. A cheap, very effective data-viz device.
- `cameraSnap.js`, `pathRotation.js`, `polarToCartesian.js`, `biasedWiggle.js` — motion helpers worth
  knowing by name.

### 2.3 Motion blur is temporal integration

AE's **shutter angle** (default 180°) is not a filter; it is how long the virtual shutter stays open.
180° means half the frame interval. Correct web implementation: evaluate the scene at N sub-times
spread across the shutter window and **average**. A directional blur is a different, physically wrong
effect that happens to look similar on straight-line motion and wrong on everything else.

Also: the **impact frame is often the sharpest frame in the shot.** Cutting blur to 0 for the contact
frame and holding it for 2 frames is a real editorial technique, not a trick.

### 2.4 Text animators

AE's per-character properties (position, scale, rotation, opacity, tracking, fill) driven by a
**range selector** with an **offset** are why AE type feels alive. The range selector is the original
stagger: animator properties apply with a delay across the character index, and the offset slides
that window along the text. Reimplemented in code, it is a per-glyph transform loop keyed on index
with `ctx.measureText` for advance widths.

### 2.5 Lottie's exact AE feature limits (documented, not guessed)

From `airbnb/lottie/after-effects.md` (saved verbatim in `source_snapshots/`):

- **Supported:** shape layers, fills, strokes, gradients, trim paths, masks, solids, images, text,
  parenting, transform properties.
- **Not supported:** expressions, effects from the effects menu, blending modes, luma mattes, layer
  styles (drop shadow, colour overlay, stroke).
- Convert Illustrator/EPS/SVG/PDF art to **shape layers** or it will not export.
- Export composition at **1× the asset size**; pixel values become points/dp on mobile.
- **Glyphs** option converts text to shapes (needed when the font will not be available).
- Heavy path keyframes explode file size — avoid auto-trace and the wiggler for export.
- Alpha matte cost scales with the **size of the matte**; keep mattes as small as possible.
- Debug broken exports by exporting layer subsets to isolate the offender.

**Consequence for us:** every one of the unsupported features (grade, glow, grain, CA, vignette)
must be applied **after** export, in our renderer. That is not a limitation for our pipeline — it is
where we already do our compositing.

### 2.6 Render automation, honestly

`nexrender` drives `aerender` from a job JSON: template path, composition, output module, output
extension, and an `assets` array that swaps images/footage/data per render. It supports render farms
and, per its README, render-only workers do not each need a licensed AE. One documented trap: **AE
2023 and later need an explicitly configured output module, or `aerender` can render nothing and
report success.** Worth knowing before anyone promises a batch pipeline.

---

## Part 3 — The translation table

| AE | Our pipeline | Status |
|---|---|---|
| Graph-editor bezier easing | `EASE` table in `SKILLS_AFTER_EFFECTS.md` §3.1 | tested in the lab |
| Spring / settle | `spring(t, m, k, c, v0)` | tested in the lab |
| Motion blur (shutter) | N-sample accumulation, additive weighting | tested in the lab |
| Track matte alpha | `destination-in` on an offscreen canvas | implemented in prior films |
| Track matte luma | luminance→alpha pass, then `destination-in` | technique, not yet used |
| Blend modes | Canvas GCO (`multiply`/`screen`/`lighter`/`overlay`/… ) | implemented |
| Parent/child | transform hierarchy, parent world × child local | implemented |
| IK limb (Duik) | 2-bone analytic: `θ₂ = π − acos((a²+b²−c²)/(2ab))` | maths only, not yet built |
| Text animator | per-glyph loop + index stagger + offset delay | implemented |
| `wiggle` | seeded multi-octave noise | seeded, verified deterministic |
| `loopOut` | modulo time mapping / ping-pong | verified source captured |
| Camera shake | multi-frequency noise on the camera transform | implemented in prior films |
| DOF | blur by depth plane, not uniform gaussian | technique |
| Light wrap | blur bright surroundings → `screen` over the edge | tested in the lab |
| Bloom | bright-pass → blur → add | tested in the lab |
| Chromatic aberration | per-channel radial offset, 1–3 px | tested in the lab |
| Film grain | seeded noise per frame index | tested in the lab |
| Vignette | frame-corner radial darkening, 10–25 % | tested in the lab |
| Grade | WebGL shader or CSS `filter` chain | implemented |
| 3D layers + camera | Three.js, or 2.5D parallax | implemented |
| `aerender` / Media Encoder | FFmpeg + headless Chromium capture | the render path we use |

---

## Part 4 — What the test actually proved

`viz/motion_library.js` was loaded in headless Chromium 154 and captured via
`page.evaluate('window.captureFrame(t)')`.

- **Determinism:** frames at t = 0.0, 1.2, 3.4, 5.6, 7.9, 9.3, 11.6 s captured, then re-captured in
  shuffled order (9.3, 0.0, 7.9, 1.2, 11.6, 3.4, 5.6). **All seven SHA-256 digests matched.** Raw
  evidence: `.cache/ae_research/LAB_TEST.json`.
- **Page errors:** `[]` — no exceptions.
- **Export contract:** `window.renderFrame(t)`, `window.__SEEK__(t)`, `window.captureFrame(t, type, q)`,
  `DURATION`, `FPS`, `TOTAL_FRAMES`, `__READY__` — the same contract our films expose.

### Problems found in testing and fixed

Three real layout/craft defects were caught by cropping the rendered frames and looking at them, then
fixed and re-tested:

1. **Motion-blur panel:** the single-sample box was drawn over the "12 samples inside a 180° shutter"
   caption. Rows and captions repositioned; panel grew 232→262 px.
2. **Weight panel:** the "weighted" label collided with the parameter note line, and the motion trail
   fell through the ground plane. Label/note separated; the trail is now clipped above the ground.
3. **Grade panel:** the title collided with the stage name and the step indicator overlapped the
   corner caption; and the vignette was implemented as a dark ring around the subject. Rebuilt the
   stage name and step bar into separate rows, and the vignette now darkens the **frame corners**
   with the type drawn over it — which is also the correct "keep type sharp, grade underneath" rule.

---

## Part 5 — Honest limits

- After Effects was never installed, licensed, or run. No `.aep` file was created, opened or parsed
  in this workspace.
- Bodymovin, Duik, nexrender, `aerender`, CEP panels: **README/source inspection only.** None was
  executed. Their documented behaviour is reported as documented, not as experienced.
- The `.aep` parsers were verified to exist and were read; the format itself was not reverse-engineered
  here and is not needed for our renderer.
- Star counts and licences are a snapshot of 1 October 2026 and drift.
- The lab's techniques are demonstrated on synthetic shapes. Applying them to a real film still
  requires per-shot art direction — the curves are the grammar, not the sentence.
