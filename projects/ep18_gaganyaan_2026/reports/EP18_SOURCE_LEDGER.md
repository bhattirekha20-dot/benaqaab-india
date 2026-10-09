# EP-18 · Gaganyaan 2026 — Official Source Media Ledger
**Channel:** Benaqaab India (बेनाक़ाब इंडिया) · **Verified on:** 2026-10-10
**Asset root:** `projects/ep18_gaganyaan_2026/assets/official_sources/`

---

## ⚠️ Read this first — the input ledger had serious errors

The 25-asset ledger supplied with the brief **could not be executed as written**. Every URL and PRID
below was HTTP-checked live in this session. Findings:

| Ledger claim | Actual result of the check |
|---|---|
| SRC-01 → `pib.gov.in/PressReleasePage.aspx?PRID=2056108` = Cabinet Gaganyaan/BAS approval | **FALSE.** PRID 2056108 is *"गति शक्ति विश्वविद्यालय और मोनाश यूनिवर्सिस्टी…"* — a Ministry of Railways MoU, PIB Chandigarh, 17 Sep 2024. Correct PRID is **2055978**. |
| SRC-06 → `PRID=1969620` = TV-D1 parachutes | **FALSE.** PRID 1969620 is *"Ministry of Mines … Special Campaign 3.0"*, PIB Delhi. Correct TV-D1 PRID is **1969644**. |
| `isro.gov.in/LVM3.html` | **HTTP 404** — page does not exist. |
| `isro.gov.in/CE20_Human_Rated_Cryogenic_Engine.html` | **HTTP 404** — page does not exist. |
| `isro.gov.in/TV_D1_Mission.html` | **HTTP 404** — real page is `Gaganyaan_TV-D1_Mission.html`. |
| `lpsc.gov.in` | **DNS does not resolve.** Must be `www.lpsc.gov.in`. |
| `isro.gov.in/media/isro-image` | **HTTP 404.** ISRO media actually lives at `/media_isro/image/…`. |
| SRC-09 "IISU Robotics and Humanoid Actuators" bulletin | **Does not exist.** IISU has no such publication; the ISRO IISU page carries only a campus photo. Note: ISRO's *"MISSION MITRA"* page is a **Ladakh analog crew-psychology mission**, not the Vyommitra robot — easy to confuse. |
| SRC-14 ECLSS cabin photo, SRC-15 crew module cutaway, SRC-16 CES static firing, SRC-17 human-rated Vikas, SRC-18 S200 acoustic test, SRC-20 ESA Kourou antenna, SRC-21 INS Dhruv, SRC-22 BAS-01 render, SRC-24 PAT-1 | **No official public image found** on the listed portals (see Gap Register below). Not fabricated — listed as gaps. |
| Naming convention (`.jpg` only) | **Not workable.** ISRO's current site serves **WebP** originals; there is no `.jpg` behind them (stripping `.webp` returns HTTP 404). Extensions were set from actual file signatures. |

**Net result:** **75 files retrieved from 23 verified official sources, 123.3 MB.** 16 requested subjects have
**no** publicly released official image and are logged in the Gap Register rather than substituted with third-party material.

---

## ✅ RETRIEVED — verified official assets

### SRC-01 · Cabinet approval, ₹20,193 Cr + BAS-01 — text evidence
- **Page:** https://www.pib.gov.in/PressReleasePage.aspx?PRID=2055978
- **Entity / date:** PIB Delhi (Cabinet Secretariat / Dept. of Space) · **18 Sep 2024, 3:10 PM**
- **Title:** *"Bharatiya Anthariksh Station (BAS): Our own Space Station for Scientific research to be established with the launch of its first module in 2028"*
- **Key facts:** net additional ₹11,170 Cr; total revised funding **₹20,193 Cr**; eight missions by Dec 2028; BAS-01 first module 2028.
- **⚠ No photograph is embedded in this release.** The evidence asset is the release text — capture as a screen-record or use the PMO mirror (SRC-24). Do not source a "₹20,193 Cr" photo from anywhere else.

