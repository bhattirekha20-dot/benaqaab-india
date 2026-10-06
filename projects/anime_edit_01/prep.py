# Anime edit "NEON BLADE" (Shorts) — VO trims -> master audio, caption words, visemes.
# Adapted from projects/ep14_bullet/prep.py (same logic). No third-party audio (EXT empty).
import json, re, subprocess, os, numpy as np
P = '/home/user/projects/anime_edit_01'
W = '/home/user/.cache/anime'          # heavy intermediates outside the saved workspace
EXT = []
CAPS = [
 "Raat gyarah baje. Sheher so gaya... lekin ek talwar abhi bhi jaag rahi hai.",
 "Ye uski kahani hai, jisne apna naam bhula diya... sirf ek vaada yaad hai.",
 "Wo akela kyun? Kyunki teen aaye the use dhundhne.",
 "Unki aankhon mein laal roshni thi... aur uske haath mein ek imtihaan.",
 "Ek pal. Ek vaar. Baarish ki boondein ruk gayi.",
 "Sab kuch dhundh mein tha. Faisla... aaj raat.",
 "Chhat par, chaand ke saamne. Usne kaha... aaj koi nahi bachega.",
 "Aakhri vaar. Poori taakat. Aur phir... sab shaant.",
 "Subah hui. Wo chala gaya... kahani reh gayi. Part 2 chahiye? Comment karo.",
]
ATEMPO = float(os.environ.get('ATEMPO', '1.06')); SR = 48000
os.makedirs(W, exist_ok=True); os.makedirs(f'{P}/work', exist_ok=True)
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
GAP = [0.30, 0.30, 0.30, 0.32, 0.30, 0.32, 0.30, 0.30, 0.0]     # pause after each VO clip
for i, cap in enumerate(CAPS):
    x = load(f'{P}/vo/p{i+1}.mp3'); env = rms_env(x); thr = max(env.max()*0.06, 1e-4)
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
total = round(t + 0.7, 3)
bed = np.zeros(int(total*SR)+SR, np.float32)
for c in clips:
    y = load(f'{W}/p{c["i"]+1}_trim.wav'); s = int(c['start']*SR); bed[s:s+len(y)] += y
save(bed[:int(total*SR)], f'{W}/vo_only.wav')
vo_l = np.mean([lufs(f'{W}/p{c["i"]+1}_trim.wav') for c in clips])
# master: loudness-normalised to -14.2 LUFS with -1.5 dBTP ceiling
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{W}/vo_only.wav','-af',
    f'loudnorm=I=-14.2:TP=-1.5:LRA=9,alimiter=limit=0.88','-ar',str(SR),f'{W}/vo_master.wav'], check=True)
m = subprocess.run(['ffmpeg','-hide_banner','-i',f'{W}/vo_master.wav','-af','loudnorm=print_format=json','-f','null','-'], capture_output=True, text=True).stderr
j = json.loads(m[m.rindex('{'):m.rindex('}')+1])
vis = []
ys = load(f'{W}/vo_master.wav')
for k in range(int(total*30)+2):
    seg = ys[int(k/30*SR): int((k/30+0.14)*SR)]
    if len(seg) == 0: vis.append(0); continue
    e = rms_env(seg, 480); e = e if len(e) else np.array([0.0])
    vis.append(int(min(2, np.argmax(np.r_[e.mean(), 0]) + (1 if e.max() > 3*max(e.mean(),1e-6) else 0))))
capw_all = ' '.join(CAPS).split()
json.dump(dict(total=total, clips=clips, words=words, ext=ext, ext_words=ext_words, visemes=vis),
          open(f'{P}/work/timeline.json','w'), indent=1)
print(f'OK total={total:.3f}s clips={len(clips)} words={sum(len(c.split()) for c in CAPS)} voLUFS={vo_l:.2f} master={j["input_i"]} TP={j["input_tp"]}')
for c in clips: print(f'  p{c["i"]+1}: start={c["start"]:.3f} dur={c["dur"]:.3f} breaks={c["breaks"]}/{c["want"]}')
