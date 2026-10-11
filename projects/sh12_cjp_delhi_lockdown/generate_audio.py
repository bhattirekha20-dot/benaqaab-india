import asyncio
import edge_tts
import subprocess
import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR = Path(__file__).parent
OUTPUT_RAW_MP3 = DIR / "narration_raw.mp3"
MASTER_MP3 = DIR / "master_audio.mp3"
TIMESTAMPS_JSON = DIR / "word_timestamps.json"

# Tightened for crisp, viral, strictly under-50s retention (~47 seconds)
SCRIPT_TEXT = (
    "आज दिल्ली में ऐसा क्या हुआ कि पैंतालीस मेट्रो स्टेशन बंद कर दिए गए, "
    "पच्चीस हज़ार पुलिस तैनात हुई, और फ़्लाइट में घुसकर अरेस्ट करना पड़ा? "
    "इस पूरे बवाल के पीछे है एक संगठन— 'कॉकरोच जनता पार्टी'! "
    "नाम अजीब लगा? जब एक जज ने बेरोज़गार युवाओं को 'कॉकरोच' कहा, "
    "तो यूथ ने इसी नाम को अपना हथियार बना लिया! "
    "लेकिन आज जंतर-मंतर पर इनकी मांग क्या थी? "
    "चीफ़ इलेक्शन कमिश्नर ज्ञानेश कुमार का इस्तीफ़ा! "
    "क्योंकि वोटर लिस्ट से लाखों नौजवानों के नाम ग़ायब कर दिए गए! "
    "फ़ाउंडर अभिजीत दिपके को फ़्लाइट में अरेस्ट किया, "
    "ट्रेनें रोकीं, और इंटरनेट बंद! "
    "सुप्रीम कोर्ट ने आज फटकार लगाई: "
    "'एक मक्खी मारने के लिए हथौड़ा नहीं चलाया जाता!' "
    "सच, सबूत, बेबाक। सब्सक्राइब बेनाक़ाब इंडिया!"
)

VOICE = "hi-IN-SwaraNeural"

async def test_and_gen():
    print(f"🎙️ Generating voiceover using {VOICE} at +28% rate...")
    comm = edge_tts.Communicate(SCRIPT_TEXT, VOICE, rate="+28%", pitch="+0Hz")
    
    boundaries = []
    with open(OUTPUT_RAW_MP3, "wb") as f:
        async for chunk in comm.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] in ("WordBoundary", "SentenceBoundary"):
                boundaries.append({
                    "type": chunk["type"],
                    "offset": chunk["offset"] / 10_000_000,
                    "duration": chunk["duration"] / 10_000_000,
                    "text": chunk.get("text", "")
                })

    print(f"✅ Raw audio saved to: {OUTPUT_RAW_MP3}")
    print(f"📊 Captured {len(boundaries)} boundaries.")

    # Master audio with loudness normalization (-14 LUFS) and punchy limiting
    print("🎛️ Mastering audio to -14 LUFS broadcast standard...")
    cmd = [
        "ffmpeg", "-y",
        "-i", str(OUTPUT_RAW_MP3),
        "-filter_complex",
        "[0:a]volume=1.35,loudnorm=I=-14:LRA=6:TP=-1.0[out]",
        "-map", "[out]",
        "-c:a", "libmp3lame",
        "-b:a", "320k",
        str(MASTER_MP3)
    ]
    subprocess.run(cmd, check=True)

    # Measure exact duration
    probe = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(MASTER_MP3)
    ], capture_output=True, text=True)
    duration = float(probe.stdout.strip() or 0)
    print(f"⏱️ Master Audio Duration: {duration:.2f} seconds")

    with open(TIMESTAMPS_JSON, "w", encoding="utf-8") as f:
        json.dump({
            "duration": duration,
            "script": SCRIPT_TEXT,
            "boundaries": boundaries
        }, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    asyncio.run(test_and_gen())
