import os
import sys
import time
import base64
import subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from playwright.sync_api import sync_playwright

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

PROJECT_DIR = Path(__file__).parent.resolve()
HTML_PATH = PROJECT_DIR / "comp.html"
AUDIO_PATH = PROJECT_DIR / "master_audio.mp3"
OUTPUT_MP4 = PROJECT_DIR / "SH12_Master_Render.mp4"
THUMB_9X16 = PROJECT_DIR / "SH12_Thumbnail_9x16.jpg"
THUMB_16X9 = PROJECT_DIR / "SH12_Thumbnail_16x9.jpg"
FFMPEG_LOG = PROJECT_DIR / "ffmpeg_render.log"

TOTAL_DURATION = 47.304
FPS = 30
TOTAL_FRAMES = int(round(TOTAL_DURATION * FPS)) # 1419 frames
WIDTH = 1080
HEIGHT = 1920

def render_and_package():
    print("=" * 75)
    print("🎬 BENAQAAB INDIA — BROADCAST MASTER VIDEO & THUMBNAIL PIPELINE")
    print(f"📁 Project: SH-12 (Delhi Lockdown & The CJP Protest)")
    print(f"⏱️ Duration: {TOTAL_DURATION}s ({TOTAL_FRAMES} frames @ {FPS} FPS)")
    print(f"📐 Canvas: {WIDTH}x{HEIGHT} (9:16 Vertical Short)")
    print(f"⚡ Encoding: YouTube-Compliant H.264 (yuv420p) + AAC 320k + moov faststart")
    print("=" * 75)

    url = 'file:///' + str(HTML_PATH).replace('\\', '/') + '?render=1'
    print(f"🌐 Launching Headless Chromium with GPU Acceleration: {url}")

    log_file = open(FFMPEG_LOG, 'w')

    with sync_playwright() as p:
        browser = p.chromium.launch(args=[
            '--enable-gpu-rasterization',
            '--enable-zero-copy',
            '--ignore-gpu-blocklist',
            '--allow-file-access-from-files',
            '--force-color-profile=srgb',
            '--hide-scrollbars',
            '--no-sandbox'
        ])

        page = browser.new_page(
            viewport={'width': WIDTH, 'height': HEIGHT},
            device_scale_factor=1
        )
        page.goto(url)

        print("⏳ Waiting for composition ready state (window.ready)...")
        page.wait_for_function('window.ready === true', timeout=60000)
        print("✅ Composition ready signal received!")

        cdp = page.context.new_cdp_session(page)

        # Pre-render sanity check
        page.evaluate('window.seek(0)')
        test_shot = cdp.send('Page.captureScreenshot', {'format': 'jpeg', 'quality': 95})
        print(f"✅ Verified frame 0 snapshot ({len(base64.b64decode(test_shot['data']))} bytes).")

        # YouTube-Compliant Standard FFmpeg Command
        ffmpeg_cmd = [
            'ffmpeg', '-y',
            '-f', 'image2pipe',
            '-vcodec', 'mjpeg',
            '-r', str(FPS),
            '-i', '-',
            '-i', str(AUDIO_PATH),
            '-c:v', 'libx264',
            '-preset', 'veryfast',
            '-crf', '18',
            '-threads', '0',
            '-pix_fmt', 'yuv420p',
            '-colorspace', 'bt709',
            '-color_primaries', 'bt709',
            '-color_trc', 'bt709',
            '-c:a', 'aac',
            '-b:a', '320k',
            '-ar', '48000',
            '-movflags', '+faststart',
            '-shortest',
            str(OUTPUT_MP4)
        ]

        print(f"🎛️ Launching FFmpeg encoder process...")
        proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE, stderr=log_file)

        t_start = time.time()
        print(f"🚀 Streaming {TOTAL_FRAMES} frames into FFmpeg pipe...")

        for i in range(TOTAL_FRAMES):
            t_sec = i / float(FPS)
            page.evaluate(f'window.seek({t_sec})')

            res = cdp.send('Page.captureScreenshot', {'format': 'jpeg', 'quality': 95})
            raw_bytes = base64.b64decode(res['data'])

            try:
                proc.stdin.write(raw_bytes)
            except BrokenPipeError:
                log_file.close()
                err = open(FFMPEG_LOG, 'r', encoding='utf-8', errors='replace').read()[-1000:]
                print(f"❌ FFmpeg pipe broken at frame {i}:\n{err}")
                sys.exit(1)

            if (i + 1) % 150 == 0 or (i + 1) == TOTAL_FRAMES:
                elapsed = time.time() - t_start
                fps_render = (i + 1) / elapsed
                remaining = (TOTAL_FRAMES - (i + 1)) / fps_render if fps_render > 0 else 0
                pct = ((i + 1) / TOTAL_FRAMES) * 100.0
                print(f"  ⚡ [{i+1:4d}/{TOTAL_FRAMES}] {pct:5.1f}% | {fps_render:4.1f} FPS | Elapsed: {elapsed:4.1f}s | ETA: {remaining:4.1f}s")

        proc.stdin.close()
        print("⏳ Finalizing MP4 muxing with moov faststart atom...")
        proc.wait()
        log_file.close()

        if proc.returncode != 0:
            err = open(FFMPEG_LOG, 'r', encoding='utf-8', errors='replace').read()[-1000:]
            print(f"❌ FFmpeg failed with exit code {proc.returncode}:\n{err}")
            sys.exit(proc.returncode)

        # Generate High-CTR Thumbnails directly from the composition
        print("🎨 Generating YouTube Thumbnails...")
        # Seek to Beat 1 peak frame (t = 1.0s)
        page.evaluate('window.seek(1.0)')
        thumb_res = cdp.send('Page.captureScreenshot', {'format': 'jpeg', 'quality': 98})
        with open(THUMB_9X16, 'wb') as f:
            f.write(base64.b64decode(thumb_res['data']))
        print(f"✅ 9:16 Vertical Thumbnail saved to: {THUMB_9X16}")

        # Also create 16:9 Landscape Thumbnail (1280x720) for standard search/browse feeds
        img_9x16 = Image.open(THUMB_9X16)
        w, h = img_9x16.size
        # Crop centered vertical band and paste on blurred background
        bg_blur = img_9x16.resize((1280, 720)).filter(ImageFilter.GaussianBlur(18))
        target_h = 720
        target_w = int(w * (target_h / h))
        hero_cropped = img_9x16.resize((target_w, target_h), Image.Resampling.LANCZOS)
        bg_blur.paste(hero_cropped, ((1280 - target_w) // 2, 0))
        bg_blur.save(THUMB_16X9, quality=95)
        print(f"✅ 16:9 Landscape Thumbnail saved to: {THUMB_16X9}")

        browser.close()

    total_time = time.time() - t_start
    file_size_mb = os.path.getsize(OUTPUT_MP4) / (1024 * 1024)
    print("=" * 75)
    print(f"🎉 MASTER MP4 RENDER & THUMBNAIL PACKAGING COMPLETE!")
    print(f"📁 Master Video: {OUTPUT_MP4} ({file_size_mb:.2f} MB)")
    print(f"🖼️ 9:16 Thumbnail: {THUMB_9X16}")
    print(f"🖼️ 16:9 Thumbnail: {THUMB_16X9}")
    print(f"⏱️ Total Render Time: {total_time:.1f}s ({TOTAL_FRAMES / total_time:.1f} avg FPS)")
    print("=" * 75)

    # Verification via ffprobe
    probe = subprocess.run([
        'ffprobe', '-v', 'error',
        '-show_entries', 'format=duration,size,bit_rate:stream=width,height,codec_name,pix_fmt,r_frame_rate',
        '-of', 'json',
        str(OUTPUT_MP4)
    ], capture_output=True, text=True)

    print("📊 FFprobe Verification Data:")
    print(probe.stdout)

if __name__ == '__main__':
    render_and_package()
