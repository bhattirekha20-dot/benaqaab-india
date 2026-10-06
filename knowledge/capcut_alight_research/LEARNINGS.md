# CapCut + Alight Motion — Saved Knowledge Base

**Location:** `knowledge/capcut_alight_research/` · **Compiled:** 1 October 2026
**Companion skill:** `/home/user/SKILLS_CAPCUT_ALIGHT_MOTION.md`
**Runnable proof:** `viz/motion_library.js` · **Tools:** `tools/capcut_draft.py`, `tools/alight_project.py`

---

## 0. Why this file exists, and the one boundary

The user asked to use the **official CapCut and Alight Motion** effects and transitions to make
videos. Doing that honestly needs two separate facts, kept apart:

1. **What the official catalogues contain.** This is now known precisely — 3,424 CapCut items with
   their real ids and default durations, and Alight Motion's 196 documented effects plus its project
   XML format. Verified from source, saved here.
2. **Who renders the pixels.** CapCut and Alight Motion are proprietary mobile/desktop apps. They
   cannot be installed or run in this Linux workspace. A file we write *for* them is a project file
   **you** open in the app; an effect's look is produced by the app's own (downloaded, often VIP)
   resources, not by us.

So there are two honest paths, and both are implemented:

| Path | What happens | Where |
|---|---|---|
| **A — real app** | We generate a CapCut draft folder or an Alight Motion `.xml`; you open it in the app, tune, and export | `tools/capcut_draft.py`, `tools/alight_project.py` |
| **B — here, natively** | We reimplement the transitions in our own canvas engine using the official names/durations, and render the video ourselves | `viz/motion_library.js` → `demos/Transition_Demo_CapCut_Alight_1080x1920.mp4` |

Path B is what makes "use the official transitions" actually deliverable in this workspace. The
implementations are **faithful native reinterpretations**, not bit-exact copies of the apps'
proprietary shaders, and they are labelled that way on screen.

---

## 1. CapCut — verified ecosystem

| Repo | Stars | Licence | What it is |
|---|---|---|---|
| `GuanYixuan/pyJianYingDraft` | 4,470 | Apache-2.0 | Python draft generator for JianYing (CapCut CN); the reference implementation |
| `GuanYixuan/pyCapCut` | 691 | (no licence file) | The CapCut-international port; **source of the metadata tables used here** |
| `aoguai/pyJianYingDraft` | 17 | Apache-2.0 | Fork adding high-version support, encrypted drafts, cloud music, local fonts |
| `ShinnyYang/pyJianYingDraft` | 0 | Apache-2.0 | Fork; documents that new JianYing versions encrypt `draft_content.json` and need a `fallback_loader` |
| `sun-guannan/CapCutAPI` | 2,265 | Apache-2.0 | HTTP API around draft generation (sibling project, not used directly) |

Checked live through the GitHub API on 1 October 2026; raw data in `REPO_AUDIT.json`, READMEs in
`source_snapshots/`.

### 1.1 The draft file

A CapCut project is a folder containing `draft_content.json` (+ `draft_meta_info.json` and a
timeline/root registry). Inside: `materials` (videos/audios/photos/texts/transitions/…), `tracks`
with `segments`, a `keyframes` block, `canvas_config` (width/height/ratio), `duration` in
microseconds, `fps`, and a `config` block. Times are **microseconds** throughout.

Segment fields that matter in practice: `target_timerange {start,duration}` (where it sits on the
track), `source_timerange {start,duration}` (what part of the media it uses), `speed`, `volume`,
`clip {alpha, flip, rotation, scale, transform, visible}`, `transition`, `animations`,
`extra_material_refs`, `render_index`, `visible`.

A **transition belongs to the outgoing clip** — it is written on the segment *before* the cut, which
is exactly how the app models it.

### 1.2 The official catalogue we extracted

Parsed from pyCapCut's metadata tables (1,130 transitions + 8 other libraries = **3,424 items**, each
with an `effect_id`, `resource_id`, a `is_vip` flag and, for animations/transitions, a default
duration):

| Library | Items | Free | VIP |
|---|---|---|---|
| Transitions | 1,130 | 147 | 983 |
| Video intros (入场) | 250 | 43 | 207 |
| Video outros (出场) | 217 | 22 | 195 |
| Group animations | 107 | 71 | 36 |
| Text intros | 182 | 62 | 120 |
| Scene effects (画面特效) | 1,582 | 314 | 1,268 |
| Character effects | 251 | 120 | 131 |
| Filters | 454 | 112 | 342 |

Saved as `CATALOG_*.json` here and as `/home/user/tools/data/capcut_*.json`.

**Default transition durations** (the actual CapCut values — most transitions are 0.5 s or 2.0 s,
with 1.0 s the next most common): 0.2 (×1), 0.3 (×1), 0.4 (×4), 0.5 (×161), 0.6 (×20), 0.7 (×21),
0.8 (×41), 0.9 (×12), 1.0 (×168), 1.1 (×8), 1.2 (×14), 1.3 (×6), 1.33 (×14), 1.5 (×23), 1.67 (×14),
1.83 (×16), 2.0 (×475) … up to 4.0 s.

