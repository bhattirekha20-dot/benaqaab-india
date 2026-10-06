# EP12 — NavIC: India ka apna GPS kyun band pada hai?
### Step 1 of your Motion Kit: Understand + Plan (no code yet)

## 1. The project in 3 lines
- A 16:9 long-form YouTube explainer (~4:12, under 5 min), with a Hinglish voiceover and English on-screen text.
- What NavIC is, why India built it (Kargil 1999), why it can't give standalone location right now, and what comes next (NVS-03).
- Mostly full-screen motion graphics. The presenter appears only in the intro, one key moment and the outro. Source clips use your B&W, red-band style.

## 2. Facts I have (sourced) / NEED FROM USER
| Fact | Source |
|---|---|
| "Cannot provide standalone positioning service; timing service functional" | Lok Sabha written reply, MoS Space Jitendra Singh, 29 Jul 2026 (India Today) |
| Only IRNSS-1B, IRNSS-1I and NVS-01 give PNT; at least 4 satellites are needed (lat, long, alt, clock) | Same reply |
| 1 µs clock error ≈ 300 m position error | India Today, 30 Jul 2026 |
| Govt: "no vulnerability", because phones use multiple GNSS systems | Lok Sabha reply |
| Timing is used by power grids, telecom, banking and IST; 30,000+ fishing vessels use NavIC messaging | Gadgets Now, 30 Jul 2026 |
| NVS-02 (GSLV-F15, 29 Jan 2025, ISRO's 100th Sriharikota launch) is stuck in GTO because its oxidiser valves did not open | ISRO via ET / India Today, 3 Feb 2025 |
| US denied GPS data during Kargil 1999; project approved 2006 | Drishti / ThePrint |
| 7 satellites (3 GEO + 4 GSO); coverage India + 1,500 km; design accuracy better than 20 m | ISRO / Drishti |
| NVS-03 on GSLV, target 15–20 Oct 2026 (**reported, not officially announced**) | TOI 21 Sep 2026 |

**NEED FROM USER:** nothing is blocking. Optional: music yes or no? (Default: no music.)

## 3. Scene-by-scene plan
| # | Time | Dur | Purpose | Visual idea | Animation technique | VO summary (1 line) | Audio |
|---|---|---|---|---|---|---|---|
| 1 | 0:00–0:15 | 15s | COLD OPEN hook | India map; the location pin tries to lock, then a stamp: "STANDALONE POSITIONING — NOT AVAILABLE" (Lok Sabha, 29 Jul 2026) | Pin pops with overshoot, then searching rings; stamp slams in with a 200 ms scale-settle | "India ne apna GPS banaya… par aaj woh akela aapki location nahi bata sakta. Sarkar ne khud Parliament mein maana." | VO only |
| 2 | 0:15–0:30 | 15s | PROMISE + presenter | Presenter (intro), with 4 chapter chips beside them | Chips stagger in at 120 ms; line-mask reveal | "Agle 4 minute: kya hai NavIC, kyun bana, kya toota, aage kya." | VO |
| 3 | 0:30–1:10 | 40s | Ch1 · WHY (Kargil) | Horizontal timeline 1999 → 2006 → 2013 → 2023; India + 1,500 km coverage ring | Line draws, dots pop, dates on top, text below; ring expands | US ne Kargil mein GPS data dene se mana kiya, toh 2006 mein apna system approve hua | VO |
| 4 | 1:10–2:00 | 50s | Ch2 · HOW IT WORKS | Trilateration: phone + 4 satellites. Satellite 4 = the CLOCK. Then a counter: 1 µs → 300 m | Signal lines draw (dashoffset); circles intersect; the counter eases to 300 m with a container zoom at the end | 3 satellite = position, 4th = time. Ek micro-second ki galti = 300 metre | VO |
| 5 | 2:00–2:50 | 50s | Ch3 · WHAT BROKE (big interrupt at 2:00) | 7-slot satellite board: slots go dark one by one; "3 of 4 needed" bar; styled ISRO launch clip (NVS-02) → GTO orbit diagram, valve icon ✕ | Wipe transition; slots dim with a stagger; ONE-scale bar; orbit path draws, then stalls | Sirf 1B, 1I aur NVS-01 bache. Chaar chahiye. NVS-02 jo replacement tha, valve nahi khula, orbit mein atak gaya | VO (clip muted) |
| 6 | 2:50–3:25 | 35s | Ch4 · IMPACT | Split screen: WORKS (timing: grid, telecom, bank, IST; fishermen 30,000+ messaging) vs DOESN'T (standalone position) | Divider draws from the top; both sides fill at once; ✓ / ✕ stamps | Timing ab bhi chal raha hai; aapka phone GPS + doosre systems use karta hai, sarkar kehti hai khatra nahi | VO |
| 7 | 3:25–3:50 | 25s | Ch5 · WHAT NEXT + presenter moment | Launch window card "NVS-03 · 15–20 Oct (reported)", then NVS-04/05; the 4th slot lights up again | Card line-reveals; slot relights with follow-through glow | NVS-03 ready hai, October mein launch ki report; 4th satellite aaya toh service wapas | VO |
| 8 | 3:50–4:05 | 15s | OUTRO presenter + payoff | Presenter, then a callback to the opening pin, which now LOCKS | Pin lock with overshoot; CTA ≤10 s | "Aapko kya lagta hai, India ko apne GPS pe kitna depend karna chahiye? Comment kariye." | VO |
| 9 | 4:05–4:12 | 7s | SOURCES | Source list + "dated 2 Oct 2026" | Fade-up stagger | (silent) | – |

**Duration check:** 15+15+40+50+50+35+25+15+7 = **252 s = 4:12 ✓** (under 5:00)
- Pattern interrupts: 0:30 (timeline), 1:10 (diagram), **2:00 (source clip)**, 2:50 (split), 3:25 (presenter). Each gap is ≤60–90 s ✓
- Presenter on screen: about 30–35 s ≈ 13% ✓ (target under 20%)

## 4. Look for this episode (new look)
- **"ORBIT LEDGER":** deep navy-black, a warm saffron accent (focal points only), and a cool cyan secondary for data.
- Fonts: Space Grotesk headlines + Inter body. Slight seeded grain. No HUD, no particle network.

## 5. Next steps after your OK
1. Script (Hinglish, about 600 words).
2. Voiceover (voice-00).
3. Build.
4. Bug check + 20-point quality score.
5. MP4 + SRT + thumbnail + title, description and pinned comment.
