// auto_watcher.js - Enhanced full loop
const fs = require('fs');
const path = require('path');

const ARTIFACT_DIR = 'C:/Users/dell/.gemini/antigravity-ide/brain/cf65e5f6-8771-4074-a708-2f041e237074';

async function getTarget() {
  const res = await fetch('http://127.0.0.1:9222/json/list');
  const pages = await res.json();
  const page = pages.find(p => p.url && (p.url.includes('playnano') || p.type === 'page'));
  if (!page) throw new Error('No PlayNANO page found');
  return page;
}

function sendCDP(ws, method, params = {}) {
  return new Promise((resolve, reject) => {
    const id = Math.floor(Math.random() * 1000000);
    const listener = (ev) => {
      try {
        const msg = JSON.parse(ev.data);
        if (msg.id === id) {
          ws.removeEventListener('message', listener);
          resolve(msg.result);
        }
      } catch (err) {
        reject(err);
      }
    };
    ws.addEventListener('message', listener);
    ws.send(JSON.stringify({ id, method, params }));
  });
}

async function takeScreenshot(ws) {
  try {
    const res = await sendCDP(ws, 'Page.captureScreenshot', { format: 'png' });
    if (res && res.data) {
      fs.writeFileSync(path.join(ARTIFACT_DIR, 'live_chrome_view.png'), Buffer.from(res.data, 'base64'));
    }
  } catch (_) {}
}

async function main() {
  const target = await getTarget();
  console.log(`[INIT] Connected to PlayNANO`);

  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r));

  // If not on watch-and-learn/nano, navigate there!
  if (!target.url.includes('/watch-and-learn/nano')) {
    console.log('[NAVIGATE] Loading Watch & Learn Nano module...');
    await sendCDP(ws, 'Page.navigate', { url: 'https://playnano.online/watch-and-learn/nano' });
    await new Promise(r => setTimeout(r, 3500));
  }

  let curX = 450;
  let curY = 350;

  async function humanMouseMove(toX, toY) {
    const steps = 8;
    const dx = (toX - curX) / steps;
    const dy = (toY - curY) / steps;
    for (let i = 0; i < steps; i++) {
      curX += dx + (Math.random() * 3 - 1.5);
      curY += dy + (Math.random() * 3 - 1.5);
      await sendCDP(ws, 'Input.dispatchMouseEvent', {
        type: 'mouseMoved',
        x: Math.round(curX),
        y: Math.round(curY)
      });
      await new Promise(r => setTimeout(r, 25));
    }
  }

  console.log('[WATCHER] Monitoring videos in real time...');
  let loopCount = 0;

  while (true) {
    loopCount++;

    // Small natural mouse movement every 2-3 seconds
    if (loopCount % 5 === 0) {
      const rx = Math.floor(300 + Math.random() * 450);
      const ry = Math.floor(250 + Math.random() * 350);
      await humanMouseMove(rx, ry);
    }

    // Inspect state
    const stateScript = `
      (() => {
        const url = location.href;
        const isVerify = url.includes('captcha') || !!document.querySelector('form[action*="claim"]') || !!document.body.innerText.includes('Verify you are a Human');
        const nextBtn = document.querySelector('.watch-next-btn') || document.querySelector('#next-video-form button');
        
        let btnRect = null;
        if (nextBtn) {
          const rect = nextBtn.getBoundingClientRect();
          btnRect = { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 };
        }

        return {
          url,
          isVerify,
          nextBtn: nextBtn ? {
            text: nextBtn.innerText.trim(),
            disabled: nextBtn.disabled,
            visible: nextBtn.offsetParent !== null,
            rect: btnRect
          } : null
        };
      })()
    `;

    const res = await sendCDP(ws, 'Runtime.evaluate', { expression: stateScript, returnByValue: true });
    const info = res ? res.result.value : null;

    if (!info) {
      await new Promise(r => setTimeout(r, 500));
      continue;
    }

    // If human verification screen is reached
    if (info.isVerify) {
      console.log(`[VERIFY REACHED] Human verification screen reached! Waiting for user captcha.`);
      await sendCDP(ws, 'Runtime.evaluate', {
        expression: `(() => {
          const el = document.querySelector('iframe[src*="turnstile"], iframe[src*="hcaptcha"], .h-captcha, form');
          if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        })()`
      });
      await new Promise(r => setTimeout(r, 1200));
      await takeScreenshot(ws);
      break;
    }

    // If Next Video button is unlocked
    if (info.nextBtn) {
      if (!info.nextBtn.disabled && info.nextBtn.visible) {
        console.log(`[ACTION] Button Unlocked: "${info.nextBtn.text}"! Clicking now...`);

        if (info.nextBtn.rect) {
          await humanMouseMove(info.nextBtn.rect.x, info.nextBtn.rect.y);
        }

        await sendCDP(ws, 'Runtime.evaluate', {
          expression: `(() => {
            const b = document.querySelector('.watch-next-btn') || document.querySelector('#next-video-form button');
            if (b) {
              b.scrollIntoView({ behavior: 'smooth', block: 'center' });
              b.style.outline = '4px solid #10b981';
              b.click();
              return true;
            }
            return false;
          })()`
        });

        await takeScreenshot(ws);
        console.log(`[ACTION] Clicked! Loading next video...`);
        await new Promise(r => setTimeout(r, 3500));
        continue;
      } else {
        if (loopCount % 6 === 0) {
          process.stdout.write(`\r[WAITING] Progressing on ${info.nextBtn.text}...`);
        }
      }
    }

    await new Promise(r => setTimeout(r, 400));
  }

  ws.close();
  process.exit(0);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
