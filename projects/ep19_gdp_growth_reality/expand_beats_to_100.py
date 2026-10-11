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
total_dur = ts_data["duration"]

# Asset pool
SOURCES = [
    "assets/official_sources/src_01_mospi_press_note_gdp_78.png",
    "assets/official_sources/src_02_rbi_household_savings_crash.png",
    "assets/official_sources/src_03_worldbank_per_capita_ranking.png",
    "assets/official_sources/src_04_siam_automobile_k_shaped.png",
    "assets/official_sources/src_05_manufacturing_missing_factory.png",
    "assets/official_sources/src_06_demographic_clock_2045.png"
]

AI_PLATES = [
    "assets/ai_plates/ai_01_global_gdp_celebration_bull.jpg",
    "assets/ai_plates/ai_02_parliament_cabinet_national_accounts.jpg",
    "assets/ai_plates/ai_03_middle_class_kitchen_table_inflation.jpg",
    "assets/ai_plates/ai_04_crowded_mumbai_commuter_train.jpg",
    "assets/ai_plates/ai_05_global_superpowers_per_capita_towers.jpg",
    "assets/ai_plates/ai_06_k_shaped_economic_divergence.jpg",
    "assets/ai_plates/ai_07_luxury_suv_gurugram_cybercity.jpg",
    "assets/ai_plates/ai_08_rural_village_stagnant_two_wheelers.jpg",
    "assets/ai_plates/ai_09_pmgkay_free_ration_distribution.jpg",
    "assets/ai_plates/ai_10_rbi_financial_stability_vault.jpg",
    "assets/ai_plates/ai_11_debt_financed_consumption_credit_card.jpg",
    "assets/ai_plates/ai_12_the_missing_factory_shenzhen_comparison.jpg",
    "assets/ai_plates/ai_13_agriculture_45pct_workforce_chokepoint.jpg",
    "assets/ai_plates/ai_14_youth_demographic_clock_2045.jpg",
    "assets/ai_plates/ai_15_vocational_skilling_and_reforms_future.jpg",
    "assets/ai_plates/ai_16_benaqaab_final_verdict_stamp.jpg"
]

# Chapters timeline distribution
# Total 608.35s across 7 chapters:
# Chap 1: 0 - 85s
# Chap 2: 85 - 165s
# Chap 3: 165 - 255s
# Chap 4: 255 - 345s
# Chap 5: 345 - 435s
# Chap 6: 435 - 525s
# Chap 7: 525 - 608.35s

def get_chapter(t):
    if t < 85: return "Chapter 1: The Global Celebration vs Street Reality"
    elif t < 165: return "Chapter 2: The Per-Capita Illusion: 5th Largest vs 136th Rank"
    elif t < 255: return "Chapter 3: The K-Shaped Economy: Who Is Actually Spending?"
    elif t < 345: return "Chapter 4: The Household Balance Sheet Crisis"
    elif t < 435: return "Chapter 5: The Missing Factory: Why Manufacturing Won't Take Off"
    elif t < 525: return "Chapter 6: The 2045 Demographic Clock"
    else: return "Chapter 7: The Road Ahead & Citizen Verdict"

# Split longer sentences (> 7.5s) into 2 cuts to ensure shot length <= 5.5 - 6.0s
raw_intervals = []
for b in boundaries:
    offset = b["offset"]
    dur = b["duration"]
    text = b["text"]
    if dur > 7.5:
        half = round(dur / 2, 2)
        raw_intervals.append((offset, offset + half, text))
        raw_intervals.append((offset + half, offset + dur, text))
    else:
        raw_intervals.append((offset, offset + dur, text))

# Sort and clean intervals
raw_intervals.sort(key=lambda x: x[0])
print(f"🎬 Total Interval Cuts: {len(raw_intervals)}")

