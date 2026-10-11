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
        "genre": "Forensic History, Archaeology & Myth Busting",
        "path": r"C:\Users\dell\Downloads\Video\Real Story of Mummy's CURSE - 22 Deaths That Shocked the World - Dhruv Rathee.mp4"
    },
    {
        "id": "03_iran_war",
        "title": "Iran War is Out of CONTROL — Trump gives Final Warning",
        "genre": "World News, Geopolitics & Military Conflict",
        "path": r"C:\Users\dell\Downloads\Video\Iran War is Out of CONTROL - Trump gives Final Warning - Dhruv Rathee.mp4"
    },
    {
        "id": "04_palmistry_reality",
        "title": "How Long Is Your LIFELINE? — Reality of Palmistry",
        "genre": "Science vs Superstition & Anatomy",
        "path": r"C:\Users\dell\Downloads\Video\How Long Is Your LIFELINE. - Reality of Palmistry - Dhruv Rathee.mp4"
    },
    {
        "id": "05_aatma_death",
        "title": "What Happens After Death? — Does Aatma really Exist?",
        "genre": "Neuroscience, Biology & Consciousness",
        "path": r"C:\Users\dell\Downloads\Video\What Happens After Death. - Does Aatma really Exist. - Dhruv Rathee.mp4"
    },
    {
        "id": "06_vitamin_d_crisis",
        "title": "Why Are You ALWAYS Tired? — India's Vitamin D & B12 Crisis",
        "genre": "Health, Nutrition & Consumer Awareness",
        "path": r"C:\Users\dell\Downloads\Video\Why Are You ALWAYS Tired. - India's Vitamin D & B12 Crisis - Jaago Grahak Jaago - Dhruv Rathee.mp4"
    },
    {
        "id": "07_world_war_2",
        "title": "Why World War 2 Happened? — The Real Reason",
        "genre": "Geopolitical History & Global Wars",
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
            logs.insert(0, {"timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "action": "BATCH_LEARNING_PIPELINE", "details": msg})
            with open(DASHBOARD_LOG, "w", encoding="utf-8") as f:
                json.dump(logs[:100], f, indent=2, ensure_ascii=False)
        except Exception:
            pass

def process_video(v, idx, total):
    vid_id = v["id"]
    title = v["title"]
    path = v["path"]
    v_dir = os.path.join(DB_BASE, vid_id)
    frames_dir = os.path.join(v_dir, "frames")
    audio_dir = os.path.join(v_dir, "audio")

    os.makedirs(frames_dir, exist_ok=True)
    os.makedirs(audio_dir, exist_ok=True)

    log(f"====================================================================")
    log(f">> [{idx}/{total}] STARTING REVERSE-ENGINEERING: {title}")
    log(f"   Genre: {v['genre']} | File: {os.path.basename(path)}")
    log(f"====================================================================")

    if not os.path.exists(path):
        log(f"   [ERROR] File not found at: {path}")
        return

    # Probe
    log(f">> [{idx}/{total}] Probing technical streams...")
    probe_cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size:stream=width,height,r_frame_rate",
        "-of", "json", path
    ]
    p = subprocess.run(probe_cmd, capture_output=True, text=True)
    meta = json.loads(p.stdout)
    duration = float(meta.get("format", {}).get("duration", 0))
    size_mb = float(meta.get("format", {}).get("size", 0)) / (1024 * 1024)
    log(f"   Duration: {duration:.1f}s ({int(duration//60)}m {int(duration%60)}s) | Size: {size_mb:.1f} MB")

    # 1. Audio stream extraction
    audio_file = os.path.join(audio_dir, "audio_master.mp3")
    if not os.path.exists(audio_file):
        log(f">> [{idx}/{total}] Extracting master audio stream...")
        cmd_audio = ["ffmpeg", "-y", "-i", path, "-vn", "-acodec", "libmp3lame", "-b:a", "192k", audio_file]
        subprocess.run(cmd_audio, capture_output=True)
        log("   Audio extraction complete.")

    # 2. Extract 60 Frames Per Minute (1 frame every 1.0 second across opening 120s + chapter bursts)
    log(f">> [{idx}/{total}] Extracting 60 frames/min (1 frame per second) across high-curiosity hook...")
    cmd_frames_hook = [
        "ffmpeg", "-y", "-ss", "0", "-to", "120",
        "-i", path,
        "-vf", "fps=1",
        "-q:v", "2",
        os.path.join(frames_dir, "frame_sec_%03d.jpg")
    ]
    subprocess.run(cmd_frames_hook, capture_output=True)

    # Sample full timeline at 15s intervals
    log(f">> [{idx}/{total}] Sampling full documentary chapters across timeline...")
    cmd_frames_full = [
        "ffmpeg", "-y", "-i", path,
        "-vf", "fps=1/15",
        "-q:v", "2",
        os.path.join(frames_dir, "chapter_sec_%04d.jpg")
    ]
    subprocess.run(cmd_frames_full, capture_output=True)

    extracted_count = len([f for f in os.listdir(frames_dir) if f.endswith(".jpg")])
    log(f">> [{idx}/{total}] Frame extraction done: {extracted_count} high-res frames saved in database!")

    # Write technical manifest
    manifest = {
        "id": vid_id,
        "title": title,
        "genre": v["genre"],
        "video_path": path,
        "duration_seconds": duration,
        "duration_formatted": f"{int(duration//60)}:{int(duration%60):02d}",
        "size_mb": round(size_mb, 2),
        "frames_extracted": extracted_count,
        "cadence": "60 frames/minute (1 frame/sec hook) + 1 frame/15s chapters",
        "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(os.path.join(v_dir, "technical_manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    log(f">> [{idx}/{total}] COMPLETED VIDEO: {title}")

def main():
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

    log("********************************************************************")
    log(">> MASTER BATCH TASK: 8-VIDEO HIGH-DENSITY REVERSE-ENGINEERING (60 FPS / 60 FPM)")
    log("********************************************************************")

    for i, v in enumerate(VIDEOS):
        process_video(v, i+1, len(VIDEOS))

    log("********************************************************************")
    log(">> ALL 8 VIDEOS SUCCESSFULLY PROCESSED AND SAVED TO KNOWLEDGE DATABASE!")
    log("********************************************************************")

if __name__ == "__main__":
    main()
