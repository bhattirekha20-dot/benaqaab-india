/**
 * BENAQAAB OS — Master Intelligence Database
 * Centralized registry of all productions, vetted topics, media assets, and QA standards.
 */

const BENAQAAB_DATABASE = {
  channel: {
    name: "Benaqaab India",
    motto: "SACH · SABOOT · BEBAK",
    category: "Investigative Explainers & Visual Journalism",
    location: "Jammu, Jammu & Kashmir, India",
    established: "2026",
    standards: {
      lufs: -14.0,
      lraMax: 5.0,
      fps: 30,
      aspectShort: "9:16 (1080x1920)",
      aspectDocu: "16:9 (1920x1080 / 1280x720)",
      maxShortDuration: "60s (Strict)",
      maxDocuDuration: "3m30s - 5m00s"
    }
  },

  // 1. All Registered Channel Productions
  productions: [
    {
      id: "SH-08",
      serial: "SH-08",
      title: "Sona ₹1.5 Lakh: Asli Showroom Bill",
      format: "Shorts (9:16)",
      duration: "53.9s",
      category: "Personal Finance",
      status: "Delivered",
      date: "2026-10-06",
      videoFile: "../VIDEOS/09_Sona_150k_Bill_SHORT_54s.mp4",
      projectPath: "projects/gold_150k/",
      htmlComp: "../projects/gold_150k/comp.html",
      thumbnailCuriosity: "../projects/gold_150k/thumbnail_curiosity_text_1080x1920.jpg",
      thumbnailClean: "../projects/gold_150k/thumbnail_clean_base_1080x1920.jpg",
      thumbnailLandscape: "../projects/gold_150k/thumbnail_curiosity_text_1280x720.jpg",
      lufs: -15.1,
      hook: "Sona 1.5 lakh par pahunch gaya — par showroom mein aap kitna dete hain?",
      sources: ["IBJA Daily Bullion", "CBIC GST Schedule IV (3%)", "GJC Making Charge Survey", "BIS HUID Registry"],
      description: "24K base rate vs 22K jewelry reality: +3% GST, +15% making charges, +3% wastage. Physical Gold total ₹1.82L vs Gold ETF ₹1.50L pure cost.",
      viewsEstimate: "New Release",
      qaScore: 100
    },
    {
      id: "SH-07",
      serial: "SH-07",
      title: "Voter List Mein Naam Missing? (SIR Controversy)",
      format: "Shorts (9:16)",
      duration: "101.4s",
      category: "Civic / Governance",
      status: "Delivered",
      date: "2026-10-06",
      videoFile: "",
      projectPath: "projects/voter_list_sir/",
      htmlComp: "../projects/voter_list_sir/comp.html",
      thumbnailCuriosity: "../projects/voter_list_sir/thumbnail_ai_generated.png",
      thumbnailClean: "../projects/voter_list_sir/thumbnail_ai_generated.png",
      lufs: -14.6,
      hook: "Voter list se 13 crore naam gayab hone ki khabar? Janie Special Intensive Revision ka sach.",
      sources: ["ECI Press Note (26 Sep 2026)", "Supreme Court Hearing (5 Oct 2026)", "Indian Express Investigation"],
      description: "Draft rolls vs final deletions explained: Form 6 declaration dispute, 14 internal objections, and voter verification steps.",
      viewsEstimate: "Ready to Upload",
      qaScore: 98
    },
    {
      id: "FL-04",
      serial: "FL-04",
      title: "Flight Surcharge: IndiGo ATF Fuel Hike",
      format: "Film (16:9)",
      duration: "2m 56s",
      category: "Aviation / Economy",
      status: "Delivered",
      date: "2026-10-05",
      videoFile: "../projects/flight_surcharge/Flight_Surcharge_Short.mp4",
      projectPath: "projects/flight_surcharge/",
      htmlComp: "",
      thumbnailCuriosity: "../projects/flight_surcharge/thumbnail_1280x720.jpg",
      thumbnailClean: "../projects/flight_surcharge/thumbnail_1080x1920.jpg",
      lufs: -14.2,
      hook: "Kerosene 14% mehnga hua aur flight ticket ₹11,300 tak chad gayi.",
      sources: ["IOCL Aviation Fuel Tariff", "DGCA Circular", "Brent Crude Index ($101/bbl)"],
      description: "Aviation Turbine Fuel price shock, distance tiers from ₹1,375 to ₹11,300, and crude oil compounding math.",
      viewsEstimate: "45K",
      qaScore: 97
    },
    {
      id: "EP-16",
      serial: "EP-16",
      title: "Made-in-India Chips: 5 of 12 Live",
      format: "Docu (16:9)",
      duration: "3m 47s",
      category: "Semiconductors / Tech",
      status: "Delivered",
      date: "2026-10-04",
      videoFile: "../VIDEOS/05_Made_in_India_Chips_3m47s.mp4",
      projectPath: "projects/ep16_chips/",
      htmlComp: "",
      thumbnailCuriosity: "../brand/ref_investigative_1.png",
      thumbnailClean: "../brand/ref_investigative_1.png",
      lufs: -14.0,
      hook: "Silicon sovereignty: Bharat me pehla microchip kab ban kar niklega?",
      sources: ["India Semiconductor Mission (ISM)", "Tata Electronics Dholera Fab", "Micron Sanand ATMP"],
      description: "Dholera 28nm fab, Sanand packaging plant, Assam OSAT, and the global $1.2T chip supply chain race.",
      viewsEstimate: "112K",
      qaScore: 100
    },
    {
      id: "EP-15",
      serial: "EP-15",
      title: "Rupee 96 vs USD: Aapki Jeb Par Asar",
      format: "Docu (16:9)",
      duration: "3m 11s",
      category: "Macro Economy",
      status: "Delivered",
      date: "2026-10-03",
      videoFile: "../VIDEOS/04_Rupee_96_3m11s.mp4",
      projectPath: "projects/ep15_rupee/",
      htmlComp: "",
      thumbnailCuriosity: "../brand/ref_investigative_2.png",
      thumbnailClean: "../brand/ref_investigative_2.png",
      lufs: -14.1,
      hook: "Dollar jab 96 par pahunchta hai, toh Bharat ke crude bill par kya asar hota hai?",
      sources: ["RBI Monthly Bulletin", "US Federal Reserve", "Ministry of Commerce Data"],
      description: "Imported inflation, crude oil trade deficit, foreign exchange reserve buffers, and consumer electronics price hikes.",
      viewsEstimate: "89K",
      qaScore: 99
    },
    {
      id: "EP-14",
      serial: "EP-14",
      title: "Bullet Train 2027: Undersea Tunnel",
      format: "Docu (16:9)",
      duration: "2m 57s",
      category: "Infrastructure",
      status: "Delivered",
      date: "2026-10-02",
      videoFile: "../VIDEOS/03_Bullet_Train_2m57s.mp4",
      projectPath: "projects/ep14_bullet/",
      htmlComp: "",
      thumbnailCuriosity: "../brand/ref_investigative_3.png",
      thumbnailClean: "../brand/ref_investigative_3.png",
      lufs: -14.0,
      hook: "Samundar ke 21 meter niche 350 km/h ki raftaar: Thane Creek tunnel ka sach.",
      sources: ["NHSRCL Official Project Ledger", "JICA Bilateral Report", "Ministry of Railways"],
      description: "508 km Mumbai-Ahmedabad bullet train corridor, 21km Thane Creek undersea tunnel, and ballastless track technology.",
      viewsEstimate: "154K",
      qaScore: 100
    },
    {
      id: "EP-13",
      serial: "EP-13",
      title: "Monsoon 2026 & El Niño Deficit",
      format: "Docu (16:9)",
      duration: "3m 26s",
      category: "Science / Climate",
      status: "Delivered",
      date: "2026-10-01",
      videoFile: "../VIDEOS/02_Monsoon_ElNino_3m26s.mp4",
      projectPath: "projects/ep13_monsoon/",
      htmlComp: "",
      thumbnailCuriosity: "../brand/reference_minimal_fullscreen.png",
      thumbnailClean: "../brand/reference_minimal_fullscreen.png",
      lufs: -14.4,
      hook: "12.6% barish ki kami aur mandi mein gehu ke daam: El Niño ka chakra.",
      sources: ["IMD Monsoon End-of-Season Report", "NOAA Climate Prediction Center", "Ministry of Agriculture"],
      description: "Indian Ocean Dipole vs Pacific warming, reservoir water storage data, and kharif crop output projections.",
      viewsEstimate: "67K",
      qaScore: 98
    },
    {
      id: "EP-12",
      serial: "EP-12",
      title: "NavIC: India Ka Apna GPS",
      format: "Docu (16:9)",
      duration: "3m 21s",
      category: "Space / Defense",
      status: "Delivered",
      date: "2026-09-30",
      videoFile: "../VIDEOS/01_NavIC_3m21s.mp4",
      projectPath: "projects/ep12_navic/",
      htmlComp: "",
      thumbnailCuriosity: "../brand/ref_investigative_1.png",
      thumbnailClean: "../brand/ref_investigative_1.png",
      lufs: -14.0,
      hook: "Kargil yudh me jab America ne GPS band kiya, tab ISRO ne kya faisla liya?",
      sources: ["ISRO Satellite Centre (URSC)", "DoT Mandate Guidelines", "ITU Frequency Registration"],
      description: "7 constellation satellites, L5 and S-band frequencies, 1500km border sovereign coverage, and civilian smartphone integration.",
      viewsEstimate: "240K",
      qaScore: 100
    },
    {
      id: "SH-01",
      serial: "SH-01",
      title: "Neon Blade",
      format: "Shorts (9:16)",
      duration: "47s",
      category: "Anime / Motion Lab",
      status: "Delivered",
      date: "2026-09-28",
      videoFile: "../VIDEOS/06_Neon_Blade_SHORT_47s.mp4",
      projectPath: "projects/anime_edit_01/",
      htmlComp: "",
      thumbnailCuriosity: "",
      thumbnailClean: "",
      lufs: -14.0,
      hook: "Cyberpunk kinetic choreography benchmark.",
      sources: ["Benaqaab Motion Engine V2"],
      description: "Kinetic typography, high-velocity camera shake, neon blade combat rendering at 60fps.",
      viewsEstimate: "31K",
      qaScore: 96
    },
    {
      id: "SH-02",
      serial: "SH-02",
      title: "Laal Chaand",
      format: "Shorts (9:16)",
      duration: "48s",
      category: "Anime / Motion Lab",
      status: "Delivered",
      date: "2026-09-28",
      videoFile: "../VIDEOS/07_Laal_Chaand_SHORT_48s.mp4",
      projectPath: "projects/anime_edit_02/",
      htmlComp: "",
      thumbnailCuriosity: "",
      thumbnailClean: "",
      lufs: -14.2,
      hook: "Crimson blood moon choreography test.",
      sources: ["Benaqaab Motion Engine V2"],
      description: "Oni mask spatial depth, blossom vector dynamics, and high-contrast color grading.",
      viewsEstimate: "28K",
      qaScore: 95
    },
    {
      id: "SH-03",
      serial: "SH-03",
      title: "Safed Raat",
      format: "Shorts (9:16)",
      duration: "53s",
      category: "Anime / Motion Lab",
      status: "Delivered",
      date: "2026-09-28",
      videoFile: "../VIDEOS/08_Safed_Raat_SHORT_53s.mp4",
      projectPath: "projects/anime_edit_03/",
      htmlComp: "",
      thumbnailCuriosity: "",
      thumbnailClean: "",
      lufs: -14.1,
      hook: "Blizzard particle physics and frost simulation.",
      sources: ["Benaqaab Motion Engine V2"],
      description: "Snow particle emitters, smooth camera dollies, and high-frequency sound integration.",
      viewsEstimate: "34K",
      qaScore: 96
    }
  ],

  // 2. Master Topic Pipeline & Intelligence Matrix
  topics: [
    {
      id: "TOPIC-01",
      title: "RBI Rate Decision & Your EMI",
      category: "Economy / Personal Finance",
      priority: "TIME-CRITICAL",
      urgencyBadge: "Decision Date: 7 Oct 2026",
      certainty: "High Confidence",
      hook: "Kal aapki home loan EMI badh sakti hai — aur iska bada kaaran hai monsoon.",
      angle: "Monsoon deficit (12.6%) ➔ Food mandi inflation ➔ August CPI 4.82% ➔ Crude >$100 ➔ Rupee at 96 ➔ RBI Repo Rate Hike lever.",
      verifiedData: [
        "Current Repo Rate: 5.25% (steady for 4 reviews)",
        "Expected Move: +25 bps to 5.50% (Reuters poll 35 of 61 economists)",
        "First rate hike since February 2023"
      ],
      sources: ["RBI Monetary Policy Committee (MPC)", "Reuters Economist Consensus", "Ministry of Statistics (MoSPI)"],
      formatTarget: "Short (9:16) & Longform (16:9)",
      status: "Ready to Build"
    },
    {
      id: "TOPIC-02",
      title: "Plastic ₹10/₹20 Notes & Global UPI: India Ka Money Future?",
      category: "Currency / Digital Infrastructure",
      priority: "HIGH PRIORITY",
      urgencyBadge: "RBI August Bulletin Spine",
      certainty: "Confirmed / High Confidence",
      hook: "Paper notes phat jaate hain, par kya plastic note aur UPI physical cash ko hamesha ke liye badal denge?",
      angle: "Dual-rail future: Polymer note durability for lower denominations + UPI expansion across 11 foreign nations.",
      verifiedData: [
        "NPCI Sep 2026: 756 live banks, 24,068M transactions, ₹29.37 Lakh Crore",
        "UPI live in 11 countries for merchant QR and remittances",
        "Polymer trial: ₹10 notes field trials in 5 cities for longevity"
      ],
      sources: ["RBI Annual Report & Bulletin", "NPCI Official Product Statistics", "PIB Press Release"],
      formatTarget: "Docu Explainer (16:9 · 3m30s)",
      status: "Ready to Build"
    },
    {
      id: "TOPIC-03",
      title: "SIM Box Racket: Foreign Calls Disguised as Local",
      category: "Cyber Crime / Telephony",
      priority: "HIGH PRIORITY",
      urgencyBadge: "Active DoT Raids",
      certainty: "Verified Police Chargesheets",
      hook: "Aapko lagta hai phone call Delhi se aa raha hai, par criminal baitha hai Dubai mein.",
      angle: "How VoIP gateways bypass official international landing stations via unverified local SIM cards.",
      verifiedData: [
        "1 SIM Box holds 64 to 512 active SIM cards",
        "Government loses ₹0.30 per minute international termination fee",
        "Used extensively for Digital Arrest & customs extortion scams"
      ],
      sources: ["DoT (Department of Telecommunications)", "Delhi & Cyberabad Cyber Police", "TRAI Security Directives"],
      formatTarget: "Shorts (9:16 · 55s)",
      status: "Ready to Build"
    },
    {
      id: "TOPIC-04",
      title: "Reasi Lithium: 5.9 Million Tonnes Reality Check",
      category: "Mining / Clean Tech",
      priority: "EVERGREEN",
      urgencyBadge: "GSI Mineral Auction Phase",
      certainty: "GSI Inferred (G3 Stage)",
      hook: "Jammu ke Reasi mein mila 59 lakh tonne safed sona — par battery banne mein kitne saal lagenge?",
      angle: "G3 inferred reserves vs commercial extraction: hard rock spodumene processing, environmental clearance & refining tech.",
      verifiedData: [
        "GSI estimated 5.9 million tonnes G3 inferred lithium ore",
        "Lithium concentration: ~800 to 1,000 ppm",
        "India imported ₹33,000 Crore worth of lithium-ion batteries in 2025"
      ],
      sources: ["Geological Survey of India (GSI)", "Ministry of Mines Auction Notice", "Council on Energy, Environment and Water (CEEW)"],
      formatTarget: "Docu Explainer (16:9 · 3m45s)",
      status: "Research Completed"
    },
    {
      id: "TOPIC-05",
      title: "Train Kavach 4.0: Automatic Braking Architecture",
      category: "Railway Safety / Engineering",
      priority: "EVERGREEN",
      urgencyBadge: "National Rollout 2026-27",
      certainty: "RDSO Verified Specifications",
      hook: "Do train ek hi track par 130 km/h ki raftaar se aati hain — bina driver ke brake kaise lagta hai?",
      angle: "RFID tags on sleepers, UHF radio towers, train locomotive cab computer & SIL-4 safety certification.",
      verifiedData: [
        "Kavach 4.0 approved by RDSO (Research Designs and Standards Organisation)",
        "Over 10,000 locomotives to be retrofitted",
        "Braking distance auto-calculated within 0.1 seconds"
      ],
      sources: ["Ministry of Railways Whitepaper", "RDSO Kavach 4.0 Specification", "Indian Railways Board"],
      formatTarget: "Shorts (9:16 · 58s)",
      status: "Research Completed"
    },
    {
      id: "TOPIC-06",
      title: "IPO Grey Market Premium (GMP) Trap",
      category: "Personal Finance / Market Scams",
      priority: "INVESTIGATIVE",
      urgencyBadge: "SEBI Warning Circulars",
      certainty: "SEBI Documented",
      hook: "IPO aane se pehle 80% GMP dikha kar retailers ko kaise fasaate hain?",
      angle: "Unregulated dabba market trading, circular syndicate trades, and listing day dump mechanisms.",
      verifiedData: [
        "GMP has zero SEBI legal standing or regulatory oversight",
        "Over 65% of high-GMP hype IPOs trade below listing price after 6 months",
        "Kotak & NSE retail loss surveys"
      ],
      sources: ["SEBI Investor Protection Circular", "NSE Investor Grievance Cell", "RBI Financial Stability Report"],
      formatTarget: "Shorts (9:16 · 54s)",
      status: "Ideation"
    }
  ],

  // 3. Forensic QA Audit Standards (10-Point Production Matrix)
  qaMatrix: [
    {
      id: "Q1",
      title: "Audio Loudness Calibration",
      standard: "-14 LUFS Integrated (±1 LU), True Peak <= -1.0 dBFS",
      check: "No clipping, loudnorm filter applied, voice master clock.",
      weight: 10
    },
    {
      id: "Q2",
      title: "Frame-0 Retention Hook",
      standard: "Concrete subject / conflict communicated under 1.0 second",
      check: "Zero intro card, zero 'hello friends' greeting, instant stake.",
      weight: 10
    },
    {
      id: "Q3",
      title: "Full-Screen Visual Staging (Anti-HUD)",
      standard: "65-75% screen unobstructed; no permanent bottom thumbnail strip",
      check: "Edge-to-edge visuals, no lingering UI reels from previews.",
      weight: 10
    },
    {
      id: "Q4",
      title: "Two-Source Fact Verification",
      standard: "Official government, regulatory, or verified primary ledger",
      check: "Primary source (RBI/PIB/GSI/ISRO) verified, reported claims labeled.",
      weight: 10
    },
    {
      id: "Q5",
      title: "Typography & On-Screen Legibility",
      standard: "High-contrast font pairing; zero clipping on mobile screens",
      check: "Anton / Inter / Outfit used; tested at 375px mobile viewport.",
      weight: 10
    },
    {
      id: "Q6",
      title: "GPU Compositor Motion (60FPS)",
      standard: "Only transform and opacity animated",
      check: "Zero layout recalculations; spring deceleration physics.",
      weight: 10
    },
    {
      id: "Q7",
      title: "AI Disclosure Labels",
      standard: "AI ILLUSTRATIVE label on synthetic art & composites",
      check: "Never present AI artwork as actual real currency or official documents.",
      weight: 10
    },
    {
      id: "Q8",
      title: "1-Gate Approval Protocol",
      standard: "HTML interactive preview approved before MP4 render",
      check: "User has approved preview, duration verified, exit code 0 verified.",
      weight: 10
    },
    {
      id: "Q9",
      title: "Thumbnail Curiosity & Visual Hook",
      standard: "Full concept conveyed with large readable text & high curiosity gap",
      check: "Both Clean Base and Curiosity Text variants exported; tested in simulator.",
      weight: 10
    },
    {
      id: "Q10",
      title: "Loopable Ending & Concise CTA",
      standard: "Open closing question for comments + loop back to Frame-0",
      check: "Comments question triggers >5 word answers; concise subscribe ask.",
      weight: 10
    }
  ]
};

// Export to window
if (typeof window !== 'undefined') {
  window.BENAQAAB_DATABASE = BENAQAAB_DATABASE;
}
