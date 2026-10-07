// Benaqaab India — Topics & Production Registry Dataset
const PRODUCTIONS_DATA = [
  // ─── 16:9 FLAGSHIP DOCUMENTARIES ───────────────────────────────────────
  {
    code: "EP-17",
    title: "PFBR — India Ka Nuclear Miracle",
    hindiTitle: "500 MWe फास्ट ब्रीडर रिएक्टर — कल्पक्कम न्यूक्लियर क्रांति",
    category: "Science / Nuclear Infra",
    format: "16:9 Landscape",
    duration: "10m 29s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/ep17_pfbr/comp.html",
    thumbUrl: "/projects/ep17_pfbr/thumbnail_1280x720.jpg",
    gradeProfile: "Profile B (Documentary Cinema)",
    evidence: [
      "500 MWe Fast Breeder Reactor at Kalpakkam, Tamil Nadu",
      "Liquid sodium coolant at 550°C with 1.05 breeding ratio",
      "Stage 2 of Homi Bhabha 3-stage plan: unlocking 319,000 tonnes of Indian Thorium reserves",
      "105 visual beats rendered frame-by-frame from deterministic code"
    ],
    audioClock: "-14.0 LUFS · 10m 29s Master VO"
  },
  {
    code: "EP-12",
    title: "NavIC — India Ka Apna GPS",
    hindiTitle: "7 सैटेलाइट्स, L5/S बैंड और 1500 KM स्ट्रैटेजिक बफर",
    category: "Space / Tech",
    format: "16:9 Landscape",
    duration: "3m 21s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/ep12_navic/comp.html",
    thumbUrl: "/projects/ep12_navic/EP12_upload/thumbnail_1280x720.jpg",
    gradeProfile: "Profile B (Documentary Cinema)",
    evidence: [
      "7-satellite constellation (3 GEO + 4 GSO orbits)",
      "Dual frequency L5 (1176.45 MHz) + S-band (2492.028 MHz) for civilian accuracy",
      "1,500 km strategic security perimeter beyond India's borders",
      "MeitY mandate for smartphone 5G chip integration"
    ],
    audioClock: "-14.0 LUFS · 3m 21s Master VO"
  },
  {
    code: "EP-13",
    title: "Monsoon 2026 & El Niño",
    hindiTitle: "12.6% बारिश की कमी, अल नीनो व पॉजिटिव IOD का गणित",
    category: "Climate / Economy",
    format: "16:9 Landscape",
    duration: "3m 26s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/ep13_monsoon/comp.html",
    thumbUrl: "/projects/ep13_monsoon/EP13_upload/thumbnail_1280x720.jpg",
    gradeProfile: "Profile B (Documentary Cinema)",
    evidence: [
      "12.6% all-India monsoon rainfall deficit vs 50-year LPA",
      "Equatorial Pacific sea surface temperature anomaly (>+1.5°C)",
      "Mandi crop ledger: Kharif sowing delay & food price impact",
      "Positive Indian Ocean Dipole buffer analysis"
    ],
    audioClock: "-14.0 LUFS · 3m 26s Master VO"
  },
  {
    code: "EP-14",
    title: "Bullet Train 2027 (Mumbai–Ahmedabad)",
    hindiTitle: "508 KM कॉरिडोर, शिंकानसेन E10 और 21 KM ठाणे अंडरसी टनल",
    category: "Mega Infrastructure",
    format: "16:9 Landscape",
    duration: "2m 57s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/ep14_bullet/comp.html",
    thumbUrl: "/projects/ep14_bullet/EP14_upload/thumbnail_1280x720.jpg",
    gradeProfile: "Profile B (Documentary Cinema)",
    evidence: [
      "508 km high-speed rail corridor (12 stations, Gujarat & Maharashtra)",
      "Japan Shinkansen E10 series rolling stock, 320 km/h operational speed",
      "21 km undersea tunnel beneath Thane Creek (India's first)",
      "Travel time cut from 6h 30m down to 2h 07m"
    ],
    audioClock: "-14.0 LUFS · 2m 57s Master VO"
  },
  {
    code: "EP-15",
    title: "Rupee 96 vs USD — Aapki Jeb Par Asar",
    hindiTitle: "रुपया 96 के पार, क्रूड $100+ और फॉरेक्स डिफेंस की हकीकत",
    category: "Economy / Currency",
    format: "16:9 Landscape",
    duration: "3m 11s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/ep15_rupee/comp.html",
    thumbUrl: "/projects/ep15_rupee/EP15_upload/thumbnail_1280x720.jpg",
    gradeProfile: "Profile B (Documentary Cinema)",
    evidence: [
      "INR deprecation reaching ₹96.12/USD milestone",
      "Brent crude surge above $100/barrel inflating fuel import bill",
      "RBI forex reserves intervention ledger ($680B+ cushion)",
      "Direct inflation impact on electronics, edible oil, and fertilizer"
    ],
    audioClock: "-14.0 LUFS · 3m 11s Master VO"
  },
  {
    code: "EP-16",
    title: "Made-in-India Chips — Dholera & Sanand",
    hindiTitle: "धोलेरा 28nm फैब, माइक्रोन साणंद और असम OSAT सेमीकंडक्टर मिशन",
    category: "Technology / Industry",
    format: "16:9 Landscape",
    duration: "3m 47s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/ep16_chips/comp.html",
    thumbUrl: "/projects/ep16_chips/EP16_upload/thumbnail_1280x720.jpg",
    gradeProfile: "Profile B (Documentary Cinema)",
    evidence: [
      "Tata Electronics & PSMC ₹91,000 Cr fab at Dholera (28nm/40nm/55nm nodes)",
      "Micron $2.75B ATMP assembly & test plant at Sanand, Gujarat",
      "Tata Semiconductor Assembly in Morigaon, Assam (₹27,000 Cr)",
      "India Semiconductor Mission (ISM) ₹76,000 Cr PLI incentive tracking"
    ],
    audioClock: "-14.0 LUFS · 3m 47s Master VO"
  },
  {
    code: "EP-04",
    title: "Digital Arrest Exposed",
    hindiTitle: "साइबर रंगदारी, फर्जी पुलिस स्टेशन और म्यूल बैंक अकाउंट नेटवर्क",
    category: "Cyber Crime / Investigation",
    format: "16:9 Landscape",
    duration: "5m 21s",
    status: "DONE",
    isDelivered: true,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "Profile B (Forensic Investigation)",
    evidence: [
      "Fake Skype video calls masquerading as CBI / Mumbai Police / ED officers",
      "Fake court arrest warrants and RBI verification threats",
      "Multi-layered money mule bank accounts draining ₹120+ Cr",
      "Official Ministry of Home Affairs I4C helpline (1930) advisory"
    ],
    audioClock: "-14.0 LUFS · 5m 21s Master VO"
  },
  {
    code: "EP-09",
    title: "Chenab Bridge Engineering",
    hindiTitle: "दुनिया का सबसे ऊंचा रेलवे आर्च ब्रिज — 359 मीटर हवा में",
    category: "Engineering / Rail",
    format: "16:9 Landscape",
    duration: "3m 20s",
    status: "DONE",
    isDelivered: true,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "Profile B (Documentary Cinema)",
    evidence: [
      "359m height above Chenab riverbed (35m higher than Eiffel Tower)",
      "1,315m bridge span designed for 266 km/h wind velocity and Zone V earthquakes",
      "Special blast-proof 63mm steel engineered with DRDO",
      "USBRL rail connection linking Kashmir Valley to Indian Railways network"
    ],
    audioClock: "-14.0 LUFS · 3m 20s Master VO"
  },
  {
    code: "EP-10",
    title: "India's Last 24 Hours News Desk",
    hindiTitle: "रियल-टाइम न्यूज़ टिकर डेस्क और डायनेमिक क्लिप इन्सर्ट्स",
    category: "News Wire / Desk",
    format: "16:9 Landscape",
    duration: "3m 10s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/viz/recipes/ep10_comp_wiredesk.html",
    thumbUrl: "/viz/recipes/ep10_thumb_safe_16x9.html",
    gradeProfile: "Profile A (Newsroom Neutral)",
    evidence: [
      "Live multi-channel tickerboard architecture",
      "Dual-screen evidence pinboard with video clip inserts",
      "Automated stock & commodity ticker stream"
    ],
    audioClock: "-14.0 LUFS · Newsdesk Audio"
  },
  {
    code: "EP-11",
    title: "Market & Economic Tickerboard",
    hindiTitle: "डायनामिक फाइनेंशियल बोर्ड और मल्टी-एसेट काउंटर्स",
    category: "Finance / Markets",
    format: "16:9 Landscape",
    duration: "3m 05s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/viz/recipes/ep11_comp_tickerboard.html",
    thumbUrl: "/viz/recipes/ep11_thumb_16x9.html",
    gradeProfile: "Profile A (Newsroom Neutral)",
    evidence: [
      "BSE Sensex / Nifty 50 real-time composite counters",
      "Bond yields (10-year G-Sec) & currency parity charts",
      "Odometer rolling data visualization engine"
    ],
    audioClock: "-14.0 LUFS · Market Audio"
  },

  // ─── 9:16 YOUTUBE SHORTS ───────────────────────────────────────────────
  {
    code: "SH-08",
    title: "Sona ₹1.5 Lakh: Asli Showroom Bill",
    hindiTitle: "₹1,50,280 स्पॉट बनाम ₹1,85,000+ का असली शोरूम बिल",
    category: "Personal Finance",
    format: "9:16 Vertical Short",
    duration: "54s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/gold_150k/comp.html",
    thumbUrl: "/projects/gold_150k/thumbnail_1080x1920.jpg",
    gradeProfile: "Profile A (Neutral High-Contrast)",
    evidence: [
      "₹1,50,280 spot gold price for 24K pure bullion",
      "+3% GST mandatory charge on entire invoice",
      "12% to 18% making charges + wastage calculation",
      "Final showroom retail price exceeds ₹1,85,000 vs Gold ETF alternative"
    ],
    audioClock: "-14.0 LUFS · 53.90s Voiceover Clock"
  },
  {
    code: "SH-09",
    title: "India Last 24 Hours: 4 Badi Khabrein",
    hindiTitle: "14 सीन्स, DRI सोना ज़ब्ती, ECI तारीखें, SEBI SME IPO क्रैकडाउन",
    category: "Daily News Intelligence",
    format: "9:16 Vertical Short",
    duration: "1m 58s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/india_last_24h/comp.html",
    thumbUrl: "/projects/india_last_24h/thumbnail_1280x720.jpg",
    gradeProfile: "Profile A (Neutral High-Contrast)",
    evidence: [
      "14 dynamic scenes with DRI, ECI, PIB, NCS, BCCI official evidence cards",
      "Air Chief AP Singh statement on border readiness",
      "SEBI circular cracking down on inflated SME IPO listings",
      "Timed Hinglish narration synchronized to word-level audio timestamps"
    ],
    audioClock: "-14.0 LUFS · 118.07s Voiceover Clock"
  },
  {
    code: "SH-11",
    title: "World News 24 Hours: 5 Global Developments",
    hindiTitle: "जर्मनी BND गिरफ्तारी, फ्रांस प्रदर्शन, केन्या इबोला, फिजिक्स नोबेल",
    category: "World Geopolitics",
    format: "9:16 Vertical Short",
    duration: "58s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/world_news_24h/preview.html",
    thumbUrl: "/projects/world_news_24h/thumbnail_1280x720.jpg",
    gradeProfile: "Profile A (Neutral High-Contrast)",
    evidence: [
      "Germany BND foreign intelligence espionage arrest",
      "France nationwide student & teacher budget protests",
      "Kenya isolated Ebola hemorrhagic fever case containment",
      "Physics Nobel Prize announcement for neutrino astronomy (Halzen IceCube)",
      "Official spoken closing: 'Shor nahi, source ke saath'"
    ],
    audioClock: "-14.0 LUFS · 58.00s Voiceover Clock"
  },
  {
    code: "SH-10",
    title: "India–Japan JCM: Carbon Credits Kise Milenge?",
    hindiTitle: "आर्टिकल 6.2 पेरिस समझौता, द्विपक्षीय कार्बन क्रेडिट्स का सच",
    category: "Climate & Geopolitics",
    format: "9:16 Vertical Short",
    duration: "1m 47s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/india_japan_jcm/comp.html",
    thumbUrl: "/projects/india_japan_jcm/india_japan_jcm_short_thumbnail.jpg",
    gradeProfile: "Profile A (Neutral High-Contrast)",
    evidence: [
      "Article 6.2 bilateral Joint Crediting Mechanism signed between New Delhi & Tokyo",
      "Mandatory 'Corresponding Adjustments' mechanism preventing double counting",
      "High-efficiency industrial decarbonization project funding in India",
      "Verification ledger under UN Framework Convention on Climate Change"
    ],
    audioClock: "-14.0 LUFS · 107s Voiceover Clock"
  },
  {
    code: "SH-07",
    title: "Voter List Mein Naam Missing? (SIR 2026)",
    hindiTitle: "वोटर लिस्ट स्पेशल रिवीजन 2026 — फॉर्म 6/7/8 और सुप्रीम कोर्ट",
    category: "Civic Rights / Law",
    format: "9:16 Vertical Short",
    duration: "1m 41s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/voter_list_sir/comp.html",
    thumbUrl: null,
    gradeProfile: "Profile A (Civic Neutral)",
    evidence: [
      "2026 Special Intensive Revision (SIR) electoral roll verification",
      "Form 6 (new registration), Form 7 (objection/deletion), Form 8 (correction)",
      "Supreme Court bench notice on wrongful bulk voter name deletions",
      "Live portal guide on checking NVSP / voters.eci.gov.in"
    ],
    audioClock: "-14.0 LUFS · 101s Voiceover Clock"
  },
  {
    code: "SH-06",
    title: "UPI: How India Moves ₹314 Lakh Cr",
    hindiTitle: "4-पार्टी मॉडल, 3,729 TPS और ज़ीरो-MDR बैंकिंग स्विच आर्किटेक्चर",
    category: "Fintech Infrastructure",
    format: "9:16 Vertical Short",
    duration: "55s",
    status: "DONE",
    isDelivered: true,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "Profile A (Fintech Clean)",
    evidence: [
      "₹314 Lakh Crore annual volume handled by NPCI switch",
      "Peak throughput hitting 3,729 transactions per second (TPS)",
      "Four-party settlement model: Remitter, Issuer bank, Beneficiary bank, PSP app",
      "Zero-MDR policy mechanism and interchange subsidy"
    ],
    audioClock: "-14.0 LUFS · 55s Voiceover Clock"
  },
  {
    code: "SH-01",
    title: "Neon Blade",
    hindiTitle: "साइबरपंक कटाना और नियॉन बारिश — बीट-सिंक काइनेटिक एडिट",
    category: "Kinetic Motion Edit",
    format: "9:16 Vertical Short",
    duration: "47s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/anime_edit_01/comp.html",
    thumbUrl: "/projects/anime_edit_01/NEON_upload/thumb_1080x1920.jpg",
    gradeProfile: "Profile C (Stylized Cinema)",
    evidence: [
      "Procedural neon rain reflection rendering on HTML5 Canvas",
      "Sub-frame audio beat-sync triggers calibrated to BEATS.json",
      "Pure vector sword glints and volumetric chromatic aberration"
    ],
    audioClock: "135 BPM Beat-Synchronized Audio"
  },
  {
    code: "SH-02",
    title: "Laal Chaand",
    hindiTitle: "क्रिमसन मून, चेरी ब्लॉसम ड्रिफ्ट और सामुराई विज़ुअल रिदम",
    category: "Kinetic Motion Edit",
    format: "9:16 Vertical Short",
    duration: "48s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/anime_edit_02/comp.html",
    thumbUrl: "/projects/anime_edit_02/LAAL_upload/thumb_1080x1920.jpg",
    gradeProfile: "Profile C (Stylized Cinema)",
    evidence: [
      "Procedural sakura petal physics with turbulent wind drift",
      "Deep crimson chromatic moon displacement shaders",
      "Kinetic speed ramp transitions at 60 FPS"
    ],
    audioClock: "128 BPM Beat-Synchronized Audio"
  },
  {
    code: "SH-03",
    title: "Safed Raat",
    hindiTitle: "बर्फ़ीला तूफ़ान और आर्कटिक नॉर्दर्न सी रूट की जियोपॉलिटिक्स",
    category: "Kinetic Motion Edit",
    format: "9:16 Vertical Short",
    duration: "53s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/anime_edit_03/comp.html",
    thumbUrl: "/projects/anime_edit_03/SAFED_upload/thumb_1080x1920.jpg",
    gradeProfile: "Profile C (Stylized Cinema)",
    evidence: [
      "Dynamic procedural snow particle engine with virtual camera shake",
      "Geopolitical icebreaker maritime shipping transit map",
      "Glacial blue color grading with high-contrast HUD overlays"
    ],
    audioClock: "130 BPM Beat-Synchronized Audio"
  },

  // ─── RAPID RESPONSE & FORENSIC EXPOSES ─────────────────────────────────
  {
    code: "FL-04",
    title: "Flight Surcharge: IndiGo ATF Hike",
    hindiTitle: "एविएशन टरबाइन फ्यूल +14% उछाल और ₹11,300 तक सरचार्ज स्लैब",
    category: "Aviation / Consumer Rights",
    format: "9:16 Vertical Short",
    duration: "2m 56s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/flight_surcharge/Flight_Surcharge_Short.html",
    thumbUrl: "/projects/flight_surcharge/thumbnail_1280x720.jpg",
    gradeProfile: "Profile B (Forensic Investigation)",
    evidence: [
      "ATF (Aviation Turbine Fuel) domestic price +14% sharp increase",
      "Distance-based fuel surcharge tiers ranging from ₹1,375 to ₹11,300",
      "DGCA notification reference and airline dynamic pricing breakdown",
      "Brent crude >$100 pass-through mechanism onto passenger ticket bills"
    ],
    audioClock: "-14.0 LUFS · 176s Voiceover Clock"
  },
  {
    code: "FL-05",
    title: "Kagaz Ki Machine: Teen Scams, Ek Hi Model",
    hindiTitle: "₹734 करोड़ का फर्जी GST ITC रैकेट, 135 फर्जी फर्में और स्क्रैप बिल",
    category: "Financial Crime Docu",
    format: "16:9 Landscape",
    duration: "12m 40s",
    status: "DONE",
    isDelivered: true,
    hasComp: false,
    previewUrl: null,
    thumbUrl: "/projects/kagaz_ki_machine/thumbnail_curiosity_text_1280x720.png",
    gradeProfile: "Profile B (Forensic Investigation)",
    evidence: [
      "₹734 Crore fake Input Tax Credit (ITC) syndicate busted by ED & DGGI",
      "135 shell companies registered on forged Aadhaar & electricity bills",
      "Circular scrap paper and brass billing without actual physical transport",
      "Money laundering chain mapping to real estate and bullion purchases"
    ],
    audioClock: "-14.0 LUFS · 12m 40s Master Audio"
  },
  {
    code: "FL-06",
    title: "Hugging Face AI Model Supply Chain Hack",
    hindiTitle: "पायथन पिकल डेसीरियलाइजेशन बग और 100+ हाईजैक मॉडल वेट्स",
    category: "AI Security / Tech",
    format: "16:9 Landscape",
    duration: "4m 12s",
    status: "DONE",
    isDelivered: true,
    hasComp: true,
    previewUrl: "/projects/ai_hf_hack/film.html",
    thumbUrl: "/projects/ai_hf_hack/thumbnail.jpg",
    gradeProfile: "Profile B (Forensic Tech)",
    evidence: [
      "Python Pickle deserialization vulnerability allowing arbitrary code execution",
      "100+ public Hugging Face model repositories poisoned with malicious payloads",
      "Automated reverse shell triggers upon model download and evaluation",
      "Industry push towards SafeTensors format adoption"
    ],
    audioClock: "-14.0 LUFS · 4m 12s Master Audio"
  },

  // ─── TIME-CRITICAL LIVE CYCLES (OCTOBER 2026) ──────────────────────────
  {
    code: "LC-01",
    title: "RBI Rate Decision & Your EMI",
    hindiTitle: "कमजोर मानसून से महंगाई, रेपो रेट 5.50% और ₹50 लाख लोन पर झटका",
    category: "Economy / Personal Finance",
    format: "9:16 Vertical Short",
    duration: "~2m 15s",
    status: "LIVE_CYCLE",
    isDelivered: false,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "Profile A (Financial Neutral)",
    evidence: [
      "Weak monsoon (12.6% deficit) triggered mandi food price inflation (CPI 4.82%)",
      "Brent crude above $100 & Rupee near ₹96/USD pushing imported inflation",
      "RBI MPC expected +25 bps hike pushing repo rate from 5.25% to 5.50%",
      "Direct home loan EMI impact: ₹50 lakh loan monthly EMI rises by ₹775–₹820"
    ],
    audioClock: "Script Ready · Ready to Produce"
  },
  {
    code: "LC-02",
    title: "Census 2027 — World's First Fully Digital Census",
    hindiTitle: "15 साल बाद पहली डिजिटल जनगणना, मोबाइल सेल्फ-एन्यूमरेशन व जाति गणना",
    category: "Civic / Mega-Project",
    format: "16:9 Landscape",
    duration: "~3m 45s",
    status: "LIVE_CYCLE",
    isDelivered: false,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "Profile B (Documentary Cinema)",
    evidence: [
      "15-year gap since Census 2011; first all-digital execution",
      "Mobile self-enumeration portal (se.census.gov.in) with 16-digit ID",
      "₹11,718.24 Crore approved budget across 3.4 Million field enumerators",
      "Historic inclusion of caste enumeration after 95 years (since 1931)"
    ],
    audioClock: "Fact Ledger Locked · Ready to Produce"
  },
  {
    code: "LC-03",
    title: "Gaganyaan — Vyommitra Robot Astronaut",
    hindiTitle: "इंसान से पहले अंतरिक्ष जाएगी रोबोट व्योममित्र — इसरो का अनक्रूड मिशन",
    category: "Space / Science",
    format: "9:16 Vertical Short",
    duration: "~1m 50s",
    status: "LIVE_CYCLE",
    isDelivered: false,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "Profile B (Space Docu)",
    evidence: [
      "ISRO G1 uncrewed test flight carrying female humanoid robot 'Vyommitra'",
      "Monitoring cabin pressure, oxygen levels, g-forces, and capsule orientation",
      "Crew Escape System (CES) validation at 400 km Low Earth Orbit",
      "Pathfinder for 2027 crewed Indian astronaut spaceflight"
    ],
    audioClock: "Research Verified · Ready to Produce"
  },

  // ─── HIGH PRIORITY RESEARCHED BACKLOG ──────────────────────────────────
  {
    code: "BL-01",
    title: "National Green Hydrogen Mission",
    hindiTitle: "₹19,744 करोड़ का PLI इंसेंटिव — क्या 2030 तक ग्रीन फ्यूल सस्ता होगा?",
    category: "Clean Tech / Energy",
    format: "16:9 Landscape",
    duration: "~3m 30s",
    status: "BACKLOG",
    isDelivered: false,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "Profile B (Industrial Tech)",
    evidence: [
      "₹19,744 Cr mission budget targeting 5 MMT annual green hydrogen by 2030",
      "Electrolyzer manufacturing incentives (₹4,440 Cr SIGHT scheme)",
      "Production cost transition from $4-5/kg down to competitive $1-2/kg target",
      "Heavy industry adoption mandate: steel, refinery, and ammonia fertilizer"
    ],
    audioClock: "Researched Backlog"
  },
  {
    code: "BL-02",
    title: "Samudrayaan MATSYA 6000",
    hindiTitle: "6000 मीटर गहरे समुद्र में भारत की पनडुब्बी — रेयर मिनरल्स का खजाना",
    category: "Deep Sea / Science",
    format: "16:9 Landscape",
    duration: "~3m 15s",
    status: "BACKLOG",
    isDelivered: false,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "Profile B (Oceanic Deep)",
    evidence: [
      "Titanium alloy 80mm hull engineered for 600 bar hydrostatic pressure",
      "Exploration of Polymetallic Nodules: Nickel, Cobalt, Manganese in Indian Ocean",
      "3-person scientific crew life-support envelope for 72 hours emergency",
      "Developed by National Institute of Ocean Technology (NIOT), Chennai"
    ],
    audioClock: "Researched Backlog"
  },
  {
    code: "BL-03",
    title: "Jammu Lithium Reserve & Auction",
    hindiTitle: "रियासी में 5.9 मिलियन टन लिथियम — खनन और बैटरी मैन्युफैक्चरिंग का सच",
    category: "Mining / Economy",
    format: "9:16 Vertical Short",
    duration: "~1m 55s",
    status: "BACKLOG",
    isDelivered: false,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "Profile A (Economic Investigation)",
    evidence: [
      "GSI (Geological Survey of India) identified 5.9 Million Tonnes G3 reserve in Salal-Haimana, Reasi",
      "Composite license auction parameters and critical mineral classification",
      "Refining hurdles: hard-rock clay extraction vs South American brine extraction",
      "Direct domestic electric vehicle battery cell manufacturing impact"
    ],
    audioClock: "Researched Backlog"
  },

  // ─── PERMANENT BLACKLIST (NEVER TOUCH) ──────────────────────────────────
  {
    code: "BK-01",
    title: "Shootspace / GIFT City Cloud-Storage Ponzi",
    hindiTitle: "गिफ़्ट सिटी के नाम पर फर्जी क्लाउड स्टोरेज पोंजी स्कीम",
    category: "Blacklisted Scheme",
    format: "Prohibited",
    duration: "BLOCKED",
    status: "BLACKLIST",
    isDelivered: false,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "N/A",
    evidence: ["Permanently Blacklisted under RULE-NO-REPEAT and editorial policy."],
    audioClock: "PROHIBITED"
  },
  {
    code: "BK-02",
    title: "Task-Based Telegram Part-Time Job Scam",
    hindiTitle: "टेलीग्राम लाइक/रिव्यू टास्क और प्रीपेड क्रिप्टो वॉलेट फ्रॉड",
    category: "Blacklisted Scheme",
    format: "Prohibited",
    duration: "BLOCKED",
    status: "BLACKLIST",
    isDelivered: false,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "N/A",
    evidence: ["Covered extensively in early pilots. Never repeat."],
    audioClock: "PROHIBITED"
  },
  {
    code: "BK-03",
    title: "Generic AI Voice-Cloning Deepfake Scam",
    hindiTitle: "बिना नए डेटा के जेनेरिक AI वॉयस क्लोनिंग अवेयरनेस",
    category: "Blacklisted Scheme",
    format: "Prohibited",
    duration: "BLOCKED",
    status: "BLACKLIST",
    isDelivered: false,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "N/A",
    evidence: ["Blacklisted unless new state-sponsored forensic interception data is present."],
    audioClock: "PROHIBITED"
  },
  {
    code: "BK-04",
    title: "Generic Delhi Smog & Pollution Overview",
    hindiTitle: "बिना थर्मल इन्वर्जन सैटेलाइट डेटा के पुरानी पराली बहस",
    category: "Blacklisted Topic",
    format: "Prohibited",
    duration: "BLOCKED",
    status: "BLACKLIST",
    isDelivered: false,
    hasComp: false,
    previewUrl: null,
    thumbUrl: null,
    gradeProfile: "N/A",
    evidence: ["Fully covered in EP-06. Strictly forbidden from re-explaining."],
    audioClock: "PROHIBITED"
  }
];
