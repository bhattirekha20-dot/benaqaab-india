import json
import re
import os

with open('word_timestamps.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

boundaries = data.get('boundaries', [])
print(f"Total sentence boundaries: {len(boundaries)}")

all_chunks = []
chunk_id = 1

for b_idx, b in enumerate(boundaries):
    sent_start = float(b['offset'])
    sent_dur = float(b['duration'])
    sent_end = sent_start + sent_dur
    sent_text = b['text'].strip()
    
    # Split sentence into words
    raw_words = sent_text.split()
    if not raw_words:
        continue
        
    # Calculate word durations weighted by word character length
    # A word with 8 chars takes slightly longer than a word with 2 chars
    char_counts = [max(1, len(w)) for w in raw_words]
    total_chars = sum(char_counts)
    
    word_objs = []
    curr_t = sent_start
    for w, c in zip(raw_words, char_counts):
        w_dur = (c / total_chars) * sent_dur
        word_objs.append({
            'word': w,
            'start_s': round(curr_t, 3),
            'end_s': round(curr_t + w_dur, 3)
        })
        curr_t += w_dur
        
    # Group words into readable dynamic chunks (3 to 5 words or max 32 chars)
    curr_chunk_words = []
    curr_chunk_chars = 0
    
    for w_obj in word_objs:
        w_len = len(w_obj['word'])
        if curr_chunk_words and (len(curr_chunk_words) >= 4 or curr_chunk_chars + w_len > 30):
            # Finish current chunk
            all_chunks.append({
                'id': chunk_id,
                'start_s': curr_chunk_words[0]['start_s'],
                'end_s': curr_chunk_words[-1]['end_s'],
                'text': ' '.join([x['word'] for x in curr_chunk_words]),
                'words': curr_chunk_words
            })
            chunk_id += 1
            curr_chunk_words = [w_obj]
            curr_chunk_chars = w_len
        else:
            curr_chunk_words.append(w_obj)
            curr_chunk_chars += w_len + 1
            
    if curr_chunk_words:
        all_chunks.append({
            'id': chunk_id,
            'start_s': curr_chunk_words[0]['start_s'],
            'end_s': curr_chunk_words[-1]['end_s'],
            'text': ' '.join([x['word'] for x in curr_chunk_words]),
            'words': curr_chunk_words
        })
        chunk_id += 1

print(f"Total dynamic caption chunks generated: {len(all_chunks)}")

# Write to captions.js
js_content = f"// Generated deterministic dynamic captions for EP-19\n"
js_content += f"window.CAPTIONS_DATA = {json.dumps(all_chunks, ensure_ascii=False, indent=2)};\n"

with open('captions.js', 'w', encoding='utf-8') as f:
    f.write(js_content)

print("Saved captions.js successfully!")
