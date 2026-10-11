import sys
import os
import time
import urllib.request
import urllib.parse
import json
from pathlib import Path
from PIL import Image

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR = Path(__file__).parent
AI_DIR = DIR / "assets" / "ai_plates"
AI_DIR.mkdir(parents=True, exist_ok=True)

# Direct exact Wikimedia Commons files for our scenes (all verified high-res photos)
DIRECT_FILES = [
    ("ai_04_crowded_mumbai_commuter_train.jpg", "File:Mumbai CST commuters.jpg"),
    ("ai_07_luxury_suv_gurugram_cybercity.jpg", "File:Cyber City, Gurgaon 02.jpg"),
    ("ai_09_pmgkay_free_ration_distribution.jpg", "File:PDS Fair Price Shop in India.jpg"),
    ("ai_10_rbi_financial_stability_vault.jpg", "File:Reserve Bank of India Mumbai.jpg"),
    ("ai_12_the_missing_factory_shenzhen_comparison.jpg", "File:Robotic arm in manufacturing.jpg"),
    ("ai_13_agriculture_45pct_workforce_chokepoint.jpg", "File:Paddy transplantation in Tamil Nadu, India.jpg"),
    ("ai_15_vocational_skilling_and_reforms_future.jpg", "File:Student in CNC workshop.jpg")
]

# Fallback queries if direct title fails
FALLBACK_QUERIES = [
    ("ai_04_crowded_mumbai_commuter_train.jpg", "Chhatrapati Shivaji Terminus crowd"),
    ("ai_07_luxury_suv_gurugram_cybercity.jpg", "Gurgaon Cyber City night"),
    ("ai_09_pmgkay_free_ration_distribution.jpg", "Ration shop India"),
    ("ai_10_rbi_financial_stability_vault.jpg", "Reserve Bank of India Mumbai building"),
    ("ai_12_the_missing_factory_shenzhen_comparison.jpg", "Industrial robot welding assembly line"),
    ("ai_13_agriculture_45pct_workforce_chokepoint.jpg", "Farming in India paddy field"),
    ("ai_15_vocational_skilling_and_reforms_future.jpg", "Vocational education mechanical workshop")
]

def fetch_file_url(file_title):
    try:
        url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'BenaqaabBot/2.0 (educational investigative journalism; contact@benaqaab.in)'})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode())
        pages = data.get('query', {}).get('pages', {})
        for pid, pinfo in pages.items():
            if 'imageinfo' in pinfo:
                return pinfo['imageinfo'][0]['url']
    except Exception as e:
        print(f"Error fetching url for {file_title}: {e}")
    return None

def search_query_url(query):
    try:
        url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srnamespace=6&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'BenaqaabBot/2.0 (educational investigative journalism)'})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode())
        results = data.get('query', {}).get('search', [])
        for r in results:
            t = r['title']
            if not t.lower().endswith(('.pdf', '.djvu', '.svg', '.tif', '.webm', '.ogv')):
                img_url = fetch_file_url(t)
                if img_url:
                    return img_url
    except Exception as e:
        print(f"Error searching {query}: {e}")
    return None

def download_and_crop(img_url, dest_path):
    try:
        req = urllib.request.Request(img_url, headers={'User-Agent': 'BenaqaabBot/2.0 (educational investigative journalism)'})
        temp_path = dest_path.parent / f"temp_{dest_path.name}"
        with urllib.request.urlopen(req, timeout=20) as resp:
            with open(temp_path, "wb") as f:
                f.write(resp.read())
                
        with Image.open(temp_path) as im:
            im = im.convert("RGB")
            target_w, target_h = 1920, 1080
            src_w, src_h = im.size
            src_ratio = src_w / src_h
            target_ratio = 16 / 9
            
            if src_ratio > target_ratio:
                new_w = int(src_h * target_ratio)
                left = (src_w - new_w) // 2
                im = im.crop((left, 0, left + new_w, src_h))
            else:
                new_h = int(src_w / target_ratio)
                top = (src_h - new_h) // 2
                im = im.crop((0, top, src_w, top + new_h))
                
            im = im.resize((target_w, target_h), Image.Resampling.LANCZOS)
            im.save(dest_path, "JPEG", quality=92)
            
        if temp_path.exists():
            temp_path.unlink()
        return True
    except Exception as e:
        print(f"Error processing {dest_path.name}: {e}")
        return False

def main():
    print("🚀 Fetching real high-res photographs...")
    for filename, title in DIRECT_FILES:
        dest = AI_DIR / filename
        print(f"\nProcessing {filename} via title: {title}")
        img_url = fetch_file_url(title)
        if not img_url:
            print("Direct title failed, trying fallback search...")
            fallback_q = next((q for f, q in FALLBACK_QUERIES if f == filename), None)
            if fallback_q:
                img_url = search_query_url(fallback_q)
        
        if img_url:
            print(f"Downloading: {img_url}")
            if download_and_crop(img_url, dest):
                print(f"✅ Created 1080p real plate: {filename}")
            else:
                print(f"❌ Failed download/crop for {filename}")
        else:
            print(f"❌ Could not find URL for {filename}")
        time.sleep(2.0)  # Rate limiting to prevent 429

if __name__ == "__main__":
    main()
