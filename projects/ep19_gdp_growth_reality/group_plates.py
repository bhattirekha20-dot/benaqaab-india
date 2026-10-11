import os
from pathlib import Path

DIR = Path(__file__).parent
plates_dir = DIR / "assets" / "ai_plates"
files = sorted([f.name for f in plates_dir.glob("*.jpg")])

print(f"Total files: {len(files)}")

# Group by topic / chapter keyword
ch1_files = [] # Celebration, bull, parliament, kitchen, bills, ration, grocery, deconstruct
ch2_files = [] # Commuter train crowd, CST, World bank, skyscrapers, US, Germany, China, per capita divide
ch3_files = [] # K-shape, luxury SUV, CyberCity, two-wheeler, alto, tractor, showroom, ration queue, PMGKAY
ch4_files = [] # RBI, savings, piggybank, hospital bills, school fee, debt 45%, smartphone emi, credit card, gold loan, bank branch, borrowed bubble, vault
ch5_files = [] # Missing factory, Shenzhen, textile, IT tech park, cubicles, unemployed graduates, fragmented land, mandis, make in india, stamping press, dharavi, freight, vietnam
ch6_files = [] # Demographic clock, youth, railway exam, 2045 countdown, fertility drop, aging, pension, middle income trap, south korea, brazil, convocation, senior citizens, clock tower
ch7_files = [] # Reforms, factory sheds, garments, leather, food processing, cold storage, tax relief, gst, iti robotics, ev battery, semiconductor, corridor, msme, women, apprentice, broadband, housing, clinic, converging, top 50, savings revival, ledger, citizen, india gate, logo, verdict stamp

for f in files:
    name = f.lower()
    if any(k in name for k in ['bull', 'parliament', 'kitchen', 'grocery', 'pmgkay_free_ration_distribution', 'headline_numbers_unmasked', 'ai_01_global', 'ai_02_parliament', 'ai_03_middle_class']):
        ch1_files.append(f)
    elif any(k in name for k in ['commuter', 'crowded_mumbai', 'worldbank', 'superpowers', 'us_suburban', 'germany', 'shanghai', 'slum_highrise', 'ai_04_crowded', 'ai_05_global']):
        ch2_files.append(f)
    elif any(k in name for k in ['k_shaped', 'luxury', 'two_wheeler', 'alto', 'tractor_loan', 'pmgkay_ration_queue', 'dealership', 'mechanic', 'biometric_thumbprint', 'ai_06_k', 'ai_07_luxury', 'ai_08_rural', 'ai_017', 'ai_018', 'ai_019']):
        ch3_files.append(f)
    elif any(k in name for k in ['rbi', 'savings', 'piggybank', 'hospital', 'school_coaching', 'household_debt', 'smartphone_emi', 'credit_card', 'pawn_shop', 'loan_officer', 'borrowed_consumption', 'vault', 'loan_rejection', 'ai_020', 'ai_021', 'ai_022', 'ai_023', 'ai_024', 'ai_025', 'ai_026', 'ai_027', 'ai_028', 'ai_029', 'ai_083', 'ai_084']):
        ch4_files.append(f)
    elif any(k in name for k in ['missing_factory', 'shenzhen', 'textile', 'it_tech_park', 'it_office', 'college_graduates_unemployed', 'fragmented_land', 'mandis', 'make_in_india', 'stamping_press', 'dharavi', 'container_freight', 'empty_industrial', 'vietnam', 'cubicles', 'peasant_plowing', 'assembly_worker', 'ai_030', 'ai_031', 'ai_032', 'ai_033', 'ai_034', 'ai_035', 'ai_036', 'ai_037', 'ai_038', 'ai_039', 'ai_040', 'ai_085', 'ai_086', 'ai_087', 'ai_088', 'ai_089', 'ai_12_the_missing', 'ai_13_agriculture']):
        ch5_files.append(f)
    elif any(k in name for k in ['demographic', 'railway_recruitment', 'digital_clock_2045', 'fertility_rate', 'aging_population', 'social_security', 'middle_income_trap', 'south_korea', 'brazil', 'convocation_caps', 'senior_citizens', 'clock_tower', 'ai_041', 'ai_042', 'ai_043', 'ai_044', 'ai_045', 'ai_046', 'ai_047', 'ai_048', 'ai_049', 'ai_090', 'ai_091', 'ai_092', 'ai_14_youth']):
        ch6_files.append(f)
    else:
        ch7_files.append(f)

print(f"CH1: {len(ch1_files)} files: {ch1_files}")
print(f"CH2: {len(ch2_files)} files: {ch2_files}")
print(f"CH3: {len(ch3_files)} files: {ch3_files}")
print(f"CH4: {len(ch4_files)} files: {ch4_files}")
print(f"CH5: {len(ch5_files)} files: {ch5_files}")
print(f"CH6: {len(ch6_files)} files: {ch6_files}")
print(f"CH7: {len(ch7_files)} files: {ch7_files}")
total_grouped = len(ch1_files) + len(ch2_files) + len(ch3_files) + len(ch4_files) + len(ch5_files) + len(ch6_files) + len(ch7_files)
print(f"Total grouped: {total_grouped} / 105")
