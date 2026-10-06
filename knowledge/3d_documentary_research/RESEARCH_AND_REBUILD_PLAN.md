# Why the previous 3D documentary missed the mark
## Reference research and a practical rebuild plan
**Benaqaab India · 1 October 2026**

> **Main conclusion:** The missing ingredient was not a darker theme or more motion. It was coherent scene construction and shot direction. A 3D aircraft pasted over a moving image is not the same thing as an aircraft photographed by a camera inside a believable environment.

This document separates **observed evidence**, **documented production techniques**, and **recommendations for our next build**. It is a research deliverable, not a claim that the previous documentary has already been upgraded.

---

## 1. What was actually researched

- Read studio case studies, technical articles and the official Three.js manuals.
- Retrieved the published **54-second Lusion Gemini showcase recording**, extracted frames at **3, 13, 25, 38 and 48 seconds**, and visually inspected them. These are timestamps in the showcase recording, not universal timestamps in the interactive demo.
- Reviewed the available transcript, chapter markers and public storyboard sheets from **TomsProject’s Blender documentary-scene tutorial**. Inspected the opening examples and the approximately 10:30–11:10 scene-building/animation storyboard. This is a third-party tutorial, **not an official Fern production breakdown**.
- Audited the existing `projects/usa_iran_full/documentary.js` against these findings.
- Did **not** watch every reference end-to-end, benchmark every live site, or verify Fern/Neo’s internal software stack. Reddit speculation and promotional claims that these channels are simply AI-generated were not treated as evidence.

## 2. References worth studying

### A. Lusion — Gemini: vehicle rendering and camera presentation
**Try:** https://exp-gemini.lusion.co/

