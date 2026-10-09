with open('projects/ep18_gaganyaan_2026/comp.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print('Original line count:', len(lines))
motion_idx = -1
for i, l in enumerate(lines):
    if '../../viz/motion.js' in l:
        motion_idx = i
        break

assert motion_idx != -1, 'Could not find motion.js script tag'

# Find formatTime index
format_idx = -1
for i, l in enumerate(lines):
    if 'function formatTime(s)' in l:
        format_idx = i
        break

assert format_idx != -1, 'Could not find function formatTime'

new_lines = []
new_lines.extend(lines[:motion_idx+1])
new_lines.append('<script src="beats.js"></script>\n')
new_lines.append('<script>\n')
new_lines.append("  const canvas = document.getElementById('viewCanvas');\n")
new_lines.append("  const ctx = canvas.getContext('2d');\n")
new_lines.append("  const scrubber = document.getElementById('timeScrubber');\n")
new_lines.append("  const timeDisplay = document.getElementById('timeDisplay');\n")
new_lines.append("  const btnPlayPause = document.getElementById('btnPlayPause');\n")
new_lines.append("  const hudBeatPill = document.getElementById('hudBeatPill');\n")
new_lines.append("  const hudChapter = document.getElementById('hudChapter');\n")
new_lines.append("  const beatName = document.getElementById('beatName');\n")
new_lines.append("  const btnAudioToggle = document.getElementById('btnAudioToggle');\n")
new_lines.append("  const masterAudio = document.getElementById('masterAudio');\n")
new_lines.append("\n")
new_lines.append("  const TOTAL_DURATION = 308.56;\n")
new_lines.append("  let currentTime = 0;\n")
new_lines.append("  let isPlaying = false;\n")
new_lines.append("  let audioMuted = false;\n")
new_lines.append("  let lastTimestamp = 0;\n")
new_lines.append("\n")
new_lines.append("  const logoImg = new Image();\n")
new_lines.append("  logoImg.src = '../../brand/logo.png';\n")
new_lines.append("\n")
new_lines.append("  const BEATS_REGISTRY = window.BEATS_REGISTRY;\n")
new_lines.append("  const beatsData = BEATS_REGISTRY;\n")
new_lines.append("\n")
new_lines.append("  const imageCache = {};\n")
new_lines.append("  BEATS_REGISTRY.forEach(b => {\n")
new_lines.append("    const img = new Image();\n")
new_lines.append("    img.src = b.asset_path;\n")
new_lines.append("    imageCache[b.beat_id] = img;\n")
new_lines.append("    imageCache[b.asset_path] = img;\n")
new_lines.append("  });\n")
new_lines.append("\n")

new_lines.extend(lines[format_idx:])

with open('projects/ep18_gaganyaan_2026/comp.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print('Updated successfully! New line count:', len(new_lines))
