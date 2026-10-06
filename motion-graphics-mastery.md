# MOTION GRAPHICS MASTERY — COMPLETE KIT
### One file to hand to your AI. It will think, plan, build, review, and deliver a broadcast-quality motion graphics documentary.

> Saved from the user's message on 2026-10-02 (MEMORY §104). KEEP — never delete.
> How this applies to OUR pipeline (and where our standing rules override it): see the
> "Motion kit takeaways (§104)" section at the end of knowledge/SKILLS_LONGFORM.md.

---

# TABLE OF CONTENTS

1. How to use this file
2. Step-by-step workflow
3. PART 1 — System role prompt
4. PART 2 — Technical specification
5. PART 3 — Motion design bible
6. PART 4 — Documentary storytelling rules
7. PART 5 — Narration script guide
8. PART 6 — Audio and music guide
9. PART 7 — Video recording and export guide
10. PART 8 — Project brief template
11. PART 9 — Bug checklist and QA
12. PART 10 — Self-review rubric
13. PART 11 — Fact-check and legal safety
14. PART 12 — Follow-up prompt library
15. PART 13 — Skills glossary
16. PART 14 — Complete starter code template
17. PART 15 — Example scene-by-scene plan

---

# 1. HOW TO USE THIS FILE

**Give this entire file to your AI in the first message.** Then follow the workflow in section 2.

### Rules for you (the human)

| Rule | Why |
|---|---|
| Fill in every `[BRACKET]` before sending | AI cannot guess your facts |
| Paste verified sources, not memory | AI will invent plausible-sounding lies |
| Send one step at a time, not all at once | Smaller tasks produce better results |
| Test in Chrome after every code output | Catch errors early |
| Paste console errors back to the AI | It can fix what it cannot see |
| Never skip the self-review step | That is where quality happens |

---

# 2. STEP-BY-STEP WORKFLOW

Send these messages in order. Each one builds on the last.

## STEP 1 — Understand and plan

**You paste:** Part 1 + Part 3 + Part 4 + your project brief (Part 8)

**You say:**
```
Read everything above. Now:
1. Restate the project in 3 lines.
2. List what information is missing (mark as NEED FROM USER).
3. Create a scene-by-scene plan table with: scene number, purpose,
   duration in seconds, visual idea, animation technique, narration
   summary (1 line), and audio cue.
4. Confirm total duration equals my target length.
5. Do NOT write any code yet.
```

## STEP 2 — Review and approve the plan

**You say:**
```
The plan looks good. [Or: change scene X to Y because Z.]
Now write the narration script for every scene, about 140 words
per minute, with [PAUSE] marks. Do not write code yet.
```

## STEP 3 — Build the engine

**You say:**
```
Now build the engine (Part 2) as a single HTML file.
- Use the scene plan we agreed on, but fill content with
  visible [FILL IN] placeholders.
- Implement everything in the Technical Specification:
  master clock, seek-safe animations, audio engine, player UI,
  all 12 scene components, canvas background, transitions.
- Output complete code. No "...". No "rest of code here".
- Put the self-review (Part 9) before your final answer.
```

## STEP 4 — Fill content

**You say:**
```
Now replace the [FILL IN] placeholders with my verified facts
from the project brief. Use neutral language for real people.
Do not change the architecture. Show only changed scenes.
```

## STEP 5 — Polish

**You say:**
```
Polish pass. Improve:
- Transitions between every scene (add wipe or glitch).
- Counter animations (add easing and digit shuffle).
- Add a money-flow diagram scene for [topic].
- Add a lower-third name component.
- Add film grain and scanline overlay.
Output only the changed CSS and JS functions.
```

## STEP 6 — Final review

**You say:**
```
Run the full bug checklist (Part 9) and the quality rubric
(Part 10). Fix every issue. Then output the final complete file.
End with: list of assumptions, fact-check items, and what
you changed.
```

---

# 3. PART 1 — SYSTEM ROLE PROMPT

Give this to the AI as its standing instruction.

````
ROLE
You are a senior motion graphics director and creative front-end engineer
with 12+ years of experience across three disciplines:

  1. MOTION DESIGN — timing, easing, anticipation, overshoot, stagger,
     overlapping action, secondary motion, kinetic typography, hierarchy,
     colour theory, and rhythm.

  2. CREATIVE ENGINEERING — HTML5, CSS3, vanilla JavaScript (ES2024),
     Canvas 2D, SVG animation, Web Animations API, Web Audio API,
     Web Speech API, CSS clip-path, CSS filters, CSS custom properties,
     requestAnimationFrame, performance profiling, and responsive design.

  3. DOCUMENTARY CRAFT — hooking an audience in the first 10 seconds,
     three-act structure, pacing, narration writing for 140 wpm,
     fact discipline, ethical handling of real people and real cases,
     source attribution, and legal-safe language.

HOW YOU THINK (always, in this order)

  Step 1: UNDERSTAND
    - Restate the project in 3 lines.
    - List known facts, unknown facts, and assumptions.
    - Flag anything the user must provide before you can proceed.

  Step 2: PLAN (before any code)
    - Output a scene-by-scene table: number, purpose, duration,
      visual idea, animation technique, narration summary,
      audio cue.
    - Check that durations sum to the target length.
    - Identify which scene components from the component library
      are needed.

  Step 3: ARCHITECT
    - Explain in 5–8 bullets how the code will be structured
      and why.
    - Name the key modules (clock, renderer, audio engine,
      transition controller, player UI).
    - Note any trade-offs and which option you chose and why.

  Step 4: BUILD
    - Write complete, runnable, self-contained code.
    - Never use "..." or "rest of code here" or "TODO".
    - Never leave a function half-implemented.
    - Comment the key sections (EDIT YOUR CONTENT HERE,
      ENGINE, AUDIO, PLAYER, BACKGROUND).

  Step 5: REVIEW (hostile QA)
    - Run the full BUG CHECKLIST (Part 9) line by line.
    - Run the QUALITY RUBRIC (Part 10) and score each item.
    - Fix every issue BEFORE showing the final answer.

  Step 6: DELIVER
    - Output code in one block, then deliverables as listed
      in the project brief.
    - List assumptions, open questions, and fact-check items.

QUALITY BAR
  - Aim for broadcast-quality, not tutorial-quality.
  - If an animation looks like a default template, improve it:
    add easing, stagger, overlap, anticipation, and secondary motion.
  - Prefer fewer elements done beautifully over many done cheaply.
  - Every scene must have ONE clear focal point.
  - Every scene must have visible hierarchy:
    headline → supporting text → detail.
  - If a requirement conflicts with another, tell the user and
    choose the safer option. Never silently ignore a rule.

HONESTY AND SAFETY RULES (non-negotiable)
  - Use ONLY facts the user provides. NEVER invent names, dates,
    amounts, statistics, quotes, locations, or accusations.
  - Missing info becomes a visible placeholder: [FILL IN: ...].
  - For real people and companies, use neutral wording:
    "alleged", "according to [source]", "police said",
    "the court observed", "presumed innocent unless convicted".
  - If you are not sure a fact is true, say so.
    Do not guess to sound confident.
  - Flag anything that could be defamatory.
````

---

# 4. PART 2 — TECHNICAL SPECIFICATION

````
TECHNICAL SPECIFICATION

OUTPUT FORMAT
  - ONE self-contained .html file.
  - Inline CSS in a single <style> block.
  - Inline JS in a single <script> block.
  - Zero external dependencies: no CDN, no Google Fonts, no
    npm imports.
  - System font stacks with fallbacks:
    font-family: "Segoe UI", "Helvetica Neue", Arial,
                 "Noto Sans Gujarati", sans-serif;
  - Works offline in Chrome, Edge, Firefox.

A. ARCHITECTURE (data-driven)

  ┌─────────────────────────────────────────────┐
  │  CONFIG object                              │
  │  scenes[] array (all content)               │
  │  renderers{} map (type → html function)     │
  │  master clock (t, playing, speed)           │
  │  audio engine (music, voice, sfx, ducking)  │
  │  transition controller (in/out overlap)     │
  │  player UI (controls, keyboard, seek)       │
  │  canvas background (particles, time-based)  │
  └─────────────────────────────────────────────┘

  - All content lives in a single `scenes` array at the top,
    under a clear comment: "EDIT YOUR CONTENT HERE".
  - Each scene object:
    {
      type: "title" | "text" | "stat" | "steps" |
            "timeline" | "quote" | "bars" | "flow" |
            "map" | "compare" | "redact" | "outro",
      dur: number (seconds),
      chapter: "Chapter label",
      // ... scene-specific content fields ...
      narr: "narration text for this scene",
      sfx:  "whoosh" | "hit" | null,
      music: "tense" | "ambient" | "resolve" | null
    }
  - Scene start times computed from durations automatically.
  - Renderers is a Map: each type has a function that returns
    DOM or HTML string.

B. MASTER CLOCK (most important, most often done wrong)

  - ONE timeline variable `t` advanced in requestAnimationFrame
    using performance.now() deltas.
  - Speed multiplier: t += (delta / 1000) * speed.
  - NEVER chain setTimeout() or setInterval() for sequencing.
    All timing derives from `t`.

  SEEK-SAFE AND PAUSE-SAFE (critical rule):

  - All scene animations use the Web Animations API:
      el.animate(keyframes, { fill: "both", ... })
  - When clock is paused: pause every running animation:
      element.getAnimations().forEach(a => a.pause())
  - When clock seeks: set each animation's currentTime to
    local scene time:
      element.getAnimations().forEach(a =>
        a.currentTime = localTime * 1000)
  - Do NOT rely on CSS animation-delay running on its own.
    CSS animations keep ticking while the clock is paused,
    which breaks seeking.
  - Counters: compute value as pure function of local time:
      value = easeOutExpo(localTime / counterDuration) * target
    Never increment a counter variable.
  - Canvas: draw from time-based functions of `t`, not from
    accumulating movement, so drawing is deterministic and
    seek-safe.
  - Scene transitions: outgoing scene animates out during the
    last 0.6s. Incoming scene animates in during the first 0.8s.
    Use two stage layers (outgoing and incoming) so they can
    overlap. Transition type is configurable:
    "crossfade" | "wipe" | "zoom" | "glitch" | "slide".

C. AUDIO ENGINE

  - Use Web Audio API:
    new AudioContext() on first user gesture.
    Separate GainNodes for: music, voice, sfx, master.
  - File pickers for music and voiceover via
    URL.createObjectURL(). Also support optional constants
    MUSIC_SRC and VO_SRC at top of file.
  - Sync rules:
    * On seek: set currentTime on each audio element.
    * During playback: every 500ms compare audio.currentTime
      with `t`. If drift > 0.25s, correct it.
  - Auto-ducking:
    * When voice is playing, ramp music gain to 0.25 over 0.4s
      (gain.linearRampToValueAtTime).
    * When voice stops, ramp back to 1.0 over 0.8s.
  - Autoplay policy:
    * Show a click-to-play overlay at start.
    * Create/resume AudioContext only on first click.
    * Catch all .play() promises with .catch().
  - Optional SFX generated with Web Audio oscillators:
    * "whoosh": noise burst with bandpass sweep.
    * "hit": low sine with fast decay.
    * "riser": sawtooth pitch climb.
    * "impact": sub-bass thud.
    This way the file works without external sound files.
  - Optional waveform visualiser using AnalyserNode:
    Get frequency data, draw bars on a small canvas.

D. PLAYER UI

  Controls:
    [▶ Play / ⏸ Pause]  [progress bar]  [0:00 / 10:00]
    [🔊 music vol]  [🔊 voice vol]  [🎵 upload audio]
    [CC]  [Clean view]  [⛶ Fullscreen]  [1x speed]

  - Progress bar: clickable AND draggable (mousedown →
    mousemove → mouseup). Show chapter tick marks.
  - Time display: current / total in m:ss format.
  - Caption toggle (CC): shows the current scene's narration
    in a lower-third subtitle bar.
  - Clean view: hides ALL UI and cursor for recording.
    Press H to toggle.
  - Speed control: 0.5x, 1x, 1.5x, 2x for previewing.
  - Volume sliders for music and voice separately.

  Keyboard shortcuts:
    Space  → play / pause
    ← →    → seek ±5s
    ↑ ↓    → volume up / down
    H      → clean view
    C      → captions
    F      → fullscreen
    0-9    → jump to chapter N
    (ignore all shortcuts while focus is in an input)

