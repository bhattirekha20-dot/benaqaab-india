from pathlib import Path
import subprocess,re,json,importlib.util,shutil
import imageio_ffmpeg
R=Path(__file__).parent;O=R/'delivery';Q=O/'qa';Q.mkdir(exist_ok=True);FF=imageio_ffmpeg.get_ffmpeg_exe();v=O/'Benaqaab_World_News_07_Oct_2026.mp4'
def loud():
 r=subprocess.run([FF,'-hide_banner','-nostats','-i',str(v),'-af','loudnorm=I=-14:TP=-1.5:LRA=6:print_format=json','-f','null','-'],capture_output=True,text=True,check=True)
 return json.loads(re.findall(r'\{\s*"input_i".*?\}',r.stderr,re.S)[-1])
a=loud()
if float(a['input_tp'])>-1.5:
 gain=-1.65-float(a['input_tp']);temp=O/'safe_peak.mp4'
 subprocess.run([FF,'-v','error','-y','-i',str(v),'-c:v','copy','-af',f'volume={gain}dB','-c:a','aac','-b:a','192k','-ar','48000','-movflags','+faststart',str(temp)],check=True);temp.replace(v);a=loud()
r=subprocess.run([FF,'-hide_banner','-i',str(v),'-f','null','-'],capture_output=True,text=True);(Q/'decode.log').write_text(r.stderr);assert r.returncode==0
reader=imageio_ffmpeg.read_frames(str(v));meta=next(reader);reader.close()
spec=importlib.util.spec_from_file_location('motion',R/'repo_reference/viz/motion.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
t=json.loads((R/'TIMELINE.json').read_text());cuts=t['scene_starts'][1:]+[x for x in t['visual_switches'] if x is not None]
m=mod.motion_report(v,cuts=cuts,ffmpeg=FF)
for sec in [0,9,14,18,25,30,36,44,49,55,57.5]:
 subprocess.run([FF,'-v','error','-y','-ss',str(sec),'-i',str(v),'-frames:v','1',str(Q/f'frame_{sec}.jpg')],check=True)
report={'file':v.name,'bytes':v.stat().st_size,'metadata':meta,'decode_exit_code':r.returncode,'motion_report':m,'audio':{'integrated_lufs':float(a['input_i']),'true_peak_dbtp':float(a['input_tp']),'lra_lu':float(a['input_lra'])},'scope':'Measured on encoded MP4; source/event and rights limitations in accompanying documentation.'}
(Q/'FINAL_QC.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2))
for f in ['PHOTO_CREDITS.md','FACT_LEDGER.md','summary_captions.srt']:shutil.copy2(R/f,O/f)
