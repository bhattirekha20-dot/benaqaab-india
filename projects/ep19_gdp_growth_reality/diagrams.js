/**
 * diagrams.js — Benaqaab India Forensic Motion Graphics Diagrams Engine
 * Episode EP-19: India's 7.8% GDP vs Global Superpowers
 * 
 * Features 7 bespoke analytical diagrams rendered dynamically on top of background plates:
 * 1. drawGdpGvaDiagram (64.29s - 83.45s)
 * 2. drawPerCapitaComparisonDiagram (148.53s - 173.16s)
 * 3. drawKShapedDivergenceDiagram (185.71s - 224.59s)
 * 4. drawHouseholdDebtCrisisDiagram (335.95s - 361.60s)
 * 5. drawMissingFactoryDiagram (365.03s - 405.48s)
 * 6. drawDemographicClockDiagram (500.18s - 525.70s)
 * 7. drawFourPillarsBlueprintDiagram (532.37s - 572.61s)
 */

(function(root) {
  'use strict';

  // Easing helpers
  function easeOutCubic(x) {
    return 1 - Math.pow(1 - Math.max(0, Math.min(1, x)), 3);
  }
  function easeInOutQuad(x) {
    return x < 0.5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2;
  }

  // Draw ultra-translucent frosted glass card backdrop (High background visibility)
  function drawGlassCard(ctx, x, y, w, h, r = 16, borderColor = 'rgba(56, 189, 248, 0.38)', bgColor = null) {
    ctx.save();

    // Translucent spatial frosted glass that keeps background image vividly visible (Apple visionOS standard)
    const glassGrad = ctx.createLinearGradient(x, y, x, y + h);
    glassGrad.addColorStop(0, 'rgba(8, 14, 26, 0.44)');
    glassGrad.addColorStop(1, 'rgba(5, 8, 16, 0.36)');
    ctx.fillStyle = glassGrad;

    ctx.strokeStyle = borderColor;
    ctx.lineWidth = 1.2;
    ctx.shadowColor = 'rgba(0, 0, 0, 0.65)';
    ctx.shadowBlur = 18;
    ctx.beginPath();
    ctx.roundRect(x, y, w, h, r);
    ctx.fill();
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Specular top highlight line
    const specGrad = ctx.createLinearGradient(x, y, x + w, y);
    specGrad.addColorStop(0, 'rgba(255, 255, 255, 0)');
    specGrad.addColorStop(0.25, 'rgba(255, 255, 255, 0.35)');
    specGrad.addColorStop(0.75, borderColor);
    specGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
    ctx.strokeStyle = specGrad;
    ctx.lineWidth = 1.2;
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.stroke();

    ctx.restore();
  }

  // Draw glowing badge pill
  function drawBadge(ctx, text, x, y, textColor = '#38bdf8', bgColor = 'rgba(56, 189, 248, 0.12)', borderColor = 'rgba(56, 189, 248, 0.4)') {
    ctx.save();
    ctx.font = '700 12px "JetBrains Mono", monospace';
    const tw = ctx.measureText(text).width;
    const pw = tw + 20, ph = 24;
    ctx.fillStyle = bgColor;
    ctx.strokeStyle = borderColor;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.roundRect(x - pw/2, y - ph/2, pw, ph, 12);
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = textColor;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(text, x, y);
    ctx.restore();
  }

  // -------------------------------------------------------------
  // DIAGRAM 1: GDP vs GVA Discrepancy (64.29s - 83.45s)
  // Progressive Infographic Motion: 6 Staged Phases
  // -------------------------------------------------------------
  function drawGdpGvaDiagram(ctx, t, start_s = 64.29, end_s = 83.45) {
    if (t < start_s || t >= end_s) return;
    const dur = end_s - start_s;
    const elapsed = t - start_s;
    const remaining = end_s - t;

    // Master alpha fade in & out
    let masterAlpha = 1.0;
    if (elapsed < 0.45) masterAlpha = easeOutCubic(elapsed / 0.45);
    else if (remaining < 0.4) masterAlpha = Math.max(0, remaining / 0.4);

    ctx.save();
    ctx.globalAlpha = masterAlpha;

    // Relative progressive phase progress
    // Phase 1 (0.0s - 2.2s): Headline in Center
    // Phase 2 (2.2s - 4.2s): Headline glides to Top Anchor + guide rule wipes out
    // Phase 3 (4.2s - 8.0s): Step 1 (Production Base GVA 8.2%) enters + odometer rolls
    // Phase 4 (8.0s - 12.0s): Step 2 (Statistical Wedge -0.4%) enters + minus sign
    // Phase 5 (12.0s - 15.5s): Step 3 (Headline Result GDP 7.8%) enters + equals sign
    // Phase 6 (15.5s - 19.16s): Active connected conduits pulse + Ground Reality Verdict banner slides up

    const headerIn = Math.min(1, elapsed / 0.5);
    const headerMove = elapsed > 2.2 ? Math.min(1, (elapsed - 2.2) / 1.5) : 0;
    const headerEasedMove = 1 - Math.pow(1 - headerMove, 3); // outCubic

    // Header position: Center (cy = 490) -> Top Anchor (cy = 115)
    const headerCX = 960;
    const headerCY = 490 - headerEasedMove * 375;
    const headerScale = 1.12 - headerEasedMove * 0.12;

    // Mini Live Tag Helper
    function drawLiveBadge(bx, by, col, alp = 1.0, label = 'LIVE') {
      ctx.save();
      ctx.globalAlpha = masterAlpha * alp;
      const bw = 54, bh = 20;
      ctx.fillStyle = 'rgba(8, 14, 26, 0.85)';
      ctx.strokeStyle = col;
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.roundRect(bx, by, bw, bh, 6);
      ctx.fill();
      ctx.stroke();

      const pulse = 0.5 + 0.5 * Math.sin(t * 7);
      ctx.fillStyle = col;
      ctx.shadowColor = col;
      ctx.shadowBlur = 6 * pulse;
      ctx.beginPath();
      ctx.arc(bx + 9, by + 10, 3.2, 0, Math.PI * 2);
      ctx.fill();
      ctx.shadowBlur = 0;

      ctx.font = '800 9.5px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.textBaseline = 'middle';
      ctx.fillText(label, bx + 17, by + 10.5);
      ctx.restore();
    }

    // --- PHASE 01 & 02: HEADLINE PANEL ---
    ctx.save();
    ctx.translate(headerCX, headerCY);
    ctx.scale(headerScale, headerScale);
    ctx.globalAlpha = masterAlpha * headerIn;

    drawBadge(ctx, 'OFFICIAL DATA DISSECTION · MoSPI Q1 NATIONAL ACCOUNTS', 0, -32, '#38bdf8', 'rgba(56, 189, 248, 0.15)', 'rgba(56, 189, 248, 0.4)');
    
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 28px "Outfit", "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('THE GDP vs GVA WEDGE: WHAT HEADLINE 7.8% MASKS', 0, 10);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 14px "Inter", sans-serif';
    ctx.fillText('Gross Domestic Product = Gross Value Added + Net Indirect Taxes (Taxes − Subsidies)', 0, 38);

    if (elapsed < 2.2) {
      drawLiveBadge(290, -42, '#38bdf8', headerIn, 'AUDIT');
    } else {
      drawLiveBadge(370, -42, '#38bdf8', 0.85, 'AUDIT');
    }
    ctx.restore();

    // Baseline horizontal guide rule wipes out once header reaches top
    if (headerEasedMove > 0.3) {
      const guideAlpha = Math.min(1, (headerEasedMove - 0.3) / 0.7);
      ctx.save();
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.35)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(960 - 800 * guideAlpha, 182);
      ctx.lineTo(960 + 800 * guideAlpha, 182);
      ctx.stroke();
      ctx.restore();
    }

    // Card Layout Specs
    const colY = 200;
    const colH = 415;
    const colW = 460;
    const c1FinalX = 160;
    const c2FinalX = 730;
    const c3FinalX = 1300;

    // --- PHASE 03: STEP 1: PRODUCTION BASE (GVA 8.2%) (Enters at 4.2s) ---
    if (elapsed >= 4.0) {
      const p1 = Math.min(1, (elapsed - 4.0) / 1.0);
      const c1 = 1.70158, c3 = 2.70158;
      const overshoot1 = 1 + c3 * Math.pow(p1 - 1, 3) + c1 * Math.pow(p1 - 1, 2);
      const c1X = 400 + (c1FinalX - 400) * overshoot1;
      const float1 = elapsed > 5.5 ? Math.sin(t * 1.7) * 2.5 : 0;

      // Odometer for 8.2%
      const numProg1 = Math.min(1, Math.max(0, (elapsed - 4.3) / 1.5));
      const val1 = (8.2 * easeOutCubic(numProg1)).toFixed(1);

      ctx.save();
      ctx.globalAlpha = masterAlpha * Math.min(1, (elapsed - 4.0) / 0.4);
      drawGlassCard(ctx, c1X, colY + float1, colW, colH, 16, 'rgba(14, 165, 233, 0.45)', 'rgba(14, 165, 233, 0.08)');
      drawLiveBadge(c1X + colW - 86, colY + float1 - 12, '#38bdf8', 0.95, 'BASE');

      ctx.fillStyle = '#38bdf8';
      ctx.font = '700 14px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('STEP 1: PRODUCTION BASE', c1X + 28, colY + float1 + 42);

      ctx.fillStyle = '#ffffff';
      ctx.font = '800 24px "Inter", sans-serif';
      ctx.fillText('Real GVA Growth', c1X + 28, colY + float1 + 78);

      // Main Big Metric
      ctx.fillStyle = '#38bdf8';
      ctx.font = '900 62px "JetBrains Mono", monospace';
      ctx.shadowColor = 'rgba(56, 189, 248, 0.5)';
      ctx.shadowBlur = 14;
      ctx.fillText(val1 + '%', c1X + 28, colY + float1 + 158);
      ctx.shadowBlur = 0;

      // Sub-label
      ctx.fillStyle = '#94a3b8';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.fillText('Gross Value Added across economic sectors', c1X + 28, colY + float1 + 192);

      // Divider line
      ctx.strokeStyle = 'rgba(56, 189, 248, 0.25)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(c1X + 28, colY + float1 + 215);
      ctx.lineTo(c1X + colW - 28, colY + float1 + 215);
      ctx.stroke();

      // Bullet insights
      const bAlpha1 = Math.min(1, Math.max(0, (elapsed - 5.0) / 0.8));
      ctx.globalAlpha = masterAlpha * bAlpha1;
      ctx.fillStyle = '#e2e8f0';
      ctx.font = '500 15px "Inter", sans-serif';
      ctx.fillText('• Core supply-side output across factories & farms', c1X + 28, colY + float1 + 252);
      ctx.fillText('• Driven by capital-heavy financial & IT hubs', c1X + 28, colY + float1 + 284);
      ctx.fillText('• Rural agricultural growth stagnant at ~1.4%', c1X + 28, colY + float1 + 316);

      // Footnote Pill
      drawBadge(ctx, 'PRIMARY SOURCE: MoSPI GVA RELEASE', c1X + 170, colY + float1 + 372, '#38bdf8', 'rgba(56,189,248,0.1)', 'rgba(56,189,248,0.3)');

      ctx.restore();
    }

    // --- PHASE 04: STEP 2: STATISTICAL WEDGE (-0.4%) (Enters at 8.0s) ---
    if (elapsed >= 7.8) {
      const p2 = Math.min(1, (elapsed - 7.8) / 1.0);
      const c1 = 1.70158, c3 = 2.70158;
      const overshoot2 = 1 + c3 * Math.pow(p2 - 1, 3) + c1 * Math.pow(p2 - 1, 2);
      const c2X = 900 + (c2FinalX - 900) * overshoot2;
      const float2 = elapsed > 9.2 ? Math.sin(t * 1.7 + 1.2) * 2.5 : 0;

      // Minus Operator
      const opAlpha1 = Math.min(1, (elapsed - 7.8) / 0.4);
      ctx.save();
      ctx.globalAlpha = masterAlpha * opAlpha1;
      ctx.fillStyle = '#fbbf24';
      ctx.shadowColor = 'rgba(251, 191, 36, 0.6)';
      ctx.shadowBlur = 12;
      ctx.font = '900 48px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('−', (c1FinalX + colW + c2FinalX) / 2, colY + colH/2);
      ctx.restore();

      // Odometer for -0.4%
      const numProg2 = Math.min(1, Math.max(0, (elapsed - 8.1) / 1.5));
      const val2 = (-0.4 * easeOutCubic(numProg2)).toFixed(1);

      ctx.save();
      ctx.globalAlpha = masterAlpha * Math.min(1, (elapsed - 7.8) / 0.4);
      drawGlassCard(ctx, c2X, colY + float2, colW, colH, 16, 'rgba(251, 191, 36, 0.45)', 'rgba(251, 191, 36, 0.08)');
      drawLiveBadge(c2X + colW - 86, colY + float2 - 12, '#fbbf24', 0.95, 'WEDGE');

      ctx.fillStyle = '#fbbf24';
      ctx.font = '700 14px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('STEP 2: STATISTICAL WEDGE', c2X + 28, colY + float2 + 42);

      ctx.fillStyle = '#ffffff';
      ctx.font = '800 24px "Inter", sans-serif';
      ctx.fillText('Net Product Taxes', c2X + 28, colY + float2 + 78);

      // Main Big Metric
      ctx.fillStyle = '#fbbf24';
      ctx.font = '900 62px "JetBrains Mono", monospace';
      ctx.shadowColor = 'rgba(251, 191, 36, 0.5)';
      ctx.shadowBlur = 14;
      ctx.fillText(val2 + '%', c2X + 28, colY + float2 + 158);
      ctx.shadowBlur = 0;

      // Sub-label
      ctx.fillStyle = '#94a3b8';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.fillText('Indirect Taxes collected minus government subsidies', c2X + 28, colY + float2 + 192);

      // Divider line
      ctx.strokeStyle = 'rgba(251, 191, 36, 0.25)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(c2X + 28, colY + float2 + 215);
      ctx.lineTo(c2X + colW - 28, colY + float2 + 215);
      ctx.stroke();

      // Bullet insights
      const bAlpha2 = Math.min(1, Math.max(0, (elapsed - 8.8) / 0.8));
      ctx.globalAlpha = masterAlpha * bAlpha2;
      ctx.fillStyle = '#e2e8f0';
      ctx.font = '500 15px "Inter", sans-serif';
      ctx.fillText('• Fertilizer & food subsidy payouts trimmed sharply', c2X + 28, colY + float2 + 252);
      ctx.fillText('• Robust GST indirect tax collections inflate math', c2X + 28, colY + float2 + 284);
      ctx.fillText('• Creates an artificial statistical wedge in headline', c2X + 28, colY + float2 + 316);

      // Footnote Pill
      drawBadge(ctx, 'DISCREPANCY FORMULA: TAXES − SUBSIDIES', c2X + 210, colY + float2 + 372, '#fbbf24', 'rgba(251,191,36,0.1)', 'rgba(251,191,36,0.3)');

      ctx.restore();
    }

    // --- PHASE 05: STEP 3: HEADLINE RESULT (GDP 7.8%) (Enters at 12.0s) ---
    if (elapsed >= 11.8) {
      const p3 = Math.min(1, (elapsed - 11.8) / 1.0);
      const c1 = 1.70158, c3 = 2.70158;
      const overshoot3 = 1 + c3 * Math.pow(p3 - 1, 3) + c1 * Math.pow(p3 - 1, 2);
      const c3X = 1450 + (c3FinalX - 1450) * overshoot3;
      const float3 = elapsed > 13.2 ? Math.sin(t * 1.7 + 2.4) * 2.5 : 0;

      // Equals Operator
      const opAlpha2 = Math.min(1, (elapsed - 11.8) / 0.4);
      ctx.save();
      ctx.globalAlpha = masterAlpha * opAlpha2;
      ctx.fillStyle = '#10b981';
      ctx.shadowColor = 'rgba(16, 185, 129, 0.6)';
      ctx.shadowBlur = 12;
      ctx.font = '900 48px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('=', (c2FinalX + colW + c3FinalX) / 2, colY + colH/2);
      ctx.restore();

      // Odometer for 7.8%
      const numProg3 = Math.min(1, Math.max(0, (elapsed - 12.1) / 1.5));
      const val3 = (7.8 * easeOutCubic(numProg3)).toFixed(1);

      ctx.save();
      ctx.globalAlpha = masterAlpha * Math.min(1, (elapsed - 11.8) / 0.4);
      drawGlassCard(ctx, c3X, colY + float3, colW, colH, 16, 'rgba(16, 185, 129, 0.50)', 'rgba(16, 185, 129, 0.08)');
      drawLiveBadge(c3X + colW - 86, colY + float3 - 12, '#10b981', 0.95, 'RESULT');

      ctx.fillStyle = '#10b981';
      ctx.font = '700 14px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('STEP 3: HEADLINE RESULT', c3X + 28, colY + float3 + 42);

      ctx.fillStyle = '#ffffff';
      ctx.font = '800 24px "Inter", sans-serif';
      ctx.fillText('Real GDP Growth', c3X + 28, colY + float3 + 78);

      // Main Big Metric
      ctx.fillStyle = '#10b981';
      ctx.font = '900 62px "JetBrains Mono", monospace';
      ctx.shadowColor = 'rgba(16, 185, 129, 0.6)';
      ctx.shadowBlur = 16;
      ctx.fillText(val3 + '%', c3X + 28, colY + float3 + 158);
      ctx.shadowBlur = 0;

      // Sub-label
      ctx.fillStyle = '#94a3b8';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.fillText('Official global celebration figure', c3X + 28, colY + float3 + 192);

      // Divider line
      ctx.strokeStyle = 'rgba(16, 185, 129, 0.25)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(c3X + 28, colY + float3 + 215);
      ctx.lineTo(c3X + colW - 28, colY + float3 + 215);
      ctx.stroke();

      // Bullet insights
      const bAlpha3 = Math.min(1, Math.max(0, (elapsed - 12.8) / 0.8));
      ctx.globalAlpha = masterAlpha * bAlpha3;
      ctx.fillStyle = '#e2e8f0';
      ctx.font = '500 15px "Inter", sans-serif';
      ctx.fillText('• Fastest growing major economy in the world', c3X + 28, colY + float3 + 252);
      ctx.fillText('• Celebrated on global news & Davos summits', c3X + 28, colY + float3 + 284);
      ctx.fillText('• Conceals acute private consumption slowdown', c3X + 28, colY + float3 + 316);

      // Footnote Pill
      drawBadge(ctx, 'HEADLINE MASKS GROUND DISPARITY', c3X + 210, colY + float3 + 372, '#10b981', 'rgba(16,185,129,0.1)', 'rgba(16,185,129,0.3)');

      ctx.restore();
    }

    // --- PHASE 06: CONNECTED STREAM & GROUND REALITY VERDICT (Enters at 15.5s) ---
    if (elapsed >= 15.0) {
      // 1. Kinetic energy packets flowing along conduits
      ctx.save();
      const streamTime = t * 3.5;
      const conduitY = colY + colH / 2;

      // Packet 1: C1 -> C2
      const p1X = (c1FinalX + colW) + ((c2FinalX - (c1FinalX + colW)) * ((streamTime % 1)));
      ctx.fillStyle = '#38bdf8';
      ctx.shadowColor = '#38bdf8';
      ctx.shadowBlur = 8;
      ctx.beginPath();
      ctx.arc(p1X, conduitY, 3.5, 0, Math.PI * 2);
      ctx.fill();

      // Packet 2: C2 -> C3
      const p2X = (c2FinalX + colW) + ((c3FinalX - (c2FinalX + colW)) * (((streamTime + 0.5) % 1)));
      ctx.fillStyle = '#fbbf24';
      ctx.shadowColor = '#fbbf24';
      ctx.shadowBlur = 8;
      ctx.beginPath();
      ctx.arc(p2X, conduitY, 3.5, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();

      // 2. Bottom Ground Reality Verdict Banner
      const botP = Math.min(1, (elapsed - 15.0) / 0.9);
      const botAlpha = easeOutCubic(botP);
      const botY = 645 + (1 - botAlpha) * 35;
      const bannerW = 1600;

      ctx.save();
      ctx.globalAlpha = masterAlpha * botAlpha;
      drawGlassCard(ctx, 160, botY, bannerW, 90, 14, 'rgba(56, 189, 248, 0.40)', 'rgba(8, 14, 26, 0.88)');

      // Live tag
      drawLiveBadge(160 + bannerW - 96, botY - 12, '#38bdf8', 0.95, 'VERDICT');

      ctx.fillStyle = '#38bdf8';
      ctx.font = '800 15px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('🔍 BENAQAAB FORENSIC VERDICT:', 195, botY + 36);

      ctx.fillStyle = '#f8fafc';
      ctx.font = '600 16px "Inter", sans-serif';
      ctx.fillText('जब जीडीपी कागज़ पर 7.8% दिखता है लेकिन आम परिवार की शुद्ध बचत 47 साल के न्यूनतम स्तर पर गिर जाती है,', 195, botY + 65);

      // Highlighted punchline
      ctx.fillStyle = '#fbbf24';
      ctx.font = '700 16px "Inter", sans-serif';
      ctx.fillText('तो ग्रोथ का फ़ायदा आम जनता तक नहीं पहुंच रहा— यह केवल टॉप 15% और कॉरपोरेट मुनाफ़ों में सीमित है!', 985, botY + 65);

      ctx.restore();
    }

    ctx.restore();
  }

  // -------------------------------------------------------------
  // DIAGRAM 2: Global Per-Capita Income Comparison (148.53s - 173.16s)
  // -------------------------------------------------------------
  function drawPerCapitaComparisonDiagram(ctx, t, start_s = 148.53, end_s = 173.16) {
    if (t < start_s || t >= end_s) return;
    const elapsed = t - start_s;
    const remaining = end_s - t;

    let alpha = 1.0;
    let enterOffset = 0;
    if (elapsed < 0.5) {
      const p = elapsed / 0.5;
      alpha = easeOutCubic(p);
      enterOffset = (1 - easeOutCubic(p)) * 40;
    } else if (remaining < 0.4) {
      alpha = Math.max(0, remaining / 0.4);
    }

    ctx.save();
    ctx.globalAlpha = alpha;

    const cx = 960, cy = 525 + enterOffset;
    const cardW = 1200, cardH = 610;
    const x = cx - cardW/2, y = cy - cardH/2;

    drawGlassCard(ctx, x, y, cardW, cardH, 20, 'rgba(56, 189, 248, 0.4)');

    // Header
    drawBadge(ctx, 'WORLD BANK DATA · GLOBAL PER-CAPITA INCOME BENCHMARK', cx, y + 40, '#fbbf24', 'rgba(251, 191, 36, 0.15)', 'rgba(251, 191, 36, 0.4)');
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 28px "Outfit", "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('5th LARGEST ECONOMY vs #136 PER-CAPITA PROSPERITY', cx, y + 80);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 15px "Inter", sans-serif';
    ctx.fillText('Annual Gross National Income per Capita in USD (World Bank Atlas Method)', cx, y + 108);

    // 4 Country Rows: USA, Germany, China, India
    const rows = [
      { name: 'UNITED STATES', flag: '🇺🇸', val: 85000, disp: '$85,000', mult: '31x HIGHER', color: '#38bdf8', activeAt: 148.53 },
      { name: 'GERMANY', flag: '🇩🇪', val: 54000, disp: '$54,000', mult: '20x HIGHER', color: '#818cf8', activeAt: 157.87 },
      { name: 'CHINA', flag: '🇨🇳', val: 13500, disp: '$13,500', mult: '5x HIGHER', color: '#f59e0b', activeAt: 163.87 },
      { name: 'INDIA (OUR REALITY)', flag: '🇮🇳', val: 2730, disp: '$2,730 (₹2.28L)', mult: 'RANK #136', color: '#f43f5e', activeAt: 148.53 }
    ];

    const maxVal = 90000;
    const startY = y + 145;
    const rowH = 88;
    const barMaxW = 460;

    rows.forEach((r, idx) => {
      const ry = startY + idx * rowH;
      const isHighlighted = t >= r.activeAt;
      const rowAlpha = isHighlighted ? 1.0 : 0.35;

      ctx.save();
      ctx.globalAlpha = alpha * rowAlpha;

      // Row background
      drawGlassCard(ctx, x + 40, ry, cardW - 80, 74, 12, isHighlighted ? r.color : 'rgba(255,255,255,0.08)', isHighlighted ? 'rgba(15, 23, 42, 0.75)' : 'rgba(15, 23, 42, 0.4)');

      // Country Flag & Label
      ctx.fillStyle = '#ffffff';
      ctx.font = '800 18px "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(`${r.flag}  ${r.name}`, x + 65, ry + 44);

      // Bar progress
      const targetW = (r.val / maxVal) * barMaxW;
      const barX = x + 340;
      const barY = ry + 24;
      const barH = 26;

      // Track
      ctx.fillStyle = 'rgba(255, 255, 255, 0.06)';
      ctx.beginPath();
      ctx.roundRect(barX, barY, barMaxW, barH, 6);
      ctx.fill();

      // Filled Bar with Spring Animation
      const fillProgress = isHighlighted ? Math.min(1, (t - r.activeAt) / 0.8) : 0;
      const curW = Math.max(18, targetW * easeOutCubic(fillProgress));

      ctx.fillStyle = r.color;
      ctx.shadowColor = r.color;
      ctx.shadowBlur = isHighlighted ? 12 : 0;
      ctx.beginPath();
      ctx.roundRect(barX, barY, curW, barH, 6);
      ctx.fill();
      ctx.shadowBlur = 0;

      // Value text in dedicated column
      ctx.fillStyle = '#ffffff';
      ctx.font = '800 17px "JetBrains Mono", monospace';
      ctx.textAlign = 'right';
      ctx.fillText(r.disp, x + cardW - 220, ry + 44);

      // Multiplier Badge
      drawBadge(ctx, r.mult, x + cardW - 110, ry + 37, r.color, 'rgba(0,0,0,0.5)', r.color);

      ctx.restore();
    });

    // Bottom Note
    const noteY = y + 515;
    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 14px "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('भारत का जीडीपी पांचवां बड़ा ज़रूर है, लेकिन 143 करोड़ की आबादी में बांटने पर हम लोअर-मिडिल इनकम ब्रैकेट में हैं।', cx, noteY + 25);
    ctx.fillText('Sources: World Bank Open Data (2025-26) · IMF World Economic Outlook', cx, noteY + 50);

    ctx.restore();
  }

  // -------------------------------------------------------------
  // DIAGRAM 3: K-Shaped Divergence Diagram (185.71s - 224.59s)
  // -------------------------------------------------------------
  function drawKShapedDivergenceDiagram(ctx, t, start_s = 185.71, end_s = 224.59) {
    if (t < start_s || t >= end_s) return;
    const elapsed = t - start_s;
    const remaining = end_s - t;

    let alpha = 1.0;
    let enterOffset = 0;
    if (elapsed < 0.5) {
      const p = elapsed / 0.5;
      alpha = easeOutCubic(p);
      enterOffset = (1 - easeOutCubic(p)) * 40;
    } else if (remaining < 0.4) {
      alpha = Math.max(0, remaining / 0.4);
    }

    ctx.save();
    ctx.globalAlpha = alpha;

    const cx = 960, cy = 525 + enterOffset;
    const cardW = 1220, cardH = 620;
    const x = cx - cardW/2, y = cy - cardH/2;

    drawGlassCard(ctx, x, y, cardW, cardH, 20, 'rgba(56, 189, 248, 0.4)');

    // Header
    drawBadge(ctx, 'ECONOMIC PHENOMENON · TWO PARALLEL WORLDS', cx, y + 40, '#f43f5e', 'rgba(244, 63, 94, 0.15)', 'rgba(244, 63, 94, 0.4)');
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 28px "Outfit", "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('THE K-SHAPED RECOVERY: WHO IS ACTUALLY PROSPERING?', cx, y + 80);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 15px "Inter", sans-serif';
    ctx.fillText('An economy where the top 15% surges ahead while the bottom 85% faces wage stagnation.', cx, y + 108);

    // K-Trajectory Graphic Center
    const splitX = cx - 240;
    const splitY = cy + 15;
    const armW = 200;
    const animP = Math.min(1, elapsed / 1.2);
    const curArmW = armW * easeOutCubic(animP);

    // Baseline horizontal stem
    ctx.strokeStyle = '#64748b';
    ctx.lineWidth = 4;
    ctx.beginPath();
    ctx.moveTo(splitX - 140, splitY);
    ctx.lineTo(splitX, splitY);
    ctx.stroke();

    // Baseline Node
    ctx.fillStyle = '#38bdf8';
    ctx.beginPath();
    ctx.arc(splitX, splitY, 8, 0, Math.PI * 2);
    ctx.fill();

    // Upper Branch (Booming Top 15%) - Emerald Green Arrow
    const upEndX = splitX + curArmW;
    const upEndY = splitY - 145 * easeOutCubic(animP);
    ctx.strokeStyle = '#10b981';
    ctx.lineWidth = 6;
    ctx.shadowColor = '#10b981';
    ctx.shadowBlur = 16;
    ctx.beginPath();
    ctx.moveTo(splitX, splitY);
    ctx.lineTo(upEndX, upEndY);
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Lower Branch (Struggling Bottom 85%) - Crimson Arrow
    const downEndX = splitX + curArmW;
    const downEndY = splitY + 145 * easeOutCubic(animP);
    ctx.strokeStyle = '#f43f5e';
    ctx.lineWidth = 6;
    ctx.shadowColor = '#f43f5e';
    ctx.shadowBlur = 16;
    ctx.beginPath();
    ctx.moveTo(splitX, splitY);
    ctx.lineTo(downEndX, downEndY);
    ctx.stroke();
    ctx.shadowBlur = 0;

    // Upper Card (Top 10-15%)
    const upCardX = cx + 15;
    const upCardY = y + 145;
    const cW = 540, cH = 150;
    drawGlassCard(ctx, upCardX, upCardY, cW, cH, 14, 'rgba(16, 185, 129, 0.45)', 'rgba(6, 78, 59, 0.2)');
    ctx.fillStyle = '#34d399';
    ctx.font = '800 17px "Inter", sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('▲ UPPER ARM: TOP 10–15% ASSET OWNERS', upCardX + 22, upCardY + 34);
    ctx.fillStyle = '#f8fafc';
    ctx.font = '500 14px "Inter", sans-serif';
    ctx.fillText('• 16+ Crore Demat Accounts (Stock Market Euphoria)', upCardX + 22, upCardY + 66);
    ctx.fillText('• ₹10-Cr Luxury Flats Sell Out in Hours (Gurugram/Mumbai)', upCardX + 22, upCardY + 92);
    ctx.fillText('• Luxury SUV Sales Boom: +24.5% Growth (SIAM Data)', upCardX + 22, upCardY + 118);

    // Lower Card (Bottom 85%)
    const downCardX = cx + 15;
    const downCardY = y + 330;
    drawGlassCard(ctx, downCardX, downCardY, cW, cH, 14, 'rgba(244, 63, 94, 0.45)', 'rgba(136, 19, 55, 0.2)');
    ctx.fillStyle = '#fb7185';
    ctx.font = '800 17px "Inter", sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText('▼ LOWER ARM: BOTTOM 85% GROUND REALITY', downCardX + 22, downCardY + 34);
    ctx.fillStyle = '#f8fafc';
    ctx.font = '500 14px "Inter", sans-serif';
    ctx.fillText('• Entry-Level Small Cars (Alto/WagonR): −42% Sales Drop', downCardX + 22, downCardY + 66);
    ctx.fillText('• Rural 100cc Motorcycles: Still −14% Below 2019 Peak', downCardX + 22, downCardY + 92);
    ctx.fillText('• 80 Crore Citizens (57% Population) on Free PMGKAY Rations', downCardX + 22, downCardY + 118);

    // Bottom Verdict Pill
    const botY = y + 535;
    drawGlassCard(ctx, x + 60, botY, cardW - 120, 56, 12, 'rgba(255, 255, 255, 0.1)', 'rgba(0, 0, 0, 0.6)');
    ctx.fillStyle = '#fbbf24';
    ctx.font = '700 15px "JetBrains Mono", monospace';
    ctx.textAlign = 'center';
    ctx.fillText('KEY EVIDENCE: अमीर और ज़्यादा ख़र्च कर रहे हैं, जबकि आम मिडिल-क्लास की ख़रीद शक्ति सिकुड़ रही है!', cx, botY + 34);

    ctx.restore();
  }

  // -------------------------------------------------------------
  // DIAGRAM 4: Household Debt Crisis Flow (335.95s - 361.60s)
  // -------------------------------------------------------------
  function drawHouseholdDebtCrisisDiagram(ctx, t, start_s = 335.95, end_s = 361.60) {
    if (t < start_s || t >= end_s) return;
    const elapsed = t - start_s;
    const remaining = end_s - t;

    let alpha = 1.0;
    let enterOffset = 0;
    if (elapsed < 0.5) {
      const p = elapsed / 0.5;
      alpha = easeOutCubic(p);
      enterOffset = (1 - easeOutCubic(p)) * 40;
    } else if (remaining < 0.4) {
      alpha = Math.max(0, remaining / 0.4);
    }

    ctx.save();
    ctx.globalAlpha = alpha;

    const cx = 960, cy = 525 + enterOffset;
    const cardW = 1220, cardH = 610;
    const x = cx - cardW/2, y = cy - cardH/2;

    drawGlassCard(ctx, x, y, cardW, cardH, 20, 'rgba(244, 63, 94, 0.4)');

    // Header
    drawBadge(ctx, 'RBI FINANCIAL STABILITY REPORT · SYSTEMIC RISK WARNING', cx, y + 40, '#f43f5e', 'rgba(244, 63, 94, 0.15)', 'rgba(244, 63, 94, 0.4)');
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 28px "Outfit", "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('THE MIDDLE-CLASS BALANCE SHEET DELEVERAGING CRISIS', cx, y + 80);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 15px "Inter", sans-serif';
    ctx.fillText('How living costs and inflation forced Indian families to mortgage tomorrow’s income.', cx, y + 108);

    // 4 Sequential Nodes in Flow
    const nodes = [
      { num: '01', title: 'EXPENSES SPIKE', metric: 'Hospital + Fees', desc: 'Out-of-pocket health costs & education inflation deplete savings', color: '#38bdf8' },
      { num: '02', title: 'SAVINGS CRASH', metric: '5.3% of GDP', desc: 'Net financial savings crash to 50-year historic low (earlier 8–9%)', color: '#fbbf24' },
      { num: '03', title: 'DEBT SURGE', metric: '45.8% of GDP', desc: 'Household debt-to-GDP hits all-time record high in RBI records', color: '#f97316' },
      { num: '04', title: 'UNSECURED EMIs', metric: '58.2% Retail Debt', desc: 'Borrowing not for homes, but personal loans & Buy-Now-Pay-Later', color: '#f43f5e' }
    ];

    const nY = y + 160;
    const nW = 260, nH = 260;
    const nGap = 24;
    const totalW = 4 * nW + 3 * nGap;
    const startX = cx - totalW / 2;

    nodes.forEach((n, idx) => {
      const nx = startX + idx * (nW + nGap);
      const isLit = elapsed >= idx * 0.8;

      ctx.save();
      ctx.globalAlpha = alpha * (isLit ? 1.0 : 0.35);

      drawGlassCard(ctx, nx, nY, nW, nH, 14, isLit ? n.color : 'rgba(255,255,255,0.1)', isLit ? 'rgba(15, 23, 42, 0.85)' : 'rgba(15, 23, 42, 0.35)');

      // Step Number
      ctx.fillStyle = n.color;
      ctx.font = '900 14px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText(`PHASE ${n.num}`, nx + 20, nY + 36);

      // Title
      ctx.fillStyle = '#ffffff';
      ctx.font = '800 19px "Inter", sans-serif';
      ctx.fillText(n.title, nx + 20, nY + 68);

      // Metric Pill
      drawBadge(ctx, n.metric, nx + nW/2, nY + 116, n.color, 'rgba(0,0,0,0.5)', n.color);

      // Description
      ctx.fillStyle = '#94a3b8';
      ctx.font = '400 13px "Inter", sans-serif';
      const words = n.desc.split(' ');
      let line = '', lineY = nY + 165;
      words.forEach(w => {
        if ((line + w).length > 24) {
          ctx.fillText(line, nx + 20, lineY);
          line = w + ' ';
          lineY += 20;
        } else {
          line += w + ' ';
        }
      });
      ctx.fillText(line, nx + 20, lineY);

      // Connecting Arrow to next node
      if (idx < 3) {
        ctx.fillStyle = isLit ? '#38bdf8' : 'rgba(255,255,255,0.2)';
        ctx.font = '900 22px "Inter", sans-serif';
        ctx.textAlign = 'center';
        ctx.fillText('➔', nx + nW + nGap/2, nY + nH/2);
      }

      ctx.restore();
    });

    // Warning Banner at bottom
    const warnY = y + 450;
    drawGlassCard(ctx, x + 40, warnY, cardW - 80, 95, 12, 'rgba(244, 63, 94, 0.4)', 'rgba(76, 5, 25, 0.3)');
    ctx.fillStyle = '#f43f5e';
    ctx.font = '900 16px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText('⚠️ CRITICAL FORENSIC TAKEAWAY:', x + 65, warnY + 36);
    ctx.fillStyle = '#ffffff';
    ctx.font = '500 15px "Inter", sans-serif';
    ctx.fillText('यह इकॉनमिक ग्रोथ नए रोजगार या बढ़ती आय से नहीं, बल्कि उधार लिए गए पैसों (Credit Cards & EMIs) पर चल रही है!', x + 65, warnY + 68);

    ctx.restore();
  }

  // -------------------------------------------------------------
  // DIAGRAM 5: The "Missing Factory" Dynamic Modular System (365.03s - 405.48s)
  // Perfectly synchronized across 5 visual beats with zero screen occlusion!
  // -------------------------------------------------------------
  function drawMissingFactoryDiagram(ctx, t, start_s = 365.03, end_s = 405.48) {
    if (t < start_s || t >= end_s) return;

    // -------------------------------------------------------------------------
    // PHASE 1: [365.03s - 371.44s] Beat 44 (Shenzhen Comparison)
    // "भारत के इकनॉमिक स्ट्रक्चर में एक बहुत बड़ा पिलर ग़ायब है: द मिसिंग फ़ैक्ट्री!"
    // Floating Top-Right Diagnostic Pill (Leaves 75% of photography open)
    // -------------------------------------------------------------------------
    if (t >= 365.03 && t < 371.44) {
      const p1Elapsed = t - 365.03;
      const p1Alpha = Math.min(1.0, p1Elapsed / 0.45);
      const p1Slide = (1 - easeOutCubic(Math.min(1.0, p1Elapsed / 0.5))) * 35;

      ctx.save();
      ctx.globalAlpha = p1Alpha;
      const c1X = 1240 + p1Slide, c1Y = 110, c1W = 580, c1H = 250;
      drawGlassCard(ctx, c1X, c1Y, c1W, c1H, 16, 'rgba(244, 63, 94, 0.45)', 'rgba(10, 15, 26, 0.88)');

      drawBadge(ctx, 'STRUCTURAL DEFICIT · THE MISSING PILLAR', c1X + c1W/2, c1Y + 32, '#f43f5e', 'rgba(244, 63, 94, 0.15)', 'rgba(244, 63, 94, 0.4)');
      ctx.fillStyle = '#ffffff';
      ctx.font = '800 22px "Outfit", "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('THE "MISSING FACTORY" GAP', c1X + 32, c1Y + 76);

      // 2 Metric Pods
      const podW = (c1W - 74) / 2;
      drawGlassCard(ctx, c1X + 30, c1Y + 98, podW, 76, 10, 'rgba(244, 63, 94, 0.4)', 'rgba(244, 63, 94, 0.08)');
      ctx.fillStyle = '#f43f5e';
      ctx.font = '800 20px "JetBrains Mono", monospace';
      ctx.fillText('15.8% GDP', c1X + 44, c1Y + 128);
      ctx.fillStyle = '#94a3b8';
      ctx.font = '500 11.5px "Inter", sans-serif';
      ctx.fillText('India Mfg (Stuck 30 Yrs)', c1X + 44, c1Y + 152);

      drawGlassCard(ctx, c1X + 44 + podW, c1Y + 98, podW, 76, 10, 'rgba(251, 191, 36, 0.4)', 'rgba(251, 191, 36, 0.08)');
      ctx.fillStyle = '#fbbf24';
      ctx.font = '800 20px "JetBrains Mono", monospace';
      ctx.fillText('25.0% TARGET', c1X + 58 + podW, c1Y + 128);
      ctx.fillStyle = '#94a3b8';
      ctx.font = '500 11.5px "Inter", sans-serif';
      ctx.fillText('Make In India Goal (-9.2%)', c1X + 58 + podW, c1Y + 152);

      ctx.fillStyle = '#f8fafc';
      ctx.font = '500 12.5px "Inter", sans-serif';
      ctx.fillText('दुनिया के हर देश ने पहले फैक्ट्रियां बनाईं, भारत ने सीधे छलांग लगाई', c1X + 32, c1Y + 210);
      ctx.restore();
    }

    // -------------------------------------------------------------------------
    // PHASE 2: [371.44s - 380.81s] Beat 45 (Shenzhen Automated Line)
    // "दुनिया के हर बड़े देश ने सबने पहले मास-मैन्युफैक्चरिंग खड़ी की।"
    // Sleek Bottom-Third Horizontal Stream Ribbon (Top 70% of factory robots open!)
    // -------------------------------------------------------------------------
    else if (t >= 371.44 && t < 380.81) {
      const p2Elapsed = t - 371.44;
      const p2Alpha = Math.min(1.0, p2Elapsed / 0.45);
      const p2Slide = (1 - easeOutCubic(Math.min(1.0, p2Elapsed / 0.5))) * 30;

      ctx.save();
      ctx.globalAlpha = p2Alpha;
      const rX = 140, rY = 760 + p2Slide, rW = 1640, rH = 165;
      drawGlassCard(ctx, rX, rY, rW, rH, 16, 'rgba(56, 189, 248, 0.45)', 'rgba(10, 15, 26, 0.90)');

      drawBadge(ctx, 'GLOBAL INDUSTRIAL BLUEPRINT · USA · JAPAN · S. KOREA · CHINA', rX + rW/2, rY + 28, '#38bdf8', 'rgba(56, 189, 248, 0.15)', 'rgba(56, 189, 248, 0.4)');

      // 3 Nodes
      const nodeW = 420;
      // Node 1: Farms
      drawGlassCard(ctx, rX + 40, rY + 54, nodeW, 85, 12, 'rgba(255, 255, 255, 0.12)', 'rgba(255, 255, 255, 0.03)');
      ctx.fillStyle = '#94a3b8';
      ctx.font = '800 13px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('STAGE 1: LOW-INCOME FARMS', rX + 60, rY + 84);
      ctx.fillStyle = '#ffffff';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.fillText('Agriculture (Subsistence Labor)', rX + 60, rY + 112);

      // Flow Arrow 1
      ctx.fillStyle = '#10b981';
      ctx.font = '900 24px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('➔', rX + 40 + nodeW + 40, rY + 104);

      // Node 2: Mass Factories (ACTIVE GLOWING NODE)
      const n2X = rX + 40 + nodeW + 80;
      drawGlassCard(ctx, n2X, rY + 54, nodeW + 40, 85, 12, 'rgba(16, 185, 129, 0.75)', 'rgba(16, 185, 129, 0.12)');
      ctx.fillStyle = '#34d399';
      ctx.font = '800 13px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('STAGE 2: MASS FACTORIES (27% GDP)', n2X + 22, rY + 84);
      ctx.fillStyle = '#ffffff';
      ctx.font = '700 13px "Inter", sans-serif';
      ctx.fillText('Lifts 80 Crore Citizens to Middle Class', n2X + 22, rY + 112);

      // Flow Arrow 2
      ctx.fillStyle = '#38bdf8';
      ctx.font = '900 24px "Inter", sans-serif';
      ctx.textAlign = 'center';
      ctx.fillText('➔', n2X + nodeW + 40 + 40, rY + 104);

      // Node 3: Advanced Tech
      const n3X = n2X + nodeW + 40 + 80;
      drawGlassCard(ctx, n3X, rY + 54, nodeW, 85, 12, 'rgba(255, 255, 255, 0.12)', 'rgba(255, 255, 255, 0.03)');
      ctx.fillStyle = '#38bdf8';
      ctx.font = '800 13px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('STAGE 3: HIGH-TECH & SERVICES', n3X + 22, rY + 84);
      ctx.fillStyle = '#ffffff';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.fillText('Mature Wealthy Superpower', n3X + 22, rY + 112);

      ctx.restore();
    }

    // -------------------------------------------------------------------------
    // PHASE 3: [380.81s - 388.40s] Beat 46 (Textile Mill - THE SCREENSHOT!)
    // "खेत में काम करने वाले करोड़ों लोगों को कपड़ा और इलेक्ट्रॉनिक्स में जॉब्स मिलीं।"
    // Sleek Asymmetric Right Floating HUD (Leaves 75% of textile floor visible!)
    // -------------------------------------------------------------------------
    else if (t >= 380.81 && t < 388.40) {
      const p3Elapsed = t - 380.81;
      const p3Alpha = Math.min(1.0, p3Elapsed / 0.45);
      const p3Slide = (1 - easeOutCubic(Math.min(1.0, p3Elapsed / 0.5))) * 35;

      ctx.save();
      ctx.globalAlpha = p3Alpha;
      const c3X = 1260 + p3Slide, c3Y = 110, c3W = 560, c3H = 490;
      drawGlassCard(ctx, c3X, c3Y, c3W, c3H, 18, 'rgba(16, 185, 129, 0.45)', 'rgba(8, 14, 24, 0.90)');

      drawBadge(ctx, 'LABOR ABSORPTION ENGINE · REALITY', c3X + c3W/2, c3Y + 34, '#34d399', 'rgba(16, 185, 129, 0.15)', 'rgba(16, 185, 129, 0.4)');
      ctx.fillStyle = '#ffffff';
      ctx.font = '800 24px "Outfit", "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('MASS TEXTILES & FACTORIES', c3X + 32, c3Y + 80);
      ctx.fillStyle = '#94a3b8';
      ctx.font = '500 13px "Inter", sans-serif';
      ctx.fillText('Why China & Vietnam Absorb Farm Workers', c3X + 32, c3Y + 106);

      // Card 1: Job Density
      drawGlassCard(ctx, c3X + 28, c3Y + 130, c3W - 56, 120, 12, 'rgba(16, 185, 129, 0.35)', 'rgba(16, 185, 129, 0.06)');
      ctx.fillStyle = '#34d399';
      ctx.font = '800 13px "JetBrains Mono", monospace';
      ctx.fillText('HIGH-DENSITY JOB CREATION:', c3X + 48, c3Y + 158);
      ctx.fillStyle = '#ffffff';
      ctx.font = '900 28px "JetBrains Mono", monospace';
      ctx.fillText('250 JOBS', c3X + 48, c3Y + 196);
      ctx.fillStyle = '#94a3b8';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.fillText('Per ₹1 Crore Capex (vs only 1.2 in IT)', c3X + 48, c3Y + 226);

      // Card 2: No Degree Needed
      drawGlassCard(ctx, c3X + 28, c3Y + 266, c3W - 56, 110, 12, 'rgba(56, 189, 248, 0.35)', 'rgba(56, 189, 248, 0.06)');
      ctx.fillStyle = '#38bdf8';
      ctx.font = '800 13px "JetBrains Mono", monospace';
      ctx.fillText('EDUCATION BOUNDARY:', c3X + 48, c3Y + 294);
      ctx.fillStyle = '#ffffff';
      ctx.font = '700 15px "Inter", sans-serif';
      ctx.fillText('Zero Degree Barrier for Farm Youth', c3X + 48, c3Y + 322);
      ctx.fillStyle = '#cbd5e1';
      ctx.font = '500 12.5px "Inter", sans-serif';
      ctx.fillText('Immediate transition to monthly bank salary', c3X + 48, c3Y + 348);

      // Bottom Takeaway
      ctx.fillStyle = '#fbbf24';
      ctx.font = '600 12.5px "Inter", sans-serif';
      ctx.fillText('बिना मास-फ़ैक्ट्रियों के 45% ग्रामीण आबादी को नौकरी नामुमकिन है!', c3X + 32, c3Y + 418);
      ctx.fillStyle = '#64748b';
      ctx.font = '400 11.5px "Inter", sans-serif';
      ctx.fillText('Source: Annual Survey of Industries & World Bank Mfg Study', c3X + 32, c3Y + 444);

      ctx.restore();
    }

    // -------------------------------------------------------------------------
    // PHASE 4: [388.40s - 397.18s] Beat 47 (Samsung / Vietnam Complex)
    // "चीन की जीडीपी में मैन्युफैक्चरिंग 27% है, जिससे 80 करोड़ लोग ग़रीबी से निकले।"
    // Comparative Battle Bar Gauge (Left Side, 70% of factory complex open)
    // -------------------------------------------------------------------------
    else if (t >= 388.40 && t < 397.18) {
      const p4Elapsed = t - 388.40;
      const p4Alpha = Math.min(1.0, p4Elapsed / 0.45);
      const p4Slide = (1 - easeOutCubic(Math.min(1.0, p4Elapsed / 0.5))) * 35;
      const barFill = easeOutCubic(Math.min(1.0, p4Elapsed / 1.5));

      ctx.save();
      ctx.globalAlpha = p4Alpha;
      const c4X = 100 - p4Slide, c4Y = 120, c4W = 680, c4H = 430;
      drawGlassCard(ctx, c4X, c4Y, c4W, c4H, 18, 'rgba(56, 189, 248, 0.45)', 'rgba(8, 14, 24, 0.90)');

      drawBadge(ctx, 'MANUFACTURING SHARE OF GDP · THE ENGINE', c4X + c4W/2, c4Y + 34, '#38bdf8', 'rgba(56, 189, 248, 0.15)', 'rgba(56, 189, 248, 0.4)');
      ctx.fillStyle = '#ffffff';
      ctx.font = '800 24px "Outfit", "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('CHINA 27% vs INDIA 15.8%', c4X + 34, c4Y + 80);

      // China Bar
      ctx.fillStyle = '#34d399';
      ctx.font = '800 14px "JetBrains Mono", monospace';
      ctx.fillText('CHINA: 27.4% GDP SHARE (80 CR LIFTED)', c4X + 34, c4Y + 124);
      // Background track
      ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
      ctx.beginPath();
      ctx.roundRect(c4X + 34, c4Y + 138, 600, 26, 6);
      ctx.fill();
      // Filled bar
      const cnBarW = 600 * (27.4 / 30.0) * barFill;
      ctx.fillStyle = '#10b981';
      ctx.beginPath();
      ctx.roundRect(c4X + 34, c4Y + 138, cnBarW, 26, 6);
      ctx.fill();

      // India Bar
      ctx.fillStyle = '#f43f5e';
      ctx.font = '800 14px "JetBrains Mono", monospace';
      ctx.fillText('INDIA: 15.8% GDP SHARE (STAGNANT 30 YRS)', c4X + 34, c4Y + 204);
      ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
      ctx.beginPath();
      ctx.roundRect(c4X + 34, c4Y + 218, 600, 26, 6);
      ctx.fill();
      const inBarW = 600 * (15.8 / 30.0) * barFill;
      ctx.fillStyle = '#ef4444';
      ctx.beginPath();
      ctx.roundRect(c4X + 34, c4Y + 218, inBarW, 26, 6);
      ctx.fill();

      // Deficit Marker
      const defX = c4X + 34 + inBarW;
      const defW = (600 * (25.0 / 30.0)) - (600 * (15.8 / 30.0));
      ctx.strokeStyle = '#fbbf24';
      ctx.setLineDash([5, 4]);
      ctx.lineWidth = 1.5;
      ctx.strokeRect(defX, c4Y + 218, defW * barFill, 26);
      ctx.setLineDash([]);

      ctx.fillStyle = '#fbbf24';
      ctx.font = '700 12px "JetBrains Mono", monospace';
      ctx.fillText('▲ -9.2% DEFICIT GAP TO MAKE IN INDIA TARGET (25%)', c4X + 34, c4Y + 270);

      // Bottom Fact Box
      drawGlassCard(ctx, c4X + 34, c4Y + 296, 600, 94, 10, 'rgba(255, 255, 255, 0.1)', 'rgba(255, 255, 255, 0.03)');
      ctx.fillStyle = '#f8fafc';
      ctx.font = '600 13.5px "Inter", sans-serif';
      ctx.fillText('चीन ने 80 करोड़ लोगों को आईटी या स्टॉक मार्केट से नहीं,', c4X + 54, c4Y + 332);
      ctx.fillStyle = '#34d399';
      ctx.font = '700 13.5px "Inter", sans-serif';
      ctx.fillText('बल्कि दुनिया की फ़ैक्ट्री बनकर ग़रीबी से बाहर निकाला!', c4X + 54, c4Y + 360);

      ctx.restore();
    }

    // -------------------------------------------------------------------------
    // PHASE 5: [397.18s - 405.48s] Beat 48 (Bengaluru IT Tech Park)
    // "हमने एग्रीकल्चर से सीधे आईटी और सॉफ़्टवेयर पर छलांग लगा दी।"
    // India's Premature Jump: The Fractured Bridge HUD (Left Side)
    // -------------------------------------------------------------------------
    else if (t >= 397.18 && t < 405.48) {
      const p5Elapsed = t - 397.18;
      const p5Alpha = Math.min(1.0, p5Elapsed / 0.45);
      const p5Slide = (1 - easeOutCubic(Math.min(1.0, p5Elapsed / 0.5))) * 35;

      ctx.save();
      ctx.globalAlpha = p5Alpha;
      const c5X = 100 - p5Slide, c5Y = 120, c5W = 620, c5H = 460;
      drawGlassCard(ctx, c5X, c5Y, c5W, c5H, 18, 'rgba(244, 63, 94, 0.45)', 'rgba(8, 14, 24, 0.90)');

      drawBadge(ctx, 'THE PREMATURE JUMP · STRUCTURAL CHASM', c5X + c5W/2, c5Y + 34, '#f43f5e', 'rgba(244, 63, 94, 0.15)', 'rgba(244, 63, 94, 0.4)');
      ctx.fillStyle = '#ffffff';
      ctx.font = '800 24px "Outfit", "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText('DIRECT JUMP TO SERVICES', c5X + 32, c5Y + 80);

      // Box 1: Farms (45.4%)
      drawGlassCard(ctx, c5X + 28, c5Y + 104, c5W - 56, 76, 10, 'rgba(255, 255, 255, 0.12)', 'rgba(255, 255, 255, 0.03)');
      ctx.fillStyle = '#94a3b8';
      ctx.font = '800 12px "JetBrains Mono", monospace';
      ctx.fillText('STAGE 1: AGRICULTURE', c5X + 44, c5Y + 130);
      ctx.fillStyle = '#ffffff';
      ctx.font = '700 15px "Inter", sans-serif';
      ctx.fillText('45.4% Workforce (Contributes only 15% GDP)', c5X + 44, c5Y + 158);

      // Fractured Bridge Notice
      ctx.fillStyle = '#f43f5e';
      ctx.font = '900 14px "JetBrains Mono", monospace';
      ctx.textAlign = 'center';
      ctx.fillText('⚡ SKIPPED STAGE 2: MASS FACTORIES (STUCK AT 15.8%) ⚡', c5X + c5W/2, c5Y + 208);

      // Box 2: IT & Services
      drawGlassCard(ctx, c5X + 28, c5Y + 226, c5W - 56, 110, 10, 'rgba(56, 189, 248, 0.35)', 'rgba(56, 189, 248, 0.06)');
      ctx.textAlign = 'left';
      ctx.fillStyle = '#38bdf8';
      ctx.font = '800 12px "JetBrains Mono", monospace';
      ctx.fillText('PREMATURE JUMP: IT & HIGH SERVICES (+12.1%)', c5X + 44, c5Y + 254);
      ctx.fillStyle = '#ffffff';
      ctx.font = '900 22px "JetBrains Mono", monospace';
      ctx.fillText('EMPLOYS < 5% WORKFORCE', c5X + 44, c5Y + 288);
      ctx.fillStyle = '#94a3b8';
      ctx.font = '500 12px "Inter", sans-serif';
      ctx.fillText('Requires fluent English & Coding degrees', c5X + 44, c5Y + 316);

      // Warning Verdict
      ctx.fillStyle = '#fbbf24';
      ctx.font = '600 13px "Inter", sans-serif';
      ctx.fillText('आईटी सेक्टर 60 करोड़ ग्रामीण युवाओं को नौकरी नहीं दे सकता!', c5X + 32, c5Y + 382);
      ctx.fillStyle = '#94a3b8';
      ctx.font = '400 12px "Inter", sans-serif';
      ctx.fillText('यही कारण है कि 7.8% GDP ग्रोथ के बावजूद ग्राउंड पर जॉब्स ग़ायब हैं।', c5X + 32, c5Y + 412);

      ctx.restore();
    }
  }

  // -------------------------------------------------------------
  // DIAGRAM 6: The 2045 Demographic Clock (500.18s - 525.70s)
  // Implemented using the Progressive Infographic Motion System:
  // Phase 01: Headline in center with LIVE tag
  // Phase 02: Headline travels smoothly to top anchor
  // Phase 03: Left context card enters (Cyan #38bdf8) with LIVE badge
  // Phase 04: Central orange clock arc draws clockwise live with travelling head
  // Phase 04b: Hero year 2045 and window labels reveal
  // Phase 05: Right risk card enters (Crimson #f43f5e) with LIVE badge
  // Phase 06: Final holding state with pulsing data packets and warning banner
  // -------------------------------------------------------------
  function drawDemographicClockDiagram(ctx, t, start_s = 500.18, end_s = 525.70) {
    if (t < start_s || t >= end_s) return;
    const elapsed = t - start_s;
    const remaining = end_s - t;

    // Helper: Draw signature glowing LIVE badge from progressive motion skill
    function drawLiveBadge(bx, by, color, badgeAlpha = 1.0, label = "LIVE") {
      if (badgeAlpha <= 0.01) return;
      ctx.save();
      ctx.globalAlpha = ctx.globalAlpha * badgeAlpha;
      ctx.font = '800 11px "JetBrains Mono", monospace';
      const tw = ctx.measureText(label).width;
      const bw = tw + 34;
      const bh = 22;

      ctx.fillStyle = 'rgba(5, 12, 22, 0.88)';
      ctx.strokeStyle = color;
      ctx.lineWidth = 1.2;
      ctx.shadowColor = color;
      ctx.shadowBlur = 8;
      ctx.beginPath();
      ctx.roundRect(bx, by, bw, bh, 11);
      ctx.fill();
      ctx.stroke();
      ctx.shadowBlur = 0;

      // Pulsing dot
      const dotPulse = 0.7 + 0.3 * Math.sin(t * 8);
      ctx.fillStyle = color;
      ctx.beginPath();
      ctx.arc(bx + 11, by + bh / 2, 3.2 * dotPulse, 0, Math.PI * 2);
      ctx.fill();

      ctx.fillStyle = '#ffffff';
      ctx.textAlign = 'left';
      ctx.fillText(label, bx + 20, by + 15);
      ctx.restore();
    }

    // Helper: Draw data connection line with travelling glowing packet
    function drawDataConnection(x1, x2, yPos, color, phaseP, connAlpha) {
      if (connAlpha <= 0.01) return;
      ctx.save();
      ctx.globalAlpha = ctx.globalAlpha * connAlpha;
      ctx.strokeStyle = color;
      ctx.lineWidth = 1.5;
      ctx.setLineDash([4, 4]);
      ctx.beginPath();
      ctx.moveTo(x1, yPos);
      ctx.lineTo(x2, yPos);
      ctx.stroke();
      ctx.setLineDash([]);

      // Travelling packet
      const packetX = x1 + (x2 - x1) * (phaseP % 1);
      ctx.fillStyle = '#ffffff';
      ctx.shadowColor = color;
      ctx.shadowBlur = 10;
      ctx.beginPath();
      ctx.arc(packetX, yPos, 4, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
    }

    // Master alpha with smooth entry & exit
    let masterAlpha = 1.0;
    if (elapsed < 0.3) masterAlpha = elapsed / 0.3;
    else if (remaining < 0.4) masterAlpha = Math.max(0, remaining / 0.4);

    ctx.save();
    ctx.globalAlpha = masterAlpha;

    // Relative progressive phase progress
    // Phase 1 (0.0s - 2.5s): Headline Center
    // Phase 2 (2.5s - 4.8s): Headline Move to Top
    // Phase 3 (4.8s - 8.5s): Left Card Enter
    // Phase 4 (8.5s - 14.5s): Clock Draw Live
    // Phase 5 (14.5s - 18.5s): Right Card Enter
    // Phase 6 (18.5s - 25.5s): Full Connected Dashboard Hold

    const headerIn = Math.min(1, elapsed / 0.6);
    const headerMove = elapsed > 2.5 ? Math.min(1, (elapsed - 2.5) / 1.6) : 0;
    const headerEasedMove = 1 - Math.pow(1 - headerMove, 3); // outCubic

    // Header position: Center (cy = 500) -> Top Anchor (cy = 120)
    const headerCX = 960;
    const headerCY = 500 - headerEasedMove * 380;
    const headerScale = 1.10 - headerEasedMove * 0.15;

    // --- PHASE 01 & 02: HEADLINE PANEL ---
    ctx.save();
    ctx.translate(headerCX, headerCY);
    ctx.scale(headerScale, headerScale);
    ctx.globalAlpha = masterAlpha * headerIn;

    drawBadge(ctx, 'ACTUARIAL DEMOGRAPHIC RISK · NFHS PROJECTIONS', 0, -32, '#fb923c', 'rgba(251, 146, 60, 0.15)', 'rgba(251, 146, 60, 0.4)');
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 28px "Outfit", "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('THE 2045 DEMOGRAPHIC CLOCK: RACE AGAINST TIME', 0, 8);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 14px "Inter", sans-serif';
    ctx.fillText('India has only 19 years before its demographic dividend window permanently shuts.', 0, 36);

    // Live tag for header
    if (elapsed < 2.5) {
      drawLiveBadge(240, -42, '#fb923c', headerIn, 'LIVE');
    } else {
      drawLiveBadge(360, -42, '#fb923c', 0.85, 'LIVE');
    }
    ctx.restore();

    // Baseline horizontal divider guide rule wipes out once header reaches top
    if (headerEasedMove > 0.3) {
      const guideAlpha = Math.min(1, (headerEasedMove - 0.3) / 0.7);
      ctx.save();
      ctx.strokeStyle = 'rgba(73, 116, 147, 0.35)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(960 - 600 * guideAlpha, 185);
      ctx.lineTo(960 + 600 * guideAlpha, 185);
      ctx.stroke();
      ctx.restore();
    }

    // --- PHASE 03: LEFT DEMOGRAPHIC CONTEXT CARD (Enters at 4.8s) ---
    const cardY = 220;
    const cardH = 390;
    const cardW = 350;

    if (elapsed >= 4.5) {
      const leftP = Math.min(1, (elapsed - 4.5) / 1.1);
      // Friendly pop-in overshoot
      const c1 = 1.70158, c3 = 2.70158;
      const leftOvershoot = 1 + c3 * Math.pow(leftP - 1, 3) + c1 * Math.pow(leftP - 1, 2);
      const leftScale = 0.82 + 0.18 * Math.min(1, leftOvershoot);
      const leftFinalX = 140;
      const leftX = 420 + (leftFinalX - 420) * leftOvershoot;
      const leftFloat = elapsed > 5.8 ? Math.sin(t * 1.8) * 2 : 0;

      ctx.save();
      ctx.globalAlpha = masterAlpha * Math.min(1, (elapsed - 4.5) / 0.5);
      drawGlassCard(ctx, leftX, cardY + leftFloat, cardW, cardH, 16, 'rgba(56, 189, 248, 0.40)');

      // Live tag
      drawLiveBadge(leftX + cardW - 88, cardY + leftFloat - 14, '#38bdf8', 0.95, 'LIVE');

      ctx.fillStyle = '#38bdf8';
      ctx.font = '800 15px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('TODAY (2026 STATUS)', leftX + 24, cardY + leftFloat + 42);

      ctx.fillStyle = '#ffffff';
      ctx.font = '800 22px "Inter", sans-serif';
      ctx.fillText('Median Age: 28.4 Yrs', leftX + 24, cardY + leftFloat + 78);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '400 14px "Inter", sans-serif';
      const bulletY = cardY + leftFloat + 124;
      ctx.fillText('• 1.1 Crore Youth Enter Jobs/Yr', leftX + 24, bulletY);
      ctx.fillText('• Youngest workforce on Earth', leftX + 24, bulletY + 28);
      ctx.fillText('• Fertility Rate: 2.0 (NFHS-5)', leftX + 24, bulletY + 56);
      ctx.fillText('• Replacement level broken', leftX + 24, bulletY + 84);
      ctx.fillText('• South states already aging', leftX + 24, bulletY + 112);
      ctx.fillText('• Dependency ratio rising', leftX + 24, bulletY + 140);

      ctx.restore();
    }

    // --- PHASE 04: CENTRAL CLOCK ARC DRAWN LIVE (Enters at 8.0s) ---
    const clockCX = 960;
    const clockCY = 415;
    const clockR = 120;

    if (elapsed >= 8.0) {
      const clockIn = Math.min(1, (elapsed - 8.0) / 0.8);
      const ringP = Math.min(1, (elapsed - 8.0) / 4.8);
      const ringEased = 1 - Math.pow(1 - ringP, 3);
      const sweepEnd = -Math.PI / 2 + (Math.PI * 2 * 0.72) * ringEased;

      ctx.save();
      ctx.globalAlpha = masterAlpha * clockIn;

      // Clock frosted circular backing
      ctx.fillStyle = 'rgba(10, 15, 26, 0.40)';
      ctx.beginPath();
      ctx.arc(clockCX, clockCY, clockR + 32, 0, Math.PI * 2);
      ctx.fill();

      // Outer track circle
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
      ctx.lineWidth = 14;
      ctx.beginPath();
      ctx.arc(clockCX, clockCY, clockR, 0, Math.PI * 2);
      ctx.stroke();

      // Primary dual-band drawn orange arc
      if (ringEased > 0.02) {
        // Soft volumetric glow under arc
        ctx.strokeStyle = 'rgba(255, 105, 34, 0.4)';
        ctx.shadowColor = 'rgba(255, 132, 39, 0.8)';
        ctx.shadowBlur = 22;
        ctx.lineWidth = 16;
        ctx.lineCap = 'round';
        ctx.beginPath();
        ctx.arc(clockCX, clockCY, clockR, -Math.PI / 2, sweepEnd);
        ctx.stroke();

        // Sharp rich orange stroke
        ctx.strokeStyle = '#ff6922';
        ctx.shadowBlur = 0;
        ctx.lineWidth = 13;
        ctx.beginPath();
        ctx.arc(clockCX, clockCY, clockR, -Math.PI / 2, sweepEnd);
        ctx.stroke();

        // Inner gold accent thread
        ctx.strokeStyle = '#ffbe48';
        ctx.lineWidth = 4;
        ctx.beginPath();
        ctx.arc(clockCX, clockCY, clockR - 2, -Math.PI / 2, sweepEnd);
        ctx.stroke();
        ctx.lineCap = 'butt';

        // Glowing travelling node at the head of the arc
        const headX = clockCX + clockR * Math.cos(sweepEnd);
        const headY = clockCY + clockR * Math.sin(sweepEnd);
        ctx.fillStyle = '#ffbe48';
        ctx.shadowColor = '#ffbe48';
        ctx.shadowBlur = 14;
        ctx.beginPath();
        ctx.arc(headX, headY, 6.5, 0, Math.PI * 2);
        ctx.fill();
        ctx.shadowBlur = 0;
      }

      // Phase 04b: Hero Center Year & Countdown Labels (Reveals after ring is underway)
      if (elapsed >= 11.5) {
        const textIn = Math.min(1, (elapsed - 11.5) / 0.8);
        ctx.save();
        ctx.globalAlpha = masterAlpha * textIn;
        const textFloat = Math.sin(t * 1.5) * 1.8;

        ctx.fillStyle = '#ffffff';
        ctx.font = '900 38px "JetBrains Mono", monospace';
        ctx.textAlign = 'center';
        ctx.fillText('2045', clockCX, clockCY - 6 + textFloat);

        ctx.fillStyle = '#ff862e';
        ctx.font = '800 13px "JetBrains Mono", monospace';
        ctx.fillText('WINDOW CLOSES', clockCX, clockCY + 26 + textFloat);

        ctx.fillStyle = '#94a3b8';
        ctx.font = '500 12px "Inter", sans-serif';
        ctx.fillText('~19 Years Remaining', clockCX, clockCY + 48 + textFloat);
        ctx.restore();
      }

      // Center Live Badge
      drawLiveBadge(clockCX - 40, clockCY + clockR + 10, '#ff862e', clockIn, 'LIVE');
      ctx.restore();
    }

    // --- PHASE 05: RIGHT CONSEQUENCE CARD (Enters at 14.5s) ---
    if (elapsed >= 14.5) {
      const rightP = Math.min(1, (elapsed - 14.5) / 1.1);
      const c1 = 1.70158, c3 = 2.70158;
      const rightOvershoot = 1 + c3 * Math.pow(rightP - 1, 3) + c1 * Math.pow(rightP - 1, 2);
      const rightFinalX = 1430;
      const rightX = 1150 + (rightFinalX - 1150) * rightOvershoot;
      const rightFloat = elapsed > 15.8 ? Math.sin(t * 1.7 + 1.2) * 2 : 0;

      ctx.save();
      ctx.globalAlpha = masterAlpha * Math.min(1, (elapsed - 14.5) / 0.5);
      drawGlassCard(ctx, rightX, cardY + rightFloat, cardW, cardH, 16, 'rgba(244, 63, 94, 0.45)');

      // Live tag
      drawLiveBadge(rightX + cardW - 88, cardY + rightFloat - 14, '#f43f5e', 0.95, 'LIVE');

      ctx.fillStyle = '#f43f5e';
      ctx.font = '800 15px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText('THE MIDDLE-INCOME TRAP', rightX + 24, cardY + rightFloat + 42);

      ctx.fillStyle = '#ffffff';
      ctx.font = '800 22px "Inter", sans-serif';
      ctx.fillText('Target: $10,000 / Cap', rightX + 24, cardY + rightFloat + 78);

      ctx.fillStyle = '#94a3b8';
      ctx.font = '400 14px "Inter", sans-serif';
      const bulletY = cardY + rightFloat + 124;
      ctx.fillText('• Must reach $10k before 2045', rightX + 24, bulletY);
      ctx.fillText('• Current: $2,730 (Need 4x leap)', rightX + 24, bulletY + 28);
      ctx.fillText('• Without mass formal pensions', rightX + 24, bulletY + 56);
      ctx.fillText('• Without universal healthcare', rightX + 24, bulletY + 84);
      ctx.fillText('• Brazil/Thailand stagnation risk', rightX + 24, bulletY + 112);
      ctx.fillText('• Old age poverty trap', rightX + 24, bulletY + 140);

      ctx.restore();
    }

    // --- PHASE 06: DATA STREAM CONNECTIONS & WARNING BANNER (18.5s to 25.5s) ---
    if (elapsed >= 18.0) {
      const finalIn = Math.min(1, (elapsed - 18.0) / 0.8);

      // Data connection from Left card to Clock
      drawDataConnection(490, 840, 415, '#38bdf8', t * 0.6, finalIn);
      // Data connection from Clock to Right card
      drawDataConnection(1080, 1430, 415, '#f43f5e', t * 0.6 + 0.5, finalIn);

      // Bottom Warning Banner
      const botY = 635;
      const botW = 1260;
      const botX = 960 - botW / 2;

      ctx.save();
      ctx.globalAlpha = masterAlpha * finalIn;
      drawGlassCard(ctx, botX, botY, botW, 64, 12, 'rgba(251, 191, 36, 0.40)');

      ctx.fillStyle = '#fbbf24';
      ctx.font = '700 15.5px "JetBrains Mono", monospace';
      ctx.textAlign = 'center';
      ctx.fillText('⚠️ अगर अगले 18 सालों में पर-कैपिटा इनकम नहीं बढ़ी, तो भारत अमीर बनने से पहले बूढ़ा हो जाएगा!', 960, botY + 38);

      // Footer System Live Tracker
      ctx.fillStyle = '#64748b';
      ctx.font = '600 12px "JetBrains Mono", monospace';
      ctx.fillText('SYSTEM LIVE · DEMOGRAPHIC WINDOW ACTUARIAL MODEL (2026–2045)', 960, botY + 82);

      ctx.restore();
    }

    ctx.restore();
  }

  // -------------------------------------------------------------
  // DIAGRAM 7: The 4 Reform Pillars Blueprint (532.37s - 572.61s)
  // -------------------------------------------------------------
  function drawFourPillarsBlueprintDiagram(ctx, t, start_s = 532.37, end_s = 572.61) {
    if (t < start_s || t >= end_s) return;
    const elapsed = t - start_s;
    const remaining = end_s - t;

    let alpha = 1.0;
    let enterOffset = 0;
    if (elapsed < 0.5) {
      const p = elapsed / 0.5;
      alpha = easeOutCubic(p);
      enterOffset = (1 - easeOutCubic(p)) * 40;
    } else if (remaining < 0.4) {
      alpha = Math.max(0, remaining / 0.4);
    }

    ctx.save();
    ctx.globalAlpha = alpha;

    const cx = 960, cy = 525 + enterOffset;
    const cardW = 1260, cardH = 620;
    const x = cx - cardW/2, y = cy - cardH/2;

    drawGlassCard(ctx, x, y, cardW, cardH, 20, 'rgba(56, 189, 248, 0.4)');

    // Header
    drawBadge(ctx, 'STRATEGIC ARCHITECTURE · ACTIONABLE POLICY ROADMAP', cx, y + 40, '#10b981', 'rgba(16, 185, 129, 0.15)', 'rgba(16, 185, 129, 0.4)');
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 28px "Outfit", "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('THE 4 REFORM PILLARS: HOW INDIA TURNS GDP INTO GROUND REALITY', cx, y + 80);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 15px "Inter", sans-serif';
    ctx.fillText('Concrete structural reforms to transform headline numbers into family prosperity.', cx, y + 108);

    // 4 Architectural Pillars
    const pillars = [
      {
        id: 1,
        title: 'MASS FACTORIES',
        hi: 'लेबर-इंटेंसिव फ़ैक्ट्रीज़',
        activeAt: 532.37,
        bullets: ['Garments, footwear & agro-processing', 'Slash factory red-tape & plug-and-play parks', 'Absorb millions exiting farm distress'],
        color: '#38bdf8'
      },
      {
        id: 2,
        title: 'TAX RELIEF',
        hi: 'मिडिल क्लास बचत सुरक्षा',
        activeAt: 547.20,
        bullets: ['Abolish 18% GST on Health Insurance', 'Rationalize middle-class income slabs', 'Rebuild family net financial savings'],
        color: '#fbbf24'
      },
      {
        id: 3,
        title: 'AGRI COLD-CHAINS',
        hi: 'ग्रामीण वैल्यू-ऐड नेटवर्क',
        activeAt: 556.37,
        bullets: ['Solar cold-storages in every rural cluster', 'Direct food processing near farm gates', 'Farmer income beyond perishable mandi sales'],
        color: '#10b981'
      },
      {
        id: 4,
        title: 'VOCATIONAL SKILLS',
        hi: 'डायरेक्ट इंडस्ट्रियल स्किलिंग',
        activeAt: 566.22,
        bullets: ['Replace paper degrees with paid apprenticeships', 'ITI robotics, EV & CNC machining labs', 'Guaranteed industry job placement pathways'],
        color: '#a855f7'
      }
    ];

    const pY = y + 145;
    const pW = 275, pH = 370;
    const pGap = 20;
    const startX = cx - (4 * pW + 3 * pGap) / 2;

    pillars.forEach((p, idx) => {
      const px = startX + idx * (pW + pGap);
      const isCurrent = t >= p.activeAt;
      const isNext = (idx < 3 && t >= pillars[idx + 1].activeAt);

      // Lift animation when active
      const liftY = isCurrent && !isNext ? -12 : 0;

      ctx.save();
      ctx.globalAlpha = alpha * (isCurrent ? 1.0 : 0.4);

      drawGlassCard(ctx, px, pY + liftY, pW, pH, 16, isCurrent ? p.color : 'rgba(255,255,255,0.1)', isCurrent ? 'rgba(15, 23, 42, 0.88)' : 'rgba(15, 23, 42, 0.4)');

      // Pillar Number Top Plinth
      ctx.fillStyle = p.color;
      ctx.font = '900 14px "JetBrains Mono", monospace';
      ctx.textAlign = 'left';
      ctx.fillText(`PILLAR 0${p.id}`, px + 22, pY + liftY + 36);

      // Main Title
      ctx.fillStyle = '#ffffff';
      ctx.font = '800 20px "Inter", sans-serif';
      ctx.fillText(p.title, px + 22, pY + liftY + 68);

      // Hindi subtitle pill
      drawBadge(ctx, p.hi, px + pW/2, pY + liftY + 105, p.color, 'rgba(0,0,0,0.4)', p.color);

      // Bullets
      ctx.fillStyle = '#e2e8f0';
      ctx.font = '400 13.5px "Inter", sans-serif';
      let bY = pY + liftY + 155;
      p.bullets.forEach(b => {
        ctx.fillText(`• ${b}`, px + 20, bY);
        bY += 46;
      });

      // Bottom Status Indicator
      if (isCurrent && !isNext) {
        ctx.fillStyle = p.color;
        ctx.shadowColor = p.color;
        ctx.shadowBlur = 12;
        ctx.font = '800 13px "JetBrains Mono", monospace';
        ctx.textAlign = 'center';
        ctx.fillText('▶ ACTIVE POLICY FOCUS', px + pW/2, pY + liftY + pH - 24);
        ctx.shadowBlur = 0;
      }

      ctx.restore();
    });

    // Bottom Conclusion Pill
    const botY = y + 540;
    drawGlassCard(ctx, x + 40, botY, cardW - 80, 52, 12, 'rgba(255, 255, 255, 0.1)', 'rgba(0, 0, 0, 0.6)');
    ctx.fillStyle = '#38bdf8';
    ctx.font = '700 14.5px "JetBrains Mono", monospace';
    ctx.textAlign = 'center';
    ctx.fillText('मंज़िल 7.8% का हेडलाइन नंबर नहीं, बल्कि भारत को ग्लोबल पर-कैपिटा टॉप 50 में पहुंचाना है!', cx, botY + 32);

    ctx.restore();
  }

  // Export to window
  root.Diagrams = {
    drawGdpGvaDiagram,
    drawPerCapitaComparisonDiagram,
    drawKShapedDivergenceDiagram,
    drawHouseholdDebtCrisisDiagram,
    drawMissingFactoryDiagram,
    drawDemographicClockDiagram,
    drawFourPillarsBlueprintDiagram
  };

})(typeof window !== 'undefined' ? window : globalThis);
