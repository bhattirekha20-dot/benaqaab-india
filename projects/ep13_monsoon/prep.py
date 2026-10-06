# Ep13 "Baarish 13% Kam: Kya Aapki Thali Mehengi Hogi?" — VO trims -> master audio, caption words, visemes.
# Adapted from viz/recipes/ep11_prep.py (same logic). No third-party audio inserts (EXT empty).
import json, re, subprocess, os, numpy as np
P = '/home/user/projects/ep13_monsoon'
W = '/home/user/.cache/ep13'          # heavy intermediates outside the saved workspace
EXT = []
CAPS = [
 "Is saal India mein baarish 13% kam hui. Sabse kam baarish 2015 ke baad. Aur asli khabar? Baarish ka asar abhi shuru hua hai. Kuch cheezein jo aapki thali mein aati hain, unke daam badhne wale hain.",
 "Aaj samjhenge: El Nino kya hai, is saal kya hua, aur aane wale mahino mein kya khatra hai. Aakhir mein: kaun si cheezein sarkar aur aapko dekhni chahiye.",
 "El Nino ek samundar ki ghatna hai. Pacific Mahasagar ka ek bada hissa normal se zyada garam ho jaata hai. Isse hawaon ka pattern badal jaata hai, aur India ki monsoon kamzor pad jaati hai. 1951 ke baad, El Nino ke lagbhag saat mein se chaar saal mein India ki baarish normal se kam rehti hai. Ab 2026 wala El Nino badh raha hai. International Research Institute ke mutabik, yeh late 2026 aur 2027 ki shuruaat mein bahut strong ho sakta hai, aur March tak chal sakta hai.",
 "To is saal hua kya? Monsoon 30 September ko khatam hua. Kul baarish 759 millimetre, jabki normal 869 millimetre hoti hai. Yaani 13% kami. Yeh 2015 ke baad sabse kam baarish hai. Sabse bura haal East aur North East mein raha: wahan baarish 26% kam thi. South mein 24%. 36 mein se 24 subdivisions mein baarish 10% se zyada kam rahi.",
 "Aur baarish ka asar sirf kheton tak nahi hai. Desh ke bade reservoirs, yaani jheel aur bandh, abhi sirf 72% bhare hain. Normal se karib 12% kam. Aur 51 dams aadhe se bhi kam bhare hain. Paanch rajyon mein sookha declare hua hai. Kharif fasal ka target sarkar ne kam kar diya. America ke agriculture department ke andaza ke mutabik chawal ka production 154 se 147 million tonne gir sakta hai.",
 "Iska asar aapki jeb par dikh raha hai. September mein pyaz ke daam pichhle saal se dugne ho gaye. August mein food inflation 5.95% par tha. Gaon mein log bade saudaari karne se ruk rahe hain: August mein tractor aur do pahiya vahanon ki bikri tez girayi hai. ICRA ne kheti ki growth ka anumaan 1% kar diya hai. FMCG companies ke shares poori saal ki sabse neechi level par hain.",
 "Asli test ab shuru hota hai. Rabi ki buwai October se hoti hai: gehu, sarson, chana, masoor, aloo, pyaz. El Nino ka matlab hai lambi sookhi garmiyan aur chhota, garm sardi. Agriculture Secretary ne khud kaha hai ki is saal rabi rainfed ilaakon ke liye mushkil hogi aur production par asar padega. Ek sookhe saal ka asar agli fasal par bhi padta hai, kyunki zameen mein nami kam hoti hai.",
 "To sarkar kya kar rahi hai? 30 September ko cabinet ne gehu ka MSP 25 rupaye badha kar 2,610 rupaye per quintal kar diya. Rabi ke liye sookhe se ladne wale beej aur state level planning ka plan hai. Aap kya dekh sakte hain? Ek: reservoir ka level. Do: November aur December ki buwai ki khabar. Teen: December se February ka temperature. Chaar: pyaz, tamatar aur dalon ke daam. Yahi asli signal honge.",
 "Monsoon 13% kam hua, aur uska asar agle chhah mahine tak dikhega. El Nino ek global pattern hai, lekin iska bill India ke kisan aur aapki thali dono bharte hain. Aapke ilaake mein kya mehngai dikh rahi hai? Comment mein bataiye, aur aise explainers ke liye subscribe kijiye.",
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
GAP = [0.55, 0.55, 0.60, 0.55, 0.60, 0.55, 0.60, 0.60, 0.0]     # pause after each VO clip
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
