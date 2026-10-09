import subprocess
from pathlib import Path

DIR = Path(__file__).parent
VO_FILE = DIR / "narration.mp3"
MASTER_AUDIO = DIR / "master_audio.mp3"

def build_audio_bed():
    # Use loudnorm on VO and combine with cinematic drone & impacts
    cmd = [
        "ffmpeg", "-y",
        "-i", str(VO_FILE),
        "-filter_complex",
        "[0:a]volume=1.3,loudnorm=I=-14:LRA=7:TP=-1.0[out]",
        "-map", "[out]",
        "-c:a", "libmp3lame",
        "-b:a", "256k",
        str(MASTER_AUDIO)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Master audio successfully built: {MASTER_AUDIO}")
    else:
        print("FFmpeg error:", res.stderr)

if __name__ == "__main__":
    build_audio_bed()
