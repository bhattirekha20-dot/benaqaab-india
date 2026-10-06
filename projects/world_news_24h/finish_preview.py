from pathlib import Path
import json,re,base64,subprocess,wave,math
import numpy as np
import imageio_ffmpeg
R=Path(__file__).parent;Q=R/'qa';Q.mkdir(exist_ok=True);FF=imageio_ffmpeg.get_ffmpeg_exe()
# Preview sound mix only; no video encoding.
r=subprocess.run([FF,'-v','error','-i',str(R/'narration_repo.mp3'),'-f','f32le','-ac','1','-ar','48000','-'],capture_output=True,check=True);x=np.frombuffer(r.stdout,dtype='<f4').copy();SR=48000;total=58.0
mix=np.zeros(int(total*SR),dtype=np.float64);mix[:len(x)]=x
cuts=[7.70,16.22,22.58,33.86,42.4,52.4]
for k,t in enumerate(cuts):
 n=int(.14*SR);z=np.arange(n)/SR;f=420+100*k
 # Original short, restrained tonal edit cue. Under the narration, not a music bed.
 cue=.010*np.sin(2*np.pi*(f*z+240*z*z))*np.exp(-z*42)*np.sin(np.pi*np.minimum(1,z/.01))**2
 start=int(t*SR);mix[start:start+n]+=cue
