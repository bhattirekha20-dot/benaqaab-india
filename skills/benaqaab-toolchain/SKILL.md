---
name: benaqaab-toolchain
description: >-
  Automation and script generation for After Effects (ExtendScript JSX scripts, shape/camera/text animator expressions)
  and CapCut / Alight Motion (automated XML/JSON draft project generators, transition/effect catalogue data).
---

# 🛠️ Benaqaab Automated Toolchain & Motion Scripting

## 1. Adobe After Effects Automation (ExtendScript & Expressions)
- **Generation:** Generates pure `.jsx` ExtendScript files to automate After Effects project creation, layer setup, shape morphing, text animators, and 3D camera motion rigs.
- **Expressions:** Production-ready inertia bounce, wiggle decay, smooth dampening, and layer index staggers.

## 2. CapCut & Alight Motion Project Automation
- **CapCut Draft API (`tools/capcut_draft.py`):** Programmatically constructs valid `draft_content.json` projects, inserting video tracks, audio stems, text overlays, and keyframe animations.
- **Alight Motion XML Generator (`tools/alight_project.py`):** Compiles project XML definitions matching mobile motion parameters.
- **Full Catalogues (`tools/data/`):** Complete parsed JSON databases of official transitions, scene effects, character effects, filters, video intros, and outros.

## 3. Peak Detail Quality Gate (`tools/peak_detail_gate.py`)
- Automated validation script verifying shot breakdown schemas, timing continuity, asset resolution, and audio loudness compliance before final rendering.
