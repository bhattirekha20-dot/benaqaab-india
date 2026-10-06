import json, sys, urllib.request, urllib.parse, re, html
UA = {'User-Agent': 'BenaqaabIndiaResearch/1.0 (educational news explainer; contact via YouTube)'}
def search(q, n=6):
    p = {'action':'query','generator':'search','gsrsearch':f'filetype:bitmap {q}','gsrnamespace':6,'gsrlimit':n,
         'prop':'imageinfo','iiprop':'url|extmetadata|size','iiurlwidth':1600,'format':'json'}
    u = 'https://commons.wikimedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=20))
    out = []
    for pg in (d.get('query',{}).get('pages',{}) or {}).values():
        ii = pg['imageinfo'][0]; m = ii.get('extmetadata',{})
        g = lambda k: re.sub('<[^>]+>','',html.unescape(m.get(k,{}).get('value',''))).strip()
        out.append(dict(title=pg['title'], w=ii['width'], h=ii['height'], url=ii['url'], thumb=ii.get('thumburl'),
                        lic=g('LicenseShortName'), artist=g('Artist')[:60], date=g('DateTimeOriginal')[:20], desc=g('ImageDescription')[:90]))
    return out
if __name__ == '__main__':
    for q in sys.argv[1:]:
        print(f'\n## {q}')
        try:
            for r in search(q): print(f"  {r['w']}x{r['h']} | {r['lic']} | {r['artist']} | {r['title'][5:80]}")
        except Exception as e: print('  ERR', e)
