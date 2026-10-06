# Verified repositories for higher-detail video production

**Audit date:** 1 October 2026 · **Scope:** 20 selected repositories, not every video repository on the internet.

## Executive decision

For our next AI-image + 2D Short, retain the lightweight native Canvas route unless a specific visual requirement justifies another engine. Borrow better choreography and continuity first. Consider GSAP for timeline complexity, PixiJS for heavier layer/effect work, and Motion Canvas or HyperFrames for a tested authoring/render workflow. Remotion is an alternative stack, not an obligatory addition.

The improvement comes from asset preparation, shot direction and repeated rendered review—not from installing all of these libraries together.

## Verification method and limits

- GitHub repository metadata and README endpoints were fetched directly, rather than trusting search snippets or skill directories.
- All 20 repositories resolved successfully and their README snapshots were retained.
- Selected source/skill/licence files were retrieved; relevant implementation sections were inspected. This is **not a full source audit or a security review**.
- Source snapshots have API blob identifiers or recorded SHA-256 hashes where available in the manifests.
- No external install command or downloaded repository script was executed during this research. No runtime/performance benchmark of these libraries was performed.
- Our newly authored Python structural validator was executed and separately tested.
- Stars, claimed virality and promotional benchmark numbers are not used as quality evidence.
- Licence metadata is an initial signal, not legal clearance. Inspect the exact component, model, asset and shipped version before reuse.

## Shortlist

| # | Verified repository | Best role | Review level |
|---|---|---|---|
| 01 | https://github.com/heygen-com/hyperframes | HTML-first video framework | README + targeted source/skill/licence sections |
| 02 | https://github.com/motion-canvas/motion-canvas | 2D explanation choreography | README + targeted source/skill/licence sections |
| 03 | https://github.com/greensock/GSAP | Timeline, paths and property choreography | README + targeted source/skill/licence sections |
| 04 | https://github.com/pixijs/pixijs | GPU-accelerated 2D scene rendering | README + repository metadata |
| 05 | https://github.com/pixijs/filters | Selective 2D visual effects | README + targeted source/skill/licence sections |
| 06 | https://github.com/remotion-dev/skills | Official Remotion authoring guidance | README + targeted source/skill/licence sections |
| 07 | https://github.com/remotion-dev/remotion | React compositions and rendering | README + targeted source/skill/licence sections |
| 08 | https://github.com/apoorvlathey/motion-canvas-skills | Community Motion Canvas skill | README + targeted source/skill/licence sections |
| 09 | https://github.com/haidrrrry/claude-remotion-skill | Community motion craft checklist | README + targeted source/skill/licence sections |
| 10 | https://github.com/danielgatis/rembg | AI-image foreground preparation | README + repository metadata |
| 11 | https://github.com/facebookresearch/sam2 | Promptable image/video masks | README + repository metadata |
| 12 | https://github.com/m-bain/whisperX | Alignment and caption timing | README + targeted source/skill/licence sections |
| 13 | https://github.com/SYSTRAN/faster-whisper | Speech transcription/timestamp foundation | README + repository metadata |
| 14 | https://github.com/airbnb/lottie-web | Prepared vector animation playback | README + repository metadata |
| 15 | https://github.com/ManimCommunity/manim | Scientific and mathematical explanation | README + repository metadata |
| 16 | https://github.com/mrdoob/three.js | True 3D scenes when justified | README + repository metadata |
| 17 | https://github.com/theatre-js/theatre | Visual timeline/camera authoring | README + repository metadata |
| 18 | https://github.com/donmccurdy/glTF-Transform | 3D asset preparation/optimisation | README + repository metadata |
| 19 | https://github.com/microsoft/playwright | Browser automation and visual QA | README + repository metadata |
| 20 | https://github.com/FFmpeg/FFmpeg | Media assembly and objective inspection | README + targeted source/skill/licence sections |

## Repository-by-repository adoption notes

### 01. heygen-com/hyperframes

**Primary repository:** https://github.com/heygen-com/hyperframes

