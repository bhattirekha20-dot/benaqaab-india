import subprocess
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR = Path(__file__).parent
VO_FILE = DIR / "narration.mp3"
MASTER_AUDIO = DIR / "master_audio.mp3"

def build_master_audio():
    print("🎵 Mastering audio to YouTube broadcast standard (-14 LUFS, True Peak <= -1.0 dBFS)...")
    
    # Generate cinematic tension bed: subtle low-frequency 55Hz cinematic sub drone + high-pass sparkle + VO loudnorm
    # Duration ~50s
    cmd = [
        "ffmpeg", "-y",
        "-i", str(VO_FILE),
        "-f", "lavfi", "-i", "anoisesrc=d=50:c=pink:r=48000:a=0.015,lowpass=f=120,volume=0.8",
        "-f", "lavfi", "-i", "sine=f=60:d=50,volume=0.15",
        "-filter_complex",
        "[1:a][2:a]amix=inputs=2:duration=first[bed];"
        "[0:a]volume=1.4[voice];"
        "[voice][bed]amix=inputs=2:weights=1.0 0.25:duration=first[mix];"
        "[mix]loudnorm=I=-14:LRA=7:TP=-1.0[out]",
        "-map", "[out]",
        "-c:a", "libmp3lame",
        "-b:a", "320k",
        str(MASTER_AUDIO)
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"✅ Master audio created: {MASTER_AUDIO}")
        # Probe duration
        probe = subprocess.run([
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(MASTER_AUDIO)
        ], capture_output=True, text=True)
        dur = float(probe.stdout.strip() or 0)
        print(f"⏱️ Master Audio Duration: {dur:.2f}s")
    else:
        print("FFmpeg error:", res.stderr)

if __name__ == "__main__":
    build_master_audio()
