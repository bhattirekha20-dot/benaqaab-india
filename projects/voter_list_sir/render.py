from pathlib import Path
import base64, json, html

ROOT = Path('/home/user/voter_list_short')
OUT = ROOT / 'comp.html'


def data_uri(path: Path) -> str:
    mime = 'image/png' if path.suffix.lower() == '.png' else 'audio/mpeg'
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode('ascii')

images = [data_uri(ROOT / f'ai_{i:02d}_{name}.png') for i, name in [
    (1, 'ballot_list'), (2, 'citizen_checking'), (3, 'blo_visit'), (4, 'form6'),
    (5, 'court'), (6, 'protest'), (7, 'balance'), (8, 'final_check')
]]
audio = data_uri(ROOT / 'html_preview_narration_v2.mp3')

scenes = [
    dict(a=0, b=8, im=0, kicker='AI ILLUSTRATIVE VISUAL', title=['NAME MISSING?', 'CAN YOU STILL VOTE?'], pill='VOTER LIST', source='Editorial opener · 6 Oct 2026', accent='#f4b942'),
    dict(a=8, b=25, im=2, kicker='AI ILLUSTRATIVE VISUAL', title=['SIR', 'WHAT IS IT?'], pill='OFFICIAL PURPOSE', source='ECI press note · 26 Sep 2026', accent='#55d6be'),
    dict(a=25, b=38, im=4, kicker='AI ILLUSTRATIVE VISUAL', title=['VERIFY → NOTICE', 'CLAIM → APPEAL'], pill='PROCESS MATTERS', source='ECI material · attributed process', accent='#6ed7ff'),
    dict(a=38, b=55, im=6, kicker='REPORTED FIGURE', title=['13+ CRORE', 'DRAFT ROLLS'], pill='DRAFT ≠ FINAL', source='Indian Express report · draft-roll figure', accent='#f4b942'),
    dict(a=55, b=73, im=3, kicker='AI ILLUSTRATIVE VISUAL', title=['FORM 6', 'THE FLASHPOINT'], pill='NEW VOTER FORM', source='Indian Express report · attributed', accent='#ff6b5f'),
    dict(a=73, b=85, im=4, kicker='TWO POSITIONS', title=['ECI SAYS UPHELD', 'COURT SAYS: NOT APPROVED'], pill='5 OCTOBER', source='ECI press note + Supreme Court hearing', accent='#ff7a59'),
    dict(a=85, b=94, im=6, kicker='REPORTED INSTITUTIONAL DISPUTE', title=['14 OBJECTIONS', '10 MONTHS'], pill='ATTRIBUTED REPORT', source='Indian Express report · ECI response included', accent='#d995ff'),
    dict(a=94, b=101.5, im=7, kicker='OFFICIAL VIEWER ACTION', title=['CHECK YOUR', 'NAME NOW'], pill='VOTERS.ECI.GOV.IN', source='Official Voters’ Services Portal', accent='#55d6be'),
]

cues = [
    dict(a=0, b=6.5, text='NAME MISSING FROM THE VOTER LIST?', sub='CAN YOU STILL VOTE?'),
    dict(a=6.5, b=12.5, text='SIR = SPECIAL INTENSIVE REVISION', sub='UPDATE: 6 OCTOBER 2026'),
    dict(a=12.5, b=24.0, text='CLEAN ROLLS — KEEP ELIGIBLE VOTERS IN', sub='ECI\'S STATED PURPOSE'),
    dict(a=24.0, b=33.0, text='VERIFICATION • NOTICE • CLAIM • APPEAL', sub='PROCESS, NOT JUST A NUMBER'),
    dict(a=33.0, b=39.5, text='SUPREME COURT: POWER UPHELD', sub='BIHAR SIR · 27 MAY 2026'),
    dict(a=39.5, b=49.0, text='13+ CRORE NAMES REPORTED REMOVED', sub='DRAFT ROLLS — INDIAN EXPRESS'),
    dict(a=49.0, b=55.0, text='DRAFT FIGURE ≠ FINAL DELETION', sub='CLAIMS AND APPEALS CAN CHANGE IT'),
    dict(a=55.0, b=63.5, text='FORM 6 = NEW VOTER REGISTRATION', sub='THE CONTROVERSY\'S FLASHPOINT'),
    dict(a=63.5, b=74.5, text='WHO ADDED THE EXTRA DECLARATION?', sub='APPLICANT • PARENT • GRANDPARENT'),
    dict(a=74.5, b=85.0, text='ECI POSITION ≠ COURT CLARIFICATION', sub='THE CORE DISPUTE'),
    dict(a=85.0, b=93.5, text='14 REPORTED OBJECTIONS IN 10 MONTHS', sub='INTERNAL DISAGREEMENT — ATTRIBUTED'),
    dict(a=93.5, b=101.5, text='CHECK YOUR NAME', sub='VOTERS.ECI.GOV.IN · LIKE + SUBSCRIBE'),
]

