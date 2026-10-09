import asyncio
import edge_tts
import subprocess
from pathlib import Path

VOICE = "hi-IN-MadhurNeural"
SCRIPT_TEXT = "सच छुपाया गया? हम लाते हैं १००% सबूत! सच! सबूत! बेबाक! बेनाक़ाब इंडिया! सब्सक्राइब करें!"

OUTPUT_DIR = Path(__file__).parent
OUTPUT_MP3 = OUTPUT_DIR / "narration.mp3"

async def generate_speech():
    communicate = edge_tts.Communicate(SCRIPT_TEXT, VOICE, rate="+44%", pitch="+0Hz")
    await communicate.save(str(OUTPUT_MP3))
    print(f"Generated narration: {OUTPUT_MP3}")

    cmd = [
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(OUTPUT_MP3)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    dur = float(res.stdout.strip() or 0)
    print(f"Narration Duration: {dur:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(generate_speech())