# Build the 90+ beat timeline
full_beats = []
for idx, (st, en, txt) in enumerate(raw_intervals):
    bid = idx + 1
    t_mid = (st + en) / 2
    chap = get_chapter(t_mid)

    # Determine asset based on narrative chapter and alternate between source and AI plate
    is_source = (bid % 2 == 0)
    
    # Specific targeted asset assignment
    if "Chapter 1" in chap:
        if bid == 1:
            asset_type = "ai"
            asset_path = AI_PLATES[0]
            motion = "roadmap"
            subject = "Opening Burning Question: 7.8% GDP vs Living Reality"
            hud = "REAL GDP: 7.8% (Q1 FY26-27)"
            color = "#38bdf8"
        elif 25.0 <= st <= 32.0 or 25.0 <= en <= 32.0:
            asset_type = "ai"
            asset_path = AI_PLATES[1]
            motion = "cta"
            subject = "Channel Identity & Subscribe/Like Micro-Interaction"
            hud = "BENAQAAB INDIA: SACH · SABOOT · BEBAK"
            color = "#fbbf24"
        elif is_source:
            asset_type = "official_source"
            asset_path = SOURCES[0] # MoSPI Press Note
            motion = "highlighter"
            subject = "MoSPI Official National Accounts: Q1 Estimates"
            hud = "GOVERNMENT OF INDIA: MoSPI PRESS RELEASE"
            color = "#38bdf8"
        else:
            asset_type = "ai"
            asset_path = AI_PLATES[idx % 3]
            motion = "pin"
            subject = "Street Level Inflation vs Headline Number"
            hud = "REAL LIVING COST DISCONNECT"
            color = "#f43f5e"

    elif "Chapter 2" in chap:
        if is_source:
            asset_type = "official_source"
            asset_path = SOURCES[2] # World Bank
            motion = "loupe" if bid % 4 == 0 else "highlighter"
            subject = "World Bank Data: India Per Capita Rank #136 ($2,730)"
            hud = "WORLD BANK: PER CAPITA INCOME RANK #136"
            color = "#f43f5e"
        else:
            asset_type = "ai"
            asset_path = AI_PLATES[3] if bid % 2 == 1 else AI_PLATES[4]
            motion = "odometer" if bid % 4 == 1 else "pin"
            subject = "Global Wealth Disparity: USA 31x & China 5x"
            hud = "USA: $85,000 | GERMANY: $54,000 | INDIA: $2,730"
            color = "#38bdf8"

    elif "Chapter 3" in chap:
        if "SIAM" in txt or "गाड़ियों" in txt or "एसयूवी" in txt or is_source:
            asset_type = "official_source"
            asset_path = SOURCES[3] # SIAM Report
            motion = "highlighter"
            subject = "SIAM Flash Report: Luxury SUVs +24.5% vs Small Cars -42%"
            hud = "SIAM REPORT: K-SHAPED AUTOMOTIVE MIRROR"
            color = "#34d399"
        elif "राशन" in txt or "80 करोड़" in txt:
            asset_type = "ai"
            asset_path = AI_PLATES[8] # PMGKAY Ration
            motion = "pin"
            subject = "80 Crore Citizens on Free Ration (PMGKAY)"
            hud = "PMGKAY: 80.0 CRORE CITIZENS (57% OF INDIA)"
            color = "#f59e0b"
        elif "लग्ज़री" in txt or "अपार्टमेंट्स" in txt:
            asset_type = "ai"
            asset_path = AI_PLATES[6] # Luxury SUV Gurugram
            motion = "pin"
            subject = "Upper Arm Boom: Ultra-Luxury Penthouses & SUVs"
            hud = "ASSET CLASS BOOM: DEMAT ACCOUNTS 16+ CR"
            color = "#34d399"
        else:
            asset_type = "ai"
            asset_path = AI_PLATES[5] if bid % 2 == 0 else AI_PLATES[7]
            motion = "pin"
            subject = "The Two Indias Divergence: K-Shaped Economy"
            hud = "K-SHAPED CONSUMPTION DIVERGENCE"
            color = "#f43f5e"

    elif "Chapter 4" in chap:
        if is_source or "आरबीआई" in txt or "सेविंग्स" in txt:
            asset_type = "official_source"
            asset_path = SOURCES[1] # RBI Report
            motion = "loupe" if bid % 3 == 0 else "highlighter"
            subject = "RBI Financial Stability Report: Net Savings Crash to 5.3%"
            hud = "RBI BULLETIN: 50-YEAR HISTORIC LOW SAVINGS"
            color = "#f43f5e"
        elif "क़र्ज़" in txt or "क्रेडिट कार्ड" in txt:
            asset_type = "ai"
            asset_path = AI_PLATES[10] # Credit Card Debt
            motion = "odometer"
            subject = "Unsecured Retail Loans at Record 58.2%"
            hud = "HOUSEHOLD DEBT TO GDP: 45.8% PEAK"
            color = "#38bdf8"
        else:
            asset_type = "ai"
            asset_path = AI_PLATES[9] # Broken Vault
            motion = "pin"
            subject = "Depleting Household Balance Sheets"
            hud = "FAMILIES COPING VIA OLD SAVINGS"
            color = "#f59e0b"

    elif "Chapter 5" in chap:
        if is_source or "मेक इन इंडिया" in txt or "मैन्युफैक्चरिंग" in txt:
            asset_type = "official_source"
            asset_path = SOURCES[4] # Missing Factory
            motion = "highlighter"
            subject = "The Missing Factory: Manufacturing Stuck at 15.8%"
            hud = "MAKE IN INDIA: TARGET 25% | ACTUAL 15.8%"
            color = "#ef4444"
        elif "खेती" in txt or "मज़दूर" in txt:
            asset_type = "ai"
            asset_path = AI_PLATES[12] # Agriculture
            motion = "pin"
            subject = "45.4% Workforce Trapped in Farming (15% GDP)"
            hud = "RURAL PRODUCTIVITY CHOKEPOINT"
            color = "#f59e0b"
        else:
            asset_type = "ai"
            asset_path = AI_PLATES[11] # Automated Fab
            motion = "pin"
            subject = "China 27% Manufacturing vs India Services Island"
            hud = "SERVICES (12.1%) CANNOT EMPLOY MASS WORKFORCE"
            color = "#0ea5e9"

    elif "Chapter 6" in chap:
        if is_source or "सर्वे" in txt or "फ़र्टिलिटी" in txt:
            asset_type = "official_source"
            asset_path = SOURCES[5] # Demographic Clock
            motion = "loupe" if bid % 3 == 0 else "highlighter"
            subject = "Demographic Clock 2045: Total Fertility at 2.0"
            hud = "NFHS-5: TFR 2.0 (BELOW REPLACEMENT LEVEL)"
            color = "#f59e0b"
        else:
            asset_type = "ai"
            asset_path = AI_PLATES[13] # Youth Clock
            motion = "odometer" if bid % 2 == 0 else "pin"
            subject = "1.1 Crore Youth Annually: Getting Old Before Rich?"
            hud = "18 YEARS TO AVOID MIDDLE-INCOME TRAP"
            color = "#ef4444"

    else: # Chapter 7
        if bid == len(raw_intervals):
            asset_type = "ai"
            asset_path = AI_PLATES[15] # Final Verdict Stamp
            motion = "verdict_stamp"
            subject = "Final Forensic Verdict: Reality Unveiled"
            hud = "SACH · SABOOT · BEBAK | FINAL VERDICT"
            color = "#f43f5e"
        elif is_source:
            asset_type = "official_source"
            asset_path = SOURCES[2] # World Bank
            motion = "highlighter"
            subject = "The Target: Per Capita Income in Global Top 50"
            hud = "NATIONAL PROSPERITY HORIZON"
            color = "#38bdf8"
        else:
            asset_type = "ai"
            asset_path = AI_PLATES[14] # Reforms & Skilling
            motion = "pin"
            subject = "The 4 Urgent Reforms: Factories, Tax Relief & Skilling"
            hud = "CITIZEN PROSPERITY BLUEPRINT"
            color = "#10b981"

    beat_obj = {
        "beat_id": bid,
        "chapter": chap,
        "start_s": round(st, 2),
        "end_s": round(en, 2),
        "asset_type": asset_type,
        "asset_path": asset_path,
        "subject": subject,
        "hindi_desc": txt,
        "hud_data": hud,
        "motion_type": motion,
        "target": [960, 480],
        "elbow": [1400, 360],
        "title": subject.split(":")[0].upper(),
        "subtitle": txt[:60] + "..." if len(txt) > 60 else txt,
        "color": color
    }
    full_beats.append(beat_obj)

# Force the last beat end to exact total_duration
full_beats[-1]["end_s"] = round(total_dur, 2)

print(f"🎯 Successfully generated {len(full_beats)} distinct visual beats! (Shot length avg: {total_dur/len(full_beats):.2f}s)")

with open(BEATS_JSON, "w", encoding="utf-8") as f:
    json.dump(full_beats, f, indent=2, ensure_ascii=False)

with open(BEATS_JS, "w", encoding="utf-8") as f:
    f.write("// Benaqaab India EP-19 Visual Beats Ledger (Full 90+ Beats)\n")
    f.write(f"window.TOTAL_DURATION = {total_dur:.3f};\n")
    f.write("window.BEATS_DATA = " + json.dumps(full_beats, indent=2, ensure_ascii=False) + ";\n")

print(f"✅ Saved: {BEATS_JSON}")
print(f"✅ Saved: {BEATS_JS}")