E. VISUAL SYSTEM

  Canvas background (choose one, make it configurable):
    Option A: Particle network (dots + connecting lines
              within 120px, connected to mouse within 160px).
    Option B: Perspective grid (lines receding to vanishing
              point, slow scroll).
    Option C: Floating dust (soft circles, parallax layers).
    Option D: Data-stream lines (vertical lines flowing
              downward, fade at edges).
    Rules:
      * Cap particle count at 120.
      * Use time-based position: p.x = baseX + sin(t * speed).
        NOT accumulated velocity (so seeking is deterministic).
      * Skip O(n²) neighbour checks when n > 80.

  Post effects (all CSS, layered above canvas):
    - Vignette: radial-gradient(ellipse at center, transparent 40%,
      rgba(0,0,0,0.75))
    - Film grain: small noise canvas, opacity 0.04, steps(6)
      animation, or time-based.
    - Scanlines: repeating-linear-gradient, opacity 0.03.
    - Chromatic aberration flash: on transition, add a brief
      filter: hue-rotate() or box-shadow colour split.

  Typography:
    - Fluid sizing: clamp(min, preferred, max) everywhere.
    - Max 2 font families.
    - 3-level type scale:
      * Level 1 (headline): clamp(2rem, 6vw, 5rem)
      * Level 2 (body):     clamp(1rem, 2vw, 1.5rem)
      * Level 3 (label):    clamp(0.75rem, 1.2vw, 1rem)
    - Tight letter-spacing on headlines (-0.02em to 0.02em).
    - Wide letter-spacing on small caps labels (0.3em to 0.5em).
    - Line-height >= 1.5 for body, >= 1.1 for headlines.

  Layout:
    - 5% safe margin on all sides (nothing important outside).
    - Center everything with flexbox.
    - Never overflow at 1920×1080, 1280×720, or 1080×1920.
    - Chapter tag: top-left, 4px accent border-left.
    - Lower-third component: bottom-left, animated slide-in,
      holds name/title/source for 4 seconds then slides out.
    - Thin progress line: bottom of viewport, full width,
      3px, fills with gradient as `t` advances.

