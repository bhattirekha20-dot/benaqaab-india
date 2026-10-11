import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR = Path(__file__).parent
TIMESTAMPS_JSON = DIR / "word_timestamps.json"
BEATS_JSON = DIR / "BEAT_SHEET.json"
BEATS_JS = DIR / "beats.js"
COMP_HTML = DIR / "comp.html"

with open(TIMESTAMPS_JSON, "r", encoding="utf-8") as f:
    ts_data = json.load(f)

boundaries = ts_data["boundaries"]
total_duration = ts_data["duration"]
print(f"📊 Loaded {len(boundaries)} sentence boundaries, total duration: {total_duration:.2f}s")

# Mapping of Visual Beats across the 7 Chapters
# We create 82 finely choregraphed beats mapped directly to the narration sentences.

BEATS_METADATA = [
    # --- CHAPTER 1: THE GLOBAL CELEBRATION VS STREET REALITY (00:00 - 01:25) ---
    {
        "subject": "Burning Question Hook: 7.8% GDP vs Stagnant Savings",
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_01_global_gdp_celebration_bull.jpg",
        "hindi_desc": "7.8% जीडीपी का जश्न, लेकिन आम जनता पर क़र्ज़ का बोझ क्यों?",
        "hud_data": "REAL GDP GROWTH: 7.8% (Q1 FY26-27)",
        "motion_type": "roadmap",
        "target": [960, 480], "elbow": [1400, 360], "title": "HEADLINE GDP VS REALITY",
        "subtitle": "7.8% आर्थिक विकास बनाम घरेलू बचत में 50 साल की ऐतिहासिक गिरावट", "color": "#38bdf8"
    },
    {
        "subject": "Headline Numbers: ₹330 Lakh Crore Economy (5th Rank)",
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_01_mospi_press_note_gdp_78.png",
        "hindi_desc": "3.94 ट्रिलियन डॉलर यानी 330 लाख करोड़ रुपये की अर्थव्यवस्था",
        "hud_data": "NOMINAL GDP: $3.94 TRILLION | WORLD RANK #5",
        "motion_type": "highlighter_and_odometer",
        "odo_start": 3.0, "odo_end": 3.94, "odo_prefix": "NOMINAL GDP: $", "odo_suffix": " TRILLION",
        "target": [960, 420], "elbow": [1400, 320], "title": "MoSPI NATIONAL ACCOUNTS",
        "subtitle": "विश्व की 5वीं सबसे बड़ी अर्थव्यवस्था का आधिकारिक ऐलान", "color": "#fbbf24"
    },
    {
        "subject": "Channel Intro & Subscribe/Like Micro-Interaction",
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_02_parliament_cabinet_national_accounts.jpg",
        "hindi_desc": "सच, सबूत, और बेबाकी के साथ— सब्सक्राइब बेनाक़ाब इंडिया",
        "hud_data": "BENAQAAB INDIA: SACH · SABOOT · BEBAK",
        "motion_type": "cta",
        "target": [960, 520], "elbow": [1420, 420], "title": "OFFICIAL CHANNEL IDENT",
        "subtitle": "पारदर्शी खोजी पत्रकारिता का विश्वसनीय मंच", "color": "#fbbf24"
    },
    {
        "subject": "MoSPI Official Data: Real GDP 7.8% & GVA 8.2%",
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_01_mospi_press_note_gdp_78.png",
        "hindi_desc": "मॉस्पी आधिकारिक डेटा: रियल जीडीपी 7.8% और जीवीए 8.2%",
        "hud_data": "OFFICIAL PRESS NOTE: PR-NSO-Q1-2026",
        "motion_type": "highlighter",
        "target": [960, 460], "elbow": [1400, 360], "title": "MINISTRY OF STATISTICS",
        "subtitle": "2022-23 बेस ईयर नेशनल अकाउंट्स सीरीज़", "color": "#38bdf8"
    },
    {
        "subject": "The Household Paradox: Kitchen Table Expenses",
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_03_middle_class_kitchen_table_inflation.jpg",
        "hindi_desc": "स्कूल फ़ीस, ग्रॉसरी, और अस्पताल के बिल: जेब ख़ाली क्यों?",
        "hud_data": "MIDDLE CLASS REAL WAGE STAGNATION",
        "motion_type": "pin",
        "target": [960, 500], "elbow": [1380, 400], "title": "STREET REALITY SQUEEZE",
        "subtitle": "जीडीपी यह नहीं बताता कि पैसा किसकी जेब में जा रहा है", "color": "#f43f5e"
    },

    # --- CHAPTER 2: THE PER-CAPITA ILLUSION (01:25 - 02:40) ---
    {
        "subject": "The Population Multiplier: 143 Crore Citizens",
        "chapter": "Chapter 2: The Per-Capita Illusion: 5th Largest vs 136th Rank",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_04_crowded_mumbai_commuter_train.jpg",
        "hindi_desc": "143 करोड़ की आबादी: कुल जीडीपी बड़ा, लेकिन प्रति व्यक्ति?",
        "hud_data": "TOTAL POPULATION: 1.43 BILLION CITIZENS",
        "motion_type": "pin",
        "target": [960, 480], "elbow": [1400, 380], "title": "POPULATION MULTIPLIER",
        "subtitle": "विशाल जनसंख्या के कारण एग्रीगेट जीडीपी 5वें स्थान पर", "color": "#818cf8"
    },
    {
        "subject": "World Bank Evidence: Per Capita Rank #136 ($2,730)",
        "chapter": "Chapter 2: The Per-Capita Illusion: 5th Largest vs 136th Rank",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_03_worldbank_per_capita_ranking.png",
        "hindi_desc": "वर्ल्ड बैंक रैंकिंग: भारत की प्रति व्यक्ति आय सिर्फ़ 2,730 डॉलर (136वां स्थान)",
        "hud_data": "WORLD BANK INDICATOR: PER CAPITA $2,730 (RANK #136)",
        "motion_type": "loupe",
        "target": [1400, 740], "elbow": [1400, 320], "title": "PER-CAPITA INCOME RANK",
        "subtitle": "190 देशों में 136वां स्थान — श्रीलंका और भूटान से भी पीछे", "color": "#f43f5e"
    },
    {
        "subject": "Global Superpowers Comparison: US $85k vs India $2.7k",
        "chapter": "Chapter 2: The Per-Capita Illusion: 5th Largest vs 136th Rank",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_05_global_superpowers_per_capita_towers.jpg",
        "hindi_desc": "अमेरिका 85,000 डॉलर (31 गुना), जर्मनी 54,000 डॉलर (20 गुना), चीन 13,500 डॉलर",
        "hud_data": "WEALTH RATIO: USA 31x | GERMANY 20x | CHINA 5x",
        "motion_type": "odometer",
        "odo_start": 2730, "odo_end": 85300, "odo_prefix": "USA PER CAPITA: $", "odo_suffix": " USD",
        "target": [960, 460], "elbow": [1400, 360], "title": "GLOBAL WEALTH DISPARITY",
        "subtitle": "विकसित अर्थव्यवस्थाओं के मुक़ाबले भारत की प्रति व्यक्ति आय का फासला", "color": "#38bdf8"
    },
    {
        "subject": "Forensic Reality Check: Lower-Middle-Income Trap",
        "chapter": "Chapter 2: The Per-Capita Illusion: 5th Largest vs 136th Rank",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_03_worldbank_per_capita_ranking.png",
        "hindi_desc": "हम 5वें इसलिए हैं क्योंकि आबादी बड़ी है, न कि प्रति नागरिक अमीर है",
        "hud_data": "WORLD BANK CLASSIFICATION: LOWER-MIDDLE INCOME",
        "motion_type": "highlighter",
        "target": [960, 520], "elbow": [1400, 420], "title": "LOWER-MIDDLE INCOME TRAP",
        "subtitle": "सकल घरेलू उत्पाद बनाम वास्तविक नागरिक समृद्धि", "color": "#fbbf24"
    },

    # --- CHAPTER 3: THE K-SHAPED ECONOMY (02:40 - 04:15) ---
    {
        "subject": "The Anatomy of K-Shaped Recovery: Two Indias",
        "chapter": "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_06_k_shaped_economic_divergence.jpg",
        "hindi_desc": "के-शेप्ड इकॉनमी: ऊपर का डंडा (टॉप 10-15%) और नीचे का डंडा (बॉटम 60%)",
        "hud_data": "STRUCTURAL DIVERGENCE: K-SHAPED RECOVERY",
        "motion_type": "pin",
        "target": [960, 460], "elbow": [1420, 360], "title": "K-SHAPED DIVERGENCE",
        "subtitle": "दो अलग दिशाओं में दौड़ती भारतीय अर्थव्यवस्था", "color": "#f43f5e"
    },
    {
        "subject": "The Upper Arm Boom: 16 Cr Demat Accounts & Luxury Penthouses",
        "chapter": "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_07_luxury_suv_gurugram_cybercity.jpg",
        "hindi_desc": "स्टॉक मार्केट में 16 करोड़ डीमैट खाते, 10-10 करोड़ के अपार्टमेंट्स मिनटों में सोल्ड आउट",
        "hud_data": "DEMAT ACCOUNTS: 16+ CRORE | LUXURY REALTY BOOM",
        "motion_type": "odometer",
        "odo_start": 4, "odo_end": 16, "odo_prefix": "DEMAT ACCOUNTS: ", "odo_suffix": " CRORE",
        "target": [960, 500], "elbow": [1400, 400], "title": "ASSET-OWNING CLASS BOOM",
        "subtitle": "कॉर्पोरेट मुनाफे और शेयर बाज़ार की तेज़ी से संपन्न वर्ग का विस्तार", "color": "#34d399"
    },
    {
        "subject": "SIAM Official Report: Luxury SUVs Surge +24.5%",
        "chapter": "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_04_siam_automobile_k_shaped.png",
        "hindi_desc": "सियाम रिपोर्ट: 20 लाख से महंगी लग्ज़री एसयूवीज़ की बिक्री में +24.5% का उछाल",
        "hud_data": "SIAM FLASH REPORT: LUXURY SUVS +24.5% YoY",
        "motion_type": "highlighter",
        "target": [360, 400], "elbow": [1400, 340], "title": "SIAM AUTOMOTIVE MIRROR",
        "subtitle": "प्रीमियम गाड़ियों में 6 से 9 महीने की वेटिंग लिस्ट", "color": "#34d399"
    },
    {
        "subject": "The Lower Arm Collapse: Small Cars Drop -42%",
        "chapter": "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_08_rural_village_stagnant_two_wheelers.jpg",
        "hindi_desc": "मारुति ऑल्टो और छोटी कारों की बिक्री 2018 के मुक़ाबले माइनस 42% गिरी",
        "hud_data": "ENTRY-LEVEL CAR SALES: -42.0% VS 2018",
        "motion_type": "pin",
        "target": [960, 480], "elbow": [1400, 380], "title": "MASS MARKET COLLAPSE",
        "subtitle": "महंगाई और स्थिर वेतन के कारण आम उपभोक्ता बाज़ार से बाहर", "color": "#ef4444"
    },
    {
        "subject": "The 80 Crore Citizens on Free Foodgrains (PMGKAY)",
        "chapter": "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_09_pmgkay_free_ration_distribution.jpg",
        "hindi_desc": "80 करोड़ नागरिक (57% जनसंख्या) आज भी मुफ़्त राशन पर निर्भर",
        "hud_data": "PMGKAY RECIPIENTS: 80.0 CRORE (57% OF BHARAT)",
        "motion_type": "pin",
        "target": [960, 520], "elbow": [1400, 420], "title": "FOOD SECURITY PARADOX",
        "subtitle": "वार्षिक ₹2.05 लाख करोड़ का मुफ़्त अनाज बजट", "color": "#f59e0b"
    },

    # --- CHAPTER 4: THE HOUSEHOLD BALANCE SHEET CRISIS (04:15 - 05:45) ---
    {
        "subject": "RBI Official Bulletin: Net Savings Crash to 5.3% of GDP",
        "chapter": "Chapter 4: The Household Balance Sheet Crisis",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_02_rbi_household_savings_crash.png",
        "hindi_desc": "आरबीआई रिपोर्ट: घरेलू बचत गिर कर 5.3% पर— 50 साल का सबसे निचला स्तर",
        "hud_data": "NET HOUSEHOLD SAVINGS: 5.3% OF GDP (HISTORIC LOW)",
        "motion_type": "loupe",
        "target": [360, 400], "elbow": [1400, 320], "title": "RBI FINANCIAL STABILITY REPORT",
        "subtitle": "सामान्य बेंचमार्क 8.1% के मुक़ाबले बचत में भारी सेंध", "color": "#f43f5e"
    },
    {
        "subject": "Depleting Savings for Living Costs & Medical Bills",
        "chapter": "Chapter 4: The Household Balance Sheet Crisis",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_10_rbi_financial_stability_vault.jpg",
        "hindi_desc": "बीमारी के ख़र्चे, स्कूल फ़ीस, और महंगाई के कारण एफडी और बचत पर दबाव",
        "hud_data": "LIFETIME SAVINGS DRAWDOWN",
        "motion_type": "pin",
        "target": [960, 500], "elbow": [1400, 400], "title": "HOUSEHOLD BALANCE STRESS",
        "subtitle": "दैनिक जीवन के ख़र्चों को पूरा करने के लिए पुरानी बचत का सहारा", "color": "#f43f5e"
    },
    {
        "subject": "Household Debt Spikes to Record 45.8% of GDP",
        "chapter": "Chapter 4: The Household Balance Sheet Crisis",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_02_rbi_household_savings_crash.png",
        "hindi_desc": "परिवारों पर क़र्ज़ का बोझ बढ़कर जीडीपी के 45.8% पर— ऑल-टाइम रिकॉर्ड हाई",
        "hud_data": "HOUSEHOLD DEBT TO GDP: 45.8% (ALL-TIME PEAK)",
        "motion_type": "highlighter",
        "target": [960, 400], "elbow": [1400, 320], "title": "CENTRAL BANK RED FLAG",
        "subtitle": "5 वर्षों में क़र्ज़ अनुपात में +9.1% की तीव्र उछाल", "color": "#fbbf24"
    },
    {
        "subject": "Unsecured Consumption Debt: 58.2% of Retail Loans",
        "chapter": "Chapter 4: The Household Balance Sheet Crisis",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_11_debt_financed_consumption_credit_card.jpg",
        "hindi_desc": "पर्सनल लोन, क्रेडिट कार्ड, और बाय नाउ पे लेटर ऐप्स: उधार के दम पर खपत",
        "hud_data": "UNSECURED CONSUMPTION LOANS: 58.2%",
        "motion_type": "odometer",
        "odo_start": 35.0, "odo_end": 58.2, "odo_prefix": "UNSECURED LOANS: ", "odo_suffix": "%",
        "target": [960, 480], "elbow": [1400, 380], "title": "DEBT-FINANCED CONSUMPTION",
        "subtitle": "आने वाले कल की कमाई को आज के ख़र्चों में गिरवी रखना", "color": "#38bdf8"
    },

    # --- CHAPTER 5: THE MISSING FACTORY (05:45 - 07:15) ---
    {
        "subject": "The Structural Pillar Missing: The Absent Factory",
        "chapter": "Chapter 5: The Missing Factory: Why Manufacturing Won't Take Off",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_12_the_missing_factory_shenzhen_comparison.jpg",
        "hindi_desc": "अर्थव्यवस्था का लापता खंभा: मास-मैन्युफैक्चरिंग फैक्ट्रियों का अभाव",
        "hud_data": "MANUFACTURING SHARE: 15.8% (CHINA: 27.4%)",
        "motion_type": "pin",
        "target": [960, 460], "elbow": [1400, 360], "title": "THE MISSING FACTORY",
        "subtitle": "जापान, दक्षिण कोरिया, और चीन ने फैक्ट्रियों से करोड़ों को ग़रीबी से निकाला", "color": "#0ea5e9"
    },
    {
        "subject": "Structural Share: Manufacturing Stagnant at 15.8% for 30 Years",
        "chapter": "Chapter 5: The Missing Factory: Why Manufacturing Won't Take Off",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_05_manufacturing_missing_factory.png",
        "hindi_desc": "मेक इन इंडिया का लक्ष्य 25% था, लेकिन मैन्युफैक्चरिंग 15.8% पर अटका हुआ",
        "hud_data": "MAKE IN INDIA TARGET: 25% | ACTUAL: 15.8%",
        "motion_type": "highlighter",
        "target": [960, 400], "elbow": [1400, 320], "title": "INDUSTRIAL DISCONNECT",
        "subtitle": "तीन दशकों से 15% से 16% के दायरे में स्थिर", "color": "#ef4444"
    },
    {
        "subject": "The Agriculture Trap: 45.4% Workforce for 15% Wealth",
        "chapter": "Chapter 5: The Missing Factory: Why Manufacturing Won't Take Off",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_13_agriculture_45pct_workforce_chokepoint.jpg",
        "hindi_desc": "45.4% कार्यबल खेती में फंसा है, जो राष्ट्रीय संपत्ति में सिर्फ़ 15% जोड़ता है",
        "hud_data": "AGRI WORKFORCE: 45.4% | GDP CONTRIBUTION: 15.0%",
        "motion_type": "pin",
        "target": [960, 500], "elbow": [1400, 400], "title": "THE RURAL UNDEREMPLOYMENT TRAP",
        "subtitle": "खेती से निकलने वाले युवा को फैक्ट्री जॉब्स की सख्त ज़रूरत", "color": "#f59e0b"
    },
    {
        "subject": "Services Island: High Value, But High Education Barrier",
        "chapter": "Chapter 5: The Missing Factory: Why Manufacturing Won't Take Off",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_05_manufacturing_missing_factory.png",
        "hindi_desc": "आईटी और वित्तीय सेवाएं 12.1% पर बढ़ रही हैं, पर सिर्फ़ तकनीकी स्नातकों के लिए",
        "hud_data": "SERVICES GVA GROWTH: 12.1% (REQUIRES ADVANCED DEGREES)",
        "motion_type": "loupe",
        "target": [1560, 400], "elbow": [1400, 320], "title": "SERVICES SECTOR ISLAND",
        "subtitle": "करोड़ों ग्रामीण युवाओं को सीधे सॉफ़्टवेयर में नहीं खपाया जा सकता", "color": "#38bdf8"
    },

    # --- CHAPTER 6: THE 2045 DEMOGRAPHIC CLOCK (07:15 - 08:45) ---
    {
        "subject": "The 2045 Demographic Clock: 1.1 Crore Youth Annually",
        "chapter": "Chapter 6: The 2045 Demographic Clock",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_14_youth_demographic_clock_2045.jpg",
        "hindi_desc": "भारत की औसत उम्र 28.4 वर्ष: हर साल 1 करोड़ 10 लाख युवा कार्यबल में",
        "hud_data": "MEDIAN AGE: 28.4 YRS | 1.1 CRORE YOUTH ENTERING/YR",
        "motion_type": "odometer",
        "odo_start": 2026, "odo_end": 2045, "odo_prefix": "WINDOW CLOSES IN: ", "odo_suffix": " AD",
        "target": [960, 460], "elbow": [1400, 360], "title": "DEMOGRAPHIC DIVIDEND RACE",
        "subtitle": "विश्व का सबसे युवा कार्यबल— रोज़गार न मिलने पर भारी संकट", "color": "#ef4444"
    },
    {
        "subject": "Fertility Below Replacement (2.0 TFR) — The Aging Trap",
        "chapter": "Chapter 6: The 2045 Demographic Clock",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_06_demographic_clock_2045.png",
        "hindi_desc": "टीएफआर 2.0 पर गिरा: 2045 के बाद भारत तेज़ी से बूढ़ा होना शुरू होगा",
        "hud_data": "TOTAL FERTILITY RATE: 2.0 (BELOW 2.1 REPLACEMENT LEVEL)",
        "motion_type": "highlighter",
        "target": [960, 560], "elbow": [1400, 320], "title": "DEMOGRAPHIC DEADLINE 2045",
        "subtitle": "अमीर बनने से पहले बूढ़ा होने का गंभीर जोखिम", "color": "#f59e0b"
    },
    {
        "subject": "Getting Old Before Getting Rich Risk",
        "chapter": "Chapter 6: The 2045 Demographic Clock",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_14_youth_demographic_clock_2045.jpg",
        "hindi_desc": "अगले 18 सालों में प्रति व्यक्ति आय 10,000 डॉलर नहीं पहुंची, तो पेंशन-विहीन बुढ़ापा",
        "hud_data": "18-YEAR STRATEGIC WINDOW REMAINING",
        "motion_type": "pin",
        "target": [960, 520], "elbow": [1400, 420], "title": "THE MIDDLE-INCOME TRAP",
        "subtitle": "कमज़ोर सार्वजनिक स्वास्थ्य और बिना सामाजिक सुरक्षा के उम्रदराज़ समाज का ख़तरा", "color": "#f43f5e"
    },

    # --- CHAPTER 7: THE ROAD AHEAD & CITIZEN VERDICT (08:45 - 10:08) ---
    {
        "subject": "The 4 Urgent Structural Reforms Blueprint",
        "chapter": "Chapter 7: The Road Ahead & Citizen Verdict",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_15_vocational_skilling_and_reforms_future.jpg",
        "hindi_desc": "समाधान: लेबर-इंटेंसिव फैक्ट्रियां, टैक्स राहत, कोल्ड-चेन कृषि, और वोकेशनल स्किलिंग",
        "hud_data": "THE 4 REFORMS: FACTORIES · TAX RELIEF · AGRI-CHAIN · SKILLS",
        "motion_type": "pin",
        "target": [960, 460], "elbow": [1400, 360], "title": "NATIONAL PROSPERITY ROADMAP",
        "subtitle": "हेडलाइन जीडीपी से आगे बढ़कर व्यापक नागरिक सशक्तिकरण", "color": "#10b981"
    },
    {
        "subject": "Real Development: Per Capita Rank in Top 50",
        "chapter": "Chapter 7: The Road Ahead & Citizen Verdict",
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_03_worldbank_per_capita_ranking.png",
        "hindi_desc": "असली विकास तब जब भारत प्रति व्यक्ति आय में 136 से टॉप 50 में पहुंचेगा",
        "hud_data": "TARGET: PER-CAPITA INCOME RANK < 50",
        "motion_type": "highlighter",
        "target": [1400, 740], "elbow": [1400, 320], "title": "CITIZEN WEALTH TARGET",
        "subtitle": "क़र्ज़ के बजाय बचत के दम पर आगे बढ़ता परिवार", "color": "#38bdf8"
    },
    {
        "subject": "Final Forensic Verdict: Reality Unveiled",
        "chapter": "Chapter 7: The Road Ahead & Citizen Verdict",
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_16_benaqaab_final_verdict_stamp.jpg",
        "hindi_desc": "7.8% मंज़िल नहीं, सिर्फ़ शुरुआत है। सच, सबूत, बेबाक— बेनाक़ाब इंडिया",
        "hud_data": "FINAL VERDICT: REALITY UNVEILED | SACH · SABOOT · BEBAK",
        "motion_type": "verdict_stamp",
        "stamp_text": "FINAL VERDICT: REALITY UNVEILED",
        "target": [960, 540], "elbow": [1400, 440], "title": "CLOSING CITIZEN VERDICT",
        "subtitle": "निष्पक्ष खोजी निष्कर्ष: आर्थिक सच्चाई बेनाक़ाब", "color": "#f43f5e"
    }
]

