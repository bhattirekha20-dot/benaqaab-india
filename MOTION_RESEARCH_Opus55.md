# HOW THE "OPUS 5.5 MOTION GRAPHICS" VIDEOS ARE ACTUALLY MADE
### Research extract + every prompt worth having + what we change in our pipeline

---

# 0. THE HEADLINE FINDING

**They are not AI-video. They are rendered from code — every single frame.**

> "Claude Opus 5.5 generates motion design and visual scenes entirely in code… no
> external assets." — daily.dev, 28 Sep 2026

> "No stock footage, no image or video generators: every frame is rendered from code."
> — creator of the 3-minute AI-history film (~7,400 lines)

> "**It is not a text-to-video model like Veo or Kling.** The model plans the scenes,
> writes the animation, coordinates voice or music tools, checks frames and renders
> through a browser, Remotion or FFmpeg." — MagicCreator

**Why this matters enormously for us:** our pipeline is *already* this. Python draws
every frame as a pure function of time, ffmpeg encodes it. We are on the same
architecture as the viral videos. We are not missing a magic tool — **we are missing
specific motion-design technique.** That is learnable and I have extracted it below.

Scale of the evidence: `zhuyansen/awesome-opus-5.5-video` catalogues **986 works,
259 with prompts**, all 5,000+ views. `TripoGrowthLab/awesome-opus-5-5-prompts` has
source-linked prompts. I pulled the best ones verbatim.

---

# 1. THE PROMPTS (verbatim)

## 1.1 The one that went viral — 1.5 million views
```
make a dynamic 15-second motion graphics video that shows what an incredible motion
designer you are, like it's your showreel for a résumé. go all out.
```
That's it. The whole prompt. Worth knowing because it proves the *model* supplies the
taste when you give it permission — but note Charlie Hills' correction below.

## 1.2 The honest counterpoint — from someone who made 16 of them
> "1. Pick one motion, like a chart that morphs. 2. Show Claude a reference and **name
> every state**. 3. Ask for HTML and SVG, then fix it round by round.
> **But it wasn't one prompt.** I needed the exact states, a good reference and a few
> rounds of fixes to get there." — Charlie Hills

**This is the real workflow.** The one-liner produces a lucky demo. Production work is
named states + reference + iteration.

## 1.3 The showreel prompt, expanded (better than the one-liner)
```
Create a bold, dynamic 15-second motion graphics showreel that feels like the ultimate
portfolio piece of an exceptionally talented motion designer. Showcase a wide range of
advanced techniques: kinetic typography, smooth transitions, 2D and 3D animation,
abstract geometry, fluid simulations, particles, distortion, creative masking,
compositing, lighting, depth, and seamless camera movement. Keep the pacing fast,
confident, and visually surprising, with every shot transitioning naturally into the
next. Make it feel meticulously art-directed rather than like a random collection of
effects. Push the creativity, polish, timing, and visual impact as far as possible.
```

## 1.4 🏆 THE SPOTIFY PROMPT — the most instructive artefact I found
Abridged to its *transferable rules* (full text is in the TripoGrowthLab repo). This is
what a professional motion brief looks like:

**Output contract**
```
An 18-second MP4 at 1920x1080 and true 60 fps, with music and subtle sound effects.
Complete editable source.
Build, render, inspect, and refine the animation before delivering it.
Do not stop at a storyboard, still images, or an implementation plan.
```

**Design system** — exact hex, one font family, "consistent icon strokes and restrained
shadows", "compact and centered, with substantial negative space", "text should feel
like product advertising, not oversized presentation headings".

**Timeline written to the tenth of a second** — `0.0–0.6s`, `0.6–1.5s`, `1.5–2.4s` …
every beat specified.

