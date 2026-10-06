from pathlib import Path
import json,re,base64
from PIL import Image,ImageEnhance
import numpy as np
R=Path(__file__).parent;A=R/'assets';C=A/'neutral';C.mkdir(exist_ok=True)
p=R/'preview.html';html=p.read_text();(R/'preview_before_colour_fix.html').write_text(html)
# Correct AI plates only. Preserve documentary/source photos and the original logo.
for f in A.glob('ai_*.jpg'):
 im=Image.open(f).convert('RGB');im=ImageEnhance.Color(im).enhance(.68)
 x=np.asarray(im).astype(np.float32)/255
 # Cool warm highlights, while retaining black levels and avoiding a heavy blue wash.
 x=x*np.array([.86,.98,1.15]);x=np.clip(x,0,1)
 Image.fromarray((x*255).astype('uint8')).save(C/f.name,quality=95)
m=re.search(r'const scenes=(.*?),duration=',html);S=json.loads(m.group(1))
paths=[['ai_world.jpg'],[None,'ai_investigation.jpg'],[None,'ai_classroom.jpg'],[None,'ai_health.jpg'],[None,'ai_ballot.jpg'],[None,None],['ai_world.jpg']]
for s,ps in zip(S,paths):
 for v,name in zip(s['visuals'],ps):
  if name:v['image']='data:image/jpeg;base64,'+base64.b64encode((C/name).read_bytes()).decode()
html=html[:m.start(1)]+json.dumps(S,ensure_ascii=False)+html[m.end(1):]
# Replace UI/overlay colours; images and logo are embedded binary and unaffected.
colors={'#efaa6d':'#79c5da','#ffb778':'#9ed7e5','#ed8955':'#8bbdce','#f4ad80':'#94cadb','#e4a475':'#99bdcf','#ef7843':'#75bdcf','#e87643':'#75bdcf','#df7140':'#75bdcf','#e7b389':'#abc3d0','#e8c49b':'#b8ced8','#e8c9a6':'#bacbd3','#fff6e9':'#f4f6f7','#fff4df':'#f2f6f8','#f5ead9':'#e9eff3','#eee8db':'#d7e2e8','#e5eddf':'#dce6ec','#b9c8b9':'#b8c7d1','#a2b4a3':'#9badb9','#a5b4a6':'#9aabb8','#b3c0b5':'#b4c1cb','#9db19e':'#9cabb8','#101d19':'#111922','#112b24':'#13212c','#091c13':'#111c28','#081b13':'#101b27','#07140d':'#101923','#20332b':'#20303e','#ece4d2':'#e2eaf0','#163f36':'#203443','#173f36':'#203443','#132d25':'#152734'}
for old,new in colors.items():html=html.replace(old,new)
html=html.replace('</style>','.grain{opacity:.22}.photo-wash{filter:blur(19px) brightness(.38) saturate(.8)}.shade{background:linear-gradient(180deg,#101923bb 0%,transparent 22%,transparent 40%,#111c2830 55%,#111c289c 65%,#111c28e8 80%,#111c28 100%)}.eyebrow{color:#9bc6d8}.brand img{filter:none}</style>')
p.write_text(html)
with (R/'MEMORY.md').open('a') as f:f.write('\n## Colour correction\nUser rejected excessive warmth. AI plates were desaturated and white-balanced toward neutral/cool; originals retained. Overlay palette changed from amber/cream/forest-green to restrained cyan/neutral white/slate. Source photos and original logo pixels unchanged. No timing or narration changes. Final MP4 not rendered. Run cool_colour_pass.py after the other rebuild scripts.\n')
with (R/'REBUILD.md').open('a') as f:f.write('\nFinal colour revision: run python cool_colour_pass.py after improve_motion.py. This is the latest user-requested look.\n')
print('Neutral colour preview saved')
