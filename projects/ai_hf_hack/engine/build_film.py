#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build film.html + timeline.json + make_audio.sh/.bat (engine/ version).
Usage: python3 engine/build_film.py [project_dir]"""
import json, os, subprocess, sys, base64

PROJ = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes import SCENES, ACTS

FPS = 30
HEAD, TAIL, GAP = 0.04, 0.50, 0.30
ACT_BREAK_EXTRA = 0.55
CH_MAX = 1500.0

def dur_of(vid, text, est_mult=1.0):
    p = os.path.join(PROJ, "audio", vid + ".mp3")
    if os.path.exists(p):
        try:
            r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                "-of", "default=nw=1:nk=1", p], capture_output=True, text=True, timeout=20)
            return min(float(r.stdout.strip()), CH_MAX)
        except Exception:
            pass
    return max(6.0, min(len(text) * est_mult / 19.0, CH_MAX))

def main():
    tl, t, prev_act = [], 0.0, None
    for i, sc in enumerate(SCENES):
        vid = "vo" + sc["id"][1:].zfill(2)
        if prev_act is not None and sc["act"] != prev_act:
            t += ACT_BREAK_EXTRA
        vo_start = t + HEAD
        vd = dur_of(vid, " ".join(sc.get("cap", [])), est_mult=2.9)
        end = vo_start + vd + TAIL
        tl.append(dict(i=i, id=sc["id"], act=sc["act"], t0=round(t, 3), t1=round(end, 3),
                       vo=vid, vo_start=round(vo_start, 3), vo_dur=round(vd, 3),
                       has_vo=os.path.exists(os.path.join(PROJ, "audio", vid + ".mp3"))))
        t = end + GAP
        prev_act = sc["act"]
    total = t
    audios = {}
    for e in tl:
        p = os.path.join(PROJ, "audio", e["vo"] + ".mp3")
        if os.path.exists(p):
            with open(p, "rb") as f:
                audios[e["vo"]] = "data:audio/mpeg;base64," + base64.b64encode(f.read()).decode()
    chapters = []
    for e in tl:
        if not chapters or chapters[-1][1] != e["act"]:
            chapters.append([e["act"], e["t0"], e["id"]])
    def mmss(x):
        return "%d:%02d" % (int(x) // 60, int(x) % 60)
    chap_lines = ["%s %s (act %d · %s)" % (mmss(t0), SCENES[[c[2] for c in chapters].index(sid)]["title"],
                                           act, sid) for act, t0, sid in chapters]
    with open(os.path.join(PROJ, "timeline.json"), "w") as f:
        json.dump(dict(total=total, fps=FPS, scenes=tl, chapters=chapters), f, ensure_ascii=False, indent=1)
    with open(os.path.join(PROJ, "chapters.txt"), "w") as f:
        f.write("\n".join(chap_lines) + "\n")
    # master audio (relative paths — user-PC safe)
    parts, filt, rel_names = [], [], []
    for e in tl:
        p = os.path.join(PROJ, "audio", e["vo"] + ".mp3")
        if os.path.exists(p):
            idx = len(rel_names); rel_names.append(e["vo"])
            ms = int(round(e["vo_start"] * 1000))
            filt.append("[%d:a]aresample=44100,aformat=channel_layouts=stereo,adelay=%d|%d[v%d]"
                        % (idx, ms, ms, idx))
            parts.append("[v%d]" % idx)
    if rel_names:
        n = len(rel_names)
        fc = ";".join(filt) + ";%samix=inputs=%d:duration=longest:normalize=0[out]" % ("".join(parts), n)
        cmd = ("ffmpeg -y " + " ".join('-i "audio/%s.mp3"' % x for x in rel_names) +
               ' -filter_complex "%s" -map "[out]" -c:a libmp3lame -b:a 192k audio_master.mp3' % fc)
        with open(os.path.join(PROJ, "make_audio.sh"), "w") as f:
            f.write("#!/bin/bash\ncd \"$(dirname \"$0\")\"\n" + cmd + "\n")
        with open(os.path.join(PROJ, "make_audio.bat"), "w") as f:
            f.write("@echo off\ncd /d \"%~dp0\"\n" + cmd + "\n")
        os.chmod(os.path.join(PROJ, "make_audio.sh"), 0o755)
    data = dict(scenes=SCENES, tl=tl, total=total, fps=FPS, acts={str(k): v for k, v in ACTS.items()},
                audios=audios, missing=[e["vo"] for e in tl if not e["has_vo"]])
    html = TEMPLATE.replace("/*__DATA__*/", "const D=" + json.dumps(data, ensure_ascii=False) + ";")
    with open(os.path.join(PROJ, "film.html"), "w") as f:
        f.write(html)
    print("film.html %.1f MB · total %.1fs (%s) · scenes %d · vo present %d/%d" %
          (os.path.getsize(os.path.join(PROJ, "film.html")) / 1e6, total, mmss(total), len(tl), len(audios), len(tl)))
    print("\n".join("  " + c for c in chap_lines))
    if data["missing"]:
        print("MISSING VO:", ", ".join(data["missing"]))

TEMPLATE = r"""<!DOCTYPE html>
<html lang="hi"><head><meta charset="utf-8">
<title>AI ने खुद Hugging Face हैक कर लिया — film</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
html,body{background:#05070c;color:#eef1f6;overflow:hidden;height:100%}
:root{--acc:#f5b942;--w:1920px;--h:1080px}
body{font-family:"Noto Sans Devanagari","Nirmala UI","Mangal","Segoe UI",sans-serif}
#stage{position:absolute;left:50%;top:50%;width:var(--w);height:var(--h);transform:translate(-50%,-50%);transform-origin:center;background:#05070c}
section{position:absolute;inset:0;visibility:hidden;overflow:hidden}
section.on{visibility:visible}
.plate{position:absolute;inset:-4%;object-fit:cover;width:108%;height:108%;filter:saturate(.85) brightness(.72) contrast(1.05)}
.scrim{position:absolute;inset:0;background:linear-gradient(100deg,rgba(4,6,11,.95) 0%,rgba(4,6,11,.86) 42%,rgba(4,6,11,.42) 74%,rgba(4,6,11,.30) 100%),radial-gradient(120% 90% at 50% 120%,rgba(0,0,0,.65),transparent 60%)}
.grid{position:absolute;inset:0;background:repeating-linear-gradient(0deg,rgba(255,255,255,.028) 0 1px,transparent 1px 46px),repeating-linear-gradient(90deg,rgba(255,255,255,.028) 0 1px,transparent 1px 46px);mask-image:radial-gradient(90% 80% at 60% 40%,#000 30%,transparent 100%)}
.topbar{position:absolute;top:34px;left:56px;right:56px;display:flex;justify-content:space-between;align-items:center;z-index:5}
.actpill{display:flex;align-items:center;gap:12px;background:rgba(8,10,16,.72);border:1px solid rgba(255,255,255,.14);padding:10px 22px;border-radius:999px;font-size:22px;letter-spacing:.06em}
.actpill .dot{width:14px;height:14px;border-radius:50%;background:var(--acc);box-shadow:0 0 14px var(--acc)}
.actpill b{color:var(--acc);font-weight:800}
.datechip{background:rgba(8,10,16,.72);border:1px solid var(--acc);color:#fff;padding:10px 20px;border-radius:10px;font-size:21px;font-weight:700;letter-spacing:.05em;box-shadow:0 0 22px rgba(0,0,0,.4)}
.datechip em{color:var(--acc);font-style:normal}
.prog{position:absolute;top:0;left:0;height:5px;background:linear-gradient(90deg,var(--acc),#fff);z-index:9;box-shadow:0 0 12px var(--acc)}
.content{position:absolute;inset:0;padding:130px 78px 190px 78px;display:grid;grid-template-columns:56% 44%;gap:48px;z-index:4}
.content.hero,.content.center{grid-template-columns:1fr;align-items:center;text-align:center}
.title{font-size:64px;line-height:1.18;font-weight:800;letter-spacing:.01em;text-shadow:0 6px 30px rgba(0,0,0,.7)}
.content.hero .title{font-size:84px}
.sub{margin-top:18px;font-size:21px;letter-spacing:.42em;color:var(--acc);font-weight:700}
.note{margin-top:26px;font-size:26px;color:#cfd6e4;background:rgba(255,255,255,.05);border-left:5px solid var(--acc);padding:16px 22px;border-radius:0 12px 12px 0;max-width:92%}
.chips{display:flex;flex-wrap:wrap;gap:14px;margin-top:30px}
.chip{font-size:21px;font-weight:700;padding:11px 20px;border-radius:999px;border:1.6px solid var(--acc);color:#fff;background:rgba(0,0,0,.45);box-shadow:0 0 16px rgba(0,0,0,.35)}
.panel{background:rgba(10,13,20,.78);border:1px solid rgba(255,255,255,.13);border-radius:20px;padding:34px 34px;backdrop-filter:blur(6px);box-shadow:0 24px 60px rgba(0,0,0,.5);align-self:center}
.rows{display:flex;flex-direction:column;gap:16px}
.row{background:rgba(255,255,255,.055);border-left:5px solid var(--acc);border-radius:0 14px 14px 0;padding:16px 22px}
.row .k{font-size:26px;font-weight:800;color:#fff}
.row .v{font-size:21px;color:#c3cad8;margin-top:6px;line-height:1.45}
.quote{font-size:32px;line-height:1.4;font-weight:700;color:#fff}
.quote:before{content:"“";color:var(--acc);font-size:60px;line-height:0;position:relative;top:16px;margin-right:6px}
.who{margin-top:18px;font-size:20px;color:var(--acc);letter-spacing:.12em;font-weight:700;text-transform:uppercase}
.steps{display:flex;flex-direction:column;gap:0}
.step{display:flex;gap:20px;align-items:flex-start;position:relative;padding-bottom:26px}
.step:last-child{padding-bottom:0}
.step .num{flex:0 0 46px;height:46px;border-radius:50%;background:var(--acc);color:#08101c;font-weight:900;font-size:23px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 18px rgba(0,0,0,.5);z-index:2}
.step:not(:last-child):after{content:"";position:absolute;left:22.5px;top:46px;bottom:0;width:3px;background:linear-gradient(var(--acc),rgba(255,255,255,.15))}
.step .tx{font-size:24px;line-height:1.4;padding-top:7px;color:#e8ecf4}
.tline{position:relative;padding-left:8px}
.tl-item{display:grid;grid-template-columns:170px 1fr;gap:22px;position:relative;padding:14px 0 22px}
.tl-item .date{font-size:24px;font-weight:900;color:var(--acc);text-align:right}
.tl-item .dtx{font-size:22px;color:#d6dbe6;line-height:1.45;border-left:3px solid rgba(255,255,255,.2);padding-left:22px;position:relative}
.tl-item .dtx:before{content:"";position:absolute;left:-9px;top:6px;width:15px;height:15px;border-radius:50%;background:var(--acc);box-shadow:0 0 12px var(--acc)}
.players{display:grid;grid-template-columns:1fr 1fr;gap:18px;align-self:center}
.pcard{background:rgba(10,13,20,.82);border:1px solid rgba(255,255,255,.14);border-radius:18px;padding:20px 22px;min-height:150px}
.plogo{height:52px;object-fit:contain;object-position:left center;filter:brightness(1.4) contrast(1.1)}
.pname{font-size:25px;font-weight:900;margin-top:10px}
.pdesc{font-size:19px;color:#c3cad8;margin-top:7px;line-height:1.4}
.lessons .row{border-left-width:7px;padding:20px 24px}
.lessons .row .k{font-size:29px}
.lessons .row .v{font-size:22px}
.float{position:absolute;border-radius:18px;overflow:hidden;border:1.5px solid rgba(255,255,255,.18);box-shadow:0 30px 70px rgba(0,0,0,.65),0 0 34px rgba(0,0,0,.5);z-index:3;opacity:0;will-change:transform,opacity}
.float img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.95) brightness(.92) contrast(1.06)}
.float .glow{position:absolute;inset:0;background:linear-gradient(160deg,rgba(255,255,255,.10),transparent 40%),radial-gradient(120% 100% at 50% 120%,rgba(0,0,0,.45),transparent 60%);box-shadow:inset 0 0 36px rgba(0,0,0,.4);pointer-events:none}
.capbar{position:absolute;left:0;right:0;bottom:64px;display:flex;justify-content:center;z-index:6;pointer-events:none}
.cap{max-width:1560px;background:linear-gradient(180deg,rgba(4,6,11,.0),rgba(4,6,11,.88) 30%,rgba(4,6,11,.92));border-top:3px solid var(--acc);padding:20px 44px 22px;border-radius:16px 16px 0 0;font-size:34px;font-weight:700;text-align:center;line-height:1.4;text-shadow:0 3px 14px #000}
.src{position:absolute;right:60px;bottom:26px;font-size:15.5px;color:#9aa5b8;letter-spacing:.03em;z-index:6;max-width:1200px;text-align:right}
.wipe{position:absolute;inset:0;background:linear-gradient(120deg,var(--acc),transparent 70%);opacity:0;z-index:8;pointer-events:none}
.legend{position:absolute;left:56px;bottom:26px;font-size:15px;color:#7d879a;z-index:6;letter-spacing:.08em}
</style></head><body>
<div id="stage"></div>
<script>
/*__DATA__*/
const stage=document.getElementById("stage");
const EL=[];
const clamp=(x)=>Math.max(0,Math.min(1,x));
const seg=(p,a,b)=>clamp((p-a)/(b-a));
function el(tag,cls,html){const e=document.createElement(tag);if(cls)e.className=cls;if(html!=null)e.innerHTML=html;return e;}
function rev(node,op,y,sc){if(!node)return;node.style.opacity=op;if(y!==undefined)node.style.transform="translateY("+y+"px)";if(sc!==undefined)node.style.scale=sc;}
D.scenes.forEach((sc,i)=>{
  const t=D.tl[i], A=D.acts[String(sc.act)];
  const s=el("section");s.style.setProperty("--acc",A[2]);
  if(sc.img){const im=el("img","plate");im.src=sc.img;im.onerror=()=>im.remove();s.appendChild(im);}
  s.appendChild(el("div","scrim"));s.appendChild(el("div","grid"));
  const tb=el("div","topbar");
  const pill=el("div","actpill",'<span class="dot"></span><b>'+A[0]+'</b> · '+A[1]);
  const dc=el("div","datechip",sc.chip?'<em>▸</em> '+sc.chip:'');
  tb.appendChild(pill);tb.appendChild(dc);s.appendChild(tb);
  const pr=el("div","prog");s.appendChild(pr);s._pr=pr;s._pill=pill;s._dc=dc;
  const c=el("div","content"+(sc.lay==="hero"?" hero":""));
  const left=el("div","left");
  const title=el("div","title",sc.title);const sub=el("div","sub",sc.sub||"");
  left.appendChild(title);left.appendChild(sub);
  if(sc.chips){const ch=el("div","chips");sc.chips.forEach(x=>ch.appendChild(el("div","chip",x)));left.appendChild(ch);}
  if(sc.note){const n=el("div","note",sc.note);left.appendChild(n);}
  c.appendChild(left);
  const right=el("div","right");
  const kind=(sc.rows||sc.steps||sc.tl||sc.quote)?"panel":"panel empty";
  const p=el("div",kind);
  if(sc.tl){const tl=el("div","tline");sc.tl.forEach(it=>{const d=el("div","tl-item");d.appendChild(el("div","date",it[0]));d.appendChild(el("div","dtx",it[1]));tl.appendChild(d);});p.appendChild(tl);s._items=[...tl.children];}
  else if(sc.steps){const st=el("div","steps");sc.steps.forEach((x,k)=>{const w=el("div","step");w.appendChild(el("div","num",String(k+1)));w.appendChild(el("div","tx",x));st.appendChild(w);});p.appendChild(st);s._items=[...st.children];}
  if(sc.rows&&sc.lay!=="players"){const rw=el("div","rows");sc.rows.forEach(r=>{const w=el("div","row");w.appendChild(el("div","k",r[0]));w.appendChild(el("div","v",r[1]));rw.appendChild(w);});p.appendChild(rw);s._items=[...rw.children];}
  if(sc.quote){const q=el("div","qwrap");q.appendChild(el("div","quote",sc.quote[0]));q.appendChild(el("div","who","— "+sc.quote[1]));p.appendChild(q);s._q=q;}
  if(sc.lay==="players"){const pl=el("div","players");sc.rows.forEach(r=>{const w=el("div","pcard");if(r[2]){const lg=el("img","plogo");lg.src=r[2];lg.onerror=()=>lg.remove();w.appendChild(lg);}w.appendChild(el("div","pname",r[0]));w.appendChild(el("div","pdesc",r[1]));pl.appendChild(w);});p.appendChild(pl);s._items=[...pl.children];right.appendChild(pl);}
  else if(sc.lay!=="hero") right.appendChild(p);
  if(right.children.length)c.appendChild(right);
  if(sc.lay==="hero")c.style.placeItems="center";
  s.appendChild(c);
  if(sc.floats){s._floats=[];sc.floats.forEach(fl=>{
    const d=el("div","float");
    d.style.left=fl[1]+"%";d.style.top=fl[2]+"%";d.style.width=fl[3]+"px";d.style.height=fl[4]+"px";
    const im=el("img");im.src=fl[0];im.onerror=()=>d.remove();
    d.appendChild(im);d.appendChild(el("div","glow"));
    s.appendChild(d);s._floats.push(d);});}
  const cap=el("div","capbar");const capT=el("div","cap","");cap.appendChild(capT);s.appendChild(cap);s._cap=capT;
  s.appendChild(el("div","src","स्रोत: "+sc.src));
  s.appendChild(el("div","legend","AI · HUGGING FACE SANDBOX INCIDENT — JUL 2026"));
  const w=el("div","wipe");s.appendChild(w);s._wipe=w;
  stage.appendChild(s);EL.push(s);
});
function paint(t){
  t=Math.max(0,Math.min(D.total-1e-4,t));
  let idx=0;for(let i=0;i<D.tl.length;i++){if(t>=D.tl[i].t0)idx=i;}
  function shell(i){const tt=(i>=0&&i<D.tl.length)?D.tl[i]:null;const ss=tt?EL[i]:null;if(!ss)return;
    const on=t>=tt.t0-0.34&&t<tt.t1+0.10;
    ss.classList.toggle("on",on);
    if(!on){ss.style.opacity=0;return;}
    const op=clamp(seg(t,tt.t0-0.30,tt.t0+0.04))*clamp(seg(t,tt.t1+0.08,tt.t1-0.24));
    ss.style.opacity=op;
    const pl=ss.querySelector(".plate");
    if(pl){const Lp=clamp((t-tt.t0)/(tt.t1-tt.t0));
      const k=1.05+0.09*Lp+0.06*(1-op);
      pl.style.transform="scale("+k+") translate("+((Lp-0.5)*1.6)+"%,"+((0.5-Lp)*1.2)+"%)";
      pl.style.filter="saturate(.85) brightness(.72) contrast(1.05) blur("+((1-op)*5).toFixed(2)+"px)";}}
  shell(idx-1);shell(idx);shell(idx+1);
  const sc=D.scenes[idx],tl=D.tl[idx],s=EL[idx];
  const L=(t-tl.t0)/(tl.t1-tl.t0), span=tl.t1-tl.t0;
  s._pr.style.width=(100*t/D.total)+"%";
  rev(s._pill,seg(L,0.01,0.06),0,1-0.06*seg(L,0.01,0.08));rev(s._dc,seg(L,0.02,0.08));
  const caps=sc.cap||[], totalC=caps.reduce((a,x)=>a+x.length,0);
  let acc=0,cur=caps[0]||"";
  for(const cx of caps){if(L>=0.04&&L<0.04+(acc+cx.length/totalC)*0.93){cur=cx;break;}acc+=cx.length/totalC;}
  if(L<0.04)cur=caps[0]||"";if(L>0.97)cur=caps[caps.length-1]||cur;
  s._cap.textContent=cur;rev(s._cap,seg(L,0.02,0.05),0);
  if(s._floats){s._floats.forEach((f,k)=>{
    const dl=0.13+k*0.11;const rin=seg(L,dl,dl+0.13);
    const ph=k*2.1+idx*0.9;
    const fy=Math.sin(t*1.05+ph)*9,fx=Math.cos(t*0.78+ph)*5,rot=Math.sin(t*0.66+ph)*1.7;
    f.style.opacity=rin;
    f.style.transform="translate("+fx.toFixed(2)+"px,"+(fy+44*(1-rin)).toFixed(2)+"px) rotate("+(rot+(1-rin)*5).toFixed(2)+"deg) scale("+(0.88+0.12*rin).toFixed(3)+")";
  });}
  const items=s._items||[];
  if(sc.lay==="timeline"){items.forEach((it,i)=>{const a=0.10+i*(0.72/Math.max(1,items.length));rev(it,seg(L,a,a+0.07),26*(1-seg(L,a,a+0.07)));});}
  else if(sc.lay==="steps"){items.forEach((it,i)=>{const a=0.12+i*(0.60/Math.max(1,items.length));rev(it,seg(L,a,a+0.08),30*(1-seg(L,a,a+0.08)));});}
  else if(sc.lay==="hero"){const T=s.querySelector(".title"),U=s.querySelector(".sub"),N=s.querySelector(".note"),C=s.querySelector(".chips");
    rev(T,seg(L,0.03,0.16),54*(1-seg(L,0.03,0.16)),0.96+0.04*seg(L,0.03,0.16));rev(U,seg(L,0.14,0.24));
    if(C){const ks=C.children;[...ks].forEach((k,i)=>rev(k,seg(L,0.30+i*0.06,0.40+i*0.06),22*(1-seg(L,0.30+i*0.06,0.40+i*0.06))));}
    if(N)rev(N,seg(L,0.55,0.66),20*(1-seg(L,0.55,0.66)));}
  else{rev(s.querySelector(".title"),seg(L,0.02,0.10),40*(1-seg(L,0.02,0.10)));rev(s.querySelector(".sub"),seg(L,0.08,0.16));
    items.forEach((it,i)=>{const a=0.10+i*0.09;rev(it,seg(L,a,a+0.10),34*(1-seg(L,a,a+0.10)));});
    if(s._q)rev(s._q,seg(L,0.50,0.62),30*(1-seg(L,0.50,0.62)));
    const chips=s.querySelector(".chips");if(chips)[...chips.children].forEach((k,i)=>rev(k,seg(L,0.62+i*0.05,0.72+i*0.05),18*(1-seg(L,0.62+i*0.05,0.72+i*0.05))));
    const note=s.querySelector(".note");if(note&&sc.lay!=="hero")rev(note,seg(L,0.66,0.76),20*(1-seg(L,0.66,0.76)));
    const pan=s.querySelector(".panel");if(pan)rev(pan,seg(L,0.01,0.07),34*(1-seg(L,0.01,0.07)));}
  const rs=s.querySelector(".src");rev(rs,seg(L,0.20,0.30));
  const isFirst=D.scenes.findIndex(x=>x.act===sc.act)===idx;
  if(isFirst&&sc.act>1){const wseg=seg(t-tl.t0,0,0.55);s._wipe.style.opacity=(wseg>0&&wseg<1)?(Math.sin(Math.PI*wseg)*0.6):0;s._wipe.style.transform="translateX("+((1-wseg)*100-50)+"%)";}
  else s._wipe.style.opacity=0;
  return idx;
}
let curAudio=null,curAIdx=-1;
function tickAudio(t,idx){
  if(RENDER)return;
  const tl=D.tl[idx],vid=tl.vo,b64=D.audios[vid];
  if(!b64)return;
  const local=t-tl.vo_start;
  if(local<0||local>tl.vo_dur+0.1){if(curAudio){curAudio.pause();}return;}
  if(curAIdx!==idx){if(curAudio)curAudio.pause();curAudio=new Audio(b64);curAudio.currentTime=0;curAIdx=idx;curAudio.play().catch(()=>{});}
  if(curAudio&&!curAudio.paused&&Math.abs(curAudio.currentTime-local)>0.30){try{curAudio.currentTime=local;}catch(e){}}
}
const RENDER=/render=1/.test(location.search);
let t0perf=performance.now();
function frame(now){
  if(!RENDER){const t=(now-t0perf)/1000;if(t>D.total){t0perf=now;const idx=paint(0);tickAudio(0,idx);}else{const idx=paint(t);tickAudio(t,idx);}requestAnimationFrame(frame);}
}
window.__seek=function(t){return paint(t);};
window.__total=D.total;window.__fps=D.fps;
window.__info=function(){return{total:D.total,missing:D.missing};};
if(!RENDER)requestAnimationFrame(frame);else paint(0);
</script></body></html>"""
if __name__ == "__main__":
    main()
