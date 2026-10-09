import os
import sys
import time
import json
import base64
import io
import subprocess
import multiprocessing as mp
from PIL import Image
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Chromium GPU flags for Windows Intel Iris Xe
CHROME_GPU_ARGS = [
    '--no-sandbox',
    '--enable-gpu-rasterization',
    '--enable-zero-copy',
    '--ignore-gpu-blocklist',
    '--use-gl=angle',
    '--use-angle=d3d11',
    '--hide-scrollbars',
    '--force-color-profile=srgb',
    '--allow-file-access-from-files',
    '--mute-audio',
    '--disable-background-timer-throttling',
    '--disable-renderer-backgrounding'
]

def render_chunk(chunk_id, html_path, start_frame, end_frame, fps, width, height, out_chunk_path, progress_dict):
    from playwright.sync_api import sync_playwright
    
    total_chunk_frames = end_frame - start_frame
    print(f"[Worker {chunk_id}] Starting chunk {start_frame} -> {end_frame} ({total_chunk_frames} frames)...")
    
    # Try QSV hardware encoder first, fallback to libx264
    ffmpeg_cmd = [
        'ffmpeg', '-y', '-v', 'error',
        '-f', 'rawvideo', '-pix_fmt', 'rgb24',
        '-s', f'{width}x{height}', '-r', str(fps),
        '-i', '-',
        '-c:v', 'h264_qsv', '-preset', 'veryfast', '-b:v', '14M',
        '-pix_fmt', 'nv12',
        out_chunk_path
    ]
    
    test_proc = subprocess.run(['ffmpeg', '-y', '-f', 'lavfi', '-i', 'testsrc=size=64x64:rate=30', '-t', '0.1', '-c:v', 'h264_qsv', 'test_dummy.mp4'], capture_output=True)
    if test_proc.returncode != 0:
        print(f"[Worker {chunk_id}] QSV not active, using multi-threaded libx264...")
        ffmpeg_cmd = [
            'ffmpeg', '-y', '-v', 'error',
            '-f', 'rawvideo', '-pix_fmt', 'rgb24',
            '-s', f'{width}x{height}', '-r', str(fps),
            '-i', '-',
            '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18',
            '-pix_fmt', 'yuv420p',
            out_chunk_path
        ]
        
    ffmpeg_proc = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
    
    with sync_playwright() as pw:
        browser = pw.chromium.launch(args=CHROME_GPU_ARGS)
        page = browser.new_page(viewport={'width': width, 'height': height}, device_scale_factor=1)
        page.goto('file:///' + os.path.abspath(html_path).replace('\\', '/') + '?render=1')
        page.add_style_tag(content='header, .controls-bar { display: none !important; } body, html, .stage-container, .canvas-wrapper { margin: 0 !important; padding: 0 !important; max-width: none !important; width: 1920px !important; height: 1080px !important; border-radius: 0 !important; box-shadow: none !important; overflow: hidden !important; background: #000 !important; } canvas { position: fixed !important; top: 0 !important; left: 0 !important; width: 1920px !important; height: 1080px !important; display: block !important; }')
        page.wait_for_timeout(2500) # Ensure images loaded
        
        cdp = page.context.new_cdp_session(page)
        shot_opts = {'format': 'jpeg', 'quality': 95, 'captureBeyondViewport': False}
        
        t0 = time.time()
        for idx, frame_no in enumerate(range(start_frame, end_frame)):
            t_sec = frame_no / fps
            page.evaluate(f'window.seek({t_sec})')
            
            # CDP screenshot for ultra-low latency capture
            res = cdp.send('Page.captureScreenshot', shot_opts)
            img_bytes = base64.b64decode(res['data'])
            img = Image.open(io.BytesIO(img_bytes)).convert('RGB')
            ffmpeg_proc.stdin.write(np.asarray(img).tobytes())
            
            # Update progress
            done = idx + 1
            progress_dict[chunk_id] = done
            
            if done % 50 == 0 or done == total_chunk_frames:
                el = time.time() - t0
                speed = done / el if el > 0 else 0
                print(f"[Worker {chunk_id}] {done}/{total_chunk_frames} frames ({done*100/total_chunk_frames:.1f}%) | {speed:.1f} fps")
                
        ffmpeg_proc.stdin.close()
        ffmpeg_proc.wait()
        browser.close()
        
    print(f"[Worker {chunk_id}] Finished chunk -> {out_chunk_path}")

