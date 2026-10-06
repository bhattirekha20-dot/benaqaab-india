# Ep14 "Bullet Train 2027: 50 km pehle, 508 km poora" — VO trims -> master audio, caption words, visemes.
# Adapted from viz/recipes/ep11_prep.py (same logic). No third-party audio inserts (EXT empty).
import json, re, subprocess, os, numpy as np
P = '/home/user/projects/ep14_bullet'
W = '/home/user/.cache/ep14'          # heavy intermediates outside the saved workspace
EXT = []
CAPS = [
 "2027 mein India ki pehli bullet train chalu hone wali hai. Pehla hissa: Surat se Bilimora, sirf 50 kilometre. Lekin asli kahaani 508 kilometre ki hai, aur uspar kaam abhi bhi chal raha hai.",
 "Aaj samjhenge: yeh project kitna bada hai, abhi kitna ban chuka hai, Mumbai wala mushkil hissa kya hai, aur train kaun si chalegi. Aakhir mein: paisa aur timeline.",
 "Yeh hai kya? Mumbai ke BKC se Ahmedabad tak 508 kilometre, aur 12 stations. Rasta Maharashtra, Dadra Nagar Haveli aur Gujarat se hokar jaata hai. Design speed 350, operating speed 320 kilometre prati ghanta. Safar karib 2 ghante 7 minute ka. Aur raste ka 90% hissa hawa mein hai, viaduct par.",
 "To kaam kitna hua? Railway Minister ke mutabik, July tak project 80% poora tha. September tak 320 kilometre viaduct ban chuka, aur 206 kilometre track bed taiyaar hai. 17 nadiyon ke pul bhi ban chuke hain, aur zameen ka adhigrahan 100% poora hai. Gujarat mein kaam aage hai, Maharashtra mein peeche.",
 "Asli chunauti Mumbai mein hai. BKC se Shilphata tak 21 kilometre lambi tunnel ban rahi hai. Isi mein 7 kilometre samundar ke neeche, Thane Creek ke andar. Yeh India ki pehli undersea rail tunnel hogi. 20 September ko iska ek bada hissa poora hua. Baki kaam tunnel boring machines kar rahi hain. Isiliye Mumbai sabse aakhir mein aayega, 2029 mein.",
 "Ab train. Pehle hisse ke liye India apni hi high speed train chalayegi. BEML ko yeh kaam September 2024 mein mila, aur pehla prototype 2026 mein aana tha. Abhi car body ka squeeze test chal raha hai, taaki strength sabit ho. Japan ki agli peedhi ki Shinkansen, E10, 2030 ke dashak ki shuruaat mein aayegi.",
 "Aur paisa? Shuruaati sanctioned cost thi 1.08 lakh crore rupaye. Japan ki JICA iska 81% fund kar rahi hai: point one percent byaaj, 50 saal ka loan, aur 15 saal ki riyat. Lekin 2026 mein khabrein aayi hain ki revised cost do lakh crore ke aas paas ho sakti hai. Yeh sirf report hai, officially approve nahi hui.",
 "To aage kya dekhna hai? Ek: December tak pehle hisse ka civil kaam poora. Do: track, signal aur safety ka testing aur approval. Teen: mid 2027 mein Surat Bilimora par pehli service. Chaar: 2028 mein Thane, aur 2029 mein Mumbai. 2 ghante 7 minute mein Mumbai se Ahmedabad: yahi is project ka vaada hai.",
 "2027 ka intezaar hai. Pehla hissa 50 kilometre ka, poora rasta 508. Aapko kya lagta hai, is project ka asli fayda kya hoga? Comment mein bataiye, aur aise explainers ke liye subscribe kijiye.",
]
ATEMPO = float(os.environ.get('ATEMPO', '1.05')); SR = 48000
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
GAP = [0.55, 0.55, 0.55, 0.60, 0.60, 0.55, 0.60, 0.60, 0.0]     # pause after each VO clip
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
full = bed.copy()
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
print(f"total {total}s | words {len(words)} | master {jj['input_i']} LUFS, TP {jj['input_tp']} dBTP")
