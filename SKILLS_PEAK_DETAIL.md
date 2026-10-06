# Benaqaab India — Peak Detail Video Production Skill

**Version 1.0 · 1 October 2026**  
**Standing preference:** The user explicitly asked for substantially deeper detailing and better execution in every future video, with genuine repository research and stronger production skills.

**Read with:** `MASTER_VIDEO_GENERATION_SKILLS.md`. This document adds a stronger production standard; it does not reinstate superseded theme, music, presenter or duration restrictions.

> Peak detail means intentional, coherent and demonstrably better work. It does not mean maximum particles, maximum text, constant camera movement or importing the most libraries. An elegant, restrained scene can be more detailed in its thinking than a crowded scene.

## 1. What has actually been done

- Verified 20 repository identities and retrieved their READMEs directly through GitHub's API.
- Retrieved selected implementation, skill and licence files; inspected relevant sections, not entire codebases.
- Saved the audit, source paths and snapshots in `knowledge/peak_detail_research/`.
- Wrote this original, channel-specific production skill rather than automatically accepting third-party instructions.
- Added a reusable preproduction-plan validator and tests, whose structural scope is documented separately.

**Not done:** no full installation or runtime benchmark of all 20 repositories; no new video remake in this research task; no proof that merely reading repositories improves every future output; no permanent modification to an underlying model. Actual improvement must be demonstrated in rendered work.

## 2. The default approach for the next video

### 2.1 Plan more deeply without burdening the user

Internally develop three approaches:

1. **Mechanism:** the object or process visibly explains itself.
2. **Journey:** the camera or a recurring subject connects places, scales or consequences.
3. **Evidence/reveal:** a comparison or real document changes the interpretation.

Choose one strong approach and explain the choice briefly. Do not ask for three new approvals unless the brief is materially ambiguous. Preserve the HTML-first approval gate before the full final MP4.

### 2.2 Establish the quality target before scaling

Build a representative five-to-eight-second hero proof internally: the most demanding asset, camera, compositing and sound combination. Inspect it at final resolution and phone size. Fix the visual language there before replicating it across a long film.

A hero proof is a production technique, not necessarily a separate deliverable or additional user-approval gate.

### 2.3 Give every shot an authored purpose

Before coding, record:

- the question the shot answers;
- what the audience sees first;
- what changes and why;
- its final composition;
- the primary action and secondary reaction;
- the camera or composition movement, including an intentional hold;
- AI asset role and masking requirements;
- visual contact, reflection or occlusion requirements;
- exact text/claim and evidence source;
- audio event or intentional quiet;
- the handoff to the next shot;
- a concrete visual acceptance test.

This prevents a collection of attractive but unrelated scenes.

## 3. The eight detail passes

Run these passes on each important shot. An item may be deliberately unnecessary; document why rather than adding it automatically.

### Pass 1 — Editorial truth

- Is the displayed claim actually supported?
- Are date, unit, denominator and geographic scope correct?
- Are reconstructions and schematics labelled?
- Are temperature, total energy, pressure, speed and distance being confused?
- Does the image imply a real event or real person that the evidence does not establish?

Example: lightning-channel air versus the Sun's photosphere, not lightning versus the solar core. No attractive animation compensates for a wrong comparison.

### Pass 2 — Composition and hierarchy

- One obvious focal subject, with subordinate supporting graphics.
- Planned negative space for labels; no shrinking text to rescue a crowded layout.
- Full subject silhouette checked at start, middle and end.
- Phone-readable key information, including important caveats.
- Critical objects/captions protected from platform interface overlays.
- Brand identifiers remain subordinate to the story.

A paragraph of typography is not the subject merely because it is animated.

### Pass 3 — Asset and image craft

- Assign each image a job: environment, isolated subject, texture, evidence or illustration.
- Generate coherent reference views and compatible light direction.
- Use separate foreground/hero/background layers when the camera requires them.
- Inspect masks at 100%: halos, missing fingers, transparent windows, hair and hard-edge contamination.
- Prepare the background behind a cut-out before introducing parallax.
- Keep exact text, numbers and charts out of generated imagery; composite them separately.
- Do not pretend depth exists where a single image has no hidden-surface information.