**Useful for:** HTML-first video framework.

**Take into our workflow:** Composition contract, asset readiness, seek-safe capture, continuity reasoning.

**Caution:** No runtime benchmark here. Do not adopt its rigid cut/style rules universally or treat repository guarantees as our measured performance.

**API licence signal:** `Apache-2.0`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/heygen-com__hyperframes__README.md`.

**Selected files retrieved, with relevant sections inspected:**
- `.agents/skills/motion-doctrine/SKILL.md` — https://github.com/heygen-com/hyperframes/blob/main/.agents/skills/motion-doctrine/SKILL.md
- `docs/concepts/determinism.mdx` — https://github.com/heygen-com/hyperframes/blob/main/docs/concepts/determinism.mdx

**Installation/runtime test in this task:** none.

### 02. motion-canvas/motion-canvas

**Primary repository:** https://github.com/motion-canvas/motion-canvas

**Useful for:** 2D explanation choreography.

**Take into our workflow:** Concurrent actions versus delayed starts; narration-oriented scene design.

**Caution:** Generator authoring needs its own runtime/reset/seek validation; not automatically our draw(t) architecture.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/motion-canvas__motion-canvas__README.md`.

**Selected files retrieved, with relevant sections inspected:**
- `packages/core/src/flow/all.ts` — https://github.com/motion-canvas/motion-canvas/blob/main/packages/core/src/flow/all.ts
- `packages/core/src/flow/sequence.ts` — https://github.com/motion-canvas/motion-canvas/blob/main/packages/core/src/flow/sequence.ts

**Installation/runtime test in this task:** none.

### 03. greensock/GSAP

**Primary repository:** https://github.com/greensock/GSAP

**Useful for:** Timeline, paths and property choreography.

**Take into our workflow:** Paused seekable timelines; deliberate timing and path transitions.

**Caution:** Standard custom no-charge licence, not automatically MIT. Callback-only state and event suppression need care.

**API licence signal:** `Not identified`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/greensock__GSAP__README.md`.

**Selected files retrieved, with relevant sections inspected:**
- `package.json` — https://github.com/greensock/GSAP/blob/master/package.json
- `src/gsap-core.js` — https://github.com/greensock/GSAP/blob/master/src/gsap-core.js

**Installation/runtime test in this task:** none.

### 04. pixijs/pixijs

**Primary repository:** https://github.com/pixijs/pixijs

**Useful for:** GPU-accelerated 2D scene rendering.

**Take into our workflow:** Masks, layered sprites, filters and controlled compositing.

**Caution:** Use only when needed. Replace free-running ticker updates with absolute-time evaluation during capture.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/pixijs__pixijs__README.md`.

**Installation/runtime test in this task:** none.

### 05. pixijs/filters

**Primary repository:** https://github.com/pixijs/filters

**Useful for:** Selective 2D visual effects.

**Take into our workflow:** Local shockwave origin/radius/decay; directional blur controls.

**Caution:** Match Pixi/filter major versions; image blur is not necessarily temporal motion blur or physical simulation.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/pixijs__filters__README.md`.

**Selected files retrieved, with relevant sections inspected:**
- `src/shockwave/ShockwaveFilter.ts` — https://github.com/pixijs/filters/blob/main/src/shockwave/ShockwaveFilter.ts
- `src/shockwave/shockwave.frag` — https://github.com/pixijs/filters/blob/main/src/shockwave/shockwave.frag
- `src/motion-blur/MotionBlurFilter.ts` — https://github.com/pixijs/filters/blob/main/src/motion-blur/MotionBlurFilter.ts

**Installation/runtime test in this task:** none.

### 06. remotion-dev/skills

**Primary repository:** https://github.com/remotion-dev/skills

**Useful for:** Official Remotion authoring guidance.

**Take into our workflow:** Frame timing, structured captions and supported blur approaches.

**Caution:** Documentation APIs can be version-specific. Repository licence metadata was not identified; do not infer the framework licence from this skill repository.

**API licence signal:** `Not identified`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/remotion-dev__skills__README.md`.

