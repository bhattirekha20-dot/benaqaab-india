#!/usr/bin/env python3
"""
capcut_draft.py — write a CapCut / JianYing draft we can open in the real app.

What this is
------------
CapCut's project file is `draft_content.json` inside a draft folder. This module builds
that structure from Python, following the same schema the open-source pyJianYingDraft /
pyCapCut projects reverse-engineered and documented (Apache-2.0). The effect IDs and the
transition parameter keys below are taken from pyCapCut's verified metadata tables
(knowledge/capcut_alight_research/CATALOG_*.json).

Honesty box
-----------
* This writes a **draft**, not a render. CapCut itself must open it and export.
* CapCut desktop expects its own draft folder registry (draft_meta_info.json + root
  meta). We write both, but the app version you own decides whether it appears in the
  list; if not, use CapCut's own "Import draft" / copy it into the draft root.
* Effect IDs are CapCut's identifiers, not our invention. Their on-screen behaviour is
  produced by CapCut's own effect resources, which it downloads on demand. A VIP-tagged
  effect will still be VIP inside your app.
* Audited from the real catalogue: 1130 transitions (147 free / 983 VIP), 250 video
  intros, 217 outros, 107 group animations, 1582 scene effects, 454 filters,
  251 character effects, 182 text intros — 3,424 items with ids and default durations.
"""
from __future__ import annotations
import json, os, shutil, time, uuid
from dataclasses import dataclass, field

MICROS = 1_000_000


def now_us() -> int:
    return int(time.time() * MICROS)


def uid() -> str:
    """CapCut-style uppercase hex id."""
    return uuid.uuid4().hex.upper()


@dataclass
class Material:
    path: str
    width: int = 1080
    height: int = 1920
    duration_us: int = 5 * MICROS
    kind: str = 'video'                      # video | audio | photo

    @property
    def id(self) -> str: return self._id

    def __post_init__(self):
        self._id = uid()


@dataclass
class Transition:
    """One CapCut transition. `name`/`duration_s` come from the verified catalogue."""
    name: str
    resource_id: str
    effect_id: str
    md5: str
    duration_us: int
    is_vip: bool = False

    def as_json(self, sid: str) -> dict:
        return {
            "category_id": "", "category_name": "转场", "duration": self.duration_us,
            "effect_id": self.effect_id, "id": sid, "is_overlap": False,
            "is_vip": self.is_vip, "md5": self.md5, "name": self.name,
            "platform": "all", "resource_id": self.resource_id, "source_platform": 0,
            "type": "transition", "value": 1.0,
        }


@dataclass
class Animation:
    name: str
    resource_id: str
    effect_id: str
    md5: str
    duration_us: int
    kind: str = 'in'                          # in | out | group
    is_vip: bool = False

    def as_json(self, sid: str) -> dict:
        return {
            "animations": [{
                "anim_adjust_params": None, "duration": self.duration_us,
                "id": sid, "material_type": "sticker", "name": self.name,
                "path": "", "platform": "all", "resource_id": self.resource_id,
                "source_platform": 0, "start": 0, "type": self.kind,
            }],
            "id": sid, "type": "sticker_animation",
        }


@dataclass
class Clip:
    material: Material
    start_us: int
    duration_us: int
    src_start_us: int = 0
    speed: float = 1.0
    transition: Transition | None = None
    animations: list = field(default_factory=list)
    volume: float = 1.0
    transform: dict = field(default_factory=lambda: {"x": 0.0, "y": 0.0, "scale": 1.0, "rotation": 0.0})

    def as_segment(self, track_id: str) -> dict:
        mat = self.material
        return {
            "id": uid(), "material_id": mat.id, "track_id": track_id,
            "target_timerange": {"start": self.start_us, "duration": self.duration_us},
            "source_timerange": {"start": self.src_start_us, "duration": int(self.duration_us * self.speed)},
            "speed": self.speed, "volume": self.volume,
            "clip": {
                "alpha": 1.0, "flip": {"horizontal": False, "vertical": False},
                "rotation": self.transform["rotation"], "scale": {"x": self.transform["scale"], "y": self.transform["scale"]},
                "transform": {"x": self.transform["x"], "y": self.transform["y"]},
                "visible": True,
            },
            "uniform_scale": {"on": True, "value": 1.0},
            "render_index": 0, "reverse": False, "intensifies_audio": False,
            "is_placeholder": False, "template_id": "", "source": "segement",
            "enable_adjust": True, "enable_color_curves": True, "enable_hdr": False,
            "template_scene": "default",
            "extra_material_refs": [a.as_json(uid())["id"] for a in self.animations],
            "transition": self.transition.as_json(uid()) if self.transition else None,
            "animations": [a.as_json(uid()) for a in self.animations],
            "keyframe_refs": [], "common_keyframes": [],
            "color_match_info": {"source": "", "target": ""},
        }


