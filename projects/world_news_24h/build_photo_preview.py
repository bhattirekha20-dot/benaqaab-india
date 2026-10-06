from pathlib import Path
import runpy,json,re,base64
R=Path(__file__).parent
runpy.run_path(str(R/'build_preview.py'))
p=R/'preview.html';html=p.read_text();m=re.search(r'const scenes=(.*?),duration=',html);S=json.loads(m.group(1));manifest=json.loads((R/'assets/photo_manifest.json').read_text())
manifest['science']['label']='Francis Halzen · archival photograph'
manifest['germany']['label']='BND premises · archive, not arrest photograph'
(R/'assets/photo_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
def asset(path,label,credit='',source='',license='',licurl=''):
 data=base64.b64encode((R/path).read_bytes()).decode()
 return {'image':'data:image/jpeg;base64,'+data,'label':label,'credit':credit,'source':source,'license':license,'licurl':licurl,'ai':path.startswith('assets/ai_')}
def photo(k):
 m=manifest[k];name=m['creator']
 if k=='kenya':name='CDC / Dr. Frederick A. Murphy'
 return asset(m['path'],m['label'],name,m['source'],m['license'],m['license_url'])
def ai(name,label):return asset('assets/ai_'+name+'.jpg','AI ILLUSTRATION · '+label,'Original AI-generated explanatory artwork')
visuals=[ [ai('world','WORLD NEWS CONCEPT')], [photo('germany'),ai('investigation','NOT ACTUAL EVIDENCE')], [photo('france'),ai('classroom','NOT A SPECIFIC SCHOOL')], [photo('kenya'),ai('health','CONTACT TRACING CONCEPT')], [photo('quebec'),ai('ballot','NOT ELECTION FOOTAGE')], [photo('science'),photo('icecube')], [ai('world','WORLD NEWS CONCEPT')]]
for s,v in zip(S,visuals):s['art']='';s['visuals']=v
html=html[:m.start(1)]+json.dumps(S,ensure_ascii=False)+html[m.end(1):]
css='''
.phone{background:#112b24;color:#fff6e9}.brand{z-index:8;color:#fff6e9;text-shadow:0 1px 5px #000}.brand b{background:#f0c58b;color:#183d30}.date{z-index:8;color:#fff6e9;text-shadow:0 1px 5px #000}.line{z-index:8;background:#fff4}.art{top:0!important;left:0;width:100%;height:100%!important}.photo-wash{position:absolute;inset:-5%;width:110%;height:110%;object-fit:cover;filter:blur(19px) brightness(.38)}.photo-main{position:absolute;left:2%;top:13%;width:96%;height:49%;object-fit:contain}.ai-main{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}.shade{position:absolute;inset:0;background:linear-gradient(180deg,#07140d8c 0%,transparent 21%,transparent 46%,#091c13b3 63%,#081b13ed 83%,#081b13 100%)}.copy{top:64%;text-shadow:0 2px 7px #0008}.kicker{color:#e8c49b}h1{color:#fff6e9}h1 em{color:#ffb778}.sub{color:#e5eddf}.credit{color:#eee8db}.label{color:#e8c9a6;font-size:2.1cqw;letter-spacing:.02em;right:7%;line-height:1.35}.image-note{position:absolute;z-index:4;left:5%;right:5%;top:59.5%;background:#091c13c9;border-radius:3px;padding:5px 7px;color:#f5ead9;font-size:2.35cqw;line-height:1.3;font-weight:700}.sourcebox small{display:block;margin-top:7px;color:#b3c0b5}.photo-in{animation:photoin .28s ease-out both}@keyframes photoin{from{opacity:.25}to{opacity:1}}
'''
html=html.replace('</style>',css+'</style>')
html=html.replace('Large explanatory visuals, animated text and clear source attribution.','Real source photographs and AI illustrations, with animated text and clear attribution.')
html=html.replace('Original explanatory graphics; no third-party footage.','Licensed / public-domain archival photos + labelled AI images; no third-party footage.')
html=html.replace('let current=-1;',"let current=-1,visualKey='';")
html=html.replace("$('seek').value=t;",'''updateVisual(t,n);$('seek').value=t;''')
marker="$('play').onclick=async()=>"
func='''function updateVisual(t,n){let s=scenes[n],end=n+1<scenes.length?scenes[n+1].t:duration;let vindex=s.visuals.length>1&&t>=(s.t+end)/2?1:0,key=n+'-'+vindex;if(key===visualKey)return;visualKey=key;let v=s.visuals[vindex];$('art').innerHTML=(v.ai?'':'<img class="photo-wash" alt="" src="'+v.image+'">')+'<img class="'+(v.ai?'ai-main':'photo-main')+' photo-in" alt="'+v.label+'" src="'+v.image+'"><div class="shade"></div><div class="image-note">'+v.label+'</div>';document.querySelector('.label').textContent=v.ai?'AI-GENERATED · NOT REAL EVENT PHOTOGRAPHY':v.credit+' · '+v.license;const box=$('sourceLink');box.replaceChildren();function link(text,url){let a=document.createElement('a');a.textContent=text;a.href=url;a.target='_blank';a.rel='noopener';box.appendChild(a)}if(s.url)link(s.src,s.url);else box.appendChild(document.createTextNode('Dated world-news snapshot.'));let small=document.createElement('small');small.textContent=v.label+' — '+v.credit;box.appendChild(small);if(v.source){link('Photo source',v.source);box.appendChild(document.createTextNode(' · '));if(v.licurl)link(v.license,v.licurl);else box.appendChild(document.createTextNode(v.license));}}
'''
html=html.replace(marker,func+marker)
p.write_text(html)
credits='# Photo and AI asset credits\n\nReal photos are archival or reference material, NOT photographs of the reported 6 October events. Each is labelled in the preview. Wikimedia Commons metadata supplies the stated licence. Images are resized/JPEG-encoded, with no AI alteration. The underlying photos retain their respective licences; CC BY-SA adaptations must retain the matching share-alike terms.\n\n'
for k,v in manifest.items():credits+=f"## {k.title()}\n{v['label']}\n\nCreator: {v['creator']}\n\nLicence: {v['license']} {v['license_url']}\n\nSource: {v['source']}\n\nFile: {v['path']}\n\n"
credits+='## AI illustrations\nWorld-news globe, investigation folder, classroom, contact-tracing concept and ballot box are original AI-generated illustrations, visibly labelled. They do not depict actual evidence, patients, polling activity, protests or a particular school. No politician faces were generated.\n\n## Selection limits\nNo reuse-cleared exact-event protest, arrest, patient or election-night photograph was established. The preview does not pretend that contextual archive photographs are current event photos. Sources for the news claims remain separate in SOURCES.md.\n'
(R/'PHOTO_CREDITS.md').write_text(credits)
with (R/'SOURCES.md').open('a') as f:f.write('\n## Updated visual treatment\nThe diagram-only visuals have been replaced by six real source photographs (archival/reference) and five labelled AI images. See PHOTO_CREDITS.md and assets/photo_manifest.json for authors, file pages and licences. No original event footage or deleted brand logo has been restored.\n')
print('Updated photo + AI preview:',p,'bytes',len(html))
