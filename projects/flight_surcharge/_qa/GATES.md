# GATES.md — final verified numbers on the delivered file

File: `projects/flight_surcharge/Flight_Surcharge_Short.mp4` (H.264 CRF 18 + AAC 192 kbps)

| Gate | Target | Measured | Verdict |
|---|---|---|---|
| Container | 1080×1920 · 30 fps · yuv420p · AAC 48 kHz | h264 1080x1920 yuv420p 30/1 · aac 48000 Hz 2ch | PASS |
| Frame count | whole frames for 176.166667 s | 5285 (176.167 s) | PASS |
| Structural PLAN gate | `tools/peak_detail_gate.py` | `structural_pass: true`, 0 errors | PASS |
| Freezes | none | `[]` | PASS |
| Pops | none | `[]` | PASS |
| Still ratio | ≈ 0 | `0.0` | PASS |
| Determinism (pre-render) | same t → same pixels | `[ok] determinism check passed` | PASS |
| Decode | no errors on full decode | `none` | PASS |
| Integrated loudness | −14 LUFS for Shorts | **−14.0 LUFS** | PASS |
| Loudness range | narration mix | **2.4 LU** | PASS |
| True peak | ≤ −1.5 dBFS | **−1.6 dBFS** (measured on the muxed file) | PASS |
| Still vs render | informational | mean abs diff 2.76 / 2.06 / 1.99 at 5 s / 66 s / 145 s (motion blur in the render) | — |

**Audio re-mux note:** the first mux measured −1.1 dBFS true peak (AAC overshoot). The master was
re-run with `loudnorm … TP=-2.0:linear=true` and the file remuxed with `-c:v copy`; the video
stream MD5 is identical before and after (`f71dab0d6daf314c7437e81cb2261434`), so no pixel changed.

Full machine-readable report: `_qa/QC_render.json` · PLAN gate: `_qa/PLAN_GATE.json` ·
render log: `_qa/render_v1.log` (2931 s, 11742 captures, 3003 blurred frames).
