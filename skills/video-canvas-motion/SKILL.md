---
name: video-canvas-motion
description: >-
  Motion control and animation engine for HTML5 Canvas, WebGL, and documentary-style video generation.
  Use this skill when building canvas-based video players, cinematic scene renderers, virtual camera systems
  (zoom, pan, shake, tilt), kinetic typography, document highlights, evidence boards, animated charts,
  and Dhruv Rathee / Vox / Johnny Harris style visual investigations.
---

# 🎥 Video Canvas Motion — Cinematic Canvas & Motion Controller

The Video Canvas Motion system provides complete mathematical and programmatic patterns for rendering broadcast-quality 60FPS animations, virtual camera movements, and documentary-style visual journalism directly on HTML5 Canvas.

---

## 📸 The Virtual Camera System

Instead of animating individual objects, move a **Virtual Camera** to achieve filmic depth:

```javascript
class VirtualCamera {
  constructor(canvasWidth = 1920, canvasHeight = 1080) {
    this.w = canvasWidth;
    this.h = canvasHeight;
    this.x = canvasWidth / 2;
    this.y = canvasHeight / 2;
    this.zoom = 1.0;
    this.rotation = 0; // radians
    
    // Camera shake physics
    this.trauma = 0; // 0 to 1
    this.maxShakeAngle = 0.05; // rad
    this.maxShakeOffset = 25; // px
  }

  // Smoothly target coordinates
  panTo(targetX, targetY, targetZoom, easeFactor = 0.08) {
    this.x += (targetX - this.x) * easeFactor;
    this.y += (targetY - this.y) * easeFactor;
    this.zoom += (targetZoom - this.zoom) * easeFactor;
  }

  // Add impact shake
  addTrauma(amount) {
    this.trauma = Math.min(1.0, this.trauma + amount);
  }

  // Apply camera transform to canvas context
  begin(ctx) {
    ctx.save();
    
    // Screen center pivot
    ctx.translate(this.w / 2, this.h / 2);
    
    // Trauma-based non-linear shake (trauma^2 or trauma^3)
    if (this.trauma > 0.001) {
      const shake = this.trauma * this.trauma;
      const shakeAngle = (Math.random() * 2 - 1) * this.maxShakeAngle * shake;
      const offsetX = (Math.random() * 2 - 1) * this.maxShakeOffset * shake;
      const offsetY = (Math.random() * 2 - 1) * this.maxShakeOffset * shake;
      
      ctx.rotate(this.rotation + shakeAngle);
      ctx.translate(offsetX, offsetY);
      this.trauma = Math.max(0, this.trauma - 0.02); // decay trauma
    } else {
      ctx.rotate(this.rotation);
    }
    
    // Zoom and camera target
    ctx.scale(this.zoom, this.zoom);
    ctx.translate(-this.x, -this.y);
  }

  // Restore context
  end(ctx) {
    ctx.restore();
  }
}
```

---

## 📑 Documentary Investigation Visuals (Dhruv Rathee / Vox Style)

### 1. The Article Zoom & Yellow Highlighter Stroke
Simulates zooming into a critical news article or official report, then drawing a luminous highlighter pen over key text:

```javascript
function renderDocumentHighlight(ctx, docImg, highlightRect, progress) {
  // 1. Draw background document with slight dark tint
  ctx.drawImage(docImg, 100, 100, 800, 1000);
  
  // 2. Animate highlighter stroke (0.0 to 1.0)
  if (progress > 0) {
    ctx.save();
    ctx.globalCompositeOperation = 'multiply'; // authentic pen blend
    ctx.fillStyle = 'rgba(255, 235, 59, 0.75)'; // vibrant highlighter yellow
    
    const currentWidth = highlightRect.width * Math.min(1, progress);
    
    // Slightly imperfect marker edges
    ctx.beginPath();
    ctx.roundRect(
      highlightRect.x, 
      highlightRect.y - 2, 
      currentWidth, 
      highlightRect.height + 4, 
      [3, 3, 3, 3]
    );
    ctx.fill();
    ctx.restore();
  }
}
```

### 2. Evidence Pinboard & Red String Connector
Connects suspicious actors, transactions, or locations with an oscillating dynamic tension string:

