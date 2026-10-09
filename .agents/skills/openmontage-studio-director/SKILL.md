---
name: openmontage-studio-director
description: |
  Master video director, pipeline orchestrator, and prompt engineering engine based on OpenMontage (World's first agentic video production system). Features 12 production pipelines, CHAI 5-aspect prompting spec for Seedance 2.0 / Kling / Veo / Sora, Reference Video Analyst, Backlot living storyboard, and 3-axis critique reviewer.
---

# 🎬 OpenMontage Studio Director — Master Video Engineering Skill

This skill brings the complete **OpenMontage agentic video production system** into our workspace, synthesizing its 12 production pipelines, 130+ tools, 5-aspect prompting science, and Backlot living storyboard with Benaqaab India's forensic journalism and Antigravity 60FPS motion standards.

---

## 🏛️ 1. The 3-Layer Knowledge Architecture

OpenMontage operates on strict separation of concerns:

```
┌────────────────────────────────────────────────────────────────────────┐
│ Layer 1: tools/tool_registry.py ("What tools exist and what they do")  │
│          Dynamic runtime discovery, capabilities, provider pricing,    │
│          resource profiles, cost tracking, and selector routing.       │
└───────────────────────────────────┬────────────────────────────────────┘
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Layer 2: openmontage/skills/ ("How the studio uses these tools")       │
│          Pipeline manifests, stage director skills, artifact schemas,  │
│          taste profiles, and quality review checklists.               │
└───────────────────────────────────┬────────────────────────────────────┘
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Layer 3: .agents/skills/ ("How the underlying technology works")       │
│          Seedance 2.0, Kling Official, Grok Media, HyperFrames, Remotion│
│          Three.js, ManimCE, GSAP, FFmpeg syntax and constraints.       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 🚀 2. The 12 Production Pipelines

Every video request is treated as a **pipeline selection problem**:

| Pipeline | Best For | Visual Rhythm | Composition Engine |
|---|---|---|---|
| `animated-explainer` | Topic-to-video explainers with research & concepts | 3–6s cuts, high concept | Remotion / HyperFrames |
| `documentary-montage` | Archival, historical, real-world footage tone poems | Beat-synced archival | FFmpeg / Remotion |
| `cinematic` | High-drama trailers, teasers, atmospheric edits | 2–4s cinematic shots | HyperFrames / Canvas |
| `animation` | Motion-graphics-first design & kinetic explainers | Continuous flow | HyperFrames / GSAP |
| `character-animation` | Rigged 2D SVG cartoon characters & pose acting | Keyframe choreography | Remotion / SVG |
| `hybrid` | Real source footage + motion graphics overlays | Balanced documentary | Remotion / FFmpeg |
| `screen-demo` | Software walkthroughs, synthetic terminal & UI demos | Crisp step-by-step | Remotion / HyperFrames |
| `talking-head` | Footage-led speaker with dynamic B-roll cutaways | Speaker + 1-shape b-roll| Remotion |
| `avatar-spokesperson` | AI lip-sync presenter / spokesperson films | Dialogue-led | Remotion TalkingHead |
| `clip-factory` | Splitting long podcast/interview into viral clips | Fast-paced short cuts | FFmpeg / WhisperX |
| `podcast-repurpose` | Audio waveform + captions + dynamic highlights | Audio-led | Remotion |
| `localization-dub` | Multi-language dubbing, subtitles, translated audio | Synchronized dub | FFmpeg / WhisperX |

---

## 📐 3. The Canonical 5-Aspect Prompt Spec (CMU/Harvard CHAI Study)

Generic video prompts produce hallucinated, generic videos. Every video prompt MUST be structured across the **5 canonical aspects**:

```text
[Subject]        Type + key visual attributes + disambiguation across multiple subjects
[Subject Motion] Actions in strict temporal order; subject-to-object & subject-to-subject interactions
[Scene]          Overlays listed separately (HUD, text, lower-thirds) + POV + setting + lighting/time + dynamics
[Spatial]        Shot size (ECU/CU/MS/WS) + frame positioning + depth planes (FG/MG/BG) + camera-height-relative
[Camera]         Playback speed → lens distortion → height → angle → focus/DoF → steadiness → movement
```

### 3.1 Strict Camera Movement Primitives
- **Dolly vs. Zoom**:
  - `Dolly in/out` = Physical camera translation through 3D space (creates parallax).
  - `Zoom in/out` = Lens focal length change only (no parallax shift).
- **Pan vs. Truck**:
  - `Pan left/right` = Camera rotates in place on its axis.
  - `Truck left/right` = Camera physically moves sideways on tracks.
- **Static Strictness**:
  - If a shot is labeled `static`, it must have **zero camera movement, zero focus change, zero zoom**.

### 3.2 Model Sweet-Spot Prompt Densities

| Video Model | Recommended Word Count | Optimization Focus |
|---|---|---|
| **Seedance 2.0 (Standard/Fast)** | 200–400 words (hero), 80–150 (inserts) | Native synced audio, director camera, dialogue lip-sync |
| **Wan 2.2** | 200–400 words | Long, descriptive natural language captions |
| **Sora 2 / VEO 3.1** | 100–250 words | Photoreal lighting, art movement, cinematic physics |
| **LTX-2** | ≤ 80 words | Tight, concise motion description (degrades past 80) |
| **Runway Gen-4** | ≤ 60 words | "Focus on motion, not appearance" |

---

## 🔍 4. Reference Video Analyst Workflow (`video-reference-analyst`)

When a user pastes a reference URL (YouTube, Shorts, Reel, TikTok) saying *"Make me something like this"*:

1. **Never guess or prompt-spam**: Extract transcript, frame count, pacing, and scene timestamps.
2. **Classify Motion Type**:
   - `motion_clip`: Full AI video generation (Seedance, Kling, Veo).
   - `animated_still`: High-resolution still + 2.5D virtual camera parallax/Ken Burns.
   - `hybrid`: Data graphics + footage.
3. **Canonical 5-Aspect Breakdown**: Deconstruct hero shots into the 5 aspects.
4. **Present 2–3 Differentiated Concepts**:
   - What we keep (pacing, hook structure, visual rhythm).
   - What we change (subject matter, narrative angle, unique forensic proof).
   - Itemized tool path and honest cost estimate before generating a single frame!

---

## 🎨 5. Taste Direction & Anti-Slop Contract (`taste-direction`)

Before generating assets or code:
1. **Define the Design Read**:
   - E.g.: *"Investigative national security exposé: forensic, clinical, high contrast, austere truth."*
   - Avoid vague fluff like "modern and clean".
2. **Set the 3 Quantitative Dials (1–10)**:
   - `visual_variance` (1 = tight repeating grammar, 10 = every scene a distinct visual world)
   - `motion_intensity` (1 = calm holds, 10 = fast kinetic directional changes)
   - `information_density` (1 = single hero stat, 10 = layered HUD fact ledger)
3. **Enforce Palette Discipline**:
   - Deep chromatic base (`#07090E`), 30% structural glass, 10% high-energy forensic accent.
   - Anti-pattern: NO generic AI purple gradients on flat black!

---

## 🎭 6. Composition: Atelier Mode vs. Templated Mode

OpenMontage supports two distinct composition approaches:
- **Templated Mode**: Assembles pre-existing scene blocks (`stat_card`, `text_card`, `chart`). Fast and reliable for quick drafts and localization variants.
- **Atelier Mode (Bespoke)**: Hand-authors the composition from scratch (`composition_mode: "atelier"`):
  - Bespoke HTML5 Canvas 2D / GSAP / WebGL / Remotion stage.
  - Disney 12 animation principles applied directly to code.
  - Distinctness test: *"Could this video belong to any other channel?"* If yes, refactor!

---

## 📋 7. The Reviewer Quality Protocol (CHAI 3-Axis Rules)

Every stage gets reviewed before human presentation:
1. **Accurate**: Every finding must cite an exact line number, artifact field, or frame timestamp.
2. **Complete**: Catch all occurrences of a failure pattern across the timeline, not just the first one.
3. **Constructive**: Every critical finding MUST include a concrete proposed fix.

---

## 🖥️ 8. Backlot Living Storyboard CLI

OpenMontage includes the **Backlot living storyboard** web server:
- Start and open the live board: `python -m backlot open <project-id>`
- Live library view: `python -m backlot open`
- Server mode: `python -m backlot serve --port 4750`
- Simulation demo: `python scripts/backlot_simulate_run.py`

The board updates in real time via SSE (Server-Sent Events) from `projects/<project-id>/` files, showing the screenplay view, scene contact sheets, takes, and approval gates.