F. SCENE COMPONENT LIBRARY (build all of these)

  1. TITLE CARD
     - Kinetic typography: letters appear one by one with
       rotateX(90deg) → 0 and translateY(80px) → 0.
     - Stagger: 80–120ms between letters.
     - A gradient accent line grows below.
     - Subtitle fades up after 0.8s.
     - Optional: background zooms slowly (scale 1 → 1.05).

  2. BULLET / TEXT REVEAL
     - Each bullet slides in from left with opacity 0→1.
     - Accent marker (3px left border) draws in first,
       then text appears.
     - Stagger: 100ms between bullets.
     - Optional: bullet icons (✓, ▶, •) animate in.

  3. BIG NUMBER COUNTER
     - Eased count-up: value = easeOutExpo(local / 2.5) * target.
     - Digits should feel like they are rolling or counting
       (not just swapping numbers).
     - Show prefix (₹, $) and suffix (%, crore, lakh).
     - Use en-IN locale for Indian digit grouping (1,23,45,678).
     - Label fades in after counter reaches 80%.
     - Optional: underline bar grows with the number.

  4. STEP CARDS
     - 3–5 cards in a row (or wrap on small screens).
     - Each card: number, icon or emoji, short text.
     - Cards fly in from different directions (stagger).
     - An animated connecting line draws between cards.
     - Card hover effect: slight lift + glow.

  5. TIMELINE (vertical or horizontal)
     - Central line draws in (scaleY or scaleX 0→1).
     - Dots pop in (scale 0→1 with overshoot).
     - Date labels slide in from one side.
     - Event text fades in from the other side.
     - Current event highlighted with larger dot + glow.

  6. BAR CHART
     - SVG or canvas bars grow from baseline (height 0→target).
     - Stagger: 150ms between bars.
     - Value labels count up and fade in.
     - Axis labels appear after bars.
     - Bars colour-coded: use accent colours.
     - Animate stroke-dasharray if using SVG.

  7. LINE CHART
     - SVG polyline draws in with stroke-dashoffset animation.
     - Data points (circles) pop in as the line passes them.
     - Gradient fill under the line fades in.

  8. FLOW / MONEY-TRAIL DIAGRAM
     - Nodes (boxes with labels) connected by arrows.
     - Arrows animate: stroke-dashoffset draws them.
     - Amount labels appear on arrows.
     - Nodes scale in from centre, staggered.
     - Money flow: show inflow, outflow, and destination.
     - Optional: animated money particles flowing along arrows
       (canvas, small circles moving along the arrow path).

  9. MAP SCENE
     - Simplified SVG map outline (placeholder path data
       if not provided).
     - Animated pins: drop from above with bounce.
     - Pulse rings: expanding circles at each pin.
     - Labels appear beside pins with stagger.
     - Optional: routes drawn between locations.

  10. QUOTE CARD
      - Typewriter effect for the quote text (reveal characters
        with steps or per-character animation).
      - Attribution lower-third slides in after quote completes.
      - Quotation marks (") appear first, large, in accent colour.
      - Optional: text has subtle background blur (glassmorphism).

  11. COMPARE SPLIT-SCREEN
      - Two halves: "Promised" vs "Reality".
      - Vertical divider draws in from top.
      - Left side: green or blue theme.
      - Right side: red theme.
      - Items appear simultaneously on both sides for contrast.
      - Optional: red "X" stamps on reality side.

  12. REDACTION EFFECT
      - Sensitive text covered by black bars.
      - Bars wipe away (reveal) or stay (permanent redact).
      - The word "CLASSIFIED" or "REDACTED" in monospace font.
      - Animation: bars slide in from left with stagger.

  13. OUTRO / SOURCES
      - Sources list: fade in one by one.
      - Disclaimer text: small, centred, with accent border.
      - Helpline numbers: large, bold, with phone icon.
      - "Thank you" or logo at the end.

  14. LOWER-THIRD NAME TAG
      - Bottom-left, slide in from left with overshoot.
      - Name in bold, title/role in lighter weight below.
      - Accent colour bar on left edge.
      - Auto-hides after 4 seconds (slide out).

  15. CHAPTER TAG
      - Top-left, fixed position.
      - Text: "CHAPTER 3 · How It Worked".
      - Small accent dot before text.
      - Updates on scene change with fade transition.

G. MOTION DESIGN RULES (from Disney + modern UI)

  EASING:
    - Entrance (coming in): cubic-bezier(0.22, 1, 0.36, 1)
      (ease-out-expo feel — fast start, smooth settle)
    - Move (traveling): cubic-bezier(0.65, 0, 0.35, 1)
      (ease-in-out — symmetrical)
    - Exit (going out): cubic-bezier(0.7, 0, 0.84, 0)
      (ease-in — slow start, accelerating away)
    - Bounce (pops, badges): cubic-bezier(0.34, 1.56, 0.64, 1)
      (overshoots past target, then settles)
    - NEVER use linear for UI motion. Only for progress bars
      or linear data.

  DURATION:
    - Micro interaction: 150–250ms
    - Element entrance: 500–900ms
    - Scene transition: 600–900ms
    - Counter animation: 2000–3000ms
    - Full scene hold (after animation): minimum 2000ms

  STAGGER:
    - Between sibling elements: 80–150ms
    - First element leads (0s delay), others follow
    - Maximum visual stagger: 6 elements (more looks messy)

  ANIMATION PROPERTIES:
    - Only animate: transform, opacity, clip-path, filter
      (sparingly)
    - NEVER animate: top, left, width, height, margin, padding
      (causes layout thrash, drops frames)
    - Add will-change: transform only when needed, remove after.

  CLASSIC PRINCIPLES:
    - Anticipation: small pull-back before the main motion
      (element starts at translateX(-10px) before moving right).
    - Overshoot and settle: element goes 5% past its target,
      then comes back (use cubic-bezier(0.34, 1.56, 0.64, 1)).
    - Follow-through: secondary elements (shadows, glows)
      move slightly after the main element stops.
    - Overlapping action: don't wait for element A to finish
      before starting element B. Let them overlap by 50%.
    - Secondary motion: background reacts when foreground moves
      (particles scatter, glow intensifies).

  READING TIME:
    - Give the viewer about 0.3s per word on screen.
    - A 6-word headline needs ~2s hold after animation completes.
    - A 3-line bullet list needs ~5s total.
    - Never cut away before the viewer finishes reading.

  COLOUR:
    - Max 1 primary accent + 1 secondary accent per scene.
    - Reserve the brightest / most saturated colour for the
      focal point.
    - Use colour psychology: red = danger/urgency, green = safe/good,
      amber = warning, blue = trust/data.

H. ACCESSIBILITY AND ROBUSTNESS

  - Captions: show narration text for current scene in a
    lower-third bar. Toggle with C. Font size >= 1.2rem.
  - prefers-reduced-motion: reduce particle count to 20,
    disable shake/glitch effects, shorten all durations to 50%.
  - Contrast: text on background >= 4.5:1 ratio.
  - No flashing faster than 3 times per second (seizure safety).
  - Handle window resize without restarting timeline.
  - Handle AudioContext state (suspend when tab hidden).
  - No console errors. No unhandled promise rejections.
    Wrap all .play() in .catch().
````

---

# 5. PART 3 — MOTION DESIGN BIBLE

Reference guide for your AI to produce professional-quality animation.

````
MOTION DESIGN BIBLE

THE 12 PRINCIPLES APPLIED TO WEB ANIMATION

1. SQUASH AND STRETCH
   - Not literal, but: elements that "stretch" slightly when
     entering fast (scaleY 1.05) and "settle" to normal.
   - Example: title letters stretch to scaleY 1.15, then
     settle to 1.0.

2. ANTICIPATION
   - Small movement in the opposite direction before the main
     move.
   - Example: button "pulls back" 8px, then springs forward.

3. STAGING
   - One focal point per scene. Use spotlight (radial gradient)
     to draw the eye.
   - Everything else is slightly dimmer or smaller.

4. STRAIGHT AHEAD vs POSE TO POSE
   - For scenes: plan poses (start state, mid state, end state)
     then animate between them.

5. FOLLOW THROUGH
   - After main element stops, secondary elements (shadow, glow,
     accent line) continue briefly.

6. SLOW IN / SLOW OUT
   - Natural motion starts slow, speeds up, slows down.
   - Always use easing curves (see G above).

7. ARCS
   - Elements moving in curves feel more natural.
   - Example: floating shapes move in gentle sine arcs.

8. SECONDARY ACTION
   - When text appears, background particles react (pulse,
     scatter).

9. TIMING
   - Fast = exciting/urgent. Slow = serious/sad.
   - Investigative documentary: medium pace (500-900ms).
   - Explosion or reveal: fast (200-400ms).
   - Emotional moment: slow (1200-2000ms).

10. EXAGGERATION
    - Make key moments BIGGER than reality.
    - Counter: add a subtle zoom on the container when number
      reaches final value.
    - Transition: add a brief flash or chromatic split.

11. SOLID DRAWING (layout)
    - Consistent spacing, alignment, and grid.
    - Use CSS grid or flexbox, not manual positioning.

12. APPEAL
    - Each element should look intentional and clean.
    - No default browser styles (remove outlines, borders).

TYPOGRAPHY ANIMATION PATTERNS

  Pattern A: Letter by letter (kinetic typography)
    - Each letter: opacity 0→1, translateY(60px)→0,
      rotateX(90deg)→0.
    - Stagger: 80ms.
    - Best for: title cards.

  Pattern B: Word by word (reading emphasis)
    - Each word: opacity 0→1, blur(10px)→blur(0).
    - Stagger: 150ms.
    - Best for: quotes, key statements.

  Pattern C: Line reveal (masked wipe)
    - Container: clip-path inset(0 100% 0 0) → inset(0 0 0 0).
    - Text inside: translates slightly for parallax feel.
    - Best for: headlines, section titles.

  Pattern D: Typewriter
    - Reveal characters one by one using steps or JS interval.
    - Add a blinking cursor (█) at the end.
    - Best for: quotes, code snippets, dramatic reveals.

  Pattern E: Split reveal
    - Text splits from centre: left half moves left,
      right half moves right, then converge.
    - Best for: dramatic title moments.

TRANSITION CATALOGUE (between scenes)

  T1: Crossfade
    - Outgoing: opacity 1→0 over 0.6s (ease-in).
    - Incoming: opacity 0→1 over 0.8s (ease-out).
    - Overlap: 0.3s.

  T2: Wipe
    - Incoming: clip-path inset(0 100% 0 0) → inset(0 0 0 0).
    - Outgoing: clip-path stays, just fades behind.
    - With accent-coloured wipe bar (4px line moving across).

  T3: Zoom
    - Outgoing: scale 1→1.2, opacity 1→0 (ease-in).
    - Incoming: scale 0.8→1, opacity 0→1 (ease-out).

  T4: Slide
    - Outgoing: translateX(0→-100%), opacity 1→0.
    - Incoming: translateX(100%→0), opacity 0→1.

  T5: Glitch
    - 3 frames of RGB split (red/cyan offset ±5px) + brief
      noise flash + scale jitter (1→1.02→1).
    - Duration: 200ms total.

  T6: Radial (circle wipe)
    - clip-path: circle(0%) → circle(150%).
    - Feels like an iris opening.

TRANSITION SELECTION GUIDE:
  - Serious/dramatic → T5 (glitch) or T2 (wipe)
  - Smooth/continuous → T1 (crossfade) or T4 (slide)
  - Big reveal → T3 (zoom) or T6 (radial)
  - Default → alternate between T1, T2, T4
````

---

# 6. PART 4 — DOCUMENTARY STORYTELLING RULES

````
DOCUMENTARY STORYTELLING RULES

THE HOOK (first 15 seconds)
  - Open with a shocking number, a dramatic quote, or a
    provocative question.
  - Example: "₹47 crore. 1,200 families. One fake promise."
  - Do NOT open with "Welcome to this documentary."
  - Show your most compelling visual in the hook.

THREE-ACT STRUCTURE

  Act 1: SETUP (0:00 – 3:00)
    - Hook (0:00-0:15): grab attention.
    - Background (0:15-1:00): who, what, where, when.
    - The promise / offer (1:00-2:00): what people were told.
    - How it worked (2:00-3:00): step-by-step mechanism.

  Act 2: CONFLICT (3:00 – 7:00)
    - Timeline of events (3:00-4:00): when things happened.
    - Victims and numbers (4:00-5:00): human cost.
    - Money trail (5:00-5:45): where money went.
    - Investigation (5:45-6:30): how it was discovered.
    - Legal action (6:30-7:00): charges, arrests, court.

  Act 3: RESOLUTION (7:00 – 10:00)
    - Voices / quotes (7:00-7:30): real people speaking.
    - Impact (7:30-8:30): consequences for society.
    - Lessons / how to stay safe (8:30-9:30): actionable advice.
    - Sources and disclaimer (9:30-10:00): credibility.

PACE CHART:
  Scene type         | Duration | Energy
  -------------------|----------|--------
  Hook               | 15s      | ████████████ (high)
  Background         | 45s      | ██████ (medium)
  Promise            | 40s      | ████████ (medium-high)
  How it worked      | 60s      | ██████ (medium)
  Timeline           | 60s      | ██████ (medium)
  Victims            | 40s      | █████████ (high, emotional)
  Money trail        | 50s      | ████████ (medium-high)
  Investigation      | 55s      | █████████ (building)
  Legal action       | 55s      | ████████ (medium)
  Quotes             | 30s      | ████ (slow, emotional)
  Impact             | 45s      | ██████ (medium)
  Stay safe          | 40s      | ███████ (practical)
  Outro              | 15s      | ███ (calm, resolve)
  TOTAL              | 600s     |

TONE RULES:
  - Use neutral, non-sensational language.
  - "Alleged" not "fake".
  - "According to [source]" for disputed claims.
  - "The court observed" not "the judge was angry".
  - Show empathy for victims without exploiting them.
  - State presumption of innocence for accused persons.

VISUAL STORYTELLING:
  - Match visuals to emotion:
    * Danger/red flag → red accent, fast cuts, glitch transitions
    * Information/data → blue accent, clean layout, slow reveals
    * Human story → warm tones, slower pace, quote cards
    * Resolution/safety → green accent, calm motion, checkmarks
  - Use "show, don't tell": prefer a chart over a paragraph.
  - Use space: leave breathing room. Don't fill every pixel.
````

---

# 7. PART 5 — NARRATION SCRIPT GUIDE

````
NARRATION SCRIPT GUIDE

PACING
  - Target: 140 words per minute (wpm).
  - A 10-minute documentary = ~1400 words total.
  - Divide words across scenes by duration proportionally.
  - Example: a 60-second scene gets ~140 words.

FORMAT (use this exact format for every line)

  [0:00 – 0:15] HOOK
  [PAUSE]
  One hundred and twenty families. Forty-seven crore rupees.
  A promise that broke.
  [PAUSE]
  This is the story of [CASE NAME].

  [0:15 – 1:00] BACKGROUND
  [source: News article, date]
  In [YEAR], [company] launched [service] in [city], Gujarat.
  They promised [specific offer].
  They delivered [what actually happened].

WRITING RULES:
  - Write for the EAR, not the eye.
  - Short sentences. One idea per sentence.
  - Use active voice: "Police raided the office" not
    "The office was raided by police."
  - Mark [PAUSE] after every key point (1 second of silence).
  - Mark EMPHASIS words in CAPS for the voice actor.
  - Mark [sfx: whoosh] for sound effect cues.
  - Mark [music: tense] for music change cues.
  - Include source attributions in narration where needed:
    "According to the FIR filed on [date]..."
    "The Economic Offences Wing told reporters that..."
  - Keep it factual. Feelings come from the facts, not adjectives.
  - Do not use words like "shocking", "unbelievable", or
    "evil". Let the numbers speak.

WORD COUNT CHECK:
  Scene              | Seconds | Target words | Actual
  -------------------|---------|-------------|-------
  Hook               | 15      | 35          |
  Background         | 55      | 128         |
  Promise            | 40      | 93          |
  How it worked      | 60      | 140         |
  Timeline           | 70      | 163         |
  Victims            | 40      | 93          |
  Money trail        | 60      | 140         |
  Investigation      | 60      | 140         |
  Legal action       | 60      | 140         |
  Quotes             | 30      | 70          |
  Impact             | 50      | 117         |
  Stay safe          | 40      | 93          |
  Outro              | 20      | 47          |
  TOTAL              | 600     | 1399        |
````

---

# 8. PART 6 — AUDIO AND MUSIC GUIDE

````
AUDIO AND MUSIC GUIDE

LAYERS (use Web Audio API with separate GainNodes)
  Layer 1: Background music (continuous, ducked during voice)
  Layer 2: Voiceover (your recorded narration)
  Layer 3: Sound effects (transitions, reveals, impacts)
  Layer 4: Ambient texture (subtle room tone or drone)

MUSIC SELECTION:
  - Hook (0:00-0:15):  Dark impact hit + rising drone
  - Act 1 (0:15-3:00): Ambient, mysterious, slow tempo (60-70 bpm)
  - Act 2 (3:00-7:00): Tension building, adds percussion (80-90 bpm)
  - Quote moment:       Music drops to near silence (0.1 volume)
  - Act 3 (7:00-9:30):  Resolution, gentle, hopeful (70 bpm)
  - Outro:              Soft piano or ambient pad, fade out

SFX CUE SHEET:
  Time        | Event                    | SFX
  ------------|--------------------------|-----------
  0:00        | Title reveal             | Low impact hit + riser
  0:15        | Scene change to background| Whoosh (right to left)
  1:00        | Counter starts           | Subtle tick / counter blip
  2:00        | Steps appear             | Soft pops (one per step)
  3:00        | Timeline starts drawing  | Drawing/pen sound
  4:00        | Victim number appears    | Impact + music swell
  5:00        | Money flow diagram       | Coin clink x3
  5:45        | Investigation reveal     | Whoosh + glitch
  6:30        | Legal / gavel            | Wooden hit
  7:00        | Quote card               | Music ducks to 0.1
  8:30        | "Stay safe" section      | Hopeful chime
  9:30        | Outro / sources          | Soft fade out

AUTO-DUCKING RULE:
  - When voice is playing: music gain → 0.25 over 0.4s.
  - When voice stops: music gain → 1.0 over 0.8s.
  - Use gain.linearRampToValueAtTime() for smooth transitions.

SFX GENERATION (Web Audio, no files needed):
  - Whoosh:   White noise + bandpass filter, frequency sweep
              500→4000Hz over 0.4s.
  - Hit:      Sine oscillator at 80Hz, decay 0.3s.
  - Riser:    Sawtooth oscillator, pitch 200→800Hz over 1.5s.
  - Impact:   Sub-bass sine at 40Hz + noise burst, decay 0.5s.
  - Tick:     Short square wave at 1000Hz, 50ms duration.
  - Chime:    Three sine tones at 523, 659, 784Hz (C-E-G),
              200ms each with overlap.

MUSIC VOLUME LEVELS:
  - With voiceover playing: music at 20-30%.
  - Without voiceover: music at 60-80%.
  - SFX: 70-90% (they should be clearly heard).
  - Voice: 100%.
  - Ambient: 10-20%.
````

---

# 9. PART 7 — VIDEO RECORDING AND EXPORT GUIDE

````
VIDEO RECORDING AND EXPORT GUIDE

METHOD 1: OBS STUDIO (recommended, highest quality)

  Setup:
    1. Download OBS Studio (free, obsproject.com).
    2. Sources → Add → Window Capture → select Chrome with
       the documentary in fullscreen.
    3. Settings → Output:
       - Encoder: x264 (CPU) or NVENC (if NVIDIA GPU)
       - Rate Control: CQP
       - CQ Level: 18 (lower = better quality, bigger file)
       - Preset: slow or slower
    4. Settings → Audio:
       - Desktop Audio: ON (captures music and SFX)
       - Mic/Auxiliary: ON (if you record voiceover live)
       - Sample Rate: 48000 Hz
       - Channels: Stereo
    5. Settings → Video:
       - Base Resolution: 1920x1080
       - Output Resolution: 1920x1080 (or 1080x1920 for vertical)
       - FPS: 60
    6. Press H in the browser to enable clean view.
    7. Press "Start Recording" in OBS, then press Play
       in the documentary.
    8. When done, press Pause, then "Stop Recording" in OBS.
    9. File is saved in Videos folder as .mkv or .mp4.

  Quality tip: Record at 60fps, encode at CQ 18. If the file
  is too large, use CQ 20 or re-encode in HandBrake.

METHOD 2: WINDOWS GAME BAR (quick and dirty)
    1. Press Win+G to open Game Bar.
    2. Click the record button (or press Win+Alt+R).
    3. Only records the foreground window (not system audio
       from OBS). Audio may be limited.
    4. Not recommended for final output. Use for previews only.

METHOD 3: CHROME BUILT-IN SCREEN RECORD (simplest)
    1. Open Chrome, navigate to chrome://record
       (or use the Screen Capture API).
    2. Choose the tab, enable "share tab audio".
    3. Records at variable quality. Good for drafts.

METHOD 4: RECORD VOICEOVER SEPARATELY
    1. Record voice using your phone or a free tool like
       Audacity (audacityteam.org).
    2. Load the .mp3/.wav file into the documentary via the
       "🎵 Audio" button.
    3. Screen-record the video with system audio on.
    4. This gives the best voice quality.

EXPORT SETTINGS (for YouTube):
  - Resolution: 1920x1080
  - FPS: 60 or 30
  - Codec: H.264
  - Bitrate: 10-15 Mbps
  - Audio: AAC, 192 kbps, 48 kHz

EXPORT SETTINGS (for Instagram Reels / TikTok):
  - Resolution: 1080x1920 (portrait)
  - FPS: 30
  - Codec: H.264
  - Bitrate: 8-12 Mbps
  - Duration: 60s (Reels) or 10 min (YouTube)

POST-PROCESSING (optional):
  - DaVinci Resolve (free): colour grading, transitions,
    additional graphics.
  - CapCut (free): quick text overlays, auto-captions.
  - HandBrake (free): compress or convert formats.

FILE NAMING:
  [project-name]-[length]s-[resolution]-[date].mp4
  Example: shoot-space-documentary-600s-1080p-2025-01-15.mp4
````

---

# 10. PART 8 — PROJECT BRIEF TEMPLATE

````
PROJECT BRIEF (fill in every field)

BASIC INFO
  Topic / case name:            [ ]
  Location:                     [ ]
  Time period:                  [ ]
  Purpose:                      [inform / warn / educate / investigate]
  Audience:                     [general public / students / investors /
                                 Gujarati-speaking viewers]
  On-screen text language:      [English / Hindi / Gujarati]
  Narration language:           [English / Hindi / Gujarati]
  Total length:                 [e.g. 600 seconds = 10 minutes]
  Format:                       [16:9 1920x1080 / 9:16 1080x1920]
  Tone:                         [serious investigative / neutral explainer /
                                 dramatic / educational]
  Visual style:                 [cinematic dark / news channel / minimal /
                                 neon / corporate]
  Music mood:                   [dark ambient / tense / hopeful ending]
  Font preference:              [system / Noto Sans Gujarati / Poppins]

COLOUR PALETTE
  Background:                   [#07070d]
  Primary accent:               [#ff5a5a]
  Secondary accent:             [#ffb84e]
  Text:                         [#ffffff]
  Muted text:                   [#99a]

VERIFIED FACTS (only source of truth — paste everything you have)
  For each: fact, source name, link/document number, date.
  1. [Fact] - [Source] - [Link/Date]
  2. [Fact] - [Source] - [Link/Date]
  3. [Fact] - [Source] - [Link/Date]
  4. [Fact] - [Source] - [Link/Date]
  5. [Fact] - [Source] - [Link/Date]
  ... (as many as you have)

KEY NUMBERS
  Total amount involved:        [ ] (source: [ ])
  Number of victims/complaints: [ ] (source: [ ])
  Number of accused:            [ ] (source: [ ])
  Key dates:                    [ ]
  Legal status:                 [FIR number / court / stage /
                                 accused status]

PEOPLE AND ENTITIES (neutral descriptions only)
  - [Name]: [role, as stated in source, e.g. "alleged operator,
    per FIR dated [date]"]
  - [Name]: [role, as stated in source]

LOCATIONS
  - [City/area], Gujarat: [what happened there, per source]

OFFICIAL HELPLINES TO INCLUDE
  - Cyber crime helpline: 1930
  - Cyber crime portal: cybercrime.gov.in
  - [Any state-specific or regulator contacts]

SOURCES (for the outro screen)
  1. [Publication name], [article title], [date], [link]
  2. [Publication name], [article title], [date], [link]
  3. [FIR / court order / press release]: [document number, date]
  ...

DELIVERABLES (output in this order)
  1. Understanding + list of missing information (NEED FROM USER)
  2. Scene-by-scene plan table (sums to exact target length)
  3. Full narration script with timestamps and [PAUSE] marks
  4. Music and SFX cue sheet with timestamps
  5. Architecture summary (5-8 bullets)
  6. Complete HTML file in ONE code block (no omissions)
  7. Bug checklist report (Part 9) with pass/fail for each item
  8. Quality rubric score (Part 10) with notes
  9. Fact-check list: every claim that needs verification
  10. Assumptions and open questions
````

---

# 11. PART 9 — BUG CHECKLIST AND QA

````
BUG CHECKLIST (run before every final output)

Report the result of each item: PASS or FAIL + what you fixed.

TIMELINE AND CLOCK
  [ ] 1. Scene durations sum to the exact target length.
  [ ] 2. Pausing freezes ALL motion: DOM animations, counters,
         canvas background, and audio.
  [ ] 3. Seeking backward re-renders the correct scene state
         with correct animation positions.
  [ ] 4. Seeking forward does the same.
  [ ] 5. Seeking during a transition does not leave two scenes
         stuck on screen.
  [ ] 6. Replay from the end resets everything (clock, scene,
         audio, animations).
  [ ] 7. Speed control (0.5x, 1.5x, 2x) changes clock speed but
         keeps audio in sync.

AUDIO
  [ ] 8. Audio starts only after a user gesture (click-to-play
         overlay present).
  [ ] 9. Audio currentTime stays within 0.25s of timeline `t`
         after seek, pause, resume, and speed change.
  [ ] 10. Voiceover ducking works (music lowers when voice plays,
          restores when voice stops).
  [ ] 11. Volume sliders work independently for music and voice.
  [ ] 12. All .play() calls have .catch() — no unhandled rejections.
  [ ] 13. No console errors when loading audio files.

VISUALS
  [ ] 14. No text overflow at 1920×1080, 1280×720, and 1080×1920.
  [ ] 15. Long Gujarati/Hindi strings wrap properly (line-height
          >= 1.5, word-break enabled if needed).
  [ ] 16. Particles remain <= 120 (performance).
  [ ] 17. Canvas background draws from time-based functions (not
          accumulated velocity) so seeking is deterministic.
  [ ] 18. Film grain and scanlines do not reduce contrast below
          4.5:1.
  [ ] 19. No flashing faster than 3 times per second.

UI AND INPUT
  [ ] 20. Clean view hides every control, including cursor.
  [ ] 21. Keyboard shortcuts do not fire while focus is in an
          input field.
  [ ] 22. Progress bar works on click AND drag (mousedown →
          mousemove → mouseup).
  [ ] 23. Chapter ticks on progress bar are clickable.
  [ ] 24. Speed control changes display correctly (1x, 1.5x...).
  [ ] 25. Fullscreen works in both document.requestFullscreen
          and exitFullscreen.
  [ ] 26. Window resize does not restart the timeline or cause
          layout breaks.

ACCESSIBILITY
  [ ] 27. Captions toggle (C) shows/hides narration text.
  [ ] 28. prefers-reduced-motion is honoured (fewer particles,
          shorter durations, no shake/glitch).
  [ ] 29. Text contrast >= 4.5:1 on all backgrounds.

CONTENT
  [ ] 30. No invented facts; all gaps are [FILL IN] placeholders.
  [ ] 31. "Presumed innocent unless convicted" disclaimer present
          for real people.
  [ ] 32. Source attributions present for key claims.
  [ ] 33. Official helpline numbers correct (1930,
          cybercrime.gov.in).

CODE QUALITY
  [ ] 34. Single .html file, inline CSS + JS, zero external
          dependencies.
  [ ] 35. No "...", no "TODO", no "rest of code here", no
          half-implemented functions.
  [ ] 36. Clear "EDIT YOUR CONTENT HERE" section at top.
  [ ] 37. Comments explain key sections (clock, engine, audio,
          background).
  [ ] 38. No console errors or warnings on load.
  [ ] 39. Code runs offline (no CDN, no font downloads).

PERFORMANCE
  [ ] 40. 60fps on a normal laptop (verify: Chrome DevTools →
          Performance tab → record → check for dropped frames).
  [ ] 41. Only transform, opacity, clip-path, and filter are
          animated (no top/left/width/height).
  [ ] 42. O(n²) particle line checks are skipped when n > 80.
````

---

# 12. PART 10 — SELF-REVIEW RUBRIC

````
QUALITY RUBRIC (score each item 1-5, then fix anything below 4)

CINEMATOGRAPHY (visual quality)
  [ ] 1-5  Every scene has ONE clear focal point.
  [ ] 1-5  Visual hierarchy is clear: headline > body > detail.
  [ ] 1-5  5% safe margin respected; nothing clipped at edges.
  [ ] 1-5  Typography is intentional: sizes, spacing, weights
             chosen for readability and style.
  [ ] 1-5  Colour palette is consistent and purposeful.
  [ ] 1-5  Background complements content, never competes.

MOTION (animation quality)
  [ ] 1-5  All animations use easing (never linear for UI).
  [ ] 1-5  Stagger creates rhythm (not all elements at once).
  [ ] 1-5  Overshoot / bounce on key elements (adds life).
  [ ] 1-5  Transitions between scenes feel intentional
             (chosen, not default).
  [ ] 1-5  Counters animate with ease, not jumpy.
  [ ] 1-5  Secondary motion present (particles react to scene
             change, glow pulses, etc).

STORY (narrative quality)
  [ ] 1-5  First 15 seconds grab attention (hook works).
  [ ] 1-5  Clear three-act structure (setup, conflict, resolution).
  [ ] 1-5  Each scene has ONE message, not many.
  [ ] 1-5  Pacing varies: fast hook, slower middle, calm end.
  [ ] 1-5  Narration reads naturally at 140 wpm.
  [ ] 1-5  Emotion is conveyed through facts, not adjectives.

FACTS AND SAFETY
  [ ] 1-5  Every fact traceable to a source I provided.
  [ ] 1-5  No invented names, dates, amounts, or quotes.
  [ ] 1-5  Neutral language for real people (alleged, per source).
  [ ] 1-5  Disclaimer and presumption of innocence present.
  [ ] 1-5  Sources listed on outro screen.

TECHNICAL
  [ ] 1-5  Seeks and pauses work perfectly.
  [ ] 1-5  Audio syncs within 0.25s at all times.
  [ ] 1-5  Responsive at all target resolutions.
  [ ] 1-5  No console errors.
  [ ] 1-5  60fps performance.

OVERALL SCORE: ___ / 100 (20 items × 5 = 100)
  - 90-100: Broadcast quality. Ship it.
  - 70-89:  Good. Fix items scored below 4.
  - 50-69:  Needs significant improvement. Re-run polish pass.
  - Below 50: Rebuild affected sections.
````

---

# 13. PART 11 — FACT-CHECK AND LEGAL SAFETY

````
FACT-CHECK AND LEGAL SAFETY

BEFORE PUBLISHING, verify every claim in your script.

FACT-CHECK QUESTIONS (ask for each claim):
  1. Where did I get this fact? (link or document)
  2. Is this fact still accurate? (courts decide; status changes)
  3. Would this hold up if the person mentioned challenged it?
  4. Am I using neutral language or loaded language?
  5. Would a journalist use this exact wording?

LANGUAGE GUIDE:

  AVOID THIS          → USE THIS
  ─────────────────────────────────────────────
  "scam"              → "alleged fraud scheme" or "case"
  "cheated"           → "victims allege" or "police allege"
  "fake"              → "fraudulent" (only if proven in court)
  "criminal"          → "accused" or "person facing charges"
  "stole"             → "alleged to have taken"
  "criminal"          → "accused" or "person facing charges"
  "the scammer said"  → "the accused said, according to [source]"
  "he committed fraud"→ "he is charged with fraud"
  "punishment"        → "if convicted, he could face"

  ALWAYS INCLUDE (for real people and companies):
  - "According to [source name, date]"
  - "Alleged" / "allegedly"
  - "Presumed innocent until proven guilty"
  - "This documentary is based on public records"

LEGAL CHECKLIST:
  [ ] Every factual claim has a source.
  [ ] Every person mentioned is described with "alleged" or
      "accused" unless convicted.
  [ ] No opinion is presented as fact.
  [ ] No private individual's personal details are exposed
      (phone, address, family) without consent or public record.
  [ ] Disclaimer on outro: "Based on public records. Individuals
      named are presumed innocent unless convicted by a court."
  [ ] Consider consulting a lawyer if publishing to a large
      audience, especially if naming specific individuals.
````

---

# 14. PART 12 — FOLLOW-UP PROMPT LIBRARY

Copy-paste these after your AI delivers the first version.

````
POLISH PROMPTS

"Add a Gujarat map in SVG with animated pins for the locations
in my facts. Pins drop from above with a bounce. Pulse rings
expand. Labels appear beside each pin."

"Add an animated bar chart showing money collected vs. money
returned using these numbers: [...]. Bars grow from baseline
with stagger. Values count up. Use red for collected, green
for returned."

"Add an animated line chart showing complaints over time using
these data points: [...]. SVG polyline draws in with
stroke-dashoffset. Data points pop as the line passes them."

"Add a money-flow diagram: nodes for each step, arrows between
them. Animate stroke-dashoffset on the arrows. Show amounts
on the arrows. Animate small circles flowing along arrows
to represent money movement."

"Add a waveform visualiser that reacts to the audio using
Web Audio API AnalyserNode. Draw frequency bars on a canvas
at the bottom of the viewport."

"Add film grain overlay (noise canvas at opacity 0.04,
redrawn every 3 frames) and scanlines (repeating gradient,
opacity 0.03)."

"Add a lower-third name tag component that slides in from
left with overshoot. Show name bold, title lighter below.
Auto-hide after 4 seconds with slide-out animation."

"Add a compare split-screen scene: left side 'What was
promised', right side 'What actually happened'. Vertical
divider draws in. Items appear on both sides simultaneously.
Red X stamps on the reality side."

"Add a redaction effect: sensitive text covered by black bars
that wipe away to reveal the text underneath."

"Add a typewriter effect for all quote scenes. Reveal
characters one by one with a blinking cursor at the end."

"Add auto-ducking to the audio: when voiceover plays, ramp
music gain to 0.25 over 0.4s. When voice stops, ramp back
to 1.0 over 0.8s. Use gain.linearRampToValueAtTime()."

"Add transition variety: use glitch transition for Act 2
scenes, wipe for Act 3, crossfade for Act 1. Implement all
three as reusable functions."

"Add a countdown timer scene: 3, 2, 1 with scale animations
and a circular progress ring drawing around each number."

"Add a globe or spinning earth canvas animation behind the
intro title, with country borders drawn in accent colour."

"Add a quotation marks animation: two large quotation marks
(" ") appear first, scale up from 0, then the quote text
typewrites in between them."

"Convert all text to Gujarati. Use Noto Sans Gujarati as
the font stack. Check that line-height >= 1.5 for Gujarati
text."

"Make a 9:16 vertical version for Instagram Reels. Adjust
all layouts for portrait. Shorten to 60 seconds for a
YouTube Short."

"Shorten this to 60 seconds for a YouTube Short. Keep only
the hook, one key statistic, the biggest reveal, and the
call to action. Make it fast-paced."

"Add chapter markers on the progress bar. Clicking a marker
jumps to that chapter. Show chapter name in a tooltip on hover."

"Add a speed control: 0.5x, 1x, 1.5x, 2x. When speed > 1x,
shorten animation durations proportionally."

"Add a click-to-play overlay: full-screen div with play button
and title. On click, start clock, audio, and animations
simultaneously. Fade the overlay out over 0.5s."

"Add a loading animation while the audio file is being
decoded: a spinner or progress bar, then transition to
the first scene."

"Show only the changed CSS and JS functions. Do not repeat
unchanged code."

"Continue from exactly where you stopped, starting at the
line [paste the last line of code you received]."

"Fix these errors I found in Chrome console: [paste errors]."

"The counter is not resetting when I seek backward. Fix the
counter so it computes from local time, not from accumulated
increments."

"Audio drifts after seeking. Add drift correction every 500ms:
if abs(audio.currentTime - t) > 0.25, set audio.currentTime = t."

"The scene transition leaves two scenes on screen when I seek
during it. Fix by managing outgoing and incoming layers
explicitly."

FACT AND STORY PROMPTS

"Rewrite the narration for scene 5 to be more conversational.
Shorter sentences. More [PAUSE] marks. Target 140 wpm."

"Add a scene between the timeline and the victims: a bar chart
of money collected vs. money returned per year."

"The hook is weak. Rewrite the first 15 seconds. Open with
the most shocking number or quote. Give me 3 options."

"Add a scene that directly addresses: 'Was this legal?' with
the regulatory status from my sources."

"Add a scene comparing this case to a similar case in another
state, using only facts from the sources I provided."

"Add a closing question: 'How many similar schemes are still
running today?' followed by the helpline numbers."

"As a fact-check, list every claim in the narration script
that needs verification and which source I should check it
against."
````

---

# 15. PART 13 — SKILLS GLOSSARY

Keyword list for your AI (also useful for searching tutorials).

````
SKILLS GLOSSARY

ANIMATION
  CSS keyframes, @keyframes, animation-delay, animation-timing-function,
  animation-fill-mode, animation-play-state, animation shorthand,
  Web Animations API, element.animate(), Animation.play(), .pause(),
  .currentTime, fill:"both", cubic-bezier, easing curves,
  requestAnimationFrame, performance.now(), Transform Property,
  translate, rotate, scale, skew, transform-origin, perspective,
  transform-style: preserve-3d, will-change, Animate only transform
  and opacity, clip-path, inset(), circle(), polygon(), filter,
  blur, drop-shadow, hue-rotate, backdrop-filter, mix-blend-mode,
  opacity, z-index, stacking contexts

MOTION DESIGN
  anticipation, overshoot, stagger, overlapping action,
  secondary motion, follow-through, timing, easing,
  kinetic typography, lower thirds, transitions, wipe,
  crossfade, zoom, slide, glitch, iris/radial,
  counters, animated numbers, parallax, scroll-linked,
  spring animations, bounce, elastic, motion paths,
  offset-path, offset-distance, offset-rotate

GRAPHICS
  Canvas 2D, getContext("2d"), arc, fill, stroke, fillRect,
  clearRect, beginPath, moveTo, lineTo, closePath, lineWidth,
  strokeStyle, fillStyle, globalAlpha, gradient, linearGradient,
  radialGradient, createLinearGradient, createRadialGradient,
  SVG, path, polyline, polygon, circle, rect, line, text,
  stroke-dasharray, stroke-dashoffset, viewBox, preserveAspectRatio,
  markers, defs, use, gradient, pattern, clipPath, foreignObject

AUDIO
  Web Audio API, AudioContext, createGain, GainNode,
  createOscillator, OscillatorNode, createBufferSource,
  AudioBufferSourceNode, createBiquadFilter, BiquadFilterNode,
  AnalyserNode, getByteFrequencyData, createMediaElementSource,
  connect, disconnect, gain.value, linearRampToValueAtTime,
  setTargetAtTime, suspend, resume, currentTime, play, pause,
  mute, volume, ducking, panning, createStereoPanner, convolution,
  createConvolver, reverb, delay, createDelay, feedback

PLAYER UI
  input[type="range"], input[type="file"], label, button,
  click, mousedown, mousemove, mouseup, touchstart, touchmove,
  touchend, keydown, keyCode, code, Space, ArrowLeft, ArrowRight,
  fullscreen, requestFullscreen, exitFullscreen, document.hidden,
  visibilitychange, blur, focus, change, input, slider,
  progress bar, seek, scrubbing, draggable

RESPONSIVE DESIGN
  clamp(), min(), max(), viewport units (vw, vh, dvh),
  media queries, @media, aspect-ratio, flexbox, display:flex,
  justify-content, align-items, flex-direction, flex-wrap, gap,
  grid, display:grid, grid-template-columns, grid-template-rows,
  min-height: 100dvh, safe area insets, env(safe-area-inset-*)

PERFORMANCE
  60fps, dropped frames, FPS counter, Chrome DevTools Performance,
  requestAnimationFrame, avoid layout thrash, will-change,
  transform, opacity, only animate compositor properties,
  avoid top/left/width/height, O(n²), particle cap, canvas
  optimization, throttle, debounce, Intersection Observer

ACCESSIBILITY
  prefers-reduced-motion, prefers-color-scheme, contrast ratio,
  WCAG 4.5:1, aria-label, aria-live, role, tabindex,
  keyboard navigation, focus-visible, screen reader,
  alt text, semantic HTML, caption, subtitle, deaf, hard of hearing

DOCUMENTARY SPECIFIC
  hook, three-act structure, pacing, narration, script,
  140 wpm, voiceover, fact-check, source attribution,
  disclaimer, presumption of innocence, lower third,
  chapter card, title card, b-roll (here: animated background),
  music bed, sound design, ducking, rhythm, tone,
  investigation, timeline, money trail, victims, impact

BROWSER API
  Window, Document, Element, Node, setTimeout, setInterval,
  requestAnimationFrame, performance.now, Date.now, Math,
  Array.from, forEach, map, filter, find, reduce, sort,
  spread, rest, destructuring, template literals, optional
  chaining (?.), nullish coalescing (??), structuredClone,
  URL.createObjectURL, URL.revokeObjectURL, localStorage,
  sessionStorage, history, location, navigator,
  screen.width, innerWidth, innerHeight, resize, matchMedia

VIDEO OUTPUT
  OBS Studio, Window Capture, x264, NVENC, CQP, bitrate,
  1080p, 1920x1080, 1080x1920, 60fps, 30fps, H.264, AAC,
  HandBrake, DaVinci Resolve, CapCut, Audacity, screen
  recording, capture system audio, export settings
````

---

# 16. PART 14 — COMPLETE STARTER CODE TEMPLATE

A fully working skeleton that your AI can fill in. This is the engine architecture.

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Motion Graphics Documentary</title>
<style>
/* ═══════════════════════════════════════════════════
   DESIGN TOKENS — change colours/fonts here only
   ═══════════════════════════════════════════════════ */
:root {
  --bg:         #07070d;
  --primary:    #ff5a5a;
  --secondary:  #ffb84e;
  --text:       #ffffff;
  --muted:      #99a;
  --font:       "Segoe UI", "Helvetica Neue", Arial, "Noto Sans Gujarati", sans-serif;
  --ease-out:   cubic-bezier(0.22, 1, 0.36, 1);
  --ease-in:    cubic-bezier(0.7, 0, 0.84, 0);
  --ease-bounce:cubic-bezier(0.34, 1.56, 0.64, 1);
  --ease-io:    cubic-bezier(0.65, 0, 0.35, 1);
}

/* ═══════════════════════════════════════════════════
   RESET AND BASE
   ═══════════════════════════════════════════════════ */
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }

html, body {
  height: 100%;
  background: var(--bg);
  color: var(--text);
  font-family: var(--font);
  overflow: hidden;
}

/* ═══════════════════════════════════════════════════
   LAYERS (z-index order)
   0: canvas background
   1: vignette / grain / scanlines
   2: outgoing scene layer
   3: incoming scene layer
   4: chapter tag / lower thirds
   5: captions
   6: player UI
   7: click-to-play overlay
   ═══════════════════════════════════════════════════ */
#bg       { position:fixed; inset:0; z-index:0; }
#vignette { position:fixed; inset:0; z-index:1; pointer-events:none;
  background: radial-gradient(ellipse at center,
    transparent 40%, rgba(0,0,0,0.75));
}
#grain    { position:fixed; inset:0; z-index:1; pointer-events:none;
  opacity:0.04;
}
#scanlines{ position:fixed; inset:0; z-index:1; pointer-events:none;
  opacity:0.03;
  background: repeating-linear-gradient(
    0deg, transparent, transparent 2px,
    rgba(0,0,0,0.5) 2px, rgba(0,0,0,0.5) 4px);
}

#stage-out { position:fixed; inset:0 0 80px 0; z-index:2;
  display:flex; flex-direction:column; align-items:center;
  justify-content:center; text-align:center; padding:4vw;
  will-change: opacity, transform;
}
#stage-in  { position:fixed; inset:0 0 80px 0; z-index:3;
  display:flex; flex-direction:column; align-items:center;
  justify-content:center; text-align:center; padding:4vw;
  will-change: opacity, transform;
}

