import json
import sys

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

with open('projects/ep19_gdp_growth_reality/word_timestamps.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

for i, b in enumerate(d['boundaries']):
    off = b['offset']
    end = off + b['duration']
    txt = b['text']
    print(f"{i+1:02d}. [{off:6.2f}s - {end:6.2f}s] {txt}")
