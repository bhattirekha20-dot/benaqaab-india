// inspect_login.js
const fs = require('fs');
const path = require('path');
const ARTIFACT_DIR = 'C:/Users/dell/.gemini/antigravity-ide/brain/cf65e5f6-8771-4074-a708-2f041e237074';

async function main() {
  const res = await fetch('http://127.0.0.1:9222/json/list');
  const pages = await res.json();
  const page = pages.find(p => p.url.includes('playnano') || p.type === 'page');
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r));

  function call(method, params = {}) {
    return new Promise(resolve => {
      const id = Math.floor(Math.random() * 1000000);
      const listener = ev => {
        const msg = JSON.parse(ev.data);
        if (msg.id === id) {
          ws.removeEventListener('message', listener);
          resolve(msg.result);
        }
      };
      ws.addEventListener('message', listener);
      ws.send(JSON.stringify({ id, method, params }));
    });
  }

  const script = `
    (() => {
      const links = Array.from(document.querySelectorAll('nav a, header a')).map(a => a.innerText.trim()).filter(Boolean);
      return {
        url: location.href,
        title: document.title,
        navLinks: links.slice(0, 15)
      };
    })()
  `;

  const info = await call('Runtime.evaluate', { expression: script, returnByValue: true });
  console.log('Page info:', JSON.stringify(info.result.value));

  // Take screenshot
  const snap = await call('Page.captureScreenshot', { format: 'png' });
  if (snap && snap.data) {
    fs.writeFileSync(path.join(ARTIFACT_DIR, 'live_chrome_view.png'), Buffer.from(snap.data, 'base64'));
    console.log('Screenshot updated');
  }

  ws.close();
  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
