# 🏛️ ASSET MANIFEST — Brand Identity, Watermarks & Host Avatars
### Visual Asset Mapping & Significance Guide for AI Agents

All files in `brand/` establish the core visual identity, authenticity, and presentation rules for Benaqaab India:

---

## 🏷️ Brand Identity & Logos (`brand/`)

| File Name | Resolution | Archetype | Factual & Visual Significance | Agent Drawing Directive |
|---|---|---|---|---|
| `benaqaab_os_logo.png` | `192×192` (PNG Alpha) | Canonical Channel Logo Bug | Official high-resolution transparent channel mark. | Place on top-left of every video composition (`top: 36px, left: 32px` on 1080×1920). Opacity: 85–95%. |
| `logo.png` | `192×192` (PNG Alpha) | Root Brand Watermark | Identical alias of `benaqaab_os_logo.png` ensuring backward compatibility for legacy scripts. | Used interchangeably with `benaqaab_os_logo.png`. |
| `ref_investigative_1.png` | `1135×440` | Typographic Benchmark | High-contrast card border and bold sans-serif headline standards. | Reference for 1px translucent card borders and type hierarchy. |
| `ref_investigative_2.png` | `1702×377` | Pinboard Wireframe Benchmark | Multi-node connecting lines and 2X loupe reticle layouts. | Reference when rendering pinboard connections in `comp.html`. |
| `ref_investigative_3.png` | `1120×367` | Split-Screen Breaking News Benchmark | Multi-window comparative evidence layouts. | Reference for dual-source breaking news verification. |
| `reference_minimal_fullscreen.png` | `316×505` | Minimal Layout Benchmark | Chenab Bridge style 65–75% screen occupancy minimalism with 2-word caption pills. | Enforce generous breathing room and zero clutter. |

---

## 🎙️ Host Lip-Sync & Avatar Overlays (`brand/host/`)
* **Core Rule:** Presenter screen time must be **strictly under 20%** of total video duration. Visual journalism prioritizes the evidence, not the presenter.
* **Phoneme Frames (`host_base.jpg`, `host_mid.jpg`, `host_open.jpg`):** Discrete mouth shapes (closed, mid, open) driven by voiceover audio RMS amplitude:
  - `host_base.jpg` (Closed): Audio RMS < 0.05
  - `host_mid.jpg` (Mid Open): Audio RMS 0.05 – 0.18
  - `host_open.jpg` (Full Open): Audio RMS > 0.18
* **Alpha Cutouts (`host_rgba_0.png`, `host_rgba_1.png`, `host_rgba_2.png`):** Transparent presenter cutouts anchored to bottom corners with scale < 35% of viewport height.

---

## 🛡️ Fair-Use Broadcast Styling (`brand/style_refs/`)
* `source_footage_ref.png` & `source_footage_style_demo.jpg`: The official newsprint halftone filter + red redaction bar applied over broadcast clips to defeat automated copyright strikes while reinforcing our forensic style.
