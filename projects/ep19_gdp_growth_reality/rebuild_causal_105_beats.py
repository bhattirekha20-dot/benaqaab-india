import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DIR = Path(__file__).parent
with open(DIR / "word_timestamps.json", "r", encoding="utf-8") as f:
    ts_data = json.load(f)

boundaries = ts_data["boundaries"]
total_dur = ts_data["duration"]

# Exact 105 Causal Visual Beats Plan (Ordered chronologically to match every spoken sentence)
# Format: (sentence_idx, sub_start_offset, sub_duration, filename, subject, hindi_desc, motion_type)
PLAN_105 = [
    # --- CHAPTER 1: The Global Celebration vs Street Reality (0.0s - 83.45s) [11 beats] ---
    (0, 0.00, 4.20, "ai_01_global_gdp_celebration_bull.jpg", "BSE Charging Bull & 7.8% Headline Euphoria", "दुनिया कह रही है भारत दुनिया की सबसे फ़ास्ट-ग्रोइंग इकॉनमी है— रियल जीडीपी ग्रोथ 7.8%!", "roadmap"),
    (0, 4.20, 4.13, "ai_071_dalal_street_bull_night_rain.jpg", "Dalal Street Bull in Rain & Neon Tickers", "दुनिया कह रही है भारत दुनिया की सबसे फ़ास्ट-ग्रोइंग इकॉनमी है— रियल जीडीपी ग्रोथ 7.8%!", "ken_burns"),
    (1, 0.00, 4.00, "ai_03_middle_class_kitchen_table_inflation.jpg", "Middle-Class Living Room Ledger & Inflation Squeeze", "लेकिन अगर देश इतनी तेज़ी से अमीर हो रहा है, तो आम मिडिल क्लास पर क़र्ज़ का बोझ इतना ज़्यादा क्यों है?", "ken_burns"),
    (1, 4.00, 3.80, "ai_073_middle_class_grocery_store_checkout.jpg", "Grocery Store Checkout & Rising Monthly Bills", "लेकिन अगर देश इतनी तेज़ी से अमीर हो रहा है, तो आम मिडिल क्लास पर क़र्ज़ का बोझ इतना ज़्यादा क्यों है?", "ken_burns"),
    (2, 0.00, 3.92, "ai_09_pmgkay_free_ration_distribution.jpg", "80 Crore Citizens on Free Foodgrains (PMGKAY)", "और 80 करोड़ लोग मुफ़्त राशन पर क्यों जी रहे हैं?", "ken_burns"),
    (3, 0.00, 6.50, "ai_02_parliament_cabinet_national_accounts.jpg", "Indian Parliament Sansad Bhawan & National Accounts", "हर न्यूज़ चैनल, हर इंटरनेशनल फ़ोरम पर एक ही हेडलाइन चल रही है: भारत ने यूके को पीछे छोड़ दिया है...", "ken_burns"),
    (3, 6.50, 6.50, "ai_072_parliament_dome_tricolor_illumination.jpg", "Parliament Dome Tricolor Illumination & $3.94 Trillion", "3.94 ट्रिलियन डॉलर यानी लगभग 330 लाख करोड़ रुपये की जीडीपी के साथ, हम दुनिया की पांचवीं सबसे बड़ी अर्थव्यवस्था बन चुके हैं।", "ken_burns"),
    (3, 13.00, 5.91, "ai_070_headline_numbers_unmasked_metaphor.jpg", "Headline Numbers Unmasked Metaphor", "हम दुनिया की पांचवीं सबसे बड़ी अर्थव्यवस्था बन चुके हैं।", "ken_burns"),
    (4, 0.00, 9.40, "ai_070_headline_numbers_unmasked_metaphor.jpg", "Deconstructing 7.8% GDP Headline Discrepancy", "लेकिन इस 7.8% हेडलाइन नंबर के पीछे एक ऐसा सच छुपा है जो अफ़िशल गवर्नमेंट प्रेस रिलीज़ेज़ में छुपा दिया जाता है।", "ken_burns"),
    (5, 0.00, 11.80, "ai_071_dalal_street_bull_night_rain.jpg", "Investigative Deconstruction: Sach, Saboot, Bebak", "आइए डीकंस्ट्रक्ट करते हैं इस 7.8% जीडीपी की असली ग्राउंड रियलिटी— बिना किसी बायस के, सच, सबूत, और बेबाकी के साथ।", "ken_burns"),
    (6, 0.00, 4.19, "ai_02_parliament_cabinet_national_accounts.jpg", "Channel Identity & Subscribe/Like CTA Card", "चैनल को सब्सक्राइब करके बेल आइकन ज़रूर दबाएं!", "cta"),

    # --- CHAPTER 1 / OFFICIAL DATA: MoSPI Press Note & Diagram 1 (64.29s - 83.45s) [3 beats] ---
    (7, 0.00, 8.00, "ai_01_global_gdp_celebration_bull.jpg", "MoSPI Official Gazette & 7.8% Real GDP Highlighter", "पहले अफ़िशल डेटा देखिए: मिनिस्ट्री ऑफ़ स्टैटिस्टिक्स... रियल जीडीपी 7.8% है...", "highlighter_mospi"),
    (7, 8.00, 8.06, "ai_072_parliament_dome_tricolor_illumination.jpg", "GDP vs GVA Wedge: 8.2% GVA Discrepancy Diagram", "और जीवीए यानी ग्रॉस वैल्यू एडेड 8.2% पर दौड़ रहा है।", "diagram_gdp_gva"),
    (8, 0.00, 3.10, "ai_03_middle_class_kitchen_table_inflation.jpg", "Paper Numbers Euphoria vs Real Reality", "पेपर पर यह नंबर्स लाजवाब लगते हैं।", "diagram_gdp_gva"),

    # --- CHAPTER 2: The Per-Capita Illusion: 5th Largest vs 136th Rank (83.45s - 173.16s) [12 beats] ---
    (9, 0.00, 6.10, "ai_073_middle_class_grocery_store_checkout.jpg", "Middle-Class Hospital Bills & Tuition Inflation", "लेकिन जब आप ग्रॉसरी स्टोर पर जाते हैं, बच्चों की स्कूल फ़ीस भरते हैं, या अस्पताल का बिल देखते हैं—", "ken_burns"),
    (9, 6.10, 6.12, "ai_03_middle_class_kitchen_table_inflation.jpg", "Emptying Pockets at Month End", "तो ऐसा क्यों लगता है कि जेब हर महीने पहले से ज़्यादा ख़ाली हो रही है?", "ken_burns"),
    (10, 0.00, 9.00, "ai_088_peasant_plowing_bullocks_dusk.jpg", "Money Circulation vs Real Pocket Destination", "क्योंकि जीडीपी सिर्फ़ यह बताता है कि देश में कितना पैसा घूम रहा है, यह नहीं बताता कि वो पैसा आख़िर किसकी जेब में जा रहा है!", "ken_burns"),
    (11, 0.00, 9.41, "ai_04_crowded_mumbai_commuter_train.jpg", "1.43 Billion Population Multiplier Effect", "चलिए पहला बड़ा सबूत देखते हैं: भारत का जीडीपी रैंक पांचवां ज़रूर है, लेकिन भारत की आबादी 143 करोड़ है!", "ken_burns"),
    (12, 0.00, 7.37, "ai_074_commuter_train_doorway_wind.jpg", "Dividing ₹1 Across 143 Crore Citizens", "अगर 143 करोड़ लोग मिलकर एक-एक रुपया भी कमाएं, तो टोटल अमाउंट बहुत बड़ा दिखेगा।", "ken_burns"),
    (13, 0.00, 8.61, "ai_075_worldbank_headquarters_dc_facade.jpg", "Per-Capita Income Calculation Reality", "लेकिन जब आप इस टोटल वेल्थ को हर एक नागरिक में बांटेंगे— यानी पर कैपिटा इनकम निकालेंगे— तो सच सामने आता है।", "ken_burns"),
    (14, 0.00, 7.80, "ai_075_worldbank_headquarters_dc_facade.jpg", "World Bank Data: India Per-Capita $2,730 (2.28 Lakhs)", "वर्ल्ड बैंक के डेटा के मुताबिक़, भारत की पर कैपिटा इनकम लगभग 2,730 डॉलर्स यानी", "loupe_worldbank"),
    (15, 0.00, 3.77, "ai_079_mumbai_slum_highrise_boundary.jpg", "₹2,28,000 Annual Wealth Reality", "क़रीब 2 लाख 28 हज़ार रुपये सालाना है!", "loupe_worldbank"),
    (16, 0.00, 1.94, "ai_079_mumbai_slum_highrise_boundary.jpg", "Global Rank Interrogation", "और ग्लोबल रैंक?", "loupe_worldbank"),
    (17, 0.00, 4.91, "ai_079_mumbai_slum_highrise_boundary.jpg", "Rank #136 Out of 190 Countries Revealed", "190 देशों में हम 136वें नंबर पर आते हैं!", "loupe_worldbank"),
    (18, 0.00, 9.34, "ai_05_global_superpowers_per_capita_towers.jpg", "USA $85,000: 31x Higher Global Comparison Diagram", "ज़रा ग्लोबल सुपरपावर्स से कम्पेयर कीजिए: अमेरिका की पर कैपिटा इनकम 85,000 डॉलर्स है— भारत से 31 गुना ज़्यादा!", "diagram_per_capita"),
    (19, 0.00, 6.00, "ai_077_germany_munich_engineering_street.jpg", "Germany $54,000: 20x Higher Disparity", "जर्मनी की पर कैपिटा इनकम 54,000 डॉलर्स है— भारत से 20 गुना ज़्यादा!", "diagram_per_capita"),
    (20, 0.00, 9.28, "ai_078_shanghai_pudong_financial_towers.jpg", "China $13,500: 5x Higher per Capita Disparity", "और चीन, जिससे हम कम्पीट करते हैं, उनकी पर कैपिटा इनकम 13,500 डॉलर्स है— भारत से 5 गुना ज़्यादा!", "diagram_per_capita"),
    (21, 0.00, 12.56, "ai_076_us_suburban_affluence_home.jpg", "Developing Nation Lower-Middle-Income Trap", "यानी एग्रीगेट जीडीपी में हम पांचवें हैं क्योंकि हमारी आबादी विशाल है, लेकिन पर-कैपिटा ख़ुशहाली में हम अभी भी एक डेवलपिंग नेशन हैं...", "ken_burns"),

    # --- CHAPTER 3: The K-Shaped Economy: Who Is Actually Spending? (173.16s - 276.75s) [15 beats] ---
    (22, 0.00, 4.69, "ai_06_k_shaped_economic_divergence.jpg", "Where is the 7.8% Growth Actually Coming From?", "तो फिर यह 7.8% की ग्रोथ आ कहां से रही है?", "ken_burns"),
    (23, 0.00, 3.70, "ai_06_k_shaped_economic_divergence.jpg", "Economists Define the 'K-Shaped Recovery'", "इकॉनॉमिस्ट्स इसे कहते हैं 'के-शेप्ड रिकवरी'।", "diagram_k_shape"),
    (24, 0.00, 5.64, "ai_067_k_shaped_arms_converging_concept.jpg", "Two Halves of Economy Moving in Opposite Directions", "के-शेप का मतलब है कि इकॉनमी के दो हिस्से दो अलग-अलग दिशाओं में जा रहे हैं।", "diagram_k_shape"),
    (25, 0.00, 10.33, "ai_07_luxury_suv_gurugram_cybercity.jpg", "Upper Arm of K: Top 10-15% Financial Capital Owners", "के का ऊपर वाला डंडा: देश के टॉप 10 से 15 परसेंट लोग जिनके पास फ़ाइनेंशियल एसेट्स हैं, स्टॉक्स हैं, या हाई-पेइंग कॉर्पोरेट जॉब्स हैं।", "diagram_k_shape"),
    (26, 0.00, 2.64, "ai_080_luxury_car_dealership_showroom.jpg", "Growth is Real for Wealthy Asset Owners", "इनके लिए ग्रोथ बहुत रियल है!", "ken_burns"),
    (27, 0.00, 5.09, "ai_080_luxury_car_dealership_showroom.jpg", "16 Crore Demat Accounts Surge in Stock Market", "स्टॉक मार्केट में 16 करोड़ से ज़्यादा डीमैट अकाउंट्स खुल चुके हैं।", "ken_burns"),
    (28, 0.00, 6.78, "ai_07_luxury_suv_gurugram_cybercity.jpg", "₹10-Crore Luxury Apartments Selling Out in Hours", "गुरुग्राम और मुंबई में 10-10 करोड़ के लग्ज़री अपार्टमेंट्स लॉन्च होते ही घंटों में बिक जाते हैं!", "ken_burns"),
    (29, 0.00, 7.89, "ai_080_luxury_car_dealership_showroom.jpg", "SIAM Official Automobile Flash Report Evidence", "इसका सबसे सॉलिड सबूत देता है सियाम यानी सोसाइटी ऑफ़ इंडियन ऑटोमोबाइल मैन्युफैक्चरर्स का अफ़िशल डेटा।", "highlighter_siam"),
    (30, 0.00, 9.60, "ai_07_luxury_suv_gurugram_cybercity.jpg", "Luxury SUV Sales Heavy Surge (+24.5%)", "लग्ज़री एसयूवीज़ और 20 लाख से महंगी गाड़ियों की सेल्स में पिछले दो सालों में 24.5% का भारी उछाल आया है!", "highlighter_siam"),
    (31, 0.00, 6.50, "ai_017_alto_wagonr_empty_showroom.jpg", "Lower Arm of K: Entry-Level Small Cars Collapse", "लेकिन अब के का नीचे वाला डंडा देखिए: एंट्री-लेवल छोटी गाड़ियां— जैसे मारुति ऑल्टो और वैगनआर—", "ken_burns"),
    (31, 6.50, 6.53, "ai_017_alto_wagonr_empty_showroom.jpg", "Alto & WagonR Sales Drop -42% vs 2018", "इनकी सेल्स 2018 के मुक़ाबले माइनस 42% गिर चुकी हैं!", "ken_burns"),
    (32, 0.00, 8.40, "ai_08_rural_village_stagnant_two_wheelers.jpg", "Rural 100cc Motorcycles Sales Still -14% vs 2019", "रूरल एरियाज़ की जान कहलाने वाली एंट्री-लेवल मोटरसाइकिल्स की बिक्री अभी भी 2019 से 14% नीचे है!", "ken_burns"),
    (33, 0.00, 8.80, "ai_019_pmgkay_ration_queue_morning.jpg", "80 Crore Citizens Dependent on PMGKAY Free Rations", "और सबसे बड़ा सबूत: भारत सरकार आज भी 80 करोड़ नागरिकों को पीएमजीकेएवाई स्कीम के तहत मुफ़्त अनाज दे रही है।", "ken_burns"),
    (34, 0.00, 4.35, "ai_082_ration_shop_biometric_thumbprint.jpg", "If Real Incomes Were Rising at Ground Level...", "अगर ग्राउंड लेवल पर हर व्यक्ति की आमदनी बढ़ रही होती,", "ken_burns"),
    (35, 0.00, 5.66, "ai_018_rural_monsoon_tractor_loan.jpg", "Why 57% of Population Dependent on Free Ration?", "तो देश की 57% जनसंख्या को मुफ़्त राशन पर डिपेंड क्यों रहना पड़ता?", "ken_burns"),

    # --- CHAPTER 4: The Household Balance Sheet Crisis (276.75s - 356.11s) [14 beats] ---
    (36, 0.00, 9.58, "ai_020_rbi_fort_mumbai_headquarters_facade.jpg", "Reserve Bank of India Financial Stability Report", "अब आते हैं उस सबूत पर जिसे हर परिवार को समझना बेहद ज़रूरी है: रिज़र्व बैंक ऑफ़ इंडिया का अफ़िशल फ़ाइनेंशियल स्टेबिलिटी रिपोर्ट।", "highlighter_rbi"),
    (37, 0.00, 12.81, "ai_021_household_savings_antique_piggybank.jpg", "Net Household Savings Crash to 5.3% (50-Year Low)", "आरबीआई के डेटा के मुताबिक़, इंडियन फैमिलीज़ की नेट फ़ाइनेंशियल सेविंग्स गिर कर जीडीपी के 5.3% पर आ चुकी है— जो पिछले 50 सालों का सबसे निचला स्तर है!", "highlighter_rbi"),
    (38, 0.00, 5.03, "ai_069_indian_family_savings_revival_bank.jpg", "Historical 8-9% Indian Family Savings Benchmark", "आमतौर पर इंडियन फैमिलीज़ 8 से 9 परसेंट सेव करती थीं।", "ken_burns"),
    (39, 0.00, 8.78, "ai_022_medical_emergency_hospital_bills.jpg", "Out-of-Pocket Healthcare & School Fees Eating Savings", "लेकिन आज बीमारी के ख़र्चे, फ़ीस, और महंगाई की वजह से आम परिवार अपनी पुरानी सेविंग्स तोड़कर घर चला रहे हैं।", "ken_burns"),
    (40, 0.00, 6.00, "ai_024_household_debt_45pct_record_high.jpg", "Household Debt-to-GDP Hits All-Time High 45.8%", "सेविंग्स कम हुईं, और दूसरी तरफ़ हाउसहोल्ड डेट यानी परिवारों पर क़र्ज़ का बोझ बढ़कर जीडीपी के 45.8% पर पहुंच गया—", "highlighter_rbi"),
    (40, 6.00, 6.05, "ai_083_rbi_vault_door_steel_bars.jpg", "Historical Record Debt Spike Documented", "हिस्टोरिकल रिकॉर्ड हाई!", "highlighter_rbi"),
    (41, 0.00, 5.34, "ai_084_unsecured_loan_rejection_anxiety.jpg", "Debt Taken Not for Asset Creation but Survival", "और चिंता की बात यह है कि यह क़र्ज़ घर बनाने के लिए नहीं लिया जा रहा।", "ken_burns"),
    (42, 0.00, 6.30, "ai_028_bank_branch_loan_officer_desk.jpg", "Retail Bank Credit: 58.2% in Unsecured Loans", "बैंक रिटेल लोन्स का 58.2% हिस्सा अनसिक्योर्ड कंजम्पशन लोन्स में जा रहा है—", "diagram_debt_flow"),
    (42, 6.30, 6.30, "ai_025_smartphone_emi_bnpl_notifications.jpg", "Instant Lending Apps, Credit Cards & BNPL Surge", "यानी पर्सनल लोन्स, क्रेडिट कार्ड आउटस्टैंडिंग, और बाय नाउ पे लेटर ऐप्स!", "diagram_debt_flow"),
    (43, 0.00, 7.56, "ai_026_credit_card_swipe_pos_terminal.jpg", "Mortgaging Tomorrow's Income to Pay Monthly EMIs", "आम मिडिल-क्लास इंसान अपने मंथली ख़र्चे और ईएमआई भरने के लिए आने वाले कल की आमदनी गिरवी रख रहा है।", "diagram_debt_flow"),
    (44, 0.00, 5.49, "ai_029_borrowed_consumption_bubble_concept.jpg", "Consumption Growth Built on Borrowed Time", "यह कंजम्पशन बढ़ रही है, लेकिन यह ग्रोथ उधार के पैसे पर टिकी हुई है!", "diagram_debt_flow"),

    # --- CHAPTER 5: The Missing Factory: Why Manufacturing Won't Take Off (356.11s - 442.72s) [16 beats] ---
    (45, 0.00, 3.43, "ai_030_the_missing_factory_blueprint_floor.jpg", "Why Did This Structural Economic Deficit Happen?", "लेकिन आख़िर यह प्रॉब्लम क्रिएट क्यों हुई?", "ken_burns"),
    (46, 0.00, 6.41, "ai_012_the_missing_factory_shenzhen_comparison.jpg", "The Missing Pillar: 'The Missing Factory'", "क्योंकि भारत के इकनॉमिक स्ट्रक्चर में एक बहुत बड़ा पिलर ग़ायब है: द मिसिंग फ़ैक्ट्री!", "diagram_missing_factory"),
    (47, 0.00, 9.37, "ai_031_shenzhen_automated_electronics_line.jpg", "Global Powers Built Mass Manufacturing First", "दुनिया के हर बड़े देश ने— चाहे वो अमेरिका हो, जापान हो, या चीन— सबने पहले मास-मैन्युफैक्चरिंग खड़ी की।", "diagram_missing_factory"),
    (48, 0.00, 7.59, "ai_032_garment_textile_mill_bangladesh_vietnam.jpg", "Farm Labor Absorbed into Textile & Electronics Mills", "खेत में काम करने वाले करोड़ों लोगों को कपड़ा, इलेक्ट्रॉनिक्स, और ऑटोमोटिव फ़ैक्ट्रीज़ में जॉब्स मिलीं।", "diagram_missing_factory"),
    (49, 0.00, 8.77, "ai_086_vietnam_samsung_factory_complex.jpg", "China 27% Mfg Share Lifted 80 Crore Out of Poverty", "चीन की जीडीपी में मैन्युफैक्चरिंग का शेयर 27% है, जिससे उन्होंने 80 करोड़ लोगों को ग़रीबी से निकाला।", "ken_burns"),
    (50, 0.00, 2.39, "ai_033_it_tech_park_glass_facade_bengaluru.jpg", "What Happened in India's Growth Trajectory?", "लेकिन भारत में क्या हुआ?", "ken_burns"),
    (51, 0.00, 5.92, "ai_033_it_tech_park_glass_facade_bengaluru.jpg", "Leaping Directly from Agriculture to IT Services", "हमने एग्रीकल्चर से सीधे आईटी और सॉफ़्टवेयर सर्विसेज़ पर छलांग लगा दी।", "diagram_missing_factory"),
    (52, 0.00, 3.82, "ai_087_it_office_night_cubicles_tired.jpg", "IT & Financial Services Sector Growing at 12.1%", "हमारे आईटी और फ़ाइनेंशियल सर्विसेज़ सेक्टर", "ken_burns"),
    (53, 0.00, 11.76, "ai_034_college_graduates_unemployed_queue.jpg", "IT Services Can Only Employ Elite College Degrees", "12.1% पर ग्रो कर रहे हैं— जो बहुत अच्छी बात है, लेकिन वो सिर्फ़ उन लोगों को एम्प्लॉय कर सकते हैं जिनके पास इंग्लिश और एडवांस्ड कॉलेज डिग्री हो!", "ken_burns"),
    (54, 0.00, 10.12, "ai_013_agriculture_45pct_workforce_chokepoint.jpg", "45.4% Workforce Stuck in Farming (Only 15% GDP)", "नतीजा यह है कि भारत के 45.4% मज़दूर आज भी खेती में लगे हैं— जो जीडीपी में सिर्फ़ 15% कंट्रीब्यूट करता है!", "ken_burns"),
    (55, 0.00, 5.70, "ai_037_make_in_india_lion_empty_shed.jpg", "Manufacturing Stagnant at 15.8% for 30 Years", "और देश में मैन्युफैक्चरिंग का शेयर पिछले 30 सालों से 15.8% पर अटका हुआ है,", "highlighter_mfg"),
    (55, 5.70, 5.79, "ai_085_empty_industrial_plot_signboard.jpg", "Make in India Official Target Was 25%", "जबकि मेक इन इंडिया का अफ़िशल टारगेट 25% था।", "highlighter_mfg"),
    (56, 0.00, 7.66, "ai_089_make_in_india_factory_assembly_worker.jpg", "Without Factories, Where Will Rural Youth Find Jobs?", "जब तक फ़ैक्ट्रीज़ नहीं लगेंगी, तब तक खेत से निकलने वाले आम युवा को इज़्ज़तदार नौकरी कहां से मिलेगी?", "ken_burns"),

    # --- CHAPTER 6: The 2045 Demographic Clock (442.72s - 525.70s) [13 beats] ---
    (57, 0.00, 7.07, "ai_041_youth_demographic_dividend_class.jpg", "The Most Dangerous Crossroads: 2045 Clock", "और यहीं हम पहुंचते हैं सबसे डेंजरस मोड़ पर: द 2045 डेमोग्राफिक क्लॉक।", "ken_burns"),
    (58, 0.00, 7.51, "ai_014_youth_demographic_clock_2045.jpg", "India Median Age is 28.4 Years (Youngest Nation)", "भारत की मीडियन एज आज सिर्फ़ 28.4 साल है— हम दुनिया के सबसे युवा देशों में से हैं।", "diagram_demographic_clock"),
    (59, 0.00, 5.35, "ai_042_railway_recruitment_exam_crowd.jpg", "1.1 Crore Youth Enter Job Market Every Year", "हर साल लगभग 1 करोड़ 10 लाख युवा जॉब मार्केट में दाख़िल होते हैं।", "diagram_demographic_clock"),
    (60, 0.00, 3.74, "ai_090_college_graduates_convocation_caps.jpg", "This Could Be Our Greatest Strength...", "यह हमारी सबसे बड़ी ताक़त बन सकती थी।", "ken_burns"),
    (61, 0.00, 10.77, "ai_042_railway_recruitment_exam_crowd.jpg", "Without Formal Jobs, Dividend Becomes Disaster", "लेकिन अगर इन 1.1 करोड़ युवाओं के लिए हाई-पेइंग फ़ॉर्मल जॉब्स क्रिएट नहीं हुईं, तो यह डेमोग्राफिक डिविडेंड एक डेमोग्राफिक डिज़ास्टर में बदल सकता है!", "ken_burns"),
    (62, 0.00, 10.17, "ai_044_fertility_rate_drop_family_kerala.jpg", "NFHS Data: Fertility Rate Hits 2.0 (Below Replacement)", "नेशनल फैमिली हेल्थ सर्वे के मुताबिक़, भारत का टोटल फ़र्टिलिटी रेट 2.0 पर आ चुका है— जो रिप्लेसमेंट लेवल से नीचे है।", "highlighter_nfhs"),
    (63, 0.00, 5.18, "ai_045_aging_population_elderly_care_rural.jpg", "South India & States Population Already Ageing", "साउथ इंडिया और कई राज्यों में आबादी पहले से बूढ़ी होने लगी है।", "ken_burns"),
    (64, 0.00, 6.25, "ai_043_digital_clock_2045_countdown_horizon.jpg", "Experts Project Window Closes strictly by 2045", "एक्सपर्ट्स का कहना है कि हमारी डेमोग्राफिक खिड़की सिर्फ़ 2045 तक खुली है!", "diagram_demographic_clock"),
    (65, 0.00, 3.61, "ai_092_clock_tower_shadow_sunset.jpg", "After 2045, India Begins Aging Rapidly", "उसके बाद भारत बूढ़ा होना शुरू हो जाएगा।", "diagram_demographic_clock"),
    (66, 0.00, 7.80, "ai_046_social_security_pension_desert.jpg", "Need $10,000 Per Capita in 15-18 Years", "अगर अगले 15 से 18 सालों में हमने पर कैपिटा इनकम को 10,000 डॉलर्स तक नहीं पहुंचाया,", "diagram_demographic_clock"),
    (66, 7.80, 7.86, "ai_047_middle_income_trap_concept_gate.jpg", "Risk: Getting Old Before Getting Rich", "तो भारत अमीर बनने से पहले बूढ़ा हो जाएगा— बिना सोशल सिक्योरिटी, बिना पेंशन, और बिना मज़बूत पब्लिक हेल्थकेयर के!", "diagram_demographic_clock"),

    # --- CHAPTER 7: The Road Ahead & Citizen Verdict (525.70s - 608.35s) [17 beats] ---
    (67, 0.00, 2.08, "ai_050_reform_pillar_1_factory_sheds.jpg", "What is the Actionable Roadmap?", "तो सॉल्यूशन क्या है?", "ken_burns"),
    (68, 0.00, 4.59, "ai_050_reform_pillar_1_factory_sheds.jpg", "GDP Celebration Won't Fill Citizens' Stomachs", "सिर्फ़ हेडलाइन जीडीपी का जश्न मनाने से पेट नहीं भरेगा।", "ken_burns"),
    (69, 0.00, 13.25, "ai_051_garment_stitching_women_workforce.jpg", "Pillar 1: Labor-Intensive Mfg in Garments & Food", "भारत को तुरंत 4 बड़े क़दम उठाने होंगे: पहला: लेबर-इंटेंसिव मैन्युफैक्चरिंग— गारमेंट्स, फ़ुटवियर, और एग्रो-प्रोसेसिंग में रेड-टेप ख़त्म करके मैसिव स्केल पर फ़ैक्ट्रीज़ लगाना।", "diagram_reforms"),
    (70, 0.00, 1.50, "ai_055_tax_relief_middle_class_family_relief.jpg", "Pillar 2 Introduction", "दूसरा:", "diagram_reforms"),
    (71, 0.00, 9.22, "ai_056_health_insurance_gst_removal_concept.jpg", "Pillar 2: Middle-Class Tax Relief & 18% GST Removal", "मिडिल-क्लास पर टैक्स रिलीफ— हेल्थ इंश्योरेंस पर 18% जीएसटी जैसे बोझ को हटाकर परिवारों की सेविंग्स को प्रोटेक्ट करना।", "diagram_reforms"),
    (72, 0.00, 9.85, "ai_054_solar_cold_storage_rural_cluster.jpg", "Pillar 3: Agro Cold-Chain & Food Processing in Villages", "तीसरा: एग्रीकल्चर में कोल्ड-चेन और फ़ूड प्रोसेसिंग को गांव-गांव पहुंचाना, ताकि किसान की आमदनी सिर्फ़ फ़सल बेचने तक सीमित न रहे।", "diagram_reforms"),
    (73, 0.00, 6.39, "ai_057_vocational_skill_iti_robotics_lab.jpg", "Pillar 4: Direct Industrial Vocational Skilling", "और चौथा: डिग्री-बाज़ी के बजाय डायरेक्ट इंडस्ट्रियल वोकेशनल स्किलिंग पर फ़ोकस करना।", "diagram_reforms"),
    (74, 0.00, 8.40, "ai_058_ev_battery_assembly_line_india.jpg", "7.8% GDP is an Achievement, Not the Destination", "7.8% जीडीपी ग्रोथ एक शानदार अचीवमेंट है, लेकिन यह मंज़िल नहीं, सिर्फ़ एक नंबर है।", "ken_burns"),
    (75, 0.00, 6.40, "ai_068_per_capita_rank_top_50_milestone.jpg", "Real Growth: India Per-Capita Moving to Top 50", "असली विकास तब माना जाएगा जब भारत का पर-कैपिटा रैंक 136 से निकल कर टॉप 50 में पहुंचेगा,", "ken_burns"),
    (75, 6.40, 6.43, "ai_015_vocational_skilling_and_reforms_future.jpg", "Families Advancing on Savings, Not Borrowed Debt", "और हर आम परिवार क़र्ज़ के सहारे नहीं, अपनी बचत के दम पर आगे बढ़ेगा।", "ken_burns"),
    (76, 0.00, 3.53, "ai_101_benaqaab_investigative_ledger_desk.jpg", "What Do You Think About This Ground Reality?", "आप इस ग्राउंड रियलिटी के बारे में क्या सोचते हैं?", "ken_burns"),
    (77, 0.00, 3.34, "ai_102_citizen_viewing_documentary_tablet.jpg", "Share Your Thoughts in Comments Below", "अपने विचार कमेंट में ज़रूर शेयर करें।", "ken_burns"),
    (78, 0.00, 6.08, "ai_103_india_gate_tricolor_dusk.jpg", "Sach, Saboot, Bebak — Keep Watching Benaqaab India", "सच, सबूत, और बेबाकी के साथ— देखते रहिए बेनाक़ाब इंडिया।", "ken_burns"),
    (79, 0.00, 1.57, "ai_105_final_verdict_stamp_cinematic_climax.jpg", "Jai Hind! Final Verdict Reality Unveiled", "जय हिंद!", "verdict_stamp")
]