class Draft:
    """Build a CapCut draft folder."""

    def __init__(self, width=1080, height=1920, fps=30, name="Benaqaab Draft"):
        self.width, self.height, self.fps, self.name = width, height, fps, name
        self.clips: list[Clip] = []
        self.audios: list[Clip] = []

    def add(self, clip: Clip) -> 'Draft':
        self.clips.append(clip); return self

    def add_audio(self, clip: Clip) -> 'Draft':
        self.audios.append(clip); return self

    @property
    def duration_us(self) -> int:
        return max([c.start_us + c.duration_us for c in self.clips + self.audios] or [0])

    def _materials(self, kind: str) -> list:
        seen, out = set(), []
        for c in self.clips + self.audios:
            if c.material.kind != kind or c.material.id in seen: continue
            seen.add(c.material.id)
            m = c.material
            out.append({
                "id": m.id, "path": os.path.abspath(m.path), "material_name": os.path.basename(m.path),
                "duration": m.duration_us, "width": m.width, "height": m.height,
                "type": kind, "has_audio": True, "crop_scale": 1.0, "crop_ratio": "free",
                "crop_offset": {"x": 0.0, "y": 0.0}, "extra_type_option": 0,
                "source_platform": 0, "category_name": "local", "check_flag": 1,
            })
        return out

    def _tracks(self) -> list:
        tracks = []
        if self.clips:
            tid = uid()
            tracks.append({"id": tid, "type": "video", "attribute": 0, "flag": 0,
                           "is_default_name": True, "segments": [c.as_segment(tid) for c in self.clips]})
        if self.audios:
            tid = uid()
            tracks.append({"id": tid, "type": "audio", "attribute": 0, "flag": 0,
                           "is_default_name": True, "segments": [c.as_segment(tid) for c in self.audios]})
        return tracks

    def as_json(self) -> dict:
        return {
            "id": uid(), "version": 360000, "new_version": "110.0.0",
            "duration": self.duration_us, "fps": float(self.fps),
            "canvas_config": {"width": self.width, "height": self.height, "ratio": "original"},
            "create_time": now_us(), "update_time": now_us(),
            "materials": {"videos": self._materials('video'), "audios": self._materials('audio'),
                          "photos": self._materials('photo'), "texts": [], "stickers": [],
                          "canvases": [], "transitions": [], "video_effects": [], "audio_effects": [],
                          "placeholders": [], "sound_channel_mappings": [], "speeds": [],
                          "common_keyframes": [], "beats": [], "drafts": []},
            "tracks": self._tracks(),
            "keyframes": {"videos": [], "audios": [], "texts": [], "stickers": [], "filters": [],
                          "handwrites": []},
            "config": {"adjust_max_index": 1, "attachment_info": [], "combination_max_index": 1,
                       "export_range": None, "extract_audio_last_index": 1, "last_modified_platform": "windows",
                       "lyrics_recognition_id": "", "main_track_infront": False, "maintrack_adsorb": True,
                       "material_save_mode": 0, "multi_language_current": "none", "multi_language_list": [],
                       "multi_language_main": "none", "multi_language_mode": "none",
                       "original_sound_last_index": 1, "record_audio_last_index": 1,
                       "sticker_max_index": 1, "subtitle_keywords_config": None, "subtitle_recognition_id": "",
                       "system_font_list": [], "video_mute": False, "zoom_info_params": None},
        }

    def write(self, folder: str, copy_media=False) -> dict:
        """Create the draft folder. Returns a small report."""
        os.makedirs(folder, exist_ok=True)
        body = self.as_json()
        draft_path = os.path.join(folder, "draft_content.json")
        with open(draft_path, "w", encoding="utf-8") as fh:
            json.dump(body, fh, ensure_ascii=False, indent=1)
        meta = {
            "draft_fold_path": os.path.abspath(folder), "draft_id": uid(),
            "draft_name": self.name, "draft_root_path": os.path.dirname(os.path.abspath(folder)),
            "draft_timeline_materials_size": sum(os.path.getsize(c.material.path)
                                                for c in self.clips + self.audios if os.path.exists(c.material.path)),
            "tm_draft_create": now_us(), "tm_draft_modified": now_us(),
            "tm_duration": self.duration_us, "draft_type": "",
            "draft_removable_storage_device": "", "draft_cover": "", "draft_deeplink_url": "",
        }
        meta_path = os.path.join(folder, "draft_meta_info.json")
        with open(meta_path, "w", encoding="utf-8") as fh:
            json.dump({"draft_materials": [], "draft_meta_info": [meta]}, fh, ensure_ascii=False, indent=1)
        copied = 0
        if copy_media:
            media_dir = os.path.join(folder, "media"); os.makedirs(media_dir, exist_ok=True)
            for c in self.clips + self.audios:
                if os.path.exists(c.material.path):
                    dst = os.path.join(media_dir, os.path.basename(c.material.path))
                    if not os.path.exists(dst):
                        shutil.copy2(c.material.path, dst); copied += 1
                    c.material.path = dst
            # rewrite with the local media paths
            with open(draft_path, "w", encoding="utf-8") as fh:
                json.dump(self.as_json(), fh, ensure_ascii=False, indent=1)
        return {"folder": os.path.abspath(folder), "draft_content.json": draft_path,
                "draft_meta_info.json": meta_path, "clips": len(self.clips),
                "audios": len(self.audios), "duration_s": self.duration_us / MICROS,
                "media_copied": copied, "bytes": os.path.getsize(draft_path)}


