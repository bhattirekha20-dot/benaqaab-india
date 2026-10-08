---
name: benaqaab-investigative-motion
description: >-
  Investigative documentary motion graphics in the style of Dhruv Rathee, Vox, and Johnny Harris.
  Generates code-rendered motion (HTML5/Canvas, WebGL, GSAP, Remotion, FFmpeg), dynamic evidence pinboards,
  authentic yellow highlighter multiply overlays, camera pan/zoom/shake rigs, high-contrast cinema cards,
  and Opus 5.5 Vector Law continuity choreography.
---

# 🕵️ Benaqaab Investigative Motion Graphics & Visual Storytelling

## 1. Code-Rendered Motion Pipeline (Opus 5.5 Methodology)
- Every frame is rendered from deterministic code (HTML5 Canvas, GSAP, WebGL, SVG, CSS, FFmpeg).
- Pin-sharp typography, exact data metrics, animated financial charts, and zero AI-hallucinated text artifacts.
- Synchronized sound triggers for whooshes, tape clicks, and forensic camera shutter snaps.
- Pure time function: `render(t)` where state is completely reproducible at any millisecond.

## 2. The 6 Signature Investigative Motifs
1. **Dynamic Evidence Pinboard:**
   - Dark corkboard/slate texture with forensic polaroids, newspaper clippings, red string connectors (`ctx.bezierCurveTo`), and thumbtack nodes.
   - Dynamic zoom and dolly into specific evidence nodes.
2. **Authentic Yellow Highlighter Pen:**
   - Render document scans/news articles.
   - Apply translucent yellow highlighter pen stroke with `ctx.globalCompositeOperation = 'multiply'` and natural edge wobble.
3. **Forensic Redacted Stamp & Document Unredact:**
   - Bold black/red marker reveal, animated redaction bar slide-offs revealing confidential figures.
4. **Neon-Gold Geopolitical Maps:**
   - Deep slate/obsidian terrain with glowing neon borders (`#f59e0b` / `#38bdf8`), pulse radar rings around scam hubs, and animated dotted flight/flow paths.
5. **Rolling Metric / Financial Counters:**
   - Numeric counters with monospace styling (`JetBrains Mono`), spinning up with cubic deceleration to staggering numbers (e.g., ₹14,250 Crores).
6. **High-Contrast Cinema Glass Cards:**
   - Deep dark obsidian cards (`rgba(10, 13, 20, 0.85)`), specular borders (`rgba(255, 255, 255, 0.15)`), vibrant orange/amber accents (`#f97316`). Never dull grey.

## 3. Continuity Laws & Anti-Slideshow Architecture (Pass 2 Research)
- **Vector Law:** How Scene A exits decides how Scene B enters — same axis, same direction, matched speed, cut mid-motion on BOTH sides. Never use mirrored vectors.
- **The Current:** One dominant direction per film (e.g., forward push or left-to-right flow). Reserved vectors: Up = reveal/escalation, Z-forward = deeper into same thought, Z-backward = arrival/context, Scale-burst = leaving a world.
- **The Carry Rule (`onetake`):** At every scene boundary, name the surviving element that carries across. Bare cuts allowed ONLY in staccato impact bursts and hard outro.
- **3 Concepts Before Beat Sheet:** Pick 1 of 3: Single element transforms through everything / Before-after split / Chain reaction.
- **White-Flash Guard:** Paint stage `#root` opaque `#07090E` so crossfade dips never flash white.

## 4. Narration & Picture Synchronization
- Every sentence gets a live visual response (camera push, micro-zoom, highlight sweep, or state update).
- **New elements enter ONLY at semantic beat boundaries** (prevents screen clutter).
- **One protagonist per beat:** Oversized, bearing glow/accent, yields when line ends. Maximum 3 subject groups on screen simultaneously.
- **Not shown before its beat:** Elements 100% invisible until anchor word lands (tolerance: -6 to +3 frames; anchor timestamps measured from mutagen/TTS).
- **Continuous action + settle:** Nothing still > 3s (Shorts < 1s). Final beat holds 30–45 frames with no new elements, then exits. No fake idle floating/breathing; use purposeful slow camera push (`1.00 -> 1.05`).
- **Filming Evidence:** Real portals (TAFCOP, Sanchar Saathi, court orders) rendered in DOM, panned, stopped, highlighted with `multiply` blend mode, and magnified with DOM-measured coordinates.
- **Vertical Safe Zones (9:16):** Persistent UI bottom/top-left; right 120px clear for YouTube buttons; bottom 180px clear for title/audio pills.

## 5. Motion Craft Mathematics
- **Closed-Form Springs:** Never use linear interpolation. Sum of one spring per change.
- **4 Named Curves:** `ARRIVE` (<=600ms), `SETTLE` (30–45 frames), `SWEEP`, `CUT/EXIT` (250–330ms, exits faster than entrances, reaches exactly 0).
- **Camera in Log-Space Zoom:** Scale interpolated in log space to eliminate perceptual velocity warping. Maximum 1 camera move per shot, separate from entrances; subtitles remain locked in screen space.
- **Masked Kinetic Typography:** Text rises from `translateY(105%)` inside `overflow:hidden`, 55–70ms word stagger.
- **Adaptive Subframe Motion Blur:** 1–12 passes by velocity; stationary text remains 100% razor sharp.

## 6. Rigid Quality Gates
1. **Stills-First Inspection Gate:** Review 1 still per semantic beat before full render.
2. **Harsh-Director Pass:** Score hook (<=2s), phone readability, motion, variety, composition, sound sync. List 3 worst problems with timestamps and fix.
3. **Freeze & Pop Probe:** FFmpeg freezedetect and frame-diff spike check.
4. **The Blind-Read Gate (`wcfcarolina13`):** Evaluator states core thesis from stills + on-screen text alone without hearing audio.
5. **Zero Fabrication:** Illustrative/mock data labeled "ILLUSTRATION" in mono.
