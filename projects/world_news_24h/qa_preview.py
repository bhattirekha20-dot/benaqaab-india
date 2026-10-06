from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import numpy as np,json,io
R=Path(__file__).parent;Q=R/'qa';Q.mkdir(exist_ok=True);tim=json.loads((R/'TIMELINE.json').read_text());fps=10;frames=[]
with sync_playwright() as w:
 b=w.chromium.launch(headless=True,args=['--no-sandbox']);p=b.new_page(viewport={'width':900,'height':900});errors=[];p.on('pageerror',lambda e:errors.append(str(e)));p.goto((R/'preview.html').as_uri());p.wait_for_function('window.ready===true');p.add_style_tag(content='main{grid-template-columns:270px 1fr!important}.phone{width:270px!important;}')
 node=p.locator('.phone')
 for i in range(int(tim['duration']*fps)):
  t=i/fps;p.evaluate(f'window.seek({t})');img=Image.open(io.BytesIO(node.screenshot())).convert('L').resize((90,160),Image.Resampling.BILINEAR);frames.append(np.asarray(img,dtype=np.float32)/255.)
  if i%100==0:print('Sampled',t,flush=True)
 fr=np.array(frames);delta=np.abs(np.diff(fr,axis=0));changed=(delta>.02).mean(axis=(1,2));still=changed<.002;freezes=[];start=None
 for i,flag in enumerate(np.append(still,False)):
  if flag and start is None:start=i
  elif not flag and start is not None:
   if (i-start)/fps>=.8:freezes.append([round(start/fps,2),round(i/fps,2)])
   start=None
 report={'scope':'HTML screenshot motion probe; not encoded MP4 and not the unmodified repository motion_report','sample_fps':fps,'frames':len(frames),'thresholds':{'pixel_change':.02,'fraction_pixels':.002,'freeze_seconds':.8},'freezes':freezes,'still_ratio':round(float(still.mean()),3),'js_errors':errors}
 p.evaluate('window.seek(28.7)');a=node.screenshot();p.evaluate('window.seek(9.4)');p.evaluate('window.seek(28.7)');report['repeat_seek_pixel_identical']=a==node.screenshot()
 p.add_style_tag(content='main{grid-template-columns:minmax(280px,410px) 1fr!important}.phone{width:100%!important;}')
 checks=[]
 for width in [1000,375]:
  p.set_viewport_size({'width':width,'height':920})
  for t in [0,8.5,13.9,17,20,25,30,35,40,44,49,53,57.7]:
   p.evaluate(f'window.seek({t})');g=p.evaluate('''()=>{const c=document.querySelector('.copy').getBoundingClientRect(),r=document.querySelector('.credit').getBoundingClientRect(),f=document.querySelector('.phone').getBoundingClientRect();return {textClear:c.bottom<r.top,phoneWidth:f.width,images:[...document.querySelectorAll('.phone img')].every(i=>i.complete&&i.naturalWidth>0)}}''');checks.append({'width':width,'t':t,**g})
  p.evaluate('window.seek(30)');p.screenshot(path=str(Q/f'preview_{width}.png'))
 report['layout_checks']=checks;report['audio_duration']=p.eval_on_selector('audio','a=>a.duration');b.close()
(Q/'HTML_MOTION_AND_LAYOUT.json').write_text(json.dumps(report,indent=2));print(json.dumps({k:v for k,v in report.items() if k!='layout_checks'},indent=2),flush=True)
