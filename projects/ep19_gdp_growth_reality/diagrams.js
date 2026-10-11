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

    // Translucent spatial frosted glass that keeps background image vividly visible
    if (!bgColor || bgColor === 'rgba(8, 13, 24, 0.90)' || bgColor === 'rgba(8, 13, 24, 0.88)') {
      const glassGrad = ctx.createLinearGradient(x, y, x, y + h);
      glassGrad.addColorStop(0, 'rgba(8, 13, 24, 0.48)');
      glassGrad.addColorStop(1, 'rgba(5, 8, 16, 0.36)');
      ctx.fillStyle = glassGrad;
    } else {
      ctx.fillStyle = bgColor;
    }

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
  // -------------------------------------------------------------
  function drawGdpGvaDiagram(ctx, t, start_s = 64.29, end_s = 83.45) {
    if (t < start_s || t >= end_s) return;
    const dur = end_s - start_s;
    const elapsed = t - start_s;
    const remaining = end_s - t;

    // Spring entrance & exit fade
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

    const cx = 960, cy = 530 + enterOffset;
    const cardW = 1180, cardH = 580;
    const x = cx - cardW/2, y = cy - cardH/2;

    drawGlassCard(ctx, x, y, cardW, cardH, 20, 'rgba(56, 189, 248, 0.4)');

    // Header Tag & Title
    drawBadge(ctx, 'OFFICIAL DATA DISSECTION · MoSPI Q1 NATIONAL ACCOUNTS', cx, y + 42, '#38bdf8', 'rgba(56, 189, 248, 0.15)', 'rgba(56, 189, 248, 0.4)');
    
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 28px "Outfit", "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('THE GDP vs GVA WEDGE: WHAT HEADLINE 7.8% MASKS', cx, y + 84);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 15px "Inter", sans-serif';
    ctx.fillText('Gross Domestic Product = Gross Value Added + Net Indirect Taxes (Taxes − Subsidies)', cx, y + 112);

    // 3 Formula Comparison Columns
    const colY = y + 155;
    const colH = 265;
    const colW = 340;

    // Column 1: GVA 8.2%
    const c1X = x + 40;
    drawGlassCard(ctx, c1X, colY, colW, colH, 14, 'rgba(14, 165, 233, 0.3)', 'rgba(14, 165, 233, 0.06)');
    ctx.fillStyle = '#38bdf8';
    ctx.font = '700 15px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText('STEP 1: PRODUCTION BASE', c1X + 24, colY + 38);
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 22px "Inter", sans-serif';
    ctx.fillText('Real GVA Growth', c1X + 24, colY + 70);
    ctx.fillStyle = '#38bdf8';
    ctx.font = '900 52px "JetBrains Mono", monospace';
    ctx.fillText('8.2%', c1X + 24, colY + 135);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '400 13.5px "Inter", sans-serif';
    ctx.fillText('• Core output across sectors', c1X + 24, colY + 175);
    ctx.fillText('• Boosted by financial & IT hubs', c1X + 24, colY + 198);
    ctx.fillText('• Farm sector growth muted at ~2%', c1X + 24, colY + 221);

    // Math Operator Minus
    ctx.fillStyle = '#fbbf24';
    ctx.font = '900 36px "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('−', x + 40 + colW + 40, colY + colH/2);

    // Column 2: Net Tax Discrepancy -0.4%
    const c2X = x + 420;
    drawGlassCard(ctx, c2X, colY, colW, colH, 14, 'rgba(251, 191, 36, 0.35)', 'rgba(251, 191, 36, 0.06)');
    ctx.fillStyle = '#fbbf24';
    ctx.font = '700 15px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText('STEP 2: STATISTICAL WEDGE', c2X + 24, colY + 38);
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 22px "Inter", sans-serif';
    ctx.fillText('Net Product Taxes', c2X + 24, colY + 70);
    ctx.fillStyle = '#fbbf24';
    ctx.font = '900 52px "JetBrains Mono", monospace';
    ctx.fillText('−0.4%', c2X + 24, colY + 135);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '400 13.5px "Inter", sans-serif';
    ctx.fillText('• Lower government subsidy payouts', c2X + 24, colY + 175);
    ctx.fillText('• High indirect tax collections', c2X + 24, colY + 198);
    ctx.fillText('• Creates artificial headline divergence', c2X + 24, colY + 221);

    // Math Operator Equals
    ctx.fillStyle = '#10b981';
    ctx.font = '900 36px "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('=', x + 420 + colW + 40, colY + colH/2);

    // Column 3: Real GDP 7.8%
    const c3X = x + 800;
    drawGlassCard(ctx, c3X, colY, colW, colH, 14, 'rgba(16, 185, 129, 0.4)', 'rgba(16, 185, 129, 0.08)');
    ctx.fillStyle = '#10b981';
    ctx.font = '700 15px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText('STEP 3: HEADLINE RESULT', c3X + 24, colY + 38);
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 22px "Inter", sans-serif';
    ctx.fillText('Real GDP Growth', c3X + 24, colY + 70);
    ctx.fillStyle = '#10b981';
    ctx.font = '900 52px "JetBrains Mono", monospace';
    ctx.fillText('7.8%', c3X + 24, colY + 135);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '400 13.5px "Inter", sans-serif';
    ctx.fillText('• Official global bragging headline', c3X + 24, colY + 175);
    ctx.fillText('• Fastest growing major economy', c3X + 24, colY + 198);
    ctx.fillText('• Hides unequal income distribution', c3X + 24, colY + 221);

    // Bottom Summary Banner
    const botY = y + 445;
    drawGlassCard(ctx, x + 40, botY, cardW - 80, 95, 12, 'rgba(255, 255, 255, 0.1)', 'rgba(0, 0, 0, 0.5)');
    ctx.fillStyle = '#38bdf8';
    ctx.font = '700 15px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText('🔍 GROUND REALITY VERDICT:', x + 65, botY + 36);
    ctx.fillStyle = '#f8fafc';
    ctx.font = '500 15.5px "Inter", sans-serif';
    ctx.fillText('जब जीडीपी बढ़ता है लेकिन आम आदमी की बचत गिरती है, तो इसका मतलब है कि ग्रोथ कागज़ पर टैक्स और उच्च-आय वालों के दम पर है, आम उपभोग पर नहीं!', x + 65, botY + 68);

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
  // DIAGRAM 5: The "Missing Factory" Structural Gap (365.03s - 405.48s)
  // -------------------------------------------------------------
  function drawMissingFactoryDiagram(ctx, t, start_s = 365.03, end_s = 405.48) {
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

    const cx = 960, cy = 515 + enterOffset;
    const cardW = 1140, cardH = 540;
    const x = cx - cardW/2, y = cy - cardH/2;

    drawGlassCard(ctx, x, y, cardW, cardH, 20, 'rgba(56, 189, 248, 0.4)');

    // Header
    drawBadge(ctx, 'STRUCTURAL DEFICIT · THE ASIAN DEVELOPMENT PARADOX', cx, y + 36, '#fbbf24', 'rgba(251, 191, 36, 0.15)', 'rgba(251, 191, 36, 0.4)');
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 26px "Outfit", "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('THE MISSING FACTORY: WHY MANUFACTURING WON’T ABSORB LABOR', cx, y + 74);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 14px "Inter", sans-serif';
    ctx.fillText('Every industrial power transitioned from Agriculture to Factories before Services. India skipped factories.', cx, y + 98);

    // Track 1: Normal Route (China / East Asia)
    const t1Y = y + 120;
    drawGlassCard(ctx, x + 30, t1Y, cardW - 60, 125, 14, 'rgba(16, 185, 129, 0.35)', 'rgba(16, 185, 129, 0.05)');
    ctx.fillStyle = '#34d399';
    ctx.font = '800 15px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText('STANDARD EAST ASIAN PATHWAY (China, S. Korea, Taiwan):', x + 50, t1Y + 30);

    ctx.fillStyle = '#ffffff';
    ctx.font = '700 15.5px "Inter", sans-serif';
    ctx.fillText('Agriculture (Farms)', x + 50, t1Y + 68);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '400 12.5px "Inter", sans-serif';
    ctx.fillText('Low productivity labor', x + 50, t1Y + 90);

    ctx.fillStyle = '#10b981';
    ctx.font = '900 22px "Inter", sans-serif';
    ctx.fillText('➔', x + 240, t1Y + 76);

    ctx.fillStyle = '#ffffff';
    ctx.font = '700 15.5px "Inter", sans-serif';
    ctx.fillText('MASS MANUFACTURING (27% GDP)', x + 295, t1Y + 68);
    ctx.fillStyle = '#34d399';
    ctx.font = '700 12.5px "Inter", sans-serif';
    ctx.fillText('Lifted 80 Crore citizens into middle class', x + 295, t1Y + 90);

    ctx.fillStyle = '#10b981';
    ctx.font = '900 22px "Inter", sans-serif';
    ctx.fillText('➔', x + 615, t1Y + 76);

    ctx.fillStyle = '#ffffff';
    ctx.font = '700 15.5px "Inter", sans-serif';
    ctx.fillText('High-End Services & Tech', x + 670, t1Y + 68);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '400 12.5px "Inter", sans-serif';
    ctx.fillText('Advanced mature economy', x + 670, t1Y + 90);

    // Track 2: India's Chasm / Skipped Route
    const t2Y = y + 260;
    drawGlassCard(ctx, x + 30, t2Y, cardW - 60, 175, 14, 'rgba(244, 63, 94, 0.45)', 'rgba(244, 63, 94, 0.06)');
    ctx.fillStyle = '#f43f5e';
    ctx.font = '800 15px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText('INDIA’S STRUCTURAL CHASM (THE PREMATURE JUMP):', x + 50, t2Y + 30);

    // Box 1: Farm Choke
    ctx.fillStyle = '#ffffff';
    ctx.font = '700 15.5px "Inter", sans-serif';
    ctx.fillText('Agriculture (45.4% Workforce)', x + 50, t2Y + 68);
    ctx.fillStyle = '#f87171';
    ctx.font = '700 12.5px "Inter", sans-serif';
    ctx.fillText('Contributes ONLY 15% to GDP!', x + 50, t2Y + 90);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '400 12px "Inter", sans-serif';
    ctx.fillText('Disguised farm unemployment', x + 50, t2Y + 110);

    // The Broken Chasm
    const chasmX = x + 300, chasmY = t2Y + 45, chasmW = 320, chasmH = 105;
    drawGlassCard(ctx, chasmX, chasmY, chasmW, chasmH, 10, 'rgba(244, 63, 94, 0.6)', 'rgba(76, 5, 25, 0.35)');
    ctx.fillStyle = '#f43f5e';
    ctx.font = '900 14px "JetBrains Mono", monospace';
    ctx.textAlign = 'center';
    ctx.fillText('❌ THE MISSING FACTORY GAP', chasmX + chasmW/2, chasmY + 30);
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 19px "JetBrains Mono", monospace';
    ctx.fillText('STUCK AT 15.8% GDP', chasmX + chasmW/2, chasmY + 58);
    ctx.fillStyle = '#fbbf24';
    ctx.font = '500 12px "Inter", sans-serif';
    ctx.fillText('Make in India Target was 25% (Deficit 9.2%)', chasmX + chasmW/2, chasmY + 84);

    // Box 2: Elite Services
    const servX = x + 660;
    ctx.textAlign = 'left';
    ctx.fillStyle = '#ffffff';
    ctx.font = '700 15.5px "Inter", sans-serif';
    ctx.fillText('IT & Financial Services (12.1% Growth)', servX, t2Y + 68);
    ctx.fillStyle = '#38bdf8';
    ctx.font = '700 12.5px "Inter", sans-serif';
    ctx.fillText('Employs <5% with English & Tech Degrees', servX, t2Y + 90);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '400 12px "Inter", sans-serif';
    ctx.fillText('Cannot absorb 45% farm labor!', servX, t2Y + 110);

    // Bottom Conclusion
    const botY = y + 450;
    ctx.fillStyle = '#f8fafc';
    ctx.font = '500 14px "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('जब तक भारत कपड़ा, जूते और इलेक्ट्रॉनिक्स की मास-फ़ैक्ट्रीज़ नहीं लगाएगा, आम ग्रामीण युवा को सम्मानजनक नौकरी नहीं मिल सकती!', cx, botY + 36);

    ctx.restore();
  }

  // -------------------------------------------------------------
  // DIAGRAM 6: The 2045 Demographic Clock (500.18s - 525.70s)
  // -------------------------------------------------------------
  function drawDemographicClockDiagram(ctx, t, start_s = 500.18, end_s = 525.70) {
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

    drawGlassCard(ctx, x, y, cardW, cardH, 20, 'rgba(251, 146, 60, 0.4)');

    // Header
    drawBadge(ctx, 'ACTUARIAL DEMOGRAPHIC RISK · NFHS PROJECTIONS', cx, y + 40, '#fb923c', 'rgba(251, 146, 60, 0.15)', 'rgba(251, 146, 60, 0.4)');
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 28px "Outfit", "Inter", sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText('THE 2045 DEMOGRAPHIC CLOCK: RACE AGAINST TIME', cx, y + 80);

    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 15px "Inter", sans-serif';
    ctx.fillText('India has only 19 years before its demographic dividend window permanently shuts.', cx, y + 108);

    // Left Column: Today's Advantage (Youth)
    const colW = 340, colH = 340, colY = y + 145;
    const leftX = x + 40;
    drawGlassCard(ctx, leftX, colY, colW, colH, 16, 'rgba(56, 189, 248, 0.35)', 'rgba(15, 23, 42, 0.6)');
    ctx.fillStyle = '#38bdf8';
    ctx.font = '800 16px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText('TODAY (2026 STATUS)', leftX + 24, colY + 38);
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 22px "Inter", sans-serif';
    ctx.fillText('Median Age: 28.4 Yrs', leftX + 24, colY + 74);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '400 14px "Inter", sans-serif';
    ctx.fillText('• 1.1 Crore Youth Enter Jobs/Yr', leftX + 24, colY + 120);
    ctx.fillText('• Youngest workforce on Earth', leftX + 24, colY + 148);
    ctx.fillText('• Fertility Rate: 2.0 (NFHS-5)', leftX + 24, colY + 176);
    ctx.fillText('• Replacement level broken', leftX + 24, colY + 204);
    ctx.fillText('• South states already aging', leftX + 24, colY + 232);

    // Centerpiece: The Glowing Clock Gauge
    const clockCX = cx;
    const clockCY = colY + colH/2;
    const radius = 110;

    // Outer Track
    ctx.strokeStyle = 'rgba(255, 255, 255, 0.1)';
    ctx.lineWidth = 14;
    ctx.beginPath();
    ctx.arc(clockCX, clockCY, radius, 0, Math.PI * 2);
    ctx.stroke();

    // Animated Ticking Progress Arc (Remaining Window)
    const clockProgress = 0.65 + Math.sin(t * 3) * 0.02;
    ctx.strokeStyle = '#fb923c';
    ctx.shadowColor = '#fb923c';
    ctx.shadowBlur = 18;
    ctx.lineWidth = 14;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.arc(clockCX, clockCY, radius, -Math.PI/2, -Math.PI/2 + Math.PI * 2 * clockProgress);
    ctx.stroke();
    ctx.shadowBlur = 0;
    ctx.lineCap = 'butt';

    // Center Text
    ctx.fillStyle = '#ffffff';
    ctx.font = '900 36px "JetBrains Mono", monospace';
    ctx.textAlign = 'center';
    ctx.fillText('2045', clockCX, clockCY - 5);
    ctx.fillStyle = '#fb923c';
    ctx.font = '800 13px "JetBrains Mono", monospace';
    ctx.fillText('WINDOW CLOSES', clockCX, clockCY + 26);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '500 12px "Inter", sans-serif';
    ctx.fillText('~19 Years Remaining', clockCX, clockCY + 46);

    // Right Column: The Risk (Growing Old Before Rich)
    const rightX = x + cardW - 40 - colW;
    drawGlassCard(ctx, rightX, colY, colW, colH, 16, 'rgba(244, 63, 94, 0.45)', 'rgba(136, 19, 55, 0.2)');
    ctx.fillStyle = '#f43f5e';
    ctx.font = '800 16px "JetBrains Mono", monospace';
    ctx.textAlign = 'left';
    ctx.fillText('THE MIDDLE-INCOME TRAP', rightX + 24, colY + 38);
    ctx.fillStyle = '#ffffff';
    ctx.font = '800 22px "Inter", sans-serif';
    ctx.fillText('Target: $10,000 / Cap', rightX + 24, colY + 74);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '400 14px "Inter", sans-serif';
    ctx.fillText('• Must reach $10k before 2045', rightX + 24, colY + 120);
    ctx.fillText('• Current: $2,730 (Need 4x leap)', rightX + 24, colY + 148);
    ctx.fillText('• Without mass formal pensions', rightX + 24, colY + 176);
    ctx.fillText('• Without universal healthcare', rightX + 24, colY + 204);
    ctx.fillText('• Brazil/Thailand stagnation risk', rightX + 24, colY + 232);

    // Bottom Warning Banner
    const botY = y + 510;
    drawGlassCard(ctx, x + 40, botY, cardW - 80, 68, 12, 'rgba(255, 255, 255, 0.12)', 'rgba(0, 0, 0, 0.6)');
    ctx.fillStyle = '#fbbf24';
    ctx.font = '700 15px "JetBrains Mono", monospace';
    ctx.textAlign = 'center';
    ctx.fillText('⚠️ अगर अगले 18 सालों में पर-कैपिटा इनकम नहीं बढ़ी, तो भारत अमीर बनने से पहले बूढ़ा हो जाएगा!', cx, botY + 40);

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
