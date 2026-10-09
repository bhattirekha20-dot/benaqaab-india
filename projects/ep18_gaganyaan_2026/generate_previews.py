from playwright.sync_api import sync_playwright
import os

preview_dir = 'projects/ep18_gaganyaan_2026/previews'
os.makedirs(preview_dir, exist_ok=True)

html_path = 'file:///' + os.path.abspath('projects/ep18_gaganyaan_2026/comp.html').replace('\\', '/') + '?render=1'

beats_to_capture = [
    (2.0, '01_intro_roadmap_hook.jpg', '00:02 — 3-Step Roadmap Hook Card (Act 0)'),
    (8.5, '02_pib_gazette_lively_highlighter.jpg', '00:08 — PIB Gazette with Dynamic Yellow Text Highlighter'),
    (14.0, '03_burning_question_vyommitra.jpg', '00:14 — Burning Question 01: Why Robot Before Humans?'),
    (20.0, '04_real_hlvm3_assembly_stack.jpg', '00:20 — Real Official ISRO Assembly Stack at SDSC SHAR'),
    (28.5, '05_channel_subscribe_bell_cta.jpg', '00:28 — Channel Logo + Animated Subscribe/Bell Micro-Interaction'),
    (33.0, '06_ccea_8_missions_roadmap.jpg', '00:33 — CCEA 8-Mission Roadmap by Dec 2028'),
    (45.0, '07_geopolitical_space_station_race.jpg', '00:45 — Geopolitical Race: ISS Retiring & Tiangong Monopoly'),
    (76.0, '08_cryo_chokepoint_loupe.jpg', '01:16 — CE-20 Cryogenic Extreme Physics & Evidence Loupe'),
    (88.0, '09_real_ce20_world_record_test.jpg', '01:28 — Real ISRO 8,810s World Record Hot Test at IPRC'),
    (125.0, '10_real_tvd1_supersonic_abort.jpg', '02:05 — Real PIB Photo: TV-D1 Supersonic Separation at Mach 1.2'),
    (150.0, '11_water_recovery_verdict_stamp.jpg', '02:30 — Real Crew Module Sea Recovery & Qualified Verdict Stamp'),
    (218.0, '12_real_pmo_astronaut_wings_vssc.jpg', '03:38 — Real PMO Photo: PM Modi Bestows Wings to 4 Gaganyatris'),
    (242.0, '13_real_shukla_nasa_axiom4_iss.jpg', '04:02 — Real NASA Photo: Wg Cdr Shukla with Commander Whitson'),
    (280.0, '14_bas_full_space_station_2035.jpg', '04:40 — 2035 Full 52-Tonne Bharatiya Antariksh Station'),
    (304.0, '15_moon_2040_final_verdict_stamp.jpg', '05:04 — 2040 Manned Moon Landing & Sovereign Verdict Stamp')
]

with sync_playwright() as pw:
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={'width': 1920, 'height': 1080})
    page.goto(html_path)
    page.add_style_tag(content='header, .controls-bar { display: none !important; } body, html, .stage-container, .canvas-wrapper { margin: 0 !important; padding: 0 !important; max-width: none !important; width: 1920px !important; height: 1080px !important; border-radius: 0 !important; box-shadow: none !important; overflow: hidden !important; background: #000 !important; } canvas { position: fixed !important; top: 0 !important; left: 0 !important; width: 1920px !important; height: 1080px !important; display: block !important; }')
    page.wait_for_timeout(2000)
    
    for t, fname, label in beats_to_capture:
        page.evaluate(f'window.seek({t})')
        page.wait_for_timeout(150)
        out_p = os.path.join(preview_dir, fname)
        page.screenshot(path=out_p, quality=92, type='jpeg')
        print(f"Captured: {fname} ({label})")
        
    browser.close()

print("All preview stills captured cleanly!")
