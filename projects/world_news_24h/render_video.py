from pathlib import Path
import subprocess,concurrent.futures,math,json
from playwright.sync_api import sync_playwright
import imageio_ffmpeg
R=Path(__file__).parent; O=R/'delivery';O.mkdir(exist_ok=True);C=R/'.cache'/'render_v2';C.mkdir(exist_ok=True,parents=True)
FF=imageio_ffmpeg.get_ffmpeg_exe();FPS=30;FRAMES=1740
CSS='''html,body{margin:0!important;padding:0!important;width:1080px!important;height:1920px!important;overflow:hidden!important;background:#111922!important}main{display:block!important;padding:0!important;margin:0!important;width:1080px!important;max-width:none!important}main>section:first-child{width:1080px!important}.phone{width:1080px!important;height:1920px!important;aspect-ratio:auto!important;margin:0!important;border:0!important;border-radius:0!important;box-shadow:none!important}.info,.controls{display:none!important}'''
def part(k):
 start=k*580;end=min(FRAMES,start+580);out=C/f'part_{k}.mp4'
 if out.exists() and out.stat().st_size>1000:
  try:
   reader=imageio_ffmpeg.read_frames(str(out));meta=next(reader);reader.close()
   if abs(meta['duration']-(end-start)/FPS)<.02:
    print('Reusing completed part',k,flush=True);return out
  except Exception:pass
 log=(C/f'part_{k}.log').open('w')
 cmd=[FF,'-hide_banner','-loglevel','error','-y','-f','image2pipe','-vcodec','mjpeg','-framerate',str(FPS),'-i','-','-an','-c:v','libx264','-threads','2','-preset','fast','-crf','18','-profile:v','high','-pix_fmt','yuv420p','-r',str(FPS),str(out)]
 enc=subprocess.Popen(cmd,stdin=subprocess.PIPE,stderr=log)
 try:
  with sync_playwright() as pw:
   b=pw.chromium.launch(headless=True,args=['--no-sandbox','--disable-dev-shm-usage']);p=b.new_page(viewport={'width':1080,'height':1920},device_scale_factor=1);errors=[];p.on('pageerror',lambda e:errors.append(str(e)));p.goto((R/'preview.html').as_uri());p.wait_for_function('window.ready===true');p.add_style_tag(content=CSS)
   for f in range(start,end):
    p.evaluate('(t)=>window.seek(t)',f/FPS)
    enc.stdin.write(p.screenshot(type='jpeg',quality=96,clip={'x':0,'y':0,'width':1080,'height':1920}))
    if (f-start)%150==0:print('Part',k,'frame',f,flush=True)
   if errors:raise RuntimeError(errors)
   b.close()
  enc.stdin.close();code=enc.wait();log.close()
  if code:raise RuntimeError((C/f'part_{k}.log').read_text())
  print('Part',k,'complete',flush=True)
 except Exception:
  enc.kill();raise
 return out
with concurrent.futures.ThreadPoolExecutor(1) as pool:parts=list(pool.map(part,range(3)))
(C/'concat.txt').write_text(''.join(f"file '{p}'\n" for p in parts))
out=O/'Benaqaab_World_News_07_Oct_2026.mp4'
subprocess.run([FF,'-hide_banner','-loglevel','error','-y','-f','concat','-safe','0','-i',str(C/'concat.txt'),'-i',str(R/'preview_audio.mp3'),'-map','0:v:0','-map','1:a:0','-c:v','copy','-c:a','aac','-b:a','192k','-ar','48000','-t','58','-movflags','+faststart',str(out)],check=True)
print('FINAL',out,'bytes',out.stat().st_size,flush=True)
