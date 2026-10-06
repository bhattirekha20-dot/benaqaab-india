# Motion-graphics skills research — verified, distilled, adopted (2026-09-30)

Companion to `MOTION_RESEARCH_Opus55.md` (the first pass, 2026-09-29) and
`PROMPT_LIBRARY_opus55.md` (883 unique prompts, verbatim). The user pasted a second research
pass from another chat; everything in it was **checked against GitHub directly** and the repos
were cloned and read, not summarised from READMEs.

---

## 1. Every repo from that research exists (GitHub API, 2026-09-30)

| Repo | ★ | What it is | What I took |
|---|---:|---|---|
| calesthio/OpenMontage | 61,891 | Agentic video production system, 12 pipelines | Architecture ideas only — depends on paid Veo/Kling/fal providers |
| heygen-com/hyperframes | 54,265 | HTML → deterministic MP4 framework, 21 agent skills | **Vector Law, "the current", carriers, white-flash guard, faceless-explainer flow** |
| Vincentwei1021/video-shotcraft | 9,939 | Cinematic product videos, 152 shot recipes | Product-video only; skimmed |
| remotion-dev/skills | 4,773 | Official Remotion skills | Reference |
| Vincentwei1021/anything2explainer | 2,171 | **Topic in → narrated explainer out** (Remotion) | **Most rules below: stillness, settle, protagonist, beats, narration principles** |
| Alisa0808/vox-director | 2,084 | Topic → Vox paper-collage explainer | "The collage look is born in the IMAGE step" |
| LottieFiles/motion-design-skill | 1,823 | Motion principles | Timing tables (premium 350–600 ms, stagger total < 500 ms) |
| Vincentwei1021/video-talkcraft | 1,298 | Voiceover-driven explainer studio, 108 recipe cards | **Anti-slideshow rule, word-anchored beats, evidence filming, vertical safe zones** |
| nateherkai/hyperframes-student-kit | 1,104 | Shorts/reels editing kit, 14 skills | Shorts safe zones, curiosity-led openings |
| feitangyuan/onetake | 981 | "Films that never cut to the next slide" | **Carry rule; 3 concepts before a beat sheet** |
| yihui-dev/awesome-opus5-5-videos | 915 | 389 prompts | Merged into the prompt library |
| iart-ai/motion-skills | 594 | 50 motion skills | Reference |
| Barty-Bart/motion-graphics | 337 | Motion B-roll, one morphing shape, 4-subframe blur | Morph with lead/trail edges; pace 0.4–1.2 s per spoken beat |
| zhuyansen/awesome-claude-video-skills | 297 | Index of 183 repos, security-graded | Index |
| haidrrrry/claude-remotion-skill | 224 | Remotion craft rules + render→inspect loop | Exits faster than entrances; never linear |
| opusvideo/awesome-claude-video | 163 | Curated videos | — |
| howseen-ai/claude-motion-design | 105 | HTML + Playwright + ffmpeg pipeline | **"4 subframes = ghosting, 6–8 for fast moves"; log-space zoom; pops check** |
| makevoid/motion-graphics-music-video-skill | 69 | Music-video plugin | — |
| guanmo-ai/awesome-ai-motion | 66 | Chinese prompt archive | Merged into the prompt library |
| zhuyansen/awesome-opus-5.5-video | 52 | Catalogue of works | — |
| iart-ai/motion-design-skills | 38 | Fundamentals | — |
| charlie947/motion-graphics-skills | 27 | 13 launch/chart/Vox/reel skills | "No card covers another card's text" |
| TripoGrowthLab/awesome-opus-5-5-prompts | 21 | Source-linked prompts incl. Spotify brief | Already in MOTION_RESEARCH_Opus55.md |
| Mort1d/motion-graphics-skills | 13 | Showreel + original soundtrack | — |
| Li-Evan/awesome-opus-5.5-video-prompts | 1 | 334 verified-verbatim prompts, categorised | Merged (best source for explainers/history) |
| X-RayLuan/…, RealBetterToken/…, seoceandigital/broll-motion, felipefernandees/…, wcfcarolina13/motion-studio, AidenChenCode/…, lowfatgeek/…, myceldigital/… | 0–1 | New this week | wcfcarolina13: the **blind-read gate** |

