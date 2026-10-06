#!/usr/bin/env python3
"""Build the full workspace zip for handover to another AI.

Includes: every text/code/skill/research/tool/brand/project source file.
Excludes on purpose: rendered MP4s (heavy, and an AI cannot watch them — the delivered film stays
in the workspace at projects/anime_edit/Anime_Edit.mp4), .cache scratch, __pycache__, and the two
older backup archives (redundant here, still downloadable separately in the workspace).
Writes a manifest with sizes + SHA-256 for every included file.
"""
import hashlib, json, pathlib, zipfile

ROOT = pathlib.Path('/home/user')
OUT = ROOT / 'BENAQAAB_WORKSPACE_FULL_2026-10-04.zip'
SKIP_DIRS = {'.cache', '__pycache__', 'node_modules', '.venv', 'dist', 'build', 'out', 'target',
             '.arena', '.npm', '.config', '.local'}
SKIP_SUFFIX = {'.mp4', '.mov', '.mkv', '.webm'}
SKIP_NAMES = {'WORKSPACE_TEXT_BACKUP.zip', 'WORKSPACE_TEXT_BACKUP_2026-10-04.zip',
              'BENAQAAB_COMPLETE_BACKUP_2026-10-04.zip', OUT.name}

def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()

files, skipped = [], []
for p in sorted(ROOT.rglob('*')):
    if p.is_dir():
        continue
    rel = p.relative_to(ROOT)
    if any(part in SKIP_DIRS for part in rel.parts):
        skipped.append((rel.as_posix(), 'cache/scratch')); continue
    if p.suffix.lower() in SKIP_SUFFIX:
        skipped.append((rel.as_posix(), 'video (kept in workspace separately)')); continue
    if p.name in SKIP_NAMES:
        skipped.append((rel.as_posix(), 'older backup archive')); continue
    files.append(p)

manifest = {
    'what': 'Benaqaab India video-production workspace — full handover package for an AI agent',
    'created': '2026-10-04',
    'read_first': ['START_HERE.md', 'BENAQAAB_AI_AGENT_COMPACT.md',
                   'BENAQAAB_AI_AGENT_MASTER_SKILL.md (look up by §INDEX, do not read linearly)'],
    'counts': {'files': len(files)}, 'sizes': {}, 'sha256': {},
    'excluded': sorted({r for r, why in skipped}),
}
total = 0
with zipfile.ZipFile(OUT, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in files:
        rel = p.relative_to(ROOT).as_posix()
        z.write(p, rel)
        n = p.stat().st_size
        total += n
        manifest['sizes'][rel] = n
        manifest['sha256'][rel] = sha(p)
    z.writestr('_ZIP_MANIFEST.json', json.dumps(manifest, indent=1, ensure_ascii=False))

print(f'zip: {OUT.name}')
print(f'  files included : {len(files)}')
print(f'  raw size       : {total/1024/1024:.1f} MB')
print(f'  zip size       : {OUT.stat().st_size/1024/1024:.1f} MB')
print(f'  excluded       : {len(manifest["excluded"])} files (videos + old backups + caches)')
