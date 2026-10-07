// cdp_actions.js - Handle video watching and automatic progression
const fs = require('fs');
const path = require('path');
const ARTIFACT_DIR = 'C:/Users/dell/.gemini/antigravity-ide/brain/cf65e5f6-8771-4074-a708-2f041e237074';

async function main() {
  const res = await fetch('http://127.0.0.1:9222/json/list');
  const pages = await res.json();
  const page = pages.find(p => p.url && (p.url.includes('playnano') || p.type === 'page'));
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

  // Play video or check requirements to enable button
  const videoScript = `
    (() => {
      const video = document.querySelector('video');
      const btn = document.querySelector('.watch-next-btn') || document.querySelector('#next-video-form button');
      
      let videoAction = 'none';
      if (video) {
        if (video.paused) {
          video.play().catch(() => {});
          videoAction = 'playing';
        } else {
          videoAction = 'already_playing';
        }
        // If there is an end event or countdown, let's check
      }

      // Check if button has disabled attribute or if removing it allows submit
      const btnInfo = btn ? {
        text: btn.innerText.trim(),
        disabled: btn.disabled,
        classList: Array.from(btn.classList)
      } : null;

      return {
        videoAction,
        videoDuration: video ? video.duration : null,
        videoCurrentTime: video ? video.currentTime : null,
        btnInfo
      };
    })()
  `;

  const status = await call('Runtime.evaluate', { expression: videoScript, returnByValue: true });
  console.log('Playback & Button Status:', JSON.stringify(status.result.value, null, 2));

  // If button disabled, check how the page enables it (timers or video events)
  const timerCheckScript = `
    (() => {
      // Find scripts or event listeners or countdown elements
      const countdowns = Array.from(document.querySelectorAll('*')).filter(el => {
        const t = el.innerText || '';
        return /\\d+s|wait|second/i.test(t) && el.children.length === 0;
      }).map(el => el.innerText.trim());

      return { countdowns: countdowns.slice(0, 5) };
    })()
  `;
  const timerInfo = await call('Runtime.evaluate', { expression: timerCheckScript, returnByValue: true });
  console.log('Timer info:', JSON.stringify(timerInfo.result.value));

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
