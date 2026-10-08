---
name: ui-ux-pro-max
description: >-
  Advanced UI/UX design intelligence and reasoning engine for web applications, websites, and digital interfaces.
  Use this skill whenever designing or building user interfaces, modern websites, web apps, component design systems,
  color palettes, typography hierarchies, layout systems, or when eliminating generic "AI slop" in frontends.
---

# 🎨 UI/UX Pro Max — Master Design Intelligence

UI/UX Pro Max is a comprehensive design reasoning framework engineered to eliminate generic, uninspired AI interfaces ("AI slop") and produce stunning, world-class digital products that feel handcrafted by top-tier product designers.

---

## 🚫 The Anti-"AI-Slop" Manifesto

Most AI-generated websites look identical: generic purple/blue gradients, centered Hero text, 3 identical rounded cards, Inter font, and zero soul. **Never make interfaces that look like templates.**

### Forbidden Clichés vs. Pro Replacements

| AI Cliché (FORBIDDEN) | Pro Replacement |
| :--- | :--- |
| Generic purple-to-blue gradient on pure `#000` | Custom multi-stop mesh gradients with deep chromatic blacks (`#07090E`, `#0A0D14`, `#0D1117`) |
| Centered H1 + subtitle + generic button | Asymmetric editorial layout, prominent eyebrow tag, dynamic hero badge, dual-action CTAs |
| 3 identical cards with generic Lucide icons | Varied Bento Grid (1x2, 2x1, 1x1 cells) with interactive widgets, live previews, data callouts |
| Browser-default system fonts or plain Inter | Curated typography pairings: Editorial Serif (Playfair, Instrument Serif) or Geometric Display (Outfit, Plus Jakarta Sans, Syne) + crisp Body (Inter, Satoshi) |
| Hard flat boxes without elevation | Multi-layer elevation: subtle border (`rgba(255,255,255,0.08)`), diffuse ambient shadow, frosted glass reflection |
| Static non-interactive elements | Micro-interactions: magnetic hover, subtle spring scale (1.02), shimmer borders, dynamic cursor reactions |

---

## 📐 The 7 Golden Laws of Visual Hierarchy

1. **The 60-30-10 Color Rule**:
   - **60% Dominant Base**: Deep dark slate/obsidian or pristine warm off-white (`#F8F9FA`).
   - **30% Structural Secondary**: Surfaces, cards, navigation, drawers (`rgba(255,255,255,0.03)` to `0.06`).
   - **10% High-Impact Accent**: Primary brand pop (Vibrant Amber `#FFB800`, Electric Cyan `#00F2FE`, Neon Emerald `#10B981`, Hot Coral `#FF4D4D`).

2. **Typography Scale & Contrast (Major Third / 1.25 Ratio)**:
   - Eyebrow / Overline: `11px - 13px`, Uppercase, tracking `+0.12em` to `+0.2em`, bold (`700`).
   - H1 Display Hero: `48px - 72px` (Desktop), line-height `1.05 - 1.15`, letter-spacing `-0.03em`.
   - H2 Section Headline: `32px - 44px`, letter-spacing `-0.025em`, font-weight `700`.
   - H3 Card / Subheader: `20px - 26px`, letter-spacing `-0.015em`, font-weight `600`.
   - Body Text: `15px - 17px`, line-height `1.6 - 1.7`, high legibility, color `#94A3B8` (dark mode) or `#475569` (light mode).
   - Data / Code: `12px - 14px`, JetBrains Mono or Fira Code, tracking `-0.01em`.

3. **Spatial Cadence (8pt Grid System)**:
   - Spacings must strictly follow multiples of 4 and 8: `4px, 8px, 12px, 16px, 24px, 32px, 48px, 64px, 96px, 128px`.
   - Card internal padding: minimum `24px - 32px`.
   - Section vertical padding: `80px - 140px` on desktop, `48px - 80px` on mobile.

