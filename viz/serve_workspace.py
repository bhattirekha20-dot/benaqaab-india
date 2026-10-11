#!/usr/bin/env python3
"""
Benaqaab India - High-Performance Range-Capable Static Media Server
Supports HTTP 206 Partial Content for instant audio/video seeking in Chromium/Safari.
"""
import http.server
import os
import re
import socketserver
import sys
import urllib.parse

WORKSPACE_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8765

MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.mp3': 'audio/mpeg',
    '.wav': 'audio/wav',
    '.mp4': 'video/mp4',
    '.webm': 'video/webm',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.webp': 'image/webp',
    '.svg': 'image/svg+xml',
    '.txt': 'text/plain; charset=utf-8'
}

class RangeRequestHandler(http.server.BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.1'

    def log_message(self, format, *args):
        # Concise logging
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")

    def _get_file_path(self):
        clean_path = urllib.parse.unquote(self.path.split('?')[0])
        if clean_path.startswith('/'):
            clean_path = clean_path[1:]
        abs_path = os.path.abspath(os.path.join(WORKSPACE_ROOT, clean_path))
        if os.path.isdir(abs_path):
            index_path = os.path.join(abs_path, 'index.html')
            if os.path.isfile(index_path):
                return index_path
        return abs_path

    def do_HEAD(self):
        fp = self._get_file_path()
        if not fp.startswith(WORKSPACE_ROOT) or not os.path.isfile(fp):
            self.send_error(404, "File not found")
            return
        size = os.path.getsize(fp)
        ext = os.path.splitext(fp)[1].lower()
        ctype = MIME_TYPES.get(ext, 'application/octet-stream')

        self.send_response(200)
        self.send_header('Content-Type', ctype)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(size))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        self.end_headers()

    def do_GET(self):
        fp = self._get_file_path()
        if not fp.startswith(WORKSPACE_ROOT) or not os.path.isfile(fp):
            self.send_error(404, f"File not found: {self.path}")
            return

        size = os.path.getsize(fp)
        ext = os.path.splitext(fp)[1].lower()
        ctype = MIME_TYPES.get(ext, 'application/octet-stream')
        start, end, status_code = 0, size - 1, 200

        range_header = self.headers.get('Range')
        if range_header:
            m = re.match(r'bytes=(\d*)-(\d*)$', range_header.strip())
            if m:
                g1, g2 = m.group(1), m.group(2)
                if g1 and g2:
                    start = int(g1)
                    end = min(int(g2), size - 1)
                elif g1:
                    start = int(g1)
                    end = size - 1
                elif g2:
                    start = max(0, size - int(g2))
                    end = size - 1

                if start > end or start >= size:
                    self.send_response(416)
                    self.send_header('Content-Range', f'bytes */{size}')
                    self.end_headers()
                    return
                status_code = 206

        content_len = end - start + 1
        self.send_response(status_code)
        self.send_header('Content-Type', ctype)
        self.send_header('Accept-Ranges', 'bytes')
        self.send_header('Content-Length', str(content_len))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        if status_code == 206:
            self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.end_headers()

        try:
            with open(fp, 'rb') as f:
                f.seek(start)
                remaining = content_len
                while remaining > 0:
                    chunk_size = min(131072, remaining)
                    chunk = f.read(chunk_size)
                    if not chunk:
                        break
                    self.wfile.write(chunk)
                    remaining -= len(chunk)
        except (BrokenPipeError, ConnectionResetError):
            pass

class ThreadedTCPServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

if __name__ == '__main__':
    server_address = ('0.0.0.0', PORT)
    with ThreadedTCPServer(server_address, RangeRequestHandler) as httpd:
        print(f"[Benaqaab Range Server] Serving {WORKSPACE_ROOT} on http://0.0.0.0:{PORT} / http://localhost:{PORT}")
        sys.stdout.flush()
        httpd.serve_forever()
