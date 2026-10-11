import json
import sys
from pathlib import Path

if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
        sys.stderr.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

DIR = Path(__file__).parent
OUTPUT_FILE = DIR / "scene_timeline.json"
OUTPUT_SRT = DIR / "subtitles.srt"

TOTAL_DURATION = 47.304

# 30 Word-Synchronized Visual Beats with Exact Audio Timestamps
BEATS_DATA = [
    {
        "id": 1,
        "start": 0.0,
        "end": 1.85,
        "spoken": "Aaj Delhi mein aisa kya hua...",
        "caption": ["45 METRO", "GATES LOCKED!"],
        "color": "#EF4444",
        "camera": {"scale": [1.08, 1.0], "ease": "cubic-bezier(0.16, 1, 0.3, 1)"},
        "motion": "barricade_sweep"
    },
    {
        "id": 2,
        "start": 1.85,
        "end": 3.90,
        "spoken": "...ki 45 metro station band kar diye gaye...",
        "caption": ["45 STATIONS", "SHUT DOWN!"],
        "color": "#FBBF24",
        "camera": {"scale": [1.0, 1.06], "ease": "ease-out"},
        "motion": "metro_map_pulse"
    },
    {
        "id": 3,
        "start": 3.90,
        "end": 5.80,
        "spoken": "...25,000 police tainaat hui...",
        "caption": ["25,000 POLICE", "DEPLOYED!"],
        "color": "#38BDF8",
        "camera": {"scale": [1.05, 1.0], "ease": "ease-in-out"},
        "motion": "security_flash"
    },
    {
        "id": 4,
        "start": 5.80,
        "end": 7.80,
        "spoken": "...aur flight mein ghuskar arrest...",
        "caption": ["IN-FLIGHT", "DRAMATIC ARREST!"],
        "color": "#EF4444",
        "camera": {"scale": [1.0, 1.08], "ease": "spring"},
        "motion": "target_lock_crosshair"
    },
    {
        "id": 5,
        "start": 7.80,
        "end": 10.00,
        "spoken": "Is poore bawal ke peeche hai ek sangathan...",
        "caption": ["WHO IS", "CJP?"],
        "color": "#FBBF24",
        "camera": {"scale": [1.06, 1.0], "ease": "ease-out"},
        "motion": "cinematic_reveal"
    },
    {
        "id": 6,
        "start": 10.00,
        "end": 12.40,
        "spoken": "...Cockroach Janta Party!...",
        "caption": ["COCKROACH", "JANTA PARTY!"],
        "color": "#FBBF24",
        "camera": {"scale": [1.0, 1.07], "ease": "ease-in-out"},
        "motion": "emblem_glow"
    },
    {
        "id": 7,
        "start": 12.40,
        "end": 14.10,
        "spoken": "Naam ajeeb laga?...",
        "caption": ["NAME SOUNDS", "STRANGE?"],
        "color": "#38BDF8",
        "camera": {"scale": [1.08, 1.0], "ease": "ease-out"},
        "motion": "question_pulse"
    },
    {
        "id": 8,
        "start": 14.10,
        "end": 16.70,
        "spoken": "Jab ek judge ne berozgaar yuvaon ko...",
        "caption": ["YOUTH CALLED", "'COCKROACHES'!"],
        "color": "#EF4444",
        "camera": {"scale": [1.0, 1.06], "ease": "spring"},
        "motion": "gavel_shake"
    },
    {
        "id": 9,
        "start": 16.70,
        "end": 18.00,
        "spoken": "...cockroach kaha...",
        "caption": ["INSULT TURNED", "INTO WEAPON!"],
        "color": "#FBBF24",
        "camera": {"scale": [1.04, 1.0], "ease": "ease-out"},
        "motion": "highlighter_sweep"
    },
    {
        "id": 10,
        "start": 18.00,
        "end": 21.00,
        "spoken": "...youth ne isi naam ko hathiyar bana liya!...",
        "caption": ["GEN Z", "ON STREETS!"],
        "color": "#34D399",
        "camera": {"scale": [1.0, 1.06], "ease": "ease-in-out"},
        "motion": "protest_march"
    },
    {
        "id": 11,
        "start": 21.00,
        "end": 22.80,
        "spoken": "Lekin aaj Jantar Mantar par...",
        "caption": ["JANTAR MANTAR", "SURROUNDED!"],
        "color": "#EF4444",
        "camera": {"scale": [1.06, 1.0], "ease": "spring"},
        "motion": "cordon_lock"
    },
    {
        "id": 12,
        "start": 22.80,
        "end": 24.50,
        "spoken": "...inki maang kya thi?...",
        "caption": ["DEMANDING", "RESIGNATION!"],
        "color": "#FBBF24",
        "camera": {"scale": [1.0, 1.05], "ease": "ease-out"},
        "motion": "banner_drop"
    },
    {
        "id": 13,
        "start": 24.50,
        "end": 25.70,
        "spoken": "Chief Election Commissioner...",
        "caption": ["ELECTION COMMISSION", "HEADQUARTERS"],
        "color": "#38BDF8",
        "camera": {"scale": [1.05, 1.0], "ease": "ease-out"},
        "motion": "institution_pan"
    },
    {
        "id": 14,
        "start": 25.70,
        "end": 27.20,
        "spoken": "...Gyanesh Kumar ka isteefa!...",
        "caption": ["CHIEF ELECTION", "COMMISSIONER"],
        "color": "#FBBF24",
        "camera": {"scale": [1.0, 1.08], "ease": "ease-in-out"},
        "motion": "loupe_zoom"
    },
    {
        "id": 15,
        "start": 27.20,
        "end": 28.50,
        "spoken": "Kyunki voter list se...",
        "caption": ["SPECIAL INTENSIVE", "REVISION 2026"],
        "color": "#38BDF8",
        "camera": {"scale": [1.05, 1.0], "ease": "ease-out"},
        "motion": "gazette_reveal"
    },
    {
        "id": 16,
        "start": 28.50,
        "end": 29.80,
        "spoken": "...laakhon naujawaano ke...",
        "caption": ["FORM 7", "VOTER PURGE!"],
        "color": "#EF4444",
        "camera": {"scale": [1.0, 1.06], "ease": "ease-out"},
        "motion": "form7_highlighter"
    },
    {
        "id": 17,
        "start": 29.80,
        "end": 31.80,
        "spoken": "...naam gayab kar diye gaye!...",
        "caption": ["MILLIONS OF", "NAMES REMOVED!"],
        "color": "#EF4444",
        "camera": {"scale": [1.05, 1.0], "ease": "spring"},
        "motion": "odometer_3M"
    },
    {
        "id": 18,
        "start": 31.80,
        "end": 33.10,
        "spoken": "Founder Abhijeet Dipke ko...",
        "caption": ["FOUNDER", "ABHIJEET DIPKE"],
        "color": "#38BDF8",
        "camera": {"scale": [1.0, 1.06], "ease": "ease-out"},
        "motion": "profile_card"
    },
    {
        "id": 19,
        "start": 33.10,
        "end": 34.20,
        "spoken": "...flight mein arrest kiya...",
        "caption": ["DETAINED ON", "THE RUNWAY!"],
        "color": "#EF4444",
        "camera": {"scale": [1.06, 1.0], "ease": "spring"},
        "motion": "runway_arrest"
    },
    {
        "id": 20,
        "start": 34.20,
        "end": 34.80,
        "spoken": "...hirasat...",
        "caption": ["3,000+ ACTIVISTS", "DETAINED!"],
        "color": "#EF4444",
        "camera": {"scale": [1.0, 1.05], "ease": "ease-out"},
        "motion": "siren_strobe"
    },
    {
        "id": 21,
        "start": 34.80,
        "end": 35.60,
        "spoken": "...trainein roki...",
        "caption": ["TRAINS STOPPED", "OUTSIDE DELHI!"],
        "color": "#FBBF24",
        "camera": {"scale": [1.05, 1.0], "ease": "ease-out"},
        "motion": "railway_empty"
    },
    {
        "id": 22,
        "start": 35.60,
        "end": 36.50,
        "spoken": "...aur internet band!...",
        "caption": ["MOBILE INTERNET", "SHUT DOWN!"],
        "color": "#EF4444",
        "camera": {"scale": [1.0, 1.06], "ease": "spring"},
        "motion": "telecom_no_signal"
    },
    {
        "id": 23,
        "start": 36.50,
        "end": 37.45,
        "spoken": "...fortress Delhi...",
        "caption": ["FORTRESS DELHI", "4 CORDONS!"],
        "color": "#38BDF8",
        "camera": {"scale": [1.06, 1.0], "ease": "ease-out"},
        "motion": "satellite_cordons"
    },
    {
        "id": 24,
        "start": 37.45,
        "end": 38.60,
        "spoken": "Supreme Court ne aaj...",
        "caption": ["SUPREME COURT", "HEARS PLEA!"],
        "color": "#FBBF24",
        "camera": {"scale": [1.0, 1.06], "ease": "ease-out"},
        "motion": "apex_court_dolly"
    },
    {
        "id": 25,
        "start": 38.60,
        "end": 39.60,
        "spoken": "...fatkaar lagayi:...",
        "caption": ["BENCH GRILLS", "AUTHORITIES!"],
        "color": "#38BDF8",
        "camera": {"scale": [1.05, 1.0], "ease": "spring"},
        "motion": "courtroom_shake"
    },
    {
        "id": 26,
        "start": 39.60,
        "end": 41.00,
        "spoken": "...ek makkhi maarne ke liye...",
        "caption": ["HAMMER TO", "KILL A FLY!"],
        "color": "#EF4444",
        "camera": {"scale": [1.0, 1.07], "ease": "spring"},
        "motion": "historic_quote"
    },
    {
        "id": 27,
        "start": 41.00,
        "end": 42.40,
        "spoken": "...hathouda nahi chalaya jaata!...",
        "caption": ["DISPROPORTIONATE", "FORCE!"],
        "color": "#EF4444",
        "camera": {"scale": [1.07, 1.0], "ease": "spring"},
        "motion": "verdict_stamp"
    },
    {
        "id": 28,
        "start": 42.40,
        "end": 43.60,
        "spoken": "Sach, Saboot...",
        "caption": ["FACTS FULLY", "VERIFIED!"],
        "color": "#34D399",
        "camera": {"scale": [1.0, 1.05], "ease": "ease-out"},
        "motion": "ledger_highlight"
    },
    {
        "id": 29,
        "start": 43.60,
        "end": 44.80,
        "spoken": "...Bebak...",
        "caption": ["SACH · SABOOT", "BEBAK!"],
        "color": "#FBBF24",
        "camera": {"scale": [1.05, 1.0], "ease": "ease-out"},
        "motion": "brand_credo"
    },
    {
        "id": 30,
        "start": 44.80,
        "end": 47.304,
        "spoken": "Subscribe Benaqaab India!...",
        "caption": ["SUBSCRIBE TO", "BENAQAAB INDIA!"],
        "color": "#EF4444",
        "camera": {"scale": [1.0, 1.08], "ease": "spring"},
        "motion": "subscribe_cta"
    }
]