### SRC-02 · Human-Rated LVM3 (HLVM3) — Gaganyaan-G1 assembly ⭐ best-in-set
- **Page:** https://www.isro.gov.in/LVM3_first_uncrewed_flight_Gaganyaan.html
- **Entity / date:** ISRO / SDSC SHAR
- **Files:** `src_02_…_01.png` (767×1150), `…_02.png` (1600×1062), **`…_03.png` (2752×4128, 17.3 MB)** ← hero image
- **Caption:** *"Gaganyaan-G1 Launch campaign commences: Human Rated LVM3 assembly starts at SDSC for the first uncrewed flight."*

### SRC-03 · CE-20 cryogenic engine tests, IPRC Mahendragiri
- **Pages:** `LVM3_CE20_vacuum_ignition_trial_cryogenic_engine_successful.html`, `CE20_Cryogenic_Engine_flight_acceptance_hot_test_successful_LVM3-M6_Mission.html`, `Boot_Strap_Mode_CE20_Cryogenic_Engine.html`, `Successful_Hot_Test_of_CE20_Cryogenic.html`
- **Entity:** ISRO / IPRC Mahendragiri (LPSC)
- **Files:** 6 images, best are `…_03.webp` (3000×2000) and `…_04.webp` (2400×1600)
- **Note:** The ledger's claim of a "8,810 s human-rating qualification" release dated 21 Feb 2024 at that URL is **unverified** — no such page exists. Use these test stills with the actual ISRO release titles above.

### SRC-04 / SRC-04P · TV-D1 abort mission, 21 Oct 2023 ⭐ best-in-set
- **Page:** https://www.isro.gov.in/Gaganyaan_TV-D1_Mission.html
- **Images:** `ANN_9677.jpg.webp` (**4912×7360**), `BPT_9811.jpg.webp` (**3648×5472**)
- **PDF:** `TVD1_Brochure_new.pdf` — **13.2 MB official ISRO mission brochure** (mission profile, abort sequence). Best primary documentary evidence in the whole set.

### SRC-05 · TV-D1 CES/CM separation — PIB official photographs ⭐
- **Page:** https://www.pib.gov.in/PressReleasePage.aspx?PRID=1969644
- **Entity / date:** PIB Delhi / Dept. of Space · **21 Oct 2023, 12:18 PM**
- **Files:** 3 JPGs — 2778×2424, 2644×2723, **5301×3472**
- **Release:** *"Test flight success of Abort Mission-1 (TV-D1) heralds successive sequential trial flights before the final 'Gaganyaan' launch" — MoS Space Dr Jitendra Singh.*
- **Wayback:** http://web.archive.org/web/20251018193816/https://www.pib.gov.in/PressReleasePage.aspx?PRID=1969644

### SRC-06 · Crew module under main parachute (IMAT / IADT)
- **Pages:** `Integrated_Main_Parachute_Air_Drop_Test.html`, `Integrated_Air_Drop_Test_for_Gaganyaan_Missions.html`, `ISRO_conducts_Second_Integrated_Air_Drop_Test_for_Gaganyaan.html`
- **Files:** 9 images incl. **`Crew_module.jpg` 5760×3840**, `Airlift.jpg` 3984×2656, `iADT_img2.jpg.webp` 6000×4000
- **⚠ Honesty note:** these are **air-drop test** frames, **not** the TV-D1 Bay of Bengal sea recovery. Do not caption them as TV-D1 splashdown.

### SRC-07 · Crew module flotation / water-recovery qualification tests
- **Page:** https://www.isro.gov.in/Tests_Crew_Module_systems_of_Gaganyaan_Mission.html
- **Files:** 3 images, 3000×4000 / 3060×4080 (floatation, umbilical separation, crew module)
- **⚠ This is NOT the Indian Navy sea recovery.** No Indian Navy / MoD official recovery photograph was located on a government portal in this session.

### SRC-08 · ISRO Gaganyaan official image set
- **Page:** https://www.isro.gov.in/Gaganyaan.html · 7 files (162×372 to 674×319)
- **⚠ Low resolution.** These are the site's own thumbnails — usable for B-roll at small size or as on-screen references, not for full-frame 4K.

