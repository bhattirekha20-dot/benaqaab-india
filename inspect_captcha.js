// inspect_captcha.js
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
          const iframes = Array.from(document.querySelectorAll('iframe')).map(f => ({
            id: f.id,
            src: f.src.slice(0, 80),
            name: f.name
          }));
          const inputs = Array.from(document.querySelectorAll('input, textarea')).map(i => ({
            type: i.type,
            name: i.name,
            value: (i.value || '').slice(0, 30),
            disabled: i.disabled
          }));
          const captchaElements = Array.from(document.querySelectorAll('[class*="captcha"], [class*="turnstile"], [class*="geetest"], [id*="captcha"]')).map(el => ({
            tag: el.tagName,
            id: el.id,
            className: el.className
          }));
          const submitBtn = Array.from(document.querySelectorAll('button, input[type="submit"]')).find(b => 
            (b.innerText || b.value || '').toLowerCase().includes('keep watching')
          );
          return {
            iframes,
            inputs,
            captchaElements,
            submitBtn: submitBtn ? { text: submitBtn.innerText || submitBtn.value, disabled: submitBtn.disabled } : null
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
