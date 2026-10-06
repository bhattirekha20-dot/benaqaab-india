# Ep12 "NavIC: India ka apna GPS kyun band pada hai?" — VO trims -> master audio, caption words, visemes.
# Adapted from viz/recipes/ep11_prep.py (same logic). No third-party audio inserts (EXT empty).
import json, re, subprocess, os, numpy as np
P = '/home/user/projects/ep12_navic'
W = '/home/user/.cache/ep12'          # heavy intermediates outside the saved workspace
EXT = []
FILES = [1, 2, 3, 4, 5, 9, 6, 7, 8]   # vo file order -> scene order (p9 = armed-forces beat, after p5)
CAPS = [
 "India ne apna khud ka GPS banaya, NavIC. Lekin aaj yeh aapki location akela nahi bata sakta. Yeh baat sarkar ne khud Parliament mein maani hai. Aur wajah? Ek chhoti si technical galti.",
 "To chaliye poora safar dekhte hain: NavIC bana kyun, kaam kaise karta hai, kya toota, aur aage kya hone wala hai.",
 "Kahaani 1999 se shuru hoti hai. Kargil jung ke waqt India ko America ka GPS chahiye tha, lekin data dene se mana kar diya gaya. Us din ek sabak mila: apni location kisi doosre desh ke haath mein nahi ho sakti. 2006 mein sarkar ne apna navigation system approve kiya, aur 2013 se satellite orbit mein jaane lage. Naam mila, NavIC. Coverage? Poora India, aur border se pandrah sau kilometre aage tak.",
 "Ab samajhiye yeh kaam kaise karta hai. Aapka phone chaar alag satellite se signal leta hai. Teen satellite se aapki latitude, longitude aur height pata chalti hai. Aur chautha satellite? Woh sirf time batata hai. Kyunki signal light ki speed se chalta hai, waqt ki chhoti galti, doori ki badi galti ban jaati hai. Ek microsecond ki galti, zameen par teen sau metre. Isiliye har satellite ke andar atomic clock lagta hai. Poora NavIC saat satellite se banta hai: teen geostationary, aur chaar geosynchronous orbit mein.",
 "To kya toda? Saat slot bhare the, lekin saal beete aur satellite purane ho gaye. Pehli generation ke atomic clocks, jo videsh se aaye the, ek ke baad ek fail hote gaye. Aur January 2025 mein ISRO ka sauwan launch, NVS-02. Satellite orbit mein pahunch gaya, lekin uska engine hi nahi chala. Fuel line ka valve kholne wala signal pahuncha hi nahi. Satellite aaj tak galat orbit mein hai. Nateeja: sirf teen satellite bache, IRNSS 1B, IRNSS 1I, aur NVS-01. Chaar chahiye, teen hain.",
 "Aur yeh sirf phone ki baat nahi hai. NavIC ka ek encrypted signal India ki armed forces ke liye hai. Missile navigation, warship coordination, aur troop movement, sab isi par nirbhar karte hain. Jab satellite kam padte hain, to yeh strategic sahara bhi kamzor padta hai. Isiliye NVS-03 sirf ek satellite nahi, ek zaroorat hai.",
 "Lekin sab kuch band nahi hai. Timing service abhi bhi chalu hai: power grid, telecom, banking, aur desh ka standard time isi par chalta hai. Tees hazaar se zyada fishing boats NavIC ke message bhej paate hain. Hawaai jahaazon ke liye alag system, GAGAN, pehle se kaam kar raha hai. Bas standalone positioning nahi milti. Sarkar kehti hai koi khatra nahi, kyunki aapke phone mein GPS aur doosre systems bhi hote hain.",
 "Aur ab ummeed ki khabar. NVS-03 taiyaar hai. Reports ke mutabik launch window hai pandrah se bees October. GSLV rocket ka pehla stage Sriharikota par lag chuka hai. Agar sab theek chala, to chautha satellite orbit mein pahunchega, aur NavIC ki positioning wapas. Uske baad NVS-04 aur NVS-05.",
 "Unnees sau ninyanve mein humein apna system banana pada tha. Aaj NavIC apne chaathe satellite ka intezaar kar raha hai. Aapko kya lagta hai, humein apne navigation par kitna depend karna chahiye? Comment mein bataiye, aur aise videos ke liye subscribe kijiye.",
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
GAP = [0.40, 0.55, 0.55, 0.55, 0.60, 0.55, 0.55, 0.55, 0.0]     # pause after each VO clip
for i, cap in enumerate(CAPS):
    x = load(f'{P}/vo/p{FILES[i]}.mp3'); env = rms_env(x); thr = max(env.max()*0.06, 1e-4)
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