### Pass 4 — Meaningful primary motion

The primary action must express the sentence: fluid moves through a pipe, pressure expands, a route reaches a chokepoint, a comparison reveals a gap.

Write its trajectory, timing and final state. Choose easing according to behaviour: constant speed, acceleration, impact, spring return or a deliberate stop. Never apply spring easing to every physical process by habit.

### Pass 5 — Secondary motion and physical coherence

Choose only relevant secondary cues:

- an object stops and a strap or liquid settles;
- a shock/pressure effect radiates from the same origin as its cause;
- particles respond to the depicted process;
- a foreground element occludes a moving subject;
- a light source changes nearby surfaces coherently;
- a ship's wake follows its current transform;
- a tracked annotation follows the actual subject.

Do not add idle sine-wave wobble simply to avoid a still frame. An intentional quiet hold is valid.

### Pass 6 — Transition and continuity

Use a limited transition vocabulary appropriate to the story. At each boundary choose one:

- match the subject or graphic carrier;
- continue a motion vector;
- reveal a deeper scale of the same object;
- cut deliberately to evidence, geography or consequence;
- use a motivated dissolve or hold.

For a matched-motion seam, inspect outgoing and incoming position, direction and speed. Do not impose that test on a deliberately unrelated hard cut. A change to narration timing reopens the adjacent seams for review.

### Pass 7 — Sound and speech

- Start from measured narration, not guessed speech speed.
- Match accents to visible actions and semantic reveals.
- Separate voice, ambience, movement, transition and music stems where practical.
- Use quiet as a deliberate choice.
- Check a phone-speaker-like mix and the final encoded audio where possible.
- Measure loudness and peaks; never invent a listening or measurement result.
- If word-synced captions are requested, align and manually review names, numbers and Hinglish code-switching.

### Pass 8 — Finish and performance

- Apply colour treatment coherently across plates, objects and graphics.
- Add local effects selectively; keep explanatory text sharp.
- Check mask edges, gradient banding, blur clipping and texture scale.
- Test final-resolution rendering, not only a reduced preview.
- Separate preview performance from final export correctness.
- Preserve deterministic seeking and offline delivery.

## 4. Repository selection: use the smallest suitable stack

### 4.1 Default for our editable HTML Shorts

**Keep native Canvas 2D where it can meet the look.** It already delivers simple offline playback and predictable frame evaluation. Improve the shot design rather than replacing the engine reflexively.

Add **GSAP** when explicit timeline choreography, path work or SVG morphing materially reduces complexity. Use a paused timeline evaluated at the requested time; do not let a wall-clock ticker determine export state. Verify the current standard licence and any distribution restrictions before bundling.

Use **PixiJS + matching Pixi filters** when layer count, masks or selective effects exceed the practical Canvas implementation. Their compatibility matrix matters. This is an alternative rendering layer, not an instruction to mix every engine together.

### 4.2 Visual explanation and richer authoring

Study **Motion Canvas** for concurrent, staggered and narration-oriented scene choreography. Use its runtime/editor only when the workflow fits. Generator-based animation is not automatically a drop-in pure `draw(t)` function; test arbitrary seeking and export behaviour.

Consider **HyperFrames** for its HTML composition/rendering contract and seekable adapters. Its repository is verified, and selected determinism/motion material was inspected. It has not been installed or benchmarked in this research task; do not promise our current HTML is already a HyperFrames project.

Use **Remotion** when React-based reusable compositions and its rendering ecosystem justify the larger stack. Check its current licence. Remotion guidance is useful even when no migration is necessary.

### 4.3 Optional specialists

- **rembg / SAM 2:** cutouts and masks. Inspect edges and model-specific rights; they do not create the missing background.
- **WhisperX / faster-whisper:** transcript/timing workflows. Mixed-language alignment needs manual checks and model availability.
- **Manim:** precise mathematical and scientific mechanism sequences; usually a specialist baked component, not a standalone-HTML replacement.
- **Lottie-web:** prepared vector animation assets. Validate renderer support and the rights of the individual animation.
- **Three.js / Theatre.js / glTF Transform:** only when true 3D, richer camera authoring or asset optimisation is justified.
- **Playwright / FFmpeg:** controlled capture, media inspection and QA. Automated checks cannot certify cinematic quality.

