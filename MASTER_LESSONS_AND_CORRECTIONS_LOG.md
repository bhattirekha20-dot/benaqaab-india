# 🛡️ BENAQAAB INDIA — MASTER LESSONS, RULES & CORRECTIONS LEDGER

> **Authoritative Directive for all AI Models & Agents working on Benaqaab India (`SACH · SABOOT · BEBAK`).**  
> *Compiled on 07 October 2026 from user feedback, forensic project audits, and workspace handoffs.*

---

## 🏛️ PART 1: CHANNEL IDENTITY & WORKFLOW COMMANDMENTS

1. **User Location & Cadence:**
   - Channel: **Benaqaab India** (`SACH · SABOOT · BEBAK` / `Shor nahi, source ke saath`).
   - Location: Jammu, Jammu & Kashmir, India.
   - Language: Conversational Hinglish narration with crisp English on-screen terminology unless Hindi text is explicitly requested.

2. **The 1-Gate Approval Protocol (Mandatory):**
   - **NEVER** render a final `.mp4` video until the user explicitly tests and approves the HTML preview (`comp.html`) or explicitly issues the command: `"render the video"`.
   - If the user says *"show me and I will approve"*, create a visual test or interactive HTML preview first. Do not jump to an MP4 render.
   - If the user says *"do not render until I tell you"*, that command remains active indefinitely.

3. **Frame-0 Retention Hook (0.0s Rule):**
   - The Short **MUST** begin at `0:00` with a direct, high-stakes question naming the core topic.
   - **Zero** intro cards, zero channel bumpers, zero *"Hello friends"* greetings. Instant stake within the first 1.0 second.

4. **Permanent Benaqaab OS Brand Logo:**
   - Always place the official **Benaqaab OS logo** in the top-left safe area of every 1080×1920 vertical frame and 16:9 widescreen frame.
   - Keep its native proportions and colors (`gold-glow` border). Never redraw, crop, recolor, or replace it with plain typed text.

5. **AI Visual Disclosure & Currency Rules:**
   - Mark synthetic art and composites with a subtle `AI ILLUSTRATION` label.
   - **NEVER** present AI-generated currency artwork as an actual legal specimen of Indian currency.

---

## 🚨 PART 2: FORENSIC CORRECTIONS LOG (ALL 14 RESOLVED ERRORS)

