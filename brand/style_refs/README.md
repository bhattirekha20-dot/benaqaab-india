# 🛡️ BROADCAST VIDEO COPYRIGHT PROTECTION & FORENSIC STYLIZATION
### Official Benaqaab India Visual Treatment Standard for External Footage

---

## 📌 Origin & Mandate
To ensure 100% fair-use protection and defeat automated YouTube Content ID copyright detection on broadcast government/news clips (such as Ministry of External Affairs press briefings, Parliament footage, or court proceedings), all external video clips must pass through the **Benaqaab Forensic Stylization Filter**.

---

## 🖼️ Reference Assets

### 1. `source_footage_ref.png` (535×863)
* **Visual Anchor:** Dr. S. Jaishankar (Minister of External Affairs) speaking at an international forum.
* **Filter Stack:**
  1. High-contrast monochrome / desaturated base.
  2. Newsprint dot-matrix halftone texture (organic newspaper dot grid).
  3. Matte red horizontal censorship bar (`#ef4444`, 65% opacity) over the eye line / focal subject.

### 2. `source_footage_style_demo.jpg` (1532×800)
* **Proof Demonstration:** Side-by-side comparison of MEA spokesperson Randhir Jaiswal:
  - **Left:** Original reference anchor.
  - **Center:** Applied to 9:16 vertical Shorts format.
  - **Top Right:** Original broadcast clip.
  - **Bottom Right:** Applied to 16:9 horizontal documentary format.

---

## 💻 AI Agent Implementation Directive
Whenever an AI agent composites external source footage in `comp.html` or through `viz/motion.js`:
- Never display raw unedited broadcast news footage.
- Always apply the halftone screen overlay and red redaction bar (`drawRedactionPeel` or static bar) as codified in `BENAQAAB_FORENSIC_MOTION_SYSTEM.md`.