Full repository audit: `knowledge/peak_detail_research/VERIFIED_REPOSITORIES.md`.

## 5. Specific techniques learned from inspected material

### 5.1 Concurrency is not staggering

Motion Canvas's inspected `all()` starts tasks concurrently and joins them. Its `sequence()` starts tasks at a constant delay; it does not wait for each previous task to finish before beginning the next.

**Adoption:** distinguish a simultaneous physical cause, a staggered explanatory reveal and a true sequential dependency. Do not add stagger where events should occur together.

### 5.2 Seekable timelines require explicit state

The inspected GSAP `seek()` routes through timeline total time with event-suppression behaviour. State mutations performed only inside callbacks can therefore become a trap for export seeking.

**Adoption:** timeline-driven properties or explicit state evaluation should determine the image. Do not make render correctness depend on whether a callback happened during previous playback.

### 5.3 Effects have an origin, radius and lifetime

The inspected Pixi shockwave fragment shader applies a local radial displacement around a centre, computes radius from time/speed and fades toward a maximum radius.

**Adoption:** anchor effects to a causal source, limit their spatial extent and decay them. Keep them off labels. A shockwave filter is a visual treatment, not a physically validated pressure simulation.

### 5.4 Not all motion blur is temporal integration

The inspected Pixi motion-blur code uses direction/velocity and kernel settings. The inspected Remotion guidance describes fractional-frame sampling and averaging for an available component, with version/browser requirements.

**Adoption:** distinguish directional image blur from exposure integration. Use either only after checking it at the actual motion speed. Pin supported versions; do not blindly paste a recently changed API into the existing engine.

### 5.5 Fonts and asset readiness are part of quality

HyperFrames's determinism documentation requires fixed time/size and assets resolved before capture. It distinguishes preview speed from seek-driven export.

**Adoption:** pre-load Devanagari/Latin fonts, finish image/video decoding, keep randomness seeded, and commit frames only after asynchronous dependencies are settled. A requestAnimationFrame preview loop is acceptable if it merely displays an externally determined time; it must not be the export clock.

### 5.6 Captions are editorial data

Inspected Remotion caption guidance treats text, start/end timestamps and whitespace as structured data. WhisperX's inspected alignment source contains a Hindi model mapping, but its README documents vocabulary, number, overlap and language-model limitations.

**Adoption:** preserve token spacing, align against approved speech and manually review code-switching. Availability of a Hindi model is not proof of accurate Hinglish word timing.

## 6. What we explicitly reject from some third-party skills

The inspected community Remotion skill includes absolute rules such as no linear interpolation, Ken Burns on every still and idle breathing. Its render–inspect–fix loop is useful; those universal style rules are not adopted.

The inspected HyperFrames motion doctrine contains useful continuity guidance but also strong restrictions against certain cuts/dissolves. Those are house rules for that approach, not universal laws of filmmaking.

One internal tension was noticed in that doctrine: it warns that the incoming scene must not visibly fight an established zoom direction during its entry, yet its timed entry effects can themselves include a scale component. On re-reading, this is less a contradiction than a scoping rule — the ban applies to the scene’s *own* entrance animation, not to the matched physical carrier object that crosses the seam (a container that docks, a mark that flies into its slot, a cursor mid-path), which is expected to continue the outgoing zoom at matched speed. With that reading, the principle is: **match the carrier; let the surrounding content settle naturally.**

Also noted: it states the exit should be roughly 75 percent of the entry duration, while its cut-the-curve technique inverts that relationship (entry roughly 127 percent of exit) for action-continuity cuts. So a film using both techniques across different seams would need to record which rule governs each seam rather than applying “exit is always shorter” globally.

Both observations are recorded here rather than silently imported into our workflow.

Our rules:

