import urllib.request
import re
from pathlib import Path

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

urls = [
    'https://the420.in/cloned-fingerprints-used-aeps-fraud-aligarh-police-arrest-accused/',
    'https://www.deccanchronicle.com/nation/crime/050822/cyberabad-cops-bust-fingerprint-cloning-gang-recover-2500-clones.html'
]

for url in urls:
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=6) as resp:
            html = resp.read().decode('utf-8', errors='ignore')
            imgs = re.findall(r'<img[^>]+src=["\']([^"\']+\.(?:jpg|png|jpeg))["\']', html)
            print(f'Found {len(imgs)} images on {url}:')
            for img in imgs[:8]:
                print('  ', img)
    except Exception as e:
        print(f'Error fetching {url}:', e)
