#!/usr/bin/env python3
"""
🖼️ BENAQAAB VISUAL ASSET MASTER LEDGER GENERATOR
Scans every image in the repository, determines its project linking, archetype,
forensic significance, color profile, and AI agent usage directives.
Outputs:
1. brand/visual_assets_ledger.json (machine-readable)
2. VISUAL_ASSET_MASTER_LEDGER.md (human & AI markdown documentation)
"""

import os
import sys
import json
from pathlib import Path
from PIL import Image

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def classify_asset(path, name, folder, w, h):
    p = path.lower()
    
    # 1. BRAND & IDENTITY
    if folder == "brand":
        if "logo" in name.lower():
            return {
                "project_id": "BRAND",
                "archetype": "Brand Identity & Watermark",
                "subject": "Official Benaqaab India OS Logo Bug",
                "significance": "Canonical channel branding emblem. Top-left placement creates instant viewer recognition across Shorts and long-form documentaries.",
                "color_profile": "Universal (Brand Alpha)",
                "agent_instruction": "Composite at top-left safe area (X: 32-55px, Y: 30-40px on 1080x1920) with 85-95% opacity. Never occlude with headline text."
            }
        elif "ref_investigative" in name.lower() or "minimal" in name.lower():
            return {
                "project_id": "BRAND",
                "archetype": "Style Benchmark & Visual Standard",
                "subject": "Investigative Layout & Density Benchmark",
                "significance": "Defines high-contrast typography, dark card boundaries, pinboard lines, and minimal 65-75% screen occupancy standards.",
                "color_profile": "Profile B (Forensic Dossier)",
                "agent_instruction": "Consult during scene design. Ensure card borders are 1px solid rgba(255,255,255,0.08) and typography has clear hierarchy."
            }
    
    # 2. BRAND HOST PHONEMES & CUTOUTS
    if folder == "brand/host":
        if "rgba" in name.lower():
            return {
                "project_id": "BRAND_HOST",
                "archetype": "Host Alpha Cutout",
                "subject": "Transparent Presenter Overlay",
                "significance": "Alpha-channel presenter frame for composited talking-head commentary, keeping human screen time strictly under 20%.",
                "color_profile": "Universal",
                "agent_instruction": "Anchor to bottom-left or bottom-right corner. Maintain presenter scale under 35% of total viewport height."
            }
        else:
            return {
                "project_id": "BRAND_HOST",
                "archetype": "Host Lip-Sync Phoneme",
                "subject": f"Presenter Mouth Phoneme State ({name.split('.')[0].replace('host_', '')})",
                "significance": "Discrete mouth shape (closed, mid, open) driven by voiceover audio RMS amplitude to deliver natural lip-sync animation.",
                "color_profile": "Universal",
                "agent_instruction": "Swap image based on audio RMS threshold in comp.html canvas loop: base (RMS < 0.05), mid (0.05-0.18), open (> 0.18)."
            }

    # 3. BRAND STYLE REFS & COPYRIGHT TREATMENT
    if folder == "brand/style_refs":
        return {
            "project_id": "STYLE_REF",
            "archetype": "Broadcast Video Copyright Protection Standard",
            "subject": "MEA / Dr. Jaishankar Forensic Stylization Benchmark",
            "significance": "Demonstrates the official Benaqaab newsprint halftone filter + red redaction bar applied to government and broadcast clips to defeat automated copyright strikes while establishing an unmistakable investigative look.",
            "color_profile": "Profile B (Forensic Dossier)",
            "agent_instruction": "When incorporating external news or MEA footage, apply halftone dot grid and red horizontal bar (#ef4444 at 65% opacity) over eyes/face as demonstrated in this reference."
        }

    # 4. CREATOR UPLOADS
    if folder == "uploads":
        if "image-1" in name:
            return {
                "project_id": "CREATOR_DIRECTIVE",
                "archetype": "Clean Reference Capture",
                "subject": "Dr. S. Jaishankar Halftone & Red Bar Treatment Frame",
                "significance": "High-resolution digital master of the visual treatment requested by the creator for all source footage integration.",
                "color_profile": "Profile B (Forensic Dossier)",
                "agent_instruction": "Use as reference when implementing the dynamic broadcast filter in canvas or PIL pipeline."
            }
        else:
            return {
                "project_id": "CREATOR_DIRECTIVE",
                "archetype": "Creator Operational Directives",
                "subject": "Photographed Mobile Directives (Copyright Safe + motion.py Preservation)",
                "significance": "Historic direct instructions from the channel creator commanding: (1) source video protection via visual treatment, and (2) absolute preservation of motion.py and rendering tools.",
                "color_profile": "Historical Record",
                "agent_instruction": "Read instructions embedded in this image to understand the creator's non-negotiable intent regarding toolchain stability and copyright safety."
            }

    # 5. KNOWLEDGE & 3D RESEARCH
    if folder.startswith("knowledge"):
        return {
            "project_id": "KNOWLEDGE",
            "archetype": "Research Benchmark",
            "subject": "3D Spatial Parallax Camera Study",
            "significance": "Exploration of virtual camera dollying, depth maps, and multi-plane evidence layering in investigative documentaries.",
            "color_profile": "Research",
            "agent_instruction": "Use as mathematical reference for virtual camera pan, zoom, and tilt parameters in video-canvas-motion."
        }

    # 6. SH-11: WORLD NEWS 24H
    if "world_news_24h" in p:
        if "photo_" in name:
            subject_map = {
                "photo_germany.jpg": "Story 1: Germany BND Domestic Intelligence Arrest (Russian Sabotage)",
                "photo_france.jpg": "Story 2: France High School Anti-Austerity Protests",
                "photo_kenya.jpg": "Story 3: Kenya Health Authority Suspected Hemorrhagic Fever Case",
                "photo_quebec.jpg": "Story 4: Canada Quebec By-Election Polling Station",
                "photo_icecube.jpg": "Story 5: Antarctica IceCube Neutrino Observatory (Nobel Prize)",
                "photo_science.jpg": "Story 5: Physics Nobel Prize Cosmic Neutrino Discovery",
                "photo_check.jpg": "Fact-Check Verified Badge Stamp"
            }
            sub = subject_map.get(name, "Verified World News Photo")
            return {
                "project_id": "SH-11",
                "archetype": "Verified Editorial News Photo",
                "subject": sub,
                "significance": "Real primary-source editorial photograph backing the spoken narration of World News 24H with zero AI hallucinations.",
                "color_profile": "Profile A (Neutral News: 6200K, Sat 1.02, Contrast 1.06)",
                "agent_instruction": "Draw on canvas background with slow Ken Burns drift (1.00x -> 1.06x over 8s). Pair with yellow highlighter on document text."
            }
        elif "ai_" in name:
            return {
                "project_id": "SH-11",
                "archetype": "Forensic Background Texture",
                "subject": f"Atmospheric News Backdrop ({name.split('.')[0].replace('ai_', '').capitalize()})",
                "significance": "Subtle thematic background texture used under semi-transparent documents, data tables, and evidence loupe callouts.",
                "color_profile": "Profile A (Neutral News)",
                "agent_instruction": "Layer behind evidence cards with 40-50% opacity and 8px gaussian blur. Never use as standalone primary evidence."
            }
        elif "thumbnail" in name or "cover" in name:
            return {
                "project_id": "SH-11",
                "archetype": "Delivery Thumbnail Pack",
                "subject": f"SH-11 Delivery Cover ({w}x{h})",
                "significance": "Uncropped public thumbnail package for YouTube Shorts and horizontal displays featuring bold 4-word hook and top-left logo.",
                "color_profile": "Profile A (Neutral News)",
                "agent_instruction": "Present directly in root and delivery/ for user download and YouTube Studio upload."
            }
        elif "qa" in name or "frame_" in name or "preview" in name:
            return {
                "project_id": "SH-11",
                "archetype": "Render QA Proof",
                "subject": f"Headless Browser Timeline Capture ({name})",
                "significance": "Deterministic QA screenshot captured during headless Chromium Playwright rendering to audit typography, contrast, and safe zones.",
                "color_profile": "QA Audit",
                "agent_instruction": "Inspect to verify that no headline text enters the forbidden safe zone margins (Top 230px, Bottom 423px, Right 173px)."
            }

    # 7. SH-09: INDIA LAST 24H
    if "india_last_24h" in p:
        if "source_images" in folder:
            subject_map = {
                "air_chief_pib": "Story 1: IAF Chief AP Singh Press Conference (PIB Official)",
                "sme_growth_fund": "Story 2: SEBI SME IPO Crackdown & Valuation Disclosure (PIB)",
                "bcci": "Story 3: ICC Women's T20 World Cup Highlights (BCCI Public)",
                "rahul_gandhi": "Story 4: Rahul Gandhi Kolhapur Rally & Statue Address",
                "dri_gold": "National Brief: DRI Gold Seizure Operations (PIB)",
                "eci_security": "Electoral Commission Security Protocol",
                "itla_pib": "National Infrastructure & Transport Update (PIB)"
            }
            sub = "Verified National News Photo"
            for k, v in subject_map.items():
                if k in name.lower():
                    sub = v
                    break
            return {
                "project_id": "SH-09",
                "archetype": "Verified Editorial News Photo",
                "subject": sub,
                "significance": "Real primary source news image from official Indian government (PIB), sporting, or public registries establishing documentary authenticity.",
                "color_profile": "Profile A (Neutral News)",
                "agent_instruction": "Render as focal proof in the relevant story segment. Accompany with dynamic FACT_LEDGER data ticker."
            }
        elif "text_" in name:
            return {
                "project_id": "SH-09",
                "archetype": "Kinetic Typography Alpha Layer",
                "subject": f"Segment Caption Overlay ({name.split('.')[0]})",
                "significance": "Pre-rendered typographic headline layer with alpha transparency for high-performance canvas compositing.",
                "color_profile": "Typography Alpha",
                "agent_instruction": "Composite at safe Y-position (Y: 1350-1420px) synchronized with voiceover narration timestamps."
            }
        elif "scene_" in name or "render_frame" in name or "preview_bg" in name:
            return {
                "project_id": "SH-09",
                "archetype": "Export Motion Frame / Scene Composite",
                "subject": f"National News Timeline Frame ({name.split('.')[0]})",
                "significance": "Rendered video sequence frame capturing national news stories, weather ticker, cricket scores, and closing sign-off.",
                "color_profile": "Profile A (Neutral News)",
                "agent_instruction": "Verify timeline transition continuity and safe-zone compliance."
            }
        elif "proof_" in name or "qc_" in name:
            return {
                "project_id": "SH-09",
                "archetype": "Render QA Proof",
                "subject": f"Quality Control Verification Frame ({name})",
                "significance": "Milestone frame certified during 1-gate approval check to confirm color grading, audio sync, and text readability.",
                "color_profile": "QA Audit",
                "agent_instruction": "Use to ensure video meets Benaqaab 10-point production standards."
            }
        elif "thumbnail" in name or "cover" in name:
            return {
                "project_id": "SH-09",
                "archetype": "Delivery Thumbnail Pack",
                "subject": f"SH-09 Delivery Cover ({w}x{h})",
                "significance": "High-impact delivery thumbnail for India Last 24 Hours roundup.",
                "color_profile": "Profile A",
                "agent_instruction": "Serve in delivery/ for platform upload."
            }

    # 8. SH-08: GOLD 150K
    if "gold_150k" in p:
        if "shots" in folder:
            shots_map = {
                "shot_01_bullion.jpg": "Shot 1: Bank Bullion Vault 99.9% Gold Stacks (Reserve Accumulation)",
                "shot_02_showroom.jpg": "Shot 2: Indian Jewelry Retail Showroom (Domestic Bridal Demand)",
                "shot_03_melting.jpg": "Shot 3: Goldsmith Crucible Melting (Scrap Recycling & Fabrication)",
                "shot_04_etf.jpg": "Shot 4: Digital Gold ETF & SGB Price Chart (Investment Inflows)"
            }
            return {
                "project_id": "SH-08",
                "archetype": "Forensic Hero Photo",
                "subject": shots_map.get(name, "Gold Investigation Hero Photo"),
                "significance": "High-fidelity investigative shot visually driving one of the 4 core pillars of the 1.5 Lakh Gold price analysis.",
                "color_profile": "Profile B (Forensic Dossier: Warm Gold Tonal Accent)",
                "agent_instruction": "Bind to respective narration act: Bullion (0-14s), Showroom (14-27s), Melting (27-40s), ETF (40-54s)."
            }
        else:
            return {
                "project_id": "SH-08",
                "archetype": "Delivery Thumbnail Pack",
                "subject": f"SH-08 Gold Investigation Cover ({name})",
                "significance": "Uncropped high-CTR thumbnail variants exploring curiosity hooks around gold price surges.",
                "color_profile": "Profile B (Forensic Dossier)",
                "agent_instruction": "Deliver landscape (1280x720) for YouTube search/browse and vertical (1080x1920) for Shorts feed."
            }

    # 9. SH-10: INDIA JAPAN JCM
    if "india_japan_jcm" in p:
        return {
            "project_id": "SH-10",
            "archetype": "Scene Storyboard & Motion Frame",
            "subject": f"Indo-Japan Clean Energy Credit Scene ({name.split('.')[0]})",
            "significance": "Illustrates bilateral climate funding, Joint Crediting Mechanism (JCM) carbon baseline registries, and green technology transfer.",
            "color_profile": "Profile A (Neutral News)",
            "agent_instruction": "Use in scrollytelling canvas stage to demonstrate bilateral environmental cooperation metrics."
        }

    # 10. FL-03: AI MODEL HUGGING FACE HACK
    if "ai_hf_hack" in p:
        if "web" in folder:
            return {
                "project_id": "FL-03",
                "archetype": "Factual Corporate Evidence Logo",
                "subject": f"Corporate Disclosure Identity ({name.split('.')[0].replace('-', ' ').title()})",
                "significance": "Official transparent corporate brand mark of entities involved in the AI supply chain security vulnerability disclosure.",
                "color_profile": "Universal",
                "agent_instruction": "Display on pinboard evidence node when quoting official vulnerability CVE reports."
            }
        elif "images" in folder:
            return {
                "project_id": "FL-03",
                "archetype": "Forensic AI Composite & Scene Storyboard",
                "subject": f"AI Supply Chain Cyber Investigation Scene ({name.split('.')[0]})",
                "significance": "Sequential documentary visual depicting model weight manipulation, malicious serialization, pickle deserialization exploits, and server telemetry.",
                "color_profile": "Profile B (Forensic Dossier: High-Tech Cyan/Dark Amber)",
                "agent_instruction": "Map to scene index in FL-03 comp.html to visualize abstract cyber concepts clearly."
            }
        else:
            return {
                "project_id": "FL-03",
                "archetype": "Delivery Thumbnail Pack",
                "subject": "FL-03 Cyber Security Investigation Thumbnail",
                "significance": "High-contrast YouTube cover for the Hugging Face AI security breakdown.",
                "color_profile": "Profile B",
                "agent_instruction": "Serve as delivery thumbnail."
            }

    # 11. ANIME & COLOR EDIT SHORTS (SH-01, SH-02, SH-03)
    if "anime_edit" in p:
        if "shots" in folder:
            return {
                "project_id": "SH-01",
                "archetype": "Kinetic Shot Breakdown Frame",
                "subject": f"NEON Motion Cut Frame {name.split('.')[0]}",
                "significance": "Fast-paced kinetic animation frame demonstrating rapid montage cutting and color-graded impact frames.",
                "color_profile": "High-Energy Kinetic",
                "agent_instruction": "Study for rapid 12-frame cutting rhythm and dynamic spring deceleration."
            }
        else:
            proj = "SH-01" if "01" in folder else ("SH-02" if "02" in folder else "SH-03")
            return {
                "project_id": proj,
                "archetype": "Delivery Thumbnail",
                "subject": f"{proj} Vertical Cover Art (1080x1920)",
                "significance": "Cover art showcasing specialized monochromatic/neon color grading profiles.",
                "color_profile": "Stylized Color Series",
                "agent_instruction": "Serve as Shorts cover."
            }

    # 12. FLAGSHIP EPISODE THUMBNAILS (EP-12 TO EP-16)
    if any(k in p for k in ["ep12", "ep13", "ep14", "ep15", "ep16"]):
        ep = [k.upper() for k in ["ep12", "ep13", "ep14", "ep15", "ep16"] if k in p][0]
        titles = {
            "EP12": "NavIC GPS Alternative",
            "EP13": "Monsoon Agricultural Economy",
            "EP14": "Bullet Train High-Speed Corridor",
            "EP15": "Rupee Global Currency Push",
            "EP16": "Semiconductor Fab Revolution"
        }
        return {
            "project_id": ep,
            "archetype": "Flagship Delivery Thumbnail",
            "subject": f"{ep}: {titles.get(ep, 'Documentary')} 16:9 Thumbnail",
            "significance": "Official high-resolution 1280x720 YouTube landscape thumbnail with top-left channel branding and sharp curiosity copy.",
            "color_profile": "Profile A / B (Editorial Hybrid)",
            "agent_instruction": "Serve in EP delivery package. Adhere to zero uncropped edges rule."
        }

    # 13. KAGAZ KI MACHINE & FLIGHT SURCHARGE
    if "kagaz_ki_machine" in p or "flight_surcharge" in p:
        proj = "FL-01" if "kagaz" in p else "SH-07"
        return {
            "project_id": proj,
            "archetype": "Delivery Thumbnail Pack",
            "subject": f"{proj} Investigation Thumbnail",
            "significance": "Delivery cover for Electoral Bonds or Airline Surge Pricing investigation.",
            "color_profile": "Profile B / C",
            "agent_instruction": "Serve as platform thumbnail."
        }

    # 14. SAAS ASSETS
    if "saas" in p:
        return {
            "project_id": "SAAS",
            "archetype": "Web App Brand Identity",
            "subject": "Benaqaab OS Analytics Dashboard Logo",
            "significance": "Companion web application brand logo for real-time investigation metrics and project tracking.",
            "color_profile": "Universal",
            "agent_instruction": "Use in header navigation of web dashboards."
        }

    # Fallback
    return {
        "project_id": "GENERAL",
        "archetype": "Supporting Graphic Asset",
        "subject": f"Asset {name}",
        "significance": "Supporting documentary graphic asset.",
        "color_profile": "Universal",
        "agent_instruction": "Maintain aspect ratio and attribution."
    }

