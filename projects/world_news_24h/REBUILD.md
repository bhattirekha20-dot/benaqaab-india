# Rebuild this preview

Install Python packages Pillow, NumPy, requests, imageio-ffmpeg and Playwright. The assets, narration and measured timing files are already saved.

From this project directory run, in order:
1. python build_photo_preview.py
2. python apply_repo_style.py
3. python finish_preview.py
4. python improve_motion.py

Optional browser checks: install Playwright Chromium and dependencies, then python qa_preview.py. The structural check is in repo_reference/tools/peak_detail_gate.py; use PLAN.json with this project as root.

Do not rerun the narration-generation tool for a visual-only revision. Do not execute unrelated repository setup or app code. Final MP4 generation remains approval-gated.

Final colour revision: run python cool_colour_pass.py after improve_motion.py. This is the latest user-requested look.
