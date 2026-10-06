from pathlib import Path
import ast,json,subprocess,wave,math
import numpy as np
from PIL import Image,ImageDraw,ImageFont,ImageOps
import imageio_ffmpeg
from concurrent.futures import ThreadPoolExecutor
R=Path(__file__).parent; O=R/'delivery'; O.mkdir(exist_ok=True); T=R/'render_work';T.mkdir(exist_ok=True)
FF=imageio_ffmpeg.get_ffmpeg_exe(); FPS=24; W,H=1080,1920
font='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
def F(n):return ImageFont.truetype(font,n)
def run(args):
 r=subprocess.run([FF,'-hide_banner','-loglevel','error','-y']+args,capture_output=True,text=True)
 if r.returncode:raise RuntimeError(r.stderr)
def decode(n):
 r=subprocess.run([FF,'-v','error','-i',str(R/f'narration_{n:02}.mp3'),'-f','s16le','-ac','1','-ar','48000','-'],capture_output=True,check=True)
 return np.frombuffer(r.stdout,dtype='<i2').copy()
a,b=decode(1),decode(2); d1=len(a)/48000;d2=len(b)/48000
# Remove the incorrect spoken target, preserving the original selected voice.
x,y=int(42.27*48000),int(43.56*48000)
left,right=b[:x].copy(),b[y:].copy();fade=240
left[-fade:]=(left[-fade:]*np.linspace(1,0,fade)).astype(np.int16);right[:fade]=(right[:fade]*np.linspace(0,1,fade)).astype(np.int16)
audio=np.concatenate([a,left,right,np.zeros(28800,dtype=np.int16)])
with wave.open(str(O/'narration_final.wav'),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(48000);w.writeframes(audio.tobytes())
starts=[0,11.1,16.6,35.4,39.55,50.75,d1,d1+7.2,d1+16.35,d1+19.6,d1+29.0,d1+38.8,d1+42.27,d1+44.47]
frames=[round(t*FPS) for t in starts]+[math.ceil(len(audio)/48000*FPS)]
scenes=next(ast.literal_eval(n.value) for n in ast.parse((R/'build_comp.py').read_text()).body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='scenes' for t in n.targets))
scenes[11]['s']='WI 171 · India 172/2 in 14.4 overs · Target 172'
scenes[12].update(k='SPORTS · THE SCORE',h='172/2 IN 14.4 OVERS',s='India won by 8 wickets · Lucknow',src='BCCI official scorecard · 6 Oct 2026')
def lines(draw,text,font,maxw):
 out=[];line=''
 for w in text.split():
  q=(line+' '+w).strip()
  if draw.textlength(q,font=font)>maxw and line:out.append(line);line=w
  else:line=q
 if line:out.append(line)
 return out
def block(d,text,x,y,size,width,color,space=8):
 for l in lines(d,text,F(size),width):
  d.text((x,y),l,font=F(size),fill=color,stroke_width=1,stroke_fill=(0,0,0,130));y+=size+space
 return y
for i,s in enumerate(scenes,1):
 im=Image.new('RGBA',(W,H));d=ImageDraw.Draw(im)
 # Modest copy sits below the enlarged source images.
 d.rectangle((70,1437,104,1443),fill='#10bfe8');d.text((120,1416),s['k'],font=F(26),fill='#ffd35b')
 y=block(d,s['h'],70,1470,54,940,'white',5)
 y=block(d,s['s'],70,y+18,30,940,'#e3faff',7)
 y=max(1740,y+20)
 d.rectangle((70,y,75,y+55),fill='#f0ad24')
 block(d,s['src'],90,y+3,21,910,'white',5)
 if i in [1,10,11,14]:d.text((70,1847),'AI ILLUSTRATION'+(' · SOURCE DATA CARD' if i in [10,11] else ''),font=F(18),fill='#d7e2ec')
 im.save(T/f'text_{i:02}.png')
 # Static reference at full animation opacity.
 bg=Image.open(R/f'preview_bg_{i:02}.jpg').convert('RGBA');bg.alpha_composite(im);bg.convert('RGB').save(O/f'proof_{i:02}.jpg',quality=87)

def render(i):
 duration=(frames[i]-frames[i-1])/FPS
 filt="[0:v]setsar=1[b];[1:v]format=rgba,fade=t=in:st=0:d=0.28:alpha=1[t];[b][t]overlay=x=0:y='24*max(0,1-t/0.35)':shortest=1,format=yuv420p[v]"
 run(['-threads','2','-loop','1','-framerate',str(FPS),'-i',str(R/f'preview_bg_{i:02}.jpg'),'-loop','1','-framerate',str(FPS),'-i',str(T/f'text_{i:02}.png'),'-filter_complex_threads','1','-filter_complex',filt,'-map','[v]','-frames:v',str(frames[i]-frames[i-1]),'-c:v','libx264','-threads','2','-preset','fast','-crf','22','-an',str(T/f'scene_{i:02}.mp4')]);print('Rendered scene',i,round(duration,2),flush=True)
with ThreadPoolExecutor(2) as pool:list(pool.map(render,range(1,15)))
(T/'concat.txt').write_text(''.join(f"file '{T/f'scene_{i:02}.mp4'}'\n" for i in range(1,15)))
run(['-f','concat','-safe','0','-i',str(T/'concat.txt'),'-i',str(O/'narration_final.wav'),'-map','0:v','-map','1:a','-c:v','copy','-c:a','aac','-b:a','192k','-af','loudnorm=I=-16:TP=-1.5:LRA=11','-movflags','+faststart','-shortest',str(O/'Benaqaab_India_07_Oct_2026.mp4')])
timing=[dict(scene=i+1,start=frames[i]/FPS,end=frames[i+1]/FPS,**s) for i,s in enumerate(scenes)]
(O/'scene_timing.json').write_text(json.dumps(timing,ensure_ascii=False,indent=2))
def stamp(t):
 ms=round(t*1000);return f'{ms//3600000:02}:{ms//60000%60:02}:{ms//1000%60:02},{ms%1000:03}'
(O/'headline_captions.srt').write_text('\n\n'.join(f"{i+1}\n{stamp(s['start'])} --> {stamp(s['end'])}\n{s['h']}\n{s['s']}" for i,s in enumerate(timing)),encoding='utf-8')
print('FINAL',O/'Benaqaab_India_07_Oct_2026.mp4','duration',len(audio)/48000,flush=True)
