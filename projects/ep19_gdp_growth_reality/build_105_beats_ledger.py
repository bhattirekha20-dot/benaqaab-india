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
BEATS_JSON = DIR / "BEAT_SHEET.json"
BEATS_JS = DIR / "beats.js"

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

print(f"🎬 Total intervals: {len(intervals)}, spanning {intervals[0][0]}s to {intervals[-1][1]}s")

# Import the existing plates and expanded prompts from generate_105_master_prompts
from generate_105_master_prompts import EXISTING, EXPANDED_PROMPTS, get_chapter

# Official source windows for strict evidentiary adherence
EVIDENCE_WINDOWS = [
    (64.29, 83.45, "assets/official_sources/src_01_mospi_press_note_gdp_78.png", "MoSPI Official Gazette & Press Note"),
    (121.45, 148.53, "assets/official_sources/src_03_worldbank_per_capita_ranking.png", "World Bank Official Global Per-Capita Income Table"),
    (224.59, 242.08, "assets/official_sources/src_04_siam_automobile_k_shaped.png", "SIAM Flash Automobile Industry Report"),
    (282.36, 336.00, "assets/official_sources/src_02_rbi_household_savings_crash.png", "RBI Financial Stability Report on Household Savings"),
    (431.23, 450.38, "assets/official_sources/src_05_manufacturing_missing_factory.png", "National Accounts Manufacturing 15.8% Share Audit"),
    (484.82, 510.04, "assets/official_sources/src_06_demographic_clock_2045.png", "NFHS-5 Demographic Clock 2045 Projection")
]

def get_evidence_source(st, en):
    mid = (st + en) / 2
    for w_st, w_en, src_path, label in EVIDENCE_WINDOWS:
        if w_st <= mid <= w_en:
            return src_path, label
    return None, None

# Fallback pool based on chapters
CHAPTER_FALLBACKS = {
    "Chapter 1": "assets/ai_plates/ai_01_global_gdp_celebration_bull.jpg",
    "Chapter 2": "assets/ai_plates/ai_04_crowded_mumbai_commuter_train.jpg",
    "Chapter 3": "assets/ai_plates/ai_07_luxury_suv_gurugram_cybercity.jpg",
    "Chapter 4": "assets/ai_plates/ai_11_debt_financed_consumption_credit_card.jpg",
    "Chapter 5": "assets/ai_plates/ai_12_the_missing_factory_shenzhen_comparison.jpg",
    "Chapter 6": "assets/ai_plates/ai_14_youth_demographic_clock_2045.jpg",
    "Chapter 7": "assets/ai_plates/ai_16_benaqaab_final_verdict_stamp.jpg"
}

beats = []
for i in range(105):
    beat_num = i + 1
    st, en, txt = intervals[i]
    chap_code, chap_name = get_chapter((st + en) / 2)
    full_chap = f"{chap_code}: {chap_name}"

    if beat_num in EXISTING:
        fname, subj, prompt = EXISTING[beat_num]
        asset_path = f"assets/ai_plates/{fname}"
        fallback_path = asset_path
    else:
        exp_idx = beat_num - 17
        fname, subj, prompt = EXPANDED_PROMPTS[exp_idx]
        asset_path = f"assets/ai_plates/{fname}"
        fallback_path = CHAPTER_FALLBACKS.get(chap_code, "assets/ai_plates/ai_01_global_gdp_celebration_bull.jpg")

    # Check if this beat is within an official evidentiary document inspection window
    ev_src, ev_label = get_evidence_source(st, en)
    if ev_src:
        # During official document inspection, primary asset is the real official source document!
        # And fallback is the AI plate
        official_asset_path = ev_src
        official_fallback_path = asset_path
    else:
        official_asset_path = asset_path
        official_fallback_path = fallback_path

    # Determine motion type tag
    mtype = "ken_burns"
    if st < 5.5:
        mtype = "roadmap"
    elif 60.1 <= st <= 64.3:
        mtype = "cta"
    elif 64.29 <= st <= 83.45:
        mtype = "highlighter_mospi"
    elif 121.45 <= st <= 148.53:
        mtype = "loupe_worldbank"
    elif 224.59 <= st <= 242.08:
        mtype = "highlighter_siam"
    elif 282.36 <= st <= 336.00:
        mtype = "highlighter_rbi"
    elif 431.23 <= st <= 450.38:
        mtype = "highlighter_mfg"
    elif 484.82 <= st <= 510.04:
        mtype = "highlighter_nfhs"
    elif st >= 600.0:
        mtype = "verdict_stamp"

    beat_obj = {
        "beat_id": beat_num,
        "chapter": full_chap,
        "start_s": st,
        "end_s": en,
        "duration_s": round(en - st, 2),
        "asset_path": official_asset_path,
        "fallback_path": official_fallback_path,
        "target_ai_plate": fname,
        "subject": subj,
        "hindi_desc": txt,
        "motion_type": mtype
    }
    beats.append(beat_obj)

print(f"✅ Generated {len(beats)} beats!")

# Write to BEAT_SHEET.json
with open(BEATS_JSON, "w", encoding="utf-8") as f:
    json.dump(beats, f, ensure_ascii=False, indent=2)
print(f"✅ Saved {BEATS_JSON}")

# Write to beats.js
js_content = "// Benaqaab India EP-19 Causal Beats Ledger (105 Visual Beats in Lockstep)\n"
js_content += f"window.TOTAL_DURATION = {total_dur:.3f};\n"
js_content += "window.BEATS_DATA = " + json.dumps(beats, ensure_ascii=False, indent=2) + ";\n"

with open(BEATS_JS, "w", encoding="utf-8") as f:
    f.write(js_content)
print(f"✅ Saved {BEATS_JS} with {len(beats)} beats!")
