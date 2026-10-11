import json
from pathlib import Path

with open('projects/ep19_gdp_growth_reality/BEAT_SHEET.json', 'r', encoding='utf-8') as f:
    beats = json.load(f)

cur = None
for b in beats:
    ch = b['chapter']
    if ch != cur:
        print(f"{b['start_s']:6.2f}s | Beat {b['beat_id']:03d} | {ch}")
        cur = ch
print(f"End: {beats[-1]['end_s']:6.2f}s | Total beats: {len(beats)}")
