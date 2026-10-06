#!/usr/bin/env python3
"""
render_mp4.py — Deterministic headless video rendering engine for Benaqaab India
Project: Sona ₹1.5 Lakh: The Real Showroom Bill (SH-08)
Pipeline: Playwright Headless Chromium -> CDP captureScreenshot -> FFmpeg image2pipe muxed with Edge Neural Audio.
Atomic render to .mp4.part, loudness normalization (-14 LUFS), stream verification, and rename to .mp4.
"""

import os
import sys
import time
import base64
import subprocess
from pathlib import Path

# Fix Windows console UTF-8 output
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
WORKSPACE_ROOT = ROOT.parent.parent
COMP_HTML = ROOT / "comp.html"
AUDIO_MP3 = ROOT / "narration.mp3"
PART_MP4 = ROOT / "Gold_150k_Short.mp4.part"
FINAL_MP4 = ROOT / "Gold_150k_Short.mp4"
VIDEOS_MP4 = WORKSPACE_ROOT / "VIDEOS" / "09_Sona_150k_Bill_SHORT_54s.mp4"

def render():
    print(f"🎬 [Benaqaab Video Engine] Initiating render for {ROOT.name}...")
    if not COMP_HTML.exists():
        raise FileNotFoundError(f"Missing composition HTML: {COMP_HTML}")
    if not AUDIO_MP3.exists():
        raise FileNotFoundError(f"Missing voiceover audio: {AUDIO_MP3}")

    with sync_playwright() as p:
        print("🌐 Launching Headless Chromium...")
        browser = p.chromium.launch(args=[
            '--no-sandbox',
            '--disable-gpu',
            '--hide-scrollbars',
            '--force-color-profile=srgb',
            '--disable-lcd-text',
            '--mute-audio',
            '--allow-file-access-from-files'
        ])
        page = browser.new_page(viewport={'width': 1080, 'height': 1920}, device_scale_factor=1)
        
        file_url = 'file:///' + str(COMP_HTML.resolve()).replace('\\', '/') + '?render=1'
        print(f"📄 Navigating to: {file_url}")
        page.goto(file_url)
        page.wait_for_function('window.ready === true', timeout=45000)
        
        duration = float(page.evaluate('window.DURATION || 53.9'))
        fps = int(page.evaluate('window.FPS || 30'))
        total_frames = int(duration * fps)
        print(f"✅ Composition Ready: Duration = {duration:.2f}s | FPS = {fps} | Total Frames = {total_frames}")

        cdp = page.context.new_cdp_session(page)
        shot_config = {'format': 'jpeg', 'quality': 90}

        # Setup FFmpeg image2pipe process
        ffmpeg_cmd = [
            'ffmpeg', '-y',
            '-f', 'image2pipe',
            '-vcodec', 'mjpeg',
            '-r', str(fps),
            '-i', 'pipe:0',
            '-i', str(AUDIO_MP3),
            '-c:v', 'libx264',
            '-preset', 'fast',
            '-crf', '19',
            '-pix_fmt', 'yuv420p',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-af', 'loudnorm=I=-14:TP=-2.0:LRA=11',
            '-shortest',
            '-f', 'mp4',
            str(PART_MP4)
        ]

        log_path = ROOT / "ffmpeg_render.log"
        log_file = open(log_path, "w", encoding="utf-8", errors="replace")
        proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=log_file)

        t_start = time.time()
        print(f"⏳ Rendering {total_frames} frames to {PART_MP4.name}...")

        try:
            for frame_idx in range(total_frames):
                t_curr = frame_idx / fps
                page.evaluate(f'window.seek({t_curr:.4f})')
                
                res = cdp.send('Page.captureScreenshot', shot_config)
                frame_bytes = base64.b64decode(res['data'])
                proc.stdin.write(frame_bytes)

                if (frame_idx + 1) % 150 == 0 or (frame_idx + 1) == total_frames:
                    elapsed = time.time() - t_start
                    curr_fps = (frame_idx + 1) / elapsed
                    remaining_frames = total_frames - (frame_idx + 1)
                    eta_sec = remaining_frames / curr_fps if curr_fps > 0 else 0
                    pct = ((frame_idx + 1) / total_frames) * 100
                    print(f"   [{pct:5.1f}%] Frame {frame_idx + 1}/{total_frames} | Speed: {curr_fps:4.1f} fps | ETA: {eta_sec:4.1f}s")
        except Exception as e:
            print(f"❌ Error during frame capture: {e}")
            proc.kill()
            raise
        finally:
            if proc.stdin and not proc.stdin.closed:
                try:
                    proc.stdin.close()
                except Exception:
                    pass
            log_file.close()

        print("🔄 Finalizing FFmpeg encoding...")
        proc.wait()
        if proc.returncode != 0:
            with open(log_path, "r", encoding="utf-8", errors="replace") as f:
                err_tail = f.read()[-2000:]
            print("FFmpeg stderr tail:\n", err_tail)
            raise RuntimeError(f"FFmpeg failed with exit code {proc.returncode}")

        browser.close()

    render_sec = time.time() - t_start
    print(f"✨ Rendering completed in {render_sec:.2f}s ({render_sec/60:.1f} mins)!")

    # Verification with ffprobe
    print(f"🔍 Verifying stream integrity: {PART_MP4}")
    probe_cmd = [
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration,size,bit_rate:stream=codec_name,width,height,r_frame_rate',
        '-of', 'json', str(PART_MP4)
    ]
    probe_res = subprocess.run(probe_cmd, capture_output=True, text=True)
    if probe_res.returncode != 0:
        raise RuntimeError(f"ffprobe verification failed: {probe_res.stderr}")
    print(f"📊 ffprobe metrics:\n{probe_res.stdout.strip()}")

    # Atomic Rename
    if FINAL_MP4.exists():
        FINAL_MP4.unlink()
    PART_MP4.rename(FINAL_MP4)
    print(f"🏆 Output atomically committed to: {FINAL_MP4} (Size: {FINAL_MP4.stat().st_size / (1024*1024):.2f} MB)")

    # Copy to showcase VIDEOS folder
    if VIDEOS_MP4.parent.exists():
        import shutil
        shutil.copy2(FINAL_MP4, VIDEOS_MP4)
        print(f"📁 Copied to public showroom: {VIDEOS_MP4}")

if __name__ == "__main__":
    render()
