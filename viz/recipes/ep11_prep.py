# Ep10 "India: last 24 hours" — VO trims + official MEA clip inserts -> master audio, caption words, visemes.
import json, re, subprocess, os, numpy as np
P = '/home/user/projects/ep11_market'
W = '/home/user/.cache/ep11'          # heavy intermediates outside the saved workspace (§77)
MEA = None        # MEA briefing 29 Sep 2026 (YouTube n3mA8lB38Y0), section from 186 s
CAPS = [
 "Sirf ek mahine mein share bazaar se ₹17 lakh crore saaf! Nifty apne peak se 14% neeche. Aakhir market gir kyun raha hai? 5 wajah.",
 "Pehli, kachcha tel. West Asia ki jung se Brent crude $100 ke paar hai. Aur India apna 88% se zyada tel bahar se kharidta hai. Tel mehenga, to mehengai aur kamzor rupaya.",
 "Doosri, videshi niveshak bech rahe hain. September mein FII ne ₹33,864 crore ke shares beche. Aur 29 September ko ek hi din mein ₹9,980 crore, 6 mahine mein sabse zyada.",
 "Teesri, rupaya. Ek dollar ab karib ₹96 ka. Dollar mein dekhein to Sensex is saal 20% se zyada gira hai, 15 saal mein sabse bura.",
 "Chauthi, America mein oonchi byaaj darein aur bond yield, to paisa wahan ja raha hai. Aur paanchvi, ghar ki do pareshaniyaan: kamzor monsoon, is saal baarish 13% kam rahi, aur IPO ki baadh, jo market se paisa kheench rahi hai.",
 "Par ek baat: desi niveshak September ke beeson din kharidte rahe, ₹64,000 crore se zyada. Isliye girawat aur zyada nahi hui. Ye nivesh salah nahi hai. Aapko kya lagta hai, October mein market sambhlega? Comment kijiye, aur aise hi saboot ke liye subscribe kijiye. Yaad rakhiye...",
]
# official clip inserts (after VO clip index 2): source seconds inside MEA, and word onsets (whisper + envelope, verified)
EXT = []   # no official clip inserts in Ep11
ATEMPO = float(os.environ.get('ATEMPO', '1.05')); SR = 48000
def load(path, ss=None, to=None):
    cmd = ['ffmpeg','-v','error'] + (['-ss',str(ss),'-to',str(to)] if ss is not None else []) + ['-i',path,'-ac','1','-ar',str(SR),'-f','f32le','-']
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).copy()
def save(x, path): subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-',path], input=x.astype(np.float32).tobytes(), check=True)
def rms_env(x, hop=480): n = len(x)//hop; return np.sqrt((x[:n*hop].reshape(n,hop)**2).mean(1)+1e-12)
def lufs(path):
    m = subprocess.run(['ffmpeg','-hide_banner','-i',path,'-af','loudnorm=print_format=json','-f','null','-'], capture_output=True, text=True).stderr
    return float(json.loads(m[m.rindex('{'):m.rindex('}')+1])['input_i'])
def syl(w):
    w = re.sub(r'[^a-zA-Z0-9₹]', '', w.lower())
    if not w: return 0.5
    if re.search(r'\d', w): return 2.0 + 0.4*len(w)
    return max(1, len(re.findall(r'[aeiouy]+', w)))
