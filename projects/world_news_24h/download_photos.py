from pathlib import Path
import json,re,requests,io
from PIL import Image
P=Path(__file__).parent
choices={'germany':('bnd','2019-08-30 BND Zentrale Berlin OK 0322','BND headquarters · archive, not arrest photo'),'france':('france','Facade lycée Carnot','Paris school · archive, not these protests'),'kenya':('kenya','Ebola virus em.jpg','CDC Ebola micrograph · reference, not patient sample'),'quebec':('quebec','Assemblée nationale','Quebec legislature · archive, not election night'),'science':('science','Halzen-Neutel','Francis Halzen · archival portrait'),'icecube':('icecube','IceCube Neutrino','IceCube observatory · 2023 archive')}
out={}
for key,(name,match,label) in choices.items():
 pages=json.loads((P/'assets'/f'{name}_candidates.json').read_text())['query']['pages'];p=next(x for x in pages.values() if match in x['title']);ii=p['imageinfo'][0];m=ii['extmetadata'];url=ii.get('thumburl',ii['url']);r=requests.get(url,headers={'User-Agent':'EditorialPreview/1.0'},timeout=30)
 if r.status_code!=200:r=requests.get(ii['url'],headers={'User-Agent':'EditorialPreview/1.0'},timeout=30)
 r.raise_for_status();im=Image.open(io.BytesIO(r.content)).convert('RGB');im.thumbnail((1600,1600));im.save(P/'assets'/f'photo_{key}.jpg',quality=93)
 clean=lambda field:re.sub('<[^>]+>','',m.get(field,{}).get('value','')).strip()
 out[key]={'title':p['title'],'source':ii['descriptionurl'],'creator':clean('Artist'),'license':clean('LicenseShortName'),'license_url':clean('LicenseUrl'),'date':clean('DateTimeOriginal'),'description':clean('ImageDescription'),'label':label,'path':f'assets/photo_{key}.jpg','modification':'Resized and JPEG encoded; no AI alteration.'};print(key,im.size,out[key]['creator'],out[key]['license'],flush=True)
(P/'assets'/'photo_manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2))
