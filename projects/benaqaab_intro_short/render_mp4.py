#!/usr/bin/env python3
"""
render_mp4.py — Deterministic headless video rendering engine for Benaqaab India
Project: Official Channel Intro Promo Short (10s)
Pipeline: Playwright Headless Chromium -> CDP captureScreenshot -> FFmpeg image2pipe muxed with Master Audio.
"""

import sys
import time
import base64
import subprocess
from pathlib import Path

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
AUDIO_MP3 = ROOT / "master_audio.mp3"
PART_MP4 = ROOT / "Benaqaab_Intro_Short.mp4.part"
FINAL_MP4 = ROOT / "Benaqaab_Intro_Short.mp4"
VIDEOS_MP4 = WORKSPACE_ROOT / "VIDEOS" / "Benaqaab_Channel_Intro_SHORT_10s.mp4"

def render():
    print(f"🎬 [Benaqaab Video Engine] Initiating render for {ROOT.name}...")
    if not COMP_HTML.exists():
        raise FileNotFoundError(f"Missing composition HTML: {COMP_HTML}")
    if not AUDIO_MP3.exists():
        raise FileNotFoundError(f"Missing master audio: {AUDIO_MP3}")

    VIDEOS_MP4.parent.mkdir(parents=True, exist_ok=True)

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
        
        duration = float(page.evaluate('window.DURATION || 10.0'))
        fps = int(page.evaluate('window.FPS || 30'))
        total_frames = int(duration * fps)
        print(f"✅ Composition Ready: Duration = {duration:.2f}s | FPS = {fps} | Total Frames = {total_frames}")

        cdp = page.context.new_cdp_session(page)
        shot_config = {'format': 'jpeg', 'quality': 92}

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
            '-crf', '18',
            '-pix_fmt', 'yuv420p',
            '-c:a', 'aac',
            '-b:a', '256k',
            '-af', 'loudnorm=I=-14:TP=-1.0:LRA=7',
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

                if frame_idx % 30 == 0 or frame_idx == total_frames - 1:
                    pct = (frame_idx + 1) / total_frames * 100
                    elapsed = time.time() - t_start
                    fps_render = (frame_idx + 1) / (elapsed + 1e-5)
                    print(f"  Frame {frame_idx + 1}/{total_frames} ({pct:.1f}%) | {fps_render:.1f} fps")

            proc.stdin.close()
            proc.wait()
            log_file.close()

            if proc.returncode != 0:
                raise RuntimeError(f"FFmpeg failed with exit code {proc.returncode}. See {log_path}")

            # Atomic rename
            if PART_MP4.exists():
                if FINAL_MP4.exists():
                    FINAL_MP4.unlink()
                PART_MP4.rename(FINAL_MP4)
                print(f"🎉 Master Render Complete: {FINAL_MP4} ({FINAL_MP4.stat().st_size / (1024*1024):.2f} MB)")
                
                # Copy to workspace VIDEOS folder
                import shutil
                shutil.copy2(FINAL_MP4, VIDEOS_MP4)
                print(f"📦 Broadcast Deliverable mirrored: {VIDEOS_MP4}")

        except Exception as e:
            proc.kill()
            log_file.close()
            raise e
        finally:
            browser.close()

if __name__ == "__main__":
    render()
