#!/usr/bin/env python3
"""serve_delivery.py: live download page for a finished episode.

Use it when the workspace file viewer does not show the MP4. The live preview is served
straight from the sandbox, so it does not depend on turn-end snapshots.

  python3 viz/serve_delivery.py --video EP8_1_October_Niyam.mp4 \
          --project projects/ep8_oct_rules --port 8080 [--note "Upload before midnight"]

Routes: /  page (video, download button, copy-ready title/description/pinned comment/hashtags, thumbnails)
        /v/<file>   inline, with HTTP Range support (needed for iPhone/Safari playback and seeking)
        /dl/<file>  forced download (Content-Disposition: attachment)
        /img/<file> thumbnails and the logo
Reads <project>/UPLOAD.md (## Title (chosen), ## Hashtags, ## Pinned comment, ## Upload settings)
and <project>/description.txt. Binds 0.0.0.0. Every request is logged to stdout, so downloads can be verified.
"""
import argparse, glob, html, json, mimetypes, os, re, subprocess, sys
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from urllib.parse import unquote, urlparse

ap = argparse.ArgumentParser()
ap.add_argument('--video', required=True)
ap.add_argument('--project', required=True)
ap.add_argument('--port', type=int, default=8080)
ap.add_argument('--note', default='')
ap.add_argument('--label', default='')
a = ap.parse_args()

VIDEO = os.path.abspath(a.video)
PROJ = os.path.abspath(a.project)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))          # /home/user
if not os.path.isfile(VIDEO):
    sys.exit(f'video not found: {VIDEO}')

FILES = {os.path.basename(VIDEO): VIDEO}
THUMBS = sorted(glob.glob(os.path.join(PROJ, 'thumbs', '*.jpg')))   # ascending: 1080x1920 (narrow column) before 1280x720
for p in THUMBS:
    FILES[os.path.basename(p)] = p
for extra in ('description.txt', 'UPLOAD.md'):
    p = os.path.join(PROJ, extra)
    if os.path.isfile(p):
        FILES[extra] = p
LOGO = os.path.join(ROOT, 'brand', 'logo.png')
if os.path.isfile(LOGO):
    FILES['logo.png'] = LOGO


def probe(path):
    try:
        out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration:stream=width,height',
                              '-of', 'json', path], capture_output=True, text=True, timeout=20).stdout
        j = json.loads(out)
        st = next((s for s in j.get('streams', []) if s.get('width')), {})
        return float(j['format']['duration']), st.get('width'), st.get('height')
    except Exception:
        return None, None, None


DUR, W, H = probe(VIDEO)


def sections(md):
    out, cur = {}, None
    for line in md.splitlines():
        if line.startswith('## '):
            cur = line[3:].strip().lower()
            out[cur] = []
        elif cur is not None:
            out[cur].append(line)
    return out


def clean(s):
    return re.sub(r'[`*]', '', s).strip()


def pack():
    up = open(FILES['UPLOAD.md'], encoding='utf-8').read() if 'UPLOAD.md' in FILES else ''
    sec = sections(up)
    first = lambda key: next((clean(l) for l in next((v for k, v in sec.items() if k.startswith(key)), []) if l.strip()), '')
    block = lambda key: '\n'.join(l.strip() for l in next((v for k, v in sec.items() if k.startswith(key)), []) if l.strip())
    settings = [clean(l.lstrip('- ')) for l in next((v for k, v in sec.items() if k.startswith('upload settings')), [])
                if l.strip().startswith('-')]
    desc = open(FILES['description.txt'], encoding='utf-8').read().strip() if 'description.txt' in FILES else ''
    return {'title': first('title'), 'desc': desc, 'pinned': block('pinned comment'),
            'tags': first('hashtags'), 'settings': settings}


def aspect(t):
    m = re.search(r'(\d+)x(\d+)', os.path.basename(t))
    return ('9:16' if int(m.group(1)) < int(m.group(2)) else '16:9') if m else 'image'


