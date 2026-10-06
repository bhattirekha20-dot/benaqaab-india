#!/usr/bin/env bash
# Benaqaab toolchain — restores everything in a fresh sandbox.
# Installs do NOT persist between chats (only /home/user files do): run at the start of every chat.
#   bash /home/user/setup.sh        (safe to re-run; skips what is already there)
set -u
H=/home/user
log(){ echo "[setup] $*"; }

# 1) system: ffmpeg + Chromium (needs sudo — present in the 2026-09-30 sandbox)
if ! command -v ffmpeg >/dev/null || [ ! -x /usr/lib/chromium/chromium-headless-shell ]; then
  if sudo -n true 2>/dev/null; then
    log "apt: ffmpeg chromium-headless-shell chromium fonts-noto-core (2-4 min)"
    sudo apt-get update -qq && sudo DEBIAN_FRONTEND=noninteractive apt-get install -y -qq \
      --no-install-recommends ffmpeg chromium-headless-shell chromium fonts-noto-core >/dev/null 2>&1 \
      || log "apt FAILED"
  else
    log "no sudo -> Pillow-only fallback (imageio-ffmpeg). HTML renderer unavailable this chat."
  fi
fi

# 2) python packages (pip is not persistent either)
pip install -q numpy pillow mutagen imageio-ffmpeg playwright pyyaml faster-whisper >/dev/null 2>&1 || log "pip FAILED"

# 3) fonts (brand/fonts) + channel logo (from MEMORY §47 if missing)
[ -x $H/viz/get_fonts.sh ] && bash $H/viz/get_fonts.sh
if [ ! -s $H/brand/logo.png ] && [ -f $H/MEMORY.md ]; then
python3 - <<'EOF'
import base64, re, os
md = open('/home/user/MEMORY.md', encoding='utf-8').read()
m = re.search(r'<<<LOGO_B64\n(.*?)\nLOGO_B64>>>', md, re.S)
if m:
    os.makedirs('/home/user/brand', exist_ok=True)
    open('/home/user/brand/logo.png', 'wb').write(base64.b64decode(''.join(m.group(1).split())))
    print('[setup] logo restored from MEMORY §47')
EOF
fi

# 4) report
command -v ffmpeg >/dev/null && log "$(ffmpeg -version | head -1 | cut -c1-32)"
[ -x /usr/lib/chromium/chromium-headless-shell ] && log "$(/usr/lib/chromium/chromium-headless-shell --version 2>/dev/null)"
python3 -c "import numpy, PIL, mutagen, playwright; print('[setup] python OK')" 2>/dev/null || log "python deps missing"
log "fonts: $(ls $H/brand/fonts/*.ttf 2>/dev/null | wc -l) · logo: $([ -s $H/brand/logo.png ] && echo ok || echo MISSING)"
log "renderer: python3 viz/hrender.py comp.html out.mp4 --audio vo.wav --check   (run via start_process)"
log OK