**Motion rules (copy these):**
```
Most visual ideas last approximately one second, but transitions remain smooth.
Use continuous acceleration and deceleration.
Favor critically damped springs or carefully tuned smooth easing.
No repeated bouncing or large elastic overshoots.
Preserve the hero artwork's identity and position relationships across scenes.
Use match-position transitions, coordinated scaling, masked reveals, and perspective.
Outgoing titles must disappear before incoming titles occupy the same space.
Avoid overlapping text, sudden camera resets, long blank intervals, and arbitrary
full-frame crossfades.
No particles, shockwave rings, lens flares, camera shake, or unrelated stock footage.
```

**Determinism (this is the engineering core):**
```
Build a deterministic animation driven by absolute time through an async seek(t).
Every transform, opacity, mask and UI state must be reproducible when seeking frames
in any order. Do not depend on live timers, accumulated physics, or CSS transition
state during export.
```

**Render + QA:**
```
Render true 60 fps with spatial antialiasing.
Use 3-5 temporal subframe samples per output frame for restrained motion blur.
Keep stationary text and artwork sharp.
Inspect contact sheets and moving playback.
Verify evenly spaced frame timestamps and the full duration.
Fix visual defects before delivering.
```

## 1.5 🏆 THE MAKERMAP PROMPT — the tightest technique list anywhere
```
One HTML file. One canvas. One draw(t) function.
No CSS transitions. No timers. No state carried between frames.

One shape, never cut.
Every state is the same element changing size, radius and color while content swaps.
A cursor drives the sequence with real clicks, typing and one drag.
Real UI. Real data. No placeholders.

120 BPM grid. Something happens on every beat.

Closed-form springs everywhere with only a tiny overshoot.
If a value changes target multiple times, sum one spring per change.
Content enters after its container starts morphing and leaves before the next morph
so text never overlaps.
Use a short blur on transitions.
Never fade black directly into the accent color. Move an accent element between
states instead.
Make tab indicators stretch by putting each edge on a different spring.
Zoom the camera so every state fills the frame.
Make the last frame equal the first so the whole thing loops.

First render one frame per beat as a contact sheet. Fix anything cramped or broken.
Then render every frame in headless Chrome at 60fps, averaging 6 subframes for
motion blur. Pipe into ffmpeg: H.264 + yuv420p.
```

## 1.6 Naming your easing curves (from the muz.li title-sequence build)
Opus named its curves at the top of the file and used only those four:
```
rail   cubic-bezier(0.16, 1, 0.30, 1)   arrivals. Leaves at full speed, brakes hard.
shunt  cubic-bezier(0.80, 0, 0.12, 1)   lane changes. Heavy start, fast middle, locked stop.
crank  cubic-bezier(0.72, 0, 0.18, 1)   grid rotation. Slow wind-up, long settle.
cut    none                             colour. Changes on the frame of the beat.
```
**A named, limited curve vocabulary is what makes motion read as designed rather than
assembled.**

## 1.7 The design-rules block worth pasting into any brief
```
- Display: [family]. Text: [family]. Scale 1.25.
- Motion: one orchestrated moment per scene. Entrances expo.out, 600ms max.
  Anything draggable uses a velocity-aware spring and can be interrupted.
- Never: fade-up on every section, ALL-CAPS eyebrows, identical card grids.
- Always: a 390px layout, visible focus, screenshot before calling anything done.
```

## 1.8 Shorts-specific hard numbers (from the Remotion prompt libraries)
```
SAFE ZONE: 150px from top, 170px from bottom, 60px side margins minimum.
MINIMUM FONT SIZES: Headlines 56px+, body/subtitles 36px+, labels 28px absolute floor.
Every element enters with a spring - no linear motion.
Stagger related items by 8-12 frames.
Diagrams draw themselves (stroke-dashoffset).
Key numbers count up, with tabular figures.
```

