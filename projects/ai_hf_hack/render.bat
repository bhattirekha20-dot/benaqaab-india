@echo off
REM render.sh — Windows version: frames -> FINAL.mp4 (with VO audio)
REM Needs: python3 (python.org), playwright (pip install playwright && playwright install chromium), ffmpeg (in PATH)
cd /d "%~dp0"

echo [1/3] rendering frames (resumable — re-run if interrupted)...
python render.py frames
if errorlevel 1 goto :err

echo [2/3] building master audio...
call make_audio.bat

echo [3/3] encoding FINAL.mp4 (1080p30 + VO)...
ffmpeg -y -framerate 30 -i frames\f_%%06d.png -i audio_master.mp3 -map 0:v -map 1:a -c:v libx264 -preset medium -crf 18 -pix_fmt yuv420p -c:a aac -b:a 192k -movflags +faststart -shortest "AI_hacked_HuggingFace_FINAL.mp4"
if errorlevel 1 goto :err

echo ==================================================
dir AI_hacked_HuggingFace_FINAL.mp4
echo DONE — upload-ready file: AI_hacked_HuggingFace_FINAL.mp4
goto :eof
:err
echo.
echo ERROR — check the messages above (missing python/ffmpeg/playwright?)
pause
