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

# Tuned to strictly hit ~47.5-48.5 seconds (under 50s rule)
SCRIPT_TEXT = (
    "बिना OTP, बिना ATM कार्ड, और बिना बैंक जाए— "
    "अकाउंट से पूरे दस हज़ार रुपये साफ़ हो गए! "
    "और चोर के पास सिर्फ़ एक चीज़ थी: आपका नकली सिलिकॉन अंगूठा! "
    "यह है AePS यानी आधार इनेबल्ड पेमेंट सिस्टम का सबसे बड़ा फ्रॉड! "
    "स्कैमर्स ज़मीन रजिस्ट्री साइट्स से सेल डीड डाउनलोड करते हैं, "
    "जहाँ आपका हाई-रेज़ फिंगरप्रिंट और आधार नंबर पब्लिकली मौजूद है! "
    "बटर पेपर और लिक्विड सिलिकॉन से बनती है हूबहू नकली उंगली! "
    "और पुराने L0 स्कैनर पर लगाते ही बैंक से पूरे ₹10,000 ग़ायब! "
    "लेकिन बचने का एक अचूक तरीक़ा है: "
    "अभी mAadhaar ऐप खोलें, और बायोमेट्रिक्स को LOCK कर दें! "
    "इसके बाद कोई क्लोन भी लगा ले, तो स्क्रीन पर आएगा— एरर तीन सौ तीस: लॉक्ड! "
    "सच, सबूत, बेबाक। सब्सक्राइब बेनाक़ाब इंडिया!"
)

VOICE = "hi-IN-SwaraNeural"

async def test_and_gen():
    print(f"🎙️ Generating voiceover using {VOICE} at +31% rate...")
    comm = edge_tts.Communicate(SCRIPT_TEXT, VOICE, rate="+31%", pitch="+0Hz")
    
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

    # Master audio with loudness normalization (-14 LUFS) and punchy broadcast limiting
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