BRK = re.compile(r'[.,?:!…]["\']?$')
clips, words, ext, ext_words = [], [], [], []
t = 0.25
GAP = [0.30, 0.34, 0.34, 0.34, 0.36, 0.0]     # pause after each VO clip
for i, cap in enumerate(CAPS):
    x = load(f'{P}/vo/p{i+1}.wav'); env = rms_env(x); thr = max(env.max()*0.06, 1e-4)
    voiced = np.where(env > thr)[0]; a, b = voiced[0], voiced[-1]+1
    x = x[max(0,a*480-960): min(len(x), b*480+1440)]
    x = np.frombuffer(subprocess.run(['ffmpeg','-v','error','-f','f32le','-ar',str(SR),'-ac','1','-i','-','-af',f'atempo={ATEMPO}','-f','f32le','-'],
                      input=x.tobytes(), capture_output=True, check=True).stdout, np.float32).copy()
    env = rms_env(x); thr = max(env.max()*0.06, 1e-4); dur = len(x)/SR
    quiet = env < thr; pauses = []; s = None
    for k, q in enumerate(np.append(quiet, False)):
        if q and s is None: s = k
        elif not q and s is not None:
            if k - s >= 11 and s > 5 and k < len(env)-5: pauses.append((k - s, s*0.01, k*0.01))
            s = None
    capw = cap.split(); brk = [bool(BRK.search(w)) for w in capw]
    breaks_after = [j for j in range(len(capw)-1) if brk[j]]
    wts = np.array([syl(w) for w in capw]); cum = np.cumsum(wts)/wts.sum()
    chosen, used = [], set()
    for j in breaks_after:
        exp_t = cum[j]*dur; best = None
        for k, pz in enumerate(pauses):
            if k in used or (chosen and pz[1] <= chosen[-1][1]): continue
            dd = abs((pz[1]+pz[2])/2 - exp_t)
            if best is None or dd < best[0]: best = (dd, k)
        if best is not None and best[0] < 0.9: used.add(best[1]); chosen.append(pauses[best[1]] + (j,))
    bounds = [0.0] + [p for c in chosen for p in (c[1], c[2])] + [dur]
    spans = [(bounds[2*k], bounds[2*k+1]) for k in range(len(bounds)//2)]
    cut = set(c[3] for c in chosen); phrases, cur = [], []
    for j in range(len(capw)):
        cur.append(j)
        if j in cut: phrases.append(cur); cur = []
    if cur: phrases.append(cur)
    for ph, (s0, s1) in zip(phrases, spans):
        ww = np.array([syl(capw[j]) for j in ph]); edges = s0 + (s1-s0)*np.r_[0, np.cumsum(ww)]/ww.sum()
        for j, e0, e1 in zip(ph, edges[:-1], edges[1:]):
            words.append(dict(w=capw[j], t0=round(t+e0,3), t1=round(t+e1,3), p=i, b=int(brk[j])))
    clips.append(dict(i=i, start=round(t,3), dur=round(dur,3), breaks=len(chosen), want=len(breaks_after)))
    save(x, f'{W}/p{i+1}_trim.wav')
    t += dur + GAP[i]
    if i == 2:                                            # --- official MEA clip inserts ---
        for k, e in enumerate(EXT):
            y = load(MEA, e['s0'], e['s1']); n = len(y); f = int(0.03*SR)
            y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
            save(y, f'{W}/{e["name"]}.wav')
            d = n/SR; ext.append(dict(name=e['name'], s0=e['s0'], s1=e['s1'], start=round(t,3), dur=round(d,3)))
            ws = e['words']
            for j, (w, st) in enumerate(ws):
                t1 = ws[j+1][1] if j+1 < len(ws) else e['end']
                ext_words.append(dict(w=w, t0=round(t+st-e['s0'],3), t1=round(t+t1-e['s0'],3), seg=e['name'], b=int(j == len(ws)-1)))
            t += d + (0.30 if k == 0 else 0.40)
total = round(t + 0.7, 3)
# VO-only bed (drives the visemes) and the full bed (VO + MEA, each insert loudness-matched to the VO)
bed = np.zeros(int(total*SR)+SR, np.float32)
for c in clips:
    y = load(f'{W}/p{c["i"]+1}_trim.wav'); s = int(c['start']*SR); bed[s:s+len(y)] += y
save(bed[:int(total*SR)], f'{W}/vo_only.wav')
vo_l = np.mean([lufs(f'{W}/p{c["i"]+1}_trim.wav') for c in clips])
full = bed.copy()
for e in ext:
    y = load(f'{W}/{e["name"]}.wav'); g = 10**((vo_l - lufs(f'{W}/{e["name"]}.wav'))/20)
    s = int(e['start']*SR); full[s:s+len(y)] += y*g
    print(f"{e['name']}: gain {20*np.log10(g):+.1f} dB")
save(full[:int(total*SR)], f'{W}/vo_raw.wav')
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{W}/vo_raw.wav','-af','highpass=f=70',f'{W}/vo_hp.wav'], check=True)
m = subprocess.run(['ffmpeg','-hide_banner','-i',f'{W}/vo_hp.wav','-af','loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json','-f','null','-'], capture_output=True, text=True).stderr
j = json.loads(m[m.rindex('{'):m.rindex('}')+1])
af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
      f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{W}/vo_hp.wav','-af',af,'-ar','48000','-ac','2', f'{W}/vo_master.wav'], check=True)
chk = subprocess.run(['ffmpeg','-hide_banner','-i',f'{W}/vo_master.wav','-af','loudnorm=print_format=json','-f','null','-'], capture_output=True, text=True).stderr
jj = json.loads(chk[chk.rindex('{'):chk.rindex('}')+1])
y = load(f'{W}/vo_only.wav'); env = rms_env(y, SR//30); env = env/(np.percentile(env[env>1e-3], 95)+1e-9)
vis = np.where(env > 0.55, 2, np.where(env > 0.18, 1, 0))
for k in range(1, len(vis)-1):
    if vis[k-1] == vis[k+1] != vis[k]: vis[k] = vis[k-1]
json.dump(dict(total=total, clips=clips, words=words, ext=ext, ext_words=ext_words, visemes=vis.tolist()), open(f'{P}/work/timeline.json','w'), ensure_ascii=False)
print("clips:", [(c['start'], c['dur'], f"{c['breaks']}/{c['want']}") for c in clips])
print("ext:", [(e['name'], e['start'], e['dur']) for e in ext])
print(f"total {total}s | words {len(words)} + ext {len(ext_words)} | master {jj['input_i']} LUFS, TP {jj['input_tp']} dBTP")