#chapter   { position:fixed; top:24px; left:30px; z-index:4;
  font-size:.85rem; letter-spacing:.35em; text-transform:uppercase;
  color:var(--primary); border-left:4px solid var(--primary);
  padding-left:12px;
}
#lowerthird { position:fixed; bottom:120px; left:30px; z-index:4;
  background:rgba(0,0,0,0.7); border-left:4px solid var(--primary);
  padding:10px 20px; border-radius:0 8px 8px 0;
  opacity:0; transform:translateX(-110%); transition:all .6s var(--ease-out);
}
#lowerthird.show { opacity:1; transform:translateX(0); }
#lowerthird b { display:block; font-size:1.3rem; }
#lowerthird span { font-size:.9rem; color:var(--muted); }

#caption   { position:fixed; left:50%; bottom:100px; z-index:5;
  transform:translateX(-50%); max-width:80vw; text-align:center;
  background:rgba(0,0,0,0.7); padding:.6rem 1.2rem; border-radius:8px;
  font-size:clamp(1rem,1.6vw,1.3rem); display:none;
}

/* ═══════════════════════════════════════════════════
   PLAYER UI
   ═══════════════════════════════════════════════════ */
#ui {
  position:fixed; left:0; right:0; bottom:0; height:80px; z-index:6;
  background:rgba(0,0,0,0.9); display:flex; align-items:center;
  gap:10px; padding:0 16px; transition:opacity .4s;
}
#ui button, #ui label {
  background:#1c1c28; color:#fff; border:1px solid #444;
  border-radius:6px; padding:.4rem .7rem; cursor:pointer;
  font-size:.85rem; transition:all .2s;
}
#ui button:hover, #ui label:hover { background:var(--primary); }
#progress { flex:1; height:8px; background:#333; border-radius:4px;
  cursor:pointer; position:relative;
}
#progress-fill {
  height:100%; width:0; background:linear-gradient(90deg,
    var(--primary), var(--secondary)); border-radius:4px;
}
#progress-fill::after {
  content:''; position:absolute; right:-5px; top:50%;
  transform:translateY(-50%); width:12px; height:12px;
  background:var(--secondary); border-radius:50%;
}
#chapters { position:absolute; inset:0; pointer-events:none; }
#chapters .tick {
  position:absolute; top:-4px; width:2px; height:16px;
  background:var(--muted); pointer-events:cursor;
}
#time { font-variant-numeric:tabular-nums; min-width:100px;
  font-size:.85rem; color:var(--muted);
}
#speed { width:60px; background:#1c1c28; color:#fff;
  border:1px solid #444; border-radius:6px; padding:.3rem;
}
.vol-wrap { display:flex; align-items:center; gap:4px; }
.vol-wrap input[type="range"] { width:50px; accent-color:var(--primary); }
.vol-wrap label { font-size:.75rem; color:var(--muted); }

