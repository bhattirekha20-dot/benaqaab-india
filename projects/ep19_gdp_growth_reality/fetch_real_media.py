import sys
import os

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

import urllib.request
import urllib.parse
import json
from pathlib import Path
from PIL import Image

DIR = Path(__file__).parent
AI_DIR = DIR / "assets" / "ai_plates"
AI_DIR.mkdir(parents=True, exist_ok=True)

# Wikimedia search queries for our scenes
SEARCH_QUERIES = [
    ("ai_01_global_gdp_celebration_bull.jpg", "Statue of Bull in front of BSE Mumbai"),
    ("ai_02_parliament_cabinet_national_accounts.jpg", "Parliament of India building New Delhi"),
    ("ai_04_crowded_mumbai_commuter_train.jpg", "Mumbai commuter crowd railway"),
    ("ai_07_luxury_suv_gurugram_cybercity.jpg", "Cyber City Gurgaon night"),
    ("ai_08_rural_village_stagnant_two_wheelers.jpg", "Rural road India motorcycle village"),
    ("ai_09_pmgkay_free_ration_distribution.jpg", "Public Distribution System ration India"),
    ("ai_10_rbi_financial_stability_vault.jpg", "Reserve Bank of India Mumbai headquarters building"),
    ("ai_12_the_missing_factory_shenzhen_comparison.jpg", "Automated manufacturing factory robotic arm"),
    ("ai_13_agriculture_45pct_workforce_chokepoint.jpg", "Paddy farming India workers harvest"),
    ("ai_15_vocational_skilling_and_reforms_future.jpg", "Vocational training India technical institute")
]

def search_and_download(filename, query):
    try:
        # Search commons API
        search_url = f"https://commons.wikimedia.org/w/api.php?action=query&list=search&srsearch={urllib.parse.quote(query)}&srnamespace=6&format=json"
        req = urllib.request.Request(search_url, headers={'User-Agent': 'BenaqaabBot/1.0 (educational journalism)'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
        
        search_results = data.get('query', {}).get('search', [])
        if not search_results:
            print(f"❌ No results for {query}")
            return False
            
        page_title = search_results[0]['title']
        print(f"🔍 Found: {page_title} for {filename}")
        
        # Get image URL
        info_url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(page_title)}&prop=imageinfo&iiprop=url&format=json"
        req2 = urllib.request.Request(info_url, headers={'User-Agent': 'BenaqaabBot/1.0 (educational journalism)'})
        with urllib.request.urlopen(req2, timeout=10) as resp2:
            data2 = json.loads(resp2.read().decode())
            
        pages = data2.get('query', {}).get('pages', {})
        for pid, pinfo in pages.items():
            if 'imageinfo' in pinfo:
                img_url = pinfo['imageinfo'][0]['url']
                print(f"⬇️ Downloading: {img_url}")
                
                req3 = urllib.request.Request(img_url, headers={'User-Agent': 'BenaqaabBot/1.0 (educational journalism)'})
                dest = AI_DIR / filename
                with urllib.request.urlopen(req3, timeout=15) as img_resp:
                    img_data = img_resp.read()
                    
                # Save and crop/scale to 1920x1080
                temp_path = AI_DIR / f"temp_{filename}"
                with open(temp_path, "wb") as f:
                    f.write(img_data)
                    
                with Image.open(temp_path) as im:
                    im = im.convert("RGB")
                    # Crop to 16:9
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
                    im.save(dest, "JPEG", quality=92)
                    
                if temp_path.exists():
                    temp_path.unlink()
                print(f"✅ Successfully created 1080p real plate: {filename}")
                return True
    except Exception as e:
        print(f"⚠️ Error downloading {filename}: {e}")
        return False

def main():
    success_count = 0
    for filename, query in SEARCH_QUERIES:
        if search_and_download(filename, query):
            success_count += 1
    print(f"\n🎯 Downloaded {success_count}/{len(SEARCH_QUERIES)} real images!")

if __name__ == "__main__":
    main()
