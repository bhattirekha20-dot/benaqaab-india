import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DIR = Path(__file__).parent
TIMESTAMPS_JSON = DIR / "word_timestamps.json"
OUTPUT_FILE = DIR / "AI_IMAGE_GENERATION_PROMPTS_MASTER.md"

with open(TIMESTAMPS_JSON, "r", encoding="utf-8") as f:
    ts_data = json.load(f)

boundaries = ts_data["boundaries"]
total_dur = ts_data["duration"]

# Create EXACTLY 105 intervals by splitting the 25 longest sentences across the full 608.35s runtime
sorted_by_dur = sorted([(i, float(b['duration'])) for i, b in enumerate(boundaries)], key=lambda x: x[1], reverse=True)
split_indices = set([x[0] for x in sorted_by_dur[:25]])

intervals = []
for i, b in enumerate(boundaries):
    offset = float(b['offset'])
    dur = float(b['duration'])
    text = b['text'].strip()
    if i in split_indices:
        half = round(dur / 2, 2)
        intervals.append((offset, round(offset + half, 2), text))
        intervals.append((round(offset + half, 2), round(offset + dur, 2), text))
    else:
        intervals.append((offset, round(offset + dur, 2), text))

# Clamp first start to 0.0s and last end to total_dur
intervals[0] = (0.0, intervals[0][1], intervals[0][2])
intervals[-1] = (intervals[-1][0], round(total_dur, 2), intervals[-1][2])

print(f"Total intervals prepared: {len(intervals)}, spanning {intervals[0][0]}s to {intervals[-1][1]}s")

def get_chapter(t):
    if t < 85: return ("Chapter 1", "The Global Celebration vs Street Reality")
    elif t < 175: return ("Chapter 2", "The Per-Capita Illusion: 5th Largest vs 136th Rank")
    elif t < 275: return ("Chapter 3", "The K-Shaped Economy: Who Is Actually Spending?")
    elif t < 355: return ("Chapter 4", "The Household Balance Sheet Crisis")
    elif t < 445: return ("Chapter 5", "The Missing Factory: Why Manufacturing Won't Take Off")
    elif t < 525: return ("Chapter 6", "The 2045 Demographic Clock")
    else: return ("Chapter 7", "The Road Ahead & Citizen Verdict")

