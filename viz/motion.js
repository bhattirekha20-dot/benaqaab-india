/* motion.js — browser port of viz/motion.py v2 (same maths, same numbers).
 *
 * Load with a classic <script src="motion.js"></script> (file:// safe) -> window.Motion
 * or require('./motion.js') in node (parity tests).
 *
 * Composition contract used by viz/hrender.py:
 *   window.seek(t)   draw frame at t seconds (pure function of t; may return a Promise)
 *   window.ready     true after fonts/images load
 *   window.DURATION  seconds;  optional window.FPS / WIDTH / HEIGHT
 *   window.speed(t)  optional: fastest on-screen speed, px/s  -> adaptive motion blur
 *   window.state(t)  optional: signature of everything visible -> safe frame reuse
 */
(function (root) {
  'use strict';
  const clamp01 = (x) => (x <= 0 ? 0 : x >= 1 ? 1 : x);
  const smoothstep = (x) => { x = clamp01(x); return x * x * (3 - 2 * x); };

  function cubicBezier(p1x, p1y, p2x, p2y) {
    const bez = (t, a, b) => 3 * (1 - t) ** 2 * t * a + 3 * (1 - t) * t * t * b + t ** 3;
    const slope = (t, a, b) => 3 * (1 - t) ** 2 * a + 6 * (1 - t) * t * (b - a) + 3 * t * t * (1 - b);
    return function (x) {
      if (x <= 0) return 0; if (x >= 1) return 1;
      let t = x;
      for (let i = 0; i < 8; i++) {
        const s = slope(t, p1x, p2x); if (Math.abs(s) < 1e-6) break;
        t -= (bez(t, p1x, p2x) - x) / s; t = Math.min(1, Math.max(0, t));
      }
      if (Math.abs(bez(t, p1x, p2x) - x) > 1e-7) {
        let lo = 0, hi = 1;
        for (let i = 0; i < 40; i++) { t = (lo + hi) / 2; if (bez(t, p1x, p2x) < x) lo = t; else hi = t; }
      }
      return bez(t, p1y, p2y);
    };
  }

  function spring(t, d = 0.68, w = 13.0) {
    if (t <= 0) return 0;
    if (d >= 1) return 1 - Math.exp(-w * t) * (1 + w * t);
    const wd = w * Math.sqrt(1 - d * d);
    return 1 - Math.exp(-d * w * t) * (Math.cos(wd * t) + (d * w / wd) * Math.sin(wd * t));
  }
  function springVelocity(t, d = 0.68, w = 13.0) {
    if (t <= 0) return 0;
    if (d >= 1) return w * w * t * Math.exp(-w * t);
    const wd = w * Math.sqrt(1 - d * d);
    return Math.exp(-d * w * t) * (w * w / wd) * Math.sin(wd * t);
  }
  function springSettled(t, d = 0.68, w = 13.0, eps = 1 / 2000) {
    return t > 0 && Math.abs(1 - spring(t, d, w)) < eps && Math.exp(-Math.min(d, 1) * w * t) < eps;
  }

  const ARRIVE = (t) => spring(t);                  // everything that enters (t in seconds)
  const SETTLE = cubicBezier(0.16, 1.0, 0.30, 1.0); // brakes hard into position
  const SWEEP = cubicBezier(0.80, 0.0, 0.12, 1.0);  // masks, wipes, camera moves
  const CUT = (t) => (t > 0 ? 1 : 0);               // colour, on the beat only

  class Track {
    constructor(start = 0, d = 0.68, w = 13.0) { this.v0 = +start; this.d = d; this.w = w; this.keys = []; this.steps = []; }
    to(t, value, d, w) {
      this.keys.push([+t, +value, d ?? this.d, w ?? this.w]);
      this.keys.sort((a, b) => a[0] - b[0]);
      let prev = this.v0; this.steps = [];
      for (const [ts, v, dd, ww] of this.keys) { this.steps.push([ts, v - prev, dd, ww]); prev = v; }
      return this;
    }
    target(t) { let v = this.v0; for (const [ts, dv] of this.steps) if (ts <= t) v += dv; return v; }
    at(t) { let v = this.v0; for (const [ts, dv, dd, ww] of this.steps) if (t > ts) v += dv * spring(t - ts, dd, ww); return v; }
    velocity(t) { let s = 0; for (const [ts, dv, dd, ww] of this.steps) if (t > ts) s += dv * springVelocity(t - ts, dd, ww); return s; }
    moving(t, eps = 1 / 2000) {
      for (const [ts, dv, dd, ww] of this.steps) {
        if (Math.abs(t - ts) < 1e-9 && Math.abs(dv) > 1e-9) return true;
        if (t > ts && Math.abs(dv) > 1e-9 && !springSettled(t - ts, dd, ww, eps)) return true;
      }
      return false;
    }
    settled(t, eps) { return !this.moving(t, eps); }
    restAt(t, eps) { return this.settled(t, eps) ? this.target(t) : this.at(t); }
  }

  class Beat {
    constructor(bpm = 120, offset = 0) { this.period = 60 / bpm; this.offset = offset; }
    snap(t) { return this.offset + Math.round((t - this.offset) / this.period) * this.period; }
    index(t) { return Math.floor((t - this.offset) / this.period); }
    times(total) { const o = []; for (let k = 0; this.offset + k * this.period < total; k++) o.push(this.offset + k * this.period); return o; }
  }

  const lin = (c) => { c /= 255; return c <= 0.04045 ? c / 12.92 : ((c + 0.055) / 1.055) ** 2.4; };
  const srgb = (x) => { x = clamp01(x); return 255 * (x <= 0.0031308 ? 12.92 * x : 1.055 * x ** (1 / 2.4) - 0.055); };
  function mixColor(a, b, k) {          // linear-light blend, no muddy midpoints
    k = clamp01(k);
    const o = [0, 1, 2].map((i) => Math.round(srgb(lin(a[i]) + (lin(b[i]) - lin(a[i])) * k)));
    if (a.length > 3 || b.length > 3) { const aa = a[3] ?? 255, bb = b[3] ?? 255; o.push(Math.round(aa + (bb - aa) * k)); }
    return o;
  }
  const css = (c) => (c.length > 3 ? `rgba(${c[0]},${c[1]},${c[2]},${(c[3] / 255).toFixed(3)})` : `rgb(${c[0]},${c[1]},${c[2]})`);

  /* ONE shape that never cuts: edges on springs (leading edge stiffer -> stretch),
     radius on a spring, colour switches on the beat (CUT) unless colorBlend > 0. */
  class Morph {
    constructor({ x, y, w, h, r = 0, color = [255, 255, 255], d = 0.68, wLead = 15, wTrail = 11, colorBlend = 0 }) {
      this.L = new Track(x, d); this.T = new Track(y, d); this.R = new Track(x + w, d); this.B = new Track(y + h, d);
      this.rad = new Track(r, d, 12); this.wLead = wLead; this.wTrail = wTrail;
      this.colors = [[-1e9, color]]; this.colorBlend = colorBlend;
    }
    to(t, { x, y, w, h, r, color } = {}) {
      const L0 = this.L.target(t), T0 = this.T.target(t), R0 = this.R.target(t), B0 = this.B.target(t);
      const L1 = x ?? L0, T1 = y ?? T0, R1 = w == null ? L1 + (R0 - L0) : L1 + w, B1 = h == null ? T1 + (B0 - T0) : T1 + h;
      const cx = (L1 + R1) - (L0 + R0), cy = (T1 + B1) - (T0 + B0), wl = this.wLead, wt = this.wTrail;
      this.R.to(t, R1, undefined, cx >= 0 ? wl : wt); this.L.to(t, L1, undefined, cx >= 0 ? wt : wl);
      this.B.to(t, B1, undefined, cy >= 0 ? wl : wt); this.T.to(t, T1, undefined, cy >= 0 ? wt : wl);
      if (r != null) this.rad.to(t, r);
      if (color) { this.colors.push([t, color]); this.colors.sort((a, b) => a[0] - b[0]); }
      return this;
    }
    colorAt(t) {
      let prev = this.colors[0][1];
      for (let i = 1; i < this.colors.length; i++) {
        const [tc, c] = this.colors[i];
        if (t < tc) break;
        if (this.colorBlend > 0 && t < tc + this.colorBlend) return mixColor(prev, c, SETTLE((t - tc) / this.colorBlend));
        prev = c;
      }
      return prev;
    }
    at(t) {
      const L = this.L.at(t), T = this.T.at(t), R = this.R.at(t), B = this.B.at(t);
      const w = Math.max(0, R - L), h = Math.max(0, B - T);
      return { x: L, y: T, w, h, r: Math.max(0, Math.min(this.rad.at(t), w / 2, h / 2)), color: this.colorAt(t) };
    }
    speed(t) { return Math.max(...[this.L, this.T, this.R, this.B].map((k) => Math.abs(k.velocity(t)))); }
    moving(t) { return [this.L, this.T, this.R, this.B, this.rad].some((k) => k.moving(t)); }
    signature(t) { return [this.L, this.T, this.R, this.B, this.rad].map((k) => +k.restAt(t).toFixed(2)).concat([this.colorAt(t).join(',')]); }
    /** apply to a DOM element (absolutely positioned) */
    apply(el, t) {
      const s = this.at(t);
      el.style.transform = `translate(${s.x}px,${s.y}px)`; el.style.width = `${s.w}px`; el.style.height = `${s.h}px`;
      el.style.borderRadius = `${s.r}px`; el.style.background = css(s.color);
      return s;
    }
  }

  /* One transform for the content layer; zoom interpolated in LOG space. */
  class Camera {
    constructor(zoom = 1, x = 0, y = 0) { this.start = [zoom, x, y]; this.moves = []; }
    key(t0, t1, { zoom, x, y, curve } = {}) { this.moves.push([t0, t1, zoom, x, y, curve || SWEEP]); this.moves.sort((a, b) => a[0] - b[0]); return this; }
    at(t) {
      let [z, x, y] = this.start;
      for (const [t0, t1, zz, xx, yy, curve] of this.moves) {
        if (t <= t0) break;
        const k = curve(clamp01((t - t0) / Math.max(1e-6, t1 - t0)));
        if (zz != null) z = Math.exp(Math.log(z) + (Math.log(zz) - Math.log(z)) * k);
        if (xx != null) x += (xx - x) * k;
        if (yy != null) y += (yy - y) * k;
      }
      return { zoom: z, x, y };
    }
    speed(t, radius = 1101, dt = 1 / 240) {
      const a = this.at(t - dt), b = this.at(t + dt);
      const pan = Math.hypot(b.x - a.x, b.y - a.y) * (a.zoom + b.zoom) / 2;
      return (pan + Math.abs(b.zoom - a.zoom) * radius) / (2 * dt);
    }
    /** CSS transform for a stage of size W x H, zooming about (cx, cy) in stage px */
    transform(t, W = 1080, H = 1920) {
      const { zoom, x, y } = this.at(t);
      return `translate(${W / 2}px,${H / 2}px) scale(${zoom}) translate(${-W / 2 + x}px,${-H / 2 + y}px)`;
    }
    validate() {
      const warn = []; let lastDir = 0, z = this.start[0];
      for (const [t0, , zz] of this.moves) {
        if (zz == null) continue;
        const dir = Math.sign(zz - z);
        if (dir && lastDir && dir !== lastDir) warn.push(`zoom reverses at t=${t0.toFixed(2)}s`);
        lastDir = dir || lastDir; z = zz;
      }
      return warn;
    }
  }

  function handoff(t, outAt, inAt, fade = 0.18, curve = smoothstep) {
    inAt = Math.max(inAt, outAt + fade);
    return [1 - curve(clamp01((t - outAt) / fade)), curve(clamp01((t - inAt) / fade))];
  }
  const appear = (t, t0, dur = 0.6, curve = ARRIVE) => (t <= t0 ? 0 : curve === ARRIVE ? curve(t - t0) : curve(clamp01((t - t0) / dur)));
  const leave = (t, t0, dur = 0.25) => 1 - clamp01((t - t0) / dur) ** 1.5;

  const WORD_STAGGER = 0.070, LETTER_STAGGER = 0.025, READ_RATE_WPS = 3.0;
  const readTime = (text, floor = 1.2) => Math.max(floor, String(text).trim().split(/\s+/).length / READ_RATE_WPS);

  /* Masked word rise (translateY 105% inside overflow:hidden) with 55-70 ms stagger.
     Build once with splitWords(el), then call riseWords(spans, t, t0) every frame. */
  function splitWords(el) {
    const words = el.textContent.trim().split(/\s+/); el.textContent = '';
    return words.map((w, i) => {
      const mask = document.createElement('span'); mask.style.cssText = 'display:inline-block;overflow:hidden;vertical-align:bottom;padding:0 .04em .08em';
      const inner = document.createElement('span'); inner.style.cssText = 'display:inline-block'; inner.textContent = w;
      // NO will-change on these spans: it makes Chromium reuse stale rasters (frames depend on render order)
      mask.appendChild(inner); el.appendChild(mask); if (i < words.length - 1) el.appendChild(document.createTextNode(' '));
      return inner;
    });
  }
  function riseWords(spans, t, t0, stagger = WORD_STAGGER, rot = 4) {
    spans.forEach((s, i) => {
      const k = appear(t, t0 + i * stagger);
      s.style.transform = `translateY(${(1 - k) * 105}%) rotate(${(1 - k) * rot}deg)`;
      s.style.opacity = k > 0 ? 1 : 0;
    });
  }

  function drawOdometer(ctx, t, startT, duration, startVal, targetVal, prefix = '', suffix = '', x = 960, y = 540, cardColor = '#fbbf24') {
    if (t < startT) return;
    // Handle legacy signature (ctx, t, startT, duration, startVal, targetVal, x, y)
    if (typeof prefix === 'number') {
      const oldX = prefix;
      const oldY = typeof suffix === 'number' ? suffix : 540;
      x = oldX;
      y = oldY;
      prefix = '';
      suffix = '';
    }
    const p = Math.max(0, Math.min(1, (t - startT) / duration));
    const eased = p === 1 ? 1 : 1 - Math.pow(2, -10 * p); // outExpo
    const current = (targetVal % 1 !== 0 || startVal % 1 !== 0)
      ? (startVal + (targetVal - startVal) * eased).toFixed(1)
      : Math.round(startVal + (targetVal - startVal) * eased).toLocaleString('en-IN');

    const cardW = 680;
    const cardH = 96;
    const halfW = cardW / 2;
    const halfH = cardH / 2;

    ctx.save();
    ctx.translate(x, y);

    // Frosted glass capsule card
    ctx.fillStyle = 'rgba(10, 15, 26, 0.94)';
    ctx.strokeStyle = cardColor;
    ctx.lineWidth = 1.5;
    ctx.shadowColor = 'rgba(0, 0, 0, 0.7)';
    ctx.shadowBlur = 24;
    ctx.beginPath();
    ctx.roundRect(-halfW, -halfH, cardW, cardH, 20);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Left indicator pill
    ctx.fillStyle = cardColor;
    ctx.beginPath();
    ctx.roundRect(-halfW, -halfH, 6, cardH, [20, 0, 0, 20]);
    ctx.fill();

    // Metric Text
    ctx.fillStyle = '#94a3b8';
    ctx.font = '700 13px "JetBrains Mono", monospace';
    ctx.textAlign = 'center';
    ctx.fillText((prefix || 'VERIFIED METRIC').toUpperCase(), 0, -halfH + 28);

    ctx.fillStyle = cardColor;
    ctx.font = '800 42px "JetBrains Mono", monospace';
    ctx.shadowColor = cardColor;
    ctx.shadowBlur = 14;
    ctx.fillText(`${current}${suffix}`, 0, halfH - 20);
    ctx.restore();
  }

  function drawHighlighter(ctx, t, startT, duration, x, y, width, height) {
    if (t < startT) return;
    const p = Math.max(0, Math.min(1, (t - startT) / duration));
    const easedWidth = width * (1 - Math.pow(1 - p, 3)); // outCubic
    ctx.save();
    ctx.globalCompositeOperation = 'multiply';
    ctx.fillStyle = 'rgba(250, 204, 21, 0.65)';
    ctx.fillRect(x, y, easedWidth, height);
    ctx.restore();
  }

  function drawRedactionPeel(ctx, t, startT, duration, x, y, width, height) {
    let offset = 0;
    if (t >= startT) {
      const p = Math.max(0, Math.min(1, (t - startT) / duration));
      offset = (p * (2 - p)) * (width + 40); // outQuad slide
    }
    const remainingW = Math.max(0, width - offset);
    if (remainingW <= 0) return;
    ctx.save();
    ctx.fillStyle = '#09090b';
    ctx.shadowColor = 'rgba(0,0,0,0.5)';
    ctx.shadowBlur = 10;
    ctx.fillRect(x + offset, y, remainingW, height);
    if (offset < width * 0.4) {
      ctx.fillStyle = '#71717a';
      ctx.font = '700 18px monospace';
      ctx.fillText('TOP SECRET · PENDING VERIFICATION', x + 20 + offset, y + height * 0.65);
    }
    ctx.restore();
  }

  // -------------------------------------------------------------------
  // TRAUMA-BASED NOISE & CAMERA SHAKE RIG (Natural 1/f noise, zero aliasing)
  // -------------------------------------------------------------------
  const hash = n => { const x = Math.sin(n * 127.1) * 43758.5453; return x - Math.floor(x); };
  const noise = x => { const i = Math.floor(x), f = x - i, u = f * f * (3 - 2 * f);
    return (hash(i) * (1 - u) + hash(i + 1) * u) * 2 - 1; };

  function traumaShake(t, hits, maxPx = 22, decay = 2.4) {
    let tr = 0;
    const hitList = Array.isArray(hits) ? hits : [hits];
    for (const h of hitList) {
      if (t >= h) tr = Math.max(tr, 1 - (t - h) * decay);
    }
    const k = Math.max(0, tr) ** 2; // Trauma squared feels organic and physical
    return {
      x: maxPx * k * noise(t * 22),
      y: maxPx * k * noise(t * 22 + 50),
      rot: 0.015 * k * noise(t * 22 + 99)
    };
  }

  function drawEvidenceLoupe(ctx, t, startT, cx, cy, radius, zoomScale = 2.5, sourceImg = null, targetX = null, targetY = null) {
    if (t < startT) return;
    const p = t - startT;
    const k = spring(p, 0.68, 14.0);
    if (k <= 0) return;

    const R = radius * Math.min(1.0, k);
    const tx = targetX !== null ? targetX : cx;
    const ty = targetY !== null ? targetY : cy;
    const sw = (2 * R) / zoomScale;

    ctx.save();
    // Heavy physical drop shadow behind lens bezel
    ctx.shadowColor = 'rgba(0, 0, 0, 0.75)';
    ctx.shadowBlur = 28;

    // Draw magnified image through clipped circular aperture
    ctx.beginPath();
    ctx.arc(cx, cy, R, 0, Math.PI * 2);
    ctx.clip();

    if (sourceImg && sourceImg.complete && sourceImg.naturalWidth > 0) {
      ctx.drawImage(sourceImg, tx - sw / 2, ty - sw / 2, sw, sw, cx - R, cy - R, 2 * R, 2 * R);
    } else {
      ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
      ctx.fillRect(cx - R, cy - R, 2 * R, 2 * R);
    }

    // Specular glass reflection
    const glassGrad = ctx.createRadialGradient(cx - R * 0.35, cy - R * 0.35, 0, cx, cy, R);
    glassGrad.addColorStop(0, 'rgba(255, 255, 255, 0.22)');
    glassGrad.addColorStop(0.5, 'rgba(56, 189, 248, 0.05)');
    glassGrad.addColorStop(1, 'rgba(0, 0, 0, 0.25)');
    ctx.fillStyle = glassGrad;
    ctx.fillRect(cx - R, cy - R, 2 * R, 2 * R);
    ctx.restore();

    // Metallic outer bezel
    ctx.save();
    ctx.lineWidth = 8;
    ctx.strokeStyle = '#e2e8f0';
    ctx.shadowColor = 'rgba(0, 0, 0, 0.5)';
    ctx.shadowBlur = 12;
    ctx.beginPath();
    ctx.arc(cx, cy, R, 0, Math.PI * 2);
    ctx.stroke();

    // Cyan glowing inner reticle
    ctx.lineWidth = 2.5;
    ctx.strokeStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(cx, cy, R - 4, 0, Math.PI * 2);
    ctx.stroke();

    // Precision crosshairs
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.65)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(cx - R + 15, cy); ctx.lineTo(cx + R - 15, cy);
    ctx.moveTo(cx, cy - R + 15); ctx.lineTo(cx, cy + R - 15);
    ctx.stroke();

    // Center target ring
    ctx.beginPath();
    ctx.arc(cx, cy, 14, 0, Math.PI * 2);
    ctx.stroke();

    // VERIFIED tag pill
    ctx.fillStyle = '#0a0f1d';
    ctx.shadowColor = 'rgba(0, 0, 0, 0.6)';
    ctx.shadowBlur = 14;
    ctx.beginPath();
    ctx.roundRect(cx + 30, cy - R - 14, 155, 34, 8);
    ctx.fill();
    ctx.shadowBlur = 0;

    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 1.5;
    ctx.stroke();

    ctx.fillStyle = '#38bdf8';
    ctx.font = '800 13px "JetBrains Mono", monospace';
    ctx.textAlign = 'center';
    ctx.fillText('VERIFIED 2.5X', cx + 30 + 155 / 2, cy - R + 8);

    ctx.restore();
  }

  function drawVerdictStamp(ctx, t, hitT, textEn, textHi, cx = 960, cy = 540) {
    if (t < hitT) return;
    const p = t - hitT;
    const springVal = spring(p, 0.72, 16.0);
    const scale = 2.5 - 1.5 * Math.min(1.0, springVal);
    const shk = traumaShake(t, hitT, 20, 2.5);

    ctx.save();
    ctx.translate(cx + shk.x, cy + shk.y);
    ctx.rotate(-0.07 + shk.rot);
    ctx.scale(scale, scale);

    // High-impact red double-border stamp box
    ctx.strokeStyle = '#dc2626';
    ctx.lineWidth = 10;
    ctx.beginPath();
    ctx.roundRect(-360, -90, 720, 180, 20);
    ctx.stroke();

    ctx.strokeStyle = '#ef4444';
    ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.roundRect(-345, -75, 690, 150, 12);
    ctx.stroke();

    ctx.fillStyle = '#ef4444';
    ctx.textAlign = 'center';
    ctx.font = '900 52px "Outfit", -apple-system, sans-serif';
    ctx.fillText(textEn, 0, -10);

    ctx.fillStyle = '#fca5a5';
    ctx.font = '800 34px "Noto Sans Devanagari", sans-serif';
    ctx.fillText(textHi, 0, 48);
    ctx.restore();
  }

  function drawCalloutPin(ctx, t, startT, targetX, targetY, elbowX, elbowY, labelEn, labelHi, tagColor = '#38bdf8') {
    if (t < startT) return;
    const p = Math.min(1, Math.max(0, (t - startT) / 0.5));
    const reticleScale = Math.min(1.2, 1 - Math.exp(-p * 8) * Math.cos(p * 10));
    
    ctx.save();
    ctx.strokeStyle = tagColor;
    ctx.lineWidth = 2.5;
    ctx.beginPath();
    ctx.arc(targetX, targetY, 14 * reticleScale, 0, Math.PI * 2);
    ctx.stroke();
    
    const ping = (t - startT) % 1.5;
    if (ping < 1.0) {
      ctx.strokeStyle = tagColor;
      ctx.globalAlpha = 1.0 - ping;
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.arc(targetX, targetY, 14 + ping * 24, 0, Math.PI * 2);
      ctx.stroke();
      ctx.globalAlpha = 1.0;
    }

    ctx.fillStyle = tagColor;
    ctx.beginPath();
    ctx.arc(targetX, targetY, 4, 0, Math.PI * 2);
    ctx.fill();

    if (p > 0.1) {
      const lineP = Math.min(1, (p - 0.1) / 0.5);
      const currElbowX = targetX + (elbowX - targetX) * lineP;
      const currElbowY = targetY + (elbowY - targetY) * lineP;
      
      ctx.strokeStyle = tagColor;
      ctx.lineWidth = 2;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(targetX, targetY);
      ctx.lineTo(currElbowX, currElbowY);
      ctx.stroke();
      ctx.setLineDash([]);

      if (lineP >= 0.8) {
        const badgeP = Math.min(1, (lineP - 0.8) / 0.2);
        const badgeScale = 0.8 + 0.2 * badgeP;
        const dir = elbowX >= targetX ? 1 : -1;
        const badgeW = 340;
        const badgeH = 76;
        const bx = dir > 0 ? elbowX : elbowX - badgeW;
        const by = elbowY - badgeH / 2;

        ctx.save();
        ctx.translate(elbowX, elbowY);
        ctx.scale(badgeScale, badgeScale);
        ctx.translate(-elbowX, -elbowY);

        ctx.fillStyle = 'rgba(10, 15, 24, 0.94)';
        ctx.shadowColor = 'rgba(0, 0, 0, 0.6)';
        ctx.shadowBlur = 18;
        ctx.beginPath();
        ctx.roundRect(bx, by, badgeW, badgeH, 10);
        ctx.fill();
        ctx.shadowBlur = 0;

        ctx.strokeStyle = tagColor;
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.fillStyle = tagColor;
        ctx.beginPath();
        ctx.roundRect(bx, by, 6, badgeH, [10, 0, 0, 10]);
        ctx.fill();

        ctx.fillStyle = '#ffffff';
        ctx.font = '700 20px -apple-system, sans-serif';
        ctx.textAlign = 'left';
        ctx.fillText(labelEn, bx + 18, by + 30);

        ctx.fillStyle = '#94a3b8';
        ctx.font = '600 16px sans-serif';
        ctx.fillText(labelHi, bx + 18, by + 56);
        ctx.restore();
      }
    }
    ctx.restore();
  }

  function drawRoadmapCard(ctx, t, startT, duration, points, centerX = null, centerY = null, cardWidth = null) {
    if (t < startT || t > startT + duration) return;
    const W = ctx.canvas ? ctx.canvas.width : 1920;
    const H = ctx.canvas ? ctx.canvas.height : 1080;
    const isShorts = H > W;

    // Adaptively clamp width within safe zones (80px margins on Shorts, 100px on 16:9)
    const maxSafeW = isShorts ? (W - 160) : Math.min(1080, W - 200);
    const resolvedW = cardWidth ? Math.min(cardWidth, maxSafeW) : maxSafeW;
    const cx = centerX !== null ? centerX : W / 2;
    const cy = centerY !== null ? centerY : H / 2;

    const p = Math.min(1, Math.max(0, (t - startT) / 0.5));
    const scale = 0.88 + 0.12 * Math.sin(p * Math.PI * 0.5);
    ctx.save();
    ctx.translate(cx, cy);
    ctx.scale(scale, scale);

    const cardH = 120 + points.length * 110;
    const halfW = resolvedW / 2;
    const halfH = cardH / 2;

    ctx.fillStyle = 'rgba(10, 15, 26, 0.94)';
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.4)';
    ctx.lineWidth = 1.5;
    ctx.shadowColor = 'rgba(0, 0, 0, 0.7)';
    ctx.shadowBlur = 30;
    ctx.beginPath();
    ctx.roundRect(-halfW, -halfH, cardWidth, cardH, 16);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    ctx.fillStyle = '#38bdf8';
    ctx.font = '700 16px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText('⚡ 5-SECOND ROADMAP HOOK', -halfW + 40, -halfH + 45);

    ctx.fillStyle = '#ffffff';
    ctx.font = '800 28px Inter, sans-serif';
    ctx.fillText('Iss video mein hum cover karenge:', -halfW + 40, -halfH + 85);

    const ptDur = duration / points.length;
    points.forEach((pt, idx) => {
      const ptStart = startT + idx * ptDur;
      const ptEnd = ptStart + ptDur;
      const isActive = t >= ptStart && t < ptEnd;
      const isPassed = t >= ptEnd;
      const y = -halfH + 115 + idx * 110;
      const rowW = cardWidth - 80;

      ctx.fillStyle = isActive ? 'rgba(56, 189, 248, 0.12)' : (isPassed ? 'rgba(16, 185, 129, 0.08)' : 'rgba(255, 255, 255, 0.03)');
      ctx.strokeStyle = isActive ? '#38bdf8' : (isPassed ? '#10b981' : 'rgba(255, 255, 255, 0.08)');
      ctx.lineWidth = isActive ? 2 : 1;
      ctx.beginPath();
      ctx.roundRect(-halfW + 40, y, rowW, 90, 12);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = isActive ? '#38bdf8' : (isPassed ? '#10b981' : '#475569');
      ctx.beginPath();
      ctx.roundRect(-halfW + 40, y, 6, 90, [12, 0, 0, 12]);
      ctx.fill();

      ctx.fillStyle = isActive ? '#38bdf8' : (isPassed ? '#10b981' : '#94a3b8');
      ctx.font = '700 20px "JetBrains Mono", monospace';
      ctx.fillText(pt.en, -halfW + 65, y + 36);

      ctx.fillStyle = isActive ? '#ffffff' : (isPassed ? '#cbd5e1' : '#64748b');
      ctx.font = '600 18px Inter, sans-serif';
      ctx.fillText(pt.hi, -halfW + 65, y + 68);
    });
    ctx.restore();
  }

  function drawLivelyHighlighter(ctx, t, startT, duration, x, y, width, height, color = 'rgba(253, 224, 71, 0.72)') {
    if (t < startT) return 0;
    const p = Math.max(0, Math.min(1, (t - startT) / duration));
    const eased = 1 - Math.pow(1 - p, 3); // outCubic
    const w = width * eased;
    if (w <= 2) return p;

    ctx.save();
    // Multiply composite operation: highlights paper behind without covering text
    ctx.globalCompositeOperation = 'multiply';
    ctx.fillStyle = color;
    ctx.beginPath();
    ctx.roundRect(x, y, w, height, 4);
    ctx.fill();
    ctx.restore();

    // Soft warm ambient glow
    ctx.save();
    ctx.fillStyle = 'rgba(250, 204, 21, 0.18)';
    ctx.shadowColor = 'rgba(234, 179, 8, 0.5)';
    ctx.shadowBlur = 14;
    ctx.beginPath();
    ctx.roundRect(x, y, w, height, 4);
    ctx.fill();
    ctx.restore();

    // Lively animated pen-tip nib / glowing dot while actively sweeping
    if (p > 0.02 && p < 0.98) {
      ctx.save();
      ctx.fillStyle = '#eab308';
      ctx.shadowColor = 'rgba(234, 179, 8, 0.9)';
      ctx.shadowBlur = 12;
      ctx.beginPath();
      ctx.arc(x + w, y + height / 2, height * 0.42, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }
    return p;
  }

  function drawAudienceQuestionCard(ctx, t, startT, duration, badgeText, questionText, subText, accentColor = '#38bdf8', cx = null, cy = null) {
    if (t < startT || t > startT + duration) return;
    const W = ctx.canvas ? ctx.canvas.width : 1920;
    const H = ctx.canvas ? ctx.canvas.height : 1080;
    const isShorts = H > W;

    const maxSafeW = isShorts ? (W - 160) : Math.min(1120, W - 200);
    const resolvedCx = cx !== null ? Math.min(cx, W - maxSafeW / 2) : W / 2;
    const resolvedCy = cy !== null ? cy : (isShorts ? H * 0.72 : 850);

    const elapsed = t - startT;
    const remaining = (startT + duration) - t;
    
    // Spring entrance & exit
    let scale = 1.0;
    let alpha = 1.0;
    if (elapsed < 0.45) {
      const p = elapsed / 0.45;
      scale = 0.85 + 0.15 * Math.sin(p * Math.PI * 0.5);
      alpha = p;
    } else if (remaining < 0.35) {
      alpha = Math.max(0, remaining / 0.35);
      scale = 1.0 - 0.05 * (1 - alpha);
    }

    const cardW = maxSafeW;
    const cardH = isShorts ? 170 : 136;
    const halfW = cardW / 2;
    const halfH = cardH / 2;

    ctx.save();
    ctx.translate(resolvedCx, resolvedCy);
    ctx.scale(scale, scale);
    ctx.globalAlpha = alpha;

    // Frosted glass background
    ctx.fillStyle = 'rgba(10, 15, 26, 0.93)';
    ctx.strokeStyle = accentColor;
    ctx.lineWidth = 1.5;
    ctx.shadowColor = 'rgba(0, 0, 0, 0.75)';
    ctx.shadowBlur = 24;
    ctx.beginPath();
    ctx.roundRect(-halfW, -halfH, cardW, cardH, 16);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Glowing accent left bar
    ctx.fillStyle = accentColor;
    ctx.beginPath();
    ctx.roundRect(-halfW, -halfH, 8, cardH, [16, 0, 0, 16]);
    ctx.fill();

    // Top Category Badge
    ctx.fillStyle = accentColor;
    ctx.font = '800 13px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText(badgeText.toUpperCase(), -halfW + 36, -halfH + 34);

    // Main Question
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 25px Inter, sans-serif';
    ctx.fillText(questionText, -halfW + 36, -halfH + 74);

    // Subtitle / English context
    ctx.fillStyle = '#94a3b8';
    ctx.font = '600 14px "JetBrains Mono", monospace';
    ctx.fillText(subText, -halfW + 36, -halfH + 106);

    ctx.restore();
  }

  function drawSubscribeLikeCTA(ctx, t, startT, duration = 2.8, logoImg = null, cx = 960, cy = 840) {
    if (t < startT || t > startT + duration) return;
    const elapsed = t - startT;
    const remaining = (startT + duration) - t;

    // Spring entrance & exit
    let scale = 1.0;
    let alpha = 1.0;
    let slideY = 0;
    if (elapsed < 0.45) {
      const p = elapsed / 0.45;
      scale = 0.7 + 0.3 * (1 - Math.exp(-p * 8) * Math.cos(p * 10));
      alpha = Math.min(1, p * 2);
      slideY = (1 - p) * 30;
    } else if (remaining < 0.4) {
      const p = remaining / 0.4;
      alpha = p;
      scale = 0.95 + 0.05 * p;
      slideY = (1 - p) * 25;
    }

    const cardW = 680;
    const cardH = 92;
    const halfW = cardW / 2;
    const halfH = cardH / 2;

    ctx.save();
    ctx.translate(cx, cy + slideY);
    ctx.scale(scale, scale);
    ctx.globalAlpha = alpha;

    // Glowing obsidian capsule
    ctx.fillStyle = 'rgba(8, 12, 22, 0.95)';
    ctx.strokeStyle = 'rgba(251, 191, 36, 0.45)';
    ctx.lineWidth = 1.5;
    ctx.shadowColor = 'rgba(0, 0, 0, 0.8)';
    ctx.shadowBlur = 24;
    ctx.beginPath();
    ctx.roundRect(-halfW, -halfH, cardW, cardH, 46);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Channel Logo Avatar with pulsing gold ring
    const avatarX = -halfW + 48;
    const avatarY = 0;
    const avatarR = 26;
    ctx.save();
    ctx.beginPath();
    ctx.arc(avatarX, avatarY, avatarR, 0, Math.PI * 2);
    ctx.clip();
    if (logoImg && logoImg.complete && logoImg.naturalWidth > 0) {
      ctx.drawImage(logoImg, avatarX - avatarR, avatarY - avatarR, avatarR * 2, avatarR * 2);
    } else {
      ctx.fillStyle = '#fbbf24';
      ctx.fillRect(avatarX - avatarR, avatarY - avatarR, avatarR * 2, avatarR * 2);
      ctx.fillStyle = '#000';
      ctx.font = '800 18px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('BI', avatarX, avatarY + 6);
    }
    ctx.restore();

    ctx.strokeStyle = '#fbbf24';
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.arc(avatarX, avatarY, avatarR, 0, Math.PI * 2);
    ctx.stroke();

    // Channel Title & Tagline
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 18px Inter, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('BENAQAAB INDIA', avatarX + 38, avatarY - 5);

    ctx.fillStyle = '#fbbf24';
    ctx.font = '700 11px "JetBrains Mono", monospace';
    ctx.fillText('SACH · SABOOT · BEBAK', avatarX + 38, avatarY + 16);

    // Animated Interactive Buttons (Like & Subscribe)
    const isLiked = elapsed >= 0.75;
    const isSubscribed = elapsed >= 1.25;

    // 1. LIKE BUTTON
    const likeX = avatarX + 265;
    const likeY = avatarY - 20;
    const likeW = 92;
    const likeH = 40;
    ctx.fillStyle = isLiked ? 'rgba(56, 189, 248, 0.18)' : 'rgba(255, 255, 255, 0.06)';
    ctx.strokeStyle = isLiked ? '#38bdf8' : 'rgba(255, 255, 255, 0.15)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.roundRect(likeX, likeY, likeW, likeH, 20);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = isLiked ? '#38bdf8' : '#cbd5e1';
    ctx.font = '700 14px Inter, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(isLiked ? '👍 LIKED' : '👍 LIKE', likeX + likeW / 2, likeY + 25);

    // 2. SUBSCRIBE BUTTON
    const subX = likeX + likeW + 14;
    const subY = avatarY - 20;
    const subW = 160;
    const subH = 40;

    if (!isSubscribed) {
      // Vivid Red Subscribe Button
      ctx.fillStyle = '#dc2626';
      ctx.shadowColor = 'rgba(220, 38, 38, 0.5)';
      ctx.shadowBlur = 10;
      ctx.beginPath();
      ctx.roundRect(subX, subY, subW, subH, 20);
      ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = '#ffffff';
      ctx.font = '800 14px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('SUBSCRIBE ▶', subX + subW / 2, subY + 25);
    } else {
      // Subscribed State with wiggling Bell
      const bellWiggle = Math.sin((elapsed - 1.25) * 20) * (elapsed < 2.0 ? 0.2 : 0);
      ctx.fillStyle = 'rgba(255, 255, 255, 0.12)';
      ctx.strokeStyle = 'rgba(251, 191, 36, 0.6)';
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.roundRect(subX, subY, subW, subH, 20);
      ctx.fill();
      ctx.stroke();

      ctx.save();
      ctx.translate(subX + 28, subY + 20);
      ctx.rotate(bellWiggle);
      ctx.fillStyle = '#fbbf24';
      ctx.font = '16px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('🔔', 0, 5);
      ctx.restore();

      ctx.fillStyle = '#fbbf24';
      ctx.font = '800 13px Inter, sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('SUBSCRIBED', subX + subW / 2 + 10, subY + 25);
    }

    ctx.restore();
  }

  let _grainTiles = null;
  function initGrainTiles() {
    if (_grainTiles || typeof document === 'undefined') return;
    _grainTiles = [];
    for (let tileIdx = 0; tileIdx < 8; tileIdx++) {
      const c = document.createElement('canvas');
      c.width = 256;
      c.height = 256;
      const gctx = c.getContext('2d');
      const imgData = gctx.createImageData(256, 256);
      const seed = (tileIdx + 1) * 19.17;
      for (let i = 0; i < imgData.data.length; i += 4) {
        const pxIdx = i / 4;
        const val = Math.floor(Math.abs(Math.sin(pxIdx * 0.127 + seed) * 43758.5453) % 256);
        imgData.data[i] = val;
        imgData.data[i + 1] = val;
        imgData.data[i + 2] = val;
        imgData.data[i + 3] = 38;
      }
      gctx.putImageData(imgData, 0, 0);
      _grainTiles.push(c);
    }
  }

  function drawGrain(ctx, width, height, opacity = 0.03, t = 0) {
    initGrainTiles();
    if (_grainTiles && _grainTiles.length === 8) {
      const tileIndex = Math.floor((t || 0) * 24) % 8;
      const activeTile = _grainTiles[tileIndex];
      ctx.save();
      ctx.globalAlpha = opacity;
      ctx.fillStyle = ctx.createPattern(activeTile, 'repeat');
      ctx.fillRect(0, 0, width, height);
      ctx.restore();
    }
  }

  function drawDynamicCaption(ctx, t, captionsData, cx = 960, cy = 965) {
    if (!captionsData || !captionsData.length) return;

    let activeChunk = null;
    if (t <= captionsData[0].start_s) {
      activeChunk = captionsData[0];
    } else {
      for (let i = 0; i < captionsData.length; i++) {
        const c = captionsData[i];
        if (t >= c.start_s && t < c.end_s) {
          activeChunk = c;
          break;
        } else if (i < captionsData.length - 1 && t >= c.end_s && t < captionsData[i + 1].start_s) {
          // Continuous smooth hold across micro-pauses between sentences
          activeChunk = c;
          break;
        }
      }
      if (!activeChunk && t >= captionsData[captionsData.length - 1].start_s) {
        activeChunk = captionsData[captionsData.length - 1];
      }
    }
    if (!activeChunk) return;

    const elapsed = Math.max(0, t - activeChunk.start_s);
    const remaining = Math.max(0, activeChunk.end_s - t);

    // Smooth spring entrance & exit
    let enterScale = 1.0;
    let alpha = 1.0;
    if (t < activeChunk.start_s) {
      enterScale = 1.0;
      alpha = 0.95;
    } else if (elapsed < 0.12) {
      const p = elapsed / 0.12;
      enterScale = 0.90 + 0.10 * Math.sin(p * Math.PI * 0.5);
      alpha = Math.max(0.7, p);
    } else if (remaining < 0.10 && t <= activeChunk.end_s) {
      alpha = Math.max(0.7, remaining / 0.10);
      enterScale = 0.96 + 0.04 * alpha;
    }

    ctx.save();
    ctx.font = '700 23px -apple-system, BlinkMacSystemFont, "Inter", "Plus Jakarta Sans", sans-serif';

    const wordMetrics = [];
    let totalWordsWidth = 0;
    const wordGap = 10;

    activeChunk.words.forEach((wObj, idx) => {
      const isCurrent = t >= wObj.start_s && t < wObj.end_s;
      const isPast = t >= wObj.end_s;
      const width = ctx.measureText(wObj.word).width;
      wordMetrics.push({
        word: wObj.word,
        width,
        isCurrent,
        isPast,
        start_s: wObj.start_s,
        end_s: wObj.end_s
      });
      totalWordsWidth += width + (idx < activeChunk.words.length - 1 ? wordGap : 0);
    });

    const padX = 26;
    const pillW = Math.max(220, totalWordsWidth + padX * 2 + 14);
    const pillH = 52;
    const halfW = pillW / 2;
    const halfH = pillH / 2;

    ctx.translate(cx, cy);
    ctx.scale(enterScale, enterScale);
    ctx.globalAlpha = alpha;

    // 1. Frosted Glass Obsidian Pill
    ctx.fillStyle = 'rgba(7, 10, 18, 0.88)';
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.32)';
    ctx.lineWidth = 1.2;
    ctx.shadowColor = 'rgba(0, 0, 0, 0.8)';
    ctx.shadowBlur = 18;
    ctx.beginPath();
    ctx.roundRect(-halfW, -halfH, pillW, pillH, 26);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    // 2. Animated audio soundwave pulse on far left of pill
    const waveX = -halfW + 16;
    const waveH1 = 8 + Math.sin(t * 18) * 5;
    const waveH2 = 12 + Math.cos(t * 22) * 6;
    const waveH3 = 7 + Math.sin(t * 15 + 1) * 4;
    ctx.fillStyle = '#38bdf8';
    ctx.fillRect(waveX, -waveH1 / 2, 2.5, waveH1);
    ctx.fillRect(waveX + 5, -waveH2 / 2, 2.5, waveH2);
    ctx.fillRect(waveX + 10, -waveH3 / 2, 2.5, waveH3);

    // 3. Render Words with Word-Level Active Karaoke Glow
    let curX = -halfW + padX + 14;
    const textBaselineY = 8;

    wordMetrics.forEach((wm) => {
      if (wm.isCurrent) {
        ctx.save();
        const wordMidX = curX + wm.width / 2;
        ctx.translate(wordMidX, textBaselineY);
        ctx.scale(1.08, 1.08);

        // Highlight pill behind active word
        ctx.fillStyle = 'rgba(56, 189, 248, 0.18)';
        ctx.beginPath();
        ctx.roundRect(-wm.width / 2 - 5, -20, wm.width + 10, 28, 6);
        ctx.fill();

        ctx.fillStyle = '#38bdf8';
        ctx.shadowColor = 'rgba(56, 189, 248, 0.9)';
        ctx.shadowBlur = 14;
        ctx.textAlign = 'center';
        ctx.fillText(wm.word, 0, 0);
        ctx.restore();
      } else if (wm.isPast) {
        ctx.fillStyle = '#ffffff';
        ctx.textAlign = 'left';
        ctx.fillText(wm.word, curX, textBaselineY);
      } else {
        ctx.fillStyle = '#94a3b8';
        ctx.textAlign = 'left';
        ctx.fillText(wm.word, curX, textBaselineY);
      }
      curX += wm.width + wordGap;
    });

    ctx.restore();
  }

  // --- CLOSED-FORM ANALYTICAL SPRING ENGINE (Deterministic Seek-Safe) ---
  const SpringEngine = (function () {
    const PRESETS = {
      snappy:  { response: 0.22, damping: 0.80 },
      default: { response: 0.40, damping: 0.86 },
      heavy:   { response: 0.50, damping: 1.00 },
      impact:  { response: 0.28, damping: 0.55 },
    };

    function step(tau, preset = 'default') {
      if (tau <= 0) return 0;
      const p = typeof preset === 'string' ? PRESETS[preset] || PRESETS.default : preset;
      const w = (2 * Math.PI) / p.response;
      const z = p.damping;
      if (z < 1) {
        const wd = w * Math.sqrt(1 - z * z);
        return 1 - Math.exp(-z * w * tau) * (Math.cos(wd * tau) + ((z * w) / wd) * Math.sin(wd * tau));
      }
      if (z === 1) return 1 - Math.exp(-w * tau) * (1 + w * tau);
      const wd = w * Math.sqrt(z * z - 1);
      return 1 - Math.exp(-z * w * tau) * (Math.cosh(wd * tau) + ((z * w) / wd) * Math.sinh(wd * tau));
    }

    function springVal(t, t0, from, to, preset = 'default') {
      return from + (to - from) * step(t - t0, preset);
    }

    return { PRESETS, step, springVal };
  })();

  // --- PROCEDURAL INK BLEED FORENSIC HIGHLIGHTER ---
  function drawForensicHighlighter(ctx, t, startT, duration, x, y, width, height, baseColor = '#FFE600') {
    if (t < startT) return 0;
    const p = Math.max(0, Math.min(1, (t - startT) / duration));
    const eased = 1 - Math.pow(1 - p, 3);
    const w = width * eased;
    if (w <= 2) return p;

    ctx.save();
    ctx.globalCompositeOperation = 'multiply';

    ctx.fillStyle = 'rgba(255, 230, 0, 0.75)';
    ctx.beginPath();
    ctx.moveTo(x, y + 1);

    const steps = Math.max(4, Math.floor(w / 12));
    for (let i = 0; i <= steps; i++) {
      const px = x + (i / steps) * w;
      const bleed = (Math.sin(px * 0.45) * 1.2) + (Math.cos(px * 0.9) * 0.8);
      ctx.lineTo(px, y + bleed);
    }

    ctx.lineTo(x + w, y + height);

    for (let i = steps; i >= 0; i--) {
      const px = x + (i / steps) * w;
      const bleed = (Math.cos(px * 0.5) * 1.1) + (Math.sin(px * 0.8) * 0.7);
      ctx.lineTo(px, y + height + bleed);
    }
    ctx.closePath();
    ctx.fill();

    ctx.globalCompositeOperation = 'source-over';
    ctx.fillStyle = 'rgba(250, 204, 21, 0.16)';
    ctx.shadowColor = 'rgba(234, 179, 8, 0.45)';
    ctx.shadowBlur = 14;
    ctx.fillRect(x, y, w, height);

    if (p > 0.02 && p < 0.98) {
      ctx.fillStyle = '#eab308';
      ctx.shadowColor = 'rgba(234, 179, 8, 0.95)';
      ctx.shadowBlur = 14;
      ctx.beginPath();
      ctx.arc(x + w, y + height / 2, height * 0.44, 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.restore();
    return p;
  }

  // --- OFFICIAL PRIMARY SOURCE BROADCAST LOWER-THIRD STRAP ---
  function drawOfficialSourceStrap(ctx, t, startT, dur, strap, x = 76, y = 870) {
    if (t < startT || t > startT + dur) return;

    const elapsed = t - startT;
    const remaining = (startT + dur) - t;

    const barGrow = SpringEngine.step(elapsed, 'snappy') * (remaining < 0.4 ? remaining / 0.4 : 1);
    const panelWipe = SpringEngine.step(elapsed - 0.15, 'default') * (remaining < 0.4 ? remaining / 0.4 : 1);
    const textRise = SpringEngine.step(elapsed - 0.28, 'snappy');
    const tabSlide = SpringEngine.step(elapsed - 0.40, 'snappy');

    if (barGrow <= 0) return;

    ctx.save();
    const accentColor = strap.accent || '#fbbf24';
    const displayFont = '800 24px -apple-system, BlinkMacSystemFont, "Inter", sans-serif';
    const subFont = '700 13px "JetBrains Mono", monospace';

    ctx.font = displayFont;
    const docW = ctx.measureText(strap.document).width;
    ctx.font = subFont;
    const authW = ctx.measureText(strap.authority.toUpperCase()).width;

    const barW = 8;
    const padX = 26;
    const panelH = 50;
    const tabH = 30;
    const panelW = Math.max(docW + padX * 2, authW + padX * 2 + 60);

    // 1. Accent Left Bar
    ctx.fillStyle = accentColor;
    ctx.shadowColor = accentColor;
    ctx.shadowBlur = 12;
    ctx.fillRect(x, y + panelH * (1 - barGrow), barW, (panelH + tabH) * barGrow);
    ctx.shadowBlur = 0;

    // 2. Main Frosted Obsidian Document Panel
    if (panelWipe > 0.01) {
      ctx.save();
      ctx.beginPath();
      ctx.rect(x + barW, y, panelW * panelWipe, panelH);
      ctx.clip();

      ctx.fillStyle = 'rgba(8, 12, 22, 0.94)';
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.14)';
      ctx.lineWidth = 1;
      ctx.fillRect(x + barW, y, panelW, panelH);
      ctx.strokeRect(x + barW, y, panelW, panelH);

      const textY = y + panelH / 2 + (1 - textRise) * 30 + 7;
      ctx.fillStyle = '#f8fafc';
      ctx.font = displayFont;
      ctx.textBaseline = 'alphabetic';
      ctx.fillText(strap.document, x + barW + padX, textY);
      ctx.restore();
    }

    // 3. Lower Authority Source Tag Tab
    if (tabSlide > 0.01 && panelWipe > 0.3) {
      const tabY = y + panelH;
      ctx.save();
      ctx.beginPath();
      ctx.rect(x + barW, tabY, (panelW * 0.88) * tabSlide, tabH);
      ctx.clip();

      ctx.fillStyle = accentColor;
      ctx.fillRect(x + barW, tabY, panelW * 0.88, tabH);

      ctx.fillStyle = '#07090e';
      ctx.font = subFont;
      ctx.fillText(`OFFICIAL RECORD · ${strap.authority.toUpperCase()} [${strap.date || 'VERIFIED'}]`, x + barW + 16, tabY + 20);
      ctx.restore();
    }

    ctx.restore();
  }

  const api = { clamp01, smoothstep, cubicBezier, spring, springVelocity, springSettled, ARRIVE, SETTLE, SWEEP, CUT,
    Track, Beat, Morph, Camera, mixColor, css, handoff, appear, leave, WORD_STAGGER, LETTER_STAGGER, READ_RATE_WPS,
    readTime, splitWords, riseWords,
    drawOdometer, drawHighlighter, drawLivelyHighlighter, drawForensicHighlighter, drawOfficialSourceStrap,
    drawAudienceQuestionCard, drawSubscribeLikeCTA,
    drawRedactionPeel, drawEvidenceLoupe, drawVerdictStamp, drawCalloutPin,
    drawRoadmapCard, drawGrain, drawDynamicCaption, SpringEngine };
  root.Motion = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);