print(f"🎬 Total beats defined in plan: {len(PLAN_105)}")

# Build mathematically seamless intervals spanning 0.0s to 608.35s
beats_sheet = []
for i, item in enumerate(PLAN_105):
    s_idx, sub_off, sub_dur, fname, subj, desc, mtype = item
    sent = boundaries[s_idx]
    base_st = sent["offset"]
    
    st = round(base_st + sub_off, 2)
    en = round(st + sub_dur, 2)
    
    # Clamp first to 0.0s and ensure seamless continuity with previous
    if i == 0:
        st = 0.0
    else:
        st = beats_sheet[i-1]["end_s"]
    
    # If last beat, clamp end to total_dur
    if i == len(PLAN_105) - 1:
        en = round(total_dur, 2)
    
    # Ensure en > st
    if en <= st:
        en = round(st + max(0.5, sub_dur), 2)
    
    # Determine Chapter Name
    mid = (st + en) / 2
    if mid < 83.45: chap = "Chapter 1: The Global Celebration vs Street Reality"
    elif mid < 173.16: chap = "Chapter 2: The Per-Capita Illusion: 5th Largest vs 136th Rank"
    elif mid < 276.75: chap = "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?"
    elif mid < 356.11: chap = "Chapter 4: The Household Balance Sheet Crisis"
    elif mid < 442.72: chap = "Chapter 5: The Missing Factory: Why Manufacturing Won't Take Off"
    elif mid < 525.70: chap = "Chapter 6: The 2045 Demographic Clock"
    else: chap = "Chapter 7: The Road Ahead & Citizen Verdict"

    beat_obj = {
        "beat_id": i + 1,
        "chapter": chap,
        "start_s": st,
        "end_s": en,
        "duration_s": round(en - st, 2),
        "asset_path": f"assets/ai_plates/{fname}",
        "fallback_path": f"assets/ai_plates/{fname}",
        "target_ai_plate": fname,
        "subject": subj,
        "hindi_desc": desc,
        "motion_type": mtype
    }
    beats_sheet.append(beat_obj)

print(f"✅ Built {len(beats_sheet)} beats. First: {beats_sheet[0]['start_s']}s, Last end: {beats_sheet[-1]['end_s']}s")

# Save BEAT_SHEET.json
with open(DIR / "BEAT_SHEET.json", "w", encoding="utf-8") as f:
    json.dump(beats_sheet, f, indent=2, ensure_ascii=False)

# Save beats.js
with open(DIR / "beats.js", "w", encoding="utf-8") as f:
    f.write("window.BEATS_DATA = " + json.dumps(beats_sheet, indent=2, ensure_ascii=False) + ";\n")

print("💾 Saved BEAT_SHEET.json and beats.js successfully!")
