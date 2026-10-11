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

TARGETS = [
    ("ai_05_global_superpowers_per_capita_towers.jpg", "File:Downtown-NewYork.jpg"),
    ("ai_07_luxury_suv_gurugram_cybercity.jpg", "File:DLF Cyber City with Rapid Metro, Gurgaon.jpg"),
    ("ai_11_debt_financed_consumption_credit_card.jpg", "File:Credit-cards.jpg"),
    ("ai_12_the_missing_factory_shenzhen_comparison.jpg", "File:Robotic welding in an automotive factory.jpg"),
    ("ai_15_vocational_skilling_and_reforms_future.jpg", "File:CNC PCB Milling Machine.jpg")
]

def fetch_file_url(file_title):
    try:
        url = f"https://commons.wikimedia.org/w/api.php?action=query&titles={urllib.parse.quote(file_title)}&prop=imageinfo&iiprop=url&format=json"
        req = urllib.request.Request(url, headers={'User-Agent': 'BenaqaabBot/3.0 (educational journalism)'})
        with urllib.request.urlopen(req, timeout=12) as resp:
            data = json.loads(resp.read().decode())
        pages = data.get('query', {}).get('pages', {})
        for pid, pinfo in pages.items():
            if 'imageinfo' in pinfo:
                return pinfo['imageinfo'][0]['url']
    except Exception as e:
        print(f"Error fetching url for {file_title}: {e}")
    return None

def download_and_crop(img_url, dest_path):
    try:
        req = urllib.request.Request(img_url, headers={'User-Agent': 'BenaqaabBot/3.0 (educational journalism)'})
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
    print("🚀 Fetching remaining real plates...")
    for filename, title in TARGETS:
        dest = AI_DIR / filename
        print(f"\nProcessing {filename} -> {title}")
        img_url = fetch_file_url(title)
        if img_url:
            print(f"Downloading: {img_url}")
            if download_and_crop(img_url, dest):
                print(f"✅ Created 1080p plate: {filename}")
            else:
                print(f"❌ Failed download/crop: {filename}")
        else:
            print(f"❌ URL not found for {title}")
        time.sleep(2.0)

if __name__ == "__main__":
    main()
