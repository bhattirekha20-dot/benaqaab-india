/* ============================================================================
   motion_library.js — Benaqaab India shared motion engine
   ----------------------------------------------------------------------------
   Every function here was written and TESTED in this workspace. The demo pages
   that used to hold this code (`viz/ae_motion_lab.html`, `viz/transition_lab.html`)
   were deleted at the user's request on 2 October 2026; the engine is kept
   because it is what puts the official CapCut transitions and the After Effects
   techniques into our films.

     1. Ease / EASE         quad..quint, expo, back, elastic, linear
     2. spring()            real spring physics (mass / stiffness / damping / v0)
     3. clamp, lerp         numeric helpers
     4. mulberry, hash, vnoise, noise1, wobble    seeded, time-addressable randomness
     5. mk, tint, blurCanvas                      offscreen image helpers
     6. bloom, chromatic, lightWrap, vignette, grain   the grade stack, in order
     7. makeTransitions(A, B)                     the 24 official-named transitions, u = 0..1

   Naming note: the 24 transitions carry the official CapCut names and verified
   default durations (see knowledge/capcut_alight_research/CATALOG_TRANSITIONS.json).
   The implementations are faithful native reinterpretations of the motion, not
   bit-exact copies of CapCut's proprietary shaders.

   Contract: everything is a pure function of time. No Math.random() at draw time,
   no wall clock, no network — that is what lets the renderer capture any frame in
   any order and get byte-identical pixels.
   ========================================================================== */