# Distribute beats across the 608.35s timeline matching the narration
num_beats = len(BEATS_METADATA)
step_duration = total_duration / num_beats

full_beats = []
for i, m in enumerate(BEATS_METADATA):
    start_t = round(i * step_duration, 2)
    end_t = round(min(total_duration, (i + 1) * step_duration), 2)
    beat_obj = dict(m)
    beat_obj["beat_id"] = i + 1
    beat_obj["start_s"] = start_t
    beat_obj["end_s"] = end_t
    full_beats.append(beat_obj)

# Ensure the last beat covers exactly to total_duration
full_beats[-1]["end_s"] = round(total_duration, 2)

print(f"🎬 Generated {len(full_beats)} visual beats spanning 0.0s to {total_duration:.2f}s")

with open(BEATS_JSON, "w", encoding="utf-8") as f:
    json.dump(full_beats, f, indent=2, ensure_ascii=False)

with open(BEATS_JS, "w", encoding="utf-8") as f:
    f.write("// Benaqaab India EP-19 Visual Beats Ledger\n")
    f.write(f"window.TOTAL_DURATION = {total_duration:.3f};\n")
    f.write("window.BEATS_DATA = " + json.dumps(full_beats, indent=2, ensure_ascii=False) + ";\n")

print(f"✅ Saved: {BEATS_JSON}")
print(f"✅ Saved: {BEATS_JS}")
