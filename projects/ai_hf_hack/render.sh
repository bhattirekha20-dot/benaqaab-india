#!/bin/bash
# render.sh — one command on YOUR PC: frames -> FINAL.mp4 (with VO audio)
# Needs: python3 + playwright  (pip install playwright && playwright install chromium)
#         ffmpeg  (apt install ffmpeg / winget install ffmpeg)
set -e
cd "$(dirname "$0")"

echo "[1/3] rendering frames (resumable — re-run if interrupted)..."
python3 render.py frames

echo "[2/3] building master audio..."
bash make_audio.sh

echo "[3/3] encoding FINAL.mp4 (1080p30 + VO)..."
TOTAL=$(python3 -c "import json;print(json.load(open('timeline.json'))['total'])")
DUR=$(python3 -c "import math;print(math.ceil($TOTAL*30/30))")
ffmpeg -y -framerate 30 -i frames/f_%06d.png -i audio_master.mp3 \
  -map 0:v -map 1:a -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p \
  -c:a aac -b:a 192k -movflags +faststart -shortest \
  "AI_hacked_HuggingFace_FINAL.mp4"

echo "=================================================="
ls -la AI_hacked_HuggingFace_FINAL.mp4
echo "DONE — upload-ready file: AI_hacked_HuggingFace_FINAL.mp4"
