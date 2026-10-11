/**
 * forensic_overlays.js — Benaqaab India Forensic Motion Graphics HUD & Overlays
 * Episode EP-19: India's 7.8% GDP vs Global Superpowers
 * 
 * Provides bespoke glassmorphic HUD cards, data pills, and evidence callouts
 * for every single beat across the entire documentary film, ensuring ZERO bare slides.
 */

(function(root) {
  'use strict';

  function easeOutCubic(x) {
    return 1 - Math.pow(1 - Math.max(0, Math.min(1, x)), 3);
  }

  // Draw frosted glassmorphic card with specular highlights (High background image visibility)
  function drawGlassCard(ctx, x, y, w, h, r = 16, borderColor = 'rgba(56, 189, 248, 0.38)', bgColor = null) {
    ctx.save();

    // Translucent spatial frosted glass that keeps background image vividly visible
    if (!bgColor || bgColor === 'rgba(7, 10, 18, 0.88)' || bgColor === 'rgba(8, 12, 22, 0.92)' || bgColor === 'rgba(8, 12, 22, 0.90)') {
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
    specGrad.addColorStop(0.3, 'rgba(255, 255, 255, 0.35)');
    specGrad.addColorStop(0.7, borderColor);
    specGrad.addColorStop(1, 'rgba(255, 255, 255, 0)');
    ctx.strokeStyle = specGrad;
    ctx.lineWidth = 1.2;
    ctx.beginPath();
    ctx.moveTo(x + r, y);
    ctx.lineTo(x + w - r, y);
    ctx.stroke();

    // Subtle corner HUD reticle brackets
    const bracketSize = 10;
    ctx.strokeStyle = borderColor;
    ctx.lineWidth = 1.5;
    // Top-left bracket
    ctx.beginPath();
    ctx.moveTo(x + 4, y + 4 + bracketSize);
    ctx.lineTo(x + 4, y + 4);
    ctx.lineTo(x + 4 + bracketSize, y + 4);
    ctx.stroke();
    // Top-right bracket
    ctx.beginPath();
    ctx.moveTo(x + w - 4 - bracketSize, y + 4);
    ctx.lineTo(x + w - 4, y + 4);
    ctx.lineTo(x + w - 4, y + 4 + bracketSize);
    ctx.stroke();

    ctx.restore();
  }

  // Draw category tag pill
  function drawTagPill(ctx, text, x, y, color = '#38bdf8', bg = 'rgba(56, 189, 248, 0.12)') {
    ctx.save();
    ctx.font = '700 11px "JetBrains Mono", monospace';
    const tw = ctx.measureText(text).width;
    const pw = tw + 18, ph = 22;
    ctx.fillStyle = bg;
    ctx.strokeStyle = color;
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.roundRect(x, y - ph/2, pw, ph, 11);
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = color;
    ctx.textAlign = 'left';
    ctx.textBaseline = 'middle';
    ctx.fillText(text, x + 9, y);
    ctx.restore();
    return pw;
  }

  // ---------------------------------------------------------------------------
  // OVERLAY DEFINITIONS FOR NON-DIAGRAM BEATS
  // ---------------------------------------------------------------------------
  const OVERLAYS = [
    // CHAPTER 1 BEATS
    {
      start_s: 8.28, end_s: 16.07,
      pos: 'top-right',
      theme: 'amber',
      tag: 'GROUND REALITY CHECK · HOUSEHOLD LEDGER',
      title: 'THE INFLATION SQUEEZE ON SAVINGS',
      stats: [
        { label: 'NET FINANCIAL SAVINGS', val: '5.3% GDP', sub: '47-Year Historical Low', color: '#f43f5e' },
        { label: 'HOUSEHOLD DEBT LIABILITIES', val: '45.8% GDP', sub: 'Surging Borrowing Rate', color: '#fbbf24' }
      ],
      verdict: '7.8% विकास के बावजूद आम परिवार की बचत लगातार सिकुड़ रही है।'
    },
    {
      start_s: 16.07, end_s: 19.99,
      pos: 'top-right',
      theme: 'crimson',
      tag: 'WELFARE REALITY · PMGKAY LEDGER',
      title: '80 CRORE CITIZENS ON FREE FOODGRAINS',
      stats: [
        { label: 'TOTAL BENEFICIARIES', val: '80.0 Crore', sub: 'Extended Till 2028', color: '#f43f5e' },
        { label: 'POPULATION SHARE', val: '57.0%', sub: 'Dependent on Basic Rations', color: '#fbbf24' }
      ],
      verdict: 'अगर देश समृद्ध हो रहा है, तो 57% आबादी मुफ्त अनाज पर क्यों निर्भर है?'
    },
    {
      start_s: 19.99, end_s: 29.44,
      pos: 'top-right',
      theme: 'cyan',
      tag: 'OFFICIAL MACRO DATA · PARLIAMENT ACCOUNTS',
      title: 'INDIA OVERTAKES UK: 5th LARGEST ECONOMY',
      stats: [
        { label: 'NOMINAL GDP SIZE', val: '$3.94 Trillion', sub: 'Global 5th Rank', color: '#38bdf8' },
        { label: 'UK GDP OVERTAKEN', val: '$3.30 Trillion', sub: 'Historical Milestone', color: '#34d399' }
      ],
      verdict: 'सकल आकार में ब्रिटेन को पछाड़ा, लेकिन प्रति-व्यक्ति आय की कहानी बिल्कुल अलग है।'
    },
    {
      start_s: 29.44, end_s: 38.90,
      pos: 'top-right',
      theme: 'cyan',
      tag: 'NATIONAL INCOME LEDGER · ₹330 LAKH CRORE',
      title: 'THE $3.94 TRILLION HEADLINE EUPHORIA',
      stats: [
        { label: 'TOTAL ECONOMY IN RUPEES', val: '₹330 Lakh Cr', sub: 'Annual Production Base', color: '#38bdf8' },
        { label: 'OFFICIAL REAL GDP', val: '7.8% Growth', sub: 'Fastest Among G20', color: '#34d399' }
      ],
      verdict: 'ग्लोबल फोरम पर तालियां, लेकिन इस संपत्ति का वितरण किसके पास जा रहा है?'
    },
    {
      start_s: 38.90, end_s: 48.30,
      pos: 'center-bento',
      theme: 'crimson',
      tag: 'INVESTIGATIVE ANCHOR · THE 7.8% HEADLINE DECONSTRUCTION',
      title: 'THE DISCREPANCY UNMASKED: HEADLINE vs STREET REALITY',
      subtitle: 'What Official Government Press Releases Leave Unsaid',
      cells: [
        { title: 'Headline Claim', metric: '7.8% GDP', desc: 'Fastest growing major world economy', color: '#34d399' },
        { title: 'Ground Truth', metric: '5.3% Savings', desc: 'Household savings at 47-year historical low', color: '#f43f5e' },
        { title: 'Per-Capita Rank', metric: '#136th', desc: '2,730 dollars annual per-capita income', color: '#fbbf24' }
      ],
      verdict: 'हेडलाइन 7.8% है, लेकिन ज़मीनी हक़ीक़त में आम आदमी की जेब खाली हो रही है।'
    },
    {
      start_s: 48.30, end_s: 60.10,
      pos: 'top-right',
      theme: 'amber',
      tag: 'FORENSIC AUDIT METHODOLOGY · SACH · SABOOT · BEBAK',
      title: 'DECONSTRUCTING THE REAL GDP PUZZLE',
      stats: [
        { label: 'PRIMARY DATA SOURCES', val: 'MoSPI + RBI', sub: 'National Accounts Gazettes', color: '#fbbf24' },
        { label: 'GLOBAL BENCHMARKS', val: 'World Bank', sub: 'Cross-Country Comparison', color: '#38bdf8' }
      ],
      verdict: 'बिना किसी बायस के, ऑफिशियल डेटा और सबूतों के साथ पूरा सच।'
    },

    // CHAPTER 2 BEATS: PER-CAPITA INCOME ILLUSION
    {
      start_s: 83.45, end_s: 104.66,
      pos: 'top-right',
      theme: 'amber',
      tag: 'CHAPTER 2 ANCHOR · THE PER-CAPITA PARADOX',
      title: 'AGGREGATE GDP vs CITIZEN WALLET REALITY',
      stats: [
        { label: 'COST OF LIVING SURGE', val: '+28.5%', sub: 'Education, Health & Housing', color: '#f43f5e' },
        { label: 'REAL WAGE GROWTH', val: '< 1.0%', sub: 'Adjusted for Inflation', color: '#fbbf24' }
      ],
      verdict: 'सकल जीडीपी 5वीं सबसे बड़ी है, लेकिन 143 करोड़ नागरिकों में बंटने पर क्या बचता है?'
    },
    {
      start_s: 104.66, end_s: 114.07,
      pos: 'top-left',
      theme: 'cyan',
      tag: 'DEMOGRAPHIC DENOMINATOR · 1.43 BILLION',
      title: 'THE 143 CRORE CITIZEN MULTIPLIER',
      stats: [
        { label: 'TOTAL POPULATION', val: '1.43 Billion', sub: 'World Largest Population', color: '#38bdf8' },
        { label: 'SHARE OF GLOBAL POPULATION', val: '17.8%', sub: '1 in Every 5.6 Humans', color: '#34d399' }
      ],
      verdict: 'बड़ी अर्थव्यवस्था केवल इसलिए दिखती है क्योंकि जनसंख्या दुनिया में सबसे अधिक है।'
    },
    {
      start_s: 114.07, end_s: 121.45,
      pos: 'top-right',
      theme: 'amber',
      tag: 'MATHEMATICAL FORMULA · PER-CAPITA DIVISION',
      title: 'TOTAL WEALTH DIVIDED BY 143 CRORE',
      stats: [
        { label: 'PER-CAPITA INCOME (USD)', val: '$2,730 / yr', sub: 'World Bank Atlas Method', color: '#fbbf24' },
        { label: 'MONTHLY PER-CAPITA', val: '₹18,900 / mo', sub: 'Gross Average (Skewed by Billionaires)', color: '#38bdf8' }
      ],
      verdict: 'सकल जीडीपी को 143 करोड़ से भाग दें तो हम विश्व में 136वें स्थान पर आते हैं।'
    },
    {
      start_s: 121.45, end_s: 137.96,
      pos: 'top-right',
      theme: 'crimson',
      tag: 'OFFICIAL WORLD BANK RANKING TABLE',
      title: 'INDIA AT RANK #136 OUT OF 190 COUNTRIES',
      stats: [
        { label: 'WORLD RANKING', val: '#136th', sub: 'Lower-Middle Income Bracket', color: '#f43f5e' },
        { label: 'COMPARISON BRACKET', val: 'Below Bhutan', sub: 'Similar to Angola & Rep. Congo', color: '#fbbf24' }
      ],
      verdict: 'सकल आकार 5वां, लेकिन प्रति-व्यक्ति समृद्धि में हम 135 देशों से पीछे हैं।'
    },
    {
      start_s: 137.96, end_s: 148.53,
      pos: 'top-right',
      theme: 'cyan',
      tag: 'DEVELOPED ECONOMY BENCHMARK · THE THRESHOLD',
      title: 'THE HIGH-INCOME DISTANCE: $14,005+',
      stats: [
        { label: 'HIGH-INCOME THRESHOLD', val: '$14,005+', sub: 'World Bank High Income Line', color: '#34d399' },
        { label: 'INDIA CURRENT INCOME', val: '$2,730', sub: '5.1x Income Expansion Needed', color: '#f43f5e' }
      ],
      verdict: 'अमीर देश बनने के लिए प्रति-व्यक्ति आय को कम से कम 5 गुना बढ़ाना होगा।'
    },

    // CHAPTER 3 BEATS: K-SHAPED DIVERGENCE
    {
      start_s: 173.16, end_s: 185.71,
      pos: 'center-bento',
      theme: 'cyan',
      tag: 'CHAPTER 3 ANCHOR · THE K-SHAPED ECONOMIC SPLIT',
      title: 'THE K-SHAPED DIVERGENCE: TWO OPPOSING WORLDS',
      subtitle: 'Where Is the 7.8% Growth Actually Flowing?',
      cells: [
        { title: 'Upper Arm of K', metric: 'Top 10-15%', desc: 'Asset owners, stock market wealth, luxury boom', color: '#34d399' },
        { title: 'Lower Arm of K', metric: 'Bottom 85%', desc: 'Small cars crash -42%, bikes down -14%, 80Cr rations', color: '#f43f5e' },
        { title: 'Core Insight', metric: 'K-Split', desc: 'Two halves of India moving in opposite directions', color: '#fbbf24' }
      ],
      verdict: 'यह पूरे देश का विकास नहीं, बल्कि केवल शीर्ष 15% का सुपर-बूम है।'
    },
    {
      start_s: 224.59, end_s: 242.08,
      pos: 'top-right',
      theme: 'mint',
      tag: 'AUTOMOBILE FLASH DATA · SIAM REPORT',
      title: 'UPPER K: LUXURY SUVS BOOMING (+24.5%)',
      stats: [
        { label: 'LUXURY VEHICLE SALES', val: '+24.5%', sub: 'Record Sales in Premium Segment', color: '#34d399' },
        { label: 'DEMAT ACCOUNTS CREATED', val: '15.0 Crore', sub: 'Capital Gains Windfall', color: '#38bdf8' }
      ],
      verdict: 'अमीरों के लिए बूम: लग्जरी गाड़ियों और रियल एस्टेट में रिकॉर्ड तेजी।'
    },
    {
      start_s: 242.08, end_s: 255.11,
      pos: 'top-left',
      theme: 'crimson',
      tag: 'AUTOMOBILE CONSUMPTION RETREAT · LOWER K',
      title: 'LOWER K: ENTRY-LEVEL SMALL CARS COLLAPSE',
      stats: [
        { label: 'SMALL HATCHBACK SALES', val: '-42.0%', sub: 'Pre-Covid Peak vs 2026', color: '#f43f5e' },
        { label: 'MASS MARKET BUYERS', val: 'Exited Market', sub: 'Pricing Exceeded Family Budgets', color: '#fbbf24' }
      ],
      verdict: 'आम मिडिल क्लास कार खरीदना छोड़ चुका है— छोटी कारों की बिक्री 42% गिरी।'
    },
    {
      start_s: 255.11, end_s: 260.00,
      pos: 'top-right',
      theme: 'crimson',
      tag: 'RURAL ECONOMIC PULSE · TWO-WHEELERS',
      title: 'RURAL 100cc MOTORCYCLES DOWN -14%',
      stats: [
        { label: 'COMMUTER MOTORCYCLES', val: '-14.0%', sub: 'Below 2018-19 Peak Sales', color: '#f43f5e' },
        { label: 'RURAL REAL WAGES', val: 'Negative Growth', sub: 'Inflation Eroding Farm Purchasing Power', color: '#fbbf24' }
      ],
      verdict: 'गाँव का मजदूर और छोटा किसान नई बाइक खरीदने की स्थिति में नहीं है।'
    },
    {
      start_s: 260.00, end_s: 263.51,
      pos: 'top-right',
      theme: 'amber',
      tag: 'FARM EQUIPMENT DEMAND · RURAL SLOWDOWN',
      title: 'FARM MACHINERY & TRACTOR SALES SLUGGISH',
      stats: [
        { label: 'TRACTOR SALES GROWTH', val: '-8.5%', sub: 'Subdued Agricultural Capex', color: '#f43f5e' },
        { label: 'INPUT INFLATION', val: '+18.0%', sub: 'Diesel, Fertilizer & Seeds', color: '#fbbf24' }
      ],
      verdict: 'खेती की लागत बढ़ी, लेकिन उपज के दाम नहीं— ग्रामीण अर्थव्यवस्था पर दबाव।'
    },
    {
      start_s: 263.51, end_s: 272.30,
      pos: 'top-right',
      theme: 'crimson',
      tag: 'WELFARE DEPENDENCY · GOVT NOTIFICATION',
      title: 'PMGKAY EXTENSION: 80 CRORE ON FREE RATIONS',
      stats: [
        { label: 'SCHEME EXTENSION', val: '5 Full Years', sub: 'Extended Till December 2028', color: '#f43f5e' },
        { label: 'FISCAL ALLOCATION', val: '₹11.8 Lakh Cr', sub: 'Food Subsidy Budget', color: '#fbbf24' }
      ],
      verdict: 'अगर 7.8% ग्रोथ से गरीबी खत्म हो रही है, तो 80 करोड़ को मुफ्त राशन क्यों?'
    },
    {
      start_s: 272.30, end_s: 276.75,
      pos: 'top-right',
      theme: 'amber',
      tag: 'STRUCTURAL DIVERGENCE SUMMARY',
      title: 'TWO CONSUMPTION BASKETS IN ONE COUNTRY',
      stats: [
        { label: 'TOP 10% BASKET', val: 'Luxury Spending', sub: 'Foreign Travel & Penthouse Living', color: '#38bdf8' },
        { label: 'BOTTOM 85% BASKET', val: 'Survival Staples', sub: 'Subsidized Wheat & Rice', color: '#f43f5e' }
      ],
      verdict: 'के-शेप्ड इकॉनमी का मतलब: मुट्ठी भर लोगों की चमक, बाकी देश का ठहराव।'
    },

    // CHAPTER 4 BEATS: HOUSEHOLD BALANCE SHEET CRISIS
    {
      start_s: 276.75, end_s: 291.50,
      pos: 'center-bento',
      theme: 'crimson',
      tag: 'CHAPTER 4 ANCHOR · RESERVE BANK OF INDIA DATA',
      title: 'THE VANISHING MIDDLE CLASS: DEBT TRAP EXPLOSION',
      subtitle: 'RBI Financial Stability Report: Indian Households Under Pressure',
      cells: [
        { title: 'Net Financial Savings', metric: '5.3% GDP', desc: 'Plunged to a 47-year low (was 11.5%)', color: '#f43f5e' },
        { title: 'Household Liabilities', metric: '45.8% GDP', desc: 'Household debt reaching all-time high', color: '#fbbf24' },
        { title: 'Unsecured EMIs', metric: '58.2%', desc: 'Credit cards & personal loans for consumption', color: '#f43f5e' }
      ],
      verdict: 'जीडीपी बढ़ रही है, लेकिन आम भारतीय परिवार गंभीर कर्ज में डूब रहा है।'
    },
    {
      start_s: 291.50, end_s: 302.20,
      pos: 'top-right',
      theme: 'crimson',
      tag: 'RBI FINANCIAL STABILITY REPORT · HISTORICAL LOW',
      title: 'NET FINANCIAL SAVINGS PLUNGE TO 5.3%',
      stats: [
        { label: 'CURRENT NET SAVINGS', val: '5.3% GDP', sub: 'Historical Low in 2026', color: '#f43f5e' },
        { label: 'PREVIOUS PEAK LEVEL', val: '11.5% GDP', sub: 'Savings Cut by More than Half', color: '#38bdf8' }
      ],
      verdict: '47 साल में पहली बार भारतीय परिवारों की शुद्ध बचत इस निचले स्तर पर पहुंची है।'
    },
    {
      start_s: 302.20, end_s: 311.60,
      pos: 'top-right',
      theme: 'amber',
      tag: 'GROSS ASSETS vs RISING LIABILITIES',
      title: 'SAVINGS DRAIN: LIABILITIES SURPASS ASSETS',
      stats: [
        { label: 'GROSS FINANCIAL ASSETS', val: '13.5% GDP', sub: 'Bank FDs, Insurance, Mutual Funds', color: '#38bdf8' },
        { label: 'FINANCIAL LIABILITIES', val: '8.2% GDP', sub: 'EMIs, Home Loans, Credit Borrowing', color: '#f43f5e' }
      ],
      verdict: 'कमाई का बड़ा हिस्सा सीधे बैंक की किस्तों और ब्याज़ में जा रहा है।'
    },
    {
      start_s: 311.60, end_s: 318.56,
      pos: 'top-right',
      theme: 'crimson',
      tag: 'MIDDLE CLASS COST LIVING SQUEEZE',
      title: 'WHY SAVINGS COLLAPSED: BASIC EXPENSES TRIPLED',
      stats: [
        { label: 'EDUCATION INFLATION', val: '11.5% / yr', sub: 'School Fees & Coaching', color: '#f43f5e' },
        { label: 'HEALTHCARE EXPENSES', val: '14.2% / yr', sub: 'Hospital Bills & Out-of-Pocket', color: '#fbbf24' }
      ],
      verdict: 'शिक्षा, स्वास्थ्य और घर के खर्च वेतन वृद्धि से 3 गुना तेजी से बढ़ रहे हैं।'
    },
    {
      start_s: 318.56, end_s: 325.20,
      pos: 'top-right',
      theme: 'crimson',
      tag: 'HOUSEHOLD DEBT MILESTONE · 45.8% OF GDP',
      title: 'HOUSEHOLD DEBT REACHES HISTORIC 45.8%',
      stats: [
        { label: 'TOTAL HOUSEHOLD DEBT', val: '45.8% GDP', sub: 'All-Time Record in Indian History', color: '#f43f5e' },
        { label: 'UNSECURED PERSONAL LOANS', val: '+28.4% YoY', sub: 'Fastest Growing Loan Segment', color: '#fbbf24' }
      ],
      verdict: 'मध्यम वर्ग अपने भविष्य की कमाई को आज के खर्चों के लिए गिरवी रख रहा है।'
    },
    {
      start_s: 325.20, end_s: 331.00,
      pos: 'top-right',
      theme: 'amber',
      tag: 'CREDIT CARD OUTSTANDINGS · RBI WARNING',
      title: 'CREDIT CARD DEBT PEAKS: ₹2.6 LAKH CRORE',
      stats: [
        { label: 'TOTAL CREDIT CARD DEBT', val: '₹2.60 Lakh Cr', sub: 'Surged by 32% in 2 Years', color: '#f43f5e' },
        { label: 'DEFAULT RISK WEIGHT', val: '125% Hiked', sub: 'RBI Imposed Risk Capital Buffer', color: '#fbbf24' }
      ],
      verdict: 'क्रेडिट कार्ड स्वाइप से खरीदारी बढ़ रही है, लेकिन यह उधार का उपभोग है।'
    },
    {
      start_s: 331.00, end_s: 335.95,
      pos: 'top-right',
      theme: 'amber',
      tag: 'NBFC GOLD COLLATERAL SURGE',
      title: 'PLEDGING FAMILY GOLD FOR CASH FLOW',
      stats: [
        { label: 'GOLD LOAN DISBURSALS', val: '+34.0% YoY', sub: 'Surge in Pawnshops & NBFCs', color: '#fbbf24' },
        { label: 'PURPOSE OF BORROWING', val: 'Family Medical / Fees', sub: 'Emergency Cash Flow Strain', color: '#f43f5e' }
      ],
      verdict: 'घर का सोना गिरवी रखकर रोजमर्रा के खर्च और फीस भरी जा रही है।'
    },

    // CHAPTER 5 BEATS: THE MISSING FACTORY (INCLUDING SS2 BEAT 43!)
    {
      start_s: 361.60, end_s: 365.03,
      pos: 'center-bento',
      theme: 'cyan',
      tag: 'CHAPTER 5 INVESTIGATION · ROOT CAUSE ANALYSIS',
      title: 'THE STRUCTURAL BOTTLENECK: WHY GROWTH BYPASSES JOBS',
      subtitle: 'The Core Paradox of India\'s 7.8% Headline Expansion',
      cells: [
        { title: 'Headline GDP Growth', metric: '7.8%', desc: 'Fastest among G20 major economies', color: '#34d399' },
        { title: 'Manufacturing GDP Share', metric: '15.8%', desc: 'Target was 25% by 2022 (Stagnant for 30 yrs)', color: '#fbbf24' },
        { title: 'Mass Job Creation', metric: 'Missing', desc: 'Farm workers unable to transition to factories', color: '#f43f5e' }
      ],
      verdict: 'सवाल: अगर इकॉनमी 7.8% बढ़ रही है, तो करोड़ों युवाओं के लिए फैक्ट्रियां कहाँ गायब हैं?'
    },
    {
      start_s: 405.48, end_s: 409.40,
      pos: 'top-right',
      theme: 'mint',
      tag: 'SERVICE SECTOR EXPANSION · HIGH-TECH',
      title: 'IT & FINANCIAL SERVICES EXPANSION (+12.1%)',
      stats: [
        { label: 'IT SECTOR GROWTH RATE', val: '12.1% YoY', sub: 'Leading Export Engine', color: '#34d399' },
        { label: 'TOTAL EXPORT REVENUE', val: '$245 Billion', sub: 'Software & Cloud Services', color: '#38bdf8' }
      ],
      verdict: 'आईटी और फाइनेंस शानदार कर रहे हैं, लेकिन क्या वो 143 करोड़ को नौकरी दे सकते हैं?'
    },
    {
      start_s: 409.40, end_s: 415.00,
      pos: 'top-left',
      theme: 'crimson',
      tag: 'EDUCATION CREDENTIAL BOTTLENECK',
      title: 'THE 5% ELITE WORKFORCE BOUNDARY',
      stats: [
        { label: 'TECH WORKFORCE SHARE', val: '< 5% Total Jobs', sub: 'Requires Advanced English & Coding', color: '#f43f5e' },
        { label: 'WORKFORCE WITHOUT TECH DEGREE', val: '95% (50+ Cr)', sub: 'Trapped in Low-Income Informal Work', color: '#fbbf24' }
      ],
      verdict: 'आईटी केवल शीर्ष 5% अंग्रेजी-भाषी युवाओं को रोजगार दे सकता है, 95% के लिए नहीं।'
    },
    {
      start_s: 415.00, end_s: 423.50,
      pos: 'top-right',
      theme: 'amber',
      tag: 'CAPITAL-INTENSIVE vs LABOR-INTENSIVE',
      title: 'HIGH-TECH CAPITAL INTENSITY PARADOX',
      stats: [
        { label: 'SEMICONDUCTOR FAB CAPEX', val: '₹91,000 Cr', sub: 'High Technology Infrastructure', color: '#38bdf8' },
        { label: 'DIRECT JOBS CREATED', val: '~20,000 Jobs', sub: 'High Capital, Very Low Mass Employment', color: '#f43f5e' }
      ],
      verdict: 'अरबों डॉलर की सेमीकंडक्टर फैब बहुत कम लोगों को प्रत्यक्ष रोजगार देती है।'
    },
    {
      start_s: 423.50, end_s: 431.23,
      pos: 'top-right',
      theme: 'mint',
      tag: 'MASS EMPLOYMENT INDUSTRIES · BLUE COLLAR',
      title: 'WHERE ARE TEXTILES, FOOTWEAR & TOYS?',
      stats: [
        { label: 'TEXTILES & GARMENTS', val: 'Job Multiplier 10x', sub: 'Absorbs Unskilled Farm Workers', color: '#34d399' },
        { label: 'INDIA EXPORT SHARE', val: 'Stagnant at 4.2%', sub: 'Lost to Vietnam & Bangladesh', color: '#f43f5e' }
      ],
      verdict: 'कपड़ा और जूता फैक्ट्रियां ही 10वीं पास युवाओं को सम्मानजनक वेतन दे सकती हैं।'
    },
    {
      start_s: 431.23, end_s: 450.38,
      pos: 'top-right',
      theme: 'crimson',
      tag: 'MANUFACTURING SHARE IN GDP · 15.8%',
      title: 'MANUFACTURING SHARE STALLED AT 15.8%',
      stats: [
        { label: 'INDIA MFG SHARE', val: '15.8% GDP', sub: 'Stagnant for 3 Decades', color: '#f43f5e' },
        { label: 'CHINA MANUFACTURING', val: '27.0% GDP', sub: 'Lifted 80 Crore Out of Poverty', color: '#38bdf8' }
      ],
      verdict: 'मेक इन इंडिया का लक्ष्य 25% था, लेकिन हम आज भी 15.8% पर अटके हुए हैं।'
    },
    {
      start_s: 450.38, end_s: 457.45,
      pos: 'top-left',
      theme: 'amber',
      tag: 'STRUCTURAL REASON: WHY VIETNAM WON',
      title: 'TARIFF BARRIERS vs GLOBAL SUPPLY CHAINS',
      stats: [
        { label: 'VIETNAM FREE TRADE PACTS', val: '16 Global FTAs', sub: 'Zero-Duty Access to EU & US', color: '#34d399' },
        { label: 'FEMALE LABOR PARTICIPATION', val: '73% in Vietnam', sub: 'India Female Workforce Only 37%', color: '#f43f5e' }
      ],
      verdict: 'वियतनाम और बांग्लादेश ने मुक्त व्यापार और महिला श्रम बल से बाजी मार ली।'
    },

    // CHAPTER 6 BEATS: THE 2045 DEMOGRAPHIC CLOCK
    {
      start_s: 457.45, end_s: 470.20,
      pos: 'top-right',
      theme: 'amber',
      tag: 'CHAPTER 6 ANCHOR · THE DEMOGRAPHIC CLOCK',
      title: 'THE 2045 DEADLINE: MEDIAN AGE 28.7 YEARS',
      stats: [
        { label: 'MEDIAN AGE OF INDIA', val: '28.7 Years', sub: 'Youngest Major World Economy', color: '#38bdf8' },
        { label: 'WORKING AGE POPULATION', val: '68.0%', sub: 'Historic Demographic Dividend', color: '#34d399' }
      ],
      verdict: 'भारत के पास दुनिया का सबसे बड़ा युवा कार्यबल है— लेकिन केवल अगले 19 साल तक!'
    },
    {
      start_s: 470.20, end_s: 477.50,
      pos: 'top-right',
      theme: 'cyan',
      tag: 'HISTORICAL PRECEDENT · EAST ASIA',
      title: 'EAST ASIAN TIGERS GOT RICH BEFORE AGING',
      stats: [
        { label: 'JAPAN / KOREA / CHINA', val: '$12,000+ per cap', sub: 'Income Reached Before Median Age Hit 38', color: '#34d399' },
        { label: 'INDIA CURRENT INCOME', val: '$2,730', sub: 'Danger of Growing Old Before Rich', color: '#f43f5e' }
      ],
      verdict: 'चीन, कोरिया और जापान बूढ़े होने से पहले अमीर बन गए। भारत के सामने उल्टा खतरा है।'
    },
    {
      start_s: 477.50, end_s: 484.82,
      pos: 'center-bento',
      theme: 'crimson',
      tag: 'THE MIDDLE-INCOME TRAP DEFINED',
      title: 'THE MIDDLE-INCOME TRAP: GETTING OLD BEFORE RICH',
      subtitle: 'The Greatest Strategic Challenge Facing India\'s Next Generation',
      cells: [
        { title: 'Demographic Tipping Point', metric: 'Year 2045', desc: 'Aging begins, dependency ratio rises rapidly', color: '#f43f5e' },
        { title: 'Current Per-Capita Income', metric: '$2,730', desc: 'Rank #136 in the lower-middle income tier', color: '#fbbf24' },
        { title: 'Target Income Needed', metric: '$12,000+', desc: 'Required to fund pensions & geriatric health', color: '#34d399' }
      ],
      verdict: 'अगर 2045 तक प्रति-व्यक्ति आय 12,000 डॉलर नहीं पहुंची, तो देश पेंशन संकट में फंस जाएगा।'
    },
    {
      start_s: 484.82, end_s: 500.18,
      pos: 'top-right',
      theme: 'amber',
      tag: 'FERTILITY RATE COLLAPSE · TFR 2.0',
      title: 'FERTILITY DROPS BELOW REPLACEMENT (2.0)',
      stats: [
        { label: 'NATIONAL FERTILITY RATE', val: '2.0 TFR', sub: 'Below Replacement Level (2.1)', color: '#fbbf24' },
        { label: 'SOUTHERN STATES TFR', val: '1.5 - 1.7', sub: 'Aging Faster Than North America', color: '#f43f5e' }
      ],
      verdict: 'दक्षिण भारत में जन्म दर यूरोप जितनी कम हो चुकी है— जनसंख्या तेजी से बूढ़ी होगी।'
    },

    // CHAPTER 7 BEATS: THE ROADMAP & CITIZEN VERDICT
    {
      start_s: 525.70, end_s: 532.37,
      pos: 'center-bento',
      theme: 'mint',
      tag: 'CHAPTER 7 ANCHOR · THE 2047 REFORM BLUEPRINT',
      title: 'THE ACTIONABLE ROADMAP: HOW INDIA BECOMES TRULY RICH',
      subtitle: 'Four Non-Negotiable Structural Pillars Beyond GDP Hype',
      cells: [
        { title: 'Pillar 1', metric: 'Mass Factories', desc: 'Plug-and-play coastal industrial clusters', color: '#38bdf8' },
        { title: 'Pillar 2', metric: 'Tax Relief', desc: 'Cut GST on food & health; boost consumption', color: '#fbbf24' },
        { title: 'Pillar 3', metric: 'Agri Cold Chains', desc: '100% solar cold storage; food processing hubs', color: '#34d399' }
      ],
      verdict: 'पीआर और हेडलाइन हाइप से परे: असली सुधारों का 4-सूत्रीय मास्टर प्लान।'
    },
    {
      start_s: 572.61, end_s: 578.00,
      pos: 'top-right',
      theme: 'mint',
      tag: 'PILLAR 1 IMPLEMENTATION · MASS CLUSTERS',
      title: 'COASTAL EXPORT CLUSTERS & TARIFF CUTS',
      stats: [
        { label: 'EXPORT PROCESSING ZONES', val: 'Plug & Play Infra', sub: 'Shenzhen-Style Mega Parks', color: '#34d399' },
        { label: 'IMPORT TARIFF REFORMS', val: 'Duty Reductions', sub: 'Enable Global Supply Chain Assembly', color: '#38bdf8' }
      ],
      verdict: 'करोड़ों युवाओं को रोजगार देने के लिए बड़े तटीय औद्योगिक क्लस्टर जरूरी हैं।'
    },
    {
      start_s: 578.00, end_s: 584.20,
      pos: 'top-right',
      theme: 'amber',
      tag: 'PILLAR 2 IMPLEMENTATION · MIDDLE-CLASS RELIEF',
      title: 'RESTORE MIDDLE-CLASS DISPOSABLE INCOME',
      stats: [
        { label: 'GST RATIONALIZATION', val: '0% on Health/Life', sub: 'Remove 18% Tax on Family Protection', color: '#34d399' },
        { label: 'TAX BRACKET RELIEF', val: 'Raise Exemptions', sub: 'Boost In-Hand Household Spend', color: '#fbbf24' }
      ],
      verdict: 'बीमा और अनिवार्य वस्तुओं से टैक्स हटाकर घरेलू बचत को फिर से खड़ा करना होगा।'
    },
    {
      start_s: 584.20, end_s: 590.00,
      pos: 'top-right',
      theme: 'mint',
      tag: 'PILLAR 3 IMPLEMENTATION · AGRI VALUE CHAINS',
      title: 'COLD STORAGE & FOOD PROCESSING REVOLUTION',
      stats: [
        { label: 'FARM POST-HARVEST LOSS', val: '₹1.5 Lakh Cr saved', sub: 'Solar Cold Chain Logistics', color: '#34d399' },
        { label: 'FARMER INCOME MULTIPLIER', val: '2.5x Real Value', sub: 'Direct Consumer Processing Hubs', color: '#38bdf8' }
      ],
      verdict: 'सब्जी और फल सड़ने से बचेंगे तो किसान की आय सीधे 2.5 गुना बढ़ेगी।'
    },
    {
      start_s: 590.00, end_s: 595.50,
      pos: 'top-right',
      theme: 'cyan',
      tag: 'PILLAR 4 IMPLEMENTATION · GERMAN DUAL APPRENTICESHIP',
      title: 'TIED VOCATIONAL ITI SKILLING MODEL',
      stats: [
        { label: 'DUAL VOCATIONAL MODEL', val: 'German Standard', sub: '3 Days Factory, 2 Days Theory', color: '#38bdf8' },
        { label: 'GUARANTEED EMPLOYMENT', val: '90%+ Placement', sub: 'Direct Industrial Absorption', color: '#34d399' }
      ],
      verdict: 'केवल रद्दी डिग्रियों से नहीं, उद्योग-आधारित व्यावहारिक हुनर से रोजगार मिलेगा।'
    },
    {
      start_s: 595.50, end_s: 600.50,
      pos: 'top-right',
      theme: 'amber',
      tag: 'THE CITIZEN VERDICT · SACH · SABOOT · BEBAK',
      title: 'LOOK BEYOND THE 7.8% HEADLINE NOISE',
      stats: [
        { label: 'REAL CITIZEN QUESTION', val: 'Is My Saving Rising?', sub: 'True Yardstick of National Prosperity', color: '#fbbf24' },
        { label: 'ACCOUNTABILITY', val: 'Demand Real Jobs', sub: 'Not Subsidized Survival Dependent on Govt', color: '#34d399' }
      ],
      verdict: 'असली देशप्रेम हेडलाइन पर ताली बजाना नहीं, बल्कि व्यवस्था से सही सवाल पूछना है।'
    }
  ];

  // ---------------------------------------------------------------------------
  // RENDER ENGINE
  // ---------------------------------------------------------------------------
  function drawOverlay(ctx, t) {
    // 1. Check if one of the 7 big full-screen diagrams is active
    const isDiagramActive = (
      (t >= 64.29 && t <= 83.45) ||
      (t >= 148.53 && t <= 173.16) ||
      (t >= 185.71 && t <= 224.59) ||
      (t >= 335.95 && t <= 361.60) ||
      (t >= 365.03 && t <= 405.48) ||
      (t >= 500.18 && t <= 525.70) ||
      (t >= 532.37 && t <= 572.61) ||
      (t < 5.5) ||                     // Opening roadmap card
      (t >= 60.1 && t <= 64.3) ||      // Subscribe CTA
      (t >= 600.5)                     // Final verdict stamp
    );
    if (isDiagramActive) return; // Yield completely to full diagrams

    // 2. Find matching overlay for current time t
    let active = null;
    for (let i = 0; i < OVERLAYS.length; i++) {
      const o = OVERLAYS[i];
      if (t >= o.start_s && t < o.end_s) {
        active = o;
        break;
      }
    }
    if (!active) return;

    const elapsed = t - active.start_s;
    const remaining = active.end_s - t;

    // Smooth spring entrance (0.35s) and exit (0.25s)
    let alpha = 1.0;
    let enterOffset = 0;
    if (elapsed < 0.35) {
      const p = elapsed / 0.35;
      alpha = easeOutCubic(p);
      enterOffset = (1 - easeOutCubic(p)) * 25;
    } else if (remaining < 0.25) {
      alpha = Math.max(0, remaining / 0.25);
    }

    ctx.save();
    ctx.globalAlpha = alpha;

    // Theme color palettes
    const themes = {
      cyan: { border: 'rgba(56, 189, 248, 0.40)', tagColor: '#38bdf8', tagBg: 'rgba(56, 189, 248, 0.12)' },
      amber: { border: 'rgba(251, 191, 36, 0.40)', tagColor: '#fbbf24', tagBg: 'rgba(251, 191, 36, 0.12)' },
      crimson: { border: 'rgba(244, 63, 94, 0.40)', tagColor: '#f43f5e', tagBg: 'rgba(244, 63, 94, 0.12)' },
      mint: { border: 'rgba(52, 211, 153, 0.40)', tagColor: '#34d399', tagBg: 'rgba(52, 211, 153, 0.12)' }
    };
    const curTheme = themes[active.theme] || themes.cyan;

    // -------------------------------------------------------------------------
    // RENDER STYLE A: CENTER BENTO CARD (Major Chapter Turning Points like SS1)
    // -------------------------------------------------------------------------
    if (active.pos === 'center-bento') {
      // Soft ambient radial focus directly behind center bento, leaving perimeter and hero photo completely visible
      const bentoGrad = ctx.createRadialGradient(960, 480, 160, 960, 480, 950);
      bentoGrad.addColorStop(0, 'rgba(4, 7, 14, 0.20)');
      bentoGrad.addColorStop(1, 'rgba(4, 7, 14, 0.02)');
      ctx.fillStyle = bentoGrad;
      ctx.fillRect(0, 0, 1920, 1080);

      const cx = 960, cy = 480 + enterOffset;
      const cardW = 1180, cardH = 540;
      const x0 = cx - cardW / 2, y0 = cy - cardH / 2;

      drawGlassCard(ctx, x0, y0, cardW, cardH, 20, curTheme.border, null);

      // Top Tag Pill
      drawTagPill(ctx, active.tag, x0 + 40, y0 + 36, curTheme.tagColor, curTheme.tagBg);

      // Title & Subtitle
      ctx.fillStyle = '#ffffff';
      ctx.font = '800 28px "Outfit", "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(active.title, x0 + 40, y0 + 82);

      if (active.subtitle) {
        ctx.fillStyle = '#94a3b8';
        ctx.font = '600 15px "Inter", sans-serif';
        ctx.fillText(active.subtitle, x0 + 40, y0 + 112);
      }

      // 3 Bento Cells
      if (active.cells) {
        const cellY = y0 + 140;
        const cellW = 345, cellH = 260;
        const cellGap = 28;

        active.cells.forEach((c, idx) => {
          const cellX = x0 + 40 + idx * (cellW + cellGap);
          drawGlassCard(ctx, cellX, cellY, cellW, cellH, 14, 'rgba(255, 255, 255, 0.12)', 'rgba(10, 15, 28, 0.35)');

          // Cell Step Header
          ctx.fillStyle = c.color;
          ctx.font = '700 12px "JetBrains Mono", monospace';
          ctx.fillText(`PHASE ${idx + 1}: ${c.title.toUpperCase()}`, cellX + 22, cellY + 36);

          // Big Metric
          ctx.fillStyle = '#ffffff';
          ctx.font = '800 38px "Outfit", sans-serif';
          ctx.fillText(c.metric, cellX + 22, cellY + 92);

          // Divider
          ctx.fillStyle = 'rgba(255, 255, 255, 0.08)';
          ctx.fillRect(cellX + 22, cellY + 114, cellW - 44, 1);

          // Description
          ctx.fillStyle = '#94a3b8';
          ctx.font = '500 14px "Inter", sans-serif';
          const words = c.desc.split(' ');
          let line = '', lineY = cellY + 144;
          for (let w of words) {
            const testLine = line + w + ' ';
            if (ctx.measureText(testLine).width > cellW - 44) {
              ctx.fillText(line, cellX + 22, lineY);
              line = w + ' ';
              lineY += 22;
            } else {
              line = testLine;
            }
          }
          ctx.fillText(line, cellX + 22, lineY);
        });
      }

      // Bottom Verdict Strip
      const verdY = y0 + cardH - 64;
      ctx.fillStyle = 'rgba(255, 255, 255, 0.04)';
      ctx.strokeStyle = 'rgba(255, 255, 255, 0.08)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.roundRect(x0 + 40, verdY, cardW - 80, 42, 8);
      ctx.fill();
      ctx.stroke();

      ctx.fillStyle = curTheme.tagColor;
      ctx.font = '700 14px "JetBrains Mono", monospace';
      ctx.fillText('🔍 GROUND REALITY VERDICT:', x0 + 56, verdY + 26);

      ctx.fillStyle = '#f8fafc';
      ctx.font = '600 14px "Inter", sans-serif';
      ctx.fillText(active.verdict, x0 + 290, verdY + 26);
    }

    // -------------------------------------------------------------------------
    // RENDER STYLE B: ASYMMETRIC FLOATING HUD DATA CARDS (Upper-Right or Left)
    // -------------------------------------------------------------------------
    else {
      const cardW = 560, cardH = 210;
      let cardX = 1300, cardY = 100 + enterOffset;
      if (active.pos === 'top-left') {
        cardX = 80;
        cardY = 100 + enterOffset;
      }

      drawGlassCard(ctx, cardX, cardY, cardW, cardH, 16, curTheme.border, null);

      // Top Tag Pill
      drawTagPill(ctx, active.tag, cardX + 24, cardY + 28, curTheme.tagColor, curTheme.tagBg);

      // Card Title
      ctx.fillStyle = '#ffffff';
      ctx.font = '800 18px "Outfit", "Inter", sans-serif';
      ctx.textAlign = 'left';
      ctx.fillText(active.title, cardX + 24, cardY + 68);

      // 2 Structured Metric Columns
      if (active.stats && active.stats.length >= 2) {
        const colW = (cardW - 48 - 16) / 2;

        active.stats.forEach((st, idx) => {
          const colX = cardX + 24 + idx * (colW + 16);
          const colY = cardY + 86;

          // Mini Metric Pod
          ctx.fillStyle = 'rgba(255, 255, 255, 0.03)';
          ctx.strokeStyle = 'rgba(255, 255, 255, 0.07)';
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.roundRect(colX, colY, colW, 68, 8);
          ctx.fill();
          ctx.stroke();

          ctx.fillStyle = '#94a3b8';
          ctx.font = '700 10px "JetBrains Mono", monospace';
          ctx.fillText(st.label, colX + 12, colY + 20);

          ctx.fillStyle = st.color;
          ctx.font = '800 20px "Outfit", sans-serif';
          ctx.fillText(st.val, colX + 12, colY + 44);

          ctx.fillStyle = '#64748b';
          ctx.font = '500 10px "Inter", sans-serif';
          ctx.fillText(st.sub, colX + 12, colY + 60);
        });
      }

      // Bottom Micro-Verdict / Sach Saboot Bebak Takeaway
      ctx.fillStyle = 'rgba(255, 255, 255, 0.05)';
      ctx.fillRect(cardX + 24, cardY + 164, cardW - 48, 1);

      ctx.fillStyle = '#f8fafc';
      ctx.font = '500 12px "Inter", sans-serif';
      ctx.fillText(`• ${active.verdict}`, cardX + 24, cardY + 188);
    }

    ctx.restore();
  }

  root.ForensicOverlays = {
    drawOverlay,
    OVERLAYS
  };

})(window);