### SRC-09 · Drogue parachute deployment tests
- **Page:** https://www.isro.gov.in/Drogue_Parachute_Test.html · 1306×1077, 1242×750
- **Wayback:** http://web.archive.org/web/20250714093821/https://www.isro.gov.in/Drogue_Parachute_Test.html

### SRC-10 · PM Modi bestows astronaut wings, VSSC — 27 Feb 2024 ⭐
- **Page:** https://www.pmindia.gov.in/en/news_updates/pm-visits-vikram-sarabhai-space-center-vssc-in-thiruvananthapuram-kerala/
- **Entity / date:** Prime Minister's Office · **27 Feb 2024**
- **Files:** `H20240227154907.jpg` (**2200×2486**) and the og:image hero (1600×996)
- **Wayback:** http://web.archive.org/web/20250430034154/…

### SRC-11 · Service Module Propulsion System (SMPS)
- **Pages:** `Successful_hot_tests_Gaganyaan_SMPS.html`, `Successful_accomplishment_SMPS_Gaganyaan.html` · Jul 2025 · 1280×853, 855×570

### SRC-12 · Gaganyatri Shubhanshu Shukla / Axiom-4 ⭐ best-in-set
**Two independent official sources:**

**(a) NASA — public domain, 8256×5504 originals** (via `images-api.nasa.gov`)
| File | NASA ID | Title |
|---|---|---|
| `src_12_nasa_axiom4_01_iss073e0252429.jpg` | iss073e0252429 | Shubhanshu Shukla poses for a portrait (10.5 MB) |
| `src_12_nasa_axiom4_02_iss073e0252954.jpg` | iss073e0252954 | Peggy Whitson and Shubhanshu Shukla |
| `src_12_nasa_axiom4_03_iss073e0511059.jpg` | iss073e0511059 | Expedition 73 and Ax-4 astronauts pose for a portrait |
| `src_12_nasa_axiom4_04_iss073e0249239.jpg` | iss073e0249239 | Ax-4 private astronauts gather inside the ISS |
| `src_12_nasa_axiom4_05_iss073e0249698.jpg` | iss073e0249698 | Ax-4 and Expedition 73 group portrait |
| `src_12_nasa_axiom4_06_iss073e0249492.jpg` | iss073e0249492 | Dragon carrying Ax-4 approaches the ISS |
| `src_12_nasa_axiom4_07_iss073e0252473.jpg` | iss073e0252473 | Jonny Kim joins Ax-4 crew for lunch |
| `src_12_nasa_axiom4_08_NHQ202509150011.jpg` | NHQ202509150011 | Crew at the Indian Ambassador's residence (7900×4657, 17.9 MB) |

Detail pages: `https://images.nasa.gov/details/<NASA_ID>`

**(b) ISRO official set** — `Axiom04_mission_successfully_concluded_return_ISRO_Gaganyatri_ShubhanshuShukla.html` yields 7 PNGs of which **4 were sub-400px thumbnails** (352×265, 346×194, 334×250, 372×251) and have been moved to `_superseded_lowres/`; 3 remain at 553–622px wide. Better ISRO frames from adjacent release pages: **`src_12_ax4_farewell_05.webp` 1600×1039** (farewell address aboard ISS, 14 Jul 2025), `src_12_ax4_experiments_06.jpg` 1280×774 (sprouting experiment) and `…_07.jpg` 1280×703 (myogenesis experiment).

### SRC-13 · Ax-4 Crew Dragon undocking from ISS
- **Page:** https://www.isro.gov.in/Axiom4_Successful_Undocking_of_Crew_Dragon_Spacecraft.html · 2 PNGs (672×378, 691×389)

### SRC-14 · ISRO–NASA Ax-4 post-splashdown
- **Page:** https://www.isro.gov.in/ISRO_NASA_Axiom4_mission_post_splash_down_activities.html · 17 Jul 2025
- **Files:** incl. **5120×3840** and **3024×4032**
- **Wayback:** http://web.archive.org/web/20251021123629/…

### SRC-15 · Gaganyatri Shukla with Dr V Narayanan, Chairman ISRO
- **Page:** https://www.isro.gov.in/GaganyatriShubhanshuShukla_called_Dr_V_Narayanan.html · 1379×919, 1152×864, 1280×963

