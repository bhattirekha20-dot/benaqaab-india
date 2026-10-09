import os
import sys
import time
import base64
import subprocess
from pathlib import Path
from playwright.sync_api import sync_playwright

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR = Path(__file__).resolve().parent
WORKSPACE_ROOT = DIR.parent.parent
COMP_HTML = DIR / "comp.html"
AUDIO_MP3 = DIR / "master_audio.mp3"
PART_MP4 = DIR / "ep18_gaganyaan_promo_short_master.mp4.part"
FINAL_MP4 = DIR / "ep18_gaganyaan_promo_short_master.mp4"
VIDEOS_DIR = WORKSPACE_ROOT / "VIDEOS"
VIDEOS_MP4 = VIDEOS_DIR / "EP18_Gaganyaan_Promo_Short_11Oct_4AM.mp4"

def render():
    print("🎬 [Benaqaab Video Engine] Initiating 9:16 Master Render for YouTube Promo Short...")
    if not COMP_HTML.exists():
        raise FileNotFoundError(f"Missing composition HTML: {COMP_HTML}")
    if not AUDIO_MP3.exists():
        raise FileNotFoundError(f"Missing master audio: {AUDIO_MP3}")

    VIDEOS_DIR.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        print("🌐 Launching Headless Chromium (1080x1920)...")
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
        
        # Enforce pure canvas render isolation (RULE-PURE-CANVAS-RENDER-ONLY)
        page.add_style_tag(content='''
            header, .controls-bar, .top-bar, .player-deck { display: none !important; }
            body, html, .stage-container, .app-container {
                margin: 0 !important; padding: 0 !important; width: 1080px !important; height: 1920px !important;
                background: #000 !important; border: none !important; border-radius: 0 !important; box-shadow: none !important;
            }
            canvas#shortCanvas, canvas#videoCanvas, canvas {
                position: fixed !important; top: 0 !important; left: 0 !important;
                width: 1080px !important; height: 1920px !important; display: block !important;
            }
        ''')

        time.sleep(1.0)

        duration = float(page.evaluate('window.DURATION || 49.44'))
        fps = int(page.evaluate('window.FPS || 30'))
        total_frames = int(duration * fps)
        print(f"✅ Composition Ready: Duration = {duration:.2f}s | FPS = {fps} | Total Frames = {total_frames}")

        cdp = page.context.new_cdp_session(page)
        shot_config = {'format': 'jpeg', 'quality': 95}

        # Setup FFmpeg image2pipe process
        ffmpeg_cmd = [
            'ffmpeg', '-y',
            '-f', 'image2pipe',
            '-vcodec', 'mjpeg',
            '-r', str(fps),
            '-i', 'pipe:0',
            '-i', str(AUDIO_MP3),
            '-c:v', 'libx264',
            '-preset', 'veryfast',
            '-crf', '17',
            '-pix_fmt', 'yuv420p',
            '-c:a', 'aac',
            '-b:a', '320k',
            '-af', 'loudnorm=I=-14:TP=-1.0:LRA=7',
            '-shortest',
            '-f', 'mp4',
            str(PART_MP4)
        ]

        log_path = DIR / "ffmpeg_render.log"
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

                if frame_idx > 0 and frame_idx % 150 == 0:
                    elapsed = time.time() - t_start
                    fps_render = frame_idx / elapsed
                    eta = (total_frames - frame_idx) / (fps_render + 1e-5)
                    pct = (frame_idx / total_frames) * 100
                    print(f"  Frame {frame_idx}/{total_frames} ({pct:.1f}%) | Speed: {fps_render:.1f} FPS | ETA: {eta:.0f}s")

            proc.stdin.close()
            proc.wait()
            log_file.close()

            if proc.returncode != 0:
                print("❌ FFmpeg exited with error. Check ffmpeg_render.log")
                return False

            if PART_MP4.exists():
                if FINAL_MP4.exists():
                    FINAL_MP4.unlink()
                PART_MP4.rename(FINAL_MP4)
                
                # Also copy to VIDEOS folder
                import shutil
                shutil.copy2(FINAL_MP4, VIDEOS_MP4)
                
                total_time = time.time() - t_start
                size_mb = FINAL_MP4.stat().st_size / (1024 * 1024)
                print(f"🎉 Render Complete! Output: {FINAL_MP4.name} ({size_mb:.1f} MB in {total_time:.1f}s)")
                print(f"📦 Master Short archived to: {VIDEOS_MP4}")
                return True

        except Exception as e:
            print(f"❌ Error during rendering: {e}")
            if proc.stdin:
                proc.stdin.close()
            proc.kill()
            log_file.close()
            return False

if __name__ == '__main__':
    render()
