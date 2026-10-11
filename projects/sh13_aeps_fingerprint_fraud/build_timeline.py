import json
from pathlib import Path

DIR = Path(__file__).parent
OUTPUT_FILE = DIR / "scene_timeline.json"

beats_data = [
    # Sentence 1: 0.00s - 6.74s
    {"id": "beat_01", "start": 0.00, "end": 1.70, "file": "beat_01.jpg", "caption": "A/C DEBITED: ₹10,000", "camera": "zoom_in"},
    {"id": "beat_02", "start": 1.70, "end": 3.40, "file": "beat_02.jpg", "caption": "ZERO OTP · ZERO CARD", "camera": "pan_down"},
    {"id": "beat_03", "start": 3.40, "end": 5.10, "file": "beat_03.jpg", "caption": "₹10,000 SAAF!", "camera": "shake"},
    {"id": "beat_04", "start": 5.10, "end": 6.74, "file": "beat_04.jpg", "caption": "CHOR KA ASLI HATHYAR?", "camera": "zoom_in"},

    # Sentence 2: 6.74s - 11.30s
    {"id": "beat_05", "start": 6.74, "end": 8.30, "file": "beat_05.jpg", "caption": "NAKLI SILICONE UNGLI!", "camera": "zoom_in"},
    {"id": "beat_06", "start": 8.30, "end": 9.80, "file": "beat_06.jpg", "caption": "1,000+ CLONES SEIZED", "camera": "pan_left"},
    {"id": "beat_07", "start": 9.80, "end": 11.30, "file": "beat_07.jpg", "caption": "AePS SYSTEM EXPOSED", "camera": "zoom_out"},

    # Sentence 3: 11.30s - 16.03s
    {"id": "beat_08", "start": 11.30, "end": 12.80, "file": "beat_08.jpg", "caption": "BUILT FOR RURAL BHARAT", "camera": "pan_right"},
    {"id": "beat_09", "start": 12.80, "end": 14.40, "file": "beat_09.jpg", "caption": "LETHAL FLAW: ZERO 2FA", "camera": "shake"},
    {"id": "beat_10", "start": 14.40, "end": 16.03, "file": "beat_10.jpg", "caption": "DATA LEAK AT REGISTRY", "camera": "pan_up"},

    # Sentence 4: 16.03s - 23.74s
    {"id": "beat_11", "start": 16.03, "end": 17.50, "file": "beat_11.jpg", "caption": "REGISTERED SALE DEED", "camera": "zoom_in"},
    {"id": "beat_12", "start": 17.50, "end": 19.00, "file": "beat_12.jpg", "caption": "UNMASKED THUMBPRINT", "camera": "loupe_magnify"},
    {"id": "beat_13", "start": 19.00, "end": 20.60, "file": "beat_13.jpg", "caption": "AADHAAR NUMBER EXPOSED", "camera": "highlighter_sweep"},
    {"id": "beat_14", "start": 20.60, "end": 22.20, "file": "beat_14.jpg", "caption": "ZERO LOGIN DOWNLOAD", "camera": "pan_down"},
    {"id": "beat_15", "start": 22.20, "end": 23.74, "file": "beat_15.jpg", "caption": "BUTTER PAPER PRINT", "camera": "zoom_in"},

    # Sentence 5: 23.74s - 27.67s
    {"id": "beat_16", "start": 23.74, "end": 25.00, "file": "beat_16.jpg", "caption": "UV POLY-STAMPER MACHINE", "camera": "pan_left"},
    {"id": "beat_17", "start": 25.00, "end": 26.30, "file": "beat_17.jpg", "caption": "3D RUBBER FINGER BORN", "camera": "zoom_in"},
    {"id": "beat_18", "start": 26.30, "end": 27.67, "file": "beat_18.jpg", "caption": "ROGUE BANK MITRA POS", "camera": "pan_down"},

    # Sentence 6: 27.67s - 32.51s
    {"id": "beat_19", "start": 27.67, "end": 29.30, "file": "beat_19.jpg", "caption": "OLDER L0 SCANNER FLAW", "camera": "pan_right"},
    {"id": "beat_20", "start": 29.30, "end": 30.90, "file": "beat_20.jpg", "caption": "98% MATCH CONFIRMED", "camera": "zoom_in"},
    {"id": "beat_21", "start": 30.90, "end": 32.51, "file": "beat_21.jpg", "caption": "₹10,000 GAYAB!", "camera": "odometer_roll"},

    # Sentence 7: 32.51s - 38.49s (The Pivot to Shield)
    {"id": "beat_22", "start": 32.51, "end": 34.00, "file": "beat_22.jpg", "caption": "THE 60-SECOND SHIELD", "camera": "zoom_in"},
    {"id": "beat_23", "start": 34.00, "end": 35.50, "file": "beat_23.jpg", "caption": "OPEN mAadhaar APP", "camera": "pan_up"},
    {"id": "beat_24", "start": 35.50, "end": 37.00, "file": "beat_24.jpg", "caption": "LOCK BIOMETRICS TOGGLE", "camera": "zoom_in"},
    {"id": "beat_25", "start": 37.00, "end": 38.49, "file": "beat_25.jpg", "caption": "IMMUNIZED AGAINST CLONES", "camera": "pan_down"},

    # Sentence 8: 38.49s - 44.20s
    {"id": "beat_26", "start": 38.49, "end": 40.40, "file": "beat_26.jpg", "caption": "SCAMMER TRIES AGAIN...", "camera": "pan_left"},
    {"id": "beat_27", "start": 40.40, "end": 42.30, "file": "beat_27.jpg", "caption": "ERROR 330: LOCKED!", "camera": "shake"},
    {"id": "beat_28", "start": 42.30, "end": 44.20, "file": "beat_28.jpg", "caption": "DIAL 1930 CYBER HELPLINE", "camera": "pan_right"},

    # Sentence 9: 44.20s - 49.03s
    {"id": "beat_29", "start": 44.20, "end": 46.50, "file": "beat_29.jpg", "caption": "CLONED SCAM EXPOSED", "camera": "verdict_slam"},
    {"id": "beat_30", "start": 46.50, "end": 49.03, "file": "beat_30.jpg", "caption": "BENAQAAB INDIA · SUBSCRIBE", "camera": "zoom_out"}
]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump({
        "total_duration": 49.03,
        "total_cuts": len(beats_data),
        "asl_sec": round(49.03 / len(beats_data), 2),
        "beats": beats_data
    }, f, indent=2, ensure_ascii=False)

print(f"✅ Generated {len(beats_data)} beats timeline in scene_timeline.json (ASL: {round(49.03 / len(beats_data), 2)}s)")