### SRC-16 to SRC-21 · Official ISRO centre imagery
| ID | Subject | Page | Best size |
|---|---|---|---|
| SRC-16 | Human Space Flight Centre (HSFC), Bengaluru | `HSFC.html` | 1023×683 ×3 |
| SRC-17 | Mission Control Centre, SDSC SHAR | `SDSC.html` | 1024×683 |
| SRC-18 | ISRO Propulsion Complex, Mahendragiri | `IPRC.html` | 1023×244 |
| SRC-19 | Vikram Sarabhai Space Centre | `VSSC.html` | 1023×680 |
| SRC-20 | ISRO Inertial Systems Unit (IISU) | `IISU.html` | 1023×673 |
| SRC-21 | Liquid Propulsion Systems Centre (LPSC) | `LPSC.html` | **4496×2435** |

### SRC-22 · ISRO Space Analog Mission, Tso Kar Valley, Ladakh
- **Page:** https://www.isro.gov.in/Space_Analog_Mission.html · 2043×588, 602×338

### SRC-23 · Rajya Sabha reply — Gaganyaan milestones + BAS roadmap ⭐ key textual evidence
- **Page:** https://www.pib.gov.in/PressReleasePage.aspx?PRID=2295557
- **Entity / date:** PIB Delhi / Dept. of Space · **6 Aug 2026, 5:00 PM**
- **Content:** *"First uncrewed Gaganyaan mission carrying Vyommitra targeted in Q4 2026"*; all five CES motor types developed and static-tested; Orbital Module Preparation Facility, Gaganyaan Control Centre, Crew Training Facility and Second Launch Pad modifications established; BAS on track for 2035.
- **This is the single most current authoritative source for the EP-18 2026 timeline.** No photo — text evidence.

### SRC-24 · PMO mirror of the Sept 2024 BAS approval
- **Page:** https://www.pmindia.gov.in/en/news_updates/bharatiya-anthariksh-station-bas-our-own-space-station-for-scientific-research-to-be-established-with-the-launch-of-its-first-module-in-2028/ · 18 Sep 2024

### SRC-25 · 3rd National Space Day 2026, Ahmedabad
- **Page:** https://www.isro.gov.in/3rd_National_Space_Day_2026.html · 24 Aug 2026 · **5472×3648**
- **Wayback:** http://web.archive.org/web/20260827140601/…

---

## 🕳️ GAP REGISTER — requested subjects with NO official public image

Do **not** fill these with stock, agency wire, or AI-generated material. Options given are the honest routes.

