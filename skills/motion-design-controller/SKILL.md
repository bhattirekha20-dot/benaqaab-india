---
name: motion-design-controller
description: >-
  Master motion design, web animation, and kinetic choreography skill.
  Use this skill whenever creating animations, UI motion, GSAP timelines, Framer Motion springs,
  smooth scrolling (Lenis), CSS micro-interactions, canvas/WebGL choreography, 3D tilt effects,
  scroll-driven interactions, or cinematic transitions.
---

# ⚡ Motion Design Controller — Master Motion & Animation Engine

The Motion Design Controller provides precise engineering patterns, physics-based springs, timeline choreography, and micro-interaction mechanics to make digital interfaces feel alive, fluid, and cinematic.

---

## 🎯 The 5 Core Laws of UI Motion

1. **Purpose-Driven Motion**: Every animation must serve a purpose: guide attention, establish spatial relationship, or give feedback. Never animate merely for decoration.
2. **Snappy Over Laggy**: UI interactions (clicks, hovers, toggles) should complete between `150ms - 250ms`. Modals and drawers between `300ms - 450ms`. Complex page transitions between `500ms - 800ms`.
3. **Physics-First Easing**: Avoid linear movement. Natural objects accelerate and decelerate with friction and momentum. Always use spring physics or customized cubic-bezier curves.
4. **Compositor-Only Properties**: ONLY animate properties that trigger GPU composition without reflow or repaint:
   - ✅ `transform` (`translate3d`, `scale`, `rotate`)
   - ✅ `opacity`
   - ✅ `filter` (with caution)
   - ❌ NEVER animate `top`, `left`, `width`, `height`, `margin`, or `padding`.
5. **Reduced Motion Respect**: Always respect user accessibility preferences via `@media (prefers-reduced-motion: reduce)`.

---

## 🏎️ Premium Easing Curves Catalog

Use these fine-tuned cubic-bezier curves for instant professional feel:

```css
:root {
  /* Fast entrance with gentle deceleration */
  --ease-out-expo: cubic-bezier(0.16, 1, 0.3, 1);
  
  /* Snappy dynamic pop */
  --ease-out-back: cubic-bezier(0.34, 1.56, 0.64, 1);
  
  /* Velvety smooth luxury motion */
  --ease-smooth: cubic-bezier(0.25, 0.1, 0.25, 1);
  
  /* Cinematic slow-down */
  --ease-cinematic: cubic-bezier(0.05, 0.7, 0.1, 1);
  
  /* Natural spring equivalent */
  --ease-spring: cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
```

---

## 🎬 GSAP 3 Master Recipes (Timelines & ScrollTrigger)

When building complex sequences or scroll animations, **GSAP (GreenSock)** is the gold standard:

### 1. Staggered Hero Reveal Timeline
```javascript
import gsap from 'gsap';

// Create a master timeline
const tl = gsap.timeline({ defaults: { ease: 'power4.out', duration: 1.0 } });

tl.from('.hero-eyebrow', {
  y: -20,
  opacity: 0,
  duration: 0.6
})
.from('.hero-title-word', {
  y: 60,
  opacity: 0,
  rotateX: -20,
  stagger: 0.08,
  duration: 1.2
}, '-=0.3')
.from('.hero-description', {
  y: 30,
  opacity: 0,
  duration: 0.8
}, '-=0.7')
.from('.hero-cta-group > *', {
  y: 20,
  opacity: 0,
  stagger: 0.15,
  ease: 'back.out(1.7)',
  duration: 0.7
}, '-=0.5')
.from('.hero-visual-card', {
  scale: 0.9,
  opacity: 0,
  y: 40,
  duration: 1.4,
  ease: 'power3.out'
}, '-=0.8');
```

### 2. ScrollTrigger Parallax & Reveal
```javascript
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
gsap.registerPlugin(ScrollTrigger);

// Pinning & Scrubbing showcase
gsap.to('.parallax-layer-back', {
  yPercent: 30,
  ease: 'none',
  scrollTrigger: {
    trigger: '.showcase-section',
    start: 'top bottom',
    end: 'bottom top',
    scrub: true
  }
});

// Staggered Bento Cards Scroll Reveal
gsap.from('.bento-item', {
  scrollTrigger: {
    trigger: '.bento-grid',
    start: 'top 80%',
    toggleActions: 'play none none reverse'
  },
  y: 50,
  opacity: 0,
  duration: 0.8,
  stagger: 0.12,
  ease: 'power3.out'
});
```

---

## 🌊 Framer Motion & Spring Physics Patterns

For React applications, use Framer Motion with realistic spring damping:

```jsx
import { motion } from 'framer-motion';

// Natural bouncy spring transition
export const springTransition = {
  type: "spring",
  stiffness: 380,
  damping: 30,
  mass: 0.8
};

// Cinematic smooth card
export const SmoothCard = ({ children }) => (
  <motion.div
    initial={{ opacity: 0, y: 30, scale: 0.96 }}
    whileInView={{ opacity: 1, y: 0, scale: 1 }}
    viewport={{ once: true, margin: "-50px" }}
    transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
    whileHover={{ 
      y: -6, 
      scale: 1.015, 
      transition: springTransition 
    }}
    whileTap={{ scale: 0.98 }}
    className="pro-card"
  >
    {children}
  </motion.div>
);
```

---

## 🧲 Interactive Micro-Interactions

### 1. Magnetic Hover Button (Vanilla JS)
Buttons that pull gently toward the user's cursor:

```javascript
function initMagneticButtons() {
  const magnets = document.querySelectorAll('[data-magnetic]');
  
  magnets.forEach(btn => {
    btn.addEventListener('mousemove', (e) => {
      const rect = btn.getBoundingClientRect();
      const x = e.clientX - (rect.left + rect.width / 2);
      const y = e.clientY - (rect.top + rect.height / 2);
      
      // Pull button slightly (e.g. 35% of offset)
      btn.style.transform = `translate3d(${x * 0.35}px, ${y * 0.35}px, 0)`;
    });
    
    btn.addEventListener('mouseleave', () => {
      btn.style.transform = 'translate3d(0, 0, 0)';
      btn.style.transition = 'transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275)';
      setTimeout(() => { btn.style.transition = ''; }, 500);
    });
  });
}
```

### 2. 3D Perspective Tilt Card
```javascript
function initTiltCards() {
  document.querySelectorAll('.tilt-card').forEach(card => {
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = (e.clientX - rect.left) / rect.width - 0.5;
      const y = (e.clientY - rect.top) / rect.height - 0.5;
      
      const tiltX = y * -15; // Max 15deg tilt
      const tiltY = x * 15;
      
      card.style.transform = `perspective(1000px) rotateX(${tiltX}deg) rotateY(${tiltY}deg) scale3d(1.02, 1.02, 1.02)`;
    });
    
    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
      card.style.transition = 'transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)';
      setTimeout(() => { card.style.transition = ''; }, 600);
    });
  });
}
```

### 3. Smooth Butter Scroll (Lenis Integration)
```javascript
import Lenis from 'lenis';

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // smooth exponential
  smoothWheel: true,
  touchMultiplier: 1.5,
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);
```

---

## 📋 Pre-Flight Animation Checklist

- [ ] Does every animation use `transform` or `opacity`?
- [ ] Are hover interactions under `250ms`?
- [ ] Are staggered child reveals offset between `0.06s` and `0.12s`?
- [ ] Is there an active state for mobile touch devices?
- [ ] Does `@media (prefers-reduced-motion: reduce)` disable non-essential motion?
- [ ] Is GPU layer promotion (`will-change: transform`) applied only to active animating elements?
