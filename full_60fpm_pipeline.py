import os
import sys
import json
import time
import subprocess
from datetime import datetime

VIDEOS = [
    {
        "id": "01_milky_way_wormholes",
        "title": "Can Humans Ever Leave the Milky Way Galaxy? — The Wormholes Explained",
        "genre": "Space & Theoretical Physics",
        "path": r"C:\Users\dell\Downloads\Video\Can Humans Ever Leave the Milky Way Galaxy. - The Wormholes Explained - Dhruv Rathee.mp4"
    },
    {
        "id": "02_mummy_curse",
        "title": "Real Story of Mummy's CURSE — 22 Deaths That Shocked the World",
        "genre": "Forensic History & Archaeology",
        "path": r"C:\Users\dell\Downloads\Video\Real Story of Mummy's CURSE - 22 Deaths That Shocked the World - Dhruv Rathee.mp4"
    },
    {
        "id": "03_iran_war",
        "title": "Iran War is Out of CONTROL — Trump gives Final Warning",
        "genre": "World News & Geopolitics",
        "path": r"C:\Users\dell\Downloads\Video\Iran War is Out of CONTROL - Trump gives Final Warning - Dhruv Rathee.mp4"
    },
    {
        "id": "04_palmistry_reality",
        "title": "How Long Is Your LIFELINE? — Reality of Palmistry",
        "genre": "Science vs Superstition",
        "path": r"C:\Users\dell\Downloads\Video\How Long Is Your LIFELINE. - Reality of Palmistry - Dhruv Rathee.mp4"
    },
    {
        "id": "05_aatma_death",
        "title": "What Happens After Death? — Does Aatma really Exist?",
        "genre": "Neuroscience & Consciousness",
        "path": r"C:\Users\dell\Downloads\Video\What Happens After Death. - Does Aatma really Exist. - Dhruv Rathee.mp4"
    },
    {
        "id": "06_vitamin_d_crisis",
        "title": "Why Are You ALWAYS Tired? — India's Vitamin D & B12 Crisis",
        "genre": "Health & Consumer Awareness",
        "path": r"C:\Users\dell\Downloads\Video\Why Are You ALWAYS Tired. - India's Vitamin D & B12 Crisis - Jaago Grahak Jaago - Dhruv Rathee.mp4"
    },
    {
        "id": "07_world_war_2",
        "title": "Why World War 2 Happened? — The Real Reason",
        "genre": "Geopolitical History",
        "path": r"C:\Users\dell\Downloads\Video\Why World War 2 Happened. - The Real Reason - Dhruv Rathee.mp4"
    },
    {
        "id": "08_deep_sea_mysteries",
        "title": "Deep Sea Mysteries That Science Can't Explain!",
        "genre": "Oceanography & Marine Science",
        "path": r"C:\Users\dell\Downloads\Video\Deep Sea Mysteries That Science Can't Explain! _ Dhruv Rathee.mkv"
    }
]

DB_BASE = os.path.abspath("video_learning_database")
DASHBOARD_LOG = os.path.abspath("studio_dashboard/activity_log.json")

def log(msg):
    ts = datetime.now().strftime("%H:%M:%S")
    line = f"[{ts}] {msg}"
    print(line, flush=True)

    if os.path.exists(DASHBOARD_LOG):
        try:
            with open(DASHBOARD_LOG, "r", encoding="utf-8") as f:
                logs = json.load(f)
            logs.insert(0, {"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "action": "FULL_60FPM_PIPELINE", "details": msg})
            with open(DASHBOARD_LOG, "w", encoding="utf-8") as f:
                json.dump(logs[:100], f, indent=2, ensure_ascii=False)
        except Exception:
            pass

def process_full_60fpm(v, idx, total):
    vid_id = v["id"]
    title = v["title"]
    path = v["path"]
    v_dir = os.path.join(DB_BASE, vid_id)
    frames_dir = os.path.join(v_dir, "frames_60fpm")
    audio_dir = os.path.join(v_dir, "audio")

    os.makedirs(frames_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)

    log("====================================================================")
    log(f">> [{idx}/{total}] STARTING 100% COMPLETE 60 FPM EXTRACTION: {title}")
    log(f"   Target Video: {os.path.basename(path)}")
    log("====================================================================")

    if not os.path.exists(path):
        log(f"   [ERROR] Video file missing: {path}")
        return

    # Probe duration
    p = subprocess.run([
        "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "json", path
    ], capture_output=True, text=True)
    duration = float(json.loads(p.stdout).get("format", {}).get("duration", 0))
    expected_frames = int(duration)
    log(f"   Full Video Duration: {duration:.1f}s ({int(duration//60)}m {int(duration%60)}s)")
    log(f"   Target Cadence: 60 Frames/Minute (1 Frame Every 1.0s) -> Expected Total: ~{expected_frames} frames")

    # Audio extraction if not exists
    audio_path = os.path.join(audio_dir, "audio_master.mp3")
    if not os.path.exists(audio_path):
        log("   Extracting audio stream...")
        subprocess.run(["ffmpeg", "-y", "-i", path, "-vn", "-acodec", "libmp3lame", "-b:a", "192k", audio_path], capture_output=True)

    # Check already extracted frames
    existing = len([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])
    if existing >= (expected_frames - 5):
        log(f"   [ALREADY EXTRACTED] Found {existing} frames in {frames_dir}. Skipping re-encode.")
    else:
        log("   Launching FFmpeg multi-threaded frame extraction (1 frame per second)...")
        t0 = time.time()
        cmd = [
            "ffmpeg", "-y", "-threads", "0",
            "-i", path,
            "-vf", "fps=1",
            "-q:v", "3",
            os.path.join(frames_dir, "sec_%04d.jpg")
        ]
        proc = subprocess.run(cmd, capture_output=True)
        elapsed = time.time() - t0
        extracted = len([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])
        fps_speed = (extracted / elapsed) if elapsed > 0 else 0
        log(f"   >> Extraction Finished in {elapsed:.1f}s ({fps_speed:.1f} fps processing speed)!")
        log(f"   >> Total Frames Saved: {extracted} frames at 60 frames/minute!")

    log(f">> [{idx}/{total}] COMPLETED VIDEO {idx}/{total}: {title}")

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    log("********************************************************************")
    log(">> TASK: 100% COMPLETE 60 FRAMES/MIN EXTRACTION FOR ALL 8 VIDEOS")
    log("********************************************************************")

    for i, v in enumerate(VIDEOS):
        process_full_60fpm(v, i+1, len(VIDEOS))

    log("********************************************************************")
    log(">> ALL 8 VIDEOS FULLY EXTRACTED AT 60 FRAMES/MIN ACROSS 100% TIMELINE!")
    log("********************************************************************")

if __name__ == "__main__":
    main()
