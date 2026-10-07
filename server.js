// Benaqaab India — Localhost Studio Server
const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = process.env.PORT || 3000;
const ROOT_DIR = __dirname;

const MIME_TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.mjs': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.webp': 'image/webp',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.mp4': 'video/mp4',
  '.webm': 'video/webm',
  '.mp3': 'audio/mpeg',
  '.wav': 'audio/wav',
  '.ogg': 'audio/ogg',
  '.txt': 'text/plain; charset=utf-8',
  '.srt': 'text/plain; charset=utf-8',
  '.md': 'text/markdown; charset=utf-8',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
  '.ttf': 'font/ttf'
};

const server = http.createServer((req, res) => {
  // Enable permissive CORS
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET, HEAD, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', '*');

  if (req.method === 'OPTIONS') {
    res.writeHead(204);
    return res.end();
  }

  const parsedUrl = url.parse(req.url);
  let pathname = decodeURIComponent(parsedUrl.pathname);

  // Root redirect -> /dashboard/ for clean relative path resolution
  if (pathname === '/') {
    res.writeHead(302, { 'Location': '/dashboard/' });
    return res.end();
  }
  if (pathname === '/dashboard' || pathname === '/dashboard/') {
    pathname = '/dashboard/index.html';
  }

  // Security: prevent directory traversal
  const safePath = path.normalize(pathname).replace(/^(\.\.[\/\\])+/, '');
  let filePath = path.join(ROOT_DIR, safePath);

  fs.stat(filePath, (err, stats) => {
    if (err || !stats.isFile()) {
      // Fallback 1: check if file exists directly under dashboard/
      const dashCandidate = path.join(ROOT_DIR, 'dashboard', safePath);
      if (fs.existsSync(dashCandidate) && fs.statSync(dashCandidate).isFile()) {
        filePath = dashCandidate;
        stats = fs.statSync(dashCandidate);
      } else if (stats && stats.isDirectory()) {
        const candidate = path.join(filePath, 'index.html');
        if (fs.existsSync(candidate)) {
          filePath = candidate;
          stats = fs.statSync(candidate);
        } else {
          res.writeHead(404, { 'Content-Type': 'text/plain' });
          return res.end('404 Not Found');
        }
      } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        return res.end('404 Not Found: ' + pathname);
      }
    }

    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';
    const totalSize = stats ? stats.size : 0;

    // Handle HTTP Range Requests for MP4/MP3 media streaming
    const range = req.headers.range;
    if (range && stats) {
      const parts = range.replace(/bytes=/, "").split("-");
      const start = parseInt(parts[0], 10);
      const end = parts[1] ? parseInt(parts[1], 10) : totalSize - 1;

      if (start >= totalSize || end >= totalSize) {
        res.writeHead(416, { 'Content-Range': `bytes */${totalSize}` });
        return res.end();
      }

      const chunksize = (end - start) + 1;
      const fileStream = fs.createReadStream(filePath, { start, end });
      res.writeHead(206, {
        'Content-Range': `bytes ${start}-${end}/${totalSize}`,
        'Accept-Ranges': 'bytes',
        'Content-Length': chunksize,
        'Content-Type': contentType
      });
      fileStream.pipe(res);
    } else {
      res.writeHead(200, {
        'Content-Length': totalSize,
        'Content-Type': contentType,
        'Accept-Ranges': 'bytes'
      });
      fs.createReadStream(filePath).pipe(res);
    }
  });
});

server.listen(PORT, '127.0.0.1', () => {
  console.log(`\n======================================================`);
  console.log(`  BENAQAAB INDIA — STUDIO LOCALHOST COMMAND CENTER`);
  console.log(`  Running live at: http://localhost:${PORT}`);
  console.log(`  Dashboard URL:   http://localhost:${PORT}/dashboard/`);
  console.log(`======================================================\n`);
});
