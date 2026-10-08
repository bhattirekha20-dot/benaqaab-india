#!/usr/bin/env node
/**
 * render.mjs — Puppeteer Frame Capture & FFmpeg Encoder
 * Deterministic Canvas2D Title Card Video Engine
 */

import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { execSync } from 'node:child_process';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

// Command line arguments
const args = process.argv.slice(2);
const STILLS_ONLY = args.includes('--stills') || args.includes('--stills-only');
const NO_ENCODE = args.includes('--no-encode');

// MIME types dictionary for static file server
const MIME_TYPES = {
  '.html': 'text/html',
  '.js': 'application/javascript',
  '.mjs': 'application/javascript',
  '.css': 'text/css',
  '.woff2': 'font/woff2',
  '.woff': 'font/woff',
  '.ttf': 'font/ttf',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.json': 'application/json'
};

/**
 * 1. Serve the current directory over a free HTTP port so fonts load reliably
 */
function createStaticServer() {
  return new Promise((resolve, reject) => {
    const server = http.createServer((req, res) => {
      let reqPath = decodeURI(req.url.split('?')[0]);
      if (reqPath === '/' || reqPath === '') reqPath = '/index.html';

      const filePath = path.join(__dirname, reqPath);

      if (!filePath.startsWith(__dirname)) {
        res.writeHead(403);
        return res.end('Forbidden');
      }

      fs.stat(filePath, (err, stats) => {
        if (err || !stats.isFile()) {
          res.writeHead(404, { 'Content-Type': 'text/plain' });
          return res.end(`Not Found: ${reqPath}`);
        }

        const ext = path.extname(filePath).toLowerCase();
        const contentType = MIME_TYPES[ext] || 'application/octet-stream';

        res.writeHead(200, {
          'Content-Type': contentType,
          'Access-Control-Allow-Origin': '*',
          'Cache-Control': 'no-cache'
        });

        const stream = fs.createReadStream(filePath);
        stream.pipe(res);
      });
    });

    server.listen(0, '127.0.0.1', () => {
      const port = server.address().port;
      resolve({ server, port });
    });

    server.on('error', reject);
  });
}

/**
 * Find local Chromium / Chrome executable if available
 */
function findChromeExecutable() {
  const candidates = [
    'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
    'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe',
    '/usr/bin/google-chrome-stable',
    '/usr/bin/google-chrome',
    '/usr/bin/chromium',
    '/usr/bin/chromium-browser'
  ];
  for (const candidate of candidates) {
    if (fs.existsSync(candidate)) return candidate;
  }
  return undefined;
}

