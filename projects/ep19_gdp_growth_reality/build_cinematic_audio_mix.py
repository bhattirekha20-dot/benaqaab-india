import sys
import subprocess
from pathlib import Path
from pydub import AudioSegment

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

DIR = Path(__file__).parent
SFX_DIR = Path(r"c:\Users\dell\Desktop\my ai bot skills ok\.agents\skills\hyperframes-media\assets\sfx")

VO_RAW = DIR / "narration_raw.mp3"
BGM_WAV = DIR / "ambient_documentary_bed.wav"
SFX_TRACK_WAV = DIR / "sfx_track.wav"
MASTER_MP3 = DIR / "master_audio.mp3"

print("🎙️ Assembling Bespoke Cinematic Foley & Sound Design Track (Causal SFX Lockstep)...")

# Load Voiceover to get exact duration
vo = AudioSegment.from_file(VO_RAW)
total_ms = len(vo)
print(f"Total voiceover duration: {total_ms / 1000.0:.2f} seconds ({total_ms} ms)")

# Create silent base track for SFX
sfx_track = AudioSegment.silent(duration=total_ms + 1500)

def load_sfx(name, gain_db=0):
    p = SFX_DIR / name
    if not p.exists():
        print(f"Warning: SFX file not found: {p}")
        return AudioSegment.silent(duration=100)
    seg = AudioSegment.from_file(p)
    return seg + gain_db

# Load SFX assets with calibrated gain
whoosh_cine = load_sfx("whoosh-cinematic.mp3", gain_db=-7)
whoosh_short = load_sfx("whoosh-short.mp3", gain_db=-5)
click_sfx = load_sfx("click.mp3", gain_db=-5)
click_soft = load_sfx("click-soft.mp3", gain_db=-5)
chime_sfx = load_sfx("chime.mp3", gain_db=-6)
pop_sfx = load_sfx("pop.mp3", gain_db=-4)
riser_sfx = load_sfx("riser.mp3", gain_db=-6)
impact_bass = load_sfx("impact-bass-1.mp3", gain_db=-2)
impact_subtle = load_sfx("impact-bass-2.mp3", gain_db=-6)

# Place SFX at exact editing cutpoints & visual graphics timestamps
cues = [
    # Chapter 1: The Global Celebration vs Street Reality (0.0s - 83.45s)
    (500, whoosh_cine, "0.5s: 5-Second Roadmap Card Hook"),
    (8270, whoosh_short, "8.3s: Middle-Class Kitchen Ledger & Inflation Squeeze"),
    (16070, impact_subtle, "16.1s: 80 Crore Citizens on Free Foodgrains Queue"),
    (19990, whoosh_cine, "20.0s: Indian Parliament & $3.94 Trillion Headline"),
    (60100, click_sfx, "60.1s: Channel CTA Like Button Click"),
    (61300, chime_sfx, "61.3s: Channel CTA Subscribed Bell Chime"),
    (64300, whoosh_short, "64.3s: MoSPI Official Gazette Document Slide"),
    (67000, whoosh_short, "67.0s: MoSPI 7.8% Yellow Highlighter Sweep"),
    (67500, click_soft, "67.5s: 7.8% GDP Odometer Spin Start"),
    (71000, whoosh_short, "71.0s: MoSPI 8.2% GVA Highlighter Sweep"),

    # Chapter 2: The Per-Capita Illusion (83.45s - 173.16s)
    (83450, whoosh_cine, "83.5s: Chapter 2 Transition - The Per-Capita Illusion"),
    (121450, whoosh_short, "121.5s: World Bank Ranking Document Slide"),
    (126000, pop_sfx, "126.0s: World Bank 2.2x Loupe Zoom Snap (Rank #136)"),
    (148500, whoosh_short, "148.5s: Global Superpowers Comparison Chart (US $85k, China $13.5k)"),

    # Chapter 3: The K-Shaped Economy (173.16s - 276.75s)
    (173160, whoosh_cine, "173.2s: Chapter 3 Transition - The K-Shaped Economy"),
    (186200, click_sfx, "186.2s: Top 10% Wealth Divergence & Demat Surge"),
    (224600, whoosh_short, "224.6s: SIAM Official Automobile Flash Report Document Slide"),
    (227000, whoosh_short, "227.0s: SIAM Luxury Boom +24.5% Green Highlighter"),
    (227500, click_soft, "227.5s: Luxury Boom Odometer Spin Start"),
    (242100, impact_subtle, "242.1s: Entry-Level Auto Sales Crash -42% Shockwave"),

    # Chapter 4: The Household Balance Sheet Crisis (276.75s - 356.11s)
    (276750, whoosh_cine, "276.8s: Chapter 4 Transition - Household Balance Sheet Crisis"),
    (282400, whoosh_short, "282.4s: RBI Financial Stability Report Document Slide"),
    (287000, whoosh_short, "287.0s: RBI 5.3% Savings Collapse Crimson Highlighter"),
    (287500, click_soft, "287.5s: Net Savings Odometer Spin Start"),
    (318600, whoosh_short, "318.6s: RBI 45.8% Record Debt Document Slide"),
    (321000, whoosh_short, "321.0s: RBI 45.8% Debt Spike Crimson Highlighter"),
    (321500, click_soft, "321.5s: Household Debt Odometer Spin Start"),
    (336000, click_sfx, "336.0s: Unsecured Loan & Credit Card Swipe"),

    # Chapter 5: The Missing Factory (356.11s - 442.72s)
    (356110, whoosh_cine, "356.1s: Chapter 5 Transition - The Missing Factory"),
    (376100, whoosh_short, "376.1s: Mass Manufacturing Assembly Line Contrast"),
    (431200, whoosh_short, "431.2s: Manufacturing 15.8% Share Report Document Slide"),
    (434000, whoosh_short, "434.0s: Manufacturing 15.8% Share Indigo Highlighter"),
    (434500, click_soft, "434.5s: Manufacturing Odometer Spin Start"),

    # Chapter 6: The 2045 Demographic Clock (442.72s - 525.70s)
    (442720, whoosh_cine, "442.7s: Chapter 6 Transition - The 2045 Demographic Clock"),
    (469800, click_soft, "469.8s: 1.1 Crore Youth Annual Influx Metric"),
    (484800, whoosh_short, "484.8s: Demographic Window Countdown Report Document Slide"),
    (488000, whoosh_short, "488.0s: 2045 Demographic Window Deadline Amber Highlighter"),

    # Chapter 7: The Road Ahead & Citizen Verdict (525.70s - 608.35s)
    (525700, whoosh_cine, "525.7s: Chapter 7 Transition - The Road Ahead"),
    (536000, chime_sfx, "536.0s: Solution Pillar 1 - Labor-Intensive Manufacturing"),
    (548000, chime_sfx, "548.0s: Solution Pillar 2 - Middle-Class Tax Relief"),
    (560000, chime_sfx, "560.0s: Solution Pillar 3 - Agro Cold-Chain & Food Processing"),
    (572000, chime_sfx, "572.0s: Solution Pillar 4 - Direct Industrial Vocational Skill"),
    (597500, riser_sfx[-3500:], "597.5s: Climactic Tension Riser Build-up (3.5s)"),
    (601000, impact_bass, "601.0s: FINAL FORENSIC VERDICT STAMP SLAM (Camera Trauma Shake Impact)"),
]