- Constant-speed light/sound paths can be linear when the explanatory model needs them.
- A clean flat diagram can be better than a mandatory mesh gradient.
- A static evidence hold can be better than a forced camera push.
- A hard cut can be the clearest editorial choice.
- A physical event may require simultaneous effects rather than staggering everything.
- More grain, more glow and more micro-motion do not automatically mean more quality.
- No skill repository may override the current user brief, factual integrity, rights or safety requirements.

## 7. AI imagery: the higher-detail production method

### Before generation

Write an asset card with subject identity, perspective, light direction, palette, desired negative space, scale, crop margin, layer role and prohibited errors. Define which features must match across shots.

### During preparation

1. Select the strongest generated plate rather than accepting every first result.
2. Inspect anatomy, architecture, reflections, horizon and material scale.
3. Extract a subject or foreground only when it helps the shot.
4. Inspect the mask on both light and dark backgrounds.
5. Prepare missing background regions; limit parallax if reconstruction is weak.
6. Keep colour/light adjustments compatible across layers.
7. Save the original, prepared layer, mask and provenance separately.

### During animation

- Move layers according to depth rather than applying the same zoom everywhere.
- Use local deformation only on suitable regions: a cloud, fabric, water or heat area.
- Keep a rigid subject rigid unless articulation is actually modelled.
- Match animated rain, smoke or particles to the environment's scale and wind.
- Avoid excessive camera translation exposing unpainted edges.
- Let graphics act on the subject rather than float above it arbitrarily.

### Licensing caution discovered in this audit

The retrieved rembg README distinguishes its MIT code licence from model-weight licences, and identifies a default model with separate commercial-use terms. Therefore, never assume `pip install rembg` automatically gives commercial permission for whichever model it downloads. Select and review the actual model explicitly.

## 8. A stronger shot-detail card

```json
{
  "id": "pressure_wave",
  "start": 12.36,
  "end": 18.99,
  "purpose": "Explain why lightning produces thunder",
  "hero": "A clearly labelled magnified channel of air",
  "start_state": "Cool, closely spaced schematic air particles",
  "end_state": "Expanded air with a decaying outward pressure front",
  "primary_motion": "One heating event causes an outward expansion",
  "secondary_motion": "Small local particle responses, not arbitrary whole-scene wobble",
  "camera": "Stable explanatory framing",
  "asset_roles": ["AI storm is atmospheric context, not evidence"],
  "detail_choices": ["Protected diagram boundary", "Consistent wave origin", "Sharp captions"],
  "claims": ["thunder_mechanism"],
  "audio": "A restrained low transient follows the heating cue",
  "transition": "Motivated cut to the light-versus-sound comparison",
  "acceptance": "The mechanism remains understandable with narration muted"
}
```

This is a planning example, not a claim that an upgraded pressure-wave scene has already been rendered.

## 9. Quality gates for every future delivery

### Gate A — Preproduction completeness

Run `tools/peak_detail_gate.py` on a plan using the supplied schema/example. It checks required fields, references, timing coverage, claimed units and local asset paths. It does not judge beauty or verify scientific truth.

### Gate B — Frame craft

Inspect first/middle/final frames of every shot and both sides of important transitions. Include at least one full-resolution hero frame and a realistic mobile-scale preview.

Fail for unreadable essential information, malformed hero assets, accidental crops, distracting mask edges, poor contact, inconsistent light or broken source claims.

### Gate C — Moving result

Inspect actual motion at intended speed when available. Review rapid moves and slow holds, not just selected attractive stills. If only motion samples were inspected, report exactly that.

Check event causality, speed, changes in direction, transition continuity, waveform/rain/particle origins and end-state readability.

### Gate D — Sound

Measure real durations and peaks/loudness as appropriate. Test Play, seek, mute and ending behaviour. Listen through the actual mix when a listening path is available. Do not substitute metadata for an audio review or claim listening that did not occur.

### Gate E — Determinism and delivery

- Out-of-order seek checks in each visual mode.
- Asset/font readiness and browser error checks.
- Fixed dimensions, frame rate and duration.
- Final-resolution export smoke test.
- Portable local paths and embedded dependencies.
- Licence/model review.
- Preserved prior accepted version.
- HTML approval before full final MP4 unless the current request says otherwise.

