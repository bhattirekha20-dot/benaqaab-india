# Ep10 "India: last 24 hours" — VO trims + official MEA clip inserts -> master audio, caption words, visemes.
import json, re, subprocess, os, numpy as np
P = '/home/user/projects/ep10_24hrs'
W = '/home/user/.cache/ep10'          # heavy intermediates outside the saved workspace (§77)
MEA = f'{W}/media/mea_sec.mp4'        # MEA briefing 29 Sep 2026 (YouTube n3mA8lB38Y0), section from 186 s
CAPS = [
 "Pichhle 24 ghante mein India mein kya hua? 6 badi khabrein, saboot ke saath.",
 "Pehli, Supreme Court se. Cancer ki ek dawa retailer ko ₹2,700 mein milti hai, par MRP hai ₹27,000! Court ne kaha, \"This is carnage.\" Sujhav diya, har dawa par ek jaisa 16% margin. Agli sunwai 12 October ko.",
 "Doosri, Turkey ke President Erdogan ne UN mein Kashmir ka zikr kiya. India ka jawab, MEA se suniye.",
 "Teesri, Jammu-Kashmir ke Kathua se. Sewa-2 hydro project ke camp mein, adhikariyon ke mutabik, ek CISF jawan ne apne hi saathiyon par goli chala di. 4 ki jaan gayi. Aaropi giraftar hai, aur Court of Inquiry ke aadesh ho chuke hain.",
 "Chauthi, Bihar. Nepal mein bhaari baarish se Gandak ufaan par hai. Bagaha mein jalstar 91.25 metre, ab tak ka sabse ooncha. Gopalganj aur Saran mein tatbandh toote, kai gaon par khatra.",
 "Paanchvi, achhi khabar! Asian Games mein aaj India ne compound archery ke teeno team gold jeet liye. Mahila team ne China ko haraya, 238 ke world record score ki barabari karke. Trap mixed team mein bhi gold. India ke ab 10 gold, kul 59 medal. Aur Lovlina Borgohain final mein!",
 "Chhathi, politics. Voter list ke SIR par vipakshi INDIA bloc aaj Delhi mein mila. Kharge ne kaha, Chief Election Commissioner ko hataya jaye, aur chunav ballot paper se hon. Chunav Aayog ka kehna hai, uske aadesh poori tarah kanooni hain.",
 "In 6 mein aapke liye sabse badi khabar kaunsi hai? Comment mein number likhiye. Aisi saboot wali khabron ke liye like aur subscribe kijiye, aur dekhiye...",
]
# official clip inserts (after VO clip index 2): source seconds inside MEA, and word onsets (whisper + envelope, verified)
EXT = [
 dict(name='meaA', s0=7.45, s1=14.05, words=[('India',7.60),('rejects',8.00),('the',8.80),('unwarranted',8.86),('references',9.34),('to',9.90),
      ('India,',10.77),('Indian',11.88),('Union',12.12),('Territory',12.56),('of',13.06),('Jammu',13.14),('and',13.40),('Kashmir…',13.44)], end=13.90),
 dict(name='meaB', s0=28.58, s1=32.10, words=[('…and',28.68),('no',28.90),('external',29.05),('party',29.50),('has',29.80),('any',29.98),
      ('locus',30.47),('standi',30.80),('on',31.43),('this',31.56),('issue.',31.70)], end=31.91),
]
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
GAP = [0.30, 0.36, 0.26, 0.36, 0.36, 0.36, 0.36, 0.0]     # pause after each VO clip
for i, cap in enumerate(CAPS):
    x = load(f'{P}/vo/p{i+1}.flac'); env = rms_env(x); thr = max(env.max()*0.06, 1e-4)
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