The showcase identifies this as a Three.js vehicle experience with two visual modes, slow-motion interaction and a GSAP-driven HUD. [1](https://www.webgpu.com/showcase/gemini-webgl-car-demo-lusion/)

**What the inspected frames show:**
- At 3 seconds: a three-quarter vehicle view, a ground plane, soft contact shading and restrained peripheral graphics.
- At 13 seconds: a rear-quarter view and warm lighting that describes the vehicle’s edges.
- At 25 seconds: close framing and bright environment reflections travelling across the bodywork.
- At 38 seconds: a wider composition with repeated luminous architectural forms producing a strong depth cue.
- At 48 seconds: a darker look that still preserves the silhouette and readable surface highlights.

**Our takeaway:** A convincing aircraft needs readable form, materials and a motivated camera. A continuous large heading beside a hovering model is not an equivalent treatment. These frames do not establish which exact shader implements every effect.

Study contact sheet: [Gemini frame study](gemini_study.jpg). Reference imagery belongs to its creators and is for study, not reuse in our documentary.

### B. Lusion’s studio breakdown: hybrid rendering is legitimate
Lusion documents Houdini-precomputed animation, compressed vertex-animation data, baked surface/lighting information, and a hybrid combining Redshift-rendered video with GLTF geometry and exported camera placement. It explicitly argues that not everything needs to run in real time. [2](https://www.awwwards.com/case-study-for-lusion-by-lusion-winner-of-site-of-the-month-may.html)

**Our takeaway:** Keep HTML as the delivery/runtime format, but do not force every asset and effect to originate from a few JavaScript primitives. Bake expensive elements when that materially improves quality. The published pipeline is an example, not code that can be dropped unchanged into our project.

### C. TomsProject — documentary-scene construction
**Watch:** https://www.youtube.com/watch?v=Jmcg5ZSU8a8

The tutorial describes assembling an environment, importing props and a character, setting up a camera, animating and rendering a documentary-style scene. Its published chapters include environment setup at **0:33**, asset import at **1:44**, adding the character at **4:23**, scene animation at **10:55**, and rendering/export at **12:05**. [4](https://www.youtube.com/watch?v=Jmcg5ZSU8a8)

**What the inspected storyboard shows:** A person, table, chair and food occupy the same room. Side, elevated and frontal views expose consistent spatial relationships. Even simplified character geometry can work when composition, staging and lighting are coherent.

**Our takeaway:** Photorealism is not mandatory. A deliberate stylized scene can outperform a more detailed but disconnected overlay. Study the technique; do not copy another channel’s branding or assume this tutorial proves that channel’s internal workflow.

### D. Codrops — authored camera paths
The Theatre.js/React Three Fiber tutorial loads a GLTF environment and animates a perspective camera through it using an editable timeline that can be exported as JSON. [1](https://tympanus.net/codrops/2023/02/14/animate-a-camera-fly-through-on-scroll-using-theatre-js-and-react-three-fiber/)

**Our takeaway:** Replace arbitrary sine-wave movement with an authored camera track. For a documentary, drive the timeline from narration time or frame number, not scroll position. React is optional; the lesson is the camera/timeline workflow.

### E. Codrops — cinematic browser worlds and audio choreography
The FRONTIER/LXSTNGHT production article describes Blender-authored geometry, reusable scene conventions, batching, frame-budget measurement and audio features precomputed to JSON rather than improvised from live FFT values. [2](https://tympanus.net/codrops/2026/08/22/sixty-frames-for-the-record-a-three-js-game-seven-fly-throughs-and-a-wall-of-crts/)

**Our takeaway:** Build one dependable runtime with authored shots and timed sound cues. Treat the article’s performance figures as its author’s project-specific measurements, not promises for our hardware. In a documentary, narration takes priority over both music and effects.

### F. New York Times / Forensic Architecture — evidence-driven reconstruction
The Douma reconstruction explains how photographs, videos and spatial evidence were used to reconstruct a building and examine competing accounts. [2](https://www.nytimes.com/interactive/2018/06/24/world/middleeast/douma-syria-chemical-attack-augmented-reality-ar-ul.html)

**Our takeaway:** 3D should explain something that ordinary footage cannot. Clearly distinguish an evidence-based reconstruction from a generic illustration. Never manufacture precision with invented flight paths, coordinates or unverified impact locations.

---

## 3. Specific faults in our existing HTML

These are findings from our own source code, not guesses about the references.

| Existing implementation | Why it looks weak | Required change |
|---|---|---|
| Fighter made mainly from spheres, cones and thin extrusions | Limited silhouette refinement, surface detail and material variation | Use a properly authored or licensed model; fix proportions, normals and materials before adding effects |
| `imageBG()` draws a flat image; `render3d()` draws an independently shifted/scaled WebGL canvas | Perspective, depth and lighting do not belong to one world | Shared camera and 3D set, or a deliberately restricted camera-projected plate |
| `drawImage(renderer.domElement,720,60,...)` moves the whole rendered scene in screen space | Fixes text overlap but breaks a consistent camera/compositing relationship | Compose the shot through the camera and film framing, not by dragging its finished image |
| Repeated `Math.sin()` bobbing and simple camera interpolation | Continuous movement without a clear storytelling purpose | Authored shot curves, look targets and restrained secondary motion |
| Impacts use fixed 2D screen positions | Effects are not tied to the same ground as the dropped objects | Shared world-space event anchors, projected into the frame only for labels |
| Basic lights; no environment map, shadow pipeline or post-processing composer | Flat/plastic appearance, little environmental integration | Intentional lighting, reflections, suitable shadows/baked shading and a controlled finishing pipeline |
| Each chapter is divided into four equal-duration beats | Narration and visual events drift; pacing becomes repetitive | Time shots to actual phrases and story developments |
| Same title-left / object-right / lower-card layout throughout | Feels like a slide template | Alternate full-screen scenes, close-ups, maps, restrained data moments and quiet pauses |
| A fixed synthesized bed and generic cue family | Limited sense of location, distance and material | Scene ambience, object-specific Foley and deliberate sound perspective |

**Keep what worked technically:** embedded assets, exact-time seeking, a single soundtrack, frame capture, source disclosure and offline delivery. Passing those tests did not demonstrate cinematic quality.

---

## 4. The production approach I recommend

### Step 1 — Narration-led shot list, not automatic equal blocks
Write a table containing: narration phrase, purpose of shot, focal object, camera position/movement, event, graphic, sound cue and source.

A shot must answer a visual question: Where are we? What changed? What is the relationship between these places? What is known versus uncertain?

A **3–8 second shot** is a useful starting point for many passages, not a rule. Hold longer for geography or comprehension. Do not manufacture a cut every few seconds if the explanation needs continuity.

### Step 2 — Approve the asset and environment before animation
For the hero aircraft, check silhouette, intake/exhaust shape, canopy, wing thickness, normals, seams and roughness under a neutral inspection light. Use a stylized but coherent design if a suitable realistic asset is unavailable. More polygons alone are not the objective.

Potential asset route: original modelling or a properly licensed GLB with texture maps. Keep a license manifest. An asset permitted in a rendered video is **not automatically permitted to be redistributed inside an HTML file**. Poly Haven explicitly makes its asset collection available under CC0, including commercial use and redistribution; this does not guarantee it has the specific aircraft model needed. [Poly Haven license](https://polyhaven.com/license)

### Step 3 — Give the environment real depth
Three valid options:

1. **Full 3D:** terrain, structures and aircraft occupy one scene. Best when the camera translates substantially or objects must pass behind foreground geometry.
2. **2.5D:** split an image into foreground, middle and background layers; add approximate geometry/depth. Use modest camera movement and inspect exposed edges.
3. **Camera projection:** project an AI plate onto proxy geometry and keep the camera near the projection viewpoint. Sideways movement can reveal stretching or previously unseen surfaces; it cannot conjure a correct hidden world.

Use AI for controlled plates, concept art, distant backgrounds or texture development. Do not mistake an AI image for measured terrain or authentic evidence.

### Step 4 — Direct the camera
Use separate tracks for **camera position, orientation/look target, field of view and focus**. Use spline/Bézier paths with deliberate easing; avoid uncontrolled roll and sudden look-at flips. Match the camera to the image plate’s horizon and perspective when compositing.

Suggested shot vocabulary: wide establishing view → tracking view → close detail → overhead context → quiet consequence. Each change should convey new information, not just display a different angle.

A glTF animation clip or timeline JSON can drive the scene. Blender constraints, procedural modifiers and simulations should not be assumed to survive export unchanged: test the exporter and bake supported animation where necessary.

### Step 5 — Unify lighting and colour
Match key-light direction, softness, colour temperature, contrast and atmosphere across plate and 3D objects. Use environment reflections where appropriate; add roughness variation rather than making every surface uniformly metallic. Grounded props need contact shading; high-altitude aircraft do not need an artificially sharp ground shadow.

Three.js documents that each shadow-casting light adds rendering work, and that baked light/AO information or carefully chosen fake shadows can be valid alternatives. Use shadows intentionally rather than enabling every light indiscriminately. [Three.js shadows manual](https://threejs.org/manual/en/shadows.html)

Use a consistent linear-light workflow. Colour textures normally use sRGB; normal/roughness maps are non-colour data. Avoid double tone mapping/output conversion, especially when combining a photographic plate with a WebGL render. [Three.js colour-management manual](https://threejs.org/manual/en/color-management.html)

Light, dark and mixed themes remain available. Choose per story and shot; no compulsory daylight, neon or black HUD treatment.

### Step 6 — Effects must inhabit the scene
For a generic illustrative strike, place the falling object and impact at a common **world-space anchor**. Use a brief light flash, restrained dust/debris, expanding ground effect and lingering smoke/atmosphere as separate timed components. Consider a baked flipbook or short effect plate when real-time simulation would look worse or consume excessive resources.

Respect occlusion: foreground terrain may hide smoke; effects should not always draw on top. Match wind, perspective, light and scale. Keep it non-graphic and explicitly illustrative unless evidence supports a more specific reconstruction. This is a visual-production plan, not an operational strike simulation.

### Step 7 — Finish the picture, then overlay clean editorial text
A suitable pipeline is scene render → selected atmosphere/AO/DOF or motion treatment → restrained bloom → grade/tone mapping/output conversion → sharp editorial overlays. Actual pass order depends on the effects and renderer; verify it rather than stacking defaults. Three.js provides an EffectComposer/pass system for this kind of processing. [Three.js post-processing manual](https://threejs.org/manual/en/post-processing.html)

Do not use blur, grain or bloom to hide bad modelling. For a documentary map, readability may be more valuable than shallow focus.

Prefer a date, place name or short annotation to persistent headings that occupy half the screen. Reserve larger typography for transitions or essential evidence.

### Step 8 — Choreograph sound
Narration is the anchor. Layer location ambience, aircraft movement, mechanical detail and controlled impact accents. Shape loudness and stereo position with screen movement. Use silence or reduced music where it helps explain stakes. Audible does not mean every pop-up should be louder than the narrator.

Export one fixed master soundtrack and a cue sheet. This makes browser playback and offline rendering agree.

---

## 5. A practical HTML architecture

**Authoring:** asset preparation and camera/animation blocking in Blender or equivalent; text and timing in readable JSON.

**Runtime:** Three.js with a pinned compatible version; GLTF loader; tested material pipeline; optional timeline library; selective post-processing; separate clean editorial layer.

**Export:** exact frame-time evaluation, not a recording of whichever frames the browser happens to display.

```text
project/
  index.html
  assets/       models, textures, plates, licensed effect assets
  shots.json    camera, objects, events, overlays, source IDs
  audio/        narration, stems, final master, cues
  render/       deterministic frame capture + audio mux
  licenses/     redistribution permissions and attribution
```

This can be bundled into one HTML file when size and licensing permit. A ZIP/local project is often more maintainable for larger assets; ask before changing the requested delivery format. Asset compression may require additional decoder code, which also has to work offline.

For frame `n`, evaluate the picture at `t = n / fps`. Derive every effect from that time and a fixed seed. Use a known reset/evaluation path for animation clips. Avoid accumulated physics state, `Math.random()` in frame rendering and unawaited video seeks. Embedded pre-rendered video complicates frame-exact seeking; wait for decoding and test it, or use frame-addressable assets.

**Preview and final export are separate quality tiers.** A fast preview does not prove a 1080p final is attractive; a correct slow export does not require a real-time preview to maintain 30 fps.

---

## 6. Proposed 25-second quality proof

**This is a recommendation for the next production step, not an already-created clip.**

| Time | Shot | What it tests |
|---|---|---|
| 0–4 s | Wide regional environment; aircraft crosses through depth | Scale, environment continuity, atmosphere and silhouette |
| 4–9 s | Rear-quarter tracking shot with subtle banking | Model quality, reflections, authored camera and motion |
| 9–13 s | Closer under-wing/body detail; an illustrative event begins | Material detail and causal continuity, with no operational specifications |
| 13–18 s | Wider terrain view with restrained illustrative impact | World-space alignment, occlusion, dust/light integration and sound timing |
| 18–22 s | Match cut to a restrained explanatory map | Editorial clarity, readable labels and evidence disclosure |
| 22–25 s | Quiet consequence/context shot | Pacing contrast; the documentary is not only a weapons showcase |

Full-screen visual storytelling should dominate this proof. Use minimal graphics, not the previous fixed dashboard layout. Decide theme from the selected setting and emotional purpose.

### Pass/fail gate before another long documentary
- Does the model still look convincing when paused at full resolution?
- Do its lighting, scale and perspective match the environment?
- Does the camera reveal information instead of drifting aimlessly?
- Are visual events spatially connected, including occlusion?
- Does the scene work without a wall of explanatory text?
- Are narration and effects intelligible on ordinary speakers?
- Are the reconstruction and uncertainty labels honest?
- Do nonsequential seeks reproduce the same frames?
- Does the user approve the actual moving result, not merely a contact sheet?

**If the proof fails visually, do not stretch the same approach to seven minutes.** Revise the model, scene and camera first.

---

## 7. Priority order

1. Replace the disconnected plate-plus-overlay architecture for hero shots.
2. Improve model and material quality; establish the environment.
3. Author camera shots and narration timing.
4. Integrate lighting, shadows, depth and effects.
5. Design sound and editorial graphics.
6. Optimize and package only after the look works.

**Bottom line:** HTML is not the problem. The shortcut was treating a cinematic documentary as a reusable card template with 3D decorations. The next attempt should be a small, properly directed scene that proves the quality before we scale it up.