### Gate F — Harsh director pass

Name the three worst problems, with timestamps and observable evidence. Fix the highest-impact problem first. Re-test affected frames and seams. Do not merely add embellishment while a framing or factual defect remains.

## 10. Review rubric: descriptive, not a fake quality guarantee

For each category, record **needs revision / acceptable / strong**, with a reason:

- narrative clarity;
- visual specificity;
- hero/image quality;
- composition and mobile readability;
- motion causality and timing;
- continuity;
- sound and speech intelligibility;
- factual/representational integrity;
- technical reproducibility.

Any factual, rights, essential-readability or broken-export failure blocks delivery. Strong scores elsewhere cannot compensate. User taste still determines acceptance; there is no mathematical guarantee of “cinematic” or “viral.”

## 11. Practical improvement plan for our lightning-style Shorts

Use these selectively in the next appropriate film, not as an unrequested remake:

| Existing baseline | Higher-detail direction | Proof required |
|---|---|---|
| One storm plate | Prepared cloud/foreground layers with modest parallax | No exposed holes, masks or mismatched light |
| Clean vector bolt | More organically varied branch hierarchy and a coherent local light response | Readable silhouette without repetitive flashing |
| Simple radial particles | Better staged heating, local response and decaying wave front | Mechanism clear, schematic limitations stated |
| Two schematic travel lines | A single shared-event staging with precise narration handoffs | No implication of two unrelated events |
| Scene-summary captions | Optional reviewed word-level captions when requested | Names, numbers and Hinglish alignment checked |
| Repeated transition treatment | Chosen carrier/match-cut plus deliberate quiet cuts | Better continuity, not arbitrary variation |
| Basic audio bed | More scene-specific ambience and clearer dynamic contrast | Narration stays dominant; no clipping |
| Checkpoint QA | Boundary checks plus longer motion review | Report exact scope, not exaggerated full-film verification |

## 12. Definition of done

A future video is ready to show when:

1. It answers the intended question with verified claims.
2. Its hero assets and image preparation survive a paused close inspection.
3. Its motion explains or directs, rather than merely decorating.
4. Its scenes belong to one visual world or use justified contrasts.
5. Its graphics and captions remain readable on a phone.
6. Its sound supports comprehension.
7. Its output is editable, reproducible and honestly labelled.
8. Its actual rendered result—not only the code—has been reviewed.
9. The delivery clearly distinguishes completed work, test scope and limitations.

## 13. Reuse prompt

```text
Apply Benaqaab India's Peak Detail skill to this video.
Read the latest user brief, SKILLS_PEAK_DETAIL.md and the relevant master chapters.
Develop three approaches internally and choose the strongest explanatory one.
Plan each shot's purpose, start/end states, asset roles, motion, sound and acceptance test.
Build a representative hero proof before scaling the look.
Use the smallest appropriate rendering stack; do not import libraries for prestige.
Prepare AI imagery as purposeful layers when needed, not generic zooming backgrounds.
Use meaningful primary and secondary motion, coherent light/contact, crisp graphics
and measured narration timing. Review actual rendered frames and motion.
Name and fix the three worst problems before delivery.
Preserve editable offline HTML and the approval gate for the full final MP4.
Report implementation and verification honestly; never claim untested integrations.
```

## 14. Files and maintenance

- Skill: `SKILLS_PEAK_DETAIL.md`
- Agent-loadable entry: `.agents/skills/benaqaab-peak-detail/SKILL.md`
- Verified repository report: `knowledge/peak_detail_research/VERIFIED_REPOSITORIES.md`
- Raw verification records: `REPO_AUDIT.json`, `SOURCE_INSPECTION.json`
- Selected primary-source snapshots: `source_snapshots/`
- Structural plan validator: `tools/peak_detail_gate.py`
- Example plan and test results: `knowledge/peak_detail_research/`

Update this skill after demonstrated project results and explicit feedback. Keep proposed techniques separate from tested implementations. Recheck licences, API compatibility and model requirements before adoption.