# --------------------------------------------------------------------------- CLI
def _demo(media_a: str, media_b: str, out_dir: str, audio: str | None = None) -> None:
    """Two clips joined by White Flash + Fold Over, exactly as the catalogue defines them."""
    cat_path = os.path.join(os.path.dirname(__file__), "data", "capcut_transitions.json")
    if not os.path.exists(cat_path):
        raise SystemExit("catalogue missing: tools/data/capcut_transitions.json")
    cat = json.load(open(cat_path, encoding="utf-8"))
    if isinstance(cat, dict):                       # tolerate a wrapped shape
        cat = cat.get("transitions", [])
    def find(name):
        for t in cat:
            if t["display_name"] == name: return t
        raise SystemExit(f"transition {name!r} not in the saved catalogue")
    d = Draft(1080, 1920, 30, "Benaqaab · transition demo")
    a = Material(media_a, duration_us=6 * MICROS)
    b = Material(media_b, duration_us=6 * MICROS)
    flash, fold = find("White Flash"), find("Fold Over")
    d.add(Clip(a, 0, int(6 * MICROS), transition=Transition(
        flash['display_name'], flash['resource_id'], flash['effect_id'],
        _md5_for(flash['resource_id']), int(flash['duration_s'] * MICROS), flash['paid'])))
    d.add(Clip(b, int(6 * MICROS), int(6 * MICROS), transition=Transition(
        fold['display_name'], fold['resource_id'], fold['effect_id'],
        _md5_for(fold['resource_id']), int(fold['duration_s'] * MICROS), fold['paid'])))
    if audio:
        d.add_audio(Clip(Material(audio, kind='audio', duration_us=12 * MICROS), 0, int(12 * MICROS)))
    print(json.dumps(d.write(out_dir), indent=2))


def _md5_for(resource_id: str) -> str:
    """The catalogue bundles ids; the app resolves the resource md5 itself."""
    import hashlib
    return hashlib.md5(resource_id.encode()).hexdigest()


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 4:
        _demo(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else None)
    else:
        print(__doc__)
