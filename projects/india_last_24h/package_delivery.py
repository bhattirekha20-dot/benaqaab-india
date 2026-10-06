from pathlib import Path
from PIL import Image,ImageOps,ImageDraw,ImageFont
import shutil,json,zipfile
R=Path(__file__).parent;O=R/'delivery'; O.mkdir(exist_ok=True)
F=lambda n:ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',n)
# Designed thumbnail using existing original illustrative artwork; not event footage.
im=ImageOps.fit(Image.open(R/'scene_01_newsroom_hook.jpg').convert('RGB'),(1280,720)).convert('RGBA')
ov=Image.new('RGBA',im.size);d=ImageDraw.Draw(ov)
for x in range(1280):d.line((x,0,x,720),fill=(5,12,27,int(238-155*x/1280)))
im=Image.alpha_composite(im,ov);d=ImageDraw.Draw(im)
logo=Image.open(R/'source_images/benaqaab_os_logo.png').convert('RGBA');logo=ImageOps.contain(logo,(310,95));im.alpha_composite(logo,(55,35))
d.rounded_rectangle((910,46,1220,99),radius=10,fill='#f0ad24');d.text((932,57),'7 OCT 2026',font=F(30),fill='#101a3a')
d.text((55,172),'INDIA',font=F(100),fill='white');d.text((55,280),'24 HOURS',font=F(104),fill='#ffd35b')
d.rectangle((60,410,150,417),fill='#10bfe8');d.text((57,449),'KYA BADLA?',font=F(64),fill='white')
d.text((59,551),'VOTE ROW  /  ₹10,000 CR',font=F(36),fill='#e3faff');d.text((59,604),'QUAKE  /  CRICKET',font=F(36),fill='#e3faff')
d.text((995,679),'AI illustration',font=F(17),fill='white')
im.convert('RGB').save(O/'thumbnail_1280x720.jpg',quality=95)
# Vertical cover for Shorts selection.
v=Image.open(R/'preview_bg_01.jpg').convert('RGBA');ov=Image.new('RGBA',v.size);d=ImageDraw.Draw(ov)
for y in range(750,1920):d.line((0,y,1080,y),fill=(5,12,27,int(230*(y-750)/1170)))
v=Image.alpha_composite(v,ov);d=ImageDraw.Draw(v)
d.text((65,1110),'INDIA',font=F(124),fill='white');d.text((65,1260),'24 HOURS',font=F(128),fill='#ffd35b');d.text((65,1430),'KYA BADLA?',font=F(90),fill='white');d.text((70,1580),'7 OCTOBER 2026',font=F(44),fill='#e3faff');d.text((70,1700),'SHOR NAHI, SOURCE KE SAATH.',font=F(32),fill='white');d.text((70,1830),'AI ILLUSTRATION',font=F(20),fill='white');v.convert('RGB').save(O/'cover_vertical_1080x1920.jpg',quality=94)
title='India News Roundup | 7 Oct 2026: Vote Row, ₹10,000 Cr Fund, Quake & Cricket'
(O/'title.txt').write_text(title+'\n',encoding='utf-8')
desc='''India ke 6–7 October 2026 ke headline updates, Benaqaab India ke saath.

Is roundup mein: Election Commission/SIR dispute, ₹10,000 crore SME Growth Fund, Integrated Transport & Logistics Authority, Air Chief appointment, DRI gold seizure, Chamoli earthquake, IMD weather alerts aur India–West Indies cricket.

Cricket score: West Indies 171; India 172/2 in 14.4 overs. India won by 8 wickets; the target was 172.

Benaqaab India — shor nahi, source ke saath.

EDITORIAL NOTE
This is a dated news snapshot, not a live bulletin or an exhaustive record of every event. The ECI account is attributed to the ECI; the political dispute is not presented as a settled finding. Check current NCS/IMD and local advisories for safety updates.

VISUAL & AUDIO DISCLOSURE
AI-assisted production with synthetic narration, AI illustrations, recreated data cards and attributed source stills/thumbnails. No third-party video clips are included in this version. Illustrative scenes do not depict actual event footage. Credit does not imply endorsement or transfer of copyright.

SOURCE CREDITS
ECI statement / PIB:
https://www.pib.gov.in/PressReleasePage.aspx?PRID=2319864&reg=48&lang=1
SME Growth Fund / PIB:
https://www.pib.gov.in/PressReleasePage.aspx?PRID=2319532&reg=48&lang=1
https://pib.gov.in/FactsheetDetails.aspx?id=151082&NoteId=151082&ModuleId=16&reg=48&lang=1
ITLA / PIB:
https://pib.gov.in/FactsheetDetails.aspx?id=151083&NoteId=151083&ModuleId=16&reg=48&lang=1
Air Chief / Ministry of Defence via PIB:
https://www.pib.gov.in/PressReleasePage.aspx?PRID=2319822&reg=48&lang=1
DRI / Ministry of Finance via PIB:
https://www.pib.gov.in/PressReleasePage.aspx?PRID=2319832&reg=48&lang=1
Earthquake / National Center for Seismology:
https://seismo.gov.in/MIS/riseq/earthquake
Weather / IMD bulletin:
https://mausam.imd.gov.in/backend/assets/aiwfb_pdf/928ed9696f987fb77e4db1621385e7a6.pdf
Cricket score / BCCI:
https://www.bcci.tv/matches/4e0a3e7a-11b5-43d3-a13e-2b16fc516b64/india-vs-west-indies/scorecard
Cricket thumbnail / BCCI highlights (link only, no footage reused):
https://www.bcci.tv/videos/s-ind-vs-wi-2026-1st-t20i-match-highlights-v93ob
Protest still: Congress via The Indian Express; ECI security image via The Indian Express:
https://indianexpress.com/article/india/breaking-news-live-updates-6-october-2026-india-bloc-protest-cjp-sir-gyanesh-kumar-police-murmur-weather-jeffrey-archer-death-delhi-mumbai-10908329/

#IndiaNews #BenaqaabIndia #NewsRoundup #HindiNews #Shorts
'''
(O/'description.txt').write_text(desc,encoding='utf-8')
(O/'hashtags_and_tags.txt').write_text('HASHTAGS\n#IndiaNews #BenaqaabIndia #NewsRoundup #HindiNews #Shorts\n\nTAGS\nIndia news, 7 October 2026, Benaqaab India, Benaqaab OS, Hindi news roundup, Hinglish news, Election Commission, SME Growth Fund, ITLA, Air Chief, DRI, Chamoli earthquake, IMD weather, India West Indies\n',encoding='utf-8')
report='''# Production handoff and corrections report

## Final instruction and scope
You authorised final rendering and asked to forget the third-party videos. This export therefore uses the enlarged still-image/data-card edit with animated text and existing narration. It is not a footage-based edit. No video has been posted to any platform.

## What went wrong — and responsibility
I should have checked the actual rendered output and narration timing earlier, and kept source discovery separate from successful video insertion. I also repeated permission/file questions after you had confirmed permission. That created unnecessary friction; I’m sorry.

| Issue | What caused it / what was known | Final action |
|---|---|---|
| Scene counters visible | Debug numbering was baked into earlier frames | No debug counters in final image assets or export |
| Earthquake showed unrelated DRI material | User reported a mismatch; old composite reuse and transition bleed were risks, not independently proven causes | Earthquake uses its own NCS card/background; hard scene cuts prevent cross-story bleed |
| Images too small; excessive blue space | Fixed small image boxes and oversized lower panels | Source images fitted uncropped into a 1040 × 1200 area; image-derived backgrounds and lower gradients replace flat blue blocks |
| Duplicate/oversized copy | Baked captions plus separate HTML overlays could duplicate text | Clean backgrounds and one animated headline layer; compact text below source images |
| Rejected source pill | Earlier compositor added OFFICIAL SOURCE IMAGE | Not used in final export; actual source credits retained |
| Narration/visual drift | Character-length timing estimates, not audio timestamps | Existing audio transcribed for timing; scene boundaries revised by topic |
| Closing scene effectively absent | Last preview start fraction was 1.0 | Closing now starts during the actual closing narration and remains through the ending |
| Cricket target misstated | Script said 171 was the target, although WI scored 171 and India reached 172/2 | Removed “171 ka target” from the existing narration; final graphic states target 172 |
| Video links mistaken for usable assets | Source pages were found, but access/retrieval and visual verification were incomplete | No claim that video clips were inserted; omitted as requested |
| Repeated permission questions | Workflow confused permission confirmation with file access | Your confirmation is logged; retrieval failures are a separate technical issue |
| “Cannot appear” claims too strong | Earlier response overstated checking | Final deliverable uses explicit per-scene assets, with checks documented rather than absolute guarantees |

## Video-source attempts, for the record
NDTV returned HTTP 403. ANI embedded YouTube and the Republic World upload required sign-in/bot verification. BCCI’s public page exposed a player playlist, but the extraction attempt failed. No restrictions were bypassed. No footage was downloaded successfully. Your confirmation of reuse permission for all four was recorded, but no independent licences were obtained. Sepia/orange and dark-green video grading is consequently not represented as completed work: there are no third-party clips in this version.

## Deliverables
- Benaqaab_India_07_Oct_2026.mp4 — vertical 1080 × 1920, 24 fps, H.264/AAC.
- thumbnail_1280x720.jpg — landscape upload thumbnail.
- cover_vertical_1080x1920.jpg — vertical cover artwork.
- title.txt; description.txt; hashtags_and_tags.txt — upload copy.
- narration_final.wav — original selected voice, combined with the cricket phrase edit.
- headline_captions.srt — timed headline summaries, NOT verbatim closed captions.
- scene_timing.json — final scene timings.
- source and correction documentation; reproducible project files in the full ZIP.

## Remaining limitations / publishing checks
- This is a 6–7 October 2026 edition. Do not relabel it as current news on another date.
- Research was inherited from the saved source ledger; this render pass is not a fresh independent verification of every story or an exact rolling-24-hour audit.
- Automatic speech recognition was used for timing, not factual verification. It can misrecognise Hinglish. No full human listening review was performed.
- Source stills and thumbnails remain copyrighted unless their terms say otherwise. Attribution is not a blanket licence. Source documentation is not legal clearance.
- AI maps/backgrounds are illustrative, not authoritative geographic or hazard maps.
- No music, third-party video, or fabricated politician faces were added.
- Platform upload interfaces vary; a separate JPG is supplied, but automatic custom-thumbnail support for Shorts is not guaranteed.
- Existing low-resolution source stills may look soft when enlarged. No invented detail was added to them.

## Before upload
1. Watch the MP4 once end to end, especially the edited cricket sentence and the closing line.
2. Confirm still-image reuse terms and source attribution for your publication.
3. Paste the supplied dated title and description; keep the AI/synthetic narration disclosure.
4. Use the platform’s applicable altered/synthetic-content disclosure controls.
5. Keep safety information dated and refer viewers to current local advisories.
'''
(O/'HANDOFF_AND_CORRECTIONS.md').write_text(report,encoding='utf-8')
for name in ['SOURCES.md','PUBLIC_ASSET_MANIFEST.md','PUBLIC_VIDEO_AUDIT.md','CORRECTIONS_LOG.md','RESEARCH_FACT_LEDGER.md','SCRIPT_STORYBOARD.md']:
 shutil.copy2(R/name,O/name)
print('Upload copy, thumbnails and handoff report created')
