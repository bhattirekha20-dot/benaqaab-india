import speech_recognition as sr
import subprocess
import os
import json
import sys

AUDIO_SOURCE = "video_learning_database/01_milky_way_wormholes/audio/audio_compressed.mp3"
OUT_JSON = "video_learning_database/01_milky_way_wormholes/AUDIO_VISUAL_LOCKSTEP.json"

chunks = [
    {"start": 0, "end": 30, "label": "00:00 - 00:30 (Opening Cosmic Hook)"},
    {"start": 30, "end": 60, "label": "00:30 - 01:00 (Human Lifespan & Rocket Speed Limit)"},
    {"start": 60, "end": 90, "label": "01:00 - 01:30 (Speed of Light Paradox)"},
    {"start": 90, "end": 120, "label": "01:30 - 02:00 (Distance to Nearest Stars & Proxima Centauri)"},
    {"start": 120, "end": 150, "label": "02:00 - 02:30 (Voyager 1 Reality Check)"},
    {"start": 150, "end": 180, "label": "02:30 - 03:00 (The Oort Cloud 30,000-Year Barrier)"},
]

r = sr.Recognizer()
results = []

for idx, c in enumerate(chunks):
    s = c["start"]
    e = c["end"]
    chunk_wav = f"temp_chunk_{idx}.wav"
    cmd = [
        "ffmpeg", "-y", "-ss", str(s), "-to", str(e),
        "-i", AUDIO_SOURCE,
        "-ar", "16000", "-ac", "1",
        chunk_wav
    ]
    subprocess.run(cmd, capture_output=True)

    text = ""
    try:
        with sr.AudioFile(chunk_wav) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data, language='hi-IN')
    except Exception as ex:
        text = f"[Audio processing: music swell or complex audio] - {ex}"

    # Clean temp wav
    if os.path.exists(chunk_wav):
        os.remove(chunk_wav)

    results.append({
        "chunk_index": idx + 1,
        "time_window": c["label"],
        "start_sec": s,
        "end_sec": e,
        "transcript_hi": text
    })
    print(f">> Chunk {idx+1}/{len(chunks)} transcribed: {c['label']}", flush=True)

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(">> Audio-visual lockstep transcription complete!")