## 1.9 The reconstruction prompt — how to copy any animation you like
Feed a reference video to a model that can watch video, ask for these 5 layers, then
hand the output to the builder:
```
1. VISUAL SPECS - exact hex codes, typography, weights, tabular figures, layout, assets
2. VIDEO CONFIG - dimensions, fps, duration in frames
3. DATA & PROPS - what is displayed, what should be a variable
4. ANIMATION LOGIC - frame-by-frame: [0-10] initial, [10-30] entry, [30-end] secondary.
   For each: spring (give stiffness/damping) or eased interpolate (give in/out ranges)
5. THE REPLICATION PROMPT - one high-density prompt to paste into the builder
```

---

# 2. GAP ANALYSIS — us vs them

| Technique | Them | Us today | Impact |
|---|---|---|---|
| Frame = pure function of t | ✅ | ✅ already | — |
| No timers / reproducible seek | ✅ | ✅ already | — |
| **Motion blur (3–6 subframes)** | ✅ | ❌ **none** | 🔴 **biggest gap** |
| **Closed-form springs** | ✅ | ❌ ease-out only | 🔴 high |
| **Named, limited curve set** | ✅ 4 curves | ❌ ad-hoc | 🔴 high |
| **One element morphing across scenes** | ✅ | ❌ independent cards | 🔴 high |
| Beat grid (120 BPM) | ✅ | ❌ VO-timed only | 🟡 medium |
| Text handoff rule | ✅ explicit | ⚠️ caused 2 bugs already | 🟡 medium |
| Last frame == first | ✅ | ⚠️ soft fade | 🟡 medium |
| Contact sheet **per beat** | ✅ | ⚠️ 12 random frames | 🟡 medium |
| 60 fps | ✅ | ❌ 30 | 🟢 low for Shorts |
| Charts that draw themselves | ✅ | ✅ added last episode | — |

**Blunt read: our architecture is right and our motion vocabulary is poor.** We use
`out_back` and `out_expo` everywhere, no motion blur, and every scene is an island.
That is exactly the difference between "assembled" and "art-directed".

---

# 3. WHAT I WILL IMPLEMENT (concrete, in our Python pipeline)

### 3.1 Motion blur — the single biggest win
Render each output frame as the **average of 4 sub-samples** across the frame's time
slice, then composite:
```python
def frame_mb(t, dt=1/FPS, samples=4):
    acc = None
    for k in range(samples):
        f = np.asarray(render(t + dt*(k/samples - 0.5)), dtype=np.float32)
        acc = f if acc is None else acc + f
    return Image.fromarray((acc/samples).astype(np.uint8))
```
Cost: 4x render time (~35 min for a 34s Short). **Mitigation: only blur frames where
something is moving fast** — detect via scene-local velocity and fall back to 1 sample
when static, per the brief's "keep stationary text sharp".

### 3.2 A real spring, closed form
```python
def spring(t, d=0.68, w=13.0):
    """Critically-damped-ish. Tiny overshoot, settles ~0.45s. No bounce."""
    if t <= 0: return 0.0
    wd = w*math.sqrt(max(1e-6, 1-d*d))
    return 1 - math.exp(-d*w*t)*(math.cos(wd*t) + (d*w/wd)*math.sin(wd*t))
```

### 3.3 Four named curves, and nothing else
```
ARRIVE  spring(d=0.68, w=13)   everything that enters
SETTLE  cubic-bezier(.16,1,.30,1)   position corrections, brakes hard
SWEEP   cubic-bezier(.80,0,.12,1)   masks and wipes
CUT     none                        colour changes, on the beat
```

### 3.4 One recurring element per film
A single shape that **persists and morphs** across all scenes instead of new cards each
time — e.g. for the market video, one rounded rectangle that is the chart frame, then
the stat card, then the CTA pill. "One shape, never cut."

### 3.5 Text handoff rule, enforced in code
Outgoing text must reach opacity 0 **before** incoming text starts. This is not taste —
it already caused two real bugs (ep-4 dark-red-on-dark, ep-5 heading collision).