async function main() {
  console.log('====================================================');
  console.log('🎥 TITLE-CARD DETERMINISTIC VIDEO RENDERER');
  console.log('====================================================');

  // Dynamically import puppeteer
  let puppeteer;
  try {
    puppeteer = (await import('puppeteer')).default;
  } catch (err) {
    console.error('❌ Error: puppeteer is not installed.');
    console.error('Run: npm install puppeteer in this folder first.');
    process.exit(1);
  }

  // Ensure directories exist
  const framesDir = path.join(__dirname, 'frames');
  const stillsDir = path.join(__dirname, 'stills');
  const outDir = path.join(__dirname, 'out');
  fs.mkdirSync(framesDir, { recursive: true });
  fs.mkdirSync(stillsDir, { recursive: true });
  fs.mkdirSync(outDir, { recursive: true });

  // 1. Launch HTTP server
  const { server, port } = await createStaticServer();
  const url = `http://127.0.0.1:${port}/index.html`;
  console.log(`📡 Local server listening on http://127.0.0.1:${port}`);

  // 2. Launch Puppeteer
  const chromePath = findChromeExecutable();
  console.log(`🌐 Launching headless browser... ${chromePath ? `(Using ${chromePath})` : ''}`);

  const browser = await puppeteer.launch({
    headless: true,
    executablePath: chromePath,
    args: [
      '--no-sandbox',
      '--disable-setuid-sandbox',
      '--disable-dev-shm-usage',
      '--font-render-hinting=none',
      '--force-color-profile=srgb',
      '--hide-scrollbars'
    ]
  });

  try {
    const page = await browser.newPage();
    await page.setViewport({ width: 1920, height: 1080, deviceScaleFactor: 1 });

    console.log(`🧭 Navigating to ${url}...`);
    await page.goto(url, { waitUntil: 'load', timeout: 30000 });

    // Wait for fonts & readiness contract
    console.log('⏳ Waiting for window.READY === true...');
    await page.waitForFunction('window.READY === true', { timeout: 30000 });

    const meta = await page.evaluate(() => ({
      duration: window.DURATION,
      fps: window.FPS,
      width: window.WIDTH,
      height: window.HEIGHT,
      cards: window.TIMELINE ? window.TIMELINE.cards : []
    }));

    const { duration, fps, width, height, cards } = meta;
    const totalFrames = Math.ceil(duration * fps);

    console.log(`📐 Resolution: ${width}x${height} @ ${fps} fps`);
    console.log(`⏱️ Duration: ${duration}s (${totalFrames} frames)`);
    console.log(`🗂️ Cards count: ${cards.length}`);

    // Step A: Render Stills First for Quality Verification
    console.log('\n--- 🖼️ STEP 1: RENDERING VERIFICATION STILLS (ONE PER CARD) ---');
    for (let c = 0; c < cards.length; c++) {
      const card = cards[c];
      const midT = card.startTime + 0.5 + (card.holdDuration / 2);
      await page.evaluate((t) => window.renderFrame(t), midT);

      const dataUrl = await page.evaluate(() => {
        return document.getElementById('c').toDataURL('image/png');
      });

      const base64Data = dataUrl.replace(/^data:image\/png;base64,/, '');
      const stillFile = path.join(stillsDir, `card_${c + 1}.png`);
      fs.writeFileSync(stillFile, Buffer.from(base64Data, 'base64'));

      console.log(`   ✓ Card ${c + 1} at ${midT.toFixed(2)}s: "${card.text}" -> ${path.relative(__dirname, stillFile)}`);
    }

    if (STILLS_ONLY) {
      console.log('\n✅ Stills generated successfully (--stills-only). Exiting.');
      return;
    }

    // Step B: Render Full Frame Sequence
    console.log(`\n--- 🎞️ STEP 2: RENDERING ${totalFrames} FRAMES ---`);
    const startTime = Date.now();

    for (let i = 0; i < totalFrames; i++) {
      const t = i / fps;
      await page.evaluate((currT) => window.renderFrame(currT), t);

      const dataUrl = await page.evaluate(() => {
        return document.getElementById('c').toDataURL('image/png');
      });

      const base64Data = dataUrl.replace(/^data:image\/png;base64,/, '');
      const frameFile = path.join(framesDir, `f${String(i).padStart(5, '0')}.png`);
      fs.writeFileSync(frameFile, Buffer.from(base64Data, 'base64'));

      if (i % 30 === 0 || i === totalFrames - 1) {
        const pct = ((i + 1) / totalFrames * 100).toFixed(1);
        const fpsRate = ((i + 1) / ((Date.now() - startTime) / 1000)).toFixed(1);
        process.stdout.write(`\r   Capturing frame ${i + 1}/${totalFrames} (${pct}%) @ ${fpsRate} fps...`);
      }
    }
    console.log(`\n✅ Rendered all ${totalFrames} frames in ${((Date.now() - startTime) / 1000).toFixed(1)}s.`);

    // Step C: FFmpeg Encoding
    if (!NO_ENCODE) {
      console.log('\n--- 🎬 STEP 3: ENCODING MP4 WITH FFMPEG ---');
      const inputPattern = path.join(framesDir, 'f%05d.png').replace(/\\/g, '/');
      const outputFile = path.join(outDir, 'title_cards.mp4').replace(/\\/g, '/');

      const cmd = `ffmpeg -y -framerate ${fps} -i "${inputPattern}" -c:v libx264 -preset slow -crf 18 -pix_fmt yuv420p -movflags +faststart "${outputFile}"`;
      console.log(`Running: ${cmd}`);

      execSync(cmd, { stdio: 'inherit' });
      console.log(`\n🎉 Output master created: ${outputFile}`);
      const stat = fs.statSync(outputFile);
      console.log(`📦 File size: ${(stat.size / 1024 / 1024).toFixed(2)} MB`);
    } else {
      console.log('\nℹ️ Skipping FFmpeg encoding (--no-encode).');
    }

  } finally {
    await browser.close();
    server.close();
  }

  console.log('\n====================================================');
  console.log('✅ COMPLETE: Title-card video build finished!');
  console.log('====================================================');
}

main().catch(err => {
  console.error('\n❌ Fatal execution error:', err);
  process.exit(1);
});