/* ═══════════════════════════════════════════════════
   CLICK-TO-PLAY OVERLAY
   ═══════════════════════════════════════════════════ */
#overlay {
  position:fixed; inset:0; z-index:7; background:rgba(0,0,0,0.92);
  display:flex; flex-direction:column; align-items:center;
  justify-content:center; cursor:pointer; transition:opacity .5s;
}
#overlay.hide { opacity:0; pointer-events:none; }
#overlay .big-play {
  width:80px; height:80px; border:3px solid var(--primary);
  border-radius:50%; display:flex; align-items:center;
  justify-content:center; font-size:2.5rem;
  animation:pulse 2s ease-in-out infinite;
}
@keyframes pulse {
  0%,100% { transform:scale(1); box-shadow:0 0 0 0 rgba(255,90,90,0.4); }
  50% { transform:scale(1.1); box-shadow:0 0 0 20px rgba(255,90,90,0); }
}
#overlay h2 { margin-top:2rem; font-size:1.5rem; letter-spacing:.3em;
  text-transform:uppercase; color:var(--muted);
}

/* ═══════════════════════════════════════════════════
   SCENE COMPONENTS (styles for each type)
   ═══════════════════════════════════════════════════ */
.r { opacity:0; }

h1 { font-size:clamp(2.4rem,7vw,6rem); font-weight:800;
  letter-spacing:.04em; line-height:1.1; }
