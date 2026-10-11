import numpy as np
import scipy.signal as signal
from scipy.io import wavfile
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DIR = Path(__file__).parent
OUTPUT_WAV = DIR / "ambient_documentary_bed.wav"

sr = 44100
duration = 609.0  # seconds
num_samples = int(sr * duration)
t = np.linspace(0, duration, num_samples, endpoint=False)

print(f"🎵 Synthesizing Dynamic 7-Movement Investigative Score (609s) at {sr}Hz...")

# --- CHAPTER MARKERS (from BEAT_SHEET.json) ---
CH1_END = 83.45   # The Global Celebration vs Street Reality
CH2_END = 173.16  # The Per-Capita Illusion (Rank #136)
CH3_END = 276.75  # The K-Shaped Economy (Divergence)
CH4_END = 356.11  # Household Balance Sheet Crisis (5.3% Savings, 45.8% Debt)
CH5_END = 442.72  # The Missing Factory (Industrial Pulse)
CH6_END = 525.70  # The 2045 Demographic Clock (Urgent Ticking)
CH7_END = 609.00  # The Road Ahead & Climax Verdict

# Helper for smooth windowing between chapters
def smooth_gate(t, start, end, ramp=3.0):
    enter = np.clip((t - start) / ramp, 0, 1)
    exit = np.clip((end - t) / ramp, 0, 1)
    return enter * exit

# --- BASE FREQUENCIES (D Minor Modal Palette) ---
f_d1 = 36.71
f_d2 = 73.42
f_a2 = 110.00
f_bb2 = 116.54
f_c3 = 130.81
f_d3 = 146.83
f_f3 = 174.61
f_g3 = 196.00
f_a3 = 220.00

# 1. CORE SUB-DRONE (Warm organic foundation, D1/D2)
lfo_sub = 0.5 + 0.5 * np.sin(2 * np.pi * 0.05 * t)
sub_drone = (0.35 * np.sin(2 * np.pi * f_d1 * t) + 0.25 * np.sin(2 * np.pi * f_d2 * t)) * (0.8 + 0.2 * lfo_sub)

# 2. DYNAMIC CHAPTER-AWARE PAD HARMONIES
# Phase 1: Dm (D3, F3, A2) - Investigating the headline euphoria
p1_gate = smooth_gate(t, 0.0, CH1_END, ramp=3.0)
pad1 = (np.sin(2 * np.pi * f_d3 * t) * 0.35 +
        np.sin(2 * np.pi * f_f3 * t) * 0.28 +
        np.sin(2 * np.pi * f_a2 * t) * 0.30) * p1_gate

# Phase 2: Dm -> Bb progression cycling every 16s - Inquisitive investigative contrast
p2_gate = smooth_gate(t, CH1_END, CH2_END, ramp=4.0)
cycle_16 = np.sin(2 * np.pi * (1.0 / 16.0) * t)
bb_weight = 0.5 + 0.5 * cycle_16
pad2_dm = np.sin(2 * np.pi * f_d3 * t) * 0.35 + np.sin(2 * np.pi * f_f3 * t) * 0.28 + np.sin(2 * np.pi * f_a2 * t) * 0.30
pad2_bb = np.sin(2 * np.pi * f_bb2 * t) * 0.35 + np.sin(2 * np.pi * f_d3 * t) * 0.30 + np.sin(2 * np.pi * f_f3 * t) * 0.25
pad2 = (pad2_dm * (1 - bb_weight * 0.6) + pad2_bb * (bb_weight * 0.6)) * p2_gate

# Phase 3: K-Shaped Divergence (Dm with upper harmonic shimmer & low tension)
p3_gate = smooth_gate(t, CH2_END, CH3_END, ramp=4.0)
pad3 = (np.sin(2 * np.pi * f_d3 * t) * 0.30 +
        np.sin(2 * np.pi * f_f3 * t) * 0.25 +
        np.sin(2 * np.pi * f_g3 * t) * 0.20 +
        np.sin(2 * np.pi * f_a3 * t) * 0.25) * p3_gate

# Phase 4: Household Debt Gravity (Dm suspended, deep slow swelling tension)
p4_gate = smooth_gate(t, CH3_END, CH4_END, ramp=4.0)
lfo_debt = 0.5 + 0.5 * np.sin(2 * np.pi * 0.03 * t)
pad4 = (np.sin(2 * np.pi * f_d2 * t) * 0.40 +
        np.sin(2 * np.pi * f_bb2 * t) * 0.35 +
        np.sin(2 * np.pi * f_d3 * t) * 0.30) * (0.7 + 0.3 * lfo_debt) * p4_gate

# Phase 5: The Missing Factory (Industrial rhythmic pad, Dm with 5th reinforcement)
p5_gate = smooth_gate(t, CH4_END, CH5_END, ramp=4.0)
pad5 = (np.sin(2 * np.pi * f_d2 * t) * 0.35 +
        np.sin(2 * np.pi * f_a2 * t) * 0.35 +
        np.sin(2 * np.pi * f_d3 * t) * 0.30) * p5_gate