**The VIP reality must be stated honestly:** 87 % of transitions are VIP. A generated draft that
uses one still requires the subscription *inside the app*. Free-tier staples that are safe bets:
White Flash (0.40 s), Fold Over (1.00 s), Cutout Flip (0.80 s), and the plain 叠化 dissolve (0.50 s).

### 1.3 What `tools/capcut_draft.py` writes

A draft folder with `draft_content.json`, `draft_meta_info.json`, and optional local-media copying.
Materials, one video track, segments with transitions and animations, an audio track, and the whole
`config`/`keyframes` scaffolding the app expects. Tested: generated a 2-clip, 12 s draft using the
catalogue's real White Flash (0.40 s) and Fold Over (1.00 s) entries, then structurally validated it
(required top-level keys, track/segment shape, transition `effect_id` present).

**Not claimed:** that any CapCut build will list the draft without its registry entry. The draft
root registry is version-specific; if the app does not show it, use the app's import-draft feature or
copy the folder into CapCut's draft root. This was not tested against a running app (there is none
here).

---

## 2. Alight Motion — verified documentation

`kuchingneko28/alight-motion-docs` publishes community documentation generated from the **decompiled
APK**: 697 effect asset XMLs, 20 shape templates, the strings table, and a full write-up of the
project/preset format. We saved `docs/authoring.md`, `docs/guide.md` and the README.

### 2.1 Scene document

The project file is XML. Scene attributes: `title`, `width`, `height`, `exportWidth`,
`exportHeight`, `bgcolor`, `totalTime` (ms), `fps`, `modifiedTime`, `amver`, `ffver`, `am`
(version string), `amplatform`. Then, in order: optional `<media>` declarations, then elements with
**unique ascending ids**.

Common element attributes: `id`, `label`, `startTime`, `endTime`, `fillType`, `mediaFillMode`, and
`s=".template"` for shape templates. Each element carries `<transform>` (location/scale/rotation/
opacity/anchor), then type-specific content, then `<effect>` blocks, then keyframed `<property>`
blocks.

### 2.2 Effects and properties

