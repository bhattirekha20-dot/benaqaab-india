#!/usr/bin/env python3
"""Structural preproduction-plan validation. Does NOT verify facts or visual quality."""
import argparse,json,math
from pathlib import Path
from urllib.parse import urlparse

SHOT_TEXT=('id','purpose','hero','start_state','end_state','primary_motion','secondary_motion','camera','audio','transition','acceptance')
def number(x):
    return not isinstance(x,bool) and isinstance(x,(int,float)) and math.isfinite(x)
def text(x):
    return isinstance(x,str) and bool(x.strip())
def validate(plan,project_root):
    errors=[];root=Path(project_root).resolve()
    if not isinstance(plan,dict):return ['Plan must be a JSON object.']
    dur=plan.get('duration');fps=plan.get('fps')
    if not number(dur) or dur<=0:errors.append('duration must be positive and finite.')
    if not number(fps) or fps<=0 or int(fps)!=fps:errors.append('fps must be a positive integer.')
    for k in ('width','height'):
        v=plan.get(k)
        if not isinstance(v,int) or isinstance(v,bool) or v<=0:errors.append(k+' must be a positive integer.')
    if errors:return errors
    if abs(dur*fps-round(dur*fps))>1e-5:errors.append('Output duration must correspond to a whole number of frames.')
    assets=plan.get('assets',{});claims=plan.get('claims',{})
    if not isinstance(assets,dict):errors.append('assets must be an object.');assets={}
    if not isinstance(claims,dict):errors.append('claims must be an object.');claims={}
    for aid,a in assets.items():
        if not isinstance(a,dict):errors.append(f'Asset {aid}: expected object.');continue
        for key in ('path','role','rights_note'):
            if not text(a.get(key)):errors.append(f'Asset {aid}: missing {key}.')
        if text(a.get('path')):
            p=(root/a['path']).resolve()
            if not p.is_relative_to(root):errors.append(f'Asset {aid}: path escapes project root.')
            elif not p.is_file():errors.append(f'Asset {aid}: local file not found.')
    for cid,claim in claims.items():
        if not isinstance(claim,dict):errors.append(f'Claim {cid}: expected object.');continue
        for key in ('statement','unit','qualification','source_url'):
            if not text(claim.get(key)):errors.append(f'Claim {cid}: missing {key}.')
        url=urlparse(claim.get('source_url','') if isinstance(claim.get('source_url',''),str) else '')
        if url.scheme not in ('http','https') or not url.netloc:errors.append(f'Claim {cid}: invalid source URL.')
    shots=plan.get('shots')
    if not isinstance(shots,list) or not shots:return errors+['At least one shot is required.']
    previous=0.;ids=set()
    for i,s in enumerate(shots):
        prefix=f'Shot {i+1}'
        if not isinstance(s,dict):errors.append(prefix+': expected object.');continue
        for key in SHOT_TEXT:
            if not text(s.get(key)):errors.append(prefix+': missing '+key+'.')
        sid=s.get('id')
        if text(sid):
            if sid in ids:errors.append(prefix+': duplicate shot id.')
            ids.add(sid)
        for key in ('asset_roles','detail_choices'):
            value=s.get(key)
            if not isinstance(value,list) or not value or not all(text(v) for v in value):errors.append(prefix+': '+key+' must contain explanatory text.')
        for key,lookup in [('claims',claims),('assets',assets)]:
            refs=s.get(key)
            if not isinstance(refs,list):errors.append(prefix+': '+key+' must be a list.');continue
            for ref in refs:
                if not isinstance(ref,str) or ref not in lookup:errors.append(prefix+f': unknown {key} reference {ref!r}.')
        start,end=s.get('start'),s.get('end')
        if not number(start) or not number(end):errors.append(prefix+': invalid timing.');continue
        if abs(start-previous)>1e-6:errors.append(prefix+': gap or overlap in primary shot ranges.')
        if end<=start or start<0 or end>dur+1e-6:errors.append(prefix+': invalid interval.')
        previous=end
    if abs(previous-dur)>1e-6:errors.append('Shot ranges must reach the output duration.')
    return errors

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('plan');p.add_argument('--root',help='Project asset root; defaults to the plan directory.');p.add_argument('--report');a=p.parse_args()
    path=Path(a.plan)
    try:plan=json.loads(path.read_text());errors=validate(plan,a.root or path.parent)
    except (OSError,ValueError,TypeError) as e:errors=[str(e)]
    result={'structural_pass':not errors,'visual_quality':'NOT ASSESSED','factual_accuracy':'NOT VERIFIED','licence_validity':'NOT VERIFIED','errors':errors}
    data=json.dumps(result,indent=2);print(data)
    if a.report:Path(a.report).write_text(data+'\n')
    return 0 if not errors else 1
if __name__=='__main__':raise SystemExit(main())