def main():
    scenes = []
    for b in BEATS_DATA:
        pad_id = f"{b['id']:02d}"
        scenes.append({
            "id": b["id"],
            "start": b["start"],
            "end": b["end"],
            "duration": round(b["end"] - b["start"], 3),
            "spoken": b["spoken"],
            "visual": f"assets/visuals/beat_{pad_id}.jpg",
            "caption": b["caption"],
            "color": b["color"],
            "camera": b["camera"],
            "motion": b["motion"]
        })

    data = {
        "project": "SH-12: Delhi Lockdown & The CJP Protest",
        "episode": "SH-12",
        "format": "9:16 Vertical Short (1080x1920)",
        "total_duration": TOTAL_DURATION,
        "fps": 30,
        "total_frames": 1419,
        "audio": "master_audio.mp3",
        "num_scenes": len(scenes),
        "scenes": scenes
    }

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✅ Successfully written {len(scenes)} scenes to {OUTPUT_FILE}")

    # Generate SRT subtitles
    def fmt_srt(t):
        hrs = int(t // 3600)
        mins = int((t % 3600) // 60)
        secs = int(t % 60)
        millis = int(round((t - int(t)) * 1000))
        if millis >= 1000:
            millis = 999
        return f"{hrs:02d}:{mins:02d}:{secs:02d},{millis:03d}"

    srt_lines = []
    for i, s in enumerate(scenes):
        srt_lines.append(str(i + 1))
        srt_lines.append(f"{fmt_srt(s['start'])} --> {fmt_srt(s['end'])}")
        srt_lines.append(f"{s['caption'][0]} {s['caption'][1]}")
        srt_lines.append("")

    with open(OUTPUT_SRT, "w", encoding="utf-8") as f:
        f.write("\n".join(srt_lines))

    print(f"✅ Successfully written SRT subtitles to {OUTPUT_SRT}")

if __name__ == "__main__":
    main()