**Selected files retrieved, with relevant sections inspected:**
- `skills/remotion-best-practices/SKILL.md` — https://github.com/remotion-dev/skills/blob/main/skills/remotion-best-practices/SKILL.md
- `skills/remotion-markup/timing.md` — https://github.com/remotion-dev/skills/blob/main/skills/remotion-markup/timing.md
- `skills/remotion-captions/display-captions.md` — https://github.com/remotion-dev/skills/blob/main/skills/remotion-captions/display-captions.md
- `skills/remotion-markup/motion-blur.md` — https://github.com/remotion-dev/skills/blob/main/skills/remotion-markup/motion-blur.md

**Installation/runtime test in this task:** none.

### 07. remotion-dev/remotion

**Primary repository:** https://github.com/remotion-dev/remotion

**Useful for:** React compositions and rendering.

**Take into our workflow:** Reusable compositions and a structured video toolchain.

**Caution:** Custom Remotion licence, not MIT; inspect eligibility and current terms before adoption.

**API licence signal:** `NOASSERTION`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/remotion-dev__remotion__README.md`.

**Selected files retrieved, with relevant sections inspected:**
- `LICENSE.md` — https://github.com/remotion-dev/remotion/blob/main/LICENSE.md

**Installation/runtime test in this task:** none.

### 08. apoorvlathey/motion-canvas-skills

**Primary repository:** https://github.com/apoorvlathey/motion-canvas-skills

**Useful for:** Community Motion Canvas skill.

**Take into our workflow:** Concise guidance for refs, signals, all/sequence and scenes.

**Caution:** A third-party instruction guide, not the official renderer or evidence of output quality.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/apoorvlathey__motion-canvas-skills__README.md`.

**Selected files retrieved, with relevant sections inspected:**
- `SKILL.md` — https://github.com/apoorvlathey/motion-canvas-skills/blob/main/SKILL.md

**Installation/runtime test in this task:** none.

### 09. haidrrrry/claude-remotion-skill

**Primary repository:** https://github.com/haidrrrry/claude-remotion-skill

**Useful for:** Community motion craft checklist.

**Take into our workflow:** Render–inspect–fix loop, theme consistency and deliberate exits.

**Caution:** Reject universal Ken Burns, idle breathing and never-linear rules. Its README simplification of Remotion licensing does not override the actual licence.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/haidrrrry__claude-remotion-skill__README.md`.

**Selected files retrieved, with relevant sections inspected:**
- `remotion-motion-graphics/SKILL.md` — https://github.com/haidrrrry/claude-remotion-skill/blob/main/remotion-motion-graphics/SKILL.md

**Installation/runtime test in this task:** none.

### 10. danielgatis/rembg

**Primary repository:** https://github.com/danielgatis/rembg

**Useful for:** AI-image foreground preparation.

**Take into our workflow:** Subject/background separation as a preprocessing stage.

**Caution:** Code is MIT; model weights have separate terms. The inspected README identifies a default model with commercial-use restrictions. Inspect masks and choose the model explicitly.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/danielgatis__rembg__README.md`.

**Installation/runtime test in this task:** none.

### 11. facebookresearch/sam2

**Primary repository:** https://github.com/facebookresearch/sam2

**Useful for:** Promptable image/video masks.

**Take into our workflow:** Foreground selection and region-based compositing preparation.

**Caution:** Large dependencies/model downloads and hardware considerations; not installed or benchmarked. A mask does not fill the missing background.

**API licence signal:** `Apache-2.0`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/facebookresearch__sam2__README.md`.

**Installation/runtime test in this task:** none.

### 12. m-bain/whisperX

**Primary repository:** https://github.com/m-bain/whisperX

**Useful for:** Alignment and caption timing.

**Take into our workflow:** Forced-alignment workflow and language-specific models.

**Caution:** Numbers, unsupported tokens, overlap and mixed-language speech need review. Hindi model mapping exists in inspected source; Hinglish accuracy remains untested.

**API licence signal:** `BSD-2-Clause`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/m-bain__whisperX__README.md`.

