---
name: frontend-design-auditor
description: >-
  Quality assurance, correctness linter, and design auditor for websites and web applications.
  Use this skill to audit UI/UX quality, check responsiveness across mobile/tablet/desktop, verify WCAG accessibility,
  detect layout shifts (CLS), validate color contrast ratios, inspect typography scales, and eradicate visual bugs.
---

# 🔍 Frontend Design Auditor — Quality Assurance & UX Linter

The Frontend Design Auditor acts as a strict, senior design director and web performance engineer. It scrutinizes every interface for design polish, accessibility failures, typography defects, and usability friction.

---

## 🚦 The 10-Point Production Audit Matrix

Run every web interface through this 10-point audit before finalizing:

### 1. Contrast & Readability (WCAG 2.1 AA/AAA)
- [ ] Body text on dark backgrounds must have at least **4.5:1** contrast ratio (preferred: `#94a3b8` on `#0b0d14` gives 7.2:1).
- [ ] Large headings (>= 24px) must have at least **3:1** contrast ratio.
- [ ] Subdued captions/metadata must never drop below **3.0:1**.
- [ ] Interactive link/button states must remain distinct in both focused and unfocused states.

### 2. Spacing & Rhythm Alignment
- [ ] All margins and paddings must align to the 4px / 8px scale.
- [ ] No arbitrary pixel values like `margin-top: 13px;` or `gap: 27px;`.
- [ ] Grouped related elements (e.g. title and description) have smaller spacing (`8px - 12px`) than distinct sections (`32px - 64px`).

### 3. Typography & Hierarchy Integrity
- [ ] Exactly **one** `<h1>` element per page.
- [ ] Heading levels do not skip (e.g. `<h1>` followed by `<h3>` is forbidden).
- [ ] Line heights:
  - Hero headings: `1.05 - 1.15`
  - Section headers: `1.2 - 1.3`
  - Body paragraphs: `1.5 - 1.7`
- [ ] Maximum line length for body text does not exceed **65 - 75 characters** (`max-width: 65ch`) to prevent eye fatigue.

### 4. Touch & Interaction Ergonomics
- [ ] All clickable buttons, links, and inputs have a minimum target size of **44x44px** on touch devices.
- [ ] Every clickable element has distinct `:hover`, `:focus-visible`, and `:active` styles.
- [ ] Focus rings are clearly visible for keyboard navigation (`outline: 2px solid var(--accent); outline-offset: 2px`).

### 5. Layout Shifts & CLS (Cumulative Layout Shift)
- [ ] All images and video canvases have explicit `width` and `height` or `aspect-ratio` defined to eliminate layout popping during load.
- [ ] Web fonts use `font-display: swap` with matched fallback metrics to prevent severe layout jump on font load.

### 6. Responsive Breakpoints & Viewport Stress Test
- [ ] **Mobile (375px - 428px)**: No horizontal scrolling. Hamburger/bottom bar navigation. Touch-friendly targets. Single-column card stacks.
- [ ] **Tablet (768px - 1024px)**: 2-column grids. Balanced margins.
- [ ] **Desktop (1280px - 1440px)**: 3-column / Bento layouts. Maximum content container width capped (`max-width: 1280px` or `1440px`).
- [ ] **Ultrawide (1920px - 2560px)**: Content remains centered; no awkward stretching or edge-to-edge text drift.

### 7. Motion & Frame Budget
- [ ] Animations run at a rock-solid 60FPS with zero jank or frame dropping.
- [ ] Animations do not animate reflow properties (`width`, `height`, `margin`, `top`, `left`).
- [ ] `@media (prefers-reduced-motion: reduce)` is respected, turning off heavy parallax or continuous motion loops.

### 8. Anti-AI-Slop & Soul Check
- [ ] Does the page look like a generic Bootstrap or standard Tailwind template? If yes, REVISE.
- [ ] Are the color palettes nuanced and bespoke rather than default primary blue/purple?
- [ ] Is there atmospheric polish (subtle grain, layered shadows, glass highlights)?

### 9. Forms & Error Handling
- [ ] Form inputs have clear labels (not just placeholder text that disappears on focus).
- [ ] Error messages are explicit, helpful, and placed directly adjacent to the offending input.
- [ ] Submit buttons show an unambiguous loading/disabled state while processing.

### 10. Performance & Bundle Hygiene
- [ ] No uncompressed multi-megabyte assets loaded on initial render.
- [ ] Heavy dependencies are tree-shaken or lazily loaded.
- [ ] SVGs are cleaned of unnecessary metadata and editor artifacts.
