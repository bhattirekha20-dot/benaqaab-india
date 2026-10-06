import json, re, subprocess, wave, numpy as np
from PIL import Image, ImageFilter
P = '/home/user/projects/ep8_oct_rules'
SCRIPT = [  # (VO text as spoken, on-screen caption words in Hinglish-Latin)
 ("कल, 1 October से, आपकी जेब से जुड़े 4 नियम बदल रहे हैं। और आखिरी वाला सबसे ज़्यादा confusion वाला है।",
  "Kal, 1 October se, aapki jeb se jude 4 niyam badal rahe hain. Aur aakhri wala sabse zyada confusion wala hai."),
 ("पहला: LPG. Subsidy वाला cylinder चाहिए, तो biometric Aadhaar verification ज़रूरी है। करीब 90% लोग कर चुके हैं। नहीं किया, तो subsidy वाला refill book नहीं होगा। Delivery के वक्त, distributor पर या app से हो जाता है।",
  "Pehla: LPG. Subsidy wala cylinder chahiye, to biometric Aadhaar verification zaroori hai. Kareeb 90% log kar chuke hain. Nahi kiya, to subsidy wala refill book nahi hoga. Delivery ke waqt, distributor par ya app se ho jata hai."),
 ("दूसरा: SBI. Salary account है, तो दूसरे bank के ATM पर free transactions अब 10 नहीं, सिर्फ 5। उसके बाद हर withdrawal पर 23 रुपये plus GST। Basic account में 4 free withdrawals, फिर 15 रुपये plus GST।",
  "Doosra: SBI. Salary account hai, to doosre bank ke ATM par free transactions ab 10 nahi, sirf 5. Uske baad har withdrawal par ₹23 plus GST. Basic account mein 4 free withdrawals, phir ₹15 plus GST."),
 ("तीसरा नियम हर परिवार के काम का है। जन्म या मृत्यु का registration एक साल से ज़्यादा late हुआ, तो अब DM या SDM का order चाहिए। दो साल से ज़्यादा, तो Judicial Magistrate का order। इसलिए registration time पर कराइए।",
  "Teesra niyam har parivaar ke kaam ka hai. Janm ya mrityu ka registration ek saal se zyada late hua, to ab DM ya SDM ka order chahiye. Do saal se zyada, to Judicial Magistrate ka order. Isliye registration time par karaiye."),
 ("और अब सबसे बड़ा confusion: UPI. 15 October से दुकान पर 2,000 रुपये से ऊपर के payment पर 0.4% fee लगेगी। पर ये fee दुकानदार की है, नियम के मुताबिक आपसे नहीं ली जानी चाहिए। दोस्त या family को भेजे पैसे बिल्कुल free रहेंगे।",
  "Aur ab sabse bada confusion: UPI. 15 October se dukaan par ₹2,000 se upar ke payment par 0.4% fee lagegi. Par ye fee dukandaar ki hai, niyam ke mutabik aapse nahi li jani chahiye. Dost ya family ko bheje paise bilkul free rahenge."),
 ("इन चारों में से आप पर सबसे ज़्यादा असर कौन सा डालेगा? Comment में बताइए, और like, subscribe ज़रूर कीजिए।",
  "In chaaron mein se aap par sabse zyada asar kaunsa dalega? Comment mein bataiye, aur like, subscribe zaroor kijiye."),
]
import os
ATEMPO = float(os.environ.get('ATEMPO', '1.03'))
SR = 48000
def load(path):
    raw = subprocess.run(['ffmpeg','-v','error','-i',path,'-ac','1','-ar',str(SR),'-f','f32le','-'], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).copy()
def rms_env(x, hop=480):                      # 10 ms
    n = len(x)//hop; return np.sqrt((x[:n*hop].reshape(n,hop)**2).mean(1)+1e-12)
def syl(w):                                    # rough syllable weight for Latin captions
    w = re.sub(r'[^a-zA-Z0-9₹]', '', w.lower())
    if not w: return 0.5
    if re.search(r'\d', w): return 2.0 + 0.4*len(w)
    return max(1, len(re.findall(r'[aeiouy]+', w)))
