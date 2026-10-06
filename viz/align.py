#!/usr/bin/env python3
"""Word-accurate caption timing for Hinglish/Hindi/English VO.

faster-whisper (word timestamps) transcribes each VO clip; a DP sequence alignment maps the
recognised words (often Devanagari, even for English loanwords) onto the *script's* caption words
(Latin Hinglish) using a rough Devanagari->Latin transliteration + fuzzy match. Handles 1:1, 1:2, 1:3
(one caption word = several recognised words, e.g. '115' -> 'एक सौ पंद्रह'), 2:1 (two caption words
heard as one, e.g. 'mat dijiye' -> 'मद्धीजे'), and skips on either side.

Usage (rewrites words[].t0/t1 in timeline.json and writes timeline.js next to it):
  python3 viz/align.py projects/<ep>/build/timeline.json --clips 'projects/<ep>/build/p{n}_trim.wav'
timeline.json needs: clips[i].start (clip offset in the master), words[] with w, p (clip index).
Note: PyAV in this env rejects faster-whisper's decoder kwargs, so audio is decoded with ffmpeg here.
"""
import argparse, difflib, json, os, re, subprocess, sys
import numpy as np

CONS = {'क':'k','ख':'kh','ग':'g','घ':'gh','ङ':'n','च':'ch','छ':'chh','ज':'j','झ':'jh','ञ':'n','ट':'t','ठ':'th','ड':'d','ढ':'dh',
        'ण':'n','त':'t','थ':'th','द':'d','ध':'dh','न':'n','प':'p','फ':'f','ब':'b','भ':'bh','म':'m','य':'y','र':'r','ल':'l','व':'v',
        'श':'sh','ष':'sh','स':'s','ह':'h','क़':'k','ख़':'kh','ग़':'g','ज़':'z','फ़':'f','ड़':'r','ढ़':'rh','ळ':'l'}
MATRA = {'ा':'a','ि':'i','ी':'i','ु':'u','ू':'u','े':'e','ै':'ai','ो':'o','ौ':'au','ृ':'ri','ॅ':'e','ॉ':'o'}
VOW = {'अ':'a','आ':'a','इ':'i','ई':'i','उ':'u','ऊ':'u','ए':'e','ऐ':'ai','ओ':'o','औ':'au','ऋ':'ri','ऑ':'o'}
NUKTA, VIRAMA, NASAL = '़', '्', 'ंँ'
DIG = str.maketrans('०१२३४५६७८९', '0123456789')

def translit(s):
    s = s.translate(DIG); out = []; i = 0
    while i < len(s):
        c = s[i]; c2 = s[i:i+2]
        if c2 in CONS and len(c2) == 2: c = c2; i += 1
        if c in CONS:
            out.append(CONS[c]); nxt = s[i+1] if i + 1 < len(s) else ''
            if nxt == NUKTA: i += 1; nxt = s[i+1] if i + 1 < len(s) else ''
            if nxt in MATRA: out.append(MATRA[nxt]); i += 1
            elif nxt == VIRAMA: i += 1
            elif nxt and (nxt in CONS or nxt in NASAL): out.append('a')
        elif c in VOW: out.append(VOW[c])
        elif c in NASAL: out.append('n')
        elif c in MATRA: out.append(MATRA[c])
        else: out.append(c)
        i += 1
    return ''.join(out)

def norm(s):
    s = translit(s).lower()
    s = re.sub(r'[^a-z0-9]', '', s)
    for a, b in (('ph', 'f'), ('w', 'v'), ('c', 'k'), ('q', 'k'), ('x', 'ks'), ('z', 'j'), ('ee', 'i'), ('oo', 'u'), ('y', 'i')):
        s = s.replace(a, b)
    return re.sub(r'(.)\1+', r'\1', s)

def sim(a, b):
    a, b = norm(a), norm(b)
    if not a or not b: return 0.0
    sk = lambda x: re.sub(r'[aeiou]', '', x) or x
    return max(difflib.SequenceMatcher(None, a, b).ratio(), 0.9 * difflib.SequenceMatcher(None, sk(a), sk(b)).ratio())