An effect is `<effect id="com.alightcreative.effects.box" locallyApplied="true">` with `<property>`
children — params are typed: `float`, `int`, `color` (#AARRGGBB), `vec2/3/4`, `quat`, `bool`,
`uri`, `string`. A property equal to its default is **omitted entirely** (absence means default);
a keyed property writes `<kf t="0.5" v="1.0" e="cubicBezier 0.48 0.0 1.0 1.0"/>` instead of a
`value`. Effect `id`s are canonical and do **not** always match the asset file name
(`com.alightcreative.effects.box` lives in `s3d-box.xml`).

### 2.3 The adjustment-layer grade (the most useful idea in the whole document)

Alight Motion builds grading as a stack of **adjustment layers**. The trick is that the first effect
on such a layer is **Copy Background** (`com.alightcreative.effects.lift`, `fill=0`), which computes
`mix(comp * texColor.a, texColor, fill)` — with `fill=0` the layer's texture alpha multiplies the
composite beneath it, so the layer becomes a **pass over the whole image** and every later effect
grades that result.

Documented consequences:
- The plate must cover the frame: `.rect` is a 100×100 template, so **scale = canvas / 100**
  (1080 → `10.8`).
- Grading layers go **above** the content and share its `startTime`/`endTime`.
- A full orange-and-teal grade is four passes: duotone (`lift`, `colortune2`, `colorbalance`,
  `satvib`), exposure (`lift`, `exposure`, `brightcont2`), glow (`lift`, `gaussianblur`,
  `blending="screen"`), finishing (`lift`, `sharpen`, `vignette`, `noise3`).
- Bloom = blurred copy of the composite screened back, with a radial gradient's alpha fading the
  sample.

This is the same grade order we already use in our own pipeline — independent confirmation from a
different tool's documentation.

### 2.4 What `tools/alight_project.py` writes

A scene builder: shapes, text, media, seeds/effects, keyframes with cubic-bezier easing, gradients,
strokes, adjustment layers and glow passes, plus a **validator** that checks the documented import
rules (scene attributes present, ids unique and ascending, every element has a `<transform>`, text
has `<content>`, effect ids canonical with `locallyApplied`, every property has either a value or
keyframes, media declared before elements). Tested: emitted a 4-element 6 s 1080×1920 scene, and the
validator returned `problems: []`.

**Not claimed:** that a specific Alight Motion version imports it. The documented format is from a
decompiled app; effect availability and version attributes (`amver`, `ffver`, `am`) depend on the
build you own.

---

## 3. The transition engine we built (Path B)

`viz/motion_library.js` — 24 transitions, native Canvas 2D, no libraries. Each cell is labelled
with the **official CapCut name** and its **verified default duration**:

| # | Name | Official duration | Free/VIP | Implementation |
|---|---|---|---|---|
| 1 | Dissolve · 叠化 | 0.50 s | free | cross-dissolve + 1.05→1.0 settle |
| 2 | White Flash | 0.40 s | free | flash out → cut → flash in |
| 3 | Cutout Flip | 0.80 s | free | double doors: A opens, doors close on B |
| 4 | Fold Over | 1.00 s | free | folding panel wipe with edge shading |
| 5 | Push Away 2 | 1.00 s | VIP | opposing slides with a 12 % zoom-out |
| 6 | Corner Slide | 1.00 s | VIP | diagonal corner reveal + gradient seam |
| 7 | Swipe Left | 1.30 s | VIP | out-quint push with a cast shadow |
| 8 | Shrink | 1.10 s | VIP | A shrinks and rotates away |
| 9 | Drop & Expand | 1.00 s | VIP | soft spring drop (stiffness 36/damping 7.2) + scale-in |
| 10 | Snap Zoom | 0.90 s | VIP | blur-zoom out (in-cubic) then snap focus in (out-expo) |
| 11 | Zoom to Change | 0.80 s | VIP | opposing zooms cross with blur |
| 12 | Jerky Camera | 0.90 s | VIP | 6 discrete seeded camera jerks + exposure stutter |
| 13 | Center Rotate | 1.00 s | VIP | counter-rotating layers |
| 14 | Cube Rotate | 1.00 s | VIP | real front/side faces with edge highlight |
| 15 | Flip Page | 0.70 s | VIP | page turns; the back of the page carries B |
| 16 | Paper Flip | 1.00 s | VIP | vertical card flip with lit paper edges |
| 17 | Kaleidoscope | 1.45 s | VIP | 8 mirrored wedges opening |
| 18 | Whirl | 1.50 s | VIP | counter-rotating spins with motion blur |
| 19 | Rainbow Twist | 1.00 s | VIP | counter-rotation + additive hue band |
| 20 | Film Burn | 0.70 s | VIP | additive burn streak sweeping the frame |
| 21 | Light Leaks | 1.00 s | VIP | 4 angled streaks over a dissolve |
| 22 | Neon | 0.60 s | VIP | hard-edge reveal with neon bars |
| 23 | Signal Glitch 2 | 0.67 s | VIP | sliced displacement + RGB split that settles clean |
| 24 | Wide Ripple | 2.00 s | VIP | expanding circular wipe + ripple rings |

The 60 English-named official transitions are all in `CATALOG_TRANSITIONS.json` (the other 1,070
entries are Chinese-named); 24 were implemented because they cover the distinct motion families.

### 3.1 How it is verified

- **Determinism:** 14 timestamps captured, then re-captured in shuffled order — all SHA-256 digests
  identical, `page_errors: []`.
- **Per-transition phase audit:** a QA hook (`window.__TEST_PHASE__`) renders any transition at an
  exact normalised phase; all 24 were sampled at u = 0.12 / 0.35 / 0.50 / 0.70 / 0.90 and measured.
  Every one changes brightness across its window — none is static or dead.
- **Visual inspection:** contact sheets at 5 phases × 24 transitions.

### 3.2 Bugs this testing caught (all fixed)

1. **Page 2 rendered black.** `cell()` derived its grid position from the *global* index, so page 2's
   twelve cells drew at y ≈ 3000–4300 px — outside a 1920 px canvas.
2. **`captureFrame()` ignored the current time** when called without an argument and silently seeked
   to 0 — which is why the first phase audit reported every transition as "static".
3. **Render crash at t < 0.** The house renderer samples inside a shutter window, so `t - Δ/2` can
   be negative; the page index went to −1 and the frame array read `undefined`. Time is now clamped
   before any index maths.
4. **Rainbow Twist produced a black frame.** A `destination-in` mask filled the whole canvas and
   erased the composite; rebuilt as a transparent-edged additive band.
5. **Flip Page returned to A** past the halfway point (a page's back should carry the next shot);
   and **Signal Glitch 2 stayed shredded** instead of settling on B. Both fixed and re-measured.
6. **Cutout Flip / Cube Rotate / Paper Flip** were "mystery dissolves" with no readable geometry;
   rewritten as a door fold, a front/side cube and a card flip.

---

## 4. Honest limits

- CapCut and Alight Motion were **never run**. No draft was opened in CapCut, no scene imported into
  Alight Motion, no app export was produced.
- The catalogues are a faithful parse of open-source metadata tables that mirror the apps' own ids;
  they are a 2026-10-01 snapshot and CapCut adds effects continuously.
- Effect **looks** are proprietary (shaders + downloadable resources). Our engine reproduces the
  *motion grammar* of each transition, not the app's exact pixels.
- The VIP/paid split is a property of the app's store, not a limitation we can remove.
- 87 % of CapCut transitions and most scene effects are VIP; the free ones are flagged in the saved
  catalogues so a draft can be built that a free account can actually use.