| # | Reported Error / User Feedback | Root Cause Analysis | Corrective Fix Applied | Standing "Do Not Repeat" Rule |
|---|---|---|---|---|
| **01** | **HTML Preview Freezing / Blank Screen** | `comp.html` waited for `audio.loadedmetadata` before rendering the initial frame; sandbox audio autoplay restrictions blocked initial visual paint. | Decoupled audio load from visual canvas. First frame now renders immediately at `t=0` with fallback timing. | **Rule 1:** Previews must be self-contained and visually interactive even before audio loads or if browser sound is blocked. |
| **02** | **Permanent Bottom Thumbnail Strip in Final MP4** | Debugging UI image reel was accidentally included in the composite canvas rendering pipeline. | Stripped the image reel completely from `render_final.py` and `comp.html`; lowered subtitle captions into safe margin. | **Rule 2:** Never bake UI navigation controls, debug buttons, or persistent thumbnail strips into production MP4 frames. |
| **03** | **Frame-0 Hook Not Starting as a Question** | Initial voiceover began with background context rather than an instant provocative question. | Re-scripted opening beat to start at `0:00` with an explicit question (e.g. *"CREDIT KISE MILEGA? Kya ek emission cut do baar count ho sakta hai?"*). | **Rule 3:** The first word spoken and first on-screen title MUST be a direct question stating the controversy or stakes. |
| **04** | **Debug Scene Counters Baked on Screen (`02 / 14`)** | Internal frame-builder script printed debug scene indexes into the header canvas. | Removed all debug numbering counters from `build_frames.py` and preview templates. | **Rule 4:** Never display internal debug metadata, scene counters, or frame numbers in client-facing deliverables. |
| **05** | **Visual Mismatch Across Story Transitions** | Crossfade opacity caused preceding story visuals (e.g. DRI Gold) to bleed into the subsequent story (e.g. Earthquake alert). | Replaced crossfades with hard scene cuts; regenerated clean scene backgrounds mapped 1:1 to designated news beats. | **Rule 5:** In multi-topic roundups, enforce strict scene separation. Never allow an image from Story A to linger into Story B. |
| **06** | **Tiny Images with Oversized Blue Dead Space** | Fixed 400px image boxes left massive dead space, while lower half was covered by an opaque blue block. | Enlarged source imagery to 1040×1200; replaced flat blue blocks with image-derived blurred backdrops and subtle gradients. | **Rule 6:** Keep 65–75% of the screen unobstructed. Use edge-to-edge staging and transparent gradients rather than opaque text boxes. |
| **07** | **Duplicate & Overlapping Captions** | Static text was baked into still background frames AND rendered dynamically as an HTML layer. | Switched to clean background plates with a single animated typography layer in HTML/Canvas. | **Rule 7:** Render text exactly once. Verify at 375px mobile viewport that headlines never cover source images or data cards. |
| **08** | **Rejected Source Pill Badges (`OFFICIAL SOURCE IMAGE`)** | AI added generic badge pills over official graphics, cluttering the visual hierarchy. | Removed all generic on-screen source badges; placed verified citations in YouTube description, notes, and credits. | **Rule 8:** Do not add unrequested badge pills. Let official graphics speak for themselves with clean typography. |
| **09** | **Video/Audio Drift (Scene Desynchronization)** | Scene timing was estimated from character counts rather than actual spoken audio duration. | Extracted true audio timestamps from voiceover files to synchronize visual beat cuts with precision. | **Rule 9:** Always use audio master clock timestamps to determine scene boundaries; never guess pacing from text length. |
| **10** | **Factual Cricket Calculation Error ("171 Ka Target")** | Script stated the target was 171 when West Indies scored 171 (making the target 172). | Edited the voiceover audio to remove the incorrect phrase; corrected on-screen graphics to state `Target 172`. | **Rule 10:** Verify sports, financial, and regulatory figures with two primary ledgers. Re-check match scorecards before render. |
| **11** | **Closing Scene Zero-Duration Cutoff** | Preview timeline assigned the final closing scene a start fraction of `1.0` (end of timeline), causing it to flash and vanish. | Corrected the start fraction to span the entire closing narration beat through the outro fade. | **Rule 11:** Verify all scene duration fractions. Outros must remain on screen for the full call-to-action duration. |
| **12** | **Premature MP4 Renders Without Approval** | Previous AI models rushed to execute FFmpeg rendering before user reviewed the concept or script. | Enforced strict 1-Gate protocol. MP4 rendering commands are completely blocked until explicit user command. | **Rule 12:** Present the interactive preview first. Wait for explicit approval before spending system compute on rendering. |
| **13** | **Third-Party Video Extraction & Permission Blocks** | Attempted to download third-party clips (Instagram/YouTube/BCCI) which failed on HTTP 403 / anti-bot verification. | Replaced footage dependency with high-resolution official stills, verified data cards, and clean motion graphics. | **Rule 13:** Never stall a production on third-party video scraping. Use high-contrast official stills and original graphics. |
| **14** | **Thumbnails Lacking Detail and High-Contrast Typography** | Initial AI thumbnails lacked clear text hierarchy or curiosity-inducing sharpener text. | Authored 3D embossed metallic typography, 2-word curiosity pills, and metric badges (`₹4/KG`, `₹734 Cr`, `0.88% WAPSI`). | **Rule 14:** Thumbnails must feature large readable headlines, high curiosity gaps, and verified numbers tested in feed simulators. |

---

## 📦 PART 3: NEW PRODUCTIONS CATALOGUED & SAVED

### 1. `SH-09: India Last 24 Hours — Sabse Important Kya Badla?`
- **Format:** Shorts (9:16 · 1080×1920 · 24fps · 118s).
- **Master Video File:** `VIDEOS/10_India_Last_24H_SHORT_118s.mp4`.
- **Vertical Cover Thumbnail:** `projects/india_last_24h/thumbnail_curiosity_text_1080x1920.png`.
- **Project Folder:** `projects/india_last_24h/` (14 scenes, official DRI/ECI/PIB/NCS/BCCI cards, timed narration, SRT captions).
- **Curiosity Hook:** *"INDIA 24 HOURS: KYA BADLA? Vote row • ₹10,000 crore • earthquake • cricket"*.

