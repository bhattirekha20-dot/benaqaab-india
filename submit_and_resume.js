// submit_and_resume.js
const fs = require('fs');
const path = require('path');
const ARTIFACT_DIR = 'C:/Users/dell/.gemini/antigravity-ide/brain/cf65e5f6-8771-4074-a708-2f041e237074';

async function main() {
  const res = await fetch('http://127.0.0.1:9222/json/list');
  const pages = await res.json();
  const page = pages.find(p => p.url && (p.url.includes('playnano') || p.type === 'page'));
  if (!page) throw new Error('No page found');

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

  // Click "Earn Nano & Keep Watching"
  const clickScript = `
    (() => {
      const btns = Array.from(document.querySelectorAll('button, input[type="submit"], a.btn'));
      const target = btns.find(b => (b.innerText || b.value || '').toLowerCase().includes('keep watching'));
      if (target) {
        target.style.outline = '4px solid #10b981';
        target.click();
        return { clicked: true, text: target.innerText || target.value };
      }
      return { clicked: false, error: 'Button not found' };
    })()
  `;

  const clickResult = await call('Runtime.evaluate', { expression: clickScript, returnByValue: true });
  console.log('Submit Result:', JSON.stringify(clickResult));

  // Wait 3 seconds for payout confirmation and next video load
  await new Promise(r => setTimeout(r, 3000));

  // Inspect new state
  const state = await call('Runtime.evaluate', {
    expression: '({ url: location.href, title: document.title, bodyText: document.body.innerText.slice(0, 300) })',
    returnByValue: true
  });
  console.log('New State:', JSON.stringify(state.result.value));

  // Capture screenshot
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