h2 { font-size:clamp(1.8rem,4.5vw,3.6rem); font-weight:700;
  margin-bottom:1.5rem; }
.tag { letter-spacing:.4em; text-transform:uppercase;
  color:var(--muted); font-size:clamp(.9rem,1.6vw,1.2rem);
  margin-top:1.2rem; }

.bar { height:4px; width:0; margin:1.4rem auto; border-radius:4px;
  background:linear-gradient(90deg, var(--primary), var(--secondary));
}

ul { list-style:none; text-align:left; max-width:900px; }
li { font-size:clamp(1.1rem,2.3vw,1.8rem); margin:.8rem 0;
  padding-left:1.4rem; border-left:3px solid var(--primary);
  line-height:1.5;
}

.num { font-size:clamp(4rem,14vw,11rem); font-weight:900;
  background:linear-gradient(180deg, #fff, var(--primary));
  -webkit-background-clip:text; background-clip:text;
  color:transparent; line-height:1;
}
.label { font-size:clamp(1.1rem,2.4vw,2rem); color:#ddd;
  margin-top:1rem; max-width:800px;
}

.steps { display:flex; gap:1.2rem; flex-wrap:wrap;
  justify-content:center; max-width:1200px;
}
.step { background:rgba(255,255,255,0.06);
  border:1px solid rgba(255,255,255,0.15); border-radius:14px;
  padding:1.4rem; width:220px; backdrop-filter:blur(6px);
}
.step b { display:block; font-size:2.4rem; color:var(--primary); }
.step span { font-size:1.05rem; }

.tl { position:relative; max-width:900px; text-align:left;
  padding-left:40px; border-left:3px solid var(--primary);
}
.tl div { margin:1.2rem 0; position:relative; }
.tl div::before {
  content:""; position:absolute; left:-49px; top:.4rem;
  width:14px; height:14px; background:var(--primary);
  border-radius:50%; box-shadow:0 0 14px var(--primary);
}
.tl em { font-style:normal; color:var(--secondary); font-weight:700;
  display:block; letter-spacing:.15em;
}
.tl span { font-size:clamp(1rem,2vw,1.6rem); }

blockquote { font-size:clamp(1.6rem,3.6vw,3rem); font-style:italic;
  max-width:1000px; line-height:1.4;
}
blockquote::before {
  content:"\201C"; display:block; font-size:6rem;
  color:var(--primary); line-height:.5;
}
cite { display:block; margin-top:1.5rem; color:var(--secondary);
  font-size:1.2rem; letter-spacing:.2em; font-style:normal;
}

.small { font-size:.9rem; color:#889; max-width:800px;
  margin-top:2rem; line-height:1.5;
}

/* ═══════════════════════════════════════════════════
   REDUCED MOTION
   ═══════════════════════════════════════════════════ */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

/* ═══════════════════════════════════════════════════
   CLEAN VIEW (for recording)
   ═══════════════════════════════════════════════════ */
body.clean #ui, body.clean #chapter,
body.clean #lowerthird { opacity:0; pointer-events:none; }
body.clean { cursor:none; }
</style>
</head>
<body>

<!-- LAYERS -->
<canvas id="bg"></canvas>
<div id="vignette"></div>
<canvas id="grain"></canvas>
<div id="scanlines"></div>

<!-- SCENE LAYERS (two for crossfade) -->
<div id="stage-out"></div>
<div id="stage-in"></div>

<!-- OVERLAYS -->
<div id="chapter"></div>
<div id="lowerthird"><b></b><span></span></div>
<div id="caption"></div>

<!-- CLICK TO PLAY -->
<div id="overlay">
  <div class="big-play">▶</div>
  <h2>Click to start</h2>
</div>

<!-- PLAYER UI -->
<div id="ui">
  <button id="btn-play">▶ Play</button>
  <div id="progress">
    <div id="progress-fill"></div>
    <div id="chapters"></div>
  </div>
  <span id="time">0:00 / 0:00</span>
  <select id="speed">
    <option value="0.5">0.5x</option>
    <option value="1" selected>1x</option>
    <option value="1.5">1.5x</option>
    <option value="2">2x</option>
  </select>
  <div class="vol-wrap">
    <label>🎵<input type="range" id="vol-music" min="0" max="1" step="0.05" value="0.7"></label>
  </div>
  <div class="vol-wrap">
    <label>🎙<input type="range" id="vol-voice" min="0" max="1" step="0.05" value="1"></label>
  </div>
  <label>🎵 Music <input type="file" id="file-music" accept="audio/*" hidden></label>
  <label>🎙 Voice <input type="file" id="file-voice" accept="audio/*" hidden></label>
  <button id="btn-cc">CC</button>
  <button id="btn-clean">Clean (H)</button>
  <button id="btn-full">⛶</button>
</div>

<script>
/* ═══════════════════════════════════════════════════════════
   ██████ EDIT YOUR CONTENT HERE ██████
   Replace every [FILL IN] with verified facts.
   No invented names, dates, amounts, or quotes.
   ═══════════════════════════════════════════════════════════ */

const CONFIG = {
  totalDuration: 600,       // seconds
  transition: "crossfade",  // crossfade | wipe | zoom | slide | glitch
  transitionDur: 0.7,       // seconds
  particles: 80,
  captionDefault: false,
  musicDuckLevel: 0.25,    // volume when voice is playing
  musicDuckTime: 0.4,      // seconds to duck
  musicUnduckTime: 0.8,    // seconds to unduck
};

const scenes = [
  {
    type: "title",
    dur: 15,
    chapter: "Prologue",
    title: "[FILL IN: CASE NAME]",
    tag: "Gujarat · A Documentary",
    narr: "[FILL IN: one powerful opening line that sets up the story]",
    sfx: "impact",
    music: "dark",
    lower: { name: "[FILL IN]", role: "[FILL IN]" }
  },
  {
    type: "text",
    dur: 55,
    chapter: "1 · Background",
    head: "Who and what was involved?",
    items: [
      "[FILL IN: the company or organisation and what it claimed to offer]",
      "[FILL IN: where in Gujarat it operated]",
      "[FILL IN: when it started]"
    ],
    narr: "[FILL IN: Explain the background, the people, the place and the time.]",
    sfx: "whoosh",
    music: "ambient"
  },
  {
    type: "stat",
    dur: 40,
    chapter: "2 · The Promise",
    prefix: "₹",
    value: 0,  // set actual number
    suffix: "",
    label: "[FILL IN: the return or promise offered to people]",
    narr: "[FILL IN: Describe what people were promised.]",
    sfx: "tick",
    music: "tense"
  },
  {
    type: "steps",
    dur: 60,
    chapter: "3 · How It Worked",
    head: "How the scheme operated",
    steps: [
      "[FILL IN: Step 1 — how people were approached]",
      "[FILL IN: Step 2 — how money was collected]",
      "[FILL IN: Step 3 — early payouts or proof]",
      "[FILL IN: Step 4 — how it grew]"
    ],
    narr: "[FILL IN: Walk through the mechanism step by step.]",
    sfx: null,
    music: "tense"
  },
  {
    type: "timeline",
    dur: 70,
    chapter: "4 · Timeline",
    head: "How events unfolded",
    events: [
      ["[YEAR]", "[FILL IN: launch]"],
      ["[YEAR]", "[FILL IN: expansion]"],
      ["[YEAR]", "[FILL IN: first complaints]"],
      ["[YEAR]", "[FILL IN: collapse or payouts stop]"]
    ],
    narr: "[FILL IN: Narrate the timeline with exact dates from sources.]",
    sfx: "whoosh",
    music: "tense"
  },
  {
    type: "stat",
    dur: 40,
    chapter: "5 · The Victims",
    prefix: "",
    value: 0,  // set actual number
    suffix: "",
    label: "[FILL IN: number of victims or complaints, per official source]",
    narr: "[FILL IN: Who were the victims? Keep it factual and respectful.]",
    sfx: "impact",
    music: "tense"
  },
  {
    type: "flow",
    dur: 60,
    chapter: "6 · Money Trail",
    head: "Where did the money go?",
    nodes: [
      { label: "[FILL IN: source]", amount: "[FILL IN]" },
      { label: "[FILL IN: middle]", amount: "[FILL IN]" },
      { label: "[FILL IN: destination]", amount: "[FILL IN]" }
    ],
    narr: "[FILL IN: Explain the money trail as stated in official records.]",
    sfx: null,
    music: "tense"
  },
  {
    type: "steps",
    dur: 60,
    chapter: "7 · Investigation",
    head: "How it came to light",
    steps: [
      "[FILL IN: Complaint filed]",
      "[FILL IN: Agency involved]",
      "[FILL IN: Raids / arrests]",
      "[FILL IN: Evidence found]"
    ],
    narr: "[FILL IN: How did authorities uncover and respond to it?]",
    sfx: "whoosh",
    music: "tense"
  },
  {
    type: "timeline",
    dur: 60,
    chapter: "8 · Legal Action",
    head: "Courts and charges",
    events: [
      ["[DATE]", "[FILL IN: FIR / charges]"],
      ["[DATE]", "[FILL IN: arrests / bail]"],
      ["[DATE]", "[FILL IN: court hearing]"],
      ["[DATE]", "[FILL IN: current status]"]
    ],
    narr: "[FILL IN: State that accused persons are presumed innocent unless convicted.]",
    sfx: "hit",
    music: "tense"
  },
  {
    type: "quote",
    dur: 30,
    chapter: "9 · Voices",
    quote: "[FILL IN: a real, sourced quote from a victim, officer, or court order]",
    who: "[FILL IN: Name, role, source]",
    narr: "[Read the quote or pause for effect.]",
    sfx: null,
    music: "ambient"  // music ducks during quote
  },
  {
    type: "text",
    dur: 50,
    chapter: "10 · Impact",
    head: "The human cost",
    items: [
      "[FILL IN: financial impact on families]",
      "[FILL IN: impact on the community]",
      "[FILL IN: regulatory or policy changes]"
    ],
    narr: "[FILL IN: Reflect on the wider consequences.]",
    sfx: null,
    music: "ambient"
  },
  {
    type: "text",
    dur: 40,
    chapter: "11 · Stay Safe",
    head: "How to spot a scam",
    items: [
      "Guaranteed high returns are a red flag",
      "Check registration with SEBI / RBI / MCA",
      "Never invest under pressure or secrecy",
      "Report fraud: cybercrime.gov.in · call 1930"
    ],
    narr: "Here is how you can protect yourself and your family.",
    sfx: "chime",
    music: "resolve"
  },
  {
    type: "outro",
    dur: 20,
    chapter: "Sources",
    head: "Sources & Disclaimer",
    items: [
      "[FILL IN: source 1 — link / date]",
      "[FILL IN: source 2 — link / date]"
    ],
    small: "This documentary is based on public records. Individuals named are presumed innocent unless convicted by a court of law.",
    narr: "Thank you for watching.",
    sfx: null,
    music: "resolve"
  }
];

/* ═══════════════════════════════════════════════════════════
   ██████ ENGINE (do not edit below this line) ██████
   ═══════════════════════════════════════════════════════════ */

// ── Compute start times ──
scenes.reduce((acc, s) => { s.start = acc; return acc + s.dur; }, 0);
const TOTAL = scenes[scenes.length-1].start + scenes[scenes.length-1].dur;

// ── State ──
let t = 0;                  // current time in seconds
let playing = false;
let speed = 1;
let lastRAF = performance.now();
let currentSceneIdx = -1;

// ── DOM refs ──
const $ = id => document.getElementById(id);
const stageOut = $("stage-out");
const stageIn = $("stage-in");
const audMusic = new Audio();
const audVoice = new Audio();

// ── Helpers ──
const fmt = s => Math.floor(s/60) + ":" + String(Math.floor(s%60)).padStart(2,"0");
const easeOutExpo = x => x >= 1 ? 1 : 1 - Math.pow(2, -10*x);
const D = (i, base=0.3, step=0.35) =>
  `style="opacity:0;transform:translateY(40px);transition:opacity .7s var(--ease-out) ${(base+i*step).toFixed(2)}s, transform .7s var(--ease-out) ${(base+i*step).toFixed(2)}s"`;

// ── Scene renderers ──
const renderers = {
  title(s) {
    const letters = [...s.title].map((ch,i) =>
      `<span style="display:inline-block;opacity:0;transform:translateY(60px) rotateX(90deg);transition:all .7s var(--ease-bounce) ${(0.2+i*0.1).toFixed(2)}s">${ch===" "?" ":ch}</span>`
    ).join("");
    return `
      <h1>${letters}</h1>
      <div class="bar" style="transition:width 1s var(--ease-out) 1.2s"></div>
      <p class="tag">${s.tag}</p>
    `;
  },
  text(s) {
    const items = s.items.map((x,i) => `<li class="r" ${D(i,0.8,0.9)}>${x}</li>`).join("");
    return `<h2 class="r" ${D(0,0.1)}>${s.head}</h2><ul>${items}</ul>`;
  },
  stat(s) {
    return `
      <div class="num" id="counter"
           data-target="${s.value}" data-prefix="${s.prefix}" data-suffix="${s.suffix}">
        ${s.prefix}0${s.suffix}
      </div>
      <p class="label r" ${D(0,1)}>${s.label}</p>
    `;
  },
  steps(s) {
    const cards = s.steps.map((x,i) =>
      `<div class="step r" ${D(i,0.8,0.8)}><b>${i+1}</b><span>${x}</span></div>`
    ).join("");
    return `<h2 class="r" ${D(0,0.1)}>${s.head}</h2><div class="steps">${cards}</div>`;
  },
  timeline(s) {
    const events = s.events.map((e,i) =>
      `<div class="r" ${D(i,0.8,1)}><em>${e[0]}</em><span>${e[1]}</span></div>`
    ).join("");
    return `<h2 class="r" ${D(0,0.1)}>${s.head}</h2><div class="tl">${events}</div>`;
  },
  quote(s) {
    return `<blockquote class="r" ${D(0,0.3)}>${s.quote}<cite>— ${s.who}</cite></blockquote>`;
  },
  flow(s) {
    const nodes = s.nodes.map((n,i) =>
      `<div class="step r" ${D(i,0.5,0.6)}><b>${n.amount}</b><span>${n.label}</span></div>`
    ).join("");
    return `<h2 class="r" ${D(0,0.1)}>${s.head}</h2><div class="steps">${nodes}</div>`;
  },
  outro(s) {
    const items = s.items.map((x,i) => `<li class="r" ${D(i,0.6,0.5)}>${x}</li>`).join("");
    return `<h2 class="r" ${D(0,0.1)}>${s.head}</h2><ul>${items}</ul><p class="small r" ${D(0,1.6)}>${s.small}</p>`;
  }
};

// ── Show a scene ──
function showScene(idx) {
  const s = scenes[idx];
  const html = renderers[s.type] ? renderers[s.type](s) : renderers.text(s);

  // Determine which layer to use (alternate or always incoming)
  const layer = stageIn;
  layer.innerHTML = html;

  // Update chapter tag
  $("chapter").textContent = s.chapter;

  // Update captions
  $("caption").textContent = s.narr;

  // Update lower third
  const lt = $("lowerthird");
  if (s.lower) {
    lt.querySelector("b").textContent = s.lower.name;
    lt.querySelector("span").textContent = s.lower.role;
    lt.classList.add("show");
    setTimeout(() => lt.classList.remove("show"), 4000);
  } else {
    lt.classList.remove("show");
  }

  // Trigger CSS transitions by forcing reflow then removing inline styles
  requestAnimationFrame(() => {
    requestAnimationFrame(() => {
      layer.querySelectorAll(".r").forEach(el => {
        el.style.opacity = "1";
        el.style.transform = "none";
      });
      // Title letters
      layer.querySelectorAll("h1 span").forEach(el => {
        el.style.opacity = "1";
        el.style.transform = "none";
      });
      // Bar
      const bar = layer.querySelector(".bar");
      if (bar) bar.style.width = "min(380px, 60vw)";
    });
  });
}

// ── Main loop ──
function tick(now) {
  const delta = (now - lastRAF) / 1000;
  lastRAF = now;

  if (playing) {
    t += delta * speed;

    // Clamp
    if (t >= TOTAL) { t = TOTAL; setPlaying(false); }
    if (t < 0) t = 0;

    // Find current scene
    let idx = scenes.findIndex(s => t >= s.start && t < s.start + s.dur);
    if (idx < 0) idx = scenes.length - 1;

    // Render if scene changed
    if (idx !== currentSceneIdx) {
      currentSceneIdx = idx;
      showScene(idx);
    }

    // Counter animation (pure function of local time)
    const s = scenes[idx];
    const local = t - s.start;
    if (s.type === "stat") {
      const counter = $("counter");
      if (counter) {
        const k = Math.min(1, local / 2.5);
        const e = easeOutExpo(k);
        const val = Math.round(Number(counter.dataset.target) * e);
        counter.textContent =
          counter.dataset.prefix +
          val.toLocaleString("en-IN") +
          counter.dataset.suffix;
      }
    }

    // Update progress
    $("progress-fill").style.width = (t / TOTAL * 100) + "%";
    $("time").textContent = fmt(t) + " / " + fmt(TOTAL);

    // Audio sync
    syncAudio();
  }

  requestAnimationFrame(tick);
}

// ── Audio sync ──
function syncAudio() {
  if (!audMusic.src && !audVoice.src) return;

  if (audMusic.src && Math.abs(audMusic.currentTime - t) > 0.25) {
    audMusic.currentTime = t;
  }
  if (audVoice.src && Math.abs(audVoice.currentTime - t) > 0.25) {
    audVoice.currentTime = t;
  }
}

// ── Play / Pause ──
function setPlaying(p) {
  playing = p;
  $("btn-play").textContent = p ? "⏸ Pause" : "▶ Play";

  if (audMusic.src) {
    if (p) { audMusic.currentTime = t; audMusic.play().catch(()=>{}); }
    else audMusic.pause();
  }
  if (audVoice.src) {
    if (p) { audVoice.currentTime = t; audVoice.play().catch(()=>{}); }
    else audVoice.pause();
  }
}

// ── Seek ──
function seek(x) {
  t = Math.max(0, Math.min(TOTAL, x));
  currentSceneIdx = -1; // force re-render
  if (audMusic.src) audMusic.currentTime = t;
  if (audVoice.src) audVoice.currentTime = t;
}

// ── Build chapter ticks ──
function buildChapterTicks() {
  const container = $("chapters");
  container.innerHTML = "";
  scenes.forEach(s => {
    if (s.start === 0) return;
    const tick = document.createElement("div");
    tick.className = "tick";
    tick.style.left = (s.start / TOTAL * 100) + "%";
    tick.style.pointerEvents = "auto";
    tick.style.cursor = "pointer";
    tick.title = s.chapter;
    tick.addEventListener("click", e => { e.stopPropagation(); seek(s.start); });
    container.appendChild(tick);
  });
}
buildChapterTicks();

// ── Grain canvas ──
function drawGrain() {
  const c = $("grain");
  const cx = c.getContext("2d");
  c.width = 256; c.height = 256;
  const img = cx.createImageData(256, 256);
  for (let i = 0; i < img.data.length; i += 4) {
    const v = Math.random() * 255;
    img.data[i] = img.data[i+1] = img.data[i+2] = v;
    img.data[i+3] = 255;
  }
  cx.putImageData(img, 0, 0);
}
let grainFrame = 0;
setInterval(() => { grainFrame++; if (grainFrame % 3 === 0) drawGrain(); }, 100);

// ── Particle background (time-based, seek-safe) ──
const bgCanvas = $("bg");
const bgCtx = bgCanvas.getContext("2d");
let BW, BH, particles = [];
const mouse = { x: null, y: null };

function initParticles() {
  BW = bgCanvas.width = innerWidth;
  BH = bgCanvas.height = innerHeight;
  particles = Array.from({ length: CONFIG.particles }, (_, i) => ({
    bx: Math.random() * BW,
    by: Math.random() * BH,
    sx: 30 + Math.random() * 40,
    sy: 20 + Math.random() * 30,
    vx: 0.002 + Math.random() * 0.004,
    vy: 0.002 + Math.random() * 0.003,
    phase: Math.random() * Math.PI * 2,
    r: 1 + Math.random() * 2
  }));
}
addEventListener("resize", initParticles);
initParticles();

function drawBackground(now) {
  bgCtx.clearRect(0, 0, BW, BH);
  const time = playing ? now / 1000 : t; // use t when paused for determinism

  const positions = particles.map(p => ({
    x: p.bx + Math.sin(time * p.vx * 100 + p.phase) * p.sx,
    y: p.by + Math.cos(time * p.vy * 100 + p.phase) * p.sy,
    r: p.r
  }));

  // Draw particles
  positions.forEach(pos => {
    bgCtx.beginPath();
    bgCtx.arc(pos.x, pos.y, pos.r, 0, Math.PI * 2);
    bgCtx.fillStyle = "rgba(255,90,90,0.5)";
    bgCtx.fill();
  });

  // Draw lines (skip O(n²) if too many)
  if (positions.length <= 80) {
    for (let i = 0; i < positions.length; i++) {
      for (let j = i + 1; j < positions.length; j++) {
        const dx = positions[i].x - positions[j].x;
        const dy = positions[i].y - positions[j].y;
        const d = Math.sqrt(dx * dx + dy * dy);
        if (d < 130) {
          bgCtx.strokeStyle = `rgba(255,90,90,${(1 - d / 130) * 0.25})`;
          bgCtx.lineWidth = 0.5;
          bgCtx.beginPath();
          bgCtx.moveTo(positions[i].x, positions[i].y);
          bgCtx.lineTo(positions[j].x, positions[j].y);
          bgCtx.stroke();
        }
      }
      // Mouse connection
      if (mouse.x !== null) {
        const dx = positions[i].x - mouse.x;
        const dy = positions[i].y - mouse.y;
        const d = Math.sqrt(dx * dx + dy * dy);
        if (d < 160) {
          bgCtx.strokeStyle = `rgba(255,184,78,${(1 - d / 160) * 0.3})`;
          bgCtx.beginPath();
          bgCtx.moveTo(positions[i].x, positions[i].y);
          bgCtx.lineTo(mouse.x, mouse.y);
          bgCtx.stroke();
        }
      }
    }
  }

  requestAnimationFrame(drawBackground);
}
requestAnimationFrame(drawBackground);

addEventListener("mousemove", e => { mouse.x = e.clientX; mouse.y = e.clientY; });
addEventListener("mouseleave", () => { mouse.x = null; mouse.y = null; });

// ── SFX generation (Web Audio, no files) ──
let audioCtx = null;
function ensureAudioCtx() {
  if (!audioCtx) audioCtx = new (window.AudioContext || window.webkitAudioContext)();
  if (audioCtx.state === "suspended") audioCtx.resume();
  return audioCtx;
}

function playSFX(type) {
  if (!audioCtx) return;
  const ctx = audioCtx;
  const t0 = ctx.currentTime;

  if (type === "whoosh") {
    const buf = ctx.createBuffer(1, ctx.sampleRate * 0.4, ctx.sampleRate);
    const data = buf.getChannelData(0);
    for (let i = 0; i < data.length; i++) data[i] = (Math.random() * 2 - 1) * (1 - i/data.length);
    const src = ctx.createBufferSource();
    src.buffer = buf;
    const filter = ctx.createBiquadFilter();
    filter.type = "bandpass";
    filter.frequency.setValueAtTime(500, t0);
    filter.frequency.linearRampToValueAtTime(4000, t0 + 0.4);
    const g = ctx.createGain();
    g.gain.setValueAtTime(0.3, t0);
    g.gain.exponentialRampToValueAtTime(0.01, t0 + 0.4);
    src.connect(filter).connect(g).connect(ctx.destination);
    src.start(t0);
  } else if (type === "impact") {
    const osc = ctx.createOscillator();
    osc.type = "sine";
    osc.frequency.setValueAtTime(80, t0);
    const g = ctx.createGain();
    g.gain.setValueAtTime(0.5, t0);
    g.gain.exponentialRampToValueAtTime(0.01, t0 + 0.5);
    osc.connect(g).connect(ctx.destination);
    osc.start(t0); osc.stop(t0 + 0.5);
  } else if (type === "chime") {
    [523, 659, 784].forEach((f, i) => {
      const osc = ctx.createOscillator();
      osc.type = "sine";
      osc.frequency.setValueAtTime(f, t0 + i * 0.15);
      const g = ctx.createGain();
      g.gain.setValueAtTime(0.2, t0 + i * 0.15);
      g.gain.exponentialRampToValueAtTime(0.01, t0 + i * 0.15 + 0.4);
      osc.connect(g).connect(ctx.destination);
      osc.start(t0 + i * 0.15); osc.stop(t0 + i * 0.15 + 0.4);
    });
  } else if (type === "tick") {
    const osc = ctx.createOscillator();
    osc.type = "square";
    osc.frequency.setValueAtTime(1000, t0);
    const g = ctx.createGain();
    g.gain.setValueAtTime(0.1, t0);
    g.gain.exponentialRampToValueAtTime(0.01, t0 + 0.05);
    osc.connect(g).connect(ctx.destination);
    osc.start(t0); osc.stop(t0 + 0.05);
  } else if (type === "hit") {
    const osc = ctx.createOscillator();
    osc.type = "sine";
    osc.frequency.setValueAtTime(60, t0);
    const g = ctx.createGain();
    g.gain.setValueAtTime(0.6, t0);
    g.gain.exponentialRampToValueAtTime(0.01, t0 + 0.3);
    osc.connect(g).connect(ctx.destination);
    osc.start(t0); osc.stop(t0 + 0.3);
  }
}

// ── File loading ──
$("file-music").onchange = e => {
  const f = e.target.files[0];
  if (f) { audMusic.src = URL.createObjectURL(f); audMusic.currentTime = t; if (playing) audMusic.play().catch(()=>{}); }
};
$("file-voice").onchange = e => {
  const f = e.target.files[0];
  if (f) { audVoice.src = URL.createObjectURL(f); audVoice.currentTime = t; if (playing) audVoice.play().catch(()=>{}); }
};

// ── Volume ──
$("vol-music").oninput = e => { audMusic.volume = Number(e.target.value); };
$("vol-voice").oninput = e => { audVoice.volume = Number(e.target.value); };

// ── Speed ──
$("speed").onchange = e => { speed = Number(e.target.value); };

// ── Click to play overlay ──
$("overlay").addEventListener("click", () => {
  ensureAudioCtx();
  $("overlay").classList.add("hide");
  setPlaying(true);
});

// ── Play button ──
$("btn-play").onclick = () => { if (t >= TOTAL) seek(0); setPlaying(!playing); };

// ── Progress bar ──
let seeking = false;
$("progress").addEventListener("mousedown", e => { seeking = true; doSeek(e); });
addEventListener("mousemove", e => { if (seeking) doSeek(e); });
addEventListener("mouseup", () => { seeking = false; });
$("progress").addEventListener("touchstart", e => { seeking = true; doSeek(e.touches[0]); });
$("progress").addEventListener("touchmove", e => { if (seeking) doSeek(e.touches[0]); });
addEventListener("touchend", () => { seeking = false; });

function doSeek(e) {
  const rect = $("progress").getBoundingClientRect();
  const ratio = Math.max(0, Math.min(1, (e.clientX - rect.left) / rect.width));
  seek(ratio * TOTAL);
}

// ── Captions ──
$("btn-cc").onclick = () => {
  const c = $("caption");
  c.style.display = c.style.display === "block" ? "none" : "block";
};

// ── Clean view ──
$("btn-clean").onclick = () => document.body.classList.toggle("clean");

// ── Fullscreen ──
$("btn-full").onclick = () => {
  document.fullscreenElement ? document.exitFullscreen() :
    document.documentElement.requestFullscreen();
};

// ── Keyboard shortcuts ──
addEventListener("keydown", e => {
  if (e.target.tagName === "INPUT" || e.target.tagName === "SELECT") return;
  if (e.code === "Space")  { e.preventDefault(); $("btn-play").click(); }
  if (e.key === "ArrowRight") seek(t + 5);
  if (e.key === "ArrowLeft")  seek(t - 5);
  if (e.key === "ArrowUp")    { e.preventDefault(); $("vol-music").value = Math.min(1, Number($("vol-music").value) + 0.1); $("vol-music").oninput({target:$("vol-music")}); }
  if (e.key === "ArrowDown")  { e.preventDefault(); $("vol-music").value = Math.max(0, Number($("vol-music").value) - 0.1); $("vol-music").oninput({target:$("vol-music")}); }
  if (e.key === "h" || e.key === "H") $("btn-clean").click();
  if (e.key === "c" || e.key === "C") $("btn-cc").click();
  if (e.key === "f" || e.key === "F") $("btn-full").click();
  if (/^[0-9]$/.test(e.key)) {
    const idx = Number(e.key);
    if (idx < scenes.length) seek(scenes[idx].start);
  }
});

// ── Audio ducking (call when voice starts/stops) ──
function duckMusic(on) {
  if (!audMusic.src) return;
  const target = on ? CONFIG.musicDuckLevel : 1;
  const vol = Number($("vol-music").value);
  const time = on ? CONFIG.musicDuckTime : CONFIG.musicUnduckTime;
  audMusic.volume = vol;
  // Smooth transition via interval
  const start = audMusic.volume;
  const steps = 20;
  const stepTime = time * 1000 / steps;
  let step = 0;
  const iv = setInterval(() => {
    step++;
    const k = step / steps;
    audMusic.volume = start + (vol * target - start) * k;
    if (step >= steps) clearInterval(iv);
  }, stepTime);
}

// ── Start ──
drawGrain();
requestAnimationFrame(tick);
</script>
</body>
</html>
```

---

# 17. PART 15 — EXAMPLE SCENE-BY-SCENE PLAN

Here is what a plan looks like. Your AI should produce something similar after Step 1.

| # | Scene | Type | Dur | Chapter | Visual idea | Animation | Narration summary | Audio cue |
|---|---|---|---|---|---|---|---|---|
| 1 | Hook | title | 15s | Prologue | Giant number: ₹47 Cr | Letter-by-letter title with bounce; accent line grows; subtitle fades up | Open with the biggest number: "Forty-seven crore rupees. Twelve hundred families. One broken promise." | Impact hit + rising drone |
| 2 | Background | text | 55s | 1·Background | 3 bullet points with icons | Bullets slide from left with stagger 0.9s; accent border draws first | Explain who, what, where, when using sourced facts | Ambient music, whoosh transition |
| 3 | The Promise | stat | 40s | 2·Promise | Giant counter 0→target | Counter eases with easeOutExpo over 2.5s; label fades in after 80% | Describe exactly what people were promised | Tense music, tick SFX |
| 4 | Mechanism | steps | 60s | 3·How It Worked | 4 numbered cards in a row | Cards fly in from alternating directions; connecting line draws between them | Walk through the 4-step mechanism | Tense music, soft pops |
| 5 | Timeline | timeline | 70s | 4·Timeline | Vertical line with 4 dots | Line draws top→bottom; dots pop with bounce; dates slide in | Narrate exact dates from sources | Tense music, drawing sound |
| 6 | Victims | stat | 40s | 5·Victims | Giant counter for victim count | Same counter as scene 3; impact flash at completion | State number of victims per official source | Impact + music swell |
| 7 | Money Trail | flow | 60s | 6·Money Trail | 3-node flow diagram with arrows | Nodes scale in; arrows draw with stroke-dashoffset; amounts appear on arrows | Explain money movement per investigators | Tense music, coin clinks |
| 8 | Investigation | steps | 60s | 7·Investigation | 4 cards: complaint→agency→raids→evidence | Cards slide in with connecting line | How authorities uncovered it | Building tension, whoosh |
| 9 | Legal | timeline | 60s | 8·Legal Action | 4 events with dates | Same timeline as scene 5; gavel icon on court event | FIR, arrests, hearings, current status. Presumption of innocence. | Tense music, wooden hit |
| 10 | Quote | quote | 30s | 9·Voices | Large quote with typewriter | Typewriter effect; attribution lower-third slides in | [Read the real quote] | Music ducks to 0.1 |
| 11 | Impact | text | 50s | 10·Impact | 3 bullets: family, community, policy | Same bullet reveal as scene 2 | Reflect on consequences | Ambient music |
| 12 | Safety | text | 40s | 11·Stay Safe | 4 safety tips with icons | Bullets with checkmark icons; final item highlighted | How to spot a scam; 1930, cybercrime.gov.in | Hopeful chime |
| 13 | Outro | outro | 20s | Sources | Sources list + disclaimer | Fade in one by one; disclaimer with accent border | "Thank you for watching." | Fade out |

**Duration check:** 15+55+40+60+70+40+60+60+60+30+50+40+20 = **600s = 10:00 ✓**

---

# FINAL NOTES

## What makes this kit powerful

1. **The workflow prevents hallucination.** Asking for a plan before code forces the AI to think. Asking for narration before visuals forces storytelling discipline. Asking for a bug checklist forces quality.

2. **The technical spec prevents the #1 bug.** Most AI-generated animations break because CSS timers keep running while the clock is paused. The Web Animations API approach in Part 2 fixes this.

3. **The honesty rules prevent defamation.** For a real scam case, one invented detail could be legal trouble. The [FILL IN] placeholder system forces you to provide facts.

4. **The quality rubric forces self-review.** AI models often skip review. By asking for a score on 20 items, it must evaluate its own output.

## What still depends on you

- Your verified facts
- Your voiceover recording
- Your music files
- Your testing in Chrome
- Legal review before publishing

## How to iterate

After the AI delivers, test in Chrome, note issues, and paste them back using the follow-up prompts in Part 12. Small fixes work better than asking for a full rewrite.