def dp_align(cap, rec):
    """cap: caption strings; rec: [(word, t0, t1)]. Returns per-caption (t0, t1) or None."""
    n, m = len(cap), len(rec); INF = 1e9
    D = np.full((n + 1, m + 1), INF); B = {}
    D[0, 0] = 0
    SKIP_REC, SKIP_CAP = 0.7, 0.9
    for i in range(n + 1):
        for j in range(m + 1):
            if D[i, j] >= INF: continue
            base = D[i, j]
            def relax(ii, jj, cost, op):
                if ii <= n and jj <= m and base + cost < D[ii, jj]: D[ii, jj] = base + cost; B[(ii, jj)] = (i, j, op)
            if i < n and j < m:
                relax(i + 1, j + 1, 1 - sim(cap[i], rec[j][0]), '11')
                for k in (2, 3):
                    if j + k <= m: relax(i + 1, j + k, 1 - sim(cap[i], ''.join(r[0] for r in rec[j:j + k])) + 0.1 * (k - 1), f'1{k}')
                if i + 2 <= n: relax(i + 2, j + 1, 1 - sim(cap[i] + cap[i + 1], rec[j][0]) + 0.1, '21')
            if j < m: relax(i, j + 1, SKIP_REC, 'sr')
            if i < n: relax(i + 1, j, SKIP_CAP, 'sc')
    out = [None] * n; i, j = n, m
    while (i, j) != (0, 0):
        pi, pj, op = B[(i, j)]
        if op in ('11', '12', '13'):
            out[pi] = (rec[pj][1], rec[j - 1][2], sim(cap[pi], ''.join(r[0] for r in rec[pj:j])))
        if op == '21':
            w, t0, t1 = rec[pj]; la, lb = max(1, len(norm(cap[pi]))), max(1, len(norm(cap[pi + 1])))
            mid = t0 + (t1 - t0) * la / (la + lb); sm = sim(cap[pi] + cap[pi + 1], w)
            out[pi] = (t0, mid, sm); out[pi + 1] = (mid, t1, sm)
        i, j = pi, pj
    return out, D[n, m] / max(1, n)

ACR = {'LPG': 3, 'SBI': 3, 'ATM': 3, 'GST': 3, 'UPI': 3, 'DM': 2, 'SDM': 3, 'NPS': 3, 'KYC': 3, 'RBI': 3, 'NPCI': 4,
       'OTP': 3, 'PAN': 1, 'SIM': 1, 'AI': 2, 'EMI': 3, 'ITR': 3, 'TDS': 3, 'PMUY': 4, 'OMC': 3, 'ISRO': 2, 'I4C': 3}

def syl(w):
    k = re.sub(r'[^A-Za-z0-9]', '', w)
    if k in ACR: return ACR[k]                      # letters are spoken one by one ("el-pee-jee")
    w = norm(w)
    if re.search(r'\d', w): return 2.0 + 0.4 * len(w)
    return max(1, len(re.findall(r'[aeiou]+', w)))

def pauses_of(path, off, min_len=0.11):
    x = pcm16k(path); hop = 160
    env = np.sqrt(np.convolve(x ** 2, np.ones(480) / 480, 'same')[::hop] + 1e-12)
    thr = max(env.max() * 0.06, 1e-4); q = env < thr; out = []; st = None
    for k, v in enumerate(np.append(q, False)):
        if v and st is None: st = k
        elif not v and st is not None:
            if (k - st) * 0.01 >= min_len and st > 5 and k < len(env) - 5: out.append((off + st * 0.01, off + k * 0.01))
            st = None
    return out