```javascript
function drawEvidenceString(ctx, x1, y1, x2, y2, tension = 0.95) {
  ctx.save();
  ctx.strokeStyle = '#ef4444'; // evidence red
  ctx.lineWidth = 3;
  ctx.shadowColor = 'rgba(239, 68, 68, 0.4)';
  ctx.shadowBlur = 8;
  
  const midX = (x1 + x2) / 2;
  // Sag curve based on tension
  const sag = (1 - tension) * 40;
  const midY = (y1 + y2) / 2 + sag;
  
  ctx.beginPath();
  ctx.moveTo(x1, y1);
  ctx.quadraticCurveTo(midX, midY, x2, y2);
  ctx.stroke();
  
  // Pins
  [ [x1, y1], [x2, y2] ].forEach(([px, py]) => {
    ctx.beginPath();
    ctx.arc(px, py, 6, 0, Math.PI * 2);
    ctx.fillStyle = '#dc2626';
    ctx.fill();
    ctx.strokeStyle = '#ffffff';
    ctx.lineWidth = 2;
    ctx.stroke();
  });
  
  ctx.restore();
}
```

### 3. Kinetic Number Counter with Rolling Decimals
```javascript
function renderCounter(ctx, startVal, endVal, progress, x, y, prefix = '$', suffix = '') {
  // Cubic ease out
  const t = 1 - Math.pow(1 - progress, 3);
  const current = startVal + (endVal - startVal) * t;
  
  const formatted = prefix + Math.floor(current).toLocaleString('en-US') + suffix;
  
  ctx.save();
  ctx.font = 'bold 56px "Outfit", sans-serif';
  ctx.fillStyle = '#f8fafc';
  ctx.textAlign = 'center';
  ctx.shadowColor = 'rgba(56, 189, 248, 0.5)';
  ctx.shadowBlur = 16;
  ctx.fillText(formatted, x, y);
  ctx.restore();
}
```

---

## 🎞️ Audio Synchronization Engine

Align visual scene transitions precisely with narration timestamps:

```javascript
class SceneTimeline {
  constructor(audioElement) {
    this.audio = audioElement;
    this.cues = [];
  }

  addCue(timeSeconds, sceneRenderer, options = {}) {
    this.cues.push({ time: timeSeconds, render: sceneRenderer, options });
    this.cues.sort((a, b) => a.time - b.time);
  }

  getCurrentScene() {
    const currentTime = this.audio ? this.audio.currentTime : 0;
    let activeCue = this.cues[0];
    
    for (let i = 0; i < this.cues.length; i++) {
      if (currentTime >= this.cues[i].time) {
        activeCue = this.cues[i];
      } else {
        break;
      }
    }
    return activeCue;
  }
}
```

---

## 🚀 Performance Rules for 60FPS Canvas Animation

1. **Pre-render Static Elements**: Draw static textures, document backgrounds, or intricate grids onto offscreen canvases once (`document.createElement('canvas')`). In the main loop, use `ctx.drawImage(offscreenCanvas, ...)` instead of repeating expensive vector calculations.
2. **Batch State Changes**: Minimize switching `ctx.fillStyle`, `ctx.font`, and `ctx.globalCompositeOperation`. Group all similar drawing commands together.
3. **Integer Pixel Alignment**: Subpixel rendering (`x = 100.432`) causes anti-aliasing fuzziness and extra GPU rasterization. Use `Math.round()` or `| 0` for crisp bounds.
4. **Clean up Clip & Save Stacks**: Every `ctx.save()` must strictly have an equal `ctx.restore()` to prevent memory leaks and performance degradation.

---

## 🎴 6. Deterministic Title-Card Video Engine (`projects/title_cards/`)

Silent, pure Canvas2D kinetic typography rendered frame-by-frame in headless Chrome and encoded to MP4 with FFmpeg:
- **Contract**: `window.renderFrame(t)` (and dual-compatible `window.seek(t)`) as a pure function of time; `window.READY = true` only after `document.fonts.load('700 168px "Space Grotesk"')` and `document.fonts.ready` resolve.
- **Card Kinetics**: Rise 40px while fading in over 0.5s (cubic ease-out), hold for $\max(1.2, 0.35 + \text{words}/3.2)$ seconds, fade out over 0.25s. Exactly one word per card in accent colour (`#c8ff3d`). Safe margin 144px.
- **Commands**:
  - `node render.mjs --stills` — renders one proof still per card into `stills/` for visual QA.
  - `node render.mjs` — renders full 30 FPS PNG sequence into `frames/` and encodes master MP4 with FFmpeg.
- **Boilerplate**: `viz/templates/title_cards_boilerplate.html`

