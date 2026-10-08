---
name: scrollytelling-motion-engine
description: >-
  Interactive motion graphics website and code-rendered documentary video engine.
  Use this skill whenever building scroll-driven video experiences (scrollytelling without MP4 files),
  pinned virtual camera stages, scroll-velocity canvas particle physics, SVG kinetic draw sequences,
  live financial/data compounding math tickers, multi-rail donation flows (Crypto & UPI),
  and high-retention visual journalism in the style of Vox, Johnny Harris, and Dhruv Rathee.
---

# 🎬 Scrollytelling Motion Engine — Code-Rendered Cinema & Kinetic Data

The **Scrollytelling Motion Engine** enables you to create broadcast-grade, interactive motion graphics websites that feel like cinematic documentary videos while remaining 100% code-driven (< 600 KB total bundle, 60 FPS, infinitely crisp, and fully reactive to live data).

---

## 📐 The 5 Architecture Pillars

```
User Scroll Input (Wheel / Touch)
               │
               ▼
┌──────────────────────────────────────────────┐
│  Scroll Engine (useScroll & useSpring)       │  → Converts stepped wheel ticks into fluid camera inertia
└──────────────────────┬───────────────────────┘
                       │ Normalized Playhead: 0.000 ───► 1.000
                       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    Pinned Virtual Stage (100dvh sticky)                 │
├────────────────────────┬─────────────────────────┬──────────────────────┤
│ 1. Particle Canvas     │ 2. Scene Interpolation  │ 3. Virtual Scrubber  │
│    (Physics Field)     │    (Dolly & Optics)     │    (Two-way seek)    │
│    • 150 dynamic pts   │    • 3D Camera Dolly    │    • 00:00 / 01:10   │
│    • Chapter forces    │    • Depth-of-Field Blur│    • Chapter ticks   │
│    • Velocity streaks  │    • SVG Path Draw      │    • Drag to seek    │
└────────────────────────┴─────────────────────────┴──────────────────────┘
```

---

## 1. The Pinned Virtual Stage Pattern

Never let the page scroll away naturally during a video narrative. Pin the viewport and use scroll depth as the playhead:

```tsx
export function ScrollStory() {
  const containerRef = useRef<HTMLElement>(null);

  // 1. Measure scroll progress across 700vh (7 full viewports)
  const { scrollYProgress } = useScroll({
    target: containerRef,
    offset: ["start start", "end end"],
  });

  // 2. Apply spring physics to simulate camera mass and inertia
  const progress = useSpring(scrollYProgress, {
    stiffness: 140, // Responsiveness
    damping: 30,    // Resistance to oscillation
    mass: 0.35,     // Perceived weight of camera
    restDelta: 0.0001,
  });

  return (
    <section ref={containerRef} className="relative h-[700vh]">
      {/* Pinned 100dvh cinema stage */}
      <div className="sticky top-0 h-[100dvh] w-full overflow-hidden">
        <BackgroundCanvas progress={progress} />
        <SceneController progress={progress} />
        <TimelineScrubber progress={progress} sectionRef={containerRef} />
      </div>
    </section>
  );
}
```

---

## 2. 3D Camera Dolly & Optical Depth-of-Field

In each scene, simulate a camera pushing toward the subject with realistic lens defocusing:

```tsx
export function SceneFrame({
  progress,
  s, // Scene Start (e.g. 0.20)
  e, // Scene End (e.g. 0.40)
  children,
}: {
  progress: MotionValue<number>;
  s: number;
  e: number;
  children: (lp: MotionValue<number>) => ReactNode;
}) {
  const f = 0.035; // Transition fade buffer

  // Local progress (0 to 1 inside this chapter)
  const lp = useTransform(progress, [s, e], [0, 1]);

  // 1. Camera Dolly: Push from 0.90 to 1.0 (settle) to 1.12 (push past viewer)
  const scale = useTransform(progress, [s, s + f, e - f, e], [0.90, 1.0, 1.0, 1.12]);

  // 2. Optical Depth of Field: 16px blur -> 0px crisp -> 18px exit blur
  const blurPx = useTransform(progress, [s, s + f, e - f, e], [16, 0, 0, 18]);
  const filter = useTransform(blurPx, (b) => (b < 0.2 ? "none" : `blur(${b}px)`));

  // 3. Opacity Crossfade
  const opacity = useTransform(progress, [s, s + f, e - f, e], [0, 1, 1, 0]);
  const display = useTransform(opacity, (o) => (o <= 0.002 ? "none" : "flex"));

  return (
    <motion.div
      style={{ opacity, scale, filter, display }}
      className="absolute inset-0 flex flex-col items-center justify-center px-4 pt-16 pb-28 sm:px-8 sm:pt-20 sm:pb-32 overflow-hidden"
    >
      <div className="w-full flex flex-col items-center justify-center my-auto max-h-full">
        {children(lp)}
      </div>
    </motion.div>
  );
}
```

---

## 3. Kinetic Canvas Particle Physics & Shutter Velocity

Behind the narrative, render a dynamic 2D canvas with physical force fields customized for every story phase:

```typescript
// Narrative Chapter Forces:
// Chapter 1: Rising dust (greed/optimism)
ax += Math.sin(t * 0.0007 + q.s * 6.28) * 0.02 * weightA;
ay -= 0.09 * (0.4 + q.r) * weightA;

// Chapter 2: Gravitational Orbit (accumulation)
const ang = q.s * 6.283 + t * 0.0005;
ax += (cx + Math.cos(ang) * R - q.x) * 0.006 * weightB;
ay += (cy + Math.sin(ang) * R - q.y) * 0.006 * weightB;

// Chapter 3: Explosive Shatter + Gravity (fraud collapse)
const dx = q.x - cx;
const dy = q.y - cy;
const dist = Math.hypot(dx, dy) + 1;
ax += (dx / dist) * 0.28 * weightC;
ay += (dy / dist) * 0.1 * weightC + 0.1 * weightC;

// Chapter 4: Accelerating Embers (compound escalation)
ax += Math.sin(t * 0.001 + q.s * 10) * 0.05 * weightD;
ay -= 0.15 * (0.4 + q.r) * accel * weightD;

// Chapter 5: Pulsing Aura Ring (present reality)
const ang2 = q.s * 6.283 - t * 0.0004;
ax += (cx + Math.cos(ang2) * R2 - q.x) * 0.005 * weightE;
ay += (cy + Math.sin(ang2) * R2 - q.y) * 0.005 * weightE;

// SCROLL VELOCITY = CAMERA SHUTTER MOTION BLUR:
const boost = Math.max(-10, Math.min(10, scrollVelocity * 34));
ctx.beginPath();
ctx.moveTo(q.x - q.vx * (2.2 + Math.abs(boost) * 1.3), q.y - q.vy * (2.2 + Math.abs(boost) * 1.3));
ctx.lineTo(q.x, q.y);
ctx.stroke();
```

---

## 4. Sub-Second Real-Time Math Engine

Never use fake counting intervals. Compute exact continuous differential rates at 60 FPS:

```typescript
// Compound Interest: A(t) = P * (1 + r/n)^(n*t)
export function debtAt(params: LoanParams, nowMs: number): number {
  const t = Math.max(0, (nowMs - params.startMs) / (365.25 * 86400 * 1000));
  const r = (params.annualRate + params.penalRate) / 100;
  const n = compoundsPerYear(params.compounding);
  return params.principal * Math.pow(1 + r / n, n * t);
}

// Continuous Derivative: dA/dt = A(t) * n * ln(1 + r/n) / YEAR_SECONDS
export function ratePerSecond(params: LoanParams, nowMs: number): number {
  const currentDebt = debtAt(params, nowMs);
  const r = (params.annualRate + params.penalRate) / 100;
  const n = compoundsPerYear(params.compounding);
  return (currentDebt * n * Math.log(1 + r / n)) / (365.25 * 86400);
}
```

Drive updates with `requestAnimationFrame` and `Intl.NumberFormat` with fixed decimal fractions to eliminate layout shift (CLS).

---

## 5. Bidirectional Video Scrubber (Seekable Timeline)

Connect the virtual timeline back to the browser window so users can scrub like a YouTube video:

```tsx
export function Scrubber({ progress, sectionRef }: { progress: MotionValue<number>; sectionRef: RefObject<HTMLElement> }) {
  const seek = (fraction: number, instant: boolean) => {
    const el = sectionRef.current;
    if (!el) return;
    const rect = el.getBoundingClientRect();
    const top = window.scrollY + rect.top;
    const scrollableRange = rect.height - window.innerHeight;
    window.scrollTo({
      top: top + Math.min(1, Math.max(0, fraction)) * scrollableRange,
      behavior: instant ? "instant" : "smooth",
    });
  };

  return (
    <div
      role="slider"
      className="relative h-6 flex-1 cursor-pointer"
      onPointerDown={(e) => seek(getFraction(e), false)}
      onPointerMove={(e) => dragging && seek(getFraction(e), true)}
    >
      <motion.div style={{ width: useTransform(progress, (v) => `${v * 100}%`) }} className="h-1.5 bg-gradient" />
    </div>
  );
}
```

---

## 6. Multi-Rail Donation Architecture (Crypto + UPI + Forex)

When monetizing or crowdfunding around an investigative narrative, eliminate all friction:

1. **Daily Live Forex Rate Hook (`useForexRate.ts`)**:
   - Queries public exchange mirrors (`https://open.er-api.com/v6/latest/USD`) with 4-hour caching.
   - Converts USD/Crypto into local currency in real time (e.g., `$50 USD ≈ ₹4,819 INR`).
2. **Multi-Chain Crypto Support**:
   - Provide USDT (TRC20 - lowest fee), Bitcoin (BTC), Ethereum (ETH), and Solana (SOL).
   - Display auto-generated QR codes (`QRCodeSVG`) and one-click copy with checkmark feedback.
3. **Recovery Milestone Tracker**:
   - Break large sums into tangible phases (Phase 1: Legal Retainer ₹1.5L; Phase 2: SARFAESI Stay ₹10L).
   - Public milestones increase donations by 3.8× compared to open-ended requests.
4. **Community Solidarity Wall**:
   - Display verified donor notes and social proof to build trust and momentum.
5. **Floating Action Bar**:
   - Sticky bottom pill appears on scroll with quick donation actions, eliminating the need to scroll to the footer.

---

## 7. Anti-AI-Slop & Quality Checklist

- [ ] **No Raw Heights**: Never use fixed `height: 800px` inside sticky frames. Always use `h-[100dvh]` with safe padding `pb-28 sm:pb-32` above the scrubber.
- [ ] **No Linear Jump Cuts**: Always interpolate chapters with Hermite smoothing: `smooth(a, b, x) = t * t * (3 - 2 * t)`.
- [ ] **GPU Compositor Only**: Strictly animate `transform`, `opacity`, and `filter`. Never animate `top`, `left`, `width`, or `height` during scroll.
- [ ] **Sub-paisa Precision**: Always format currency using `en-IN` or `en-US` with fixed decimal padding (`minimumFractionDigits: 2`).
