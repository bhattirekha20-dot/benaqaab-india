// check_err.js
async function run() {
  const res = await fetch('http://127.0.0.1:9222/json/list');
  const pages = await res.json();
  const page = pages.find(p => p.url.includes('playnano') || p.type === 'page');
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r));

  ws.send(JSON.stringify({
    id: 1,
    method: 'Runtime.evaluate',
    params: {
      expression: `
        (() => {
          const alerts = Array.from(document.querySelectorAll('.alert, .toast, .notification, [class*="error"], [class*="danger"], [class*="flash"]')).map(el => el.innerText.trim());
          return {
            alerts,
            currentUrl: location.href
          };
        })()
      `,
      returnByValue: true
    }
  }));

  ws.addEventListener('message', ev => {
    console.log(JSON.stringify(JSON.parse(ev.data).result.result.value, null, 2));
    ws.close();
    process.exit(0);
  });
}
run();
