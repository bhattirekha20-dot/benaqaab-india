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

VOICE = "hi-IN-MadhurNeural"
OUTPUT_DIR = Path(__file__).parent
OUTPUT_MP3 = OUTPUT_DIR / "narration.mp3"
TIMESTAMPS_JSON = OUTPUT_DIR / "word_timestamps.json"

SCRIPT_TEXT = (
    "क्या आपको लगता है गगनयान सिर्फ तीन दिन का एक छोटा सा मिशन है? बिल्कुल गलत! "
    "अठारह सितंबर को कैबिनेट ने चुपचाप बीस हज़ार एक सौ तिरानवे करोड़ रुपये का नया रोडमैप मंज़ूर किया... "
    "जिसमें सिर्फ एक नहीं, बल्कि पूरे आठ स्पेस मिशन्स तय किए गए हैं! "
    "लेकिन इंसानों से पहले अंतरिक्ष में जाएगी 'व्योममित्र'—एक फीमेल ह्यूमनॉइड रोबोट, "
    "जो ज़ीरो-ग्रैविटी में हर एक लाइफ सपोर्ट सिस्टम की जांच करेगी! "
    "क्योंकि दो हज़ार तीस में इंटरनेशनल स्पेस स्टेशन खत्म हो रहा है, "
    "और भारत को अपना खुद का भारतीय अंतरिक्ष स्टेशन खड़ा करना है! "
    "इस पूरे महा-मिशन की एक्सक्लूसिव इन्वेस्टिगेशन प्रीमियर हो रही है... "
    "ग्यारह अक्टूबर, सुबह चार बजे आई-एस-टी! "
    "सच, सबूत, बेबाक। बेनाक़ाब इंडिया को अभी सब्सक्राइब करें और बेल आइकॉन दबाएं!"
)

async def generate_speech():
    print("🎙️ Generating high-energy investigative voiceover with edge_tts...")
    communicate = edge_tts.Communicate(SCRIPT_TEXT, VOICE, rate="+24%", pitch="+0Hz")
    
    submaker = edge_tts.SubMaker()
    with open(OUTPUT_MP3, "wb") as f:
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                f.write(chunk["data"])
            elif chunk["type"] == "WordBoundary":
                submaker.feed(chunk)
                
    print(f"✅ Narration saved to: {OUTPUT_MP3}")
    
    # Measure exact audio duration
    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(OUTPUT_MP3)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    duration = float(res.stdout.strip() or 0)
    print(f"⏱️ Narration Duration: {duration:.2f} seconds")
    
    # Save word timestamps if needed
    with open(TIMESTAMPS_JSON, "w", encoding="utf-8") as f:
        json.dump({"duration": duration, "text": SCRIPT_TEXT}, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    asyncio.run(generate_speech())
