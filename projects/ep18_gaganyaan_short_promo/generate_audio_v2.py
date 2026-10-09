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
OUTPUT_MP3 = DIR / "narration_v2.mp3"
MASTER_MP3 = DIR / "master_audio_v2.mp3"

SCRIPT_TEXT = (
    "क्या आपको लगता है गगनयान सिर्फ तीन दिन का मिशन है? "
    "गलत! "
    "असली सच छुपा है इस अठारह सितंबर के कैबिनेट ऑर्डर में! "
    "सरकार ने चुपचाप बीस हज़ार एक सौ तिरानवे करोड़ का नया बजट पास किया... "
    "जिसमें एक नहीं, बल्कि पूरे आठ स्पेस मिशन्स तय हैं! "
    "और इंसानों से पहले अंतरिक्ष में जाएगी 'व्योममित्र'— "
    "एक ह्यूमनॉइड रोबोट, जो ज़ीरो-ग्रैविटी में हर एक लाइफ सपोर्ट सिस्टम टेस्ट करेगी! "
    "क्योंकि दो हज़ार तीस में इंटरनेशनल स्पेस स्टेशन खत्म हो रहा है... "
    "और भारत खड़ा कर रहा है अपना खुद का स्पेस स्टेशन! "
    "इस पूरे महा-मिशन का सबसे बड़ा खुलासा... "
    "लाइव प्रीमियर हो रहा है: ग्यारह अक्टूबर, सुबह चार बजे आई-एस-टी! "
    "बेनाक़ाब इंडिया को अभी सब्सक्राइब करें!"
)

VOICE = "hi-IN-MadhurNeural"

async def gen():
    print("🎙️ Generating punchy, fast-paced voiceover v2...")
    comm = edge_tts.Communicate(SCRIPT_TEXT, VOICE, rate="+30%", pitch="+0Hz")
    await comm.save(str(OUTPUT_MP3))
    print(f"✅ Generated {OUTPUT_MP3}")

    # Build master audio with loudnorm & punchy limiter
    cmd = [
        "ffmpeg", "-y",
        "-i", str(OUTPUT_MP3),
        "-filter_complex",
        "[0:a]volume=1.4,loudnorm=I=-14:LRA=6:TP=-1.0[out]",
        "-map", "[out]",
        "-c:a", "libmp3lame",
        "-b:a", "320k",
        str(MASTER_MP3)
    ]
    subprocess.run(cmd, check=True)

    probe = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(MASTER_MP3)
    ], capture_output=True, text=True)
    dur = float(probe.stdout.strip() or 0)
    print(f"⏱️ Master Audio Duration: {dur:.2f}s")

if __name__ == "__main__":
    asyncio.run(gen())