def page(host):
    p = pack()
    name = os.path.basename(VIDEO)
    mb = os.path.getsize(VIDEO) / 1e6
    meta = ' · '.join(x.replace(' ', '\u00a0') for x in [f'{W}×{H}' if W else '', f'{DUR:.1f} s' if DUR else '', f'{mb:.1f} MB', 'H.264 + AAC'] if x)
    big = next((os.path.basename(t) for t in THUMBS if '1080x1920' in t), os.path.basename(THUMBS[0]) if THUMBS else '')
    e = html.escape

    def box(key, label, text):
        rows = min(18, max(2, text.count('\n') + 1 + len(text) // 60))
        return (f'<section class="box"><div class="bh"><h2>{label}</h2>'
                f'<button class="cp" onclick="cp(\'{key}\',this)">Copy</button></div>'
                f'<textarea id="{key}" readonly rows="{rows}">{e(text)}</textarea></section>')

    thumbs = ''.join(
        f'<figure><img src="img/{e(os.path.basename(t))}" alt="thumbnail">'
        f'<a class="btn ghost" href="dl/{e(os.path.basename(t))}" download>Download {aspect(t)}</a></figure>'
        for t in THUMBS)
    settings = ''.join(f'<li>{e(s)}</li>' for s in p['settings'])
    logo = '<img class="logo" src="img/logo.png" alt="">' if 'logo.png' in FILES else ''
    note = f'<p class="note">{e(a.note)}</p>' if a.note else ''
    # NOTE: the raw e2b URL answers 403 outside the platform preview (sandbox has a traffic-access token),
    # so never print it for the user. Offer the player's own save option instead.
    newtab = ('<p class="small">If the button doesn\'t start a download in this panel, play the video and use the player\'s '
              '⋮ menu → Download (Chrome/Android), or long-press the video → Save video.</p>')
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(a.label or name)} · download</title>
<style>
:root{{--ink:#15171a;--mute:#5d6167;--line:#dedbd3;--paper:#f6f5f1;--card:#fff;--acc:#0e1726;--hi:#ffd60a}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.45 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}}
main{{max-width:760px;margin:0 auto;padding:20px 16px 48px}}
header{{display:flex;align-items:center;gap:10px;margin-bottom:14px}}
.logo{{width:34px;height:34px;border-radius:8px;object-fit:cover}}
.brand{{font-weight:700;letter-spacing:.04em;font-size:13px;text-transform:uppercase;color:var(--mute)}}
h1{{font-size:22px;line-height:1.25;margin:2px 0 6px}}
.meta{{color:var(--mute);font-size:14px;margin:0 0 12px}}
.note{{display:inline-block;background:var(--hi);color:#111;font-weight:600;padding:6px 10px;border-radius:6px;margin:0 0 14px;font-size:14px}}
.player{{display:flex;justify-content:center;background:#0b0d10;border-radius:14px;padding:10px;margin-bottom:12px}}
video{{height:min(70vh,760px);aspect-ratio:9/16;max-width:100%;border-radius:8px;background:#000}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:8px;text-decoration:none;font-weight:700;
     border-radius:10px;padding:14px 18px;background:var(--acc);color:#fff;border:0;font-size:16px}}
.btn.main{{width:100%;font-size:18px;padding:16px}}
.btn.ghost{{background:transparent;color:var(--acc);border:1.5px solid var(--acc);padding:9px 12px;font-size:14px}}
.small{{font-size:13px;color:var(--mute)}}
.box{{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 12px 10px;margin:14px 0}}
.bh{{display:flex;align-items:center;justify-content:space-between;margin-bottom:8px}}
h2{{font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:var(--mute);margin:0}}
.cp{{font:600 14px system-ui,sans-serif;background:var(--acc);color:#fff;border:0;border-radius:8px;padding:8px 14px;min-width:92px}}
textarea{{width:100%;border:0;resize:none;overflow:hidden;font:15px/1.45 system-ui,sans-serif;color:var(--ink);background:transparent;padding:0}}
.thumbs{{display:grid;grid-template-columns:1fr 1.5fr;gap:12px;align-items:start}}
figure .btn{{padding:8px 6px;font-size:13px;white-space:nowrap}}
figure{{margin:0;display:flex;flex-direction:column;gap:8px}}
figure img{{width:100%;border-radius:8px;border:1px solid var(--line)}}
ul{{margin:6px 0 0;padding-left:20px}} li{{margin:3px 0}}
</style></head><body><main>
<header>{logo}<span class="brand">Benaqaab India · upload pack</span></header>
<h1>{e(p["title"] or name)}</h1>
<p class="meta">{e(name)} · {e(meta)}</p>
{note}
<div class="player"><video src="v/{e(name)}" controls playsinline preload="metadata"{f' poster="img/{e(big)}"' if big else ''}></video></div>
<a class="btn main" href="dl/{e(name)}" download="{e(name)}">⬇ Download video ({mb:.1f} MB)</a>
{newtab}
{box("t", "Title", p["title"])}
{box("d", "Description", p["desc"])}
{box("c", "Pinned comment", p["pinned"])}
{box("h", "Hashtags", p["tags"])}
<section class="box"><div class="bh"><h2>Thumbnails</h2></div><div class="thumbs">{thumbs}</div></section>
{f'<section class="box"><div class="bh"><h2>Upload settings</h2></div><ul>{settings}</ul></section>' if settings else ''}
</main>
<script>
function fit(){{document.querySelectorAll('textarea').forEach(t=>{{t.style.height='auto';t.style.height=(t.scrollHeight+2)+'px';}});}}
addEventListener('load',fit);addEventListener('resize',fit);fit();
async function cp(id,btn){{
  const ta=document.getElementById(id);let ok=false;
  try{{await navigator.clipboard.writeText(ta.value);ok=true;}}catch(e){{}}
  if(!ok){{ta.focus();ta.select();ta.setSelectionRange(0,ta.value.length);try{{ok=document.execCommand('copy');}}catch(e){{}}}}
  btn.textContent=ok?'Copied ✓':'Selected';setTimeout(()=>btn.textContent='Copy',1800);
}}
</script></body></html>'''


class Handler(BaseHTTPRequestHandler):
    server_version = 'delivery/1.0'

    def log_message(self, fmt, *args):
        sys.stdout.write('%s %s range=%s\n' % (self.address_string(), fmt % args, self.headers.get('Range', '-')))
        sys.stdout.flush()

    def do_HEAD(self):
        self.do_GET()

    def do_GET(self):
        path = unquote(urlparse(self.path).path)
        if path in ('/', '/index.html'):
            body = page(self.headers.get('Host', '')).encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-cache')
            self.end_headers()
            if self.command != 'HEAD':
                self.wfile.write(body)
            return
        if path == '/healthz':
            body = b'ok\n'
            self.send_response(200); self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', str(len(body))); self.end_headers()
            if self.command != 'HEAD':
                self.wfile.write(body)
            return
        m = re.match(r'^/(v|dl|img)/([^/]+)$', path)
        if not m or m.group(2) not in FILES:
            self.send_error(404)
            return
        self.send_file(FILES[m.group(2)], attachment=(m.group(1) == 'dl'))

    def send_file(self, fp, attachment=False):
        size = os.path.getsize(fp)
        ctype = mimetypes.guess_type(fp)[0] or 'application/octet-stream'
        if fp.endswith('.md') or fp.endswith('.txt'):
            ctype = 'text/plain; charset=utf-8'
        start, end, status = 0, size - 1, 200
        rng = self.headers.get('Range')
        if rng:
            mm = re.match(r'^\s*bytes=(\d*)-(\d*)\s*$', rng)
            if mm and (mm.group(1) or mm.group(2)):
                s, t = mm.groups()
                if s == '':
                    start = max(0, size - int(t))
                else:
                    start = int(s)
                    end = min(int(t), size - 1) if t else size - 1
                if start >= size or start > end:
                    self.send_response(416)
                    self.send_header('Content-Range', f'bytes */{size}')
                    self.send_header('Content-Length', '0')
                    self.end_headers()
                    return
                status = 206
        length = end - start + 1
        self.send_response(status)
        self.send_header('Content-Type', ctype)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(length))
        if status == 206:
            self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        if attachment:
            self.send_header('Content-Disposition', f'attachment; filename="{os.path.basename(fp)}"')
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()
        if self.command == 'HEAD':
            return
        with open(fp, 'rb') as f:
            f.seek(start)
            left = length
            while left > 0:
                chunk = f.read(min(256 * 1024, left))
                if not chunk:
                    break
                try:
                    self.wfile.write(chunk)
                except (BrokenPipeError, ConnectionResetError):
                    return
                left -= len(chunk)


if __name__ == '__main__':
    srv = ThreadingHTTPServer(('0.0.0.0', a.port), Handler)
    srv.daemon_threads = True
    sid = os.environ.get('E2B_SANDBOX_ID', '')
    print(f'[delivery] serving {os.path.basename(VIDEO)} ({os.path.getsize(VIDEO)/1e6:.1f} MB) + {len(THUMBS)} thumbs on 0.0.0.0:{a.port}'
          + (f'  →  https://{a.port}-{sid}.e2b.app/' if sid else ''), flush=True)
    srv.serve_forever()
