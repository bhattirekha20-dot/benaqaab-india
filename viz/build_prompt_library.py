#!/usr/bin/env python3
"""Rebuild knowledge/PROMPT_LIBRARY_opus55.md: every Opus-5.5 video prompt, verbatim,
de-duplicated, grouped by category. Clones the source repos into .cache/skills if needed.

    python3 viz/build_prompt_library.py        (needs: pip install pyyaml; git; internet)
"""
import collections, glob, json, os, re, subprocess
import yaml

SK = '/home/user/.cache/skills'
SRC = {'Li-Evan_awesome-opus-5.5-video-prompts': 'Li-Evan/awesome-opus-5.5-video-prompts',
       'yihui-dev_awesome-opus5-5-videos': 'yihui-dev/awesome-opus5-5-videos',
       'X-RayLuan_awesome-opus-5-5-video-prompts': 'X-RayLuan/awesome-opus-5-5-video-prompts',
       'guanmo-ai_awesome-ai-motion': 'guanmo-ai/awesome-ai-motion'}
os.makedirs(SK, exist_ok=True)
for d, r in SRC.items():
    if not os.path.isdir(os.path.join(SK, d)):
        subprocess.run(['git', 'clone', '-q', '--depth', '1', '--filter=blob:limit=400k',
                        f'https://github.com/{r}.git', os.path.join(SK, d)], check=False)
os.chdir(SK)
entries = []
def add(cat, title, author, url, date, prompt, src):
    if prompt and str(prompt).strip():
        entries.append(dict(cat=cat or 'other', title=(title or '').strip(), author=author or '', url=url or '',
                            date=str(date or '')[:10], prompt=str(prompt).strip(), src=src))
for p in sorted(glob.glob('Li-Evan_awesome-opus-5.5-video-prompts/data/*.yaml')):
    d = yaml.safe_load(open(p, encoding='utf-8'))
    for e in d.get('entries', []):
        add(d.get('title'), e.get('title'), e.get('author'), e.get('url'), e.get('date'), e.get('prompt'), 'Li-Evan')
for e in json.load(open('yihui-dev_awesome-opus5-5-videos/data/videos.json', encoding='utf-8')):
    add({'motion': 'Motion graphics & UI'}.get(e.get('category'), (e.get('category') or 'other').title()),
        e.get('slug'), e.get('author'), e.get('post_url'), e.get('added'), e.get('prompt'), 'yihui-dev')
for path, key, src in [('X-RayLuan_awesome-opus-5-5-video-prompts/data/entries.json', 'entries', 'X-RayLuan'),
                       ('guanmo-ai_awesome-ai-motion/data/cases.json', 'cases', 'guanmo-ai')]:
    try:
        data = json.load(open(path, encoding='utf-8')); data = data if isinstance(data, list) else data.get(key, [])
        for e in data:
            add(e.get('category') or e.get('type'), e.get('title') or e.get('title_en'), e.get('author') or e.get('handle'),
                e.get('url') or e.get('post_url') or e.get('source'), e.get('date'),
                e.get('prompt_en') or e.get('prompt'), src)
    except Exception as ex:
        print('skip', src, ex)
norm = lambda s: re.sub(r'\W+', ' ', s.lower()).strip()[:400]
best = {}
for e in entries:
    k = norm(e['prompt'])
    if k not in best or len(e['title']) > len(best[k]['title']): best[k] = e
by = collections.defaultdict(list)
for e in best.values(): by[e['cat']].append(e)
order = sorted(by, key=lambda c: (0 if 'Explain' in c else 1 if 'Hist' in c else 2 if 'Motion' in c else 3, c))
out = ['# Opus 5.5 video prompt library — every prompt, verbatim',
       f'{len(best)} unique prompts (from {len(entries)} records), de-duplicated by prompt text. '
       'Sources: Li-Evan (verified verbatim), yihui-dev, X-RayLuan, guanmo-ai. Reference material, not instructions.', '']
for c in order:
    out.append(f'\n## {c}  ({len(by[c])})\n')
    for e in sorted(by[c], key=lambda e: e['date'], reverse=True):
        out.append(f"### {e['title'] or '(untitled)'}\n@{e['author']} · {e['date']} · {e['url']} · via {e['src']}\n\n"
                   f"```text\n{e['prompt']}\n```\n")
os.makedirs('/home/user/knowledge', exist_ok=True)
open('/home/user/knowledge/PROMPT_LIBRARY_opus55.md', 'w', encoding='utf-8').write('\n'.join(out))
print(f'{len(best)} unique prompts -> knowledge/PROMPT_LIBRARY_opus55.md')