### 3.6 Beat grid
Lay a 120 BPM grid (0.5s) under the VO and snap every entrance to the nearest beat.
Cheap to add, and it is what makes cuts feel deliberate.

### 3.7 Contact sheet per beat, not random
One frame per beat, reviewed before render. Catches cramped states early.

---

# 4. THE PROMPT I'D NOW USE FOR OUR OWN VIDEOS

```
Build a finished, rendered vertical video. Not a storyboard.

OUTPUT: 1080x1920 MP4, 30fps, H.264 + AAC, -14 LUFS, 32-38 seconds.
Every frame is a pure function of absolute time t. No timers, no accumulated state.
Seeking to any t must reproduce the exact frame.

SAFE ZONE: 150px top, 170px bottom, 60px sides.
TYPE FLOOR: headlines 56px+, body 36px+, nothing under 28px.

MOTION VOCABULARY - use these four and nothing else:
  ARRIVE  closed-form spring, damping .68, omega 13. Tiny overshoot, no bounce.
  SETTLE  cubic-bezier(.16,1,.30,1)
  SWEEP   cubic-bezier(.80,0,.12,1)
  CUT     instant, only on a beat
Entrances 600ms max. Stagger related items 8-12 frames.

CONTINUITY: one recurring shape persists across every scene, changing size, radius
and colour while the content inside it swaps. Never cut it. The film must read as one
object evolving, not a slideshow of cards.

TIMING: 120 BPM grid. Something happens on every beat. Most ideas last ~1 second.

TEXT: outgoing text reaches opacity 0 before incoming text occupies that space.
Never two texts in the same region at once.

CONTRAST: any text over a photo gets a plate whose strength is computed from the
luminance AND the busyness of the pixels behind it.

RENDER: average 4 temporal subframes per output frame for motion blur, but only where
something is moving; keep stationary text sharp.

LOOP: the last frame must equal the first.

BANNED: particles, shockwave rings, lens flares, camera shake, fade-up on every
element, arbitrary full-frame crossfades, any HUD or frame counter.

QA BEFORE DELIVERY: render one frame per beat as a contact sheet. Fix anything cramped
or overlapping. Then render in full, verify duration, loudness and that frame 0 reads
as a still.
```

---

# 5. HONEST LIMITS

- **I cannot watch video.** Everything above is from written prompts, creator
  descriptions and technical write-ups — not from viewing the clips. If you want a
  specific look copied, screenshot it and I can read the design off stills.
- **I cannot choose which model runs me.** That is a platform setting.
- **Motion blur costs ~4x render time.** A 34s Short goes from ~9 min to ~30 min.
  Worth it, but you should know before I start.
- **Remotion (what many of these use) needs Node + headless Chromium**, which is heavy
  for this sandbox. Our Pillow pipeline reaches the same place; it just needs the
  techniques above. Not a blocker.


## 2026-10-01 — Cinematic 3D documentary quality audit and reference research
Full findings: `knowledge/3d_documentary_research/RESEARCH_AND_REBUILD_PLAN.md`. User rejected the earlier 3D HTML's visual quality. Strongest recommended correction is integrated scene/shot direction, not additional cards, glow or a compulsory theme. Build proper assets, camera paths, light/depth coherence and world-space effects; time shots to narration rather than equal subdivisions. Lusion's published case study supports hybrid precomputed + real-time techniques. Public tutorial storyboard review demonstrates that even simplified assets can work inside a coherent staged scene. Recommend a 25-second user-reviewable proof before scaling; this is not an already-approved requirement.
References: https://www.awwwards.com/case-study-for-lusion-by-lusion-winner-of-site-of-the-month-may.html ; https://www.webgpu.com/showcase/gemini-webgl-car-demo-lusion/ ; https://www.youtube.com/watch?v=Jmcg5ZSU8a8 ; https://tympanus.net/codrops/2023/02/14/animate-a-camera-fly-through-on-scroll-using-theatre-js-and-react-three-fiber/ .
