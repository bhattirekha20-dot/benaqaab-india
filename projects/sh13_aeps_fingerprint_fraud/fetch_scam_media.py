import urllib.request
import urllib.parse
import json
import re
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

def search_ddg_images(query):
    print(f"Searching images for: {query}")
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode('utf-8', errors='replace')
        # find links
        links = re.findall(r'href="([^"]+)" class="result__url"', html)
        print("Found links:", len(links))
        for l in links[:5]:
            print(" ", l.strip())
    except Exception as e:
        print("Error:", e)

search_ddg_images("silicone thumb police seizure aeps")
