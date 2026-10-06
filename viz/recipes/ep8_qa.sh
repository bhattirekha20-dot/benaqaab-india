#!/usr/bin/env bash
# Ep8 QA on the ENCODED file: streams, loudness/true peak, loop seam, contact sheet of transitions + beats.
set -u
cd /home/user/projects/ep8_oct_rules
V=ep8_oct_rules.mp4
ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,pix_fmt,duration,sample_rate,channels -show_entries format=duration,size -of compact $V
echo "--- loudness"
ffmpeg -hide_banner -nostats -i $V -af ebur128=peak=true -f null - 2>&1 | sed -n '/Summary/,$p' | grep -E "I:|LRA:|Peak:"
echo "--- loop seam"
N=$(ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of csv=p=0 $V)
ffmpeg -v error -y -i $V -vf "select='eq(n\,0)+eq(n\,$((N-1)))'" -vsync 0 /tmp/ep8_seam_%d.png
python3 -c "
from PIL import Image; import numpy as np
a=np.asarray(Image.open('/tmp/ep8_seam_1.png')).astype(float); b=np.asarray(Image.open('/tmp/ep8_seam_2.png')).astype(float)
d=np.abs(a-b); print('frames $N | frame0 vs last: mean abs diff %.2f/255, pixels>8: %.2f%%' % (d.mean(), 100*(d.max(2)>8).mean()))"
mkdir -p work/qa && rm -f work/qa/*.png
for t in 0 3.6 7.35 7.45 10.8 16.2 19.6 21.55 29.0 34.9 36.05 36.2 38.6 42.9 47.5 50.5 57.9 62.2 65.8 67.0 67.15 69.6 72.5 74.2; do
  ffmpeg -v error -ss $t -i $V -frames:v 1 work/qa/f_$(printf %06.2f $t).png
done
python3 - <<'EOF'
import sys, glob; sys.path.insert(0, '/home/user/viz')
import motion as M
from PIL import Image
fs = sorted(glob.glob('/home/user/projects/ep8_oct_rules/work/qa/f_*.png'))
ims = [Image.open(f) for f in fs]; labels = [f.split('f_')[1][:-4].lstrip('0') + 's' for f in fs]
M.contact_sheet(ims, labels, cols=6).save('/home/user/projects/ep8_oct_rules/QA_contact.jpg', quality=88)
print('QA_contact.jpg <-', len(ims), 'encoded frames')
EOF