def main():
    repo_root = Path(".")
    exts = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
    
    records = []
    for p in sorted(repo_root.rglob("*")):
        if p.is_file() and p.suffix.lower() in exts:
            if ".git" in p.parts:
                continue
            rel_path = str(p).replace("\\", "/")
            name = p.name
            folder = str(p.parent).replace("\\", "/")
            size_bytes = p.stat().st_size
            
            w, h, fmt = None, None, None
            if p.suffix.lower() != ".svg":
                try:
                    with Image.open(p) as im:
                        w, h = im.size
                        fmt = im.format
                except Exception:
                    pass
            
            meta = classify_asset(rel_path, name, folder, w, h)
            rec = {
                "path": rel_path,
                "filename": name,
                "folder": folder,
                "extension": p.suffix.lower(),
                "width": w,
                "height": h,
                "format": fmt,
                "size_bytes": size_bytes,
                **meta
            }
            records.append(rec)

    print(f"✅ Classified {len(records)} visual assets.")

    # 1. Save JSON Ledger
    json_path = Path("brand/visual_assets_ledger.json")
    json_path.parent.mkdir(parents=True, exist_ok=True)
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
    print(f"✅ Saved machine-readable ledger: {json_path}")

    # 2. Generate Markdown Master Ledger
    md_path = Path("VISUAL_ASSET_MASTER_LEDGER.md")
    
    # Group by functional domains
    domains = {
        "1. Brand Identity, Watermarks & UI Graphics": [r for r in records if r["project_id"] in ["BRAND", "SAAS"] and "HOST" not in r["project_id"]],
        "2. Host Talking-Head Lip-Sync Phonemes": [r for r in records if r["project_id"] == "BRAND_HOST"],
        "3. Copyright Protection & Forensic MEA Stylization": [r for r in records if r["project_id"] in ["STYLE_REF", "CREATOR_DIRECTIVE"]],
        "4. SH-11: World News 24H Asset Ecosystem": [r for r in records if r["project_id"] == "SH-11"],
        "5. SH-09: India Last 24 Hours News Roundup": [r for r in records if r["project_id"] == "SH-09"],
        "6. SH-08: Sona 1.5 Lakh Tak (Gold Market Investigation)": [r for r in records if r["project_id"] == "SH-08"],
        "7. SH-10: Indo-Japan Clean Energy Credit Investigation": [r for r in records if r["project_id"] == "SH-10"],
        "8. FL-03: AI Model Supply Chain Security Breach (Hugging Face / JFrog)": [r for r in records if r["project_id"] == "FL-03"],
        "9. SH-01 to SH-03: Dynamic Color & Kinetic Montage Series": [r for r in records if r["project_id"] in ["SH-01", "SH-02", "SH-03"]],
        "10. Flagship Long-Form YouTube Thumbnails (EP-12 to EP-16)": [r for r in records if r["project_id"].startswith("EP")],
        "11. Standalone Documentaries & Investigations (FL-01 / SH-07)": [r for r in records if r["project_id"] in ["FL-01", "SH-07"]],
        "12. Knowledge Base & 3D Parallax Research": [r for r in records if r["project_id"] == "KNOWLEDGE"]
    }

    md_lines = []
    md_lines.append("# 🖼️ VISUAL ASSET MASTER LEDGER & SIGNIFICANCE DIRECTORY")
    md_lines.append("### Comprehensive Mapping of Every Visual Asset, Provenance & AI Usage Directive")
    md_lines.append("")
    md_lines.append("> **Channel:** Benaqaab India (बेनाक़ाब इंडिया)  ")
    md_lines.append("> **Motto:** `SACH · SABOOT · BEBAK` (Truth · Evidence · Uncompromising)  ")
    md_lines.append(f"> **Total Tracked Assets:** {len(records)} images  ")
    md_lines.append("> **Status:** Single Source of Truth for Visual Asset Significance, Provenance & Agent Directives.  ")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")
    md_lines.append("## 📜 THE LAW OF VISUAL SIGNIFICANCE (READ FIRST)")
    md_lines.append("In Benaqaab India, **no image is decorative wallpaper**. Every single image in this repository serves an exact forensic, editorial, or brand purpose:")
    md_lines.append("1. **Every Fact Needs Proof:** If narration makes a factual claim, the image on screen must be verified editorial footage, an official gazette scan, or a primary source photograph—never generic AI slop.")
    md_lines.append("2. **Zero Attribution Hallucination:** Agents must only use images mapped to the current story. Never cross-contaminate assets between unrelated investigations.")
    md_lines.append("3. **Aspect Ratio & Safe Zones:** Images placed on canvas must honor safe zones ($X: 80-900, Y: 240-1480$ on 9:16 vertical) and never stretch or warp.")
    md_lines.append("4. **Three Color Profiles:** All assets must adhere to their designated color profile: **Profile A** (Neutral News: 6200K), **Profile B** (Forensic Dossier: Deep Obsidian & Amber), or **Profile C** (Archival Sepia).")
    md_lines.append("")
    md_lines.append("---")
    md_lines.append("")

    for title, domain_records in domains.items():
        md_lines.append(f"## 📁 {title} ({len(domain_records)} assets)")
        md_lines.append("")
        md_lines.append("| Asset Path | Dim | Archetype | Factual Significance & Narrative Context | Profile | Agent Usage Directive |")
        md_lines.append("|---|---|---|---|---|---|")
        for r in domain_records:
            dim_str = f"{r['width']}x{r['height']}" if r['width'] else "Vector"
            path_link = f"[`{r['filename']}`]({r['path']})"
            md_lines.append(f"| {path_link} | `{dim_str}` | **{r['archetype']}** | {r['significance']} | `{r['color_profile']}` | {r['agent_instruction']} |")
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

    md_lines.append("## 🤖 MACHINE-READABLE INTEGRATION")
    md_lines.append("All metadata is synchronized in [`brand/visual_assets_ledger.json`](brand/visual_assets_ledger.json).")
    md_lines.append("Any Python script or AI agent can inspect asset metadata with:")
    md_lines.append("```python")
    md_lines.append("import json")
    md_lines.append("with open('brand/visual_assets_ledger.json', encoding='utf-8') as f:")
    md_lines.append("    ledger = json.load(f)")
    md_lines.append("# Query by project ID")
    md_lines.append("world_news_photos = [a for a in ledger if a['project_id'] == 'SH-11' and a['archetype'] == 'Verified Editorial News Photo']")
    md_lines.append("```")
    md_lines.append("")
    md_lines.append("*Benaqaab India — Sach • Saboot • Bebak*  ")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md_lines))
    print(f"✅ Generated master markdown ledger: {md_path}")

if __name__ == "__main__":
    main()