**Honest scope:** these are Claude Code / Codex skills — folders of instructions and scripts that
an agent loads on the user's own machine. I cannot "install a skill into myself". What I did
instead: cloned them, read the rules and code, ported the techniques into `viz/motion.py` +
`viz/motion.js`, and installed the renderer stack they use (Chromium + Playwright + ffmpeg),
which runs in this sandbox because it has sudo.

---

## 2. The rules, by the problem they solve

### Continuity — why most AI videos feel like slideshows
- **Vector Law (HyperFrames motion-doctrine):** how scene A exits decides how scene B enters —
  same axis, same direction, matched speed, cut mid-motion on BOTH sides. A shrinking exit
  answered by a grow-from-small entry is a mirrored vector — the most common violation.
- **The current:** one dominant direction per film. Reserved vectors carry meaning:
  up = conclusion/reveal · Z-forward = deeper into the same thought · Z-back = arrival ·
  scale-burst = leaving a world. Never ping-pong; a direction change needs a visible cause.
- **Carry (onetake):** at every boundary name the thing that survives and moves. "If nothing
  survives, it is a slide change, whatever the rhythm." Bare cuts only in bursts of hits and at the end.
  onetake's first two cuts were rejected as "PPT-style one by one"; v3 passed when every beat grew out of the last.
- **Three concepts before a beat sheet:** one element transforms through everything /
  before-after split / chain reaction. Pick one.
