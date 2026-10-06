from pathlib import Path
import re
R=Path(__file__).parent;p=R/'preview.html';s=p.read_text();(R/'qa/preview_motion_v1.html').write_text(s)
s=s.replace("'scale('+(1+.025*q)+') translateY('+(-q*2)+'px)'","'scale('+(1.0+.10*q)+') translateY('+(-q*5)+'px)'")
s=s.replace("'translateY('+(-1.5+3*q)+'px)'","'scale('+(.90+.10*q)+') translateY('+(-2+4*q)+'px)'")
a=s.index('function mechanism(t,n)');b=s.index('function render(t)',a)
s=s[:a]+'''function mechanism(t,n){let a=scenes[n].rail,u=t-scenes[n].t,end=(n+1<scenes.length?scenes[n+1].t:duration)-scenes[n].t,p=Math.min(.999,u/end),active=Math.floor(p*3);let body='<svg viewBox="0 0 360 54" xmlns="http://www.w3.org/2000/svg"><path d="M24 17H336" stroke="#a5b4a6" stroke-opacity=".25" stroke-width="2"/><path d="M24 17H336" stroke="#efaa6d" stroke-width="4" stroke-dasharray="9 13" stroke-dashoffset="'+(-t*220)+'" opacity=".65"/>';
for(let j=0;j<3;j++){let x=24+j*156,phase=(t*1.6+j*.31)%1;body+='<circle cx="'+x+'" cy="17" r="'+(5+phase*10)+'" fill="none" stroke="#efaa6d" stroke-width="2.8" opacity="'+((1-phase)*.8)+'"/><circle cx="'+x+'" cy="17" r="5" fill="'+(j===active?'#efaa6d':'#a2b4a3')+'"/><text x="'+x+'" y="49" text-anchor="'+(j===0?'start':j===2?'end':'middle')+'" fill="'+(j===active?'#fff4df':'#b9c8b9')+'" font-size="9" font-family="Inter,Arial" font-weight="700">'+a[j]+'</text>'}body+='</svg>';$('mechanism').innerHTML=body}
''' +s[b:]
s=s.replace('Dated snapshot, not a certified rolling-24-hour bulletin. Reports may develop.','Coverage: 6 Oct 00:00–7 Oct 00:00 IST. Fixed edition, not live news.')
s=s.replace('</style>','.mechanism{top:62.7%;height:5.5%}.image-note{top:60%}</style>')
p.write_text(s)
print('Applied uncropped camera movement and animated conceptual flow.')
