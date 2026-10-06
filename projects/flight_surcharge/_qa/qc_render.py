#!/usr/bin/env python3
"""Post-render QC for the flight-surcharge film: container, motion gates, loudness, decode."""
import json, subprocess, sys, os
sys.path.insert(0, os.path.abspath('../../viz'))
import numpy as np
from PIL import Image
import motion as M

MP4 = 'Flight_Surcharge_Short.mp4'
out = {}

def sh(cmd):
    return subprocess.run(cmd, capture_output=True, text=True).stdout

# 1 · container
probe = json.loads(sh(['ffprobe', '-v', 'error', '-print_format', 'json', '-show_format',
                       '-show_streams', MP4]))
v = next(s for s in probe['streams'] if s['codec_type'] == 'video')
a = next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)
out['container'] = {
    'duration': float(probe['format']['duration']), 'size_mb': round(int(probe['format']['size'])/1e6, 2),
    'video': f"{v['codec_name']} {v['width']}x{v['height']} {v['pix_fmt']} {v['r_frame_rate']}",
    'audio': f"{a['codec_name']} {a['sample_rate']}Hz {a['channels']}ch" if a else 'none',
}

# 2 · motion gates (freezes / pops / still ratio)
out['motion_report'] = M.motion_report(MP4)

# 3 · loudness on the MUXED file
eb = subprocess.run(['ffmpeg', '-nostats', '-i', MP4, '-filter:a', 'ebur128=peak=true', '-f', 'null', '-'],
                    capture_output=True, text=True).stderr
tail = eb[eb.rfind('Summary'):]
def grab(label):
    for ln in tail.splitlines():
        if label in ln:
            return ln.split(':')[-1].strip()
out['loudness'] = {'I': grab('I:'), 'LRA': grab('LRA:'), 'true_peak': grab('Peak:')}

# 4 · decode + frame count
dec = subprocess.run(['ffmpeg', '-v', 'error', '-i', MP4, '-f', 'null', '-'],
                     capture_output=True, text=True)
out['decode_errors'] = dec.stderr.strip() or 'none'
out['frame_count'] = int(sh(['ffprobe', '-v', 'error', '-count_frames', '-select_streams', 'v:0',
                             '-show_entries', 'stream=nb_read_frames', '-of', 'csv=p=0', MP4]).strip())

# 5 · rendered frames vs the composition stills (informational — the render adds motion blur)
def frame_at(t):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', f'{t:.3f}', '-i', MP4, '-frames:v', '1',
                          '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-'], capture_output=True).stdout
    return np.frombuffer(raw, 'u1').reshape(1920, 1080, 3).astype(np.int16)
diffs = {}
for t in (5.0, 66.0, 145.0):
    ref = np.asarray(Image.open(f'_qa/stills/still_{t:07.3f}.png').convert('RGB'), dtype=np.int16)
    got = frame_at(t + 0.5 / 30)
    diffs[t] = round(float(np.abs(ref - got).mean()), 2)
out['still_vs_render_mean_abs_diff'] = diffs

print(json.dumps(out, indent=2))
json.dump(out, open('_qa/QC_render.json', 'w'), indent=2)
