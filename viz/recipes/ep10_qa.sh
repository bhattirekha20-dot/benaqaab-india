#!/usr/bin/env bash
# Ep10 QA on the ENCODED file: streams, loudness/true peak, loop seam, A/V sync of the MEA insert, contact sheet.
set -u
cd /home/user/projects/ep10_24hrs
V=/home/user/EP10_India_24_Hours.mp4; Q=/home/user/.cache/ep10/qa
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,duration,sample_rate,channels -show_entries format=duration,size -of compact $V
echo "--- loudness"
ffmpeg -hide_banner -nostats -i $V -af ebur128=peak=true -f null - 2>&1 | sed -n '/Summary/,$p' | grep -E "I:|LRA:|Peak:"
echo "--- loop seam"
N=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 $V)
ffmpeg -v error -y -i $V -vf "select='eq(n\,0)+eq(n\,$((N-1)))'" -vsync 0 /tmp/ep10_seam_%d.png
python3 -c "
from PIL import Image; import numpy as np
a=np.asarray(Image.open('/tmp/ep10_seam_1.png')).astype(float); b=np.asarray(Image.open('/tmp/ep10_seam_2.png')).astype(float)
d=np.abs(a-b); print('frames $N | frame0 vs last: mean abs diff %.2f/255, pixels>8: %.2f%%' % (d.mean(), 100*(d.max(2)>8).mean()))"
mkdir -p $Q && rm -f $Q/*.png
for t in 0 3.2 5.4 9.8 12.8 15.6 20.0 22.3 26.0 31.5 38.4 42.0 50.6 53.5 58.8 62.4 66.5 70.0 73.4 77.0 82.5 88.6 94.0 97.4 101.0 104.3 106.3; do
  ffmpeg -v error -ss $t -i $V -frames:v 1 $Q/f_$(printf %06.2f $t).png
done
python3 - <<'PY'
import sys, glob; sys.path.insert(0, '/home/user/viz')
import motion as M
from PIL import Image
fs = sorted(glob.glob('/home/user/.cache/ep10/qa/f_*.png'))
ims = [Image.open(f) for f in fs]; labels = [f.split('f_')[1][:-4].lstrip('0') + 's' for f in fs]
cs = M.contact_sheet(ims, labels, cols=7); cs.resize((1260, int(1260 * cs.height / cs.width))).save('/home/user/projects/ep10_24hrs/QA_contact.jpg', quality=80)
print('QA_contact.jpg <-', len(ims), 'encoded frames')
PY
