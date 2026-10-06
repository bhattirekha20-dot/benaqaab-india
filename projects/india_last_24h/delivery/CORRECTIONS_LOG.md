# Corrections Log — India Last 24 Hours Short

This file records user corrections, the issue found, the fix applied and what future AI work must avoid.

## 1. Duplicate / overwritten text in preview

- **User correction:** The opening text was appearing twice and covering other text.
- **Cause:** Text was already baked into the pre-rendered frame, while the HTML preview added a second HTML text overlay.
- **Fix:** Removed the HTML overlay from the preview and made the self-contained frames the single source of visible text.
- **Do not repeat:** Never overlay HTML text on a frame that already contains the same text. Render text exactly once.

## 2. Too few public/source visuals

- **User correction:** Do not use public/source media only for Rahul Gandhi. Use public images, videos, articles, official data and other available source material for every topic wherever possible.
- **Fix:** Added multiple public or official assets across the complete roundup:
  - two ECI/protest images;
  - two official PIB SME graphics;
  - official PIB ITLA graphic;
  - official PIB Air Chief portrait;
  - two official DRI images;
  - NCS and IMD public-data cards;
  - official BCCI match thumbnail, scorecard data and official highlights link.
- **Do not repeat:** Before presenting a preview, check every story for an official image, public source image, public data card, official video thumbnail or source article card. Use AI only when a suitable public asset is not available or for explanatory background motion.

## 3. Visuals not tightly synced to narration

- **User correction:** Images must match the detail being spoken at that moment.
- **Fix:** Split the roundup into 14 shorter scenes. Scene timing is calculated from narration paragraph/sentence character weights, so democracy, economy, defence, gold, earthquake, weather, cricket and closing each have their own aligned visual markers.
- **Do not repeat:** Do not use broad arbitrary time fractions for a multi-topic voiceover. Build a sync map from the narration text before making the preview or final render.

## 4. Details hidden by image/data panels

- **User correction:** Important detail must not be hidden in the video.
- **Fix:** Reduced oversized source cards, moved source cards above the bottom text panel, separated earthquake and weather cards, and kept captions/source labels inside safe margins.
- **Do not repeat:** Check every 1080×1920 frame at small mobile size. Source image captions, source labels, headlines and subtitles must remain readable and must not be covered by another panel.

## 5. User's permanent Benaqaab OS logo

- **User correction:** Always use the supplied Benaqaab OS logo in the video and future work.
- **Fix:** Saved the original image at `/home/user/brand_assets/benaqaab_os_logo.png` and the project copy at `/home/user/india_last_24h_short/source_images/benaqaab_os_logo.png`; updated the frame builder to place the logo in the top-left safe area of all 14 scenes; created `BRAND_USAGE.md` and updated the permanent AI rulebook.
- **Do not repeat:** Never replace the logo with typed channel text, crop it, recolour it or omit it from a video/preview unless the user explicitly requests a different brand treatment.

## 6. Source labels, oversized text and missing image presentation

- **User correction:** Do not show the `OFFICIAL SOURCE IMAGE` label in the video. Reduce text size, animate text graphically over the images, and make sure every selected image actually appears in the video.
- **Cause:** Text was baked statically into the full frame, the source-label pill added clutter, and the preview was displaying pre-rendered composites instead of clean image backgrounds with animated text.
- **Fix:** Created clean `preview_bg_01.jpg` through `preview_bg_14.jpg` backgrounds, removed the source-label pills from the preview layer, reduced HTML headline/subtitle/source sizes, and restored the text as one animated HTML layer that enters with each scene. All 14 selected public/official/AI visuals now have their own scene and are included in the preview timeline.
- **Do not repeat:** Never show a source-label pill the user has rejected. Never bake duplicate headline text into a frame and then overlay it again. Always verify that every chosen visual has a corresponding scene and that the scene text is animated without hiding image or source detail.

## 7. User's public-video colour treatment and sourcing request

- **User correction/request:** When a public video is used, apply the user's reference colour treatment: warm sepia/orange with a dark green horizontal band. Find public videos of Rahul Gandhi and, where available, the other covered stories and add them to the video.
- **Fix:** Added `PUBLIC_VIDEO_AUDIT.md` with Rahul Gandhi/ECI, SME, ITLA, Air Chief, DRI, earthquake, weather and BCCI video candidates. Added `apply_public_video_grade.py`, which processes only user-supplied or permission-cleared clips and applies the requested treatment. Kept the current preview rights-safe: it uses official stills, data cards, thumbnails and source links rather than silently downloading third-party footage.
- **Do not repeat:** Never treat a public URL as automatic reuse permission. Never use an unrelated clip to represent a current event. Before insertion, verify source, date, topic match, rights and attribution; then apply the Benaqaab OS grade and retain source credit.

## 8. Scene counters, wrong earthquake visual and text/image overlap

- **User correction:** Remove visible scene counters such as `02 / 14`, ensure the earthquake alert never shows an unrelated DRI image, and do not let animated text hide half of a visual.
- **Cause:** Scene numbers were baked into the frame header as debug metadata. The preview backgrounds were generated from text-composited frames, so a stale/wrong visual could persist and full-frame AI artwork was covered by an opaque lower panel.
- **Fix:** Removed scene counters from the frame builder, rebuilt all 14 clean scene backgrounds directly from their assigned assets, rebuilt the NCS earthquake scene with only its labelled NCS data card and earthquake map, and changed full-frame AI backgrounds to a readable gradient so the image remains visible underneath the animated copy.
- **Do not repeat:** Never show debug scene numbers in the final video. Never allow a source image from one story to appear under another story's narration. Never cover the lower half of a visual with an opaque text panel; use safe placement or a transparent gradient.

## 9. User-provided Rahul Gandhi video source

- **User instruction:** Use the supplied Instagram Reel as the Rahul Gandhi public-video source.
- **Status:** Added the Reel URL to `PUBLIC_VIDEO_AUDIT.md` and `SOURCES.md`. Instagram returned HTTP 403 in the workspace, so no video file was retrieved or inserted. The source account, content and reuse permission could not be independently verified.
- **Next action:** Use the clip only after an accessible file is supplied and the user confirms they own/have permission to reuse it. Then apply the requested warm sepia/orange and dark-green band treatment, retain attribution, and sync the clip to the ECI narration.
- **Do not repeat:** Never claim that a linked social video has been added when only the URL is available. Never download or reuse a public Reel without a rights basis.

## 10. Durable instruction for future AI

- Every time the user corrects the work, append a dated entry here with: correction, cause, fix and do-not-repeat rule.
- Also update `AI_SHORTS_RULEBOOK.md` and `MEMORY.md` when the correction is a durable workflow rule.

## Larger images / less blue space
- Enlarged source-image area to 1040 × 1200; preserved complete images without cropping.
- Replaced flat blue lower blocks with image-derived blurred backdrops and a lower gradient.
- Moved animated copy to a compact lower area and retained source attribution and logo.
- Regenerated all backgrounds and comp.html; visually inspected enlarged DRI background.
- Removed crossfade opacity to prevent prior-story imagery bleeding into a new story.
- Final export remains approval-gated.

## Final export authorised and delivered
User instructed to forget third-party videos and render the full package. Created 1080x1920 / 24 fps H.264-AAC MP4, 118.07 seconds, with revised narration-topic timings, animated text, original logo, enlarged source stills and NCS-only earthquake scene. Removed incorrect spoken “171 ka target”; graphics show target 172. Fixed zero-duration closing scene. Full decode test passed; sampled earthquake/closing frames inspected. Thumbnails, upload copy, headline-summary SRT, sources and handoff report included. No third-party footage inserted.
