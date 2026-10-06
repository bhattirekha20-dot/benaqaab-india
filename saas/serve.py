#!/usr/bin/env python3
"""
serve.py — High-Performance Local Streaming Server for BENAQAAB OS SaaS
Supports HTTP 206 Partial Content (Range requests) for smooth video playback & scrubbing.
Serves from workspace root so all /VIDEOS and /projects assets load cleanly.
"""

import os
import sys
import mimetypes
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PORT = 8080
ROOT_DIR = Path(__file__).resolve().parent.parent

class RangeRequestHandler(SimpleHTTPRequestHandler):
    """HTTP handler with byte-range support for video seeking."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT_DIR), **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        super().end_headers()

    def do_GET(self):
        # Redirect root to /saas/
        if self.path in ('/', '/index.html'):
            self.send_response(302)
            self.send_header('Location', '/saas/index.html')
            self.end_headers()
            return

        path = self.translate_path(self.path)
        if not os.path.exists(path) or os.path.isdir(path):
            super().do_GET()
            return

        # Check for Range header
        range_header = self.headers.get('Range')
        if not range_header or not range_header.startswith('bytes='):
            super().do_GET()
            return

        file_size = os.path.getsize(path)
        range_val = range_header.strip().split('=')[1]
        try:
            start_str, end_str = range_val.split('-')
            start = int(start_str) if start_str else 0
            end = int(end_str) if end_str else file_size - 1
            if end >= file_size:
                end = file_size - 1
            length = end - start + 1
        except Exception:
            super().do_GET()
            return

        mime_type, _ = mimetypes.guess_type(path)
        mime_type = mime_type or 'application/octet-stream'

        self.send_response(206)
        self.send_header('Content-Type', mime_type)
        self.send_header('Content-Range', f'bytes {start}-{end}/{file_size}')
        self.send_header('Content-Length', str(length))
        self.send_header('Accept-Ranges', 'bytes')
        self.end_headers()

        with open(path, 'rb') as f:
            f.seek(start)
            bytes_left = length
            chunk_size = 64 * 1024
            while bytes_left > 0:
                to_read = min(chunk_size, bytes_left)
                data = f.read(to_read)
                if not data:
                    break
                self.wfile.write(data)
                bytes_left -= len(data)

def run():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, RangeRequestHandler)
    print("=" * 65)
    print(f"🚀 [BENAQAAB OS] SaaS Studio is Live!")
    print(f"👉 Local Access URL:   http://localhost:{PORT}/saas/index.html")
    print(f"👉 Root Directory:     {ROOT_DIR}")
    print(f"👉 Video Stream Range: HTTP 206 Enabled (Smooth Playback & Seeking)")
    print("=" * 65)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down server.")
        httpd.server_close()

if __name__ == '__main__':
    run()