### 2. `SH-10: India–Japan JCM Carbon Credit Mechanism`
- **Format:** Shorts (9:16 · 1080×1920 · 30fps · 107s).
- **Master Video File:** `VIDEOS/11_India_Japan_JCM_SHORT_107s.mp4`.
- **Master Thumbnail:** `projects/india_japan_jcm/india_japan_jcm_short_thumbnail.jpg`.
- **Project Folder:** `projects/india_japan_jcm/` (Article 6.2 fact ledger, bilateral credits, corresponding adjustments).
- **Opening Question (0:00):** *"CREDIT KISE MILEGA? Kya ek emission cut do baar count ho sakta hai?"*.

### 3. `FL-05: Kagaz Ki Machine — Teen Scams, Ek Hi Business Model`
- **Format:** Film (16:9 · 1920×1080 / 1280×720).
- **Master Landscape Thumbnail:** `projects/kagaz_ki_machine/thumbnail_curiosity_text_1280x720.png`.
- **Project Dossier:** ED ₹734 Cr fake ITC racket, 135 shell entities, ₹5,000+ Cr bogus invoices, mule accounts, scrap book recycling.
- **Key Metrics:** `₹4/KG` | `₹734 Cr` | `0.88% WAPSI`. Sources: BBC, I4C/MHA, Moneylife, Enforcement Directorate.

### 4. `FL-06: Hugging Face AI Model Supply Chain Hack`
- **Format:** Film (16:9 · 1920×1080).
- **Project Folder:** `projects/ai_hf_hack/` (`film.html` interactive player, `audio_master.mp3`, 42 scene images, 22 audio stems).
- **Thesis:** Critical code execution vulnerability in Hugging Face / JFrog AI model registries exposing enterprise LLM weights.

---

## 🎯 PART 4: VETTED INTELLIGENCE RADAR (OCTOBER 2026 FRESH LEADS)

The following 5 leads from `NEW_TOPICS_2026-10-06.md` have been verified with primary ledgers and are ready for synthesis:

1. **Topic A — RBI: Kal Aapki EMI Badlegi? (Decision 7 Oct 2026 Morning) [TIME-CRITICAL]**
   - *Hook:* "Kal subah RBI ek button dabayega — 5.25% ya 5.50%? Aapki EMI usi se chalegi."
   - *Data:* Repo currently 5.25%; inflation 4.82%; crude ~$107; rupee past ₹96/$. BofA projects first hike (+25bps). Home loan ₹50L monthly jump computed at +₹795/mo.

2. **Topic B — GST Arrest Khatam? (57th Council 8 Oct 2026, Bharat Mandapam)**
   - *Hook:* "8 अक्टूबर को GST का हथकड़ी वाला डर उतर सकता है — पर जालसाज़ कहाँ जाएँगे?"
   - *Data:* Section 69 removal; threshold ₹1 Cr ➔ ₹5 Cr; 72,393 cases / 887 arrests audited. Counterweight: ED ₹734 Cr fake ITC bust.

3. **Topic C — Green Energy Corridor Phase-III (Cabinet 30 Sep 2026)**
   - *Hook:* "₹1,86,405 करोड़ — बिजली की 'हाईवे' बनेगी, 135 GW सूरज-हवा का कंक्रीट में जाएगा।"
   - *Data:* ₹1,36,378 Cr intra-state + ₹50,000 Cr for 50 GWh battery storage evacuation by 2032-33.

4. **Topic D — SEBI Index Futures Margin Hike**
   - *Hook:* "Retail traders ke liye F&O ka darwaza band? SEBI ke naye lot size niyam."
   - *Data:* Minimum contract size ₹5L ➔ ₹15L; 91% retail F&O loss ratio cited in SEBI study.

5. **Topic E — Train Kavach 4.0 RDSO Specifications**
   - *Hook:* "Do train ek hi track par 130 km/h par aati hain — bina driver ke brake kaise lagta hai?"
   - *Data:* RDSO Kavach 4.0 certified; 10,000 locomotives; auto-braking reaction time under 0.1s.

---

## ⚖️ PART 5: RECONCILED PRODUCTION STANDARDS & CONFLICT RESOLUTIONS

*Codified on 07 October 2026 to resolve all contradictions between historical project memory, compact guidelines, and current production practice.*

### 5.1 Three Dedicated Project Color Grading Profiles (Resolving Color Conflict)

Contradictory global rules regarding color grading have been permanently eliminated. All productions must specify and apply one of three dedicated profiles:

| Profile | Target Genre | Color Palette & Visual Treatment | Technical Specification | Example Projects |
|---|---|---|---|---|
| **Profile A: Daily News & Global Roundup** *(The Clean Neutral Standard)* | Fast-paced daily news, roundups, policy bulletins, economic snapshots | **Neutral, modern, authentic documentary grade.** Natural color temperature, realistic skin tones, clean whites, balanced saturation, and crisp contrast. **Zero artificial warm, orange, or sepia cast.** Avoids muddy, dated looks on contemporary news photos and charts. | Clean source pass-through, neutral balanced levels, subtle lower-third gradient, edge-to-edge staging (`build_frames.py`). | `projects/india_last_24h/` (India Last 24 Hours / Worldwide Roundup) |
| **Profile B: Benaqaab Forensic Dossier** *(The Investigative Standard)* | Investigative exposés, political controversies, corruption scandals, financial scams | **High-contrast monochrome / desaturated plate with a vibrant Red censor/classification band.** Dark obsidian slate base (`#07090E`), deep blacks, stark highlights, and signature horizontal red banner (`#ef4444` / `#dc2626`). | Luminance conversion + contrast boost + horizontal red accent band + 4% organic grain (`brand/ref_investigative_2.png`). | `projects/voter_list_sir/`, `projects/kagaz_ki_machine/` |
| **Profile C: Historical & Archival Footage** *(The Retro Public Video Standard)* | Historical flashbacks, declassified archival footage, vintage public records | **Warm filmic sepia/orange base with a dark-green horizontal glitch band.** Evokes analog tape and archival government records without altering facial geometry or speech clarity. | BGR to luminance -> warm sepia map (RGB 182, 106, 58) + floating dark green band (`#22764e`) + Gaussian noise (`apply_public_video_grade.py`). | Retrospective archival segments, historical flashbacks |

> **Directive:** Do NOT apply Profile C's warm sepia/orange grading to Profile A daily news roundups. The latest correction on the worldwide news preview explicitly mandates **Profile A (Neutral Grade)** to preserve crisp contemporary realism.

---

### 5.2 Conflict Resolution 1: Rendering Gate (Preview First vs. Automatic Render)

- **Old Compact Rule:** *"Finish the work — topic in, finished film out; proceed automatically without stopping."* `[DEPRECATED & SUPERSEDED]`
- **Official Reconciled Rule:** **The 1-Gate Approval Protocol is Mandatory.**
- **The Execution Contract:**
  1. **Phase 1 (Autonomous):** Research topic, build verified two-source fact ledger, write conversational Hinglish script, record/synthesize narration audio with phonetic marks, produce all visual assets (source media + AI illustrations), and build the self-contained interactive HTML preview (`comp.html`).
  2. **Phase 2 (The Gate):** **STOP.** Present the interactive preview (`comp.html`), audio timestamps, and visual proof to the user.
  3. **Phase 3 (Authorization):** Render the final `.mp4` video via FFmpeg/canvas **ONLY** when the user explicitly commands: *"render the video"*, *"approved"*, or *"proceed to render"*.
  4. If the user previously stated *"do not render until I tell you"*, that instruction remains active across all turns until explicitly lifted.

---

### 5.3 Conflict Resolution 2: Logo Placement (Top-Left Standard)

- **Old Guidance:** Early templates occasionally referenced a *"tiny top-right logo"*. `[SUPERSEDED]`
- **Official Reconciled Rule:** **Official Benaqaab OS Logo in Top-Left Safe Area.**
- **Placement Parameters:**
  - **Vertical (9:16 · 1080×1920):** Top-Left corner at `x: 55px, y: 30–40px`.
  - **Widescreen (16:9 · 1920×1080):** Top-Left corner at `x: 55px, y: 35px`.
  - **Asset:** Must use the authentic `source_images/benaqaab_os_logo.png` / `brand/logo.png`.
  - **Styling:** Retain native circular proportions and the signature gold-glow border. Never crop, recolor, distort, or replace the logo with plain typed text.

---

### 5.4 Mandatory Unpacked Deliverables Standard & Immediate Display