**Selected files retrieved, with relevant sections inspected:**
- `whisperx/alignment.py` — https://github.com/m-bain/whisperX/blob/main/whisperx/alignment.py

**Installation/runtime test in this task:** none.

### 13. SYSTRAN/faster-whisper

**Primary repository:** https://github.com/SYSTRAN/faster-whisper

**Useful for:** Speech transcription/timestamp foundation.

**Take into our workflow:** Local transcription options and word timestamps.

**Caution:** README benchmark claims are not measurements on our sandbox. Transcript/timestamps still require editorial review.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/SYSTRAN__faster-whisper__README.md`.

**Installation/runtime test in this task:** none.

### 14. airbnb/lottie-web

**Primary repository:** https://github.com/airbnb/lottie-web

**Useful for:** Prepared vector animation playback.

**Take into our workflow:** Seekable vector motifs and controllable playback.

**Caution:** Validate supported effects and individual asset licences; embed dependent images/fonts for offline use.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/airbnb__lottie-web__README.md`.

**Installation/runtime test in this task:** none.

### 15. ManimCommunity/manim

**Primary repository:** https://github.com/ManimCommunity/manim

**Useful for:** Scientific and mathematical explanation.

**Take into our workflow:** Precise diagrams, transformations and explanatory mechanisms.

**Caution:** Usually a specialist rendered component, not an automatic self-contained editable HTML replacement.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/ManimCommunity__manim__README.md`.

**Installation/runtime test in this task:** none.

### 16. mrdoob/three.js

**Primary repository:** https://github.com/mrdoob/three.js

**Useful for:** True 3D scenes when justified.

**Take into our workflow:** Shared cameras, materials, geometry and environments.

**Caution:** Do not add 3D to a better 2D explanation just for prestige. Pin matching addons and inspect assets.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/mrdoob__three.js__README.md`.

**Installation/runtime test in this task:** none.

### 17. theatre-js/theatre

**Primary repository:** https://github.com/theatre-js/theatre

**Useful for:** Visual timeline/camera authoring.

**Take into our workflow:** Nuanced property tracks and authored camera movement.

**Caution:** Core Apache-2.0 versus Studio AGPL-3.0 in the inspected README. README also notes development moved temporarily private; do not infer public release readiness.

**API licence signal:** `Apache-2.0`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/theatre-js__theatre__README.md`.

**Installation/runtime test in this task:** none.

### 18. donmccurdy/glTF-Transform

**Primary repository:** https://github.com/donmccurdy/glTF-Transform

**Useful for:** 3D asset preparation/optimisation.

**Take into our workflow:** Reproducible glTF edits and packaging/optimisation.

**Caution:** Optimisation is not modelling. Some operations are lossy; compare before/after and package any decoder offline.

**API licence signal:** `MIT`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/donmccurdy__glTF-Transform__README.md`.

**Installation/runtime test in this task:** none.

### 19. microsoft/playwright

**Primary repository:** https://github.com/microsoft/playwright

**Useful for:** Browser automation and visual QA.

**Take into our workflow:** Readiness checks, controlled capture, playback tests and frame inspection.

**Caution:** Automation cannot judge art direction or replace watching/listening; browser/font versions affect reproducibility.