html_doc = r'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1">
<title>Benaqaab India · SIR HTML Approval Preview</title>
<style>
:root { --ink:#101426; --muted:#667085; --line:#e7eaf0; --gold:#f4b942; --navy:#11182d; }
* { box-sizing:border-box; }
body { margin:0; min-height:100vh; background:linear-gradient(135deg,#f6f8fc 0%,#eef1f7 100%); color:var(--ink); font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",Arial,sans-serif; }
.shell { width:min(1100px,100%); margin:0 auto; padding:24px 18px 40px; }
.header { display:flex; align-items:flex-start; justify-content:space-between; gap:18px; margin-bottom:18px; }
.eyebrow { color:#5a4a1b; font-size:11px; font-weight:800; letter-spacing:.15em; text-transform:uppercase; margin-bottom:7px; }
h1 { font-size:clamp(22px,3vw,34px); line-height:1.05; margin:0 0 7px; letter-spacing:-.035em; }
.subtitle { color:#596274; font-size:14px; max-width:690px; line-height:1.5; margin:0; }
.approval { flex:none; padding:10px 12px; border:1px solid #eed38e; color:#684d0d; background:#fff8df; border-radius:999px; font-size:12px; font-weight:800; white-space:nowrap; }
.stage-wrap { display:flex; justify-content:center; }
.stage-frame { position:relative; width:min(480px,82vw); aspect-ratio:9/16; background:#0b0d15; border-radius:22px; box-shadow:0 24px 70px rgba(22,31,54,.24); overflow:hidden; }
canvas { display:block; width:100%; height:100%; background:#0b0d15; }
.badge { position:absolute; left:14px; top:14px; z-index:2; padding:6px 8px; border-radius:8px; background:rgba(255,255,255,.88); color:#101426; font-size:10px; font-weight:900; letter-spacing:.04em; }
.controls { margin:16px auto 0; width:min(760px,100%); background:#fff; border:1px solid var(--line); border-radius:16px; padding:13px 15px 12px; box-shadow:0 12px 30px rgba(22,31,54,.07); }
.control-row { display:flex; align-items:center; gap:9px; }
button { border:0; border-radius:9px; padding:9px 12px; background:#121a31; color:#fff; font-weight:800; cursor:pointer; font-size:12px; }
button.secondary { background:#eef1f7; color:#26314b; }
button:focus-visible { outline:3px solid #f4b942; outline-offset:2px; }
input[type=range] { width:100%; accent-color:#d69d1b; }
.time { width:86px; color:#586277; font:700 12px ui-monospace,SFMono-Regular,Menlo,monospace; text-align:right; }
.note { color:#697386; font-size:11px; line-height:1.4; margin-top:9px; }
.details { margin-top:20px; display:grid; grid-template-columns:1.15fr .85fr; gap:14px; }
.card { background:#fff; border:1px solid var(--line); border-radius:16px; padding:17px 18px; }
.card h2 { margin:0 0 9px; font-size:14px; letter-spacing:.01em; }
.card p,.card li { color:#586277; font-size:12px; line-height:1.55; }
.card p { margin:0 0 8px; }
.card ul { padding-left:18px; margin:0; }
.card a { color:#1a68a7; overflow-wrap:anywhere; }
.kpi { display:inline-flex; align-items:center; gap:6px; margin:2px 6px 6px 0; padding:6px 8px; border-radius:8px; background:#f5f7fb; color:#27324a; font-size:11px; font-weight:800; }
@media (max-width:700px) { .header { display:block; } .approval { display:inline-block; margin-top:12px; } .details { grid-template-columns:1fr; } .shell { padding-top:17px; } }
@media (prefers-reduced-motion:reduce) { * { scroll-behavior:auto !important; } }
</style>
</head>
<body>
<div class="shell">
  <header class="header">
    <div>
      <div class="eyebrow">Benaqaab India · HTML-first workflow</div>
      <h1>SIR voter-list controversy — approval preview</h1>
      <p class="subtitle">New clean full-screen Short composition with Hinglish narration, English captions, attributed evidence beats and a loop-ready viewer CTA. This is the HTML video preview; no MP4 has been rendered.</p>
    </div>
    <div class="approval">WAITING FOR YOUR APPROVAL</div>
  </header>
  <div class="stage-wrap">
    <div class="stage-frame">
      <canvas id="stage" width="1080" height="1920" aria-label="Vertical video preview"></canvas>
      <div class="badge">HTML PREVIEW · NOT FINAL MP4</div>
    </div>
  </div>
  <section class="controls" aria-label="Preview controls">
    <div class="control-row">
      <button id="play">Play preview</button>
      <button id="restart" class="secondary">Restart</button>
      <button id="mute" class="secondary">Mute</button>
      <input id="seek" type="range" min="0" max="101.5" step="0.01" value="0" aria-label="Seek preview">
      <div class="time" id="time">0:00 / 1:41</div>
    </div>
    <div class="note">Click Play preview to hear the narration. Scrub the timeline to inspect the visual beats. Approval requested: reply <strong>approved</strong> only after reviewing the composition; then the MP4 render can begin.</div>
  </section>
  <section class="details">
    <div class="card">
      <h2>What changed from the old cut</h2>
      <span class="kpi">1080×1920 · 30 fps target</span><span class="kpi">1:41 narration</span><span class="kpi">No dashboard HUD</span><span class="kpi">Presenter-free</span>
      <ul>
        <li>Frame 0 starts on the concrete voter-list stake, without a greeting or intro card.</li>
        <li>Edge-to-edge illustrative visuals, compact bottom-left labels and limited top glass cards.</li>
        <li>Draft-roll figure is explicitly separated from permanent deletion; ECI, Indian Express and Supreme Court positions are attributed.</li>
        <li>Final beat includes the official portal, Like and Subscribe CTA, plus a comment question.</li>
      </ul>
    </div>
    <div class="card">
      <h2>Research links</h2>
      <p><a href="https://www.eci.gov.in/eci/public/api/document?id=17536" target="_blank" rel="noopener">ECI press note · 26 Sep 2026</a></p>
      <p><a href="https://api.sci.gov.in/supremecourt/2025/35785/35785_2025_1_1501_71617_Judgement_27-May-2026.pdf" target="_blank" rel="noopener">Supreme Court judgment · 27 May 2026</a></p>
      <p><a href="https://indianexpress.com/article/express-exclusive/election-commission-illegal-changes-form-6-gyanesh-kumar-10889714/" target="_blank" rel="noopener">Indian Express · Form 6 report</a></p>
      <p><a href="https://www.thehindu.com/news/national/supreme-court-notice-to-eci-centre-on-plea-challenging-decisions-taken-by-cec-led-poll-panel/article71546395.ece" target="_blank" rel="noopener">The Hindu · 5 Oct clarification report</a></p>
      <p><a href="https://voters.eci.gov.in/" target="_blank" rel="noopener">Official Voters’ Services Portal</a></p>
    </div>
  </section>
</div>
<audio id="audio" preload="auto"></audio>
<script>
const IMAGES = __IMAGES__;
const AUDIO = __AUDIO__;
const SCENES = __SCENES__;
const CUES = __CUES__;
const canvas = document.getElementById('stage');
const ctx = canvas.getContext('2d');
const audio = document.getElementById('audio');
audio.src = AUDIO;
const playBtn = document.getElementById('play');
const restartBtn = document.getElementById('restart');
const muteBtn = document.getElementById('mute');
const seek = document.getElementById('seek');
const timeLabel = document.getElementById('time');
const loaded = IMAGES.map(src => { const im = new Image(); im.src = src; return im; });
const W = canvas.width, H = canvas.height;
let frame = 0;
function clamp(v,a,b){ return Math.max(a,Math.min(b,v)); }
function fmt(t){ const s=Math.max(0,Math.floor(t)); return Math.floor(s/60)+':'+String(s%60).padStart(2,'0'); }
function wrap(text, maxChars){ const words=text.split(' '), lines=[]; let line=''; for(const w of words){ if((line+' '+w).trim().length>maxChars){ lines.push(line); line=w; } else line=(line+' '+w).trim(); } if(line) lines.push(line); return lines; }
function roundedRect(x,y,w,h,r){ ctx.beginPath(); ctx.moveTo(x+r,y); ctx.arcTo(x+w,y,x+w,y+h,r); ctx.arcTo(x+w,y+h,x,y+h,r); ctx.arcTo(x,y+h,x,y,r); ctx.arcTo(x,y,x+w,y,r); ctx.closePath(); }
function sceneAt(t){ return SCENES.find(s=>t>=s.a && t<s.b) || SCENES[SCENES.length-1]; }
function cueAt(t){ return CUES.find(s=>t>=s.a && t<s.b) || CUES[CUES.length-1]; }
function draw(t){
  const sc=sceneAt(t), cue=cueAt(t), im=loaded[sc.im];
  ctx.clearRect(0,0,W,H); ctx.fillStyle='#0b0d15'; ctx.fillRect(0,0,W,H);
  if(im.complete && im.naturalWidth){
    const p=clamp((t-sc.a)/(sc.b-sc.a),0,1);
    const scale=Math.max(W/im.naturalWidth,H/im.naturalHeight)*1.08;
    const dw=im.naturalWidth*scale, dh=im.naturalHeight*scale;
    const drift=((sc.im%2?1:-1)*p*18) - 9;
    ctx.save(); ctx.translate((W-dw)/2+drift,(H-dh)/2 + p*8); ctx.globalAlpha=1; ctx.drawImage(im,0,0,dw,dh); ctx.restore();
  }
  const top=ctx.createLinearGradient(0,0,0,700); top.addColorStop(0,'rgba(7,10,23,.88)'); top.addColorStop(.55,'rgba(7,10,23,.18)'); top.addColorStop(1,'rgba(7,10,23,0)'); ctx.fillStyle=top; ctx.fillRect(0,0,W,700);
  const bottom=ctx.createLinearGradient(0,1250,0,H); bottom.addColorStop(0,'rgba(7,10,23,0)'); bottom.addColorStop(.7,'rgba(7,10,23,.68)'); bottom.addColorStop(1,'rgba(7,10,23,.94)'); ctx.fillStyle=bottom; ctx.fillRect(0,1250,W,670);
  ctx.fillStyle='rgba(4,7,16,.46)'; ctx.fillRect(0,0,W,4);
  // compact logo, always top-right
  ctx.fillStyle='#f4b942'; ctx.beginPath(); ctx.arc(969,72,13,0,Math.PI*2); ctx.fill(); ctx.fillStyle='#11182d'; ctx.font='900 14px Arial'; ctx.textAlign='center'; ctx.textBaseline='middle'; ctx.fillText('B',969,72);
  ctx.fillStyle='rgba(255,255,255,.88)'; ctx.font='800 19px Arial'; ctx.textAlign='right'; ctx.textBaseline='alphabetic'; ctx.fillText('BENAQAAB INDIA',1032,105);
  // scene label
  ctx.fillStyle=sc.accent; ctx.fillRect(62,113,54,4); ctx.fillStyle='rgba(255,255,255,.85)'; ctx.font='900 17px Arial'; ctx.textAlign='left'; ctx.fillText(sc.kicker,62,102);
  // selective top glass card
  if(sc.title){
    const cardY=148, cardH=196; roundedRect(54,cardY,972,cardH,24); ctx.fillStyle='rgba(10,16,35,.60)'; ctx.fill(); ctx.strokeStyle='rgba(255,255,255,.16)'; ctx.lineWidth=2; ctx.stroke();
    ctx.fillStyle='#fff'; ctx.font='900 62px Arial'; ctx.textAlign='left'; ctx.textBaseline='alphabetic'; ctx.fillText(sc.title[0],86,cardY+86);
    ctx.fillStyle=sc.accent; ctx.font='900 62px Arial'; ctx.fillText(sc.title[1],86,cardY+157);
  }
  // compact bottom-left pill
  const pillW=Math.max(210,ctx.measureText(sc.pill).width+54); roundedRect(62,1540,pillW,52,26); ctx.fillStyle='rgba(11,20,42,.80)'; ctx.fill(); ctx.fillStyle=sc.accent; ctx.fillRect(79,1554,4,24); ctx.fillStyle='#fff'; ctx.font='900 20px Arial'; ctx.textAlign='left'; ctx.textBaseline='middle'; ctx.fillText(sc.pill,96,1566);
  // captions, never a huge full-width box
  const lines=wrap(cue.text,28); const subLines=wrap(cue.sub,38); let y=1660;
  ctx.save(); ctx.shadowColor='rgba(0,0,0,.7)'; ctx.shadowBlur=16; ctx.fillStyle='#fff'; ctx.font='900 43px Arial'; ctx.textAlign='left'; ctx.textBaseline='alphabetic';
  for(const line of lines){ ctx.fillText(line,62,y); y+=53; }
  ctx.shadowBlur=8; ctx.fillStyle=sc.accent; ctx.font='800 21px Arial'; for(const line of subLines){ ctx.fillText(line,64,y+4); y+=29; } ctx.restore();
  // source attribution, only in the scene where it matters
  ctx.fillStyle='rgba(255,255,255,.72)'; ctx.font='600 16px Arial'; ctx.textAlign='right'; ctx.fillText(sc.source,1018,1834);
  // CTA motion near the end
  if(t>=94){ const q=clamp((t-94)/2,0,1), x=62+(1-q)*140; roundedRect(x,1450,956,66,33); ctx.fillStyle='rgba(244,185,66,.94)'; ctx.fill(); ctx.fillStyle='#141a31'; ctx.font='900 24px Arial'; ctx.textAlign='center'; ctx.fillText('LIKE VIDEO ★     SUBSCRIBE NOW ▶',x+478,1491); }
  // tiny end bridge to loop
  if(t>=99.5){ ctx.fillStyle='rgba(255,255,255,.86)'; ctx.font='700 16px Arial'; ctx.textAlign='center'; ctx.fillText('NOW CHECK THE NAME YOU STARTED WITH',540,1880); }
}
function render(){ const t=audio.currentTime||0; seek.value=t; timeLabel.textContent=fmt(t)+' / 1:41'; draw(t); frame=requestAnimationFrame(render); }
playBtn.addEventListener('click', async()=>{ if(audio.paused){ try{await audio.play();}catch(e){} playBtn.textContent='Pause'; } else {audio.pause(); playBtn.textContent='Play preview';} });
restartBtn.addEventListener('click',()=>{audio.currentTime=0; audio.pause(); playBtn.textContent='Play preview';});
muteBtn.addEventListener('click',()=>{audio.muted=!audio.muted; muteBtn.textContent=audio.muted?'Unmute':'Mute';});
seek.addEventListener('input',()=>{audio.currentTime=Number(seek.value);});
audio.addEventListener('ended',()=>{playBtn.textContent='Replay preview';});
draw(0); render();
</script>
</body>
</html>'''

html_doc = html_doc.replace('__IMAGES__', json.dumps(images))
html_doc = html_doc.replace('__AUDIO__', json.dumps(audio))
html_doc = html_doc.replace('__SCENES__', json.dumps(scenes, ensure_ascii=False))
html_doc = html_doc.replace('__CUES__', json.dumps(cues, ensure_ascii=False))
OUT.write_text(html_doc, encoding='utf-8')
print(f'Wrote {OUT} ({OUT.stat().st_size/1024/1024:.1f} MB)')