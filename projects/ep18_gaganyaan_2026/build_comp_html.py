import json

with open('c:/Users/dell/Desktop/my ai bot skills ok/projects/ep18_gaganyaan_2026/BEAT_SHEET_50.json', 'r', encoding='utf-8') as f:
    beats = json.load(f)

beats_json_str = json.dumps(beats, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EP-18: Gaganyaan 2026 — Bharat Ka Space Miracle (50 Beats · 05:08)</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #07090e;
      color: #f8fafc;
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      min-height: 100vh;
      overflow-x: hidden;
      padding-bottom: 60px;
    }}
    header {{
      width: 100%;
      max-width: 1360px;
      padding: 16px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-bottom: 1px solid rgba(255, 255, 255, 0.08);
      background: rgba(10, 15, 24, 0.88);
      backdrop-filter: blur(16px);
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .brand-group {{ display: flex; align-items: center; gap: 14px; }}
    .brand-logo {{
      width: 38px;
      height: 38px;
      border-radius: 50%;
      border: 1px solid rgba(251, 191, 36, 0.6);
      box-shadow: 0 0 12px rgba(251, 191, 36, 0.3);
      background: #000;
    }}
    .brand-title {{ font-size: 18px; font-weight: 800; letter-spacing: 0.8px; color: #fff; }}
    .brand-tag {{ font-size: 11px; font-weight: 700; color: #fbbf24; letter-spacing: 1.8px; text-transform: uppercase; }}
    .meta-pills {{ display: flex; align-items: center; gap: 10px; }}
    .pill {{
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.1);
      padding: 6px 14px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 600;
      font-family: 'JetBrains Mono', monospace;
      color: #94a3b8;
    }}
    .pill.accent {{ border-color: rgba(56, 189, 248, 0.4); color: #38bdf8; background: rgba(56, 189, 248, 0.08); }}
    .pill.gold {{ border-color: rgba(251, 191, 36, 0.4); color: #fbbf24; background: rgba(251, 191, 36, 0.08); }}
    .pill.flame {{ border-color: rgba(244, 63, 94, 0.4); color: #f43f5e; background: rgba(244, 63, 94, 0.08); }}

    .stage-container {{
      width: 100%;
      max-width: 1360px;
      display: flex;
      flex-direction: column;
      align-items: center;
      margin-top: 20px;
      padding: 0 16px;
    }}
    .canvas-wrapper {{
      position: relative;
      width: 100%;
      aspect-ratio: 16 / 9;
      background: #000;
      border-radius: 14px;
      overflow: hidden;
      box-shadow: 0 25px 60px rgba(0, 0, 0, 0.85), 0 0 0 1px rgba(255, 255, 255, 0.12);
    }}
    canvas {{ width: 100%; height: 100%; display: block; }}

    .controls-bar {{
      width: 100%;
      margin-top: 18px;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      padding: 16px 22px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      backdrop-filter: blur(16px);
    }}
    .timeline-row {{ display: flex; align-items: center; gap: 16px; width: 100%; }}
    .time-readout {{
      font-family: 'JetBrains Mono', monospace;
      font-size: 14px;
      font-weight: 700;
      color: #38bdf8;
      min-width: 110px;
    }}
    .scrubber {{
      flex: 1;
      height: 8px;
      -webkit-appearance: none;
      background: rgba(255, 255, 255, 0.12);
      border-radius: 4px;
      outline: none;
      cursor: pointer;
    }}
    .scrubber::-webkit-slider-thumb {{
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: #38bdf8;
      box-shadow: 0 0 12px rgba(56, 189, 248, 0.9);
      cursor: pointer;
    }}
    .buttons-row {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 10px;
    }}
    .btn-group {{ display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }}
    button {{
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 255, 255, 0.12);
      color: #f8fafc;
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    button:hover {{
      background: rgba(56, 189, 248, 0.15);
      border-color: rgba(56, 189, 248, 0.4);
      color: #38bdf8;
    }}
    button.primary {{
      background: #38bdf8;
      color: #07090e;
      border-color: #38bdf8;
      font-weight: 700;
    }}
    button.primary:hover {{
      background: #0ea5e9;
      box-shadow: 0 0 15px rgba(56, 189, 248, 0.4);
    }}
    .beat-info-badge {{
      font-size: 13px;
      font-weight: 600;
      color: #cbd5e1;
      display: flex;
      align-items: center;
      gap: 10px;
    }}
    .beat-highlight {{
      color: #fbbf24;
      font-family: 'JetBrains Mono', monospace;
    }}
  </style>
</head>
<body>

<header>
  <div class="brand-group">
    <img src="../../brand/logo.png" alt="Benaqaab Logo" class="brand-logo" onerror="this.style.display='none'">
    <div>
      <div class="brand-title">BENAQAAB INDIA</div>
      <div class="brand-tag">Sach · Saboot · Bebak</div>
    </div>
  </div>
  <div class="meta-pills">
    <div class="pill gold">EP-18 GAGANYAAN</div>
    <div class="pill accent" id="hudChapter">ACT 0: ROADMAP HOOK</div>
    <div class="pill flame" id="hudBeatPill">BEAT 1 / 50</div>
    <div class="pill">MASTER AUDIO SYNCED</div>
  </div>
</header>

<div class="stage-container">
  <div class="canvas-wrapper">
    <canvas id="viewCanvas" width="1920" height="1080"></canvas>
  </div>

  <audio id="masterAudio" src="master_audio.mp3" preload="auto"></audio>

  <div class="controls-bar">
    <div class="timeline-row">
      <span class="time-readout" id="timeDisplay">00:00 / 05:08</span>
      <input type="range" id="timeScrubber" class="scrubber" min="0" max="308.56" step="0.1" value="0">
    </div>
    <div class="buttons-row">
      <div class="btn-group">
        <button id="btnPlayPause" class="primary">▶ Play</button>
        <button id="btnPrevBeat">⏮ Prev Beat</button>
        <button id="btnNextBeat">Next Beat ⏭</button>
        <button id="btnJumpRoadmap">0:00 Hook</button>
        <button id="btnJumpBudget">0:18 ₹20k Cr Budget</button>
        <button id="btnJumpCryo">1:08 Cryo 8810s</button>
        <button id="btnJumpAbort">2:03 TV-D1 Abort</button>
        <button id="btnJumpRobot">2:34 Vyommitra</button>
        <button id="btnJumpPilots">3:35 Astronauts</button>
        <button id="btnJumpStation">4:25 BAS 2035</button>
        <button id="btnJumpMoon">4:56 Moon 2040</button>
        <button id="btnJumpVerdict">5:02 Verdict</button>
      </div>
      <div class="beat-info-badge">
        <span>Beat: <strong class="beat-highlight" id="beatName">Roadmap 3-Step Hook</strong></span>
        <button id="btnAudioToggle">🔊 VO AUDIO: ON</button>
      </div>
    </div>
  </div>
</div>

<script src="../../viz/motion.js"></script>
<script>
  const canvas = document.getElementById('viewCanvas');
  const ctx = canvas.getContext('2d');
  const scrubber = document.getElementById('timeScrubber');
  const timeDisplay = document.getElementById('timeDisplay');
  const btnPlayPause = document.getElementById('btnPlayPause');
  const hudBeatPill = document.getElementById('hudBeatPill');
  const hudChapter = document.getElementById('hudChapter');
  const beatName = document.getElementById('beatName');
  const btnAudioToggle = document.getElementById('btnAudioToggle');
  const masterAudio = document.getElementById('masterAudio');

  const TOTAL_DURATION = 308.56;
  let currentTime = 0;
  let isPlaying = false;
  let audioMuted = false;
  let lastTimestamp = 0;

  const logoImg = new Image();
  logoImg.src = '../../brand/logo.png';

  const BEATS_REGISTRY = {beats_json_str};
  const beatsData = BEATS_REGISTRY;

  // Preload all 50 AI Images
  const imageCache = {{}};
  BEATS_REGISTRY.forEach(b => {{
    const img = new Image();
    img.src = b.asset_path;
    imageCache[b.beat_id] = img;
    imageCache[b.asset_file] = img;
  }});

  function formatTime(s) {{
    const mins = Math.floor(s / 60);
    const secs = Math.floor(s % 60);
    return `${{String(mins).padStart(2, '0')}}:${{String(secs).padStart(2, '0')}}`;
  }}

  function getActiveBeat(t) {{
    for (let b of beatsData) {{
      if (t >= b.start_s && t < b.end_s) return b;
    }}
    return beatsData[beatsData.length - 1];
  }}

  // Pure deterministic render function of time
  window.seek = function(t) {{
    currentTime = Math.max(0, Math.min(TOTAL_DURATION, t));
    scrubber.value = currentTime;
    timeDisplay.textContent = `${{formatTime(currentTime)}} / 05:08`;
    if (Math.abs(masterAudio.currentTime - currentTime) > 0.3) {{
      masterAudio.currentTime = currentTime;
    }}
    render(currentTime);
  }};

  function render(t) {{
    ctx.fillStyle = '#07090e';
    ctx.fillRect(0, 0, 1920, 1080);

    const activeBeat = getActiveBeat(t);
    if (!activeBeat) return;

    hudBeatPill.textContent = `BEAT ${{activeBeat.beat_id}} / 50`;
    hudChapter.textContent = activeBeat.chapter.toUpperCase();
    beatName.textContent = activeBeat.subject;

    const beatDur = activeBeat.end_s - activeBeat.start_s;
    const beatProgress = Math.max(0, Math.min(1, (t - activeBeat.start_s) / beatDur));

    // --- 1. DRAW HERO IMAGE WITH VIRTUAL CAMERA DRIFT ---
    const img = imageCache[activeBeat.beat_id] || imageCache[activeBeat.asset_file];
    
    if (img && img.complete && img.naturalWidth > 0) {{
      ctx.save();
      ctx.translate(960, 540);
      // Smooth virtual camera zoom (Ken Burns 1.00 -> 1.055)
      const camScale = 1.0 + beatProgress * 0.055;
      const camPanX = (beatProgress - 0.5) * 20;
      ctx.scale(camScale, camScale);
      ctx.translate(camPanX, 0);

      const imgAspect = img.naturalWidth / img.naturalHeight;
      let dw = 1920, dh = 1080;
      if (imgAspect > (16 / 9)) {{
        dw = 1080 * imgAspect;
        dh = 1080;
      }} else {{
        dw = 1920;
        dh = 1920 / imgAspect;
      }}
      ctx.drawImage(img, -dw / 2, -dh / 2, dw, dh);
      ctx.restore();
    }} else {{
      const bgGrad = ctx.createRadialGradient(960, 540, 100, 960, 540, 1000);
      bgGrad.addColorStop(0, '#0c1222');
      bgGrad.addColorStop(1, '#04060a');
      ctx.fillStyle = bgGrad;
      ctx.fillRect(0, 0, 1920, 1080);
    }}

    // --- 2. CINEMATIC VIGNETTE & CONTRAST ---
    const vigGrad = ctx.createRadialGradient(960, 540, 480, 960, 540, 1100);
    vigGrad.addColorStop(0, 'rgba(0,0,0,0)');
    vigGrad.addColorStop(0.65, 'rgba(7, 9, 14, 0.35)');
    vigGrad.addColorStop(1, 'rgba(4, 6, 10, 0.78)');
    ctx.fillStyle = vigGrad;
    ctx.fillRect(0, 0, 1920, 1080);

    // Subtle 3% Grain Overlay
    if (window.Motion && Motion.drawGrain) {{
      Motion.drawGrain(ctx, 1920, 1080, 0.03);
    }}

    // --- 3. TOP-LEFT LOGO BUG (EXACT MATCH TO USER SCREENSHOT) ---
    ctx.save();
    const pillX = 40, pillY = 34, pillW = 216, pillH = 42, pillR = 21;
    ctx.fillStyle = 'rgba(12, 16, 24, 0.78)';
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.16)';
    ctx.lineWidth = 1;
    ctx.shadowColor = 'rgba(0, 0, 0, 0.5)';
    ctx.shadowBlur = 10;
    ctx.beginPath();
    ctx.roundRect(pillX, pillY, pillW, pillH, pillR);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Circular avatar logo on left
    const iconX = pillX + 7;
    const iconY = pillY + 7;
    const iconSize = 28;
    ctx.save();
    ctx.beginPath();
    ctx.arc(iconX + iconSize/2, iconY + iconSize/2, iconSize/2, 0, Math.PI * 2);
    ctx.clip();
    if (logoImg.complete && logoImg.naturalWidth > 0) {{
      ctx.drawImage(logoImg, iconX, iconY, iconSize, iconSize);
    }} else {{
      ctx.fillStyle = '#fbbf24';
      ctx.fillRect(iconX, iconY, iconSize, iconSize);
      ctx.fillStyle = '#000';
      ctx.font = '900 13px Inter, sans-serif';
      ctx.fillText('BI', iconX + 6, iconY + 19);
    }}
    ctx.restore();

    // Subtle circle border
    ctx.strokeStyle = 'rgba(251, 191, 36, 0.6)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(iconX + iconSize/2, iconY + iconSize/2, iconSize/2, 0, Math.PI * 2);
    ctx.stroke();

    // Bold, clean white text: BENAQAAB INDIA
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 14px -apple-system, BlinkMacSystemFont, "Inter", sans-serif';
    ctx.fillText('BENAQAAB INDIA', iconX + iconSize + 11, pillY + 26);
    ctx.restore();

    // --- 4. TOP-RIGHT VISUAL DENSITY COUNTER ---
    ctx.save();
    ctx.fillStyle = 'rgba(10, 15, 24, 0.88)';
    ctx.strokeStyle = 'rgba(56, 189, 248, 0.6)';
    ctx.lineWidth = 1.5;
    ctx.shadowColor = 'rgba(0, 0, 0, 0.6)';
    ctx.shadowBlur = 12;
    ctx.beginPath();
    ctx.roundRect(1600, 34, 280, 52, 10);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    ctx.fillStyle = '#94a3b8';
    ctx.font = '600 10.5px Inter, sans-serif';
    ctx.fillText('UNIVERSAL 10-VISUALS/MIN LAW', 1620, 53);

    ctx.fillStyle = '#38bdf8';
    ctx.font = '700 17px "JetBrains Mono", monospace';
    ctx.fillText(`VISUAL BEAT ${{activeBeat.beat_id}} / 50`, 1620, 74);
    ctx.restore();

    // --- 5. LOWER-LEFT FORENSIC TELEMETRY HUD STRAP ---
    ctx.save();
    ctx.fillStyle = 'rgba(10, 15, 24, 0.84)';
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.12)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.roundRect(40, 960, 780, 80, 10);
    ctx.fill();
    ctx.stroke();

    ctx.fillStyle = '#38bdf8';
    ctx.font = '700 12px "JetBrains Mono", monospace';
    ctx.fillText(`[BEAT ${{String(activeBeat.beat_id).padStart(2, '0')}}] ${{activeBeat.hud_data || 'TELEMETRY CONFIRMED'}}`, 60, 988);

    ctx.fillStyle = '#ffffff';
    ctx.font = '700 18px Inter, sans-serif';
    ctx.fillText(activeBeat.subject, 60, 1012);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 14px Inter, sans-serif';
    ctx.fillText(activeBeat.hindi_desc, 60, 1032);
    ctx.restore();


    // --- 7. BESPOKE FORENSIC MOTION GRAPHICS OVERLAY FOR EVERY BEAT ---
    if (window.Motion) {{
      const b = activeBeat;
      const tStart = b.start_s;

      // 7.1 Opening 5.5s Roadmap Hook (Frame 0 to 5.5s)
      if (t < 5.5) {{
        Motion.drawRoadmapCard(ctx, t, 0.0, 5.5, [
          {{ en: '01. ₹20,193 CR SECRET EXPANSION', hi: '18 सितंबर 2024: यूनियन कैबिनेट का सीक्रेट फैसला' }},
          {{ en: '02. VYOMMITRA HUMANOID FLIGHT', hi: 'इंसान से पहले रोबोट क्यों? 15-DOF सेंसरियम' }},
          {{ en: '03. 2035 BHARATIYA SPACE STATION', hi: '2028 BAS-01 मॉड्यूल और 2040 मून मिशन' }}
        ], 960, 540, 1080);
      }}

      // 7.2 Draw Specific Motion Graphic Elements based on beat specifications
      if (b.motion_type === 'roadmap_and_pin') {{
        if (t >= 5.5) {{
          Motion.drawCalloutPin(ctx, t, 5.5, b.target[0], b.target[1], b.elbow[0], b.elbow[1], b.title, b.subtitle, b.color);
        }}
      }}
      else if (b.motion_type === 'loupe_and_pin') {{
        Motion.drawEvidenceLoupe(ctx, t, tStart, b.loupe_center[0], b.loupe_center[1], b.loupe_r, 2.4);
        Motion.drawCalloutPin(ctx, t, tStart, b.target[0], b.target[1], b.elbow[0], b.elbow[1], b.title, b.subtitle, b.color);
      }}
      else if (b.motion_type === 'odometer_and_pin') {{
        Motion.drawOdometer(ctx, t, tStart, 2.5, b.odo_start, b.odo_end, b.odo_prefix, b.odo_suffix, 960, 720);
        Motion.drawCalloutPin(ctx, t, tStart, b.target[0], b.target[1], b.elbow[0], b.elbow[1], b.title, b.subtitle, b.color);
      }}
      else if (b.motion_type === 'loupe_and_odometer') {{
        Motion.drawEvidenceLoupe(ctx, t, tStart, b.loupe_center[0], b.loupe_center[1], b.loupe_r, 2.4);
        Motion.drawOdometer(ctx, t, tStart, 2.8, b.odo_start, b.odo_end, b.odo_prefix, b.odo_suffix, 960, 720);
        Motion.drawCalloutPin(ctx, t, tStart, b.target[0], b.target[1], b.elbow[0], b.elbow[1], b.title, b.subtitle, b.color);
      }}
      else if (b.motion_type === 'stamp') {{
        Motion.drawVerdictStamp(ctx, t, tStart + 0.8, b.stamp_en, b.stamp_hi, 960, 540);
        Motion.drawCalloutPin(ctx, t, tStart, b.target[0], b.target[1], b.elbow[0], b.elbow[1], b.title, b.subtitle, b.color);
      }}
      else if (b.motion_type === 'pin') {{
        Motion.drawCalloutPin(ctx, t, tStart, b.target[0], b.target[1], b.elbow[0], b.elbow[1], b.title, b.subtitle, b.color);
      }}
    }}
  }}

  // Audio & Animation Synchronization Loop
  function tick(timestamp) {{
    if (isPlaying) {{
      if (!masterAudio.paused) {{
        currentTime = masterAudio.currentTime;
      }} else {{
        if (!lastTimestamp) lastTimestamp = timestamp;
        const delta = (timestamp - lastTimestamp) / 1000;
        currentTime += delta;
      }}
      lastTimestamp = timestamp;

      if (currentTime >= TOTAL_DURATION) {{
        currentTime = TOTAL_DURATION;
        isPlaying = false;
        masterAudio.pause();
        btnPlayPause.textContent = '▶ Play';
      }}
      scrubber.value = currentTime;
      timeDisplay.textContent = `${{formatTime(currentTime)}} / 05:08`;
      render(currentTime);
    }}
    requestAnimationFrame(tick);
  }}
  requestAnimationFrame(tick);

  // UI Event Handlers
  btnPlayPause.addEventListener('click', () => {{
    isPlaying = !isPlaying;
    if (isPlaying) {{
      masterAudio.currentTime = currentTime;
      masterAudio.play().catch(() => {{}});
      btnPlayPause.textContent = '⏸ Pause';
    }} else {{
      masterAudio.pause();
      btnPlayPause.textContent = '▶ Play';
    }}
  }});

  scrubber.addEventListener('input', (e) => {{
    window.seek(parseFloat(e.target.value));
  }});

  btnPrevBeat.addEventListener('click', () => {{
    const active = getActiveBeat(currentTime);
    if (active) window.seek(Math.max(0, active.start_s - 6.17));
  }});

  btnNextBeat.addEventListener('click', () => {{
    const active = getActiveBeat(currentTime);
    if (active) window.seek(Math.min(TOTAL_DURATION, active.start_s + 6.17));
  }});

  document.getElementById('btnJumpRoadmap').addEventListener('click', () => window.seek(0.0));
  document.getElementById('btnJumpBudget').addEventListener('click', () => window.seek(18.5));
  document.getElementById('btnJumpCryo').addEventListener('click', () => window.seek(67.9));
  document.getElementById('btnJumpAbort').addEventListener('click', () => window.seek(123.4));
  document.getElementById('btnJumpRobot').addEventListener('click', () => window.seek(154.3));
  document.getElementById('btnJumpPilots').addEventListener('click', () => window.seek(215.0));
  document.getElementById('btnJumpStation').addEventListener('click', () => window.seek(265.4));
  document.getElementById('btnJumpMoon').addEventListener('click', () => window.seek(296.2));
  document.getElementById('btnJumpVerdict').addEventListener('click', () => window.seek(302.4));

  btnAudioToggle.addEventListener('click', () => {{
    audioMuted = !audioMuted;
    masterAudio.muted = audioMuted;
    btnAudioToggle.textContent = audioMuted ? '🔇 VO AUDIO: OFF' : '🔊 VO AUDIO: ON';
  }});

  // Initial draw
  render(0);
</script>
</body>
</html>
"""

with open('c:/Users/dell/Desktop/my ai bot skills ok/projects/ep18_gaganyaan_2026/comp.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Rebuilt comp.html successfully with full 50-beat motion graphics and exact screenshot logo badge.")
