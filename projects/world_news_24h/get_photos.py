import requests,json,re
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
P=Path(__file__).parent
queries={'germany':'August Hanning','france':'Lycée Carnot Paris facade','kenya':'Ebola virus CDC','quebec':'Parliament building of Quebec Canada','science':'Francis Halzen','icecube':'IceCube Neutrino Observatory in 2023 02','bnd':'BND Zentrale Berlin'}
def get(item):
 key,q=item;r=requests.get('https://commons.wikimedia.org/w/api.php',params={'action':'query','format':'json','generator':'search','gsrsearch':q,'gsrnamespace':6,'gsrlimit':3,'prop':'imageinfo','iiprop':'url|extmetadata','iiurlwidth':1400},headers={'User-Agent':'EditorialPreview/1.0'},timeout=25);r.raise_for_status();d=r.json();(P/'assets'/f'{key}_candidates.json').write_text(json.dumps(d,indent=2))
 for p in sorted(d.get('query',{}).get('pages',{}).values(),key=lambda p:p.get('index',0)):
  ii=p.get('imageinfo',[{}])[0];m=ii.get('extmetadata',{});print(key,p['title'],'LICENSE',m.get('LicenseShortName',{}).get('value'),'ARTIST',re.sub('<[^>]+>','',m.get('Artist',{}).get('value',''))[:100],flush=True)
with ThreadPoolExecutor(5) as ex:list(ex.map(get,queries.items()))
