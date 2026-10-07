// check_btn.js
async function run() {
  const res = await fetch('http://127.0.0.1:9222/json/list');
  const pages = await res.json();
  const page = pages.find(p => p.url && (p.url.includes('playnano') || p.type === 'page'));
  const ws = new WebSocket(page.webSocketDebuggerUrl);
  await new Promise(r => ws.addEventListener('open', r));

  ws.send(JSON.stringify({
    id: 1,
    method: 'Runtime.evaluate',
    params: {
      expression: `
        (() => {
          const scripts = Array.from(document.querySelectorAll('script')).map(s => s.innerText).filter(t => 
            t.includes('watch-next-btn') || t.includes('disabled') || t.includes('countdown') || t.includes('timer')
          );
          return scripts.map(s => s.slice(0, 300));
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
