# YouTube captions (.srt) from an aligned timeline.json (words + optional ext_words). Balanced lines (DP), <= MAXC chars.
# usage: python3 viz/recipes/make_srt.py projects/<ep>/work/timeline.json projects/<ep>/captions.srt
import json, math, sys
TL = json.load(open(sys.argv[1])); OUT = sys.argv[2]; MAXC = 38
def ts(t):
    ms = int(round(max(0, t) * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
words = [dict(w=w['w'], t0=w['t0'], t1=w['t1'], b=w['b'], g=('p', w['p'])) for w in TL['words']]
words += [dict(w=w['w'], t0=w['t0'], t1=w['t1'], b=w['b'], g=('x', w['seg'])) for w in TL.get('ext_words', [])]
words.sort(key=lambda w: w['t0'])
phrases, cur = [], []
for i, w in enumerate(words):
    cur.append(w); nxt = words[i + 1] if i + 1 < len(words) else None
    if w['b'] or nxt is None or nxt['g'] != w['g']: phrases.append(cur); cur = []
cues = []
for ph in phrases:
    L = [len(w['w']) for w in ph]; n = len(ph); span = lambda i, j: sum(L[i:j]) + (j - i - 1)
    k = max(1, math.ceil(span(0, n) / MAXC)); best = [[(1e9, -1)] * (k + 1) for _ in range(n + 1)]; best[0][0] = (0, -1)
    for j in range(1, k + 1):
        for i in range(1, n + 1):
            for m in range(j - 1, i):
                c = max(best[m][j - 1][0], span(m, i))
                if c < best[i][j][0]: best[i][j] = (c, m)
    cuts = []; i = n
    for j in range(k, 0, -1): m = best[i][j][1]; cuts.insert(0, (m, i)); i = m
    cues += [ph[a:b] for a, b in cuts]
out = []
for idx, c in enumerate(cues):
    start = c[0]['t0']; end = c[-1]['t1'] + 0.3
    if idx + 1 < len(cues): end = min(end, cues[idx + 1][0]['t0'] - 0.04)
    out.append(f"{idx + 1}\n{ts(start)} --> {ts(end)}\n{' '.join(x['w'] for x in c)}\n")
open(OUT, 'w').write('\n'.join(out)); print(len(out), 'cues ->', OUT)