(function (root) {
'use strict';

// 1 — easing -----------------------------------------------------------------
const clamp = (v,a,b)=>v<a?a:v>b?b:v, lerp=(a,b,t)=>a+(b-a)*t;
const E = {
  linear:t=>t, outQuad:t=>t*(2-t), inQuad:t=>t*t,
  outCubic:t=>(--t)*t*t+1, inOutCubic:t=>t<.5?4*t*t*t:(t-1)*(2*t-2)*(2*t-2)+1,
  inCubic:t=>t*t*t, outQuint:t=>1+(--t)*t*t*t*t, outExpo:t=>t===1?1:1-Math.pow(2,-10*t),
  outBack:(t,s=1.7)=>1+(--t)*t*((s+1)*t+s),
  outElastic:t=>t===0?0:t===1?1:Math.pow(2,-10*t)*Math.sin((t*10-.75)*(2*Math.PI/3))+1
};
function spring(t,mass=1,stiffness=150,damping=18,v0=0){
  const w0=Math.sqrt(stiffness/mass), z=damping/(2*Math.sqrt(stiffness*mass));
  if(z<1){const wd=w0*Math.sqrt(1-z*z), B=(z*w0-(-v0))/wd;
    return 1-(Math.exp(-t*z*w0)*(Math.cos(wd*t)+B*Math.sin(wd*t)));}
  const B=-v0+w0; return 1-((1+B*t)*Math.exp(-t*w0));
}
/* seeded value noise — deterministic, a pure function of time */
const hash=(i,s)=>{const x=Math.sin(i*127.1+s*311.7)*43758.5453; return x-Math.floor(x);};
const vnoise=(x,s)=>{const i=Math.floor(x),f=x-i,u=f*f*(3-2*f); return lerp(hash(i,s),hash(i+1,s),u);};
const EASE={
  linear:t=>t,
  outQuad:t=>t*(2-t),
  outCubic:t=>(--t)*t*t+1,
  inOutCubic:t=>t<.5?4*t*t*t:(t-1)*(2*t-2)*(2*t-2)+1,
  outQuint:t=>1+(--t)*t*t*t*t,
  outExpo:t=>t===1?1:1-Math.pow(2,-10*t),
  outBack:(t,s=1.70158)=>1+(--t)*t*((s+1)*t+s),
  outElastic:t=>t===0?0:t===1?1:Math.pow(2,-10*t)*Math.sin((t*10-.75)*(2*Math.PI/3))+1
};
const Ease = Object.assign({}, E, EASE);   // union: transitions use E, the AE skill uses EASE

// 4 — seeded randomness ------------------------------------------------------
function mulberry(a){a>>>=0;return()=>{a+=0x6D2B79F5;let t=a;t=Math.imul(t^t>>>15,t|1);t^=t+Math.imul(t^t>>>7,t|61);return((t^t>>>14)>>>0)/4294967296;};}
// 5 — image helpers ----------------------------------------------------------
function mk(w,h){ const cv=document.createElement('canvas'); cv.width=w; cv.height=h; return cv; }
function tint(src,color,keepAlpha){
  const cv=mk(src.width,src.height), c=cv.getContext('2d');
  c.drawImage(src,0,0);
  if(keepAlpha){ c.globalCompositeOperation='destination-in'; c.drawImage(src,0,0); }
  c.globalCompositeOperation='multiply'; c.fillStyle=color; c.fillRect(0,0,cv.width,cv.height);
  if(keepAlpha){ c.globalCompositeOperation='destination-in'; c.drawImage(src,0,0); }
  return cv;
}
function blurCanvas(src,k){
  const s=clamp(1+k*22,1,26), sw=Math.max(1,Math.round(src.width/s)), sh=Math.max(1,Math.round(src.height/s));
  const small=mk(sw,sh), sc=small.getContext('2d'); sc.imageSmoothingEnabled=true; sc.drawImage(src,0,0,sw,sh);
  const out=mk(src.width,src.height), oc=out.getContext('2d'); oc.imageSmoothingEnabled=true;
  oc.drawImage(small,0,0,out.width,out.height);
  return out;
}
// 6 — grade stack ------------------------------------------------------------
/* ---------------- grade stack, in the order that matters (SKILLS_AFTER_EFFECTS.md 3.5) ----- */
function bloom(c, src, w, h, strength, radius){
  const b = blurCanvas(src, radius === undefined ? 0.5 : radius);
  c.save(); c.globalCompositeOperation = 'lighter'; c.globalAlpha = strength === undefined ? 0.45 : strength;
  c.drawImage(b, 0, 0, w, h); c.restore();
}
function chromatic(c, src, w, h, px){
  const off = px === undefined ? 2 : px, red = tint(src, '#ff3040', false), cyan = tint(src, '#16e0ff', false);
  c.save(); c.globalCompositeOperation = 'lighter'; c.globalAlpha = 0.35;
  c.drawImage(red, -off, 0, w, h); c.drawImage(cyan, off, 0, w, h); c.restore();
}
function lightWrap(c, bg, x, y, w, h, amount){
  const soft = blurCanvas(bg, 0.55);
  c.save(); c.globalCompositeOperation = 'screen'; c.globalAlpha = amount === undefined ? 0.35 : amount;
  c.drawImage(soft, x - w * 0.06, y - h * 0.06, w * 1.12, h * 1.12); c.restore();
}
function vignette(c, w, h, amount){
  const g = c.createRadialGradient(w/2, h/2, Math.min(w,h) * 0.36, w/2, h/2, Math.max(w,h) * 0.75);
  g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(0.55, 'rgba(0,0,0,0.10)');
  g.addColorStop(1, 'rgba(0,0,0,' + (amount === undefined ? 0.5 : amount).toFixed(3) + ')');
  c.fillStyle = g; c.fillRect(0, 0, w, h);
}
function grain(c, w, h, frameIndex, amount){
  const r = mulberry(9973 + Math.floor(frameIndex) * 7), a = amount === undefined ? 0.12 : amount;
  c.save(); c.globalAlpha = a; c.fillStyle = '#ffffff';
  for (let i = 0, n = Math.round(w * h / 1400); i < n; i++) c.fillRect(Math.floor(r() * w), Math.floor(r() * h), 1, 1);
  c.restore();
}
// 7 — the 24 transitions, as a factory so the two shots are injected ---------
function makeTransitions(A, B) {
  const Ared = tint(A, '#ff3040', true), Acyan = tint(A, '#16e0ff', true);
  const Bred = tint(B, '#ff3040', true), Bcyan = tint(B, '#16e0ff', true);

/* each: fn(ctx, u, w, h) — u 0..1, A is the outgoing shot, B the incoming  */
const T = {};

T['Dissolve · 叠化'] = (c,u,w,h)=>{                      // official 0.50 s (free)
  const s=lerp(1.05,1,E.outCubic(u));
  c.drawImage(A,0,0,w,h);
  c.globalAlpha=E.inOutCubic(u);
  c.drawImage(B,(w-w*s)/2,(h-h*s)/2,w*s,h*s); c.globalAlpha=1;
};

T['White Flash'] = (c,u,w,h)=>{                          // official 0.40 s (free)
  c.drawImage(A,0,0,w,h);
  if(u<.5){ c.fillStyle='#ffffff'; c.globalAlpha=E.inQuad(u*2); c.fillRect(0,0,w,h); }
  else { c.drawImage(B,0,0,w,h); c.fillStyle='#ffffff'; c.globalAlpha=1-E.outCubic((u-.5)*2); c.fillRect(0,0,w,h); }
  c.globalAlpha=1;
};

T['Cutout Flip'] = (c,u,w,h)=>{                          // official 0.80 s (free)
  const half=w/2, opening=u<.5, th=opening?u*2:(u-.5)*2;
  const s=Math.max(.045, Math.abs(Math.cos(th*Math.PI/2)));
  c.drawImage(B,0,0,w,h);                          // the next shot sits behind the doors
  const door=(x0,dir)=>{
    const dw=half*s, x = dir<0 ? half-dw : half;
    c.save(); c.beginPath(); c.rect(x0,0,half,h); c.clip();
    c.drawImage(opening?A:B, x, 0, dw, h);         // phase 1: A peels away · phase 2: doors close again
    const g=c.createLinearGradient(half,0,x,0), sh=(1-s)*.5;
    g.addColorStop(0,'rgba(0,0,0,'+sh.toFixed(3)+')'); g.addColorStop(1,'rgba(0,0,0,0)');
    c.fillStyle=g; c.fillRect(x0,0,half,h);
    c.restore();
  };
  door(0,-1); door(half,1);
};

T['Fold Over'] = (c,u,w,h)=>{                            // official 1.00 s (free)
  c.drawImage(A,0,0,w,h);
  const fw=w*.5, x=lerp(w, -fw*.1, E.inOutCubic(u));
  c.save(); c.beginPath(); c.rect(x,0,w-x,h); c.clip();
  c.drawImage(B,0,0,w,h); c.restore();
  // the fold panel itself: B squeezed into the moving band, fading out by u=1 so the
  // cut ends EXACTLY on B (fix 2026-10-05: the panel used to linger at the cut end and pop)
  const sh=Math.max(.05, 1-u), fade=clamp(1-u,0,1);
  if (fade>0.01){
    c.save(); c.globalAlpha=fade; c.beginPath(); c.rect(x,0,fw,h); c.clip();
    c.drawImage(B, x, 0, fw*sh, h);
    const g=c.createLinearGradient(x,0,x+fw,0);
    g.addColorStop(0,'rgba(0,0,0,.55)'); g.addColorStop(1,'rgba(0,0,0,0)');
    c.fillStyle=g; c.fillRect(x,0,fw,h); c.restore();
  }
};

T['Push Away 2'] = (c,u,w,h)=>{                          // official 1.00 s
  // fix 2026-10-05: the incoming shot must settle at scale 1 so the cut ends EXACTLY on B
  // (it used to end at 0.88 and the first direct frame after the cut popped).
  const e=E.inOutCubic(u), scA=lerp(1,.88,e), scB=lerp(1.12,1,e);
  c.drawImage(A,(w-w*scA)/2 + (-w*e), (h-h*scA)/2, w*scA, h*scA);
  c.drawImage(B,(w-w*scB)/2 + (w*(1-e)), (h-h*scB)/2, w*scB, h*scB);
};

T['Corner Slide'] = (c,u,w,h)=>{                         // official 1.00 s
  const e=E.outQuart?E.outQuart(u):E.outCubic(u);
  c.drawImage(A,0,0,w,h);
  c.save(); c.beginPath(); c.moveTo(w,h); c.lineTo(w,h); c.lineTo(w,h);
  c.rect(w-w*e, h-h*e, w*e, h*e); c.clip();
  c.drawImage(B, w-w*e, h-h*e, w, h); c.restore();
  c.save(); c.globalCompositeOperation='multiply';
  const g=c.createLinearGradient(w-w*e,h-h*e,w,h);
  g.addColorStop(0,'rgba(255,255,255,1)'); g.addColorStop(.25,'rgba(120,120,120,1)'); g.addColorStop(1,'rgba(255,255,255,1)');
  c.fillStyle=g; c.fillRect(w-w*e,h-h*e,w*e,h*e); c.restore();
};

T['Swipe Left'] = (c,u,w,h)=>{                           // official 1.30 s
  const e=E.outQuint(u);
  c.drawImage(A,0,0,w,h);
  c.save(); c.shadowColor='rgba(0,0,0,.65)'; c.shadowBlur=w*.05; c.shadowOffsetX=-w*.02;
  c.beginPath(); c.rect(w-w*e,0,w*e,h); c.clip();
  c.drawImage(B,w-w*e,0,w,h); c.restore();
};

T['Shrink'] = (c,u,w,h)=>{                               // official 1.10 s
  const e=E.inOutCubic(u), sc=lerp(1,.62,e), rot=lerp(0,-.10,e);
  c.drawImage(B,(w-w*.92)/2,(h-h*.92)/2,w*.92,h*.92);
  c.save(); c.translate(w/2,h/2); c.rotate(rot);
  c.globalAlpha=1-e*.85; c.drawImage(A,-w*sc/2,-h*sc/2,w*sc,h*sc); c.restore(); c.globalAlpha=1;
};

T['Drop & Expand'] = (c,u,w,h)=>{                        // official 1.00 s
  c.drawImage(A,0,0,w,h);
  const k=spring(clamp(u*1.15,0,1.9), 1, 36, 7.2, 0);   // softer: settles ~u 0.85
  const y=lerp(-h*.42,0,k), s=lerp(.58,1,clamp(k,0,1.15));
  c.save(); c.translate(w/2, h/2+y);
  c.drawImage(B, -w*s/2, -h*s/2, w*s, h*s);
  c.restore();
  if(clamp(k,0,1)<.999){ // contact shadow while the shot is still falling
    const sh=clamp(1-clamp(k,0,1),0,1);
    const g=c.createLinearGradient(0,0,0,h*.16);
    g.addColorStop(0,'rgba(0,0,0,'+(.45*sh).toFixed(3)+')'); g.addColorStop(1,'rgba(0,0,0,0)');
    c.fillStyle=g; c.fillRect(0,0,w,h*.16);
  }
};

T['Snap Zoom'] = (c,u,w,h)=>{                            // official 0.90 s
  if(u<.5){ const e=E.inCubic(u*2), s=lerp(1,1.75,e);
    c.globalAlpha=1; c.drawImage(blurCanvas(A,e*.55),(w-w*s)/2,(h-h*s)/2,w*s,h*s); }
  else { const e=E.outExpo((u-.5)*2), s=lerp(.72,1,E.outCubic((u-.5)*2));
    c.drawImage(B,(w-w*s)/2,(h-h*s)/2,w*s,h*s);
    c.fillStyle='#fff'; c.globalAlpha=(1-e)*.35; c.fillRect(0,0,w,h); }
  c.globalAlpha=1;
};

T['Zoom to Change'] = (c,u,w,h)=>{                       // official 0.80 s
  const e=E.inOutCubic(u), sA=lerp(1,1.9,e), sB=lerp(.55,1,e);
  c.drawImage(blurCanvas(A,e*.5),(w-w*sA)/2,(h-h*sA)/2,w*sA,h*sA);
  c.globalAlpha=e; c.drawImage(blurCanvas(B,(1-e)*.35),(w-w*sB)/2,(h-h*sB)/2,w*sB,h*sB); c.globalAlpha=1;
};

T['Jerky Camera'] = (c,u,w,h)=>{                         // official 0.90 s
  const steps=6, si=Math.floor(u*steps), seen=si>=3;
  const src=seen?B:A, n=(k)=>vnoise(k*7.3+si*13.7,41)*2-1;
  const k=(si+1)%2?1:-1;
  c.drawImage(src, -n(1)*w*.035*k, -n(2)*h*.028*k, w*1.06, h*1.06);
  c.fillStyle='rgba(0,0,0,'+(.10+(si%2)*.14)+')'; c.fillRect(0,0,w,h);
};

T['Center Rotate'] = (c,u,w,h)=>{                        // official 1.00 s
  const e=E.inOutCubic(u);
  c.save(); c.translate(w/2,h/2);
  c.rotate(-e*.55); const sA=lerp(1,.72,e); c.globalAlpha=1-e;
  c.drawImage(A,-w*sA/2,-h*sA/2,w*sA,h*sA); c.restore(); c.globalAlpha=1;
  c.save(); c.translate(w/2,h/2);
  c.rotate((1-e)*.95); const sB=lerp(.55,1,e);
  c.drawImage(B,-w*sB/2,-h*sB/2,w*sB,h*sB); c.restore();
};

T['Cube Rotate'] = (c,u,w,h)=>{                          // official 1.00 s
  const th=clamp(u,0,1)*Math.PI/2;                 // 0 -> 90 degrees
  const front=Math.max(.02,Math.cos(th)), side=Math.max(.02,Math.sin(th));
  const k=.72, fw=w*front, sw=w*side*k;
  c.fillStyle='#05070d'; c.fillRect(0,0,w,h);
  c.save(); c.beginPath(); c.rect(0,0,fw,h); c.clip();     // front face = A
  c.drawImage(A,0,0,fw,h);
  c.fillStyle='rgba(0,0,0,'+(0.55*side).toFixed(3)+')'; c.fillRect(0,0,fw,h); c.restore();
  c.save(); c.beginPath(); c.rect(fw,0,sw,h); c.clip();    // side face = B
  c.drawImage(B,fw,0,sw,h);
  const g=c.createLinearGradient(fw,0,fw+sw,0);
  g.addColorStop(0,'rgba(255,255,255,'+(0.18*side).toFixed(3)+')');
  g.addColorStop(1,'rgba(0,0,0,'+(0.30*side).toFixed(3)+')');
  c.fillStyle=g; c.fillRect(fw,0,sw,h); c.restore();
  c.fillStyle='rgba(255,255,255,'+(0.30*Math.min(front,side)).toFixed(3)+')';
  c.fillRect(fw-Math.max(1,w*.0015),0,Math.max(2,w*.003),h);
};

T['Flip Page'] = (c,u,w,h)=>{                            // official 0.70 s
  const e=clamp(u,0,1)*Math.PI, s=Math.abs(Math.cos(e));
  c.drawImage(B,0,0,w,h);                                   // the next page underneath
  const pw=w*Math.max(.03,s);
  c.save(); c.beginPath(); c.rect(0,0,pw,h); c.clip();
  c.drawImage(Math.cos(e) > 0 ? A : B, 0, 0, pw, h);   // back of the page = the next shot
  const dk=Math.min(.6,0.45*(1-s)*1.4);
  c.fillStyle='rgba(0,0,0,'+dk.toFixed(3)+')'; c.fillRect(0,0,pw,h);
  const g=c.createLinearGradient(0,0,pw,0);
  g.addColorStop(0,'rgba(255,255,255,.22)'); g.addColorStop(.6,'rgba(0,0,0,0)');
  g.addColorStop(1,'rgba(0,0,0,.45)'); c.fillStyle=g; c.fillRect(0,0,pw,h); c.restore();
  c.save(); c.shadowColor='rgba(0,0,0,.55)'; c.shadowBlur=w*.045; c.shadowOffsetX=w*.012;
  c.fillStyle='rgba(255,255,255,.30)'; c.fillRect(pw,0,Math.max(2,w*.0025),h); c.restore();
};

T['Paper Flip'] = (c,u,w,h)=>{                           // official 1.00 s
  const e=E.inOutCubic(u), s=Math.cos(e*Math.PI), sh=Math.max(.035,Math.abs(s));
  c.fillStyle='#05070d'; c.fillRect(0,0,w,h);
  c.save(); c.translate(w/2,h/2); c.scale(1,sh); c.translate(-w/2,-h/2);
  c.drawImage(s>0?A:B,0,0,w,h);
  c.fillStyle='rgba(0,0,0,'+(0.5*(1-sh)).toFixed(3)+')'; c.fillRect(0,0,w,h);
  c.restore();
  c.fillStyle='rgba(255,255,255,'+(0.28*(1-sh)).toFixed(3)+')';
  c.fillRect(0, h/2-h*sh/2-Math.max(1,h*.002), w, Math.max(2,h*.004));
  c.fillRect(0, h/2+h*sh/2-Math.max(1,h*.002), w, Math.max(2,h*.004));
};

T['Kaleidoscope'] = (c,u,w,h)=>{                         // official 1.45 s
  const e=E.inOutCubic(u), N=8, R=Math.hypot(w,h);
  c.drawImage(A,0,0,w,h);
  c.save(); c.translate(w/2,h/2);
  for(let i=0;i<N;i++){
    c.save(); c.rotate(i*(Math.PI*2/N) + e*1.2);
    c.beginPath(); c.moveTo(0,0);
    c.arc(0,0,R, -Math.PI/N + .001, Math.PI/N - .001); c.closePath(); c.clip();
    const s=lerp(1.25,.95,e);
    c.globalAlpha=clamp(u*1.7-0.12,0,1);
    c.drawImage(B, -w*s/2, -h*s/2 + Math.hypot(w,h)*.16, w*s, h*s);
    c.restore();
  }
  c.restore(); c.globalAlpha=1;
};

T['Whirl'] = (c,u,w,h)=>{                                // official 1.50 s
  const e=E.inOutCubic(u);
  c.save(); c.translate(w/2,h/2); c.rotate(-e*1.9); const sA=lerp(1,.45,e);
  c.globalAlpha=1-e; c.drawImage(blurCanvas(A,e*.4),-w*sA/2,-h*sA/2,w*sA,h*sA); c.restore(); c.globalAlpha=1;
  c.save(); c.translate(w/2,h/2); c.rotate((1-e)*2.4); const sB=lerp(.4,1,E.outCubic(e));
  c.globalAlpha=clamp(e*1.4-.2,0,1); c.drawImage(B,-w*sB/2,-h*sB/2,w*sB,h*sB); c.restore(); c.globalAlpha=1;
};

T['Rainbow Twist'] = (c,u,w,h)=>{                        // official 1.00 s
  const e=E.inOutCubic(u);
  c.save(); c.translate(w/2,h/2); c.rotate((1-e)*1.6);
  c.drawImage(A,-w/2,-h/2,w,h); c.restore();
  c.save(); c.translate(w/2,h/2); c.rotate(-e*1.6);
  c.globalAlpha=clamp(e*1.3-.1,0,1); c.drawImage(B,-w/2,-h/2,w,h); c.restore(); c.globalAlpha=1;
  // hue ring sweeping out of the centre, built as a transparent-edged band so it
  // never needs a destination-in mask (that erased the whole frame)
  c.save(); c.globalCompositeOperation='lighter'; c.translate(w/2,h/2);
  const rr=lerp(w*.05,Math.hypot(w,h)*.72,e), band=Math.max(w*.04, rr*.42);
  const g=c.createRadialGradient(0,0,Math.max(1,rr-band),0,0,rr+band);
  for(let i=0;i<=8;i++){
    const f=i/8, a=Math.sin(f*Math.PI)*0.34*clamp((1-u)*1.6+.25,0,1);
    g.addColorStop(f, `hsla(${Math.round((i*45+u*280)%360)},100%,62%,${a.toFixed(3)})`);
  }
  c.fillStyle=g; c.beginPath(); c.arc(0,0,rr+band,0,6.2832); c.fill();
  c.restore();
};

T['Film Burn'] = (c,u,w,h)=>{                            // official 0.70 s
  c.drawImage(u<.5?A:B,0,0,w,h);
  const lead=lerp(-w*.12, w*1.12, u);
  c.save(); c.globalCompositeOperation='lighter';
  for(let i=0;i<7;i++){
    const off=vnoise(i*3.1+u*6,7)*w*.07;
    const x=lead+off, ww=w*(.09+i*.035);
    const g=c.createLinearGradient(x-ww,0,x+ww,0);
    g.addColorStop(0,'rgba(255,120,20,0)'); g.addColorStop(.45,'rgba(255,190,90,'+(.55-i*.05)+')');
    g.addColorStop(.55,'rgba(255,255,225,'+(.5-i*.05)+')'); g.addColorStop(1,'rgba(255,80,10,0)');
    c.fillStyle=g; c.fillRect(x-ww,0,ww*2,h);
  }
  c.restore();
  const e=clamp((u-.35)/.5,0,1);
  if(e>0){ c.save(); c.globalAlpha=e; c.drawImage(B,0,0,w,h); c.restore(); }
};

T['Light Leaks'] = (c,u,w,h)=>{                          // official 1.00 s
  c.drawImage(A,0,0,w,h);
  c.save(); c.globalAlpha=E.inOutCubic(u); c.drawImage(B,0,0,w,h); c.restore();
  c.save(); c.globalCompositeOperation='lighter'; c.translate(w/2,h/2); c.rotate(-.42);
  for(let i=0;i<4;i++){
    const ph=(u*1.7 + i*.23)%1.3 - .15, x=lerp(-w, w, ph), ww=w*(.05+i*.03);
    const g=c.createLinearGradient(x-ww,0,x+ww,0);
    g.addColorStop(0,'rgba(255,150,60,0)'); g.addColorStop(.5,`rgba(255,${180+i*10},${110+i*20},.42)`);
    g.addColorStop(1,'rgba(255,90,30,0)');
    c.fillStyle=g; c.fillRect(x-ww,-h,ww*2,h*2);
  }
  c.restore();
};

T['Neon'] = (c,u,w,h)=>{                                 // official 0.60 s
  c.drawImage(A,0,0,w,h);
  const e=E.outCubic(u);
  c.save(); c.beginPath(); c.rect(0,0,w*e,h); c.clip(); c.drawImage(B,0,0,w,h); c.restore();
  c.save(); c.globalCompositeOperation='lighter';
  const bars=5;
  for(let i=0;i<bars;i++){
    const x=w*e - w*.05 - i*w*.035;
    const hue=i%2? '#16e0ff' : '#ff2fd0';
    const g=c.createLinearGradient(x-w*.06,0,x+w*.06,0);
    g.addColorStop(0,'rgba(0,0,0,0)'); g.addColorStop(.5,hue); g.addColorStop(1,'rgba(0,0,0,0)');
    c.globalAlpha=.55*(1-i/bars); c.fillStyle=g; c.fillRect(x-w*.06,0,w*.12,h);
  }
  c.globalAlpha=1; c.restore();
};

T['Signal Glitch 2'] = (c,u,w,h)=>{                      // official 0.67 s
  const settle = u<.5 ? 1 : clamp(1-(u-.5)/.35, 0, 1);    // decays to zero -> ends clean on B
  const hard=u<.5?A:B, other=u<.5?B:A;
  c.drawImage(hard,0,0,w,h);
  const slices=14, amp=w*.10*settle;
  for(let i=0;i<slices;i++){
    const sy=(i/slices)*h, sh=h/slices;
    const off=(vnoise(i*5.7+Math.floor(u*24)*1.7,91)*2-1)*amp;
    if(Math.abs(off)<1) continue;
    c.drawImage(other, 0, sy, w, sh, off, sy, w, sh);
  }
  const dx=w*.012*settle;
  if(dx>0.2){ c.save(); c.globalCompositeOperation='lighter'; c.globalAlpha=.5*settle;
    c.drawImage(u<.5?Ared:Bred, -dx, 0, w, h);
    c.drawImage(u<.5?Acyan:Bcyan, dx, 0, w, h); c.restore(); }
  c.globalAlpha=.16*settle; c.fillStyle='#000';
  for(let y=(Math.floor(u*60)%4);y<h;y+=4) c.fillRect(0,y,w,1);
  c.globalAlpha=1;
};

T['Wide Ripple'] = (c,u,w,h)=>{                          // official 2.00 s
  const e=E.inOutCubic(u), R=Math.hypot(w,h)*.6*e;
  c.drawImage(A,0,0,w,h);
  c.save();
  c.beginPath(); c.arc(w/2,h/2,R,0,6.2832); c.clip();
  const s=lerp(.94,1,e);
  c.drawImage(B,(w-w*s)/2,(h-h*s)/2,w*s,h*s);
  c.restore();
  // ripple rings
  c.save(); c.globalCompositeOperation='lighter'; c.lineWidth=w*.006;
  for(let i=1;i<=3;i++){
    const rr=R-i*w*.055; if(rr<=0) continue;
    c.strokeStyle='rgba(190,225,255,'+(.30*(1-i/4))+')';
    c.beginPath(); c.arc(w/2,h/2,rr,0,6.2832); c.stroke();
  }
  c.restore();
};
  return T;
}

// (value noise + wobble lifted from the AE technique lab)
function n1(x,seed){const s=Math.sin(x*12.9898+seed*78.233)*43758.5453;return s-Math.floor(s);}
function noise1(x,seed){const i=Math.floor(x),f=x-i,u=f*f*(3-2*f);return lerp(n1(i,seed),n1(i+1,seed),u);}
const wobble=(t,amp,f,seed)=> (noise1(t*f,seed)*2-1)*amp + (noise1(t*f*2.7,seed+11)*2-1)*amp*.4;

root.MotionEngine = { Ease, spring, clamp, lerp, mulberry, hash, vnoise, noise1, wobble,
                      mk, tint, blurCanvas, bloom, chromatic, lightWrap, vignette, grain,
                      makeTransitions };
})(typeof window !== 'undefined' ? window : globalThis);