**API licence signal:** `Apache-2.0`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/microsoft__playwright__README.md`.

**Installation/runtime test in this task:** none.

### 20. FFmpeg/FFmpeg

**Primary repository:** https://github.com/FFmpeg/FFmpeg

**Useful for:** Media assembly and objective inspection.

**Take into our workflow:** Encoding, frame extraction, waveform/loudness analysis and probing.

**Caution:** Licence depends on build options and linked libraries. Rendering success alone does not prove visual or editorial quality.

**API licence signal:** `NOASSERTION`; **archived flag at check:** `False`. An unarchived repository is not, by itself, proof of active maintenance.

**Saved README:** `source_snapshots/FFmpeg__FFmpeg__README.md`.

**Selected files retrieved, with relevant sections inspected:**
- `LICENSE.md` — https://github.com/FFmpeg/FFmpeg/blob/master/LICENSE.md

**Installation/runtime test in this task:** none.

## Findings that change our practice

### A. Skill instructions can conflict with actual craft
The community Remotion skill's rule to make every still zoom and every idle object breathe is not adopted. Motion Canvas's distinction between concurrent and staggered tasks is more useful than blindly staggering every event. HyperFrames's continuity principles are adopted selectively; hard cuts and purposeful stillness remain valid.

### B. Read code when the distinction matters
- Motion Canvas `all()` joins concurrent tasks; `sequence()` delays their starts rather than waiting for each to finish.
- GSAP `seek()` uses timeline time and event-suppression behaviour. Avoid relying on callback side effects to establish export state.
- Pixi's shockwave shader has a centre, time-driven radius, spatial band and decay. That supports a controlled visual effect, not a scientific pressure solver.
- WhisperX includes a Hindi alignment mapping, but that does not validate code-switched narration.

### C. Licence traps are real
- Remotion has its own eligibility/commercial licence, despite simplified community descriptions calling it free/open source.
- GSAP uses its standard licence; no-charge commercial availability is not the same thing as MIT permission for every redistribution or competing-tool use.
- Theatre core and authoring Studio have different licences.
- rembg code and the chosen model weights have independent licences.
- FFmpeg's licence depends on the compiled configuration and external libraries.
- Lottie/model/image/font assets still require their own rights checks.

### D. Version compatibility matters
The inspected Pixi filters README maps Pixi v8 to filters v6, v7 to v5, v6 to v4 and v5 to v3. Pin compatible versions rather than independently installing “latest.” Remotion blur examples describe specific version/browser support; do not assume they work in an older project.

### E. A real repository is not a tested integration
Existence and useful source code justify a candidate—not a promise of immediate improvement, speed or compatibility. Run a small project-specific proof before committing to a new dependency.

## Concrete next-production priorities

1. Better shot cards and one internally reviewed hero proof.
2. Layer-aware AI image preparation where the scene benefits.
3. Primary action plus coherent secondary response, not arbitrary decoration.
4. Causal, bounded effects and deliberate shot handoffs.
5. Optional reviewed word-level captions, never fabricated timings.
6. More rigorous scene-boundary and motion review.
7. Native Canvas remains valid; introduce a new renderer only for a visible benefit.

## Reusable files created

- `../../SKILLS_PEAK_DETAIL.md` — current production skill.
- `../../.agents/skills/benaqaab-peak-detail/SKILL.md` — compact agent-loadable entry.
- `../../tools/peak_detail_gate.py` — structural plan validator.
- `../../tools/test_peak_detail_gate.py` — 16 standard-library tests.
- `EXAMPLE_DETAIL_PLAN.json` — proposed six-second proof plan referencing an existing illustrative asset; not a rendered remake.
- `EXAMPLE_GATE_RESULT.json` — example structural result.
- `GATE_TEST_RESULTS.txt` — executed test report.

From the workspace root:

```bash
python tools/peak_detail_gate.py knowledge/peak_detail_research/EXAMPLE_DETAIL_PLAN.json --root .
python tools/test_peak_detail_gate.py
```

The gate checks planning completeness, timing coverage, references and asset paths. It explicitly reports visual quality as **NOT ASSESSED**, factual accuracy as **NOT VERIFIED** and licence validity as **NOT VERIFIED**.

## Traceability and one corrected lookup

`REPO_AUDIT.json` records repository/README verification. `SOURCE_INSPECTION.json` records individual retrievals and hashes. The initial guess of a root `SKILL.md` in `haidrrrry/claude-remotion-skill` returned 404; the tree revealed the actual file at `remotion-motion-graphics/SKILL.md`, which was retrieved successfully. This was a path correction, not evidence that the repository was fake.

Downloaded third-party instructions remain reference material. They are not automatically trusted, executed or installed into the agent.
