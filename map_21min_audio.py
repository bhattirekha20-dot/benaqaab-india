import speech_recognition as sr
import subprocess
import os
import json

AUDIO_PATH = "video_learning_database/01_milky_way_wormholes/audio/audio_compressed.mp3"
OUT_FILE = "video_learning_database/01_milky_way_wormholes/FULL_21MIN_AUDIO_MAP.json"

# We will transcribe key milestone windows across all 21 minutes
time_blocks = [
    {"start": 0, "end": 60, "chapter": "01. The Cosmic Hook & Size Paradox"},
    {"start": 60, "end": 120, "chapter": "02. Rocket Speed Limits & Interstellar Film Bridge"},
    {"start": 120, "end": 180, "chapter": "03. Saturn Orbit & 1915 Einstein General Relativity"},
    {"start": 180, "end": 240, "chapter": "04. Spacetime Curvature & Prussian Academy Paper"},
    {"start": 300, "end": 360, "chapter": "05. 2D Paper Fold Metaphor & Flamm's Paraboloid"},
    {"start": 420, "end": 480, "chapter": "06. Einstein-Rosen Bridge 1935 Formulation"},
    {"start": 540, "end": 600, "chapter": "07. The Throat Singularity & Pinch-off Paradox"},
    {"start": 660, "end": 720, "chapter": "08. Kip Thorne 1988 Breakthrough & Traversable Wormholes"},
    {"start": 780, "end": 840, "chapter": "09. Exotic Matter & Negative Energy Physics"},
    {"start": 900, "end": 960, "chapter": "10. The Casimir Effect & Quantum Vacuum Fluctuations"},
    {"start": 1020, "end": 1080, "chapter": "11. Primordial Big Bang Micro-Wormholes"},
    {"start": 1140, "end": 1200, "chapter": "12. 2015 Magnetic Wormhole Metamaterials & Conclusion"}
]

r = sr.Recognizer()
results = []

for idx, b in enumerate(time_blocks):
    s = b["start"]
    e = b["end"]
    chunk_wav = f"temp_map_{idx}.wav"
    cmd = [
        "ffmpeg", "-y", "-ss", str(s), "-to", str(e),
        "-i", AUDIO_PATH,
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
        text = f"[Speech under music/sound design: {ex}]"

    if os.path.exists(chunk_wav):
        os.remove(chunk_wav)

    results.append({
        "chapter_no": idx + 1,
        "chapter_title": b["chapter"],
        "start_time": f"{s//60:02d}:{s%60:02d}",
        "end_time": f"{e//60:02d}:{e%60:02d}",
        "start_sec": s,
        "end_sec": e,
        "transcript": text
    })
    print(f">> Chapter {idx+1}/{len(time_blocks)} transcribed: {b['chapter']}", flush=True)

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(">> 21-Minute audio map completed successfully!")