peak=max(np.max(np.abs(mix)),1e-6);mix*=10**(-2/20)/peak
with wave.open(str(Q/'mix_pre.wav'),'wb') as w:w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((np.clip(mix,-1,1)*32767).astype('<i2').tobytes())
def measure(path):
 p=subprocess.run([FF,'-hide_banner','-nostats','-i',str(path),'-af','loudnorm=I=-14:TP=-1.5:LRA=6:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
 return json.loads(re.findall(r'\{\s*"input_i".*?\}',p.stderr,re.S)[-1])
subprocess.run([FF,'-v','error','-y','-i',str(Q/'mix_pre.wav'),'-af','acompressor=threshold=0.13:ratio=3:attack=5:release=80:makeup=1','-ar','48000',str(Q/'mix_controlled.wav')],check=True)
m=measure(Q/'mix_controlled.wav');f=f"loudnorm=I=-14:TP=-1.5:LRA=6:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true"
subprocess.run([FF,'-v','error','-y','-i',str(Q/'mix_controlled.wav'),'-af',f,'-ar','48000','-c:a','libmp3lame','-b:a','192k',str(R/'preview_audio.mp3')],check=True)
measured=measure(R/'preview_audio.mp3');(Q/'PREVIEW_AUDIO_QC.json').write_text(json.dumps({'scope':'Decoded final preview MP3, NOT muxed MP4','target_lufs':-14,'target_true_peak_max_dbtp':-1.5,'measured_lufs':float(measured['input_i']),'measured_true_peak_dbtp':float(measured['input_tp']),'measured_lra_lu':float(measured['input_lra']),'duration_seconds':total,'method':'two-pass loudnorm; measured after MP3 encoding'},indent=2))
html=(R/'preview.html').read_text();(R/'preview_before_final_audit.html').write_text(html)
m=re.search(r'const scenes=(.*?),duration=',html);S=json.loads(m.group(1));S[1]['rail']=['ALLEGATION','INQUIRY','UNPROVEN'];S[4]['rail']=['ELECTION','MINORITY','NOT DECIDED']
S[1]['src']='German federal prosecutors · 6 Oct 2026';S[1]['url']='https://www.presseportal.de/blaulicht/pm/14981/6365655';S[5]['src']='NobelPrize.org · official release · 6 Oct 2026';S[5]['url']='https://www.nobelprize.org/prizes/physics/2026/press-release/'
switches=[None,13.7,19.5,28.98,39.0,46.0,None]
for s,v in zip(S,switches):s['switchAt']=v
html=html[:m.start(1)]+json.dumps(S,ensure_ascii=False)+html[m.end(1):]
html=re.sub(r',duration=57\.92',',duration=58.0',html);html=html.replace('max="57.92"','max="58"')
html=re.sub(r'<audio id="audio".*?</audio>', '<audio id="audio" preload="auto" src="data:audio/mpeg;base64,'+base64.b64encode((R/'preview_audio.mp3').read_bytes()).decode()+'"></audio>',html)
html=html.replace('t>=(s.t+end)/2','t>=(s.switchAt??((s.t+end)/2))').replace('shotStart=vi?(s.t+end)/2:s.t','shotStart=vi?(s.switchAt??((s.t+end)/2)):s.t').replace('shotDur=vi?(end-s.t)/2:(s.visuals.length>1?(end-s.t)/2:end-s.t)','shotDur=vi?(end-shotStart):(s.visuals.length>1?(s.switchAt??((s.t+end)/2))-s.t:end-s.t)')
html=html.replace("if(t===0){","if(n===0){")
html=html.replace('The exact rolling 24-hour cutoff has not been certified. Reports may develop.','Dated snapshot, not a certified rolling-24-hour bulletin. Reports may develop.')
html=html.replace('REPOSITORY-ALIGNED PREVIEW · Final export awaits approval.','AUDITED PREVIEW · Final export awaits approval.')
(R/'preview.html').write_text(html)
# Structural plan and factual-source references.
photos=json.loads((R/'assets/photo_manifest.json').read_text());assets={}
for k,v in photos.items():assets[k]={'path':v['path'],'role':'Archival/reference source photo; not a current event image','rights_note':v['creator']+'; '+v['license']+'; '+v['source']}
for k in ['world','investigation','classroom','health','ballot']:assets['ai_'+k]={'path':'assets/ai_'+k+'.jpg','role':'Labelled original conceptual illustration','rights_note':'AI-generated; not evidence or an actual event photograph'}
assets['logo']={'path':'repo_reference/brand/logo.png','role':'Unaltered channel logo','rights_note':'User-designated repository brand asset'};assets['audio']={'path':'preview_audio.mp3','role':'Narration master plus original soft edit cues','rights_note':'Previously selected synthetic voice voice-02; original sound cues'}
statements=['August Hanning arrested on espionage suspicion; allegations unproven.','Students, teachers and parents protested over school conditions in France.','Kenya announced an imported Ebola case; patient died and contacts were traced.','Parti Québécois election victory without a majority does not establish independence.','Francis Halzen received the 2026 Physics Nobel for IceCube and cosmic-neutrino work.']
claims={f'c{i}':{'statement':text,'unit':'dated news development','qualification':'6 October 2026 report; archive images are not event evidence. See FACT_LEDGER.md.','source_url':S[i]['url']} for i,text in enumerate(statements,1)}
shots=[];groups=[['ai_world'],['germany','ai_investigation'],['france','ai_classroom'],['kenya','ai_health'],['quebec','ai_ballot'],['science','icecube'],['ai_world']]
for i,s in enumerate(S):
 end=S[i+1]['t'] if i+1<len(S) else total
 shots.append({'id':f's{i}','start':s['t'],'end':end,'purpose':'Question-led opening' if i==0 else 'Explain '+s['k'],'hero':groups[i][0],'start_state':'Current story imagery only, source and archive/AI label visible','end_state':'Qualified concise headline and narration complete','primary_motion':'Time-driven semantic rail follows the current topic; content-matched source-to-illustration cut','secondary_motion':'Restrained camera drift and indicator pulse','camera':'Slow forward scale on AI plate, contained source photos with small translation','audio':'Selected narration master with measured audio levels and subtle original cut cue','transition':'Hard Cut between stories; no cross-story overlap','acceptance':'At 375px, all images load; text stays inside safe width; repeated seek returns identical frame','asset_roles':['Source photo or labelled concept, not fabricated evidence','Single headline layer and separate source note'],'detail_choices':['Native logo aspect ratio and colour','No source badge pill or scene counter','Archive-versus-event distinction stays visible'],'claims':[f'c{i}'] if 1<=i<=5 else [],'assets':groups[i]+['logo','audio']})
plan={'duration':total,'fps':30,'width':1080,'height':1920,'assets':assets,'claims':claims,'shots':shots};(R/'PLAN.json').write_text(json.dumps(plan,ensure_ascii=False,indent=2))
(R/'TIMELINE.json').write_text(json.dumps({'duration':total,'fps':30,'audio':'preview_audio.mp3','scene_starts':[s['t'] for s in S],'visual_switches':switches,'method':'automatic word timestamps, topic-boundary selection; not character counts'},indent=2))
# Summary captions are a review aid, not verbatim subtitles.
def stamp(t):
 n=round(t*1000);return f'{n//3600000:02}:{n//60000%60:02}:{n//1000%60:02},{n%1000:03}'
(R/'summary_captions.srt').write_text('\n\n'.join(f"{i+1}\n{stamp(s['t'])} --> {stamp(shots[i]['end'])}\n{re.sub('<[^>]+>',' ',s['h']).strip()}\n{s['sub']}" for i,s in enumerate(S)))
print(json.dumps(measured,indent=2));print('Preview/plan/audio updated. No MP4 rendered.')
