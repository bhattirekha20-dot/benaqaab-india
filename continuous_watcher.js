// continuous_watcher.js
// Autonomous continuous loop: Watches 1-5 videos -> triggers captcha -> waits for human puzzle solve -> auto-submits -> repeats forever!

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
    const id = Math.floor(Math.random() * 10000000);
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
  console.log(`[START] Continuous Watcher connected to PlayNANO`);

  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r));

  let curX = 450;
  let curY = 350;

  async function humanMouseMove(toX, toY) {
    const steps = 6;
    const dx = (toX - curX) / steps;
    const dy = (toY - curY) / steps;
    for (let i = 0; i < steps; i++) {
      curX += dx + (Math.random() * 4 - 2);
      curY += dy + (Math.random() * 4 - 2);
      await sendCDP(ws, 'Input.dispatchMouseEvent', {
        type: 'mouseMoved',
        x: Math.round(curX),
        y: Math.round(curY)
      });
      await new Promise(r => setTimeout(r, 20));
    }
  }

  let loopCounter = 0;
  let clickedCaptchaBox = false;

  console.log('[AUTOPILOT] Running full hands-free loop...');

  while (true) {
    loopCounter++;

    // Natural mouse movement every 2-3s
    if (loopCounter % 5 === 0) {
      const rx = Math.floor(250 + Math.random() * 500);
      const ry = Math.floor(200 + Math.random() * 400);
      await humanMouseMove(rx, ry);
    }

    // Inspect current DOM state
    const inspectScript = `
      (() => {
        const url = location.href;
        const isVerify = url.includes('captcha') || !!document.querySelector('form[action*="claim"]') || document.body.innerText.includes('Verify you are a Human');
        const nextBtn = document.querySelector('.watch-next-btn') || document.querySelector('#next-video-form button');
        
        let nextBtnInfo = null;
        if (nextBtn) {
          const rect = nextBtn.getBoundingClientRect();
          nextBtnInfo = {
            text: nextBtn.innerText.trim(),
            disabled: nextBtn.disabled,
            visible: nextBtn.offsetParent !== null,
            rect: { x: rect.left + rect.width / 2, y: rect.top + rect.height / 2 }
          };
        }

        // Check verification details
        let captchaTokenPresent = false;
        const tokenInputs = Array.from(document.querySelectorAll('input[name*="captcha"], textarea[name*="captcha"], input[name*="turnstile"], textarea[name*="turnstile"]'));
        for (const input of tokenInputs) {
          if (input.value && input.value.trim().length > 10) {
            captchaTokenPresent = true;
            break;
          }
        }

        // Also check if hcaptcha or geetest has success class
        const hasSuccessClass = !!document.querySelector('.geetest_success, [data-hcaptcha-response], .hcaptcha-success');
        if (hasSuccessClass) captchaTokenPresent = true;

        const captchaBox = document.querySelector('iframe[src*="turnstile"], iframe[src*="hcaptcha"], .h-captcha, .geetest_btn, #captcha, [class*="captcha"]');
        let captchaBoxRect = null;
        if (captchaBox) {
          const r = captchaBox.getBoundingClientRect();
          captchaBoxRect = { x: r.left + r.width / 2, y: r.top + r.height / 2 };
        }

        const keepWatchingBtn = Array.from(document.querySelectorAll('button, input[type="submit"], a.btn')).find(b => 
          (b.innerText || b.value || '').toLowerCase().includes('keep watching')
        );

        let keepBtnInfo = null;
        if (keepWatchingBtn) {
          const kr = keepWatchingBtn.getBoundingClientRect();
          keepBtnInfo = {
            text: keepWatchingBtn.innerText || keepWatchingBtn.value,
            disabled: keepWatchingBtn.disabled,
            rect: { x: kr.left + kr.width / 2, y: kr.top + kr.height / 2 }
          };
        }

        return {
          url,
          isVerify,
          nextBtnInfo,
          captchaBoxRect,
          captchaTokenPresent,
          keepBtnInfo
        };
      })()
    `;

    const state = await sendCDP(ws, 'Runtime.evaluate', { expression: inspectScript, returnByValue: true });
    const info = state ? state.result.value : null;

    if (!info) {
      await new Promise(r => setTimeout(r, 400));
      continue;
    }

    // -------------------------------------------------------------
    // CASE 1: Verification Screen (Captcha stage)
    // -------------------------------------------------------------
    if (info.isVerify) {
      // Step A: If we haven't clicked the initial captcha box yet, click it to pop up the puzzle for the human!
      if (!clickedCaptchaBox && info.captchaBoxRect) {
        console.log('[VERIFY] Clicking "I am human" box to trigger puzzle for user...');
        await humanMouseMove(info.captchaBoxRect.x, info.captchaBoxRect.y);
        
        // Click box
        await sendCDP(ws, 'Runtime.evaluate', {
          expression: `(() => {
            const b = document.querySelector('iframe[src*="turnstile"], iframe[src*="hcaptcha"], .h-captcha, [class*="captcha"]') || document.querySelector('.geetest_btn');
            if (b) {
              b.scrollIntoView({ behavior: 'smooth', block: 'center' });
              b.click();
              return true;
            }
            return false;
          })()`
        });

        clickedCaptchaBox = true;
        await takeScreenshot(ws);
        console.log('[VERIFY] Puzzle popup displayed. User solving puzzle on screen now...');
        await new Promise(r => setTimeout(r, 1500));
        continue;
      }

      // Step B: Check if human has solved the puzzle!
      if (info.captchaTokenPresent || (info.keepBtnInfo && !info.keepBtnInfo.disabled && clickedCaptchaBox)) {
        console.log('[VERIFY] Puzzle solved detected! Auto-clicking "Earn Nano & Keep Watching"...');
        
        if (info.keepBtnInfo && info.keepBtnInfo.rect) {
          await humanMouseMove(info.keepBtnInfo.rect.x, info.keepBtnInfo.rect.y);
        }

        await sendCDP(ws, 'Runtime.evaluate', {
          expression: `(() => {
            const btn = Array.from(document.querySelectorAll('button, input[type="submit"], a.btn')).find(b => 
              (b.innerText || b.value || '').toLowerCase().includes('keep watching')
            );
            if (btn) {
              btn.style.outline = '4px solid #10b981';
              btn.click();
              return true;
            }
            return false;
          })()`
        });

        console.log('[SUBMIT] Payout submitted! Resetting for next batch...');
        clickedCaptchaBox = false; // Reset for next time
        await takeScreenshot(ws);
        await new Promise(r => setTimeout(r, 3500)); // Wait for new batch to load
        continue;
      }

      // Still waiting for human to solve puzzle
      if (loopCounter % 8 === 0) {
        process.stdout.write(`\r[WAITING FOR HUMAN] Awaiting slider solve on screen...`);
      }

      await new Promise(r => setTimeout(r, 400));
      continue;
    }

    // Reset captcha flag once we leave verify page
    clickedCaptchaBox = false;

    // -------------------------------------------------------------
    // CASE 2: Video Watching Stage
    // -------------------------------------------------------------
    if (info.nextBtnInfo) {
      if (!info.nextBtnInfo.disabled && info.nextBtnInfo.visible) {
        console.log(`[ACTION] Button Unlocked: "${info.nextBtnInfo.text}"! Clicking instantly...`);

        if (info.nextBtnInfo.rect) {
          await humanMouseMove(info.nextBtnInfo.rect.x, info.nextBtnInfo.rect.y);
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
        await new Promise(r => setTimeout(r, 3000));
        continue;
      } else {
        if (loopCounter % 6 === 0) {
          process.stdout.write(`\r[WATCHING] Progressing on ${info.nextBtnInfo.text}...`);
        }
      }
    }

    await new Promise(r => setTimeout(r, 400));
  }
}

main().catch(err => {
  console.error('[ERROR]', err);
  process.exit(1);
});