def snap(words, idx, out, P, clip0, clip1, MIN_SIM=0.4):
    """Hard phrase boundaries = real pauses at punctuation; inside a phrase, confident whisper starts are
    anchors and the rest are placed by syllable share between anchors."""
    n = len(idx); cap = [words[k]['w'] for k in idx]
    rel = [o is not None and o[2] >= MIN_SIM for o in out]
    bounds, used = {}, set()
    for q in range(n - 1):
        if not words[idx[q]].get('b'): continue
        cand = [v for v in ((out[q][1] if out[q] else None), (out[q + 1][0] if out[q + 1] else None)) if v is not None]
        if not cand: continue
        tg = sum(cand) / len(cand)
        best = min(((max(0.0, s0 - tg, tg - e0), k) for k, (s0, e0) in enumerate(P) if k not in used), default=None)
        if best and best[0] < 0.6: used.add(best[1]); bounds[q] = P[best[1]]
    free = [p for k, p in enumerate(P) if k not in used and p[1] - p[0] >= 0.15]
    res = [None] * n; qa = 0
    for q in range(n):
        if not (q in bounds or q == n - 1): continue
        seg = list(range(qa, q + 1)); t_s = bounds[qa - 1][1] if qa - 1 in bounds else clip0
        t_e = bounds[q][0] if q in bounds else clip1
        st = [None] * len(seg); st[0] = t_s
        for r, qq in enumerate(seg[1:], 1):
            if rel[qq]:
                t0 = out[qq][0]
                for (p0, p1) in free:
                    if p0 <= t0 < p1: t0 = p1
                if t_s < t0 < t_e - 0.06: st[r] = t0
        # drop implausible anchors: a word may not get < 40% of its syllable-share of the phrase (or < 60 ms)
        wts = [syl(cap[qq]) for qq in seg]; tot_w = sum(wts); dur = max(1e-3, t_e - t_s)
        ex = [t_s + dur * sum(wts[:r]) / tot_w for r in range(len(seg))] + [t_e]
        last = 0
        for r in range(1, len(st)):
            if st[r] is None: continue
            if st[r] - st[last] < max(0.06 * (r - last), 0.4 * (ex[r] - ex[last])): st[r] = None
            else: last = r
        nxt = len(seg); nxt_t = t_e                                   # backward pass: room left for the words after
        for r in range(len(seg) - 1, 0, -1):
            if st[r] is None: continue
            if nxt_t - st[r] < max(0.06 * (nxt - r), 0.4 * (ex[nxt] - ex[r])): st[r] = None
            else: nxt, nxt_t = r, st[r]
        st.append(t_e); wts.append(0)
        r = 0
        while r < len(seg):
            if st[r] is not None: r += 1; continue
            L = r - 1; R = next(k for k in range(r, len(st)) if st[k] is not None)
            tot = sum(wts[L:R])
            for k in range(r, R): st[k] = st[L] + (st[R] - st[L]) * sum(wts[L:k]) / tot
            r = R
        for r, qq in enumerate(seg): res[qq] = (st[r], st[r + 1] if r + 1 < len(seg) else t_e)
        qa = q + 1
    return res

def pcm16k(path):
    return np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'],
                                        capture_output=True, check=True).stdout, np.float32).copy()

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('timeline'); ap.add_argument('--clips', required=True)
    ap.add_argument('--model', default='small'); ap.add_argument('--lang', default='hi')
    a = ap.parse_args()
    model = None                                     # loaded lazily: cached clips need no model at all
    cache_path = os.path.join(os.path.dirname(os.path.abspath(a.timeline)), 'whisper_words.json')
    cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}
    TL = json.load(open(a.timeline)); words = TL['words']; report = []
    for c in TL['clips']:
        i, off = c['i'], c['start']
        clip = a.clips.format(n=i + 1); st_ = os.stat(clip); key = f'{os.path.basename(clip)}:{st_.st_size}:{int(st_.st_mtime)}:{a.model}'
        if key in cache:
            rec = [(w, t0 + off, t1 + off) for w, t0, t1 in cache[key]]
        else:
            if model is None:
                from faster_whisper import WhisperModel
                model = WhisperModel(a.model, device='cpu', compute_type='int8', download_root='/home/user/.cache/whisper')
            segs, _ = model.transcribe(pcm16k(clip), language=a.lang, word_timestamps=True, beam_size=5)
            raw = [(w.word.strip(), w.start, w.end) for s in segs for w in s.words if w.word.strip()]
            cache[key] = raw; json.dump(cache, open(cache_path, 'w'), ensure_ascii=False)
            rec = [(w, t0 + off, t1 + off) for w, t0, t1 in raw]
        idx = [k for k, w in enumerate(words) if w['p'] == i]; cap = [words[k]['w'] for k in idx]
        out, cost = dp_align(cap, rec)
        timed = snap(words, idx, out, pauses_of(a.clips.format(n=i + 1), off), off, off + c['dur'])
        for k, (t0, t1) in zip(idx, timed): words[k]['t0'], words[k]['t1'] = round(t0, 3), round(t1, 3)
        report.append((i + 1, round(cost, 3), ' '.join(r[0] for r in rec)))
        print(f'P{i+1} cost {cost:.2f} | heard: ' + ' '.join(r[0] for r in rec))
        print('      ' + ' '.join(f"{words[k]['w']}@{words[k]['t0']:.2f}" for k in idx))
    TL['aligned'] = 'whisper-' + a.model
    json.dump(TL, open(a.timeline, 'w'), ensure_ascii=False)
    open(a.timeline[:-5] + '.js', 'w').write('window.__TL = ' + json.dumps(TL, ensure_ascii=False) + ';\n')
    bad = [r for r in report if r[1] > 0.55]
    if bad: print('WARN high alignment cost (check captions vs VO):', [(b[0], b[1]) for b in bad]); sys.exit(2)

if __name__ == '__main__':
    main()
