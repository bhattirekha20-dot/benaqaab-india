import json
from pathlib import Path

DIR = Path(__file__).parent
with open(DIR / "word_timestamps.json", "r", encoding="utf-8") as f:
    d = json.load(f)

out_lines = []
for i, b in enumerate(d["boundaries"]):
    st = b["offset"]
    en = st + b["duration"]
    txt = b["text"].strip()
    out_lines.append(f"{i+1:02d} | [{st:6.2f}s - {en:6.2f}s] ({b['duration']:5.2f}s) : {txt}")

with open(DIR / "all_sentences_with_times.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))

print(f"Dumped {len(out_lines)} sentences to all_sentences_with_times.txt")
