---
name: editing-craft
description: Elite documentary & video journalism editing craft standard for Benaqaab India. Governs rhythmic pacing, cutting syntax, audio-visual J/L cuts, sound SFX landing offsets, visual focal points, and virtual camera direction variety.
---

# 🎬 Benaqaab India: The Editing Craft & Visual Rhythm Master Skill

> **AUTHORITY:** This skill governs the visual syntax, editorial rhythm, and cinematic pacing across all Benaqaab India documentaries (16:9) and YouTube Shorts (9:16).  
> **PHILOSOPHY:** Editorial intelligence is not a mechanical beat count (e.g. uniform cuts every 2 seconds). True human craftsmanship is about **tension and release, rhythmic breath, intentional focal points, and causal audio-visual harmony**.

---

## ⚡ 1. The Pacing Law: Tension, Breath & Velocity
Uniform pacing (e.g. cutting every 1.8 seconds identically) destroys viewer retention through monotony. Editors must vary the rhythmic meter:

1. **The Fast Run (Tension & Kinetic Evidence):**
   * Rapid visual beats lasting **0.8s to 1.4s** during build-ups, evidence flurries, contrasting data points, or accelerating narratives.
2. **The Held Breath (Release & Gravity):**
   * Before dropping a bombshell statistic, official gazette revelation, or pivotal verdict, **hold the frame for 3.0s to 4.2s**.
   * Give the viewer's brain time to absorb the magnitude of the fact. Never rush past a climax.
3. **The 3:1 Rhythm Pattern:**
   * Sequence 3 rapid kinetic evidence cuts $\rightarrow$ 1 held cinematic anchor plate $\rightarrow$ 2 rapid metric callouts $\rightarrow$ 1 expansive analytical diagram.

---

## ✂️ 2. Cutting Syntax: Match Cuts, J/L Cuts & Continuity

1. **Cut On Action / Motion:**
   * When cutting between plates, align the direction of movement. If Shot A pans right, Shot B should enter with continuing rightward drift or momentum.
2. **Match Cuts (Positional & Structural Continuity):**
   * Keep the hero focal subject in the same spatial quadrant across cuts. For example, if a rupee metric transforms into a bank balance sheet, anchor the center of mass so the viewer's eye never searches the screen.
3. **Audio-Leading Picture (J-Cuts & L-Cuts):**
   * **J-Cut:** Ambient audio, voiceover cue, or SFX begins **4 to 8 frames (120ms – 250ms)** before the visual cut arrives. This pulls the viewer forward subconsciously.
   * **L-Cut:** The reverberation of an impact or the tail of an ambient sound carries over into the next shot, bridging disparate scenes.

---

## 🔊 3. Sound Design Synchronization Law: The 2-Frame Lead
Human visual perception processes auditory hits faster than retinal imagery:

1. **Pre-Impact Landing:**
   * Whooshes, paper tears, shutter clicks, and bass drops must land **1 to 2 frames (33ms – 66ms) BEFORE the visual impact**, never after.
   * If a stamp hits at $t = 12.50$s, the audio thump cue must trigger at $t = 12.44$s.
2. **Zero Naked Visuals:**
   * Every motion primitive (loupe zoom, highlighter stroke, odometer spin, verdict stamp) must have an acoustic identity.

---

## 🎯 4. Visual Focus & Negative Space

1. **One Focal Point Per Frame:**
   * Never compete for viewer attention. A frame has exactly ONE hero:
     * Either the document highlighter is speaking,
     * Or the rolling odometer is moving,
     * Or the hero portrait is emoting.
2. **Pre-Climax Negative Space:**
   * Before displaying a multi-billion dollar headline figure or verdict stamp, clear peripheral clutter. Dim secondary plates with a subtle scrim (`rgba(4, 7, 14, 0.45)`) to direct 100% of retinal focus to the evidence.

---

## 🎥 5. Camera Choreography & Directional Variety

1. **No Monotonous Zooms:**
   * Never zoom in on three consecutive shots. Alternate dynamic camera vectors:
     * Shot 1: Slow dolly in (+3% push).
     * Shot 2: Subtle lateral drift (left-to-right pan, +12px).
     * Shot 3: Steady held frame with meso-scale element motion (odometer rolling).
     * Shot 4: Gentle pull out (-2% reveal).
2. **Trauma Shake vs Elastic Slop:**
   * UI elements and cards settle with critically damped springs (`d = 0.68, w = 13.0`).
   * Heavy physical impacts (stamps, gavel strikes) use natural $1/f$ trauma-squared noise shake decaying over 120ms–250ms (`Motion.traumaShake`), strictly avoiding mechanical sine-wave oscillations.
