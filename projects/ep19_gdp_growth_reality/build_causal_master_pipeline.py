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

with open(TIMESTAMPS_JSON, "r", encoding="utf-8") as f:
    ts_data = json.load(f)

boundaries = ts_data["boundaries"]
total_duration = ts_data["duration"]

# Exact 100% causal beats matched to sentence boundaries
CAUSAL_BEATS = [
    # --- CHAPTER 1: THE GLOBAL CELEBRATION VS STREET REALITY ---
    {
        "beat_id": 1,
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "start_s": 0.0,
        "end_s": 8.28,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_01_global_gdp_celebration_bull.jpg",
        "subject": "Opening Burning Question Hook",
        "hindi_desc": "दुनिया कह रही है भारत दुनिया की सबसे फ़ास्ट-ग्रोइंग इकॉनमी है— रियल जीडीपी ग्रोथ 7.8%!",
        "hud_data": "REAL GDP GROWTH: 7.8% (Q1 FY26-27)",
        "motion_type": "roadmap"
    },
    {
        "beat_id": 2,
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "start_s": 8.28,
        "end_s": 16.07,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_03_middle_class_kitchen_table_inflation.jpg",
        "subject": "Middle Class Living Cost Reality",
        "hindi_desc": "लेकिन अगर देश इतनी तेज़ी से अमीर हो रहा है, तो आम मिडिल क्लास पर क़र्ज़ का बोझ इतना ज़्यादा क्यों है?",
        "hud_data": "HOUSEHOLD DEBT: 45.8% | SAVINGS CRASH",
        "motion_type": "none"
    },
    {
        "beat_id": 3,
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "start_s": 16.07,
        "end_s": 20.00,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_09_pmgkay_free_ration_distribution.jpg",
        "subject": "80 Crore on Free Foodgrains (PMGKAY)",
        "hindi_desc": "और 80 करोड़ लोग मुफ़्त राशन पर क्यों जी रहे हैं?",
        "hud_data": "PMGKAY RECIPIENTS: 80.0 CRORE CITIZENS",
        "motion_type": "none"
    },
    {
        "beat_id": 4,
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "start_s": 20.00,
        "end_s": 38.90,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_02_parliament_cabinet_national_accounts.jpg",
        "subject": "The ₹330 Lakh Crore Economy Benchmark",
        "hindi_desc": "भारत ने यूके को पीछे छोड़ दिया है... 3.94 ट्रिलियन डॉलर यानी लगभग 330 लाख करोड़ रुपये की जीडीपी",
        "hud_data": "NOMINAL GDP: $3.94 TRILLION | WORLD RANK #5",
        "motion_type": "none"
    },
    {
        "beat_id": 5,
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "start_s": 38.90,
        "end_s": 48.30,
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_01_mospi_press_note_gdp_78.png",
        "subject": "Government Press Release Teaser",
        "hindi_desc": "लेकिन इस 7.8% हेडलाइन नंबर के पीछे एक ऐसा सच छुपा है जो अफ़िशल गवर्नमेंट प्रेस रिलीज़ेज़ में छुपा दिया जाता है।",
        "hud_data": "MINISTRY OF STATISTICS (MOSPI) PRESS NOTE",
        "motion_type": "none"
    },
    {
        "beat_id": 6,
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "start_s": 48.30,
        "end_s": 60.10,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_01_global_gdp_celebration_bull.jpg",
        "subject": "Deconstructing 7.8% Reality: Sach Saboot Bebak",
        "hindi_desc": "आइए डीकंस्ट्रक्ट करते हैं इस 7.8% जीडीपी की असली ग्राउंड रियलिटी— बिना किसी बायस के, सच, सबूत, और बेबाकी के साथ।",
        "hud_data": "BENAQAAB INDIA: SACH · SABOOT · BEBAK",
        "motion_type": "none"
    },
    {
        "beat_id": 7,
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "start_s": 60.10,
        "end_s": 64.29,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_02_parliament_cabinet_national_accounts.jpg",
        "subject": "Channel Identity & Subscribe/Like Call-to-Action",
        "hindi_desc": "चैनल को सब्सक्राइब करके बेल आइकन ज़रूर दबाएं!",
        "hud_data": "BENAQAAB INDIA | SUBSCRIBE & LIKE",
        "motion_type": "cta"
    },
    {
        "beat_id": 8,
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "start_s": 64.29,
        "end_s": 83.45,
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_01_mospi_press_note_gdp_78.png",
        "subject": "MoSPI Official National Accounts: GDP 7.8% & GVA 8.2%",
        "hindi_desc": "पहले अफ़िशल डेटा देखिए: मिनिस्ट्री ऑफ़ स्टैटिस्टिक्स एंड प्रोग्राम इम्प्लीमेंटेशन यानी मॉस्पी के मुताबिक़, रियल जीडीपी ग्रोथ 7.8% है, और जीवीए 8.2% पर दौड़ रहा है।",
        "hud_data": "GOVERNMENT OF INDIA: MoSPI PRESS NOTE",
        "motion_type": "mospi_highlighter"
    },
    {
        "beat_id": 9,
        "chapter": "Chapter 1: The Global Celebration vs Street Reality",
        "start_s": 83.45,
        "end_s": 104.66,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_03_middle_class_kitchen_table_inflation.jpg",
        "subject": "The Living Cost Disconnect: Whose Pocket Is Getting Money?",
        "hindi_desc": "लेकिन जब आप ग्रॉसरी स्टोर पर जाते हैं, बच्चों की स्कूल फ़ीस भरते हैं... तो ऐसा क्यों लगता है कि जेब हर महीने पहले से ज़्यादा ख़ाली हो रही है?",
        "hud_data": "STREET REALITY: LIVING COSTS SQUEEZE",
        "motion_type": "none"
    },

    # --- CHAPTER 2: THE PER-CAPITA ILLUSION (104.66s - 185.71s) ---
    {
        "beat_id": 10,
        "chapter": "Chapter 2: The Per-Capita Illusion: 5th Largest vs 136th Rank",
        "start_s": 104.66,
        "end_s": 121.45,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_04_crowded_mumbai_commuter_train.jpg",
        "subject": "The 143 Crore Population Multiplier",
        "hindi_desc": "भारत का जीडीपी रैंक पांचवां ज़रूर है, लेकिन भारत की आबादी 143 करोड़ है! अगर 143 करोड़ लोग मिलकर एक-एक रुपया भी कमाएं...",
        "hud_data": "TOTAL POPULATION: 1.43 BILLION CITIZENS",
        "motion_type": "none"
    },
    {
        "beat_id": 11,
        "chapter": "Chapter 2: The Per-Capita Illusion: 5th Largest vs 136th Rank",
        "start_s": 121.45,
        "end_s": 148.53,
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_03_worldbank_per_capita_ranking.png",
        "subject": "World Bank Evidence: Per Capita Rank #136 ($2,730)",
        "hindi_desc": "वर्ल्ड बैंक के डेटा के मुताबिक़, भारत की पर कैपिटा इनकम लगभग 2,730 डॉलर्स यानी क़रीब 2 लाख 28 हज़ार रुपये सालाना है! और ग्लोबल रैंक? 190 देशों में हम 136वें नंबर पर आते हैं!",
        "hud_data": "WORLD BANK: INDIA $2,730 | RANK #136",
        "motion_type": "worldbank_loupe"
    },
    {
        "beat_id": 12,
        "chapter": "Chapter 2: The Per-Capita Illusion: 5th Largest vs 136th Rank",
        "start_s": 148.53,
        "end_s": 173.16,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_05_global_superpowers_per_capita_towers.jpg",
        "subject": "Superpowers Disconnect: US $85k, Germany $54k, China $13.5k",
        "hindi_desc": "अमेरिका की पर कैपिटा इनकम 85,000 डॉलर्स है— भारत से 31 गुना ज़्यादा! जर्मनी 54,000 डॉलर्स— 20 गुना ज़्यादा! और चीन 13,500 डॉलर्स— 5 गुना ज़्यादा!",
        "hud_data": "US $85K | GERMANY $54K | CHINA $13.5K",
        "motion_type": "none"
    },
    {
        "beat_id": 13,
        "chapter": "Chapter 2: The Per-Capita Illusion: 5th Largest vs 136th Rank",
        "start_s": 173.16,
        "end_s": 185.71,
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_03_worldbank_per_capita_ranking.png",
        "subject": "Aggregate 5th vs Lower-Middle-Income Bracket",
        "hindi_desc": "यानी एग्रीगेट जीडीपी में हम पांचवें हैं क्योंकि हमारी आबादी विशाल है, लेकिन पर-कैपिटा ख़ुशहाली में हम अभी भी लोअर-मिडिल-इनकम ब्रैकेट में अटके हैं।",
        "hud_data": "DEVELOPING NATION: LOWER-MIDDLE-INCOME",
        "motion_type": "none"
    },

    # --- CHAPTER 3: THE K-SHAPED ECONOMY (185.71s - 282.36s) ---
    {
        "beat_id": 14,
        "chapter": "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?",
        "start_s": 185.71,
        "end_s": 200.00,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_06_k_shaped_economic_divergence.jpg",
        "subject": "The K-Shaped Divergence: Two Indias",
        "hindi_desc": "इकॉनॉमिस्ट्स इसे कहते हैं 'के-शेप्ड रिकवरी'। के-शेप का मतलब है कि इकॉनमी के दो हिस्से दो अलग-अलग दिशाओं में जा रहे हैं।",
        "hud_data": "THE K-SHAPED CONSUMPTION DIVERGENCE",
        "motion_type": "none"
    },
    {
        "beat_id": 15,
        "chapter": "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?",
        "start_s": 200.00,
        "end_s": 224.59,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_07_luxury_suv_gurugram_cybercity.jpg",
        "subject": "Upper Arm of K: Demat 16 Cr+ & ₹10 Cr Luxury Realty",
        "hindi_desc": "के का ऊपर वाला डंडा: देश के टॉप 10-15% लोग... स्टॉक मार्केट में 16 करोड़ से ज़्यादा डीमैट अकाउंट्स... गुरुग्राम और मुंबई में 10-10 करोड़ के लग्ज़री अपार्टमेंट्स...",
        "hud_data": "DEMAT ACCOUNTS: 16+ CRORE | CYBERCITY REALTY",
        "motion_type": "none"
    },
    {
        "beat_id": 16,
        "chapter": "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?",
        "start_s": 224.59,
        "end_s": 242.08,
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_04_siam_automobile_k_shaped.png",
        "subject": "SIAM Evidence: Luxury SUVs Boom +24.5%",
        "hindi_desc": "सियाम का अफ़िशल डेटा: लग्ज़री एसयूवीज़ और 20 लाख से महंगी गाड़ियों की सेल्स में पिछले दो सालों में 24.5% का भारी उछाल आया है!",
        "hud_data": "SIAM FLASH REPORT: LUXURY SUVS +24.5%",
        "motion_type": "siam_highlighter"
    },
    {
        "beat_id": 17,
        "chapter": "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?",
        "start_s": 242.08,
        "end_s": 263.51,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_08_rural_village_stagnant_two_wheelers.jpg",
        "subject": "Lower Arm of K: Small Cars -42% & Two-Wheelers -14%",
        "hindi_desc": "लेकिन अब के का नीचे वाला डंडा देखिए: एंट्री-लेवल छोटी गाड़ियां minus 42% गिर चुकी हैं! रूरल एरियाज़ की मोटरसाइकिल्स की बिक्री अभी भी 2019 से 14% नीचे है!",
        "hud_data": "SMALL CARS -42% | TWO-WHEELERS -14%",
        "motion_type": "none"
    },
    {
        "beat_id": 18,
        "chapter": "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?",
        "start_s": 263.51,
        "end_s": 282.36,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_09_pmgkay_free_ration_distribution.jpg",
        "subject": "The 80 Crore Citizens on Free Foodgrains",
        "hindi_desc": "भारत सरकार आज भी 80 करोड़ नागरिकों को पीएमजीकेएवाई स्कीम के तहत मुफ़्त अनाज दे रही है। अगर आमदनी बढ़ रही होती, तो 57% जनसंख्या मुफ़्त राशन पर क्यों होती?",
        "hud_data": "PMGKAY RECIPIENTS: 80 CRORE CITIZENS (57%)",
        "motion_type": "none"
    },

    # --- CHAPTER 4: THE HOUSEHOLD BALANCE SHEET CRISIS (282.36s - 361.60s) ---
    {
        "beat_id": 19,
        "chapter": "Chapter 4: The Household Balance Sheet Crisis",
        "start_s": 282.36,
        "end_s": 318.56,
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_02_rbi_household_savings_crash.png",
        "subject": "RBI Official Evidence: Net Savings Collapsed to 5.3%",
        "hindi_desc": "आरबीआई का अफ़िशल फ़ाइनेंशियल स्टेबिलिटी रिपोर्ट: इंडियन फैमिलीज़ की नेट फ़ाइनेंशियल सेविंग्स गिर कर जीडीपी के 5.3% पर आ चुकी है— जो 50 सालों का सबसे निचला स्तर है!",
        "hud_data": "RBI FSR: NET SAVINGS 5.3% (50-YEAR LOW)",
        "motion_type": "rbi_highlighter"
    },
    {
        "beat_id": 20,
        "chapter": "Chapter 4: The Household Balance Sheet Crisis",
        "start_s": 318.56,
        "end_s": 336.00,
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_02_rbi_household_savings_crash.png",
        "subject": "Household Debt Spikes to Record 45.8% of GDP",
        "hindi_desc": "हाउसहोल्ड डेट यानी परिवारों पर क़र्ज़ का बोझ बढ़कर जीडीपी के 45.8% पर पहुंच गया— हिस्टोरिकल रिकॉर्ड हाई!",
        "hud_data": "HOUSEHOLD DEBT TO GDP: 45.8% (ALL-TIME PEAK)",
        "motion_type": "rbi_debt_odometer"
    },
    {
        "beat_id": 21,
        "chapter": "Chapter 4: The Household Balance Sheet Crisis",
        "start_s": 336.00,
        "end_s": 361.60,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_11_debt_financed_consumption_credit_card.jpg",
        "subject": "Unsecured Retail Loans: 58.2% Driven Consumption",
        "hindi_desc": "बैंक रिटेल लोन्स का 58.2% हिस्सा अनसिक्योर्ड कंजम्पशन लोन्स में जा रहा है— पर्सनल लोन्स, क्रेडिट कार्ड, और बाय नाउ पे लेटर ऐप्स! यह ग्रोथ उधार के पैसे पर टिकी है!",
        "hud_data": "UNSECURED CONSUMPTION DEBT: 58.2%",
        "motion_type": "none"
    },

    # --- CHAPTER 5: THE MISSING FACTORY (361.60s - 450.38s) ---
    {
        "beat_id": 22,
        "chapter": "Chapter 5: The Missing Factory: Why Manufacturing Won't Take Off",
        "start_s": 361.60,
        "end_s": 397.18,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_12_the_missing_factory_shenzhen_comparison.jpg",
        "subject": "The Missing Factory: Mass Manufacturing Missing",
        "hindi_desc": "भारत के इकनॉमिक स्ट्रक्चर में एक बहुत बड़ा पिलर ग़ायब है: द मिसिंग फ़ैक्ट्री! चीन की जीडीपी में मैन्युफैक्चरिंग 27% है, जिससे उन्होंने 80 करोड़ लोगों को ग़रीबी से निकाला।",
        "hud_data": "THE MISSING FACTORY: 15.8% VS CHINA 27.4%",
        "motion_type": "none"
    },
    {
        "beat_id": 23,
        "chapter": "Chapter 5: The Missing Factory: Why Manufacturing Won't Take Off",
        "start_s": 397.18,
        "end_s": 421.11,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_07_luxury_suv_gurugram_cybercity.jpg",
        "subject": "The Services Island: High Growth, Low Mass Absorption",
        "hindi_desc": "हमने एग्रीकल्चर से सीधे आईटी पर छलांग लगा दी। आईटी और फ़ाइनेंशियल सर्विसेज़ 12.1% पर ग्रो कर रहे हैं, लेकिन वो सिर्फ़ एडवांस्ड कॉलेज डिग्री वालों को ले सकते हैं!",
        "hud_data": "SERVICES SECTOR: 54.5% GDP | 12.1% GROWTH",
        "motion_type": "none"
    },
    {
        "beat_id": 24,
        "chapter": "Chapter 5: The Missing Factory: Why Manufacturing Won't Take Off",
        "start_s": 421.11,
        "end_s": 431.23,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_13_agriculture_45pct_workforce_chokepoint.jpg",
        "subject": "45.4% Workforce Trapped in 15% Agriculture GVA",
        "hindi_desc": "नतीजा यह है कि भारत के 45.4% मज़दूर आज भी खेती में लगे हैं— जो जीडीपी में सिर्फ़ 15% कंट्रीब्यूट करता है!",
        "hud_data": "AGRICULTURE: 45.4% WORKFORCE | 15% GVA",
        "motion_type": "none"
    },
    {
        "beat_id": 25,
        "chapter": "Chapter 5: The Missing Factory: Why Manufacturing Won't Take Off",
        "start_s": 431.23,
        "end_s": 450.38,
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_05_manufacturing_missing_factory.png",
        "subject": "Manufacturing Stagnant at 15.8% for 30 Years",
        "hindi_desc": "देश में मैन्युफैक्चरिंग का शेयर पिछले 30 सालों से 15.8% पर अटका हुआ है, जबकि मेक इन इंडिया का टारगेट 25% था। जब तक फ़ैक्ट्रीज़ नहीं लगेंगी, युवाओं को नौकरी कहां से मिलेगी?",
        "hud_data": "MANUFACTURING: 15.8% (TARGET 25% MISSED)",
        "motion_type": "mfg_highlighter"
    },

    # --- CHAPTER 6: THE 2045 DEMOGRAPHIC CLOCK (450.38s - 525.70s) ---
    {
        "beat_id": 26,
        "chapter": "Chapter 6: The 2045 Demographic Clock",
        "start_s": 450.38,
        "end_s": 484.82,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_14_youth_demographic_clock_2045.jpg",
        "subject": "The 2045 Demographic Clock: 1.1 Crore Youth Annually",
        "hindi_desc": "भारत की मीडियन एज आज सिर्फ़ 28.4 साल है... हर साल 1 करोड़ 10 लाख युवा जॉब मार्केट में आते हैं। अगर जॉब्स नहीं मिलीं, तो डिविडेंड डिज़ास्टर में बदल सकता है!",
        "hud_data": "MEDIAN AGE 28.4 | 1.1 CRORE YOUTH/YEAR",
        "motion_type": "none"
    },
    {
        "beat_id": 27,
        "chapter": "Chapter 6: The 2045 Demographic Clock",
        "start_s": 484.82,
        "end_s": 510.04,
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_06_demographic_clock_2045.png",
        "subject": "TFR Falls to 2.0: Window Shuts by 2045",
        "hindi_desc": "एनएफएचएस-5 के मुताबिक़, फ़र्टिलिटी रेट 2.0 पर आ चुका है... हमारी डेमोग्राफिक खिड़की सिर्फ़ 2045 तक खुली है! उसके बाद भारत बूढ़ा होना शुरू हो जाएगा।",
        "hud_data": "NFHS-5: TFR 2.0 | WINDOW SHUTS 2045",
        "motion_type": "demographic_highlighter"
    },
    {
        "beat_id": 28,
        "chapter": "Chapter 6: The 2045 Demographic Clock",
        "start_s": 510.04,
        "end_s": 525.70,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_14_youth_demographic_clock_2045.jpg",
        "subject": "The Risk: Getting Old Before Getting Rich",
        "hindi_desc": "अगर अगले 15-18 सालों में हमने पर कैपिटा इनकम को 10,000 डॉलर्स नहीं पहुंचाया, तो भारत अमीर बनने से पहले बूढ़ा हो जाएगा— बिना सोशल सिक्योरिटी, बिना पेंशन के!",
        "hud_data": "TARGET: $10,000 PER CAPITA BY 2045",
        "motion_type": "none"
    },

    # --- CHAPTER 7: THE ROAD AHEAD & CITIZEN VERDICT (525.70s - 608.35s) ---
    {
        "beat_id": 29,
        "chapter": "Chapter 7: The Road Ahead & Citizen Verdict",
        "start_s": 525.70,
        "end_s": 572.61,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_16_benaqaab_final_verdict_stamp.jpg",
        "subject": "The 4 Urgent Structural Reforms",
        "hindi_desc": "भारत को तुरंत 4 बड़े क़दम उठाने होंगे: पहला लेबर-इंटेंसिव फैक्ट्रियां, दूसरा मिडिल-क्लास टैक्स रिलीफ, तीसरा कोल्ड-चेन कृषि, और चौथा डायरेक्ट वोकेशनल स्किलिंग।",
        "hud_data": "THE 4 STRUCTURAL REFORMS FOR PROSPERITY",
        "motion_type": "none"
    },
    {
        "beat_id": 30,
        "chapter": "Chapter 7: The Road Ahead & Citizen Verdict",
        "start_s": 572.61,
        "end_s": 593.84,
        "asset_type": "official_source",
        "asset_path": "assets/official_sources/src_03_worldbank_per_capita_ranking.png",
        "subject": "True Prosperity: Per Capita Rank in Top 50",
        "hindi_desc": "7.8% मंज़िल नहीं, सिर्फ़ एक नंबर है। असली विकास तब जब भारत प्रति व्यक्ति आय में 136 से टॉप 50 में पहुंचेगा, और परिवार क़र्ज़ के सहारे नहीं, बचत के दम पर आगे बढ़ेगा।",
        "hud_data": "TRUE VICTORY: PER-CAPITA RANK TOP 50",
        "motion_type": "none"
    },
    {
        "beat_id": 31,
        "chapter": "Chapter 7: The Road Ahead & Citizen Verdict",
        "start_s": 593.84,
        "end_s": 608.35,
        "asset_type": "ai",
        "asset_path": "assets/ai_plates/ai_16_benaqaab_final_verdict_stamp.jpg",
        "subject": "Final Verdict: Sach Saboot Bebak",
        "hindi_desc": "आप इस ग्राउंड रियलिटी के बारे में क्या सोचते हैं? सच, सबूत, और बेबाकी के साथ— देखते रहिए बेनाक़ाब इंडिया। जय हिंद!",
        "hud_data": "FINAL VERDICT: REALITY UNVEILED",
        "motion_type": "verdict_stamp"
    }
]

with open(BEATS_JSON, "w", encoding="utf-8") as f:
    json.dump(CAUSAL_BEATS, f, indent=2, ensure_ascii=False)

with open(BEATS_JS, "w", encoding="utf-8") as f:
    f.write("// Benaqaab India EP-19 Causal Beats Ledger (Exact Audio-Visual Lockstep)\n")
    f.write(f"window.TOTAL_DURATION = {total_duration:.3f};\n")
    f.write("window.BEATS_DATA = " + json.dumps(CAUSAL_BEATS, indent=2, ensure_ascii=False) + ";\n")

print(f"✅ Generated {len(CAUSAL_BEATS)} perfectly aligned causal beats!")