- **White-flash guard:** paint the stage (#root opaque) — crossfade dips show white otherwise.

### Narration and picture (anything2explainer, video-talkcraft)
- Every sentence gets a **live visual response** (camera move or change in an existing element),
  but **new elements only enter at semantic beat boundaries** — "one sentence, one new element"
  is the root cause of cluttered, piled-up videos.
- **One protagonist per beat**, big, the only thing with the accent/glow; it yields when its line
  is done. At most 3 subject groups on screen at once.
- **Not shown before its beat:** an element is fully invisible until its word lands (no greyed
  previews). Tolerance −6…+3 frames; word anchors |Δ| ≤ 0.1 s from real timestamps, never hand-typed.
- **No empty stage:** a main visual enters within 10 frames of a cut; no gap > 1.5 s at shot start.
- **Continuous action + settle:** nothing fully still > 3 s (Shorts: much less); every shot's
  last beat holds **30–45 frames** with no new elements, then exits. Both "enter then freeze" and
  "settle then cut instantly" are defects. Don't fake it with floating/breathing — use a slow
  1.0 → 1.05 camera push.
- **Shots by visual unit, not by sentence:** a paragraph of 2–4 sentences = one shot; short lines
  merge into neighbours; pauses only at paragraph ends (10 frames inside, 30 at the end).
- Real footage/images are required — "zero images = watching a PPT". (Ours: AI photography.)
- **Evidence gets filmed, not pasted:** screenshot the real page with Playwright, then scroll →
  stop → highlight/magnify; annotation coordinates measured from the DOM, never eyeballed.
- Vertical: persistent elements **bottom-left** — the right edge is the Shorts like/comment column.
- Narration principles (13): start inside a situation, one spine, motivation before mechanism,
  concrete numbers on a human scale, analogies that carry weight, a voice with a view, varied
  rhythm, jargon only after the idea, stakes early / payoff late, cut hard, say what the picture
  can't, precision earns trust, hand off at the seams.

### Motion craft
- Closed-form springs; a value with many targets = sum of one spring per change; never linear.
- Four named curves only (ARRIVE/SETTLE/SWEEP/CUT). Entrances ≤ 600 ms; exits faster
  (~0.25–0.33 s) and reach exactly 0 before any cut (`1 − n^1.5`).
- Leading and trailing edges on different springs so shapes stretch (Barty-Bart, MakerMap).
- Camera = one transform on the content layer; **zoom interpolated in log space**; never zoom in
  then out back-to-back; ≤ 1 move per shot, 30–45 frames, not during entrances; captions stay put.
- Masked text rise (translateY 105% inside overflow:hidden), 55–70 ms word stagger, tiny rotation.
- Floods (circle transitions) must clear the farthest corner (hypot × 1.05) in ~0.3 s.
- **Motion blur:** 4 subframes ghost on fast moves (howseen: use 6–8) → our adaptive sampler goes
  1…12 by measured speed; stationary text stays razor sharp.

### Quality gates
- Render stills first (one per beat) and LOOK at them; fix; only then full render.
- **Harsh-director pass:** score hook ≤ 2 s · phone readability · motion · variety · composition ·
  sound sync; list the 3 worst problems with timestamps; fix; re-render only those seconds.
- **Freeze probe** (ffmpeg freezedetect n=0.003 d=0.8) and **pops** (frame-diff spikes > 3×
  neighbours, excluding intended cuts) → `motion.motion_report()`.
- **Blind read (wcfcarolina13):** someone who never saw the script states the film's thesis from
  stills + on-screen text alone. If it doesn't match, the film isn't done.
- "Zero fabrication on screen": illustrative data is labelled "Illustration"/"Example".

### Conflicts between sources, resolved for Benaqaab
| Conflict | Ruling |
|---|---|
| haidrrrry: "idle elements breathe, every still gets Ken Burns" vs anything2explainer/user §16: no fake floating, no reflexive Ken Burns | **User wins:** one slow camera push per shot, no per-element breathing |
| HyperFrames/onetake: never cut vs Shorts retention (cut every ~3 s, §37) | Carry across most seams; bare cuts only for bursts and the ending |
| Music-driven beat grids (howseen/makevoid) vs house rule VO-only (§36) | VO is the clock; beats come from word timestamps, not music |
| Chinese skills' fixed visual systems (black canvas + purple) vs §51 "new look every episode" | Borrow the rules, never the look |

---

## 3. The prompts that matter most (verbatim; 883 more in PROMPT_LIBRARY_opus55.md)

**The viral one-liner (1.5M views):**
```
make a dynamic 15-second motion graphics video that shows what an incredible motion designer you are, like it's your showreel for a résumé. go all out.
```

**The autonomous explainer brief — the model for how this channel now works** (@AstroTheWizard, "Journey of a photon"):
```
I want you to make a 60-second, fully animated explainer video, end to end, completely on your own. I'm stepping away from my computer, so work autonomously until it's done. Don't stop to ask me questions; make the calls yourself and tell me what you decided at the end.
[…] It should feel like a professional motion-design studio made it, not "AI video". […] what makes them great is that they're code-rendered: crisp, precise, with a coherent design system and one strong formal idea per scene. Aim for that bar or above.
Make it genuinely educational and accurate. Where you can, simulate the real thing […] Include real numbers […] and be honest about uncertainty in the estimates. Use humor and visual gags to keep attention […]
Deliverable: […] Burned-in captions, since most people watch on X with the sound off […]
Quality is paramount. Build verification loops: render stills of every scene and review them critically, check transitions frame by frame, measure the audio mix numerically, fix what's weak and re-render. Don't hand me a first draft. Hand me something you'd put your name on. Also give me the source code so it's reproducible
```

**Structured explainer with timed beats** (@eyishazyer, "Cute creatures explain how LLMs work", 40 s) — pattern worth copying:
hook 0–5 s (one glowing dot + typed question) → one idea per 7–8 s block, each with
*visual · narration line · one "cute detail"* → kicker that loops back ("One token at a time.
That's the whole trick."). Full text in the library.

**Harsh-director critique** (Neil_xbt full course) and **MakerMap** and **Spotify** briefs: see
`MOTION_RESEARCH_Opus55.md` §1.4–1.5 and MEMORY §59.

**The blind-read gate** (wcfcarolina13/motion-studio):
```
A blind read before shipping. A fresh agent that has never seen the source looks at one still per bar plus the on-screen text and says what the film argues. If that doesn't match the contract, the film isn't done.
```