| # | Requested subject | Status | Honest path forward |
|---|---|---|---|
| G1 | Vyommitra robot in crew module | **No ISRO/VSSC official page or photo exists.** Vyommitra was unveiled 22 Jan 2020 at a Bengaluru symposium; all circulating imagery is press/ANI. Wayback CDX query for `isro.gov.in/*vyommitra*` returned **zero** captures. | RTI request to HSFC Bengaluru / VSSC; or film the Q4-2026 G1 mission coverage live. |
| G2 | Vyommitra actuators / IISU technical bulletin | **Publication does not exist.** | Drop from the script, or RTI. |
| G3 | Four Gaganyatris official group portrait | **Not on pib.gov.in or isro.gov.in.** Widely circulated versions are PTI wire. PMO's 27 Feb 2024 page (SRC-10) is the official photo of the event. | Use SRC-10; or licence the PTI frame properly. |
| G4 | Gaganyatris at Gagarin CTC, Star City | **Not on Roscosmos/Glavkosmos public pages.** Confirmed only indirectly: SRC-23 PIB reply states *"generic training of IAF pilots … completed in Russia."* | Text citation only, or RTI to HSFC. |
| G5 | ECLSS test cabin, VSSC | **No image on vssc.gov.in.** | RTI; or cite the DoS Demands for Grants text. |
| G6 | Crew module cutaway schematic | **No public official schematic.** The TV-D1 brochure (SRC-04P, 13 MB) is the closest legitimate engineering document — extract diagrams from it. | Mine `TVD1_Brochure_new.pdf`. |
| G7 | CES HEM/LEM static firing | No standalone photo. SRC-23 (PIB, 6 Aug 2026) confirms in text all 5 CES motor types static-tested. | Text + brochure diagrams. |
| G8 | Human-rated Vikas engine on test stand | **Nothing on www.lpsc.gov.in.** | RTI to LPSC. |
| G9 | S200/HS200 solid booster acoustic test | **Not found on isro.gov.in.** | RTI to SDSC SHAR. |
| G10 | ISTRAC / MOX Bengaluru ops floor | ISTRAC page carries only a 1-file GIF banner. | ISRO press office request. |
| G11 | ESA Kourou tracking antenna for Gaganyaan | **Not verifiable** — no ESA release found tying a specific Kourou antenna to Gaganyaan ascent tracking. Treat the claim itself as unconfirmed. | ESA ESTRACK media office. |
| G12 | INS Dhruv at sea | **Not on indiannavy.nic.in in this session.** | MoD/Indian Navy spokesperson request. |
| G13 | BAS-01 concept render | **No official ISRO render published.** A 1:1 BAS-01 engineering model was unveiled at a National Space Day event, but no official ISRO image URL was found. | ISRO press office; National Space Day coverage. |
| G14 | Lok Sabha/Rajya Sabha question sheet (sansad.in) | sansad.in question PDFs are not directly linkable without session/question numbers. **SRC-23 (PIB 2295557) and the 7 Aug 2025 PIB reply are the authoritative published versions of the same answers.** | Use SRC-23; or pull the exact PDF from `sansad.in` once the question number is known. |
| G15 | Pad Abort Test-1 (PAT-1, July 2018) | **No page on the current isro.gov.in.** Pre-2020 ISRO press pages are not archived under the queried paths. | ISRO archive request; or Wayback deep-crawl of the old site structure. |
| G16 | ISRO Vision 2047 roadmap slide | No official "Vision 2047 document" image found. SRC-23 + SRC-01 give the same milestones in authoritative text (BAS-01 2028, full station 2035, crewed lunar 2040). | Cite text; build your own graphic from the official numbers. |

---

## ⚖️ Rights & attribution — practical guidance

1. **NASA (SRC-12a):** US federal government works, **public domain**. Cite as *"NASA"*. Free for commercial documentary use. Verify each item's `images.nasa.gov` detail page — a small number of NASA images carry third-party restrictions; the eight pulled here are JSC/HQ staff photography.
2. **ISRO (most of this set):** © ISRO. ISRO generally permits use of its imagery for **news, education and non-commercial** purposes with credit. A monetised YouTube documentary is a **commercial** use — obtain written permission from the ISRO Department of Communication / relevant centre before broadcast. Credit line: *"Courtesy: ISRO"*.
3. **PIB (SRC-01, 05, 23):** Government of India, PIB. Permitted for news/commentary with attribution. Credit: *"Courtesy: PIB / Press Information Bureau, Government of India."*
4. **PMO (SRC-10, 24):** Prime Minister's Office. Credit: *"Courtesy: PMO India / Prime Minister's Office."* Same commercial caveat.
5. **On-screen minimum:** every asset should carry a lower-third source bug naming the entity and date. The CSV has a `credit` column ready for your editor.
6. **Do not** re-caption air-drop tests (SRC-06) as TV-D1 splashdown, or the PMO event photo (SRC-10) as an "official four-astronaut portrait." Both are common factual errors in this beat.

---

## 📦 Package contents

```
projects/ep18_gaganyaan_2026/
├── assets/official_sources/          75 files · 123.3 MB (21 jpg, 43 webp, 10 png, 1 pdf)
│   └── _superseded_lowres/           4 ISRO thumbnails replaced by NASA originals
└── reports/
    ├── EP18_SOURCE_LEDGER.md         this document
    ├── EP18_SOURCE_LEDGER.csv        editor-ready: id, filename, WxH, entity, date, caption, URL, wayback, credit
    └── EP18_SOURCE_LEDGER.json       same, machine-readable
```

**Retrieval stats:** 75 files · 123.3 MB · 23 verified sources · 0 failed downloads · 0 orphans
(ledger record count reconciled against the directory listing — 75 = 75). Every file's format was
confirmed by magic-byte inspection and every image's pixel dimensions read from its header.