# Phase 6: The 2045 Demographic Clock (Urgent rising modal chords Dm -> Gm -> A)
p6_gate = smooth_gate(t, CH5_END, CH6_END, ramp=4.0)
lfo_clock_ramp = np.clip((t - CH5_END) / (CH6_END - CH5_END), 0, 1)
pad6 = (np.sin(2 * np.pi * f_d3 * t) * 0.30 +
        np.sin(2 * np.pi * f_g3 * t) * (0.25 + 0.15 * lfo_clock_ramp) +
        np.sin(2 * np.pi * f_a3 * t) * (0.25 + 0.20 * lfo_clock_ramp)) * p6_gate

# Phase 7: The Road Ahead & Climax (Resolute Dm -> F major resolution)
p7_gate = smooth_gate(t, CH6_END, CH7_END, ramp=4.0)
pad7 = (np.sin(2 * np.pi * f_d3 * t) * 0.35 +
        np.sin(2 * np.pi * f_f3 * t) * 0.35 +
        np.sin(2 * np.pi * f_a3 * t) * 0.30) * p7_gate

# Combined multi-movement harmonic pad
pads_all = pad1 + pad2 + pad3 + pad4 + pad5 + pad6 + pad7

# 3. DYNAMIC RHYTHMIC LAYERS (CAUSALLY SHIFTING WITH CHAPTERS)
# Layer A: 60 BPM Heartbeat Clock (Chapters 1, 2, 4, 7)
pulse_60_env = np.maximum(0, np.sin(2 * np.pi * 1.0 * t)) ** 12
pulse_60 = np.sin(2 * np.pi * 80.0 * t) * pulse_60_env * 0.16 * (p1_gate + p2_gate + p4_gate + p7_gate)

# Layer B: Industrial Mechanical Syncopated Movement (Chapter 5: Missing Factory)
# 90 BPM (1.5 Hz) mechanical tick
pulse_factory_env = np.maximum(0, np.sin(2 * np.pi * 1.5 * t)) ** 14
pulse_factory = (np.sin(2 * np.pi * 120.0 * t) * 0.18 + np.sin(2 * np.pi * 240.0 * t) * 0.08) * pulse_factory_env * p5_gate

# Layer C: The 2045 Demographic Clock Tick-Tock (Chapter 6)
# Crisp analog 1.0 Hz clock tick with acoustic ping
pulse_tick_env = np.maximum(0, np.sin(2 * np.pi * 1.0 * t)) ** 24
pulse_tick = (np.sin(2 * np.pi * 440.0 * t) * 0.14 + np.sin(2 * np.pi * 880.0 * t) * 0.06) * pulse_tick_env * p6_gate

# Layer D: Rhythmic Shimmer in Luxury K-Shape (Chapter 3)
shimmer_env = np.maximum(0, np.sin(2 * np.pi * 2.0 * t)) ** 8
shimmer = np.sin(2 * np.pi * 587.33 * t) * shimmer_env * 0.08 * p3_gate  # D5 high shimmer

# 4. CLIMACTIC TENSION RISER (597.5s to 601.0s) & FINAL VERDICT BOOM (601.0s to 608.35s)
riser_env = np.clip((t - 597.5) / 3.5, 0, 1) ** 2 * np.clip((601.2 - t) / 0.2, 0, 1)
riser_freq = 110.0 + (t - 597.5) * 120.0  # Pitch bends smoothly upwards from 110 Hz to 530 Hz!
riser_synth = np.sin(2 * np.pi * riser_freq * t) * riser_env * 0.25

# Post-verdict deep sub-boom decay (601.0s to 608.35s)
boom_t = np.maximum(0, t - 601.0)
boom_env = np.exp(-boom_t / 2.2) * (t >= 601.0)
sub_boom = (np.sin(2 * np.pi * 42.0 * t) * 0.40 + np.sin(2 * np.pi * 65.0 * t) * 0.25) * boom_env

# 5. MASTER MIXDOWN & EQUALIZATION
raw_mix = (sub_drone * 0.45 +
           pads_all * 0.40 +
           pulse_60 +
           pulse_factory +
           pulse_tick +
           shimmer +
           riser_synth +
           sub_boom)

# Analog Soft Saturation (warm tape distortion to round harsh peaks)
saturated = np.tanh(raw_mix * 1.35) / 1.35

# Butterworth Low-pass Filter at 920 Hz (4th order)
# Strictly clears the 1 kHz - 4 kHz vocal clarity band for Hindi diction!
sos = signal.butter(4, 920, 'lp', fs=sr, output='sos')
filtered = signal.sosfilt(sos, saturated)

# Smooth master fade-in (0.0s to 3.5s) and fade-out (605.0s to 609.0s)
fade_in = np.clip(t / 3.5, 0, 1)
fade_out = np.clip((duration - t) / 3.8, 0, 1)
final_audio = filtered * fade_in * fade_out

# Peak normalize to -16 dBFS to leave headroom for voiceover & SFX
peak = np.max(np.abs(final_audio))
if peak > 0:
    final_audio = (final_audio / peak) * 0.16

# Convert to 16-bit PCM WAV
audio_int16 = (final_audio * 32767).astype(np.int16)
wavfile.write(str(OUTPUT_WAV), sr, audio_int16)

print(f"✅ Master Cinematic Soundtrack Rendered: {OUTPUT_WAV} ({OUTPUT_WAV.stat().st_size / 1024 / 1024:.2f} MB)")