def main():
    html_file = 'projects/ep18_gaganyaan_2026/comp.html'
    audio_file = 'projects/ep18_gaganyaan_2026/master_audio.mp3'
    final_output = 'projects/ep18_gaganyaan_2026/ep18_gaganyaan_2026_master.mp4'
    status_file = 'projects/ep18_gaganyaan_2026/render_status.json'
    
    fps = 30
    total_dur = 308.56
    total_frames = int(round(total_dur * fps))
    width = 1920
    height = 1080
    
    num_workers = 4 # Optimized for 10-core i7-1355U & Iris Xe
    frames_per_worker = total_frames // num_workers
    
    chunks = []
    chunk_paths = []
    for w in range(num_workers):
        sf = w * frames_per_worker
        ef = (w + 1) * frames_per_worker if w < num_workers - 1 else total_frames
        chunk_path = f'projects/ep18_gaganyaan_2026/chunk_{w}.mp4'
        chunks.append((w, sf, ef, chunk_path))
        chunk_paths.append(chunk_path)
        
    print(f"=== BENAQAAB INDIA HIGH-PERFORMANCE RENDER ENGINE ===")
    print(f"Total Duration: {total_dur:.2f}s | FPS: {fps} | Total Frames: {total_frames}")
    print(f"Workers: {num_workers} parallel GPU/CPU threads | Resolution: {width}x{height}")
    
    manager = mp.Manager()
    progress_dict = manager.dict({w: 0 for w in range(num_workers)})
    
    processes = []
    start_time = time.time()
    
    for w, sf, ef, cp in chunks:
        p = mp.Process(target=render_chunk, args=(w, html_file, sf, ef, fps, width, height, cp, progress_dict))
        p.start()
        processes.append(p)
        
    # Monitor loop
    while any(p.is_alive() for p in processes):
        time.sleep(2)
        total_done = sum(progress_dict.values())
        elapsed = time.time() - start_time
        overall_pct = (total_done / total_frames) * 100
        overall_fps = total_done / elapsed if elapsed > 0 else 0
        rem_frames = total_frames - total_done
        eta_sec = rem_frames / overall_fps if overall_fps > 0 else 0
        
        status_data = {
            "status": "rendering",
            "total_frames": total_frames,
            "rendered_frames": total_done,
            "percent_complete": round(overall_pct, 1),
            "fps": round(overall_fps, 1),
            "elapsed_seconds": round(elapsed, 1),
            "eta_seconds": round(eta_sec, 1),
            "eta_formatted": f"{int(eta_sec//60)}m {int(eta_sec%60)}s",
            "workers": {f"worker_{k}": v for k, v in dict(progress_dict).items()}
        }
        with open(status_file, 'w') as sf_out:
            json.dump(status_data, sf_out, indent=2)
            
        print(f"[LIVE PROGRESS] {total_done}/{total_frames} frames ({overall_pct:.1f}%) | {overall_fps:.1f} fps | ETA: {int(eta_sec//60)}m {int(eta_sec%60)}s")
        
    for p in processes:
        p.join()
        
    print("\nAll 4 chunks rendered successfully! Merging chunks with master audio...")
    
    # Create concat list
    concat_txt = 'projects/ep18_gaganyaan_2026/chunks_list.txt'
    with open(concat_txt, 'w') as f:
        for cp in chunk_paths:
            f.write(f"file '{os.path.abspath(cp).replace(os.sep, '/')}'\n")
            
    # Concat and mux audio
    concat_cmd = [
        'ffmpeg', '-y',
        '-f', 'concat', '-safe', '0', '-i', concat_txt,
        '-i', audio_file,
        '-c:v', 'copy',
        '-c:a', 'aac', '-b:a', '192k', '-ar', '48000',
        '-shortest',
        final_output
    ]
    res = subprocess.run(concat_cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print("Concat error:", res.stderr)
        sys.exit(1)
        
    # Cleanup chunk files
    for cp in chunk_paths:
        if os.path.exists(cp):
            os.remove(cp)
    if os.path.exists(concat_txt):
        os.remove(concat_txt)
        
    total_time = time.time() - start_time
    file_size_mb = os.path.getsize(final_output) / (1024 * 1024)
    
    final_status = {
        "status": "completed",
        "output_file": final_output,
        "file_size_mb": round(file_size_mb, 1),
        "total_frames": total_frames,
        "total_render_time_sec": round(total_time, 1),
        "total_render_time_formatted": f"{int(total_time//60)}m {int(total_time%60)}s"
    }
    with open(status_file, 'w') as sf_out:
        json.dump(final_status, sf_out, indent=2)
        
    print(f"\n=======================================================")
    print(f"[SUCCESS] MASTER VIDEO RENDER COMPLETE!")
    print(f"Output: {final_output}")
    print(f"Size: {file_size_mb:.1f} MB")
    print(f"Total Time: {int(total_time//60)}m {int(total_time%60)}s")
    print(f"=======================================================")

if __name__ == '__main__':
    main()