for ms, sound, desc in cues:
    print(f" 🔊 Placing SFX [{ms/1000.0:6.1f}s]: {desc}")
    sfx_track = sfx_track.overlay(sound, position=ms)

# Export assembled SFX track
print(f"💾 Saving assembled SFX track to {SFX_TRACK_WAV}...")
sfx_track.export(str(SFX_TRACK_WAV), format="wav")
print("✅ SFX track ready!")

# Multi-track mixing with sidechain ducking & broadcast loudnorm in FFmpeg
print("🎛️ Running FFmpeg Multi-Track Broadcast Mastering (-14 LUFS, True Peak <= -1.0 dBFS)...")

filter_complex = (
    "[0:a]volume=1.30,highpass=f=80,equalizer=f=250:t=q:w=1.0:g=-1.5,"
    "equalizer=f=3200:t=q:w=1.2:g=2.5,equalizer=f=10000:t=q:w=1.0:g=1.5,"
    "acompressor=threshold=0.12:ratio=3.5:attack=15:release=120,asplit=2[vo_clean][vo_sidechain];"
    "[1:a]volume=0.22[bgm_in];"
    "[bgm_in][vo_sidechain]sidechaincompress=threshold=0.075:ratio=4.5:attack=25:release=350[ducked_bgm];"
    "[2:a]volume=0.88[sfx_in];"
    "[vo_clean][ducked_bgm][sfx_in]amix=inputs=3:duration=first:dropout_transition=2[mix_raw];"
    "[mix_raw]loudnorm=I=-14:LRA=7:TP=-1.0[master_out]"
)

cmd = [
    "ffmpeg", "-y",
    "-i", str(VO_RAW),
    "-i", str(BGM_WAV),
    "-i", str(SFX_TRACK_WAV),
    "-filter_complex", filter_complex,
    "-map", "[master_out]",
    "-c:a", "libmp3lame",
    "-b:a", "320k",
    "-threads", "0",
    str(MASTER_MP3)
]

print("Executing FFmpeg mixing command...")
subprocess.run(cmd, check=True)
print(f"🎉 Master Audio successfully generated: {MASTER_MP3} ({MASTER_MP3.stat().st_size / 1024 / 1024:.2f} MB)")
