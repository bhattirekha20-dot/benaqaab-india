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

  /* ─── 5 FORENSIC MOTION PRIMITIVES (Benaqaab Forensics Engine) ─── */
  function drawOdometer(ctx, t, startT, duration, startVal, targetVal, x, y) {
    if (t < startT) return;
    const p = Math.max(0, Math.min(1, (t - startT) / duration));
    const eased = p === 1 ? 1 : 1 - Math.pow(2, -10 * p); // outExpo
    const current = Math.round(startVal + (targetVal - startVal) * eased);
    ctx.save();
    ctx.font = '900 110px monospace';
    ctx.fillStyle = '#ef4444';
    ctx.shadowColor = 'rgba(239, 68, 68, 0.6)';
    ctx.shadowBlur = 25;
    ctx.textAlign = 'center';
    ctx.fillText(`+ ₹${current.toLocaleString('en-IN')}`, x, y);
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

  function drawEvidenceLoupe(ctx, t, startT, x, y, radius, zoomScale = 2.0) {
    if (t < startT) return;
    const p = Math.max(0, Math.min(1, (t - startT) / 0.8));
    const scale = 0.3 + 0.7 * (1 - Math.exp(-p * 8) * Math.cos(p * 12));
    ctx.save();
    ctx.translate(x, y);
    ctx.scale(scale, scale);
    ctx.shadowColor = 'rgba(0,0,0,0.6)';
    ctx.shadowBlur = 25;
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 8;
    ctx.beginPath();
    ctx.arc(0, 0, radius, 0, Math.PI * 2);
    ctx.stroke();
    ctx.fillStyle = 'rgba(56, 189, 248, 0.08)';
    ctx.fill();
    ctx.shadowBlur = 0;
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.5)';
    ctx.lineWidth = 1.5;
    ctx.beginPath();
    ctx.moveTo(-radius + 15, 0); ctx.lineTo(radius - 15, 0);
    ctx.moveTo(0, -radius + 15); ctx.lineTo(0, radius - 15);
    ctx.stroke();
    ctx.fillStyle = '#0f172a';
    ctx.beginPath();
    ctx.roundRect(40, -radius, 140, 38, 8);
    ctx.fill();
    ctx.strokeStyle = '#38bdf8';
    ctx.lineWidth = 1;
    ctx.stroke();
    ctx.fillStyle = '#38bdf8';
    ctx.font = '700 14px monospace';
    ctx.fillText('VERIFIED 2X', 60, -radius + 24);
    ctx.restore();
  }

  function drawVerdictStamp(ctx, t, hitT, textEn, textHi, cx, cy) {
    if (t < hitT) return;
    const p = t - hitT;
    const w0 = 14, z = 0.65;
    const springP = 1 - Math.exp(-p * z * w0) * (Math.cos(p * w0 * Math.sqrt(1 - z * z)));
    const scale = 2.8 - (2.8 - 1.0) * Math.min(1.2, springP);
    const impact = Math.max(0, 1 - (p * 4));
    const shakeX = Math.sin(t * 80) * 8 * impact;
    const shakeY = Math.cos(t * 70) * 8 * impact;
    ctx.save();
    ctx.translate(cx + shakeX, cy + shakeY);
    ctx.rotate(-0.08);
    ctx.scale(scale, scale);
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
    ctx.font = '900 52px -apple-system, sans-serif';
    ctx.fillText(textEn, 0, -10);
    ctx.fillStyle = '#fca5a5';
    ctx.font = '800 34px sans-serif';
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

  function drawRoadmapCard(ctx, t, startT, duration, points, centerX, centerY, cardWidth = 960) {
    if (t < startT || t > startT + duration) return;
    const p = Math.min(1, Math.max(0, (t - startT) / 0.5));
    const scale = 0.88 + 0.12 * Math.sin(p * Math.PI * 0.5);
    ctx.save();
    ctx.translate(centerX, centerY);
    ctx.scale(scale, scale);

    const cardH = 120 + points.length * 110;
    const halfW = cardWidth / 2;
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

  let _grainCanvas = null;
  function drawGrain(ctx, width, height, opacity = 0.03) {
    if (!_grainCanvas && typeof document !== 'undefined') {
      _grainCanvas = document.createElement('canvas');
      _grainCanvas.width = 256;
      _grainCanvas.height = 256;
      const gctx = _grainCanvas.getContext('2d');
      const imgData = gctx.createImageData(256, 256);
      for (let i = 0; i < imgData.data.length; i += 4) {
        const v = (Math.sin(i * 0.13) * 0.5 + 0.5) * 255;
        imgData.data[i] = v;
        imgData.data[i+1] = v;
        imgData.data[i+2] = v;
        imgData.data[i+3] = 40;
      }
      gctx.putImageData(imgData, 0, 0);
    }
    if (_grainCanvas) {
      ctx.save();
      ctx.globalAlpha = opacity;
      ctx.fillStyle = ctx.createPattern(_grainCanvas, 'repeat');
      ctx.fillRect(0, 0, width, height);
      ctx.restore();
    }
  }

  const api = { clamp01, smoothstep, cubicBezier, spring, springVelocity, springSettled, ARRIVE, SETTLE, SWEEP, CUT,
    Track, Beat, Morph, Camera, mixColor, css, handoff, appear, leave, WORD_STAGGER, LETTER_STAGGER, READ_RATE_WPS,
    readTime, splitWords, riseWords,
    drawOdometer, drawHighlighter, drawRedactionPeel, drawEvidenceLoupe, drawVerdictStamp, drawCalloutPin,
    drawRoadmapCard, drawGrain };
  root.Motion = api;
  if (typeof module !== 'undefined' && module.exports) module.exports = api;
})(typeof window !== 'undefined' ? window : globalThis);

