import time
import json
import os
import sys

status_file = 'projects/ep18_gaganyaan_2026/render_status.json'
print("=== LIVE BENAQAAB INDIA RENDER TELEMETRY ACTIVE ===", flush=True)

while True:
    try:
        if os.path.exists(status_file):
            with open(status_file, 'r') as f:
                d = json.load(f)
            
            if d.get('status') == 'completed':
                print(f"\n[DONE] 🎉 100% COMPLETE! Master file: {d.get('output_file')} ({d.get('file_size_mb')} MB) in {d.get('total_render_time_formatted')}", flush=True)
                break
            elif d.get('status') == 'rendering':
                pct = d.get('percent_complete', 0)
                done = d.get('rendered_frames', 0)
                tot = d.get('total_frames', 9257)
                fps = d.get('fps', 0)
                eta = d.get('eta_formatted', '...')
                el = int(d.get('elapsed_seconds', 0))
                
                # Visual ASCII progress bar
                bar_len = 25
                filled = int(round(bar_len * (pct / 100.0)))
                bar_str = '█' * filled + '░' * (bar_len - filled)
                
                w_str = " | ".join([f"{k}: {v}" for k, v in d.get('workers', {}).items()])
                sys.stdout.write(f"\r[{bar_str}] {pct:5.1f}% | {done}/{tot} frames | {fps:4.1f} FPS | Elapsed: {el}s | ETA: {eta} | [{w_str}]\n")
                sys.stdout.flush()
    except Exception as e:
        pass
    time.sleep(3)