4. **Surface Depth & Glassmorphism Recipes**:
   ```css
   /* Pro Dark Glass Card */
   .pro-card {
     background: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.01) 100%);
     backdrop-filter: blur(16px) saturate(180%);
     -webkit-backdrop-filter: blur(16px) saturate(180%);
     border: 1px solid rgba(255, 255, 255, 0.08);
     box-shadow: 
       0 4px 24px -1px rgba(0, 0, 0, 0.4),
       0 0 0 1px rgba(255, 255, 255, 0.02) inset;
     border-radius: 20px;
     transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
   }

   .pro-card:hover {
     border-color: rgba(255, 255, 255, 0.18);
     transform: translateY(-3px);
     box-shadow: 
       0 12px 36px -4px rgba(0, 0, 0, 0.6),
       0 0 20px rgba(var(--accent-rgb), 0.15);
   }
   ```

5. **Bento Grid Architecture**:
   Never display all features equally. A hero feature gets a large 2-column or 2-row card with an interactive preview or live demonstration. Secondary features get compact 1-column cards.
   ```
   +---------------------------------------+-------------------+
   |                                       |                   |
   |   HERO FEATURE (2x1 Bento Tile)       | STAT / METRIC     |
   |   - Interactive Chart / Live Mockup   | - Big 99.8% Stat  |
   |                                       |                   |
   +-------------------+-------------------+-------------------+
   | QUICK ACTION      | DETAIL WIDGET     | INTEGRATION LOGOS |
   | - Micro-tool      | - Animated badge  | - Infinite marquee|
   +-------------------+-------------------+-------------------+
   ```

6. **CTA (Call to Action) Hierarchy**:
   - **Primary CTA**: High contrast, vivid gradient or solid accent, glowing aura, micro-bounce on click, clear action verb (`"Start Free Trial ->"`).
   - **Secondary CTA**: Ghost/glass border button, neutral text with white hover, clear contrast distinction.
   - **Tertiary CTA**: Text-only with animated underline on hover.

7. **Psychology & UX Heuristics**:
   - **Hick’s Law**: Minimize choices. One primary action per viewport.
   - **Fitts’s Law**: Make clickable areas generous (minimum 44x44px touch targets).
   - **Jakob’s Law**: Keep standard patterns recognizable (nav at top, close 'X' top right, search with magnifying glass).
   - **Peak-End Rule**: End interactions with a delightful confirmation, smooth exit, or confetti/glow feedback.

---

## 🎨 Production Color Palette Tokens

```css
:root {
  /* Obsidian Chromatic Base */
  --bg-dark: #07090e;
  --bg-surface: #0e121a;
  --bg-card: rgba(18, 24, 38, 0.7);
  
  /* Text Tokens */
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --text-muted: #64748b;
  
  /* Accents */
  --accent-primary: #38bdf8;        /* Electric Sky */
  --accent-secondary: #818cf8;      /* Soft Indigo */
  --accent-vibrant: #f43f5e;        /* Rose Flame */
  --accent-gold: #fbbf24;           /* Warm Amber */
  --accent-emerald: #34d399;        /* Mint Glow */
  
  /* Borders */
  --border-subtle: rgba(255, 255, 255, 0.07);
  --border-active: rgba(255, 255, 255, 0.18);
  --border-glow: rgba(56, 189, 248, 0.3);
}
```

---

## 🛠️ Step-by-Step UI Execution Workflow

1. **Define Context & Mood**: Identify target vibe (Cyber Minimal, Warm Editorial, High-Tech SaaS, Luxury Glass).
2. **Setup Foundations**: Load Google Fonts (e.g., `Outfit` + `Inter`), CSS custom properties, and reset styles.
3. **Assemble Hero Section**: Eyebrow badge, magnetic heading with highlighted keyword gradient, dual CTAs, social proof bar.
4. **Construct Layout**: Build asymmetrical Bento Grid for feature highlights with varied cell weights.
5. **Add Life & Motion**: Incorporate subtle ambient background glows, button hover physics, scroll entrances, and interactive state indicators.
6. **Audit Mobile**: Ensure all grids collapse cleanly to 1-column at `<= 768px` with no horizontal overflow.