- **Historical Incident Recorded:** In October 2026 audits, critical deliverables (thumbnails, titles, descriptions, tags, SRT) were left buried exclusively inside ZIP archives (`workspace-*.zip`, `Benaqaab_India_COMPLETE_PACKAGE.zip`), causing severe friction, lost time, and verification failures for agents and the user.
- **Mandatory Deliverables Standard:**
  1. Every completed production must generate and store standalone, **unpacked files** in the project `delivery/` directory and/or project root:
     - `thumbnail_1280x720.jpg` — 16:9 high-contrast landscape thumbnail.
     - `cover_vertical_1080x1920.jpg` or `thumbnail_1080x1920.png` — 9:16 Shorts thumbnail with curiosity sharpener text.
     - `title.txt` — Primary video title and approved high-CTR variants.
     - `description.txt` — Full YouTube description with timestamps, sources, and disclosures.
     - `hashtags_and_tags.txt` — Keyword tags and SEO hashtags.
     - `headline_captions.srt` — Timestamped caption file.
  2. **Immediate Presentation in Chat:** In the final report, the AI must explicitly display the thumbnail (using markdown image embeds `![Thumbnail](...)`), quote the title and description directly, and link to the files. **Never say "the deliverables are inside the ZIP".** A ZIP bundle may be provided as an optional archive, but the deliverables must always be immediately visible and accessible outside the ZIP.

---

### 5.5 Visual Sourcing & Multi-Story Rigor (Prominent Checklist)

- **Real Source Media & AI Images — Never Diagrams Alone:**
  - Benaqaab India is a hard-hitting visual investigative documentary channel. Abstract geometric diagrams, sterile UI mockups, or lone infographic charts are NOT acceptable as the primary visual.
  - The visual spine must always be **real source media** (official government releases, PIB infographics, press conference photos, agency stills, satellite imagery, verified document scans, news coverage) combined with **photorealistic, high-detail AI-generated illustrations**. Diagrams and motion graphics are supporting layers, never the sole visual presentation.
- **Exhaustive Multi-Story Visual Sourcing (Independent Curation):**
  - In multi-topic roundups (such as daily news digests), the AI must independently locate, curate, or create distinct, high-quality visual assets for *every single story* in the lineup.
  - Sourcing must not be concentrated solely on one high-profile personality (e.g. Rahul Gandhi). Equal editorial care and visual proof must be given to economic funds, infrastructure, defence appointments, enforcement seizures, scientific data, weather, and sports.
  - Every story beat must have its own assigned visual proof plate and clear attribution.

---

### 5.6 Autonomous Execution vs. Retrieval Feasibility

- **Rule on User Permission:**
  - Once the user gives confirmation or direction (e.g., *"I have reuse permission for all clips"* or *"proceed with these sources"*), that confirmation is permanent for the workflow. The AI must **never repeatedly re-prompt the user for permission**.
- **Rule on Retrieval Feasibility (Technical Failures):**
  - A technical failure to download third-party files (e.g. HTTP 403, Cloudflare/bot challenge, login wall, private account) is entirely separate from user permission.
  - If a file cannot be retrieved due to technical barriers, do NOT stall the production and do NOT ask for permission again. Immediately and autonomously fall back to verified public stills, official data cards, and high-resolution agency releases, documenting the technical reason in the asset audit ledger (`PUBLIC_VIDEO_AUDIT.md`).

---

### 5.7 Current Worldwide & India 24H Production Dossier

The complete production assets for `projects/india_last_24h/` are verified and tracked:
- **Project Path:** `projects/india_last_24h/`
- **Topic:** India & Worldwide 24-Hour Intelligence Roundup (7 October 2026).
- **Format:** 9:16 Shorts · 1080×1920 · 24fps · Duration: 118.07 seconds.
- **Master Video:** `VIDEOS/10_India_Last_24H_SHORT_118s.mp4`.
- **Narration Audio Stems:** `narration_01.mp3` (65.38s) + `narration_02.mp3` (53.50s) -> `delivery/narration_final.wav`.
- **Scene Timings:** 14 scenes synchronized via character-weighted narration timestamps (`narration_timing.json` & `delivery/scene_timing.json`).
- **Images:** 14 full-bleed plates (`preview_bg_01.jpg` through `14.jpg`, `render_frame_01.jpg` through `14.jpg`), incorporating official PIB SME graphics, ITLA transport charter, Air Chief portrait, DRI gold seizure photos, NCS earthquake seismograph, and BCCI scorecard.
- **Color Grading:** **Profile A (Neutral Documentary Grade)** — crisp natural contrast, clean whites, zero orange/sepia tint.
- **Source Ledger:** `RESEARCH_FACT_LEDGER.md`, `SOURCES.md`, `PUBLIC_ASSET_MANIFEST.md`, `PUBLIC_VIDEO_AUDIT.md`.
- **QA Results:** `delivery/TECHNICAL_QC.txt` (Full decode test passed, 0 freeze frames, -14.2 LUFS integrated loudness).

