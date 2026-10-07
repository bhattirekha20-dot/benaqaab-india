# 🌍 ASSET MANIFEST — World News 24H (SH-11)
### Visual Asset Mapping & Significance Guide for AI Agents

Every image in `projects/world_news_24h/` is mapped to its exact factual story and timeline position in `comp.html`:

---

## 📸 Verified Primary-Source News Photos (`assets/`)

| File Name | Story / Topic | Time (comp.html) | Factual Significance | Agent Drawing Directive |
|---|---|---|---|---|
| `photo_germany.jpg` | **Story 1: Germany** | `0.0s – 14.0s` | Real news photo of Germany BND domestic intelligence arrest of accused Russian saboteur/spy in Frankfurt. | Background layer with slow Ken Burns scale `1.00 -> 1.05` over 12s. Pair with yellow highlighter on BND press release text. |
| `photo_france.jpg` | **Story 2: France** | `14.0s – 25.0s` | Editorial photo of French high school student walkouts and anti-austerity school protests in Paris. | Render at center safe area. Reveal via 0.3s exponential scale pop (`cubic-bezier(0.16, 1, 0.3, 1)`). |
| `photo_kenya.jpg` | **Story 3: Kenya** | `25.0s – 36.0s` | Official photo of Kenyan public health isolation ward and airport screening protocols for suspected hemorrhagic fever. | Composite with semi-transparent medical telemetry overlay. Highlight isolation quarantine timeline. |
| `photo_quebec.jpg` | **Story 4: Quebec** | `36.0s – 44.0s` | Polling station ballot box and voter verification in Quebec provincial by-election. | Center on ballot box. Layer red redaction peel on vote share numbers before odometer roll. |
| `photo_icecube.jpg` / `photo_science.jpg` | **Story 5: Physics Nobel** | `44.0s – 54.0s` | Antarctica IceCube Neutrino Observatory sensor array discovering ultra-high-energy cosmic neutrinos. | Hero visual behind scientific formula. Highlight Nobel committee citation text. |
| `photo_check.jpg` / `check.jpg` | **Verification Stamp** | End of Stories | Green verification checkmark icon certifying primary source authentication. | Stamp at top right of evidence cards (`X: 820, Y: 280`). |

---

## 🎨 Neutral Atmospheric Backgrounds (`assets/neutral/`)
* **Purpose:** Soft 8px-blurred thematic textures used behind transparent documents, graphs, and loupe reticles.
* **Files:** `ai_ballot.jpg` (Elections), `ai_classroom.jpg` (Education/Protests), `ai_health.jpg` (Medicine), `ai_investigation.jpg` (Intelligence/Courts), `ai_world.jpg` (Geopolitics).
* **Color Grading:** Adheres to **Profile A: Neutral News** (6200K temperature, contrast 1.06, saturation 1.02).

---

## 🖼️ Delivery Covers & Thumbnails (`delivery/`)
* `thumbnail_1280x720.jpg`: 16:9 landscape YouTube thumbnail with bold 4-word hook (*"5 BADI KHABAREIN"*), top-left channel logo bug, and uncropped safe margins.
* `cover_vertical_1080x1920.jpg` / `shorts_thumbnail*.jpg`: 9:16 vertical cover for YouTube Shorts and mobile feed previews.

---

## 🔍 QA Frame Verifications (`delivery/qa/` & `qa/`)
* 11 timestamped frame captures (`frame_0.jpg` to `frame_57.5.jpg`) used by `tools/lint_safe_zones.py` to mathematically verify zero text obstruction by YouTube mobile UI elements.