clips, words, t = [], [], 0.25                 # 0.25 s lead-in
GAP = [0.30, 0.36, 0.36, 0.36, 0.34, 0.0]      # pause after each paragraph (s)
for i, (vo, cap) in enumerate(SCRIPT):
    x = load(f'{P}/vo/p{i+1}.wav'); env = rms_env(x); thr = max(env.max()*0.06, 1e-4)
    voiced = np.where(env > thr)[0]; a, b = voiced[0], voiced[-1]+1
    x = x[max(0,a*480-960): min(len(x), b*480+1440)]           # trim silences, keep 20/30 ms pad
    x = np.frombuffer(subprocess.run(['ffmpeg','-v','error','-f','f32le','-ar',str(SR),'-ac','1','-i','-','-af',f'atempo={ATEMPO}',
                      '-f','f32le','-'], input=x.tobytes(), capture_output=True, check=True).stdout, np.float32).copy()
    env = rms_env(x); thr = max(env.max()*0.06, 1e-4); dur = len(x)/SR
    # internal pauses >= 110 ms -> candidate phrase breaks
    quiet = env < thr; pauses = []; s = None
    for k, q in enumerate(np.append(quiet, False)):
        if q and s is None: s = k
        elif not q and s is not None:
            if k - s >= 11 and s > 5 and k < len(env)-5: pauses.append((k - s, s*0.01, k*0.01))
            s = None
    # caption words; a dash is punctuation (a break after the previous word), never a timed word
    raw = cap.split(); capw, brk = [], []
    for w in raw:
        if w == '—':
            if brk: brk[-1] = True
            continue
        capw.append(w); brk.append(bool(re.search(r'[.,?:]$', w)))
    breaks_after = [j for j in range(len(capw) - 1) if brk[j]]
    wts = np.array([syl(w) for w in capw]); cum = np.cumsum(wts) / wts.sum()
    # each break takes the unused pause nearest its expected (syllable-proportional) time, in order
    chosen, used = [], set()
    for j in breaks_after:
        exp_t = cum[j] * dur; best = None
        for k, pz in enumerate(pauses):
            if k in used or (chosen and pz[1] <= chosen[-1][1]): continue
            dd = abs((pz[1] + pz[2]) / 2 - exp_t)
            if best is None or dd < best[0]: best = (dd, k)
        if best is not None and best[0] < 0.9: used.add(best[1]); chosen.append(pauses[best[1]] + (j,))
    bounds = [0.0] + [p for c in chosen for p in (c[1], c[2])] + [dur]
    spans = [(bounds[2*k], bounds[2*k+1]) for k in range(len(bounds)//2)]
    cut = set(c[3] for c in chosen); phrases, cur = [], []
    for j, w in enumerate(capw):
        cur.append(j)
        if j in cut: phrases.append(cur); cur = []
    if cur: phrases.append(cur)
    # unassigned pauses (>=150 ms) inside a phrase split it where the syllable share matches the pause position
    extra = [pz for k, pz in enumerate(pauses) if k not in used and pz[0] >= 15]
    segs = [(ph, s0, s1) for ph, (s0, s1) in zip(phrases, spans)]
    for pz in extra:
        for si, (sp, a, b) in enumerate(segs):
            if len(sp) > 1 and pz[1] > a + 0.12 and pz[2] < b - 0.12:
                ww = np.array([syl(capw[j]) for j in sp]); cum = np.cumsum(ww)[:-1] / ww.sum()
                pos = (pz[1] - a) / ((b - a) - (pz[2] - pz[1])); m = int(np.argmin(abs(cum - pos)))
                if abs(cum[m] - pos) < 0.2: segs[si:si+1] = [(sp[:m+1], a, pz[1]), (sp[m+1:], pz[2], b)]
                break
    phrases, spans = [sg[0] for sg in segs], [(sg[1], sg[2]) for sg in segs]
    for ph, (s0, s1) in zip(phrases, spans):
        ww = np.array([syl(capw[j]) for j in ph]); edges = s0 + (s1-s0)*np.r_[0, np.cumsum(ww)]/ww.sum()
        for j, e0, e1 in zip(ph, edges[:-1], edges[1:]):
            words.append(dict(w=capw[j], t0=round(t+e0,3), t1=round(t+e1,3), p=i, b=int(brk[j])))
    clips.append(dict(i=i, start=round(t,3), dur=round(dur,3), breaks=len(chosen), want=len(breaks_after)))
    subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-', f'{P}/work/p{i+1}_trim.wav'], input=x.tobytes(), check=True)
    t += dur + GAP[i]
total = round(t + 0.7, 3)                       # tail: 0.9 s hold for the loop/end card
# master VO: place clips on a silent bed, then loudnorm (two-pass) to -14 LUFS / -1 dBTP
bed = np.zeros(int(total*SR), np.float32)
for c in clips:
    y = load(f'{P}/work/p{c["i"]+1}_trim.wav'); s = int(c['start']*SR); bed[s:s+len(y)] += y
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','1','-i','-', f'{P}/work/vo_raw.wav'], input=bed.tobytes(), check=True)
m = subprocess.run(['ffmpeg','-hide_banner','-i',f'{P}/work/vo_raw.wav','-af','loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json','-f','null','-'], capture_output=True, text=True).stderr
j = json.loads(m[m.rindex('{'):m.rindex('}')+1])
af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}:"
      f"measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{P}/work/vo_raw.wav','-af',af,'-ar','48000','-ac','2', f'{P}/work/vo_master.wav'], check=True)
chk = subprocess.run(['ffmpeg','-hide_banner','-i',f'{P}/work/vo_master.wav','-af','loudnorm=print_format=json','-f','null','-'], capture_output=True, text=True).stderr
jj = json.loads(chk[chk.rindex('{'):chk.rindex('}')+1])
# per-frame mouth openness (30 fps) from the mastered VO envelope
y = load(f'{P}/work/vo_master.wav'); env = rms_env(y, SR//30); env = env/ (np.percentile(env[env>1e-3], 95)+1e-9)
vis = np.where(env > 0.55, 2, np.where(env > 0.18, 1, 0))
for k in range(1, len(vis)-1):                  # no single-frame flicker
    if vis[k-1] == vis[k+1] != vis[k]: vis[k] = vis[k-1]
json.dump(dict(total=total, clips=clips, words=words, visemes=vis.tolist()), open(f'{P}/work/timeline.json','w'), ensure_ascii=False)
print("clips:", [(c['start'], c['dur'], f"{c['breaks']}/{c['want']}") for c in clips])
print(f"total {total}s | words {len(words)} | VO loudness {jj['input_i']} LUFS, TP {jj['input_tp']} dBTP")
print("sample words:", [(w['w'], w['t0']) for w in words[:8]])