# 16 existing plates mapping
EXISTING = {
    1: ("ai_01_global_gdp_celebration_bull.jpg", "BSE Charging Bull & 7.8% Headline Euphoria", "A photorealistic cinematic wide shot of Dalal Street Bombay Stock Exchange at dusk, featuring the iconic bronze charging bull statue illuminated by vibrant neon emerald-green stock ticker arrows and dramatic upward financial charts (+7.8%), high micro-contrast, volumetric atmospheric fog, specular rim lighting, deep slate obsidian shadows, 8k resolution, shot on Arri Alexa LF 35mm lens --ar 16:9 --style raw --v 6.0"),
    2: ("ai_03_middle_class_kitchen_table_inflation.jpg", "Middle-Class Living Room Ledger & Inflation Squeeze", "An intimate, poignant documentary photograph of an authentic Indian middle-class home dining room at night; on a dark wooden table sits an open handwritten household expense ledger book alongside electricity bills, school fee receipts, grocery slips, and a digital calculator displaying accumulating expenses, warm single overhead tungsten lamp casting soft shadows, shallow depth of field, moody editorial photojournalism, cinematic realism --ar 16:9 --v 6.0 --style raw"),
    3: ("ai_09_pmgkay_free_ration_distribution.jpg", "80 Crore Citizens on Free Foodgrains (PMGKAY)", "An authentic documentary photograph of an official government Fair Price Shop ration depot in semi-rural India; neatly stacked burlap sacks of wheat and rice stamped with official food corporation marks, rural women and elderly citizens holding biometric ration cards waiting in an orderly queue under a tin roof, dignified and authentic editorial photojournalism, natural soft daylight, Reuters documentary standard --ar 16:9 --v 6.0 --style raw"),
    4: ("ai_02_parliament_cabinet_national_accounts.jpg", "Indian Parliament Sansad Bhawan & National Accounts", "Majestic architectural low-angle wide shot of the Indian Parliament building at blue hour twilight, national Ashoka pillar emblem subtly backlit with warm saffron and white specular rim light, clean ceremonial boulevard reflection in the foreground, faint digital holographic streams of national economic accounts and MoSPI statistics floating subtly in the air, hyper-detailed, photorealistic documentary realism --ar 16:9 --v 6.0 --style raw"),
    5: ("ai_01_global_gdp_celebration_bull.jpg", "Headline 7.8% Euphoria vs Hidden Reality", "Cinematic macro shot of glowing green financial tickers and digital numbers displaying '+7.8% GDP' reflected in the sunglasses of an investor on Dalal Street, deep obsidian shadows, moody high contrast --ar 16:9 --v 6.0"),
    6: ("ai_01_global_gdp_celebration_bull.jpg", "Deconstructing 7.8% Ground Reality", "A dramatic wide shot of a giant glass financial skyscraper split down the middle by a ray of light, contrasting booming stock indices with street-level retail reality, documentary style --ar 16:9 --v 6.0"),
    7: ("ai_02_parliament_cabinet_national_accounts.jpg", "Channel Identity & Subscribe/Like CTA Backdrop", "Majestic illuminated front facade of Indian Parliament Sansad Bhawan with glowing tricolor lights reflecting on wet pavement at blue hour --ar 16:9 --v 6.0"),
    8: ("ai_02_parliament_cabinet_national_accounts.jpg", "MoSPI National Accounts Formulation Desk", "Official government press conference room with empty wooden podium and Indian national emblem, soft dramatic lighting --ar 16:9 --v 6.0"),
    9: ("ai_03_middle_class_kitchen_table_inflation.jpg", "The Living Cost Disconnect & Vanishing Savings", "Close-up of a calculator and handwritten monthly expense notebook with grocery bills, warm moody tungsten light --ar 16:9 --v 6.0"),
    10: ("ai_04_crowded_mumbai_commuter_train.jpg", "1.43 Billion Population Multiplier", "High-angle cinematic documentary photograph of thousands of Indian commuters walking through the magnificent stone arches of Chhatrapati Shivaji Terminus station in Mumbai during morning rush hour, capturing the monumental scale of India's 1.43 billion population moving with intense purpose, dramatic diagonal shafts of golden morning sunlight piercing through dust motes, 35mm documentary photojournalism, National Geographic editorial grade --ar 16:9 --v 6.0"),
    11: ("ai_04_crowded_mumbai_commuter_train.jpg", "Dividing National Wealth Across 143 Crore Citizens", "Crowded Mumbai local train platform packed with daily commuters under metal roof trusses, cinematic natural daylight, editorial realism --ar 16:9 --v 6.0"),
    12: ("ai_05_global_superpowers_per_capita_towers.jpg", "Global Income Divide: US $85k vs India $2,730", "A surreal, high-concept split-screen architectural comparison: on the left side, towering illuminated glass skyscrapers of Downtown Manhattan NYC and Frankfurt Germany at dusk glowing with immense institutional wealth; on the right side, dense low-rise developing residential housing in an Indian metropolis, visually conveying the 31-fold per-capita income divide ($85,300 vs $2,730), moody twilight sky, high dynamic range, editorial financial cinema --ar 16:9 --v 6.0 --style raw"),
    13: ("ai_05_global_superpowers_per_capita_towers.jpg", "Superpowers Wealth Gap: Germany & China Comparison", "Illuminated modern skyline of Frankfurt financial district with ECB tower reflecting in river Main at twilight, high contrast cinematic photography --ar 16:9 --v 6.0"),
    14: ("ai_06_k_shaped_economic_divergence.jpg", "The 3D K-Shaped Economic Divergence Stage", "A sleek futuristic dark-mode financial infographic stage; a monumental glowing 3D letter 'K' crafted with frosted glassmorphism on an obsidian slate reflective floor: the upper arm glowing brilliant neon emerald-green rising sharply upward labeled (+24.5% Luxury Boom), the lower arm glowing deep crimson red plunging downward labeled (-42% Wage Contraction), subtle volumetric floor mist, crisp specular rim highlights, Bloomberg investigative documentary aesthetics --ar 16:9 --v 6.0"),
    15: ("ai_07_luxury_suv_gurugram_cybercity.jpg", "Upper Arm of K: Luxury SUVs & CyberCity Wealth", "A brand new luxury black metallic full-size SUV with sleek glowing LED matrix headlights parked in front of a soaring illuminated glass skyscraper plaza in DLF CyberCity Gurugram at night, sharp specular reflections of glowing corporate office windows on the polished car hood, wet asphalt reflections, affluent executive silhouette walking into the lobby, ultra-sharp 8k automotive editorial photography --ar 16:9 --v 6.0 --style raw"),
    16: ("ai_08_rural_village_stagnant_two_wheelers.jpg", "Lower Arm of K: Rural Two-Wheeler Stagnation", "A dusty roadside country tea stall along a rural highway in Uttar Pradesh during hot dry midday; an older 100cc Indian commuter motorcycle covered in fine road dust parked beside an arid unplowed agricultural field, heat shimmer shimmering on the asphalt horizon, quiet stillness capturing the economic stagnation of mass rural households, authentic documentary photojournalism, raw editorial lighting --ar 16:9 --v 6.0")
}

