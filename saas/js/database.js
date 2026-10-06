/**
 * BENAQAAB OS — Master Intelligence Database (Enhanced V2)
 * Centralized registry of all productions, vetted topics, media assets, teleprompter scripts, and QA standards.
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

  // 1. All Registered Channel Productions & Pipeline Stages
  productions: [
    {
      id: "SH-08",
      serial: "SH-08",
      title: "Sona ₹1.5 Lakh: Asli Showroom Bill",
      format: "Shorts (9:16)",
      duration: "53.9s",
      category: "Personal Finance",
      stage: "published",
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
      scriptText: "Khabar hai ki sona ₹1.5 lakh par pahunch gaya! Par agar aap showroom jayenge, toh aap ₹1,50,000 nahi denge. Asli bill dekhiye. Pehle lagta hai 3% GST — yani ₹4,500. Phir aate hain Making Charges — jo design ke naam par 12% se 18% tak jode jaate hain, yani seedhe ₹22,000 se zyada! Aur kai jagah 2 se 5% wastage alag se! 10 gram 24K gold jo ₹1.5 lakh ka dikh raha tha, showroom se nikalte nikalte ₹1,82,000 se ₹1,89,000 ka padta hai! Agar aap pehne ke liye nahi, sirf investment ke liye le rahe hain, toh Gold ETF ya Digital Gold mein ye 20% ka extra kharcha zero hota hai — bina kisi making charge ke. 1964 mein sona sirf ₹63 tha 10 gram. Aaj ₹1.5 lakh par hai — 2,300 guna ki chhalang! Aapke shehar mein aaj sona kis rate par bik raha hai? Comment kijiye, aur sach ke liye Benaqaab India subscribe kijiye!",
      titles: [
        "Sona 1.5 Lakh Par Asli Bill Dekhiye: Showroom Ka Sach",
        "Gold 1.5 Lakh? Aap Kitna Extra Dete Hain: Asli Math",
        "Sona Kharidne Se Pehle Ye Bill Dekhiye: Making Charges Exposed",
        "Gold Rate 1.5 Lakh vs Showroom Total: 31000 Ka Jhol?",
        "Physical Gold vs Gold ETF: 30000 Ka Bachat Formula"
      ],
      seoDescription: "Sona ₹1.5 lakh par pahunch gaya — par kya aapko pata hai ki showroom mein aap ₹1,50,000 nahi dete?\n\nIs Short mein Benaqaab India explain karta hai gold khareedte waqt lagne wale hidden showroom markups aur statutory taxes ka poora hisaab:\n\n1. Base 24K Spot Rate: ₹1,50,280 / 10g (IBJA Benchmark)\n2. GST (+3%): ₹4,508 flat government tax\n3. Making Charges (+12% to +18%): ₹18,000 se ₹27,000 design crafting fee\n4. Wastage / Melting Loss (+2% to +5%): ₹3,000 se ₹7,500\n5. Real Showroom Total: ₹1,82,000 se ₹1,89,000! (Lagbhag 21% extra)\n\n⏱️ TIMESTAMPS:\n0:00 Sona ₹1.5 Lakh Par Asli Showroom Bill\n0:07 Base Bullion Rate vs 3% GST\n0:18 Making Charges aur Wastage Ka Sach\n0:30 ₹1,82,000 Ka Reality Shock\n0:41 Physical Sona vs Gold ETF\n0:49 Sach • Saboot • Bebak (Subscribe)\n\n#BenaqaabIndia #GoldRate #GoldPrice #Sona #GoldInvestment #Jewellery #MakingCharges #GoldETF #FinanceHindi #Shorts",
      pinnedComment: "Aapke shehar mein aaj sona kis rate par mil raha hai, aur kitne % making charges lag rahe hain? Comment karke apna city aur rate batayein!\n\nInvestment ke liye aap Physical Gold pasand karte hain ya Gold ETF?",
      tags: ["BenaqaabIndia", "GoldRate", "GoldPrice", "Sona", "GoldRateToday", "MakingCharges", "GoldJewellery", "GoldETF", "PersonalFinance", "HindiFinance", "Shorts"],
      viewsEstimate: "142K Target",
      qaScore: 100
    },
    {
      id: "SH-07",
      serial: "SH-07",
      title: "Voter List Mein Naam Missing? (SIR Controversy)",
      format: "Shorts (9:16)",
      duration: "101.4s",
      category: "Civic / Governance",
      stage: "preview_gate",
      status: "Delivered",
      date: "2026-10-06",
      videoFile: "",
      projectPath: "projects/voter_list_sir/",
      thumbnailCuriosity: "../projects/gold_150k/thumbnail_clean_base_1080x1920.jpg",
      thumbnailClean: "../projects/gold_150k/thumbnail_clean_base_1080x1920.jpg",
      thumbnailLandscape: "../projects/gold_150k/thumbnail_clean_base_1280x720.jpg",
      lufs: -14.6,
      hook: "Voter list se 13 crore naam gayab hone ki khabar? Janie Special Intensive Revision ka sach.",
      sources: ["ECI Press Note (26 Sep 2026)", "Supreme Court Hearing (5 Oct 2026)", "Indian Express Investigation"],
      description: "Draft rolls vs final deletions explained: Form 6 declaration dispute, 14 internal objections, and voter verification steps.",
      scriptText: "Kya aapka naam voter list se bina bataye hataya ja sakta hai? Pichle kuch hafton se 13 crore naamon ke delete hone ki khabrein fail rahi hain. Sach kya hai? ECI ne 2026 mein shuru kiya Special Intensive Revision yani SIR. Iska maqsad duplicate aur expired entries ko hatana tha. Par vivaad shuru hua Form 6 par di gayi extra declaration se. Supreme Court ne saaf kiya hai ki draft roll ka matlab final deletion nahi hota. Agar aapka naam draft se hata hai, toh notice aur appeal ka adhikaar aapka kanooni haq hai. Aaj hi voters.eci.gov.in par apna naam check kijiye!",
      titles: [
        "Voter List Se Naam Missing? 13 Crore Ka Sach",
        "SIR Controversy Explained: Can You Still Vote?",
        "ECI vs Supreme Court: Voter List Revision Reality",
        "Check Your Name Now: Form 6 Declaration Dispute",
        "Voter ID Revision 2026: Asli Niyam Dekhiye"
      ],
      seoDescription: "Voter list revision controversy explained with official ECI and Supreme Court hearing facts.\n\n⏱️ TIMESTAMPS:\n0:00 Name Missing From Voter List?\n0:12 What is SIR (Special Intensive Revision)?\n0:35 13 Crore Draft Roll Reality\n0:55 Form 6 Dispute in Supreme Court\n1:25 How to verify on voters.eci.gov.in\n\n#VoterList #ECI #SupremeCourt #BenaqaabIndia #Democracy #CivicAwareness #Shorts",
      pinnedComment: "Kya aapne apna naam voters.eci.gov.in par check kiya? Agar koi samasya aayi toh comment mein batayein!",
      tags: ["BenaqaabIndia", "VoterList", "ElectionCommission", "ECI", "Form6", "SupremeCourt", "VoterID", "Shorts"],
      viewsEstimate: "95K Target",
      qaScore: 98
    },
    {
      id: "FL-04",
      serial: "FL-04",
      title: "Flight Surcharge: IndiGo ATF Fuel Hike",
      format: "Film (16:9)",
      duration: "2m 56s",
      category: "Aviation / Economy",
      stage: "published",
      status: "Delivered",
      date: "2026-10-05",
      videoFile: "../projects/flight_surcharge/Flight_Surcharge_Short.mp4",
      projectPath: "projects/flight_surcharge/",
      htmlComp: "",
      thumbnailCuriosity: "../projects/flight_surcharge/thumbnail_1280x720.jpg",
      thumbnailClean: "../projects/flight_surcharge/thumbnail_1080x1920.jpg",
      thumbnailLandscape: "../projects/flight_surcharge/thumbnail_1280x720.jpg",
      lufs: -14.2,
      hook: "Kerosene 14% mehnga hua aur flight ticket ₹11,300 tak chad gayi.",
      sources: ["IOCL Aviation Fuel Tariff", "DGCA Circular", "Brent Crude Index ($101/bbl)"],
      description: "Aviation Turbine Fuel price shock, distance tiers from ₹1,375 to ₹11,300, and crude oil compounding math.",
      scriptText: "IndiGo ne domestic flights par ₹1,375 se lekar ₹11,300 tak ka fuel surcharge laga diya hai. Kaaran? Aviation Turbine Fuel mein achanak 14% ka izafa. Ek passenger plane ke operating kharche ka 40% hissa sirf fuel hota hai. Jab international crude $100 per barrel cross karta hai, toh airline companies ye bojh seedhe aapki ticket par daal deti hain. Ye surcharge sirf nayi bookings par lagu hai.",
      titles: [
        "Flight Tickets Mehngi Kyun Hui? ATF Surcharge Exposed",
        "IndiGo Fuel Surcharge: Distance Tiers Explained",
        "Aviation Turbine Fuel Hike: Why Tickets Jumped 30%",
        "Crude at $100: Airline Ticket Math Decoded",
        "Flight Booking Se Pehle Ye Surcharge Dekhiye"
      ],
      seoDescription: "IndiGo and domestic aviation fuel surcharge decoded. Distance tiers, crude oil price linkage, and DGCA guidelines.\n\n#Aviation #FlightTickets #IndiGo #FuelSurcharge #AirTravel #BenaqaabIndia #Economy",
      pinnedComment: "Kya aapne haal hi mein flight ticket book ki hai? Kitna surcharge laga, comment mein batayein!",
      tags: ["BenaqaabIndia", "FlightSurcharge", "IndiGo", "ATF", "AviationFuel", "DGCA", "Economy"],
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
      stage: "published",
      status: "Delivered",
      date: "2026-10-04",
      videoFile: "../VIDEOS/05_Made_in_India_Chips_3m47s.mp4",
      projectPath: "projects/ep16_chips/",
      htmlComp: "",
      thumbnailCuriosity: "../brand/ref_investigative_1.png",
      thumbnailClean: "../brand/ref_investigative_1.png",
      thumbnailLandscape: "../brand/ref_investigative_1.png",
      lufs: -14.0,
      hook: "Silicon sovereignty: Bharat me pehla microchip kab ban kar niklega?",
      sources: ["India Semiconductor Mission (ISM)", "Tata Electronics Dholera Fab", "Micron Sanand ATMP"],
      description: "Dholera 28nm fab, Sanand packaging plant, Assam OSAT, and the global $1.2T chip supply chain race.",
      scriptText: "Bharat mein electronics ban rahe the, par unka dimagh — yani semiconductor chip — hamesha Taiwan, Korea ya America se aata tha. Ab Gujarat ke Dholera mein Tata ka pehla commercial fab aur Sanand mein Micron ki packaging unit shuru ho chuki hai. 28 nanometer legacy chips se lekar advanced packaging tak, India Semiconductor Mission ke tehat 5 badi facilities live ho rahi hain.",
      titles: [
        "Made-in-India Semiconductor Chips: Ground Reality",
        "Tata Dholera Fab vs Taiwan TSMC: Can India Compete?",
        "5 of 12 Chip Fabs Live: Inside India's $15B Mission",
        "Why Microchips Matter More Than Oil Today",
        "Silicon Sovereignty: Bharat Ka Semiconductor Sach"
      ],
      seoDescription: "Investigation into India Semiconductor Mission (ISM) facilities in Dholera, Sanand, and Assam.\n\n#Semiconductors #Chips #MakeInIndia #TataElectronics #Micron #TechIndia #BenaqaabIndia",
      pinnedComment: "Kya Bharat agle 5 saalon mein global chip supply chain ka leader ban sakta hai? Aapki rai kya hai?",
      tags: ["BenaqaabIndia", "Semiconductor", "Microchips", "TataElectronics", "Dholera", "Sanand", "Tech"],
      viewsEstimate: "112K",
      qaScore: 100
    },
    {
      id: "TOP-01",
      serial: "DEV-01",
      title: "RBI Rate Decision & Your Home Loan EMI",
      format: "Shorts (9:16)",
      duration: "55s Target",
      category: "Personal Finance",
      stage: "script_vo",
      status: "In Production",
      date: "2026-10-07",
      videoFile: "",
      projectPath: "projects/rbi_rate_hike/",
      htmlComp: "",
      thumbnailCuriosity: "../brand/ref_investigative_2.png",
      thumbnailClean: "../brand/ref_investigative_2.png",
      thumbnailLandscape: "../brand/ref_investigative_2.png",
      lufs: -14.0,
      hook: "Kal aapki home loan EMI badh sakti hai — aur iska bada kaaran hai monsoon.",
      sources: ["RBI Monetary Policy Committee (MPC)", "Reuters Economist Consensus", "Ministry of Statistics (MoSPI)"],
      description: "Monsoon deficit (12.6%) ➔ Food mandi inflation ➔ August CPI 4.82% ➔ Crude >$100 ➔ Rupee at 96 ➔ RBI Repo Rate Hike lever.",
      scriptText: "Kal subah 10 baje RBI Governor ek aisi ghoshna karne wale hain jo aapki har mahine ki EMI badha sakti hai. 4 reviews ke baad, pehli baar Repo Rate mein 25 basis points ke hike ki sambhavna hai. Agar aapka 50 lakh ka home loan hai, toh 0.25% ka hike har mahine lagbhag ₹800 aur 20 saal mein ₹2.4 lakh ka extra kharcha banata hai. Baarish ki kami se badhi mandi mehengai ka bojh seedhe bank interest par aata hai.",
      titles: [
        "RBI Repo Rate Hike: Aapki EMI Par Kitna Asar?",
        "Home Loan EMI Jump: 7 October MPC Decision Decoded",
        "Why Monsoon Deficit Is Increasing Your Loan Rate",
        "Repo Rate 5.25% to 5.50%: Calculation Explained",
        "Loan EMI Calculation: +25 Bps Hike Reality"
      ],
      seoDescription: "RBI Repo Rate decision breakdown and monthly home loan EMI compounding calculator.\n\n#RBIRateHike #RepoRate #HomeLoanEMI #PersonalFinance #Inflation #BenaqaabIndia #Shorts",
      pinnedComment: "Aapka home loan kis bank me hai aur kitna interest rate chal raha hai? Comment mein batayein!",
      tags: ["BenaqaabIndia", "RBIRepoRate", "HomeLoan", "EMI", "PersonalFinance", "Economy", "Shorts"],
      viewsEstimate: "Upcoming",
      qaScore: 99
    },
    {
      id: "TOP-02",
      serial: "DEV-02",
      title: "Plastic ₹10/₹20 Notes & Global UPI",
      format: "Docu (16:9)",
      duration: "3m 30s Target",
      category: "Currency / Digital Infra",
      stage: "fact_ledger",
      status: "In Research",
      date: "2026-10-07",
      videoFile: "",
      projectPath: "projects/polymer_upi_longform/",
      htmlComp: "",
      thumbnailCuriosity: "../brand/ref_investigative_3.png",
      thumbnailClean: "../brand/ref_investigative_3.png",
      thumbnailLandscape: "../brand/ref_investigative_3.png",
      lufs: -14.0,
      hook: "Paper notes phat jaate hain, par kya plastic note aur UPI physical cash ko hamesha ke liye badal denge?",
      sources: ["RBI Annual Report & Bulletin", "NPCI Official Product Statistics", "PIB Press Release"],
      description: "Dual-rail future: Polymer note durability for lower denominations + UPI expansion across 11 foreign nations.",
      scriptText: "Har saal Reserve Bank of India hazaron crore rupaye sirf kharab hue paper currency notes ko shred karke naye chapne me kharch karta hai. Isiliye ₹10 aur ₹20 ke polymer notes par charcha tez hai. Dusri taraf, UPI ab sirf Bharat me nahi, balki 11 deshon mein cross-border QR aur remittance ke liye live ho chuka hai. Cash ka substrate aur digital rail — dono ek sath badal rahe hain.",
      titles: [
        "Plastic ₹10 Notes & Global UPI: India Ka Money Future?",
        "Polymer Notes Reality Check: Will Paper Cash Vanish?",
        "UPI Live in 11 Countries: How Cross-Border QR Works",
        "RBI Bulletin Decoded: The Future of Indian Currency",
        "Cash vs Digital: Dual-Rail Monetary Architecture"
      ],
      seoDescription: "In-depth investigation of RBI polymer note trials and NPCI global UPI cross-border rail.\n\n#PolymerNotes #UPI #NPCI #RBI #IndianCurrency #Economy #BenaqaabIndia",
      pinnedComment: "Aapko India ka money future zyada cash-based lagta hai ya 100% digital UPI? Apni rai likhein!",
      tags: ["BenaqaabIndia", "PolymerNotes", "UPI", "RBI", "NPCI", "Currency", "DigitalIndia"],
      viewsEstimate: "Upcoming",
      qaScore: 98
    },
    {
      id: "TOP-03",
      serial: "DEV-03",
      title: "SIM Box Racket: Foreign Extortion Calls",
      format: "Shorts (9:16)",
      duration: "55s Target",
      category: "Cyber Crime",
      stage: "ideation",
      status: "Pitch Approved",
      date: "2026-10-07",
      videoFile: "",
      projectPath: "projects/sim_box_cyber/",
      htmlComp: "",
      thumbnailCuriosity: "../brand/reference_minimal_fullscreen.png",
      thumbnailClean: "../brand/reference_minimal_fullscreen.png",
      thumbnailLandscape: "../brand/reference_minimal_fullscreen.png",
      lufs: -14.0,
      hook: "Aapko lagta hai phone call Delhi se aa raha hai, par criminal baitha hai Dubai mein.",
      sources: ["DoT (Department of Telecommunications)", "Delhi & Cyberabad Cyber Police", "TRAI Security Directives"],
      description: "How VoIP gateways bypass official international landing stations via unverified local SIM cards.",
      scriptText: "Aapke screen par Indian number flash hota hai, par phone karne wala baitha hota hai Cambodia ya Dubai mein. Ye hota hai SIM Box ke zariye — ek aisi machine jisme ek sath 512 local SIM cards lage hote hain. International internet call ko ye machine local cellular call me convert kar deti hai. Isse na sirf telecom security bypass hoti hai, balki Digital Arrest jaise scams ko anjaam diya jata hai.",
      titles: [
        "SIM Box Racket Exposed: How Foreign Scammers Spoof Local Numbers",
        "Digital Arrest Phone Scam: The Illegal VoIP Gateway",
        "Why Fake Indian Numbers Show on Your Caller ID",
        "Inside a Cyber Crime SIM Box Farm: Ground Reality",
        "How To Identify VoIP Spoofed Calls Instantly"
      ],
      seoDescription: "Forensic breakdown of illegal SIM Box VoIP gateways used for cyber fraud in India.\n\n#CyberCrime #SIMBox #DigitalArrest #ScamExposed #CyberSecurity #BenaqaabIndia #Shorts",
      pinnedComment: "Kya aapko kabhi aisi anjaan call aayi hai jisme caller ne khud ko police ya customs bataya? Comment karein!",
      tags: ["BenaqaabIndia", "SIMBox", "CyberCrime", "ScamAlert", "DigitalArrest", "Telecom", "Shorts"],
      viewsEstimate: "Upcoming",
      qaScore: 97
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
      check: "Comments question triggers >5 words answers; concise subscribe ask.",
      weight: 10
    }
  ],

  // 4. Forensic Evidence Pinboards (Interactive Network Cases)
  evidenceCases: [
    {
      id: "case-gold",
      title: "Gold Showroom 1.5L: Real Bill Investigation",
      summary: "Tracking the flow from IBJA spot bullion benchmark to showroom bill, revealing hidden making markups and statutory 3% GST.",
      nodes: [
        { id: "n1", label: "IBJA Bullion Benchmark", category: "Benchmark", val: "₹1,50,280 / 10g", x: 60, y: 50, note: "Daily benchmark published by India Bullion and Jewellers Association for 24K 999 fine gold.", color: "#38bdf8" },
        { id: "n2", label: "Showroom Advertised Base", category: "Retail", val: "₹1,50,000", x: 340, y: 40, note: "Display board rate in prominent jewelry retail chains.", color: "#fbbf24" },
        { id: "n3", label: "Statutory 3% GST", category: "Statutory", val: "+₹4,508", x: 620, y: 60, note: "CBIC GST Schedule IV mandatory central + state tax on precious metals.", color: "#f43f5e" },
        { id: "n4", label: "Showroom Making Charges", category: "Discretionary", val: "12% - 18% (+₹22,500)", x: 220, y: 230, note: "Design crafting overhead with zero regulatory cap; negotiable on plain jewelry.", color: "#fbbf24" },
        { id: "n5", label: "Wastage & Melting Loss", category: "Discretionary", val: "2% - 5% (+₹4,500)", note: "Traditional deduction passed on to consumer despite modern induction casting.", color: "#fbbf24" },
        { id: "n6", label: "Final Showroom Bill", category: "Consumer Impact", val: "₹1,82,000 - ₹1,89,000", x: 380, y: 390, note: "Actual cash debited from customer: ~21% markup over base bullion price.", color: "#f43f5e" },
        { id: "n7", label: "Gold ETF Alternative", category: "Financial Bypass", val: "₹1,50,500 Pure Cost", x: 680, y: 370, note: "Nippon India / SBI Gold BeES on NSE with 0% making charges and 0% wastage.", color: "#34d399" }
      ],
      connections: [
        { from: "n1", to: "n2", label: "Base Reference" },
        { from: "n2", to: "n3", label: "Tax Obligation" },
        { from: "n2", to: "n4", label: "+15% Labor Overhead" },
        { from: "n2", to: "n5", label: "+3% Melting Loss" },
        { from: "n3", to: "n6", label: "Billed to Customer" },
        { from: "n4", to: "n6", label: "Markup Compounded" },
        { from: "n5", to: "n6", label: "Wastage Added" },
        { from: "n6", to: "n7", label: "₹31K Savings Contrast" }
      ]
    },
    {
      id: "case-flight",
      title: "IndiGo ATF Fuel Surcharge Surge",
      summary: "Deconstructing airfare invoices showing airline fuel surcharge remaining elevated despite international jet fuel price declines.",
      nodes: [
        { id: "n1", label: "Global Jet Fuel (ATF) Index", category: "Benchmark", val: "$78 / bbl (-6.8% Q3)", x: 60, y: 50, note: "Platts Asia Jet Fuel Index reflects softening crude costs across Indian refineries.", color: "#38bdf8" },
        { id: "n2", label: "Airline Base Fare", category: "Retail", val: "₹3,400 Displayed", x: 340, y: 40, note: "Initial ticket price advertised on aggregator search engines.", color: "#fbbf24" },
        { id: "n3", label: "Stealth Fuel Surcharge (YQ)", category: "Discretionary", val: "+₹1,650 per sector", x: 200, y: 220, note: "Non-refundable carrier surcharge bundled under 'Taxes & Fees'.", color: "#f43f5e" },
        { id: "n4", label: "DGCA Tariff Rule 135", category: "Statutory", val: "Unbundling Mandate", x: 600, y: 180, note: "Civil aviation regulation directing carriers to transparently itemize passenger tariff.", color: "#34d399" },
        { id: "n5", label: "Airport UDF & PSF Fees", category: "Statutory", val: "+₹450 Pass-Through", x: 180, y: 380, note: "User development and passenger service fees remitted directly to AAI / private operators.", color: "#38bdf8" },
        { id: "n6", label: "Final Passenger Paid", category: "Consumer Impact", val: "₹5,500 (61% Extra)", x: 440, y: 380, note: "Total checkout debit showing stealth taxes exceeding half the base fare.", color: "#f43f5e" }
      ],
      connections: [
        { from: "n1", to: "n3", label: "No Tariff Relief" },
        { from: "n2", to: "n6", label: "Base Component" },
        { from: "n3", to: "n6", label: "48% Hidden Mark" },
        { from: "n4", to: "n3", label: "Regulatory Loophole" },
        { from: "n5", to: "n6", label: "Airport Pass-Through" }
      ]
    },
    {
      id: "case-voter",
      title: "Electoral Roll SIR Revision & Deletions",
      summary: "Forensic analysis of the 13 Crore voter list controversy, Form 6 declaration dispute, and statutory verification remedies.",
      nodes: [
        { id: "n1", label: "ECI Special Intensive Revision", category: "Statutory", val: "Gazette Order 2026", x: 60, y: 50, note: "Election Commission mandate to purge deceased, duplicate, and shifted electors.", color: "#38bdf8" },
        { id: "n2", label: "13 Crore Draft Flagged Records", category: "Benchmark", val: "Draft Roll Entries", x: 340, y: 40, note: "Preliminary audit entries identified by automated SIR data cross-matching.", color: "#fbbf24" },
        { id: "n3", label: "Form 6 Extra Declaration", category: "Discretionary", val: "Citizenship Affidavit", x: 620, y: 80, note: "Controversial supplementary verification requirement challenged in legal petitions.", color: "#f43f5e" },
        { id: "n4", label: "Supreme Court Clarification", category: "Judicial", val: "5 Oct 2026 Hearing", x: 260, y: 240, note: "Apex court ruled draft roll flag does NOT equal final voting disenfranchisement.", color: "#34d399" },
        { id: "n5", label: "Form 7 & 8 Appeal Remedy", category: "Statutory", val: "30-Day Mandatory Notice", x: 540, y: 250, note: "Electoral Registration Officers must issue individual hearing notices prior to deletion.", color: "#38bdf8" },
        { id: "n6", label: "voters.eci.gov.in Verification", category: "Consumer Impact", val: "EPIC Portal Check", x: 400, y: 400, note: "Direct online database search allowing citizens to verify registration status.", color: "#34d399" }
      ],
      connections: [
        { from: "n1", to: "n2", label: "Automated Audit" },
        { from: "n1", to: "n3", label: "New Requirement" },
        { from: "n2", to: "n4", label: "Judicial Review" },
        { from: "n3", to: "n4", label: "Scrutinized by SC" },
        { from: "n4", to: "n5", label: "Mandatory Notice" },
        { from: "n5", to: "n6", label: "Public Remediation" }
      ]
    }
  ],

  // 5. 60-Second Shorts Retention Blueprints
  retentionBlueprints: [
    {
      id: "BP-01",
      title: "Sona ₹1.5L Showroom Bill (SH-08)",
      totalDuration: 54,
      totalWords: 129,
      zones: [
        {
          zone: "0s - 3s",
          title: "Frame-0 Hook (Pattern Interrupt)",
          targetSec: 3,
          vo: "Khabar hai ki sona ₹1.5 lakh par pahunch gaya! Par showroom mein aap ₹1.5L nahi denge!",
          words: 16,
          visual: "Extreme macro 35mm gold bar + bold red curiosity badge: 'ASLI BILL?'",
          sfx: "Sub-bass drop + camera shutter click",
          pacingNote: "High energy, instant stakes, zero hello greeting."
        },
        {
          zone: "3s - 15s",
          title: "Problem Statement & Anomaly",
          targetSec: 12,
          vo: "Asli bill dekhiye. Pehle lagta hai 3% GST yani ₹4,500. Phir aate hain Making Charges — 12% se 18% seedhe ₹22,000 se zyada!",
          words: 24,
          visual: "Split screen invoice: +3% GST and +18% Making Charges highlighted in fluorescent yellow multiply",
          sfx: "Cash register cha-ching + paper rip",
          pacingNote: "Clear didactic delivery; allow graphics to register."
        },
        {
          zone: "15s - 35s",
          title: "Forensic Evidence & Calculation",
          targetSec: 20,
          vo: "Aur 2 se 5% wastage alag se! 10 gram 24K gold jo ₹1.5 lakh ka dikh raha tha, showroom se nikalte nikalte ₹1,82,000 se ₹1,89,000 ka padta hai!",
          words: 31,
          visual: "Live financial ledger counter compounding rapidly from ₹1,50,000 to ₹1,82,650 with red warning flashes",
          sfx: "Compounding ticker clicks",
          pacingNote: "Math revelation beat. Viewer is surprised by the +21% jump."
        },
        {
          zone: "35s - 50s",
          title: "The Twist / Counter-Intuitive Truth",
          targetSec: 15,
          vo: "Agar aap pehne ke liye nahi, sirf investment ke liye le rahe hain, toh Gold ETF ya Digital Gold mein ye 20% ka extra kharcha zero hota hai!",
          words: 27,
          visual: "Physical Gold vs ETF side-by-side contrast card: ₹30,000 saved badge pulsing emerald green",
          sfx: "Smooth air whoosh + positive bell chime",
          pacingNote: "Empowering financial takeaway; builds deep channel trust."
        },
        {
          zone: "50s - 60s",
          title: "Bebak Verdict & Loop CTA",
          targetSec: 4,
          vo: "Aapke shehar mein aaj sona kis rate par bik raha hai? Comment kijiye, aur sach ke liye Benaqaab India subscribe kijiye!",
          words: 19,
          visual: "Interactive comment prompt pill + official Benaqaab India gold crest badge",
          sfx: "Subtle reverse riser into seamless loop",
          pacingNote: "Triggers high comment velocity with city comparison question."
        }
      ]
    },
    {
      id: "BP-02",
      title: "Voter List Missing Name (SH-07)",
      totalDuration: 58,
      totalWords: 135,
      zones: [
        {
          zone: "0s - 3s",
          title: "Frame-0 Hook (Pattern Interrupt)",
          targetSec: 3,
          vo: "Kya aapka naam voter list se bina bataye hataya ja sakta hai? 13 crore naamon ka sach!",
          words: 17,
          visual: "Red flagged voter ID card stamp: 'DELETED?' + dramatic spotlight",
          sfx: "Emergency alert chime",
          pacingNote: "Immediate civic urgency; viewer checks their own identity."
        },
        {
          zone: "3s - 15s",
          title: "The Anomaly & ECI Mandate",
          targetSec: 12,
          vo: "ECI ne 2026 mein shuru kiya Special Intensive Revision yani SIR. Duplicate aur expired entries ko hatane ke liye.",
          words: 20,
          visual: "Official ECI press note highlight overlay + animated timeline marker",
          sfx: "Paper shuffle + gavel tap",
          pacingNote: "Objective context; establishes two-source credibility."
        },
        {
          zone: "15s - 35s",
          title: "The Judicial Reality Check",
          targetSec: 20,
          vo: "Vivaad shuru hua Form 6 par di gayi extra declaration se. Par Supreme Court ne saaf kiya hai ki draft roll ka matlab final deletion nahi hota!",
          words: 29,
          visual: "Supreme Court courtroom vector backdrop with verified legal order excerpt",
          sfx: "Deep wooden gavel thud",
          pacingNote: "Debunks viral WhatsApp panic; gives relief to viewer."
        },
        {
          zone: "35s - 50s",
          title: "Statutory Citizen Protection",
          targetSec: 15,
          vo: "Agar aapka naam draft se hata hai, toh notice aur appeal ka adhikaar aapka kanooni haq hai under statutory electoral rules.",
          words: 23,
          visual: "Form 7 / Form 8 remedy cards with green verified checkmarks",
          sfx: "Positive UI click",
          pacingNote: "Actionable civic empowerment."
        },
        {
          zone: "50s - 60s",
          title: "Loop Verification & CTA",
          targetSec: 8,
          vo: "Aaj hi voters.eci.gov.in par apna naam check kijiye. Kya aapka naam list mein hai? Comment batayein aur Benaqaab India follow karein!",
          words: 22,
          visual: "Mobile browser screen recording demonstrating EPIC ID search in 5 seconds",
          sfx: "Whoosh + bell ping",
          pacingNote: "Direct utility + engagement question."
        }
      ]
    }
  ],

  // 6. Cinematic B-Roll & Visual Asset Prompt Synthesizer
  promptTemplates: [
    {
      id: "P-01",
      title: "Molten 24K Gold Crucible Pouring",
      category: "Personal Finance / Gold",
      aspect: "9:16",
      style: "Macro Forensic 35mm",
      prompt: "Extreme macro cinematic close-up of molten 24k liquid gold being poured into an iron ingot crucible, incandescent yellow-orange glow, flying spark embers, dark obsidian slate workbench, 35mm anamorphic lens, volumetric steam, photorealistic 8k, ultra-sharp textures --ar 9:16 --v 6.1 --style raw --q 2"
    },
    {
      id: "P-02",
      title: "Confidential Jewelry Invoice with Highlighter",
      category: "Personal Finance / Gold",
      aspect: "9:16",
      style: "Documentary Forensic",
      prompt: "Close-up angled shot of official jewelry showroom paper receipt resting on dark aged wooden table, vibrant neon yellow highlighter marker stroke across '18% Making Charges', single warm desk lamp illumination, shallow depth of field, documentary investigation aesthetic --ar 9:16 --v 6.1 --style raw"
    },
    {
      id: "P-03",
      title: "Commercial Boeing Turbine Jet Refueling",
      category: "Aviation / Economy",
      aspect: "16:9",
      style: "Cinematic Atmosphere",
      prompt: "Commercial Boeing airliner jet engine turbine close-up on tarmac at dusk, heavy aviation fuel hose connected with digital fuel flow meter displaying glowing green digits, rain puddles reflecting runway lighting, cinematic teal and orange grade, 50mm f/1.4 --ar 16:9 --v 6.1 --q 2"
    },
    {
      id: "P-04",
      title: "Supreme Court Gavel & Dossier",
      category: "Civic / Legal",
      aspect: "16:9",
      style: "Editorial Law Archive",
      prompt: "Solid dark mahogany courtroom desk with open Indian legal statute book, polished rosewood judicial gavel, crisp Manila dossier folder stamped CONFIDENTIAL in bold red ink, subtle dust motes floating in volumetric window beam light, 8k resolution --ar 16:9 --v 6.1 --style raw"
    },
    {
      id: "P-05",
      title: "EVM Control Unit Microprocessor",
      category: "Civic / Technology",
      aspect: "9:16",
      style: "Macro High-Tech",
      prompt: "Extreme macro photograph of electronic voting machine silicon microprocessor on green motherboard circuit board, glowing micro-LED traces, serial number laser engraved, cold technical laboratory lighting, clean scientific documentary aesthetic --ar 9:16 --v 6.1 --style raw"
    },
    {
      id: "P-06",
      title: "Vande Bharat Kavach 4.0 Locomotive Cab",
      category: "Railway Safety",
      aspect: "16:9",
      style: "Industrial High-Speed",
      prompt: "Interior view of futuristic train locomotive cabin cockpit during high-speed transit at night, multi-screen glass cockpit console displaying Kavach 4.0 automatic train protection telemetry in glowing emerald green, rain droplets streaking windshield, cinematic realism --ar 16:9 --v 6.1 --q 2"
    },
    {
      id: "P-07",
      title: "Lithium Ore White Spodumene Core Sample",
      category: "Mining / Economy",
      aspect: "9:16",
      style: "Geological Fieldwork",
      prompt: "Scientific field technician in durable work gloves holding a raw crystalline white-grey lithium spodumene ore core sample, rugged Himalayan mountain cliffs of Jammu in soft background bokeh, geological measurement scale bar, overcast natural lighting --ar 9:16 --v 6.1 --style raw"
    },
    {
      id: "P-08",
      title: "Stock Exchange Electronic Ticker Floor",
      category: "Financial Markets",
      aspect: "16:9",
      style: "Surveillance / Fast Paced",
      prompt: "Trading floor room with multi-tiered LED stock ticker wall displaying dynamic red and green financial percentage numbers, dramatic silhouette of financial analyst in foreground, desaturated slate and amber lighting, motion blur on digital numbers, cinematic 35mm --ar 16:9 --v 6.1"
    }
  ]
};

// Export to window
if (typeof window !== 'undefined') {
  window.BENAQAAB_DATABASE = BENAQAAB_DATABASE;
}
