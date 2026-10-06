#!/usr/bin/env python3
# Benaqaab — tiny static server (Range-capable) for /home/user/VIDEOS · binds 0.0.0.0:8000
import http.server, os, re, urllib.parse, socketserver

ROOT = '/home/user/VIDEOS'
CT = {'.mp4': 'video/mp4', '.html': 'text/html; charset=utf-8', '.jpg': 'image/jpeg',
      '.png': 'image/png', '.txt': 'text/plain; charset=utf-8', '.srt': 'text/plain; charset=utf-8'}

class H(http.server.BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'
    def log_message(self, *a):
        pass
    def _target(self):
        p = urllib.parse.unquote(self.path.split('?')[0])
        if p == '/' or p == '':
            p = '/index.html'
        fp = os.path.abspath(os.path.join(ROOT, p.lstrip('/')))
        return fp
    def do_GET(self):
        fp = self._target()
        if not fp.startswith(ROOT) or not os.path.isfile(fp):
            self.send_error(404); return
        size = os.path.getsize(fp)
        ctype = CT.get(os.path.splitext(fp)[1].lower(), 'application/octet-stream')
        start, end, code = 0, size - 1, 200
        rng = self.headers.get('Range')
        if rng:
            m = re.match(r'bytes=(\d*)-(\d*)$', rng.strip())
            if m and (m.group(1) or m.group(2)):
                if m.group(1): start = int(m.group(1))
                if m.group(2): end = min(int(m.group(2)), size - 1)
                if start > end or start >= size:
                    self.send_response(416)
                    self.send_header('Content-Range', f'bytes */{size}')
                    self.end_headers(); return
                code = 206
        length = end - start + 1
        self.send_response(code)
        self.send_header('Content-Type', ctype)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(length))
        self.send_header('Cache-Control', 'no-store')
        if code == 206:
            self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.end_headers()
        with open(fp, 'rb') as f:
            f.seek(start)
            rem = length
            while rem > 0:
                chunk = f.read(min(65536, rem))
                if not chunk: break
                try:
                    self.wfile.write(chunk)
                except (BrokenPipeError, ConnectionResetError):
                    return
                rem -= len(chunk)
    def do_HEAD(self):
        fp = self._target()
        if not fp.startswith(ROOT) or not os.path.isfile(fp):
            self.send_error(404); return
        self.send_response(200)
        self.send_header('Content-Type', CT.get(os.path.splitext(fp)[1].lower(), 'application/octet-stream'))
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(os.path.getsize(fp)))
        self.end_headers()

class S(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == '__main__':
    with S(('0.0.0.0', 8000), H) as srv:
        print('[serve] VIDEOS player on http://0.0.0.0:8000/', flush=True)
        srv.serve_forever()