# The remaining 89 bespoke visual prompts for Beats 17 to 105
EXPANDED_PROMPTS = [
    # Chapter 3 & 4 (Beats 17 to 40)
    ("ai_017_alto_wagonr_empty_showroom.jpg", "Small Car Showroom Contraction (-42%)", 
     "A quiet, dimly lit automobile dealership showroom in a tier-2 Indian city; a silver entry-level small hatchback sitting on clean tiles with no customers around, a lone salesman looking out the glass window, capturing the -42% collapse in entry-level passenger vehicle sales, cinematic documentary lighting, 35mm lens --ar 16:9 --v 6.0 --style raw"),

    ("ai_018_rural_monsoon_tractor_loan.jpg", "Agrarian Household Debt & Monsoon Vulnerability",
     "A weathered Indian farmer standing beside a parked tractor in a rain-soaked rural village lane at dusk, holding land revenue papers under an umbrella, atmospheric village lighting, authentic rural realism, National Geographic photojournalism --ar 16:9 --v 6.0"),

    ("ai_019_pmgkay_ration_queue_morning.jpg", "57% of Nation Dependent on Free Foodgrains",
     "Long, orderly queue of rural Indian citizens holding ration cards in the early morning fog outside a government food grain godown, morning sunlight filtering through mist, dignified editorial documentary photography --ar 16:9 --v 6.0"),

    ("ai_020_rbi_fort_mumbai_headquarters_facade.jpg", "Reserve Bank of India Monetary Policy Gate",
     "Imposing stone colonial entrance of the Reserve Bank of India in Fort Mumbai during monsoon twilight, police guard in silhouette, wet street reflections, cinematic investigative lighting --ar 16:9 --v 6.0"),

    ("ai_021_household_savings_antique_piggybank.jpg", "Net Household Savings Crashing to 5.3%",
     "A heavy brass antique Indian piggy bank (gullak) cracked open on a dark polished mahogany table, exposing only a few scattered rupee coins and folded utility bills, soft dramatic spotlight, dark obsidian background, powerful editorial concept photography --ar 16:9 --v 6.0 --style raw"),

    ("ai_022_medical_emergency_hospital_bills.jpg", "Out-of-Pocket Healthcare Depleting Family Wealth",
     "An anxious Indian family waiting on plastic chairs in a dimly lit hospital corridor at night; a man looking at a lengthy itemized medical invoice and prescription receipts, conveying out-of-pocket health expense shocks, intimate documentary realism --ar 16:9 --v 6.0"),

    ("ai_023_school_coaching_fee_tuition_burden.jpg", "Rising Education Inflation on Middle Class",
     "A focused Indian school student studying under a desk lamp in a small urban bedroom, surrounded by stacks of competitive exam textbooks and coaching class fee brochures, warm tungsten lighting, authentic domestic atmosphere --ar 16:9 --v 6.0"),

    ("ai_024_household_debt_45pct_record_high.jpg", "Household Debt-to-GDP Spikes to 45.8%",
     "A dramatic visual metaphor: a sleek miniature model of an Indian suburban home weighed down under a towering stack of metallic bank loan ledgers and credit agreements, dark reflective table, moody amber and crimson studio lighting --ar 16:9 --v 6.0"),

    ("ai_025_smartphone_emi_bnpl_notifications.jpg", "Buy Now Pay Later & Instant Loan Apps Surge",
     "Close-up of an Indian youth's hands holding a smartphone glowing in the dark, displaying multiple digital lending app notifications with 'Pre-Approved Loan ₹50,000' and 'EMI Payment Due Tomorrow', moody neon reflections on fingers, sharp contemporary realism --ar 16:9 --v 6.0"),

    ("ai_026_credit_card_swipe_pos_terminal.jpg", "Unsecured Debt Squeezing Future Income",
     "A point-of-sale credit card terminal glowing on a dark retail counter, a silver credit card being tapped to pay for basic grocery essentials, macro shallow depth of field, neon cyan retail reflections, high micro-contrast --ar 16:9 --v 6.0"),

    ("ai_027_pawn_shop_gold_loan_collateral.jpg", "Pledging Gold Ornaments for Working Capital",
     "An authentic traditional Indian goldsmith and NBFC gold loan counter; a digital balance scale weighing a gold necklace beside official pledge receipt papers, warm jeweler's lamp, rich gold reflections, documentary photojournalism --ar 16:9 --v 6.0"),

    ("ai_028_bank_branch_loan_officer_desk.jpg", "Retail Credit Surge vs Deposit Growth Slowdown",
     "A busy public sector bank branch in New Delhi; an officer reviewing retail personal loan applications under fluorescent tube lights, queue of middle-class applicants seated across the counter, documentary realism --ar 16:9 --v 6.0"),

    ("ai_029_borrowed_consumption_bubble_concept.jpg", "Debt-Financed Consumption Bubble Fragility",
     "A conceptual fine art photograph: a glowing glass sphere containing miniature urban skyscrapers and cars resting precariously on an edge, representing growth financed by borrowed consumption rather than wage gains, moody obsidian lighting --ar 16:9 --v 6.0"),

    ("ai_030_the_missing_factory_blueprint_floor.jpg", "The Missing Factory Blueprint on Industrial Ground",
     "An architect's blueprint of a mega manufacturing plant laid out on rough concrete factory foundations, a hard hat and surveyor's level beside it, moody dawn light streaming through unfinished steel pillars --ar 16:9 --v 6.0"),

    ("ai_031_shenzhen_automated_electronics_line.jpg", "East Asian Industrial Miracle Benchmark",
     "Expansive high-tech electronics manufacturing line in Shenzhen, cleanroom suits, robotic pick-and-place machines producing circuit boards at high speed, bright cleanroom illumination, industrial scale --ar 16:9 --v 6.0"),

    ("ai_032_garment_textile_mill_bangladesh_vietnam.jpg", "Labour-Intensive Textile Factories Competitor",
     "Vast garment stitching floor with hundreds of textile sewing stations operating under industrial lights, rolls of colorful fabric stacked high, documenting mass labour absorption in Asian manufacturing hubs --ar 16:9 --v 6.0"),

    ("ai_033_it_tech_park_glass_facade_bengaluru.jpg", "India's High-Tech Services Island",
     "Gleaming glass and steel corporate IT campus in Bengaluru Electronic City at dusk, illuminated skywalks, reflecting pools, software engineers walking with laptops, modern global tech aesthetic --ar 16:9 --v 6.0"),

    ("ai_034_college_graduates_unemployed_queue.jpg", "College Degree vs Industrial Employment Mismatch",
     "Thousands of young Indian job aspirants holding degree folders waiting in a massive recruitment line outside an employment exchange on a hot morning, documentary photojournalism capturing youth job hunger --ar 16:9 --v 6.0"),

    ("ai_035_tractor_plowing_small_fragmented_land.jpg", "Fragmented Landholdings in Indian Agriculture",
     "A small red tractor plowing a tiny one-acre parcel of land partitioned by dirt bunds in Bihar, lush green crops under early morning sun, capturing the economic limitations of fragmented agrarian plots --ar 16:9 --v 6.0"),

    ("ai_036_rural_mandis_crop_spoilage_monsoon.jpg", "Post-Harvest Losses & Missing Cold Chain",
     "A crowded rural agricultural mandi with mounds of harvested tomatoes and onions under open tarpaulins in heavy monsoon rain, unpaved muddy yard, highlighting post-harvest cold storage deficit --ar 16:9 --v 6.0"),

    ("ai_037_make_in_india_lion_empty_shed.jpg", "Make in India 25% Target Missed for 30 Years",
     "A large industrial tin warehouse with steel girders, an official 'Make in India' gear-lion poster hanging on the wall, clean empty concrete floor awaiting machinery, cinematic natural side lighting --ar 16:9 --v 6.0"),

    ("ai_038_automotive_stamping_press_manesar.jpg", "Heavy Precision Stamping Press in Gurgaon-Manesar",
     "Massive 2000-ton hydraulic sheet metal stamping press stamping car doors in an Indian auto plant, sparks, intense metallic reflections, industrial powerhouse photography --ar 16:9 --v 6.0"),

    ("ai_039_informal_small_scale_workshop_dharavi.jpg", "Informal Manufacturing Sector Living Reality",
     "A compact leather and metal craft workshop in an urban cluster; skilled artisans crafting goods under ceiling fans, tools hanging on wooden boards, intimate documentary realism --ar 16:9 --v 6.0"),

    ("ai_040_container_freight_terminal_nhava_sheva.jpg", "Export Logistics & Container Port Bottlenecks",
     "Towering stacks of multi-colored shipping containers at JNPT Nhava Sheva port in Mumbai, giant gantry cranes loading a container vessel at sunset, industrial maritime scale --ar 16:9 --v 6.0"),

    # Chapter 5 & 6: The Demographic Clock & Transition (Beats 41 to 75)
    ("ai_041_youth_demographic_dividend_class.jpg", "India's Median Age: 28.4 Years Advantage",
     "A vibrant classroom of young Indian engineering and polytechnic students working together around circuit boards and 3D printers, bright daylight, optimistic smiles, high human energy --ar 16:9 --v 6.0"),

    ("ai_042_railway_recruitment_exam_crowd.jpg", "1.1 Crore Young Entrants Every Single Year",
     "Massive sea of millions of young Indian candidates gathered outside an examination stadium for railway and civil defense recruitment tests, sea of backpacks and water bottles, epic documentary scale --ar 16:9 --v 6.0"),

    ("ai_043_digital_clock_2045_countdown_horizon.jpg", "The 2045 Demographic Clock Deadline",
     "A dramatic symbolic photograph of a monumental digital countdown clock standing in open salt flats under a thunderous stormy sunset, displaying 'YEAR 2045: WINDOW CLOSES', epic cinematic scale --ar 16:9 --v 6.0"),

    ("ai_044_fertility_rate_drop_family_kerala.jpg", "TFR Drops to 2.0: Below Replacement Level",
     "A modern South Indian nuclear family in a quiet sunlit suburban living room; young parents with one child looking out a window, quiet contemplative mood, domestic realism --ar 16:9 --v 6.0"),

    ("ai_045_aging_population_elderly_care_rural.jpg", "Risk of Getting Old Before Getting Rich",
     "An elderly Indian grandfather with silver hair sitting alone on a wooden charpai cot in an empty village courtyard at dusk, holding a walking stick, evocative portrait of population aging without formal pensions --ar 16:9 --v 6.0"),

    ("ai_046_social_security_pension_desert.jpg", "Absence of Universal Social Security in Informal Sector",
     "A weathered elderly Indian street artisan crafting wicker baskets on a city pavement under twilight streetlights, dignified endurance, documenting the absence of retirement safety nets --ar 16:9 --v 6.0"),

    ("ai_047_middle_income_trap_concept_gate.jpg", "The Middle-Income Trap Chokepoint",
     "A conceptual wide shot: a paved highway stretching toward a massive stone archway labeled '$10,000 PER CAPITA', dramatic stormy clouds parting into golden sunlight, editorial financial cinema --ar 16:9 --v 6.0"),

    ("ai_048_south_korea_industrialization_contrast.jpg", "South Korea / Taiwan Escape to High Income",
     "A visual benchmark: high-speed train gliding past modern semiconductor manufacturing facilities and sleek urban towers in Incheon, symbolizing the path from low income to $35,000 per capita --ar 16:9 --v 6.0"),

    ("ai_049_brazil_middle_income_stagnation.jpg", "The Cautionary Tale of Premature Deindustrialization",
     "A moody urban vista showing industrial smokestacks falling silent beside expanding favela housing, illustrating a nation that stagnated before reaching high income, documentary grade --ar 16:9 --v 6.0"),

    ("ai_050_reform_pillar_1_factory_sheds.jpg", "Reform Pillar 1: Mass Labour-Intensive Manufacturing",
     "Expansive new steel factory sheds under construction in a designated industrial corridor, yellow cranes lifting roof trusses, clean green landscaping, dawn sunrise, optimistic industry --ar 16:9 --v 6.0"),

    ("ai_051_garment_stitching_women_workforce.jpg", "Female Labour Force Participation in Industry",
     "Hundreds of skilled Indian women workers operating modern computerized sewing machines in a bright, clean, air-conditioned garment export factory in Tamil Nadu, dignified economic empowerment --ar 16:9 --v 6.0"),

    ("ai_052_shoe_leather_cluster_agra_tamilnadu.jpg", "Footwear & Leather Clusters Mass Jobs",
     "A modern leather footwear assembly line in Ambur Tamil Nadu; precision laser cutting and stitching of athletic shoes for export, bright industrial daylight, skilled craftsman hands --ar 16:9 --v 6.0"),

    ("ai_053_food_processing_mega_park.jpg", "Reform Pillar 3: Agro-Processing Mega Food Parks",
     "Automated food processing plant packaging mango pulp and dairy products, stainless steel vats, hygienic bottling conveyor belts, vibrant agricultural produce, industrial cleanliness --ar 16:9 --v 6.0"),

    ("ai_054_solar_cold_storage_rural_cluster.jpg", "Solar Cold Storage Preserving Farm Incomes",
     "A solar-powered cold storage warehouse situated right beside rural potato and vegetable farms in Uttar Pradesh; farmers loading crates into temperature-controlled vans, morning sunlight --ar 16:9 --v 6.0"),

    ("ai_055_tax_relief_middle_class_family_relief.jpg", "Reform Pillar 2: Middle-Class Tax & GST Relief",
     "A happy Indian middle-class family seated at their kitchen dining table, looking at a home budget spreadsheet on a laptop with smiles of financial breathing room, warm morning sun --ar 16:9 --v 6.0"),

    ("ai_056_health_insurance_gst_removal_concept.jpg", "Removing 18% GST on Health Insurance",
     "A family health insurance policy document lying on a desk with a medical stethoscope and pen, stamped with an official green seal '100% AFFORDABLE HEALTHCARE', warm reassuring lighting --ar 16:9 --v 6.0"),

    ("ai_057_vocational_skill_iti_robotics_lab.jpg", "Reform Pillar 4: Direct Industrial ITI Skilling",
     "Young Indian polytechnic students in blue safety uniforms programming an industrial robotic arm in a modern ITI skilling centre, computer monitors displaying robotic kinematics, bright futuristic lab --ar 16:9 --v 6.0"),

    ("ai_058_ev_battery_assembly_line_india.jpg", "High-Tech Electric Vehicle Battery Cell Assembly",
     "Pristine battery pack assembly cleanroom in an Indian EV manufacturing facility; technicians in antistatic gowns placing prismatic lithium cells into vehicle trays, cyan LED accents --ar 16:9 --v 6.0"),

    ("ai_059_semiconductor_fab_cleanroom_dholera.jpg", "Semiconductor Fab Cleanroom Milestone",
     "An ultra-clean semiconductor fabrication cleanroom under yellow monochromatic lighting; robotic overhead wafer track moving silicon wafer FOUP pods, high-tech industrial triumph --ar 16:9 --v 6.0"),

    ("ai_060_coastal_industrial_corridor_highway.jpg", "Dedicated Freight Corridors & Coastal Expressways",
     "A multi-lane access-controlled expressway and parallel electrified freight railway line running through scenic Western Ghats, container trucks and freight trains moving at sunset --ar 16:9 --v 6.0"),

    ("ai_061_msme_easy_credit_fintech_portal.jpg", "Deregulating MSMEs and Small Factory Owners",
     "An energetic small factory owner in Pune reviewing digital GST and working capital approvals on a tablet inside his metal fabrication shop, sparks in background, dignified entrepreneurship --ar 16:9 --v 6.0"),

    ("ai_062_women_entrepreneurs_rural_cooperative.jpg", "Rural Women Self-Help Enterprises & Dairy",
     "A modern cooperative dairy collection centre in Gujarat; rural women testing milk purity using digital fat analyzers, stainless steel milk cans, morning sun, community prosperity --ar 16:9 --v 6.0"),

    ("ai_063_apprentice_training_heavy_machinery.jpg", "On-the-Job Apprenticeship Direct Industry Link",
     "A young apprentice being guided by a senior master machinist on a giant industrial lathe machine turning a massive steel turbine shaft, sparks, oil sheen, intergenerational craft transmission --ar 16:9 --v 6.0"),

    ("ai_064_smart_village_broadband_logistics.jpg", "Rural Digital Logistics Hub & Cold Storage",
     "A rural distribution hub with electric delivery vans charging under solar canopies, young rural delivery agents scanning parcels with barcode terminals, modern village transformation --ar 16:9 --v 6.0"),

    ("ai_065_urban_housing_affordable_green_towers.jpg", "Affordable Urban Housing for Factory Workers",
     "Well-designed, tree-lined affordable apartment complex for industrial workers near an manufacturing zone, children playing in a landscaped courtyard, dignified urban living --ar 16:9 --v 6.0"),

    ("ai_066_public_health_primary_clinic_clean.jpg", "Robust Primary Healthcare Preventing Savings Shocks",
     "A spotless, modern public health primary care clinic in rural Punjab; a doctor examining an elderly patient with digital diagnostic tools, clean white aesthetic, accessible care --ar 16:9 --v 6.0"),

    ("ai_067_k_shaped_arms_converging_concept.jpg", "From K-Shaped Divergence to Broad-Based Growth",
     "A symbolic 3D graphic stage: the divergent arms of the 'K' slowly bending and merging into a single wide ascending golden ribbon labeled 'BROAD-BASED PROSPERITY', glowing warm amber light --ar 16:9 --v 6.0"),

    ("ai_068_per_capita_rank_top_50_milestone.jpg", "True Victory: Per-Capita Income Reaching Top 50",
     "A global world map visualization in an investigative studio; India glowing with vibrant cyan light as its rank rises toward the top quartile, high-tech financial newsroom backdrop --ar 16:9 --v 6.0"),

    ("ai_069_indian_family_savings_revival_bank.jpg", "Restoring Family Savings & Wealth Cushion",
     "An Indian family proudly receiving a fixed deposit certificate and savings passbook at a modern bank branch, smiling parents and young children, warm reassuring atmosphere --ar 16:9 --v 6.0"),

    ("ai_070_headline_numbers_unmasked_metaphor.jpg", "Sach Saboot Bebak: Unmasking Economic Headlines",
     "A striking cinematic investigative metaphor: a bold newspaper headline reading '7.8% GDP RECORD' being carefully lifted by a forensic loupe to reveal audited balance sheets underneath, dramatic side lighting --ar 16:9 --v 6.0"),

    # Climax Beats & Remaining Scenes (Beats 71 to 105)
    ("ai_071_dalal_street_bull_night_rain.jpg", "Dalal Street Bull in Rain Reflections",
     "The bronze Dalal Street bull statue reflecting in puddles of evening rain under colorful neon market ticker reflections, atmospheric noir documentary lighting --ar 16:9 --v 6.0"),

    ("ai_072_parliament_dome_tricolor_illumination.jpg", "Sansad Bhawan Central Dome Tricolor Glow",
     "Close-up of the magnificent carved stonework of the Indian Parliament dome bathed in subtle saffron, white, and emerald green architectural illumination at midnight --ar 16:9 --v 6.0"),

    ("ai_073_middle_class_grocery_store_checkout.jpg", "Supermarket Checkout Bill Reality",
     "An Indian shopper looking at a printed grocery receipt with household staples (cooking oil, pulses, milk) at an urban supermarket counter, authentic consumer realism --ar 16:9 --v 6.0"),

    ("ai_074_commuter_train_doorway_wind.jpg", "Mumbai Local Train Rush Doorway",
     "Cinematic profile shot of Indian office commuters standing safely at the open doorway of a fast-moving Mumbai suburban train, evening breeze blowing, city skyline in golden sunset --ar 16:9 --v 6.0"),

    ("ai_075_worldbank_headquarters_dc_facade.jpg", "World Bank Headquarters Washington D.C.",
     "The glass atrium and global flags at the World Bank Group headquarters in Washington D.C. on a crisp autumn afternoon, international financial authority --ar 16:9 --v 6.0"),

    ("ai_076_us_suburban_affluence_home.jpg", "United States $85,000 Per-Capita Household Standard",
     "A quiet, sunlit American suburban home with a manicured front lawn, two cars in the driveway, and solar panels on the roof, visual benchmark of high-income economies --ar 16:9 --v 6.0"),

    ("ai_077_germany_munich_engineering_street.jpg", "Germany $54,000 Per-Capita Manufacturing Core",
     "Sleek clean streetscape in Munich outside an advanced precision engineering corporation, cyclists on dedicated lanes, pristine European infrastructure --ar 16:9 --v 6.0"),

    ("ai_078_shanghai_pudong_financial_towers.jpg", "China $13,500 Per-Capita Industrial Transformation",
     "Towering skyscrapers of Shanghai Lujiazui financial center rising into evening clouds, illuminated by millions of LED lights, reflecting on the Huangpu River --ar 16:9 --v 6.0"),

    ("ai_079_mumbai_slum_highrise_boundary.jpg", "Urban Dual Economy Contrast in Mumbai",
     "A sharp editorial drone perspective showing soaring 60-story luxury residential glass towers bordering dense tin-roof residential settlements, capturing the economic dichotomy --ar 16:9 --v 6.0"),

    ("ai_080_luxury_car_dealership_showroom.jpg", "High-End Luxury SUV Showroom Boom (+24.5%)",
     "Gleaming showroom of premium German and British luxury SUVs in South Delhi; affluent buyers examining leather interiors under architectural track lighting --ar 16:9 --v 6.0"),

    ("ai_081_two_wheeler_mechanic_rural_dust.jpg", "Rural Motorcycle Repair Stall Stagnation",
     "An Indian motorcycle mechanic repairing an old 100cc commuter bike under a roadside tree, engine parts on a cloth, dry dusty farmland stretching into the distance --ar 16:9 --v 6.0"),

    ("ai_082_ration_shop_biometric_thumbprint.jpg", "PMGKAY Biometric Authentication Verification",
     "Close-up of an elderly rural woman's weathered thumb resting on a glowing red biometric PoS scanner at an official fair-price food grain shop, documentary authenticity --ar 16:9 --v 6.0"),

    ("ai_083_rbi_vault_door_steel_bars.jpg", "Central Bank Vault Steel Integrity",
     "A massive circular stainless steel bank vault door open to reveal secure safety deposit boxes, glowing warm amber security lights, banking documentary style --ar 16:9 --v 6.0"),

    ("ai_084_unsecured_loan_rejection_anxiety.jpg", "Household Loan EMI Burden Stress",
     "A young Indian professional sitting with head in hands at a home desk, laptop screen showing an overdue bank loan statement and credit card balance, moody dark shadows --ar 16:9 --v 6.0"),

    ("ai_085_empty_industrial_plot_signboard.jpg", "Industrial Corridor Vacant Plot Ready for Plants",
     "A wide expanse of graded industrial land in an economic zone; a signboard reading 'ALLOCATED FOR MANUFACTURING', yellow bulldozer parked nearby at sunset --ar 16:9 --v 6.0"),

    ("ai_086_vietnam_samsung_factory_complex.jpg", "Vietnam Mobile Assembly Mega-Complex",
     "Vast automated electronics manufacturing campus in Bac Ninh Vietnam; thousands of workers in uniform boarding transit buses, modern industrial powerhouse --ar 16:9 --v 6.0"),

    ("ai_087_it_office_night_cubicles_tired.jpg", "Services Island: The Late-Night IT Reality",
     "Glowing glass office floor in Bengaluru at 11 PM; a few IT professionals working late under desk lights on international corporate codebases, isolated urban wealth --ar 16:9 --v 6.0"),

    ("ai_088_peasant_plowing_bullocks_dusk.jpg", "Traditional Subsistence Farming Chokepoint",
     "An Indian farmer guiding a pair of white bullocks pulling a wooden plow through muddy soil at dusk, silhouette against orange twilight sky, timeless agrarian struggle --ar 16:9 --v 6.0"),

    ("ai_089_make_in_india_factory_assembly_worker.jpg", "Make in India Manufacturing Worker on Line",
     "A young Indian technician in blue overalls assembling a precision automotive gearbox on a conveyor line, safety gloves, focused concentration, sharp industrial photography --ar 16:9 --v 6.0"),

    ("ai_090_college_graduates_convocation_caps.jpg", "1.10 Crore Fresh Graduates Entering Workforce",
     "Excited young Indian university graduates tossing black mortarboards into a clear blue sky, smiles of high hope, capturing the massive potential of the demographic dividend --ar 16:9 --v 6.0"),

    ("ai_091_senior_citizens_village_temple_steps.jpg", "Elderly Population Growing in South India",
     "Group of elderly South Indian men and women sitting peacefully on stone temple steps in Kerala under coconut palms, quiet dignified aging in low-fertility regions --ar 16:9 --v 6.0"),

    ("ai_092_clock_tower_shadow_sunset.jpg", "The Passing of Time: The 18-Year Window",
     "A historic colonial clock tower casting a long shadow across an Indian city square as the orange sun sinks below the horizon, symbolic reminder of the demographic countdown --ar 16:9 --v 6.0"),

    ("ai_093_modern_garment_spinning_mill.jpg", "Automated Cotton Yarn Spinning Mill",
     "Rows of automated textile spinning spindles spinning white cotton thread at high speed, fiber mist illuminated by overhead factory lamps, precision mass production --ar 16:9 --v 6.0"),

    ("ai_094_refrigerated_cold_chain_trucks.jpg", "Cold Chain Fleet Transporting Farm Harvest",
     "A fleet of refrigerated logistics trucks loading fresh fruits and vegetables at a modern rural agro-terminal at dawn, clean asphalt, cold mist rising from open cargo doors --ar 16:9 --v 6.0"),

    ("ai_095_middle_class_budget_family_planning.jpg", "Middle-Class Family Reviewing Household Budget",
     "A husband and wife sitting together over tea in the evening, reviewing family savings and school tuition bills, thoughtful expressions, intimate editorial lighting --ar 16:9 --v 6.0"),

    ("ai_096_cnc_machinist_apprentice_training.jpg", "CNC Precision Machining Skilling Lab",
     "An expert industrial trainer guiding a young female student on setting coordinates on a CNC milling console, bright clean machine shop, cutting fluid mist --ar 16:9 --v 6.0"),

    ("ai_097_electric_bus_charging_depot.jpg", "Clean Infrastructure: Electric Bus Depot",
     "Rows of modern electric city buses plugged into high-power overhead charging gantries in a clean transit depot at night, glowing green charging indicators --ar 16:9 --v 6.0"),

    ("ai_098_container_train_western_freight_corridor.jpg", "Western Dedicated Freight Corridor Double Stack",
     "An electric freight locomotive pulling long double-stack container wagons along the dedicated freight corridor across Rajasthan, desert landscape, golden sunset --ar 16:9 --v 6.0"),

    ("ai_099_rural_handicraft_cooperative_artisan.jpg", "Dignified Livelihoods in Rural Clusters",
     "Skilled village woodcarvers and brass artisans working in an organized cooperative workshop with modern ventilation, finished goods packaged for retail export --ar 16:9 --v 6.0"),

    ("ai_100_per_capita_income_top_50_horizon.jpg", "Reaching Top 50 Per-Capita Income Horizon",
     "A soaring sunrise view over a futuristic Indian coastal city with clean industrial ports, high-speed rail bridges, and green residential districts, symbolic of genuine prosperity --ar 16:9 --v 6.0"),

    ("ai_101_benaqaab_investigative_ledger_desk.jpg", "The Benaqaab Forensic Evidence Desk",
     "A dark obsidian forensic investigation desk with spread-out government gazettes, World Bank charts, RBI reports, highlighters, and a glowing magnifying loupe, documentary cinema --ar 16:9 --v 6.0"),

    ("ai_102_citizen_viewing_documentary_tablet.jpg", "Engaged Citizen Watching Truth & Evidence",
     "An Indian viewer watching an investigative economic documentary on a tablet screen in a cozy living room at night, screen light reflecting in eyes, thoughtful expression --ar 16:9 --v 6.0"),

    ("ai_103_india_gate_tricolor_dusk.jpg", "India Gate Rajpath at Twilight Tricolor",
     "Majestic low-angle shot of India Gate New Delhi at twilight, tricolor fountain lights in foreground, serene ceremonial boulevard, national pride grounded in truth --ar 16:9 --v 6.0"),

    ("ai_104_benaqaab_channel_logo_glowing_seal.jpg", "Benaqaab India Official Glowing Brand Seal",
     "A dark metallic circular medallion bearing the Benaqaab India emblem with a glowing gold border and the embossed motto 'SACH · SABOOT · BEBAK', subtle particle drift --ar 16:9 --v 6.0"),

    ("ai_105_final_verdict_stamp_cinematic_climax.jpg", "Final Verdict Stamp Slamming Down",
     "Macro slow-motion capture of a heavy brass forensic rubber stamp slamming onto national accounts documents, tiny sparks of light scattering, embossed crimson ink imprint 'REALITY UNVEILED' --ar 16:9 --v 6.0 --style raw")
]

