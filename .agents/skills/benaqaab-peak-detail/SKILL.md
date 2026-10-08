---
name: benaqaab-peak-detail
description: >-
  Apply peak detail production standards to Benaqaab India videos, Shorts, AI composites, and 2D/3D motion graphics.
  Enforces intentional shot breakdowns, purpose-driven hero states, causal motion, and the 3-worst-problems fix loop.
---

# 🔍 Benaqaab Peak Detail Video Production System

## 1. Core Philosophy: Restrained & Intentional Detail
- **Detail does NOT mean clutter:** Maximum particles, excessive text, or constant camera shakes do not equal quality. An elegant, restrained scene with thoughtful composition is vastly superior to a crowded, messy scene.
- **Causal Motion:** Motion must have a clear cause and purpose. Physics, momentum, and intention guide every translation and scale. Intentional stillness, constant speed holds, and clean hard cuts are actively encouraged.
- **Single Source of Truth:** Scene specifications drive both the interactive HTML preview and the final MP4 render.

## 2. 9-Point Shot Planning Framework
Every single shot must explicitly define:
1. **Purpose:** Why does this shot exist in the narrative arc?
2. **Hero Subject:** What is the single focal point the viewer's eye must track?
3. **Start & End States:** Exact visual coordinates, opacity, scale, and camera framing at frame 0 vs final frame.
4. **Motion Vector:** Velocity curve, easing (e.g. cubic-bezier(0.16, 1, 0.3, 1)), direction, and duration.
5. **Asset Roles:** What is background, midground, foreground, and HUD/overlay.
6. **Sound Cues:** Specific SFX triggers synced to visual impact (whoosh, click, slam, riser).
7. **Sources & Evidence:** Real-world document citations, dates, or data points.
8. **Acceptance Test:** What exact visual check confirms this shot succeeded?
9. **Cognitive Load:** Keep text readable; never place more than 1 main idea per 3-5 seconds.

## 3. The 3-Worst-Problems Fix Loop
- After generating or previewing any scene proof, identify and eliminate the three most glaring visual/timing defects before touching minor polishes.
- Always present HTML proof to the user before initiating full MP4 rendering.
