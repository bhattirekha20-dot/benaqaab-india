import json

with open('word_timestamps.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

bounds = data.get('boundaries', [])
print('Total sentences:', len(bounds))
for i in range(min(15, len(bounds))):
    b = bounds[i]
    start = b['offset']
    end = start + b['duration']
    print(f"{i+1}: {start:.2f}s - {end:.2f}s ({b['duration']:.2f}s) | {b['text'][:60]}")