# Generate Markdown Document
md_lines = [
    "# 🎨 BENAQAAB INDIA — 105 MASTER AI IMAGE GENERATION PROMPTS",
    "## Episode EP-19: India's 7.8% GDP vs Global Superpowers (What Headline Numbers Hide)",
    "> **Channel:** Benaqaab India (बेनाक़ाब इंडिया) • **Motto:** `SACH · SABOOT · BEBAK`  ",
    "> **Total Assets:** 105 Distinct Visual Plates + 1 Master YouTube Thumbnail  ",
    "> **Format:** 16:9 Landscape Widescreen (1920×1080)  ",
    "> **Destination Folder:** `projects/ep19_gdp_growth_reality/assets/ai_plates/`  ",
    "> **Standard:** Full broadcast density (shot length ≤ 5.8s), 100% causal audio-visual lockstep (`RULE-AUDIO-VISUAL-CAUSAL-LOCKSTEP`).",
    "",
    "---",
    "",
    "## 📌 HOW TO GENERATE THESE IMAGES",
    "1. **Earlier Generated Plates (1–16):** You have already generated `ai_01` to `ai_16`! Keep those in `assets/ai_plates/`.",
    "2. **New Plates (17–105):** Copy the prompt from each block below and paste into Midjourney v6, Flux.1, Grok Imagine, or DALL-E 3.",
    "3. **File Naming:** Save each generated file with the exact name indicated in its heading.",
    "",
    "---",
    "",
    "## 🌟 MASTER YOUTUBE THUMBNAIL (HIGH-CTR BROADCAST)",
    "### File: `projects/ep19_gdp_growth_reality/thumbnail_master.jpg`",
    "```text",
    "A high-impact cinematic documentary YouTube thumbnail, dramatic split-screen composition: on the left side, a powerful bronze Dalal Street charging bull illuminated with brilliant emerald green laser light and glowing holographic stock market tickers (+7.8% GDP RECORD); on the right side, an intimate dim Indian family dining table with unpaid electricity bills, grocery receipts, and a cracked bronze piggy bank under a harsh crimson red spotlight; separated by a razor-sharp vertical light seam, volumetric atmospheric dust, ultra-high micro-contrast, photorealistic documentary realism, shot on 35mm Hasselblad --ar 16:9 --v 6.0 --style raw",
    "```",
    "",
    "---",
    "",
    "## 📋 COMPLETE 105-IMAGE SEQUENTIAL DIRECTORY",
    ""
]

# Write all 105 beats
for i in range(105):
    beat_num = i + 1
    st, en, txt = intervals[i]
    chap_code, chap_name = get_chapter((st + en) / 2)
    
    if beat_num in EXISTING:
        fname, subj, prompt = EXISTING[beat_num]
        status = "✅ [ALREADY GENERATED EARLIER]"
    else:
        exp_idx = beat_num - 17
        fname, subj, prompt = EXPANDED_PROMPTS[exp_idx]
        status = "✨ [NEW PROMPT REQUIRED]"
        
    md_lines.append(f"### Plate {beat_num:03d}: `{fname}` {status}")
    md_lines.append(f"* **Timecode:** `{st:.2f}s – {en:.2f}s` (Duration: {en-st:.2f}s)")
    md_lines.append(f"* **Chapter:** {chap_code}: {chap_name}")
    md_lines.append(f"* **Subject:** {subj}")
    md_lines.append(f"* **Voiceover Sync:** *\"{txt}\"*")
    md_lines.append(f"* **Midjourney / Flux / Grok Prompt:**")
    md_lines.append("```text")
    md_lines.append(prompt)
    md_lines.append("```")
    md_lines.append("")

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"✅ Generated {OUTPUT_FILE} with all 105 prompts!")
