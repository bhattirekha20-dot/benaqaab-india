import asyncio
import edge_tts
import subprocess
import os
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass


DIR = Path(r"projects/ep18_gaganyaan_short_promo")
CHUNK_DIR = DIR / "audio_chunks"
CHUNK_DIR.mkdir(parents=True, exist_ok=True)

# Exact Hinglish script from short/script_hinglish.md
CHUNKS = [
    {
        "id": "scene1",
        "title": "HOOK - Rocket Launch",
        "text": "18 September 2024. India की कैबिनेट ने चुपके से एक बड़ा decision लिया — Gaganyaan का budget सीधे 9000 crore से बढ़ाकर 11,193 crore! आखिर इतना पैसा क्यों?",
        "caption_main": "₹9,000 Cr → ₹11,193 Cr",
        "caption_sub": "GAGANYAAN BUDGET",
        "words": [
            ("18 SEPTEMBER 2024", 0.0, 1.8),
            ("CABINET KA BADA DECISION", 1.8, 4.2),
            ("GAGANYAAN BUDGET", 4.2, 6.5),
            ("₹9,000 Cr → ₹11,193 Cr!", 6.5, 9.8),
            ("ITNA PAISA KYUN?", 9.8, 12.0)
        ]
    },
    {
        "id": "scene2",
        "title": "MYTH BUST - Space Station",
        "text": "लोग सोचते हैं — Gaganyaan मतलब सिर्फ़ एक छोटा space trip. बिल्कुल ग़लत! India तो अपना Bharatiya Antariksh Station बना रहा है!",
        "caption_main": "SIRF EK TRIP?",
        "caption_sub": "APNA SPACE STATION",
        "words": [
            ("SIRF EK CHHOTA TRIP?", 0.0, 2.8),
            ("BILKUL GALAT!", 2.8, 4.5),
            ("BHARATIYA ANTARIKSH STATION", 4.5, 7.2),
            ("APNA SPACE STATION!", 7.2, 8.8)
        ]
    },
    {
        "id": "scene3",
        "title": "VYOMMITRA - Robot Cockpit",
        "text": "2026 के end में पहले Vyommitra — एक half-humanoid robot. उसके बाद, 2028 में — Indian astronauts की पहली उड़ान!",
        "caption_main": "2026: PEHLE ROBOT",
        "caption_sub": "VYOMMITRA",
        "words": [
            ("2026: PEHLE VYOMMITRA", 0.0, 2.8),
            ("HALF-HUMANOID ROBOT", 2.8, 5.0),
            ("AUR 2028 MEIN...", 5.0, 6.8),
            ("INDIAN ASTRONAUTS KI UDAAN!", 6.8, 8.8)
        ]
    },
    {
        "id": "scene4",
        "title": "PROOF - Capsule Parachutes",
        "text": "CE20 engine ने बनाया world record. Abort test में दिखाया — zero human risk. और 20,000 crore की यह blueprint — भारत की अगले 50 साल की आज़ादी है!",
        "caption_main": "WORLD RECORD",
        "caption_sub": "ZERO HUMAN RISK",
        "words": [
            ("CE20 WORLD RECORD", 0.0, 2.5),
            ("ABORT TEST SUCCESS", 2.5, 4.8),
            ("ZERO HUMAN RISK!", 4.8, 6.8),
            ("AGLE 50 SAAL KI AZADI!", 6.8, 10.5)
        ]
    },
    {
        "id": "scene5",
        "title": "CTA - Flag on Moon",
        "text": "Full सच, with proof — पूरी video देखो, link in bio! LIVE: 11 October, 4:00 AM IST. बेनाक़ाब इंडिया को subscribe करो! जय हिंद!",
        "caption_main": "LIVE — 11 OCT, 4:00 AM IST",
        "caption_sub": "LINK IN BIO",
        "words": [
            ("FULL SACH WITH PROOF", 0.0, 2.4),
            ("LINK IN BIO!", 2.4, 4.5),
            ("LIVE: 11 OCT · 4:00 AM IST", 4.5, 7.5),
            ("SUBSCRIBE BENAQAAB INDIA", 7.5, 9.8),
            ("JAI HIND! 🇮🇳", 9.8, 10.8)
        ]
    }
]

VOICE = "hi-IN-MadhurNeural"
RATE = "+28%"

async def generate():
    print("🎙️ Generating audio chunks with Edge-TTS (voice: Madhur, rate: +28%)...")
    concat_list = []
    current_offset = 0.0
    scene_timeline = []

    for idx, c in enumerate(CHUNKS, start=1):
        filename = f"chunk_{idx}_{c['id']}.mp3"
        filepath = CHUNK_DIR / filename
        comm = edge_tts.Communicate(c["text"], VOICE, rate=RATE)
        await comm.save(str(filepath))

        probe = subprocess.run([
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(filepath)
        ], capture_output=True, text=True)
        dur = float(probe.stdout.strip() or 0)
        print(f"  ✅ Chunk {idx} ({c['id']}): {dur:.2f}s")

        scene_timeline.append({
            "scene": idx,
            "id": c["id"],
            "image": f"assets/scene{idx}.png",
            "start": round(current_offset, 2),
            "end": round(current_offset + dur, 2),
            "duration": round(dur, 2),
            "title": c["title"],
            "caption_main": c["caption_main"],
            "caption_sub": c["caption_sub"],
            "sub_beats": [
                {
                    "text": w[0],
                    "start": round(current_offset + w[1], 2),
                    "end": round(current_offset + w[2], 2)
                } for w in c["words"]
            ]
        })
        current_offset += dur
        concat_list.append(str(filepath.resolve()))

    total_duration = current_offset
    print(f"\n⏱️ Total Voiceover Duration: {total_duration:.2f}s (Target: < 60s)")

    # Write concat list for FFmpeg
    concat_file = CHUNK_DIR / "concat_list.txt"
    with open(concat_file, "w", encoding="utf-8") as f:
        for p in concat_list:
            f.write(f"file '{p}'\n")

    # Stitch into master narration
    raw_stitched = DIR / "raw_stitched.mp3"
    subprocess.run([
        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
        "-i", str(concat_file),
        "-c", "copy",
        str(raw_stitched)
    ], check=True)

    # Master audio with loudnorm (-14 LUFS) and subtle compression
    master_mp3 = DIR / "master_audio.mp3"
    subprocess.run([
        "ffmpeg", "-y",
        "-i", str(raw_stitched),
        "-filter_complex",
        "[0:a]volume=1.35,loudnorm=I=-14:LRA=6:TP=-1.0[out]",
        "-map", "[out]",
        "-c:a", "libmp3lame",
        "-b:a", "320k",
        str(master_mp3)
    ], check=True)

    # Verify final master duration
    probe_master = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(master_mp3)
    ], capture_output=True, text=True)
    master_dur = float(probe_master.stdout.strip() or 0)
    print(f"🎵 Master Audio Rendered: {master_mp3} ({master_dur:.2f}s)")

    # Save exact scene timeline JSON
    timeline_file = DIR / "scene_timeline.json"
    with open(timeline_file, "w", encoding="utf-8") as f:
        json.dump({
            "total_duration": master_dur,
            "scenes": scene_timeline
        }, f, indent=2, ensure_ascii=False)
    print(f"📋 Timeline saved to {timeline_file}")

if __name__ == "__main__":
    asyncio.run(generate())
