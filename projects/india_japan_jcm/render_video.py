from pathlib import Path
import sys, subprocess
sys.path.insert(0, '/home/user/ffmpeg_runtime')
import imageio_ffmpeg

ROOT = Path('/home/user/india_japan_jcm_short')
FF = imageio_ffmpeg.get_ffmpeg_exe()

# Audio durations read from ffmpeg: 75.14s + 32.02s.
total = 75.14 + 32.02
fractions = [0, .10, .23, .39, .56, .76, 1]
durations = [(fractions[i+1] - fractions[i]) * total for i in range(6)]

# The static rendered frames are generated with PIL so this works with the
# compact FFmpeg build used in the workspace, which has no drawtext filter.
frames = [ROOT / f'render_frame_{i:02d}.jpg' for i in range(1, 7)]
if not all(p.exists() for p in frames):
    subprocess.run([sys.executable, str(ROOT/'build_frames.py')], check=True)

inputs = []
filter_parts = []
for i, (frame, dur) in enumerate(zip(frames, durations)):
    inputs += ['-loop', '1', '-framerate', '30', '-t', f'{dur:.3f}', '-i', str(frame)]
    filter_parts.append(f'[{i}:v]scale=1080:1920:flags=lanczos,setsar=1,format=yuv420p,setpts=PTS-STARTPTS[v{i}]')
filter_parts.append(''.join(f'[v{i}]' for i in range(6)) + 'concat=n=6:v=1:a=0,format=yuv420p[v]')
filter_parts.append('[6:a][7:a]concat=n=2:v=0:a=1,aresample=48000[a]')
filter_complex = ';'.join(filter_parts)

out = ROOT / 'india_japan_jcm_short_final.mp4'
cmd = [FF, '-y'] + inputs + ['-i', str(ROOT/'narration_01.mp3'), '-i', str(ROOT/'narration_02.mp3'), '-filter_complex', filter_complex, '-map', '[v]', '-map', '[a]', '-c:v', 'libx264', '-preset', 'medium', '-crf', '19', '-profile:v', 'high', '-level', '4.1', '-pix_fmt', 'yuv420p', '-r', '30', '-c:a', 'aac', '-b:a', '128k', '-ar', '48000', '-ac', '2', '-movflags', '+faststart', '-shortest', str(out)]
print('Rendering', out)
subprocess.run(cmd, check=True)
print('Done:', out, out.stat().st_size)
print('Scene durations:', ', '.join(f'{d:.3f}s' for d in durations), 'total', total)
