# 🛡️ BROADCAST VIDEO FORENSIC STYLIZATION & FAIR-USE PROTOCOL
### Core Methodology for Integrating External News & Public Source Clips

> **Security & Privacy Notice:** All raw leader reference images are kept strictly local and excluded from Git tracking via `.gitignore`. This document codifies the technical methodology, filter recipe, and script directives.

---

## 📌 1. The Core Idea & Editorial Purpose
Whenever incorporating external broadcast news, press briefings, or official government footage:
1. **Defeat Automated Content ID Claims:** Raw unmodified broadcast video triggers automated algorithmic copyright strikes and false takedowns.
2. **Establish Forensic Signature:** Transform generic footage into Benaqaab's distinct visual journalism aesthetic (`SACH · SABOOT · BEBAK`).
3. **Focus Viewer Attention:** Emphasize the factual spoken statement and primary-source document rather than distracting video artifacts.

---

## 🎨 2. The 3-Step Forensic Filter Recipe (In Code)
Any script or composition (`comp.html` / `viz/motion.js`) treating external video must apply:
1. **Monochrome Base Desaturation:** Desaturate video to high-contrast black-and-white (`filter: grayscale(100%) contrast(125%) brightness(95%)`).
2. **Dot-Matrix Halftone Texture:** Overlay an authentic 4px dot-matrix printing grid (`globalCompositeOperation = 'multiply'`) simulating newspaper gazette print.
3. **Forensic Redaction Bar:** Apply a matte crimson horizontal bar (`rgba(239, 68, 68, 0.65)`) across the upper focal region (`height: 12% to 16%` of frame) with 1px border.

---

## 🎙️ 3. What the AI Voiceover Must Say (Editorial Context)
When introducing external clips, the narration must establish factual provenance immediately:
- *"Official statement record se..."* (From the official statement on record...)
- *"Sarkari press briefing ke mutabiq..."* (According to the official government briefing...)
- *"Yeh bayan sidhe record par hai..."* (This statement is on official record...)

---

## 💻 4. Code Implementation
```javascript
// Example: Forensic filter applied over video frame in comp.html canvas
function applyForensicNewsFilter(ctx, videoEl, x, y, w, h) {
  // 1. Draw grayscale video
  ctx.save();
  ctx.filter = 'grayscale(100%) contrast(120%)';
  ctx.drawImage(videoEl, x, y, w, h);
  ctx.restore();

  // 2. Draw red horizontal investigative bar
  const barY = y + h * 0.28;
  const barH = h * 0.14;
  ctx.fillStyle = 'rgba(239, 68, 68, 0.65)';
  ctx.fillRect(x, barY, w, barH);
  ctx.strokeStyle = '#dc2626';
  ctx.lineWidth = 1.5;
  ctx.strokeRect(x, barY, w, barH);
}
```
