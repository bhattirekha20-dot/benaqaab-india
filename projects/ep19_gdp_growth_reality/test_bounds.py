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

print(f"Total boundaries: {len(boundaries)}, total duration: {total_dur:.2f}s")
