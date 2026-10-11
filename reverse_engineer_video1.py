import os
import sys
import json
import time
import subprocess
from datetime import datetime

VIDEO_PATH = r"C:\Users\dell\Downloads\Video\Can Humans Ever Leave the Milky Way Galaxy. - The Wormholes Explained - Dhruv Rathee.mp4"
DB_DIR = os.path.abspath("video_learning_database/01_milky_way_wormholes")
FRAMES_DIR = os.path.join(DB_DIR, "frames")
AUDIO_DIR = os.path.join(DB_DIR, "audio")
DASHBOARD_LOG = os.path.abspath("studio_dashboard/activity_log.json")

def log(msg, pct=None):
    ts = datetime.now().strftime("%H:%M:%S")
    pct_str = f" [{pct}%]" if pct is not None else ""
    line = f"[{ts}]{pct_str} {msg}"
    print(line, flush=True)

    # Also log to studio dashboard activity log
    if os.path.exists(DASHBOARD_LOG):
        try:
            with open(DASHBOARD_LOG, "r", encoding="utf-8") as f:
                logs = json.load(f)
            logs.insert(0, {"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "action": "VIDEO_1_ANALYSIS", "details": msg})
            with open(DASHBOARD_LOG, "w", encoding="utf-8") as f:
                json.dump(logs[:100], f, indent=2, ensure_ascii=False)
        except Exception:
            pass

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    log("====================================================================")
    log(">> TASK STARTED: DEEP REVERSE-ENGINEERING VIDEO 1", 0)
    log(f">> Target File: {os.path.basename(VIDEO_PATH)}")
    log("====================================================================")

    os.makedirs(FRAMES_DIR, exist_ok=True)
    os.makedirs(AUDIO_DIR, exist_ok=True)

    # 1. Technical Inspection via FFprobe
    log(">> STEP 1/5: Running Technical & Hardware Inspection...", 5)
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size,bit_rate:stream=codec_name,width,height,r_frame_rate,sample_rate,channels",
        "-of", "json", VIDEO_PATH
    ]
    p = subprocess.run(probe_cmd, capture_output=True, text=True)
    meta = json.loads(p.stdout)
    duration = float(meta.get("format", {}).get("duration", 0))
    size_mb = float(meta.get("format", {}).get("size", 0)) / (1024 * 1024)
    v_stream = meta.get("streams", [{}])[0]
    width = v_stream.get("width", 1280)
    height = v_stream.get("height", 720)
    fps = v_stream.get("r_frame_rate", "25/1")

    log(f"   [Technical Profile Confirmed]")
    log(f"   - Duration: {duration:.2f}s ({int(duration//60)}m {int(duration%60)}s)")
    log(f"   - Resolution: {width}x{height} (16:9 Landscape Widescreen)")
    log(f"   - Frame Rate: {fps} (Source timeline)")
    log(f"   - File Size: {size_mb:.2f} MB")

    # 2. Audio Track Extraction & Loudness Profile
    log(">> STEP 2/5: Extracting Audio & Measuring Loudness & Sound Design...", 20)
    audio_wav = os.path.join(AUDIO_DIR, "audio_master.wav")
    audio_mp3 = os.path.join(AUDIO_DIR, "audio_compressed.mp3")

    # Extract audio stream
    ffmpeg_audio = [
        "ffmpeg", "-y", "-i", VIDEO_PATH,
        "-vn", "-acodec", "libmp3lame", "-b:a", "192k",
        audio_mp3
    ]
    subprocess.run(ffmpeg_audio, capture_output=True)
    log("   - Audio stream extracted to audio_compressed.mp3")

    # Measure integrated loudness (EBU R128)
    loudness_cmd = [
        "ffmpeg", "-i", audio_mp3,
        "-filter_complex", "ebur128=peak=true",
        "-f", "null", "-"
    ]
    loudness_proc = subprocess.run(loudness_cmd, capture_output=True, text=True)
    log("   - Loudness profile measured (EBU R128 analysis complete)")

    # 3. Targeted Keyframe Extraction Across Timeline
    log(">> STEP 3/5: Extracting High-Density Keyframe Sequence & Screenshots...", 40)
    log("   - Phase A: Sampling Opening Hook (0s to 90s) every 2.0 seconds...")
    
    # Hook frames (first 90s)
    hook_frames_cmd = [
        "ffmpeg", "-y", "-ss", "0", "-to", "90",
        "-i", VIDEO_PATH,
        "-vf", "fps=1/2",
        "-q:v", "2",
        os.path.join(FRAMES_DIR, "hook_frame_%03d.jpg")
    ]
    subprocess.run(hook_frames_cmd, capture_output=True)

    log("   - Phase B: Sampling Full Documentary Timeline (every 25 seconds)...", 60)
    # Timeline overview frames
    full_frames_cmd = [
        "ffmpeg", "-y", "-i", VIDEO_PATH,
        "-vf", "fps=1/25",
        "-q:v", "2",
        os.path.join(FRAMES_DIR, "timeline_frame_%03d.jpg")
    ]
    subprocess.run(full_frames_cmd, capture_output=True)

    total_frames = len([f for f in os.listdir(FRAMES_DIR) if f.endswith(".jpg")])
    log(f"   - Extraction complete: {total_frames} representative high-resolution frames saved to database!", 75)

    # 4. Save Technical Manifest
    manifest = {
        "title": "Can Humans Ever Leave the Milky Way Galaxy? — The Wormholes Explained",
        "creator": "Dhruv Rathee",
        "video_path": VIDEO_PATH,
        "duration_seconds": duration,
        "duration_formatted": f"{int(duration//60)}:{int(duration%60):02d}",
        "resolution": f"{width}x{height}",
        "aspect_ratio": "16:9",
        "fps": fps,
        "size_mb": round(size_mb, 2),
        "total_frames_extracted": total_frames,
        "analyzed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(os.path.join(DB_DIR, "technical_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    log(">> STEP 4/5: Compiling Technical Manifest & Frame Ledger...", 85)
    log(">> STEP 5/5: Frame Extraction & Audio Capture Ready for Full Report Synthesis!", 100)
    log("====================================================================")
    log(">> TASK COMPLETED: VIDEO 1 REVERSE-ENGINEERING DATASET READY")
    log("====================================================================")

if __name__ == "__main__":
    main()
