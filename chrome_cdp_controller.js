// Chrome DevTools Protocol Controller for Antigravity AI

async function getPlayNanoPage() {
  const res = await fetch('http://127.0.0.1:9222/json/list');
  const pages = await res.json();
  const page = pages.find(p => p.url && (p.url.includes('playnano') || p.type === 'page'));
  if (!page) throw new Error('No PlayNANO page found');
  return page;
}

async function sendCommand(method, params = {}) {
  const page = await getPlayNanoPage();

  return new Promise((resolve, reject) => {
    const ws = new WebSocket(page.webSocketDebuggerUrl);
    const id = Date.now();

    ws.addEventListener('open', () => {
      ws.send(JSON.stringify({ id, method, params }));
    });

    ws.addEventListener('message', (event) => {
      try {
        const data = JSON.parse(event.data);
        if (data.id === id) {
          ws.close();
          resolve(data.result);
        }
      } catch (e) {
        reject(e);
      }
    });

    ws.addEventListener('error', (err) => {
      reject(err);
    });

    setTimeout(() => {
      try { ws.close(); } catch (_) {}
      reject(new Error('CDP Command timed out'));
    }, 10000);
  });
}

async function main() {
  const action = process.argv[2] || 'badge';

  if (action === 'badge') {
    const code = `
      (() => {
        let el = document.getElementById("agy-live-badge");
        if (!el) {
          el = document.createElement("div");
          el.id = "agy-live-badge";
          document.body.appendChild(el);
        }
        el.innerHTML = "🤖 <b>ANTIGRAVITY AI LIVE CONTROLLER</b>: Active & Connected";
        el.style.cssText = "position:fixed;bottom:24px;right:24px;background:#0f172a;color:#38bdf8;padding:14px 24px;border-radius:12px;font-family:system-ui,-apple-system,sans-serif;font-size:14px;box-shadow:0 10px 25px rgba(0,0,0,0.5);border:1px solid #38bdf8;z-index:999999999;transition:all 0.3s ease;";
        return { success: true, title: document.title, url: location.href };
      })()
    `;
    const res = await sendCommand('Runtime.evaluate', { expression: code, returnByValue: true });
    console.log('Result:', JSON.stringify(res));
  } else if (action === 'scroll') {
    const amount = parseInt(process.argv[3] || '500', 10);
    const code = `window.scrollBy({ top: ${amount}, behavior: 'smooth' }); ({ scrolled: ${amount}, y: window.scrollY });`;
    const res = await sendCommand('Runtime.evaluate', { expression: code, returnByValue: true });
    console.log('Result:', JSON.stringify(res));
  } else if (action === 'click') {
    const selector = process.argv[3];
    const code = `
      (() => {
        const el = document.querySelector("${selector}");
        if (el) {
          el.style.outline = "3px solid #f43f5e";
          el.click();
          return { clicked: true, text: el.innerText };
        }
        return { clicked: false, error: "Element not found" };
      })()
    `;
    const res = await sendCommand('Runtime.evaluate', { expression: code, returnByValue: true });
    console.log('Result:', JSON.stringify(res));
  } else if (action === 'navigate') {
    const url = process.argv[3];
    const res = await sendCommand('Page.navigate', { url });
    console.log('Result:', JSON.stringify(res));
  } else if (action === 'eval') {
    const expr = process.argv.slice(3).join(' ');
    const res = await sendCommand('Runtime.evaluate', { expression: expr, returnByValue: true });
    console.log('Result:', JSON.stringify(res));
  }
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
