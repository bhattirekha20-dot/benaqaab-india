---
name: antigravity-design-expert
description: >-
  Expert system for crafting spatial, weightless, and high-end futuristic interfaces ("Antigravity UI").
  Use this skill when designing bleeding-edge landing pages, dark-mode SaaS dashboards, spatial depth interfaces,
  glassmorphism layouts, glowing ambient orbs, interactive 3D cards, noise textures, and ultra-premium modern visuals.
---

# 🌌 Antigravity Design Expert — Spatial & Weightless UI

Antigravity Design is a signature visual aesthetic characterized by perceived weightlessness, luminous depth, volumetric lighting, and tactile glass surfaces. It turns standard flat screens into immersive digital environments.

---

## 💎 The 4 Pillars of Antigravity Aesthetics

1. **Atmospheric Depth (Z-Space Hierarchy)**:
   - Elements do not sit on a flat background; they float in space.
   - Closer elements have stronger specular borders, higher brightness, larger blur shadows, and faster parallax displacement.
2. **Volumetric Luminescence (The Ambient Glow)**:
   - Soft, slow-pulsing background radial gradients (orbs) that provide indirect lighting to frosted glass panels above them.
3. **Tactile Glassmorphism (Physical Realism)**:
   - Multi-layer borders: crisp 1px highlight at the top, softer edge on sides, deep dark shadow below.
   - High saturation background blur (`backdrop-filter: blur(20px) saturate(190%)`).
4. **Micro-Grain Texture (Organic Anti-Banding)**:
   - A fine 3-5% opacity SVG noise layer across the viewport. It eliminates digital gradient banding and adds filmic texture.

---

## 🎨 Token Architecture & CSS Recipes

### 1. The Obsidian Cosmic Canvas
```css
:root {
  --canvas-deep: #06080d;
  --canvas-surface: rgba(14, 18, 28, 0.75);
  --canvas-elevated: rgba(22, 28, 44, 0.85);

  --glow-cyan: rgba(56, 189, 248, 0.15);
  --glow-violet: rgba(168, 85, 247, 0.18);
  --glow-amber: rgba(251, 191, 36, 0.12);

  --glass-border: rgba(255, 255, 255, 0.08);
  --glass-highlight: rgba(255, 255, 255, 0.16);
}

body {
  background-color: var(--canvas-deep);
  color: #f1f5f9;
  font-family: 'Outfit', 'Inter', -apple-system, sans-serif;
  overflow-x: hidden;
  position: relative;
}
```

### 2. Ambient Floating Glowing Orbs
```html
<div class="ambient-glow glow-1"></div>
<div class="ambient-glow glow-2"></div>
```

```css
.ambient-glow {
  position: fixed;
  border-radius: 50%;
  filter: blur(100px);
  pointer-events: none;
  z-index: 0;
  opacity: 0.6;
  animation: floatOrb 18s ease-in-out infinite alternate;
}

.glow-1 {
  width: 500px;
  height: 500px;
  top: -100px;
  right: -50px;
  background: radial-gradient(circle, var(--glow-violet) 0%, rgba(0,0,0,0) 70%);
}

.glow-2 {
  width: 600px;
  height: 600px;
  bottom: -150px;
  left: -100px;
  background: radial-gradient(circle, var(--glow-cyan) 0%, rgba(0,0,0,0) 70%);
  animation-duration: 24s;
  animation-delay: -7s;
}

@keyframes floatOrb {
  0% { transform: translate3d(0, 0, 0) scale(1); }
  50% { transform: translate3d(60px, 40px, 0) scale(1.15); }
  100% { transform: translate3d(-40px, 80px, 0) scale(0.95); }
}
```

### 3. Organic Film Noise Overlay
```html
<div class="noise-overlay" aria-hidden="true"></div>
```

```css
.noise-overlay {
  position: fixed;
  inset: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
  z-index: 999;
  opacity: 0.035;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.8' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)'/%3E%3C/svg%3E");
}
```

### 4. Interactive Spotlight Follow Card
Moves a subtle radial highlight under the mouse cursor across cards:

```javascript
function initSpotlightCards() {
  const cards = document.querySelectorAll('.spotlight-card');
  
  cards.forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      card.style.setProperty('--mouse-x', `${x}px`);
      card.style.setProperty('--mouse-y', `${y}px`);
    });
  });
}
```

```css
.spotlight-card {
  position: relative;
  background: rgba(15, 20, 32, 0.6);
  border-radius: 20px;
  border: 1px solid rgba(255, 255, 255, 0.06);
  backdrop-filter: blur(16px);
  overflow: hidden;
}

.spotlight-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0; bottom: 0;
  background: radial-gradient(
    600px circle at var(--mouse-x, -1000px) var(--mouse-y, -1000px),
    rgba(255, 255, 255, 0.08),
    transparent 40%
  );
  pointer-events: none;
  transition: opacity 0.5s ease;
}
```

---

## 🪄 Typography That Demands Attention

Pairing is everything. For Antigravity UI:
- **Headline Display**: `Syne`, `Outfit`, or `Clash Display` (Bold, wide, high-impact).
- **Secondary Body**: `Inter` or `Plus Jakarta Sans` with loose letter spacing and high line height.
- **Accents & Eyebrows**: `Space Grotesk` or `JetBrains Mono` with uppercase tracking (`letter-spacing: 0.18em`).

```html
<span class="eyebrow-tag">NEXT GENERATION PLATFORM</span>
<h1 class="hero-display">
  Architected for <span class="gradient-text">Zero Resistance</span>
</h1>
```

```css
.eyebrow-tag {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  border-radius: 999px;
  background: rgba(56, 189, 248, 0.08);
  border: 1px solid rgba(56, 189, 248, 0.25);
  color: #38bdf8;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.15em;
  text-transform: uppercase;
}

.gradient-text {
  background: linear-gradient(135deg, #38bdf8 0%, #818cf8 50%, #c084fc 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}
```
