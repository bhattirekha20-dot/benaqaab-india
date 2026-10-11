import urllib.request
import urllib.parse
import json
import re
from pathlib import Path

def search_ddg_images(query, max_results=5):
    url = f"https://duckduckgo.com/i.js?q={urllib.parse.quote(query)}&o=json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json'
    }
    
    # First get the vqd token
    token_url = f"https://duckduckgo.com/?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(token_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            content = resp.read().decode('utf-8')
            match = re.search(r'vqd=([\'"]?)([\d-]+)\1', content)
            if not match:
                match = re.search(r'vqd=([\d-]+)', content)
            if match:
                vqd = match.group(2) if len(match.groups()) > 1 else match.group(1)
                img_api = f"https://duckduckgo.com/i.js?q={urllib.parse.quote(query)}&o=json&vqd={vqd}"
                req_api = urllib.request.Request(img_api, headers=headers)
                with urllib.request.urlopen(req_api, timeout=5) as api_resp:
                    data = json.loads(api_resp.read().decode('utf-8'))
                    return [r['image'] for r in data.get('results', [])[:max_results]]
    except Exception as e:
        print("DDG search error:", e)
    return []

if __name__ == '__main__':
    imgs = search_ddg_images("silicone thumb cloned fingerprint aeps police india")
    print("Found images:", imgs)
