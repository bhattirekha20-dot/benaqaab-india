#!/usr/bin/env python3
"""Apply the Benaqaab OS public-video colour treatment.

This is a local, rights-aware post-processing tool. It does not download video.
The caller must supply a video they are allowed to reuse.

Look: warm high-contrast sepia/orange base + a restrained dark green horizontal
band accent inspired by the user's supplied reference. The original speech,
faces and motion remain unchanged.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import cv2
import numpy as np


def grade(frame: np.ndarray, frame_no: int, band: bool = True) -> np.ndarray:
    # BGR -> luminance, then a warm sepia palette.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY).astype(np.float32) / 255.0
    gray = np.clip((gray - 0.5) * 1.18 + 0.5, 0, 1)
    out = np.empty_like(frame, dtype=np.float32)
    out[:, :, 0] = gray * 58.0       # blue
    out[:, :, 1] = gray * 106.0      # green
    out[:, :, 2] = gray * 182.0      # red / amber
    out = np.clip(out, 0, 255).astype(np.uint8)

    if band:
        h, w = out.shape[:2]
        # Slowly drift the band by a few pixels rather than locking it to a face.
        y = int((0.20 + 0.025 * np.sin(frame_no / 13.0)) * h)
        band_h = max(4, int(0.14 * h))
        overlay = out.copy()
        cv2.rectangle(overlay, (0, y), (w, min(h, y + band_h)), (34, 118, 78), -1)
        out = cv2.addWeighted(overlay, 0.56, out, 0.44, 0)

    # Very light grain keeps flat areas from looking digitally posterised.
    rng = np.random.default_rng(frame_no + 1701)
    noise = rng.normal(0, 1.7, out.shape[:2]).astype(np.float32)
    out = np.clip(out.astype(np.float32) + noise[:, :, None], 0, 255).astype(np.uint8)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument('input', type=Path)
    ap.add_argument('output', type=Path)
    ap.add_argument('--no-green-band', action='store_true')
    ap.add_argument('--max-seconds', type=float, default=0)
    args = ap.parse_args()

    cap = cv2.VideoCapture(str(args.input))
    if not cap.isOpened():
        raise SystemExit(f'Could not open input video: {args.input}')
    fps = cap.get(cv2.CAP_PROP_FPS) or 25.0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    limit = int(args.max_seconds * fps) if args.max_seconds else 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    writer = cv2.VideoWriter(str(args.output), cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))
    if not writer.isOpened():
        raise SystemExit('Could not open output writer; use a supported .mp4 codec/container.')

    n = 0
    while True:
        ok, frame = cap.read()
        if not ok or (limit and n >= limit):
            break
        writer.write(grade(frame, n, band=not args.no_green_band))
        n += 1
    cap.release(); writer.release()
    print(f'graded {n} frames -> {args.output}')


if __name__ == '__main__':
    main()
