import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DIR = Path(__file__).parent
plates_dir = DIR / "assets" / "ai_plates"
all_105_files = sorted([f.name for f in plates_dir.glob("*.jpg")])

with open(DIR / "word_timestamps.json", "r", encoding="utf-8") as f:
    ts_data = json.load(f)

boundaries = ts_data["boundaries"]
total_dur = ts_data["duration"]

# Complete 105-beat causal assignment table
# Format: (target_start, target_end, filename, subject, hindi_desc, motion_type)
BEATS_PLAN = [
    # === CHAPTER 1: The Global Celebration vs Street Reality (0.00s - 83.45s) [13 beats] ===
    (0.00, 4.20, "ai_01_global_gdp_celebration_bull.jpg", "BSE Charging Bull & 7.8% Headline Euphoria", "दुनिया कह रही है भारत दुनिया की सबसे फ़ास्ट-ग्रोइंग इकॉनमी है— रियल जीडीपी ग्रोथ 7.8%!", "roadmap"),
    (4.20, 8.28, "ai_071_dalal_street_bull_night_rain.jpg", "Dalal Street Bull in Rain & Neon Tickers", "दुनिया कह रही है भारत दुनिया की सबसे फ़ास्ट-ग्रोइंग इकॉनमी है— रियल जीडीपी ग्रोथ 7.8%!", "ken_burns"),
    (8.28, 12.00, "ai_03_middle_class_kitchen_table_inflation.jpg", "Middle-Class Living Room Ledger & Inflation Squeeze", "लेकिन अगर देश इतनी तेज़ी से अमीर हो रहा है, तो आम मिडिल क्लास पर क़र्ज़ का बोझ इतना ज़्यादा क्यों है?", "ken_burns"),
    (12.00, 16.07, "ai_073_middle_class_grocery_store_checkout.jpg", "Grocery Store Checkout & Rising Monthly Bills", "लेकिन अगर देश इतनी तेज़ी से अमीर हो रहा है, तो आम मिडिल क्लास पर क़र्ज़ का बोझ इतना ज़्यादा क्यों है?", "ken_burns"),
    (16.07, 19.99, "ai_09_pmgkay_free_ration_distribution.jpg", "80 Crore Citizens on Free Foodgrains (PMGKAY)", "और 80 करोड़ लोग मुफ़्त राशन पर क्यों जी रहे हैं?", "ken_burns"),
    (19.99, 26.50, "ai_02_parliament_cabinet_national_accounts.jpg", "Indian Parliament Sansad Bhawan & National Accounts", "हर न्यूज़ चैनल, हर इंटरनेशनल फ़ोरम पर एक ही हेडलाइन चल रही है: भारत ने यूके को पीछे छोड़ दिया है...", "ken_burns"),
    (26.50, 33.00, "ai_072_parliament_dome_tricolor_illumination.jpg", "Parliament Dome Tricolor Illumination & $3.94 Trillion", "3.94 ट्रिलियन डॉलर यानी लगभग 330 लाख करोड़ रुपये की जीडीपी के साथ...", "ken_burns"),
    (33.00, 38.90, "ai_070_headline_numbers_unmasked_metaphor.jpg", "Headline Numbers Unmasked Metaphor", "हम दुनिया की पांचवीं सबसे बड़ी अर्थव्यवस्था बन चुके हैं।", "ken_burns"),
    (38.90, 48.30, "ai_088_peasant_plowing_bullocks_dusk.jpg", "Hidden Truth Behind Government Press Releases", "लेकिन इस 7.8% हेडलाइन नंबर के पीछे एक ऐसा सच छुपा है जो अफ़िशल गवर्नमेंट प्रेस रिलीज़ेज़ में छुपा दिया जाता है।", "ken_burns"),
    (48.30, 60.10, "ai_01_global_gdp_celebration_bull.jpg", "Deconstructing 7.8% Ground Reality (Sach · Saboot · Bebak)", "आइए डीकंस्ट्रक्ट करते हैं इस 7.8% जीडीपी की असली ग्राउंड रियलिटी— बिना किसी बायस के, सच, सबूत, और बेबाकी के साथ।", "ken_burns"),
    (60.10, 64.29, "ai_02_parliament_cabinet_national_accounts.jpg", "Channel Identity & Subscribe/Like CTA Card", "चैनल को सब्सक्राइब करके बेल आइकन ज़रूर दबाएं!", "cta"),
    (64.29, 73.00, "ai_070_headline_numbers_unmasked_metaphor.jpg", "MoSPI Official Gazette & 7.8% Real GDP Highlighter", "पहले अफ़िशल डेटा देखिए: मिनिस्ट्री ऑफ़ स्टैटिस्टिक्स... रियल जीडीपी 7.8% है...", "highlighter_mospi"),
    (73.00, 83.45, "ai_072_parliament_dome_tricolor_illumination.jpg", "GDP vs GVA Discrepancy Breakdown Diagram", "और जीवीए यानी ग्रॉस वैल्यू एडेड 8.2% पर दौड़ रहा है। पेपर पर यह नंबर्स लाजवाब लगते हैं।", "diagram_gdp_gva"),

    # === CHAPTER 2: The Per-Capita Illusion: 5th Largest vs 136th Rank (83.45s - 173.16s) [13 beats] ===
    (83.45, 89.50, "ai_073_middle_class_grocery_store_checkout.jpg", "Middle-Class Hospital Bills & Tuition Inflation", "लेकिन जब आप ग्रॉसरी स्टोर पर जाते हैं, बच्चों की स्कूल फ़ीस भरते हैं, या अस्पताल का बिल देखते हैं—", "ken_burns"),
    (89.50, 95.66, "ai_03_middle_class_kitchen_table_inflation.jpg", "Emptying Pockets at Month End", "तो ऐसा क्यों लगता है कि जेब हर महीने पहले से ज़्यादा ख़ाली हो रही है?", "ken_burns"),
    (95.66, 104.66, "ai_088_peasant_plowing_bullocks_dusk.jpg", "Money Circulation vs Real Pocket Destination", "क्योंकि जीडीपी सिर्फ़ यह बताता है कि देश में कितना पैसा घूम रहा है, यह नहीं बताता कि वो पैसा आख़िर किसकी जेब में जा रहा है!", "ken_burns"),
    (104.66, 114.07, "ai_04_crowded_mumbai_commuter_train.jpg", "1.43 Billion Population Multiplier Effect", "चलिए पहला बड़ा सबूत देखते हैं: भारत का जीडीपी रैंक पांचवां ज़रूर है, लेकिन भारत की आबादी 143 करोड़ है!", "ken_burns"),
    (114.07, 121.45, "ai_074_commuter_train_doorway_wind.jpg", "Dividing ₹1 Across 143 Crore Citizens", "अगर 143 करोड़ लोग मिलकर एक-एक रुपया भी कमाएं, तो टोटल अमाउंट बहुत बड़ा दिखेगा।", "ken_burns"),
    (121.45, 130.06, "ai_075_worldbank_headquarters_dc_facade.jpg", "Per-Capita Income Calculation Reality", "लेकिन जब आप इस टोटल वेल्थ को हर एक नागरिक में बांटेंगे— यानी पर कैपिटा इनकम निकालेंगे— तो सच सामने आता है।", "ken_burns"),
    (130.06, 137.96, "ai_075_worldbank_headquarters_dc_facade.jpg", "World Bank Data: India Per-Capita $2,730 (2.28 Lakhs)", "वर्ल्ड बैंक के डेटा के मुताबिक़, भारत की पर कैपिटा इनकम लगभग 2,730 डॉलर्स यानी", "loupe_worldbank"),
    (137.96, 143.62, "ai_079_mumbai_slum_highrise_boundary.jpg", "₹2,28,000 Annual Wealth Reality", "क़रीब 2 लाख 28 हज़ार रुपये सालाना है! और ग्लोबल रैंक?", "loupe_worldbank"),
    (143.62, 148.53, "ai_079_mumbai_slum_highrise_boundary.jpg", "Rank #136 Out of 190 Countries Revealed", "190 देशों में हम 136वें नंबर पर आते हैं!", "loupe_worldbank"),
    (148.53, 157.87, "ai_05_global_superpowers_per_capita_towers.jpg", "USA $85,000: 31x Higher Global Comparison Diagram", "ज़रा ग्लोबल सुपरपावर्स से कम्पेयर कीजिए: अमेरिका की पर कैपिटा इनकम 85,000 डॉलर्स है— भारत से 31 गुना ज़्यादा!", "diagram_per_capita"),
    (157.87, 163.87, "ai_077_germany_munich_engineering_street.jpg", "Germany $54,000: 20x Higher Disparity", "जर्मनी की पर कैपिटा इनकम 54,000 डॉलर्स है— भारत से 20 गुना ज़्यादा!", "diagram_per_capita"),
    (163.87, 168.50, "ai_078_shanghai_pudong_financial_towers.jpg", "China $13,500: 5x Higher per Capita Disparity", "और चीन, जिससे हम कम्पीट करते हैं, उनकी पर कैपिटा इनकम 13,500 डॉलर्स है— भारत से 5 गुना ज़्यादा!", "diagram_per_capita"),
    (168.50, 173.16, "ai_076_us_suburban_affluence_home.jpg", "Developing Nation Lower-Middle-Income Trap", "यानी एग्रीगेट जीडीपी में हम पांचवें हैं क्योंकि हमारी आबादी विशाल है, लेकिन पर-कैपिटा ख़ुशहाली में हम अभी भी एक डेवलपिंग नेशन हैं...", "ken_burns"),

    # === CHAPTER 3: The K-Shaped Economy: Who Is Actually Spending? (173.16s - 276.75s) [14 beats] ===
    (173.16, 185.71, "ai_06_k_shaped_economic_divergence.jpg", "Developing Nation Bracket & K-Shape Origin", "लोअर-मिडिल-इनकम ब्रैकेट में अटका हुआ है। तो फिर यह 7.8% की ग्रोथ आ कहां से रही है?", "ken_burns"),
    (185.71, 194.11, "ai_06_k_shaped_economic_divergence.jpg", "Economists Define the 'K-Shaped Recovery'", "तो फिर यह 7.8% की ग्रोथ आ कहां से रही है? इकॉनॉमिस्ट्स इसे कहते हैं 'के-शेप्ड रिकवरी'।", "diagram_k_shape"),
    (194.11, 199.75, "ai_067_k_shaped_arms_converging_concept.jpg", "Two Halves of Economy Moving in Opposite Directions", "के-शेप का मतलब है कि इकॉनमी के दो हिस्से दो अलग-अलग दिशाओं में जा रहे हैं।", "diagram_k_shape"),
    (199.75, 210.08, "ai_07_luxury_suv_gurugram_cybercity.jpg", "Upper Arm of K: Top 10-15% Financial Capital Owners", "के का ऊपर वाला डंडा: देश के टॉप 10 से 15 परसेंट लोग जिनके पास फ़ाइनेंशियल एसेट्स हैं, स्टॉक्स हैं, या हाई-पेइंग कॉर्पोरेट जॉब्स हैं।", "diagram_k_shape"),
    (210.08, 217.80, "ai_080_luxury_car_dealership_showroom.jpg", "Growth is Real for Wealthy Asset Owners & Demat Surge", "इनके लिए ग्रोथ बहुत रियल है! स्टॉक मार्केट में 16 करोड़ से ज़्यादा डीमैट अकाउंट्स खुल चुके हैं।", "ken_burns"),
    (217.80, 224.59, "ai_07_luxury_suv_gurugram_cybercity.jpg", "₹10-Crore Luxury Apartments Selling Out in Hours", "गुरुग्राम और मुंबई में 10-10 करोड़ के लग्ज़री अपार्टमेंट्स लॉन्च होते ही घंटों में बिक जाते हैं!", "ken_burns"),
    (224.59, 232.47, "ai_080_luxury_car_dealership_showroom.jpg", "SIAM Official Automobile Flash Report Evidence", "इसका सबसे सॉलिड सबूत देता है सियाम यानी सोसाइटी ऑफ़ इंडियन ऑटोमोबाइल मैन्युफैक्चरर्स का अफ़िशल डेटा।", "highlighter_siam"),
    (232.47, 242.08, "ai_07_luxury_suv_gurugram_cybercity.jpg", "Luxury SUV Sales Heavy Surge (+24.5%)", "लग्ज़री एसयूवीज़ और 20 लाख से महंगी गाड़ियों की सेल्स में पिछले दो सालों में 24.5% का भारी उछाल आया है!", "highlighter_siam"),
    (242.08, 248.50, "ai_017_alto_wagonr_empty_showroom.jpg", "Lower Arm of K: Entry-Level Small Cars Collapse", "लेकिन अब के का नीचे वाला डंडा देखिए: एंट्री-लेवल छोटी गाड़ियां— जैसे मारुति ऑल्टो और वैगनआर—", "ken_burns"),
    (248.50, 255.11, "ai_017_alto_wagonr_empty_showroom.jpg", "Alto & WagonR Sales Drop -42% vs 2018", "इनकी सेल्स 2018 के मुक़ाबले माइनस 42% गिर चुकी हैं!", "ken_burns"),
    (255.11, 260.00, "ai_08_rural_village_stagnant_two_wheelers.jpg", "Rural 100cc Motorcycles Sales Down -14%", "रूरल एरियाज़ की जान कहलाने वाली एंट्री-लेवल मोटरसाइकिल्स की बिक्री अभी भी 2019 से 14% नीचे है!", "ken_burns"),
    (260.00, 263.51, "ai_081_two_wheeler_mechanic_rural_dust.jpg", "Dusty Country Roadside Garage & Stagnant Two-Wheelers", "रूरल एरियाज़ की जान कहलाने वाली एंट्री-लेवल मोटरसाइकिल्स की बिक्री अभी भी 2019 से 14% नीचे है!", "ken_burns"),
    (263.51, 272.30, "ai_019_pmgkay_ration_queue_morning.jpg", "80 Crore Citizens Dependent on PMGKAY Free Rations", "और सबसे बड़ा सबूत: भारत सरकार आज भी 80 करोड़ नागरिकों को पीएमजीकेएवाई स्कीम के तहत मुफ़्त अनाज दे रही है।", "ken_burns"),
    (272.30, 276.75, "ai_082_ration_shop_biometric_thumbprint.jpg", "Biometric Ration Dependency: 57% of Population", "अगर ग्राउंड लेवल पर हर व्यक्ति की आमदनी बढ़ रही होती, तो देश की 57% जनसंख्या को मुफ़्त राशन पर डिपेंड क्यों रहना पड़ता?", "ken_burns"),

    # === CHAPTER 4: The Household Balance Sheet Crisis (276.75s - 356.11s) [15 beats] ===
    (276.75, 282.36, "ai_018_rural_monsoon_tractor_loan.jpg", "Agrarian Household Debt & Monsoon Vulnerability", "तो देश की 57% जनसंख्या को मुफ़्त राशन पर डिपेंड क्यों रहना पड़ता?", "ken_burns"),
    (282.36, 291.94, "ai_020_rbi_fort_mumbai_headquarters_facade.jpg", "Reserve Bank of India Financial Stability Report", "अब आते हैं उस सबूत पर जिसे हर परिवार को समझना बेहद ज़रूरी है: रिज़र्व बैंक ऑफ़ इंडिया का अफ़िशल फ़ाइनेंशियल स्टेबिलिटी रिपोर्ट।", "highlighter_rbi"),
    (291.94, 300.00, "ai_021_household_savings_antique_piggybank.jpg", "Net Household Savings Crash to 5.3% (50-Year Low)", "आरबीआई के डेटा के मुताबिक़, इंडियन फैमिलीज़ की नेट फ़ाइनेंशियल सेविंग्स गिर कर जीडीपी के 5.3% पर आ चुकी है—", "highlighter_rbi"),
    (300.00, 304.74, "ai_010_rbi_financial_stability_vault.jpg", "50-Year Lowest Financial Savings Level", "जो पिछले 50 सालों का सबसे निचला स्तर है!", "highlighter_rbi"),
    (304.74, 309.78, "ai_069_indian_family_savings_revival_bank.jpg", "Historical 8-9% Indian Family Savings Benchmark", "आमतौर पर इंडियन फैमिलीज़ 8 से 9 परसेंट सेव करती थीं।", "ken_burns"),
    (309.78, 314.00, "ai_022_medical_emergency_hospital_bills.jpg", "Out-of-Pocket Healthcare Expenses Depleting Savings", "लेकिन आज बीमारी के ख़र्चे, फ़ीस, और महंगाई की वजह से आम परिवार...", "ken_burns"),
    (314.00, 318.56, "ai_023_school_coaching_fee_tuition_burden.jpg", "Education Tuition Fee Burden on Middle-Class", "अपनी पुरानी सेविंग्स तोड़कर घर चला रहे हैं।", "ken_burns"),
    (318.56, 325.00, "ai_024_household_debt_45pct_record_high.jpg", "Household Debt-to-GDP Hits All-Time High 45.8%", "सेविंग्स कम हुईं, और दूसरी तरफ़ हाउसहोल्ड डेट यानी परिवारों पर क़र्ज़ का बोझ बढ़कर जीडीपी के 45.8% पर पहुंच गया—", "highlighter_rbi"),
    (325.00, 330.61, "ai_083_rbi_vault_door_steel_bars.jpg", "Historical Record Debt Spike Documented", "हिस्टोरिकल रिकॉर्ड हाई!", "highlighter_rbi"),
    (330.61, 335.95, "ai_084_unsecured_loan_rejection_anxiety.jpg", "Debt Taken Not for Asset Creation but Survival", "और चिंता की बात यह है कि यह क़र्ज़ घर बनाने के लिए नहीं लिया जा रहा।", "ken_burns"),
    (335.95, 342.00, "ai_028_bank_branch_loan_officer_desk.jpg", "Retail Bank Credit: 58.2% in Unsecured Loans", "बैंक रिटेल लोन्स का 58.2% हिस्सा अनसिक्योर्ड कंजम्पशन लोन्स में जा रहा है—", "diagram_debt_flow"),
    (342.00, 348.55, "ai_025_smartphone_emi_bnpl_notifications.jpg", "Instant Lending Apps, Credit Cards & BNPL Surge", "यानी पर्सनल लोन्स, क्रेडिट कार्ड आउटस्टैंडिंग, और बाय नाउ पे लेटर ऐप्स!", "diagram_debt_flow"),
    (348.55, 352.50, "ai_026_credit_card_swipe_pos_terminal.jpg", "Credit Card Swipe for Everyday Essentials", "आम मिडिल-क्लास इंसान अपने मंथली ख़र्चे और ईएमआई भरने के लिए...", "diagram_debt_flow"),
    (352.50, 356.11, "ai_027_pawn_shop_gold_loan_collateral.jpg", "Gold Loan Collateral & Mortgaging Future Income", "आने वाले कल की आमदनी गिरवी रख रहा है।", "diagram_debt_flow"),
    (356.11, 361.60, "ai_029_borrowed_consumption_bubble_concept.jpg", "Consumption Growth Built on Borrowed Time", "यह कंजम्पशन बढ़ रही है, लेकिन यह ग्रोथ उधार के पैसे पर टिकी हुई है!", "diagram_debt_flow"),

    # === CHAPTER 5: The Missing Factory: Why Manufacturing Won't Take Off (356.11s - 442.72s) [17 beats] ===
    (361.60, 365.03, "ai_030_the_missing_factory_blueprint_floor.jpg", "Why Did This Structural Economic Deficit Happen?", "लेकिन आख़िर यह प्रॉब्लम क्रिएट क्यों हुई?", "ken_burns"),
    (365.03, 371.44, "ai_012_the_missing_factory_shenzhen_comparison.jpg", "The Missing Pillar: 'The Missing Factory'", "क्योंकि भारत के इकनॉमिक स्ट्रक्चर में एक बहुत बड़ा पिलर ग़ायब है: द मिसिंग फ़ैक्ट्री!", "diagram_missing_factory"),
    (371.44, 380.81, "ai_031_shenzhen_automated_electronics_line.jpg", "Global Powers Built Mass Manufacturing First", "दुनिया के हर बड़े देश ने— चाहे वो अमेरिका हो, जापान हो, या चीन— सबने पहले मास-मैन्युफैक्चरिंग खड़ी की।", "diagram_missing_factory"),
    (380.81, 388.40, "ai_032_garment_textile_mill_bangladesh_vietnam.jpg", "Farm Labor Absorbed into Textile & Electronics Mills", "खेत में काम करने वाले करोड़ों लोगों को कपड़ा, इलेक्ट्रॉनिक्स, और ऑटोमोटिव फ़ैक्ट्रीज़ में जॉब्स मिलीं।", "diagram_missing_factory"),
    (388.40, 397.18, "ai_086_vietnam_samsung_factory_complex.jpg", "China 27% Mfg Share Lifted 80 Crore Out of Poverty", "चीन की जीडीपी में मैन्युफैक्चरिंग का शेयर 27% है, जिससे उन्होंने 80 करोड़ लोगों को ग़रीबी से निकाला।", "ken_burns"),
    (397.18, 405.48, "ai_033_it_tech_park_glass_facade_bengaluru.jpg", "Leaping Directly from Agriculture to IT Services", "लेकिन भारत में क्या हुआ? हमने एग्रीकल्चर से सीधे आईटी और सॉफ़्टवेयर सर्विसेज़ पर छलांग लगा दी।", "diagram_missing_factory"),
    (405.48, 409.40, "ai_087_it_office_night_cubicles_tired.jpg", "IT & Financial Services Sector Growing at 12.1%", "हमारे आईटी और फ़ाइनेंशियल सर्विसेज़ सेक्टर", "ken_burns"),
    (409.40, 415.00, "ai_034_college_graduates_unemployed_queue.jpg", "IT Services Can Only Employ Elite College Degrees", "12.1% पर ग्रो कर रहे हैं— जो बहुत अच्छी बात है, लेकिन वो सिर्फ़ उन लोगों को एम्प्लॉय कर सकते हैं...", "ken_burns"),
    (415.00, 421.16, "ai_039_informal_small_scale_workshop_dharavi.jpg", "Informal Workshop Struggle vs Corporate Degrees", "जिनके पास इंग्लिश और एडवांस्ड कॉलेज डिग्री हो!", "ken_burns"),
    (421.16, 426.00, "ai_013_agriculture_45pct_workforce_chokepoint.jpg", "45.4% Workforce Stuck in Farming (Only 15% GDP)", "नतीजा यह है कि भारत के 45.4% मज़दूर आज भी खेती में लगे हैं—", "ken_burns"),
    (426.00, 431.23, "ai_035_tractor_plowing_small_fragmented_land.jpg", "Fragmented Small Agricultural Land Productivity Choke", "जो जीडीपी में सिर्फ़ 15% कंट्रीब्यूट करता है!", "ken_burns"),
    (431.23, 436.50, "ai_036_rural_mandis_crop_spoilage_monsoon.jpg", "Rural Mandi Crop Spoilage & Farm Distress", "और देश में मैन्युफैक्चरिंग का शेयर पिछले 30 सालों से 15.8% पर अटका हुआ है,", "highlighter_mfg"),
    (436.50, 442.72, "ai_037_make_in_india_lion_empty_shed.jpg", "Make in India Official Target Was 25% (Deficit 9.2%)", "जबकि मेक इन इंडिया का अफ़िशल टारगेट 25% था।", "highlighter_mfg"),
    (442.72, 446.50, "ai_085_empty_industrial_plot_signboard.jpg", "Empty Industrial Shed Signboard & Stalled Growth", "जब तक फ़ैक्ट्रीज़ नहीं लगेंगी,", "ken_burns"),
    (446.50, 450.38, "ai_038_automotive_stamping_press_manesar.jpg", "Heavy Automotive Stamping Press Manesar", "तब तक खेत से निकलने वाले आम युवा को इज़्ज़तदार नौकरी कहां से मिलेगी?", "ken_burns"),
    (450.38, 454.00, "ai_089_make_in_india_factory_assembly_worker.jpg", "Factory Assembly Line Worker Dignity", "जब तक फ़ैक्ट्रीज़ नहीं लगेंगी, तब तक खेत से निकलने वाले आम युवा को इज़्ज़तदार नौकरी कहां से मिलेगी?", "ken_burns"),
    (454.00, 457.45, "ai_040_container_freight_terminal_nhava_sheva.jpg", "Nhava Sheva Freight Logistics Export Terminal", "और यहीं हम पहुंचते हैं सबसे डेंजरस मोड़ पर: द 2045 डेमोग्राफिक क्लॉक।", "ken_burns"),

    # === CHAPTER 6: The 2045 Demographic Clock (457.45s - 525.70s) [13 beats] ===
    (457.45, 464.96, "ai_041_youth_demographic_dividend_class.jpg", "India Median Age is 28.4 Years (Youngest Nation)", "भारत की मीडियन एज आज सिर्फ़ 28.4 साल है— हम दुनिया के सबसे युवा देशों में से हैं।", "diagram_demographic_clock"),
    (464.96, 470.31, "ai_014_youth_demographic_clock_2045.jpg", "1.1 Crore Youth Enter Job Market Every Year", "हर साल लगभग 1 करोड़ 10 लाख युवा जॉब मार्केट में दाख़िल होते हैं।", "diagram_demographic_clock"),
    (470.31, 474.05, "ai_042_railway_recruitment_exam_crowd.jpg", "This Could Be Our Greatest Potential Strength", "यह हमारी सबसे बड़ी ताक़त बन सकती थी।", "ken_burns"),
    (474.05, 480.00, "ai_090_college_graduates_convocation_caps.jpg", "College Graduates with No Formal Job Avenues", "लेकिन अगर इन 1.1 करोड़ युवाओं के लिए हाई-पेइंग फ़ॉर्मल जॉब्स क्रिएट नहीं हुईं,", "ken_burns"),
    (480.00, 484.82, "ai_042_railway_recruitment_exam_crowd.jpg", "Demographic Dividend Turning into Demographic Disaster", "तो यह डेमोग्राफिक डिविडेंड एक डेमोग्राफिक डिज़ास्टर में बदल सकता है!", "ken_burns"),
    (484.82, 494.99, "ai_044_fertility_rate_drop_family_kerala.jpg", "NFHS Data: Fertility Rate Hits 2.0 (Below Replacement)", "नेशनल फैमिली हेल्थ सर्वे के मुताबिक़, भारत का टोटल फ़र्टिलिटी रेट 2.0 पर आ चुका है— जो रिप्लेसमेंट लेवल से नीचे है।", "highlighter_nfhs"),
    (494.99, 500.18, "ai_045_aging_population_elderly_care_rural.jpg", "South India & States Population Already Ageing", "साउथ इंडिया और कई राज्यों में आबादी पहले से बूढ़ी होने लगी है।", "ken_burns"),
    (500.18, 506.43, "ai_091_senior_citizens_village_temple_steps.jpg", "Senior Citizens in Rural Temple & Aging Reality", "एक्सपर्ट्स का कहना है कि हमारी डेमोग्राफिक खिड़की सिर्फ़ 2045 तक खुली है!", "diagram_demographic_clock"),
    (506.43, 510.04, "ai_043_digital_clock_2045_countdown_horizon.jpg", "Digital Countdown Clock: 2045 Window Deadline", "उसके बाद भारत बूढ़ा होना शुरू हो जाएगा।", "diagram_demographic_clock"),
    (510.04, 515.00, "ai_092_clock_tower_shadow_sunset.jpg", "Clock Tower Sunset Shadow: Race Against Time", "अगर अगले 15 से 18 सालों में हमने पर कैपिटा इनकम को 10,000 डॉलर्स तक नहीं पहुंचाया,", "diagram_demographic_clock"),
    (515.00, 520.00, "ai_046_social_security_pension_desert.jpg", "Risk: Ageing Without Social Security or Pension", "तो भारत अमीर बनने से पहले बूढ़ा हो जाएगा— बिना सोशल सिक्योरिटी, बिना पेंशन,", "diagram_demographic_clock"),
    (520.00, 523.00, "ai_047_middle_income_trap_concept_gate.jpg", "Middle-Income Trap Gate: Developing World Danger", "और बिना मज़बूत पब्लिक हेल्थकेयर के!", "diagram_demographic_clock"),
    (523.00, 525.70, "ai_048_south_korea_industrialization_contrast.jpg", "South Korea vs Brazil Stagnation Lessons", "तो भारत अमीर बनने से पहले बूढ़ा हो जाएगा!", "ken_burns"),

    # === CHAPTER 7: The Road Ahead & Citizen Verdict (525.70s - 608.35s) [19 beats] ===
    (525.70, 527.78, "ai_049_brazil_middle_income_stagnation.jpg", "Avoiding Brazil's Middle-Income Stagnation Trap", "तो सॉल्यूशन क्या है?", "ken_burns"),
    (527.78, 532.37, "ai_050_reform_pillar_1_factory_sheds.jpg", "Headline GDP Celebration Won't Feed Families", "सिर्फ़ हेडलाइन जीडीपी का जश्न मनाने से पेट नहीं भरेगा। भारत को तुरंत 4 बड़े क़दम उठाने होंगे:", "ken_burns"),
    (532.37, 538.00, "ai_051_garment_stitching_women_workforce.jpg", "Pillar 1: Labor-Intensive Mfg in Garments", "पहला: लेबर-इंटेंसिव मैन्युफैक्चरिंग— गारमेंट्स, फ़ुटवियर, और एग्रो-प्रोसेसिंग में...", "diagram_reforms"),
    (538.00, 542.00, "ai_052_shoe_leather_cluster_agra_tamilnadu.jpg", "Footwear & Leather Clusters in Agra & Tamil Nadu", "रेड-टेप ख़त्म करके मैसिव स्केल पर फ़ैक्ट्रीज़ लगाना।", "diagram_reforms"),
    (542.00, 545.62, "ai_053_food_processing_mega_park.jpg", "Mega Food Processing Industrial Parks", "मैसिव स्केल पर फ़ैक्ट्रीज़ लगाना।", "diagram_reforms"),
    (545.62, 547.20, "ai_093_modern_garment_spinning_mill.jpg", "Modern Garment Spinning Mill Precision", "दूसरा:", "diagram_reforms"),
    (547.20, 552.00, "ai_055_tax_relief_middle_class_family_relief.jpg", "Pillar 2: Tax Relief for Middle-Class Families", "मिडिल-क्लास पर टैक्स रिलीफ—", "diagram_reforms"),
    (552.00, 556.42, "ai_056_health_insurance_gst_removal_concept.jpg", "Remove 18% GST on Health Insurance Premiums", "हेल्थ इंश्योरेंस पर 18% जीएसटी जैसे बोझ को हटाकर परिवारों की सेविंग्स को प्रोटेक्ट करना।", "diagram_reforms"),
    (556.42, 561.00, "ai_054_solar_cold_storage_rural_cluster.jpg", "Pillar 3: Solar Cold Storages in Every Village", "तीसरा: एग्रीकल्चर में कोल्ड-चेन और फ़ूड प्रोसेसिंग को गांव-गांव पहुंचाना,", "diagram_reforms"),
    (561.00, 566.22, "ai_094_refrigerated_cold_chain_trucks.jpg", "Refrigerated Fleet to Prevent Harvest Losses", "ताकि किसान की आमदनी सिर्फ़ फ़सल बेचने तक सीमित न रहे।", "diagram_reforms"),
    (566.22, 572.61, "ai_057_vocational_skill_iti_robotics_lab.jpg", "Pillar 4: Direct Industrial Vocational Skilling", "और चौथा: डिग्री-बाज़ी के बजाय डायरेक्ट इंडस्ट्रियल वोकेशनल स्किलिंग पर फ़ोकस करना।", "diagram_reforms"),
    (572.61, 576.50, "ai_058_ev_battery_assembly_line_india.jpg", "EV Battery & Clean Tech Assembly Line Skilling", "7.8% जीडीपी ग्रोथ एक शानदार अचीवमेंट है, लेकिन यह मंज़िल नहीं,", "ken_burns"),
    (576.50, 581.01, "ai_059_semiconductor_fab_cleanroom_dholera.jpg", "Semiconductor Cleanroom Dholera & Future Tech", "सिर्फ़ एक नंबर है।", "ken_burns"),
    (581.01, 587.00, "ai_068_per_capita_rank_top_50_milestone.jpg", "Real Growth: India Per-Capita Moving to Top 50", "असली विकास तब माना जाएगा जब भारत का पर-कैपिटा रैंक 136 से निकल कर टॉप 50 में पहुंचेगा,", "ken_burns"),
    (587.00, 593.84, "ai_015_vocational_skilling_and_reforms_future.jpg", "Families Advancing on Savings, Not Borrowed Debt", "और हर आम परिवार क़र्ज़ के सहारे नहीं, अपनी बचत के दम पर आगे बढ़ेगा।", "ken_burns"),
    (593.84, 597.37, "ai_101_benaqaab_investigative_ledger_desk.jpg", "What Do You Think About This Ground Reality?", "आप इस ग्राउंड रियलिटी के बारे में क्या सोचते हैं?", "ken_burns"),
    (597.37, 600.71, "ai_102_citizen_viewing_documentary_tablet.jpg", "Share Your Thoughts in Comments Below", "अपने विचार कमेंट में ज़रूर शेयर करें।", "ken_burns"),
    (600.71, 604.50, "ai_103_india_gate_tricolor_dusk.jpg", "Sach · Saboot · Bebak — Keep Watching Benaqaab India", "सच, सबूत, और बेबाकी के साथ— देखते रहिए बेनाक़ाब इंडिया।", "ken_burns"),
    (604.50, 608.35, "ai_105_final_verdict_stamp_cinematic_climax.jpg", "Jai Hind! Final Verdict Reality Unveiled", "जय हिंद!", "verdict_stamp")
]

print(f"🎬 Total beats in BEATS_PLAN: {len(BEATS_PLAN)}")
used_files = set([b[2] for b in BEATS_PLAN])
print(f"Unique files used in plan: {len(used_files)} / {len(all_105_files)}")
missing = sorted(list(set(all_105_files) - used_files))
print(f"Still missing {len(missing)} files: {missing}")
