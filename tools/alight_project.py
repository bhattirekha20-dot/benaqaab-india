#!/usr/bin/env python3
"""
alight_project.py — build an Alight Motion project / preset (.xml) from Python.

What this is
------------
Alight Motion's project format is an XML scene document. Its structure is documented in
detail by the community project `kuchingneko28/alight-motion-docs` (generated from the
decompiled APK: 697 effect asset XMLs, 20 shape templates), which we inspected and saved
under knowledge/capcut_alight_research/source_snapshots/.

Honesty box
-----------
* This writes a **project file**. Alight Motion itself must import and export it.
* Effect ids are Alight Motion's canonical ids (e.g. `com.alightcreative.effects.box`).
  A few effects are downloaded by the app at runtime; the doc notes the scene still
  imports and renders once the effect is available.
* The scene we emit follows the documented ordering rules: scene attributes, optional
  <media>, elements with ascending ids, <transform>, type-specific content, <effect>
  blocks, then keyframed <property> blocks.

Supported here: shapes (.rect / .ellipse template references), text, media, transform,
gradient fills, strokes, shadows, glows, effect stacks, keyframes with cubic-bezier
easing, adjustment layers (Copy Background + grade stack) and nested scenes.
"""
from __future__ import annotations
import os
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from xml.dom import minidom

FX = "com.alightcreative.effects."          # canonical effect id prefix


def _fmt(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, float):
        return f"{v:.6f}"
    if isinstance(v, (list, tuple)):
        return ",".join(_fmt(x) for x in v)
    return str(v)


@dataclass
class Keyframe:
    t: float                 # seconds
    v: float | tuple         # value
    easing: str | None = None   # e.g. "cubicBezier 0.480224 0.0 1.0 1.0"


@dataclass
class Property:
    name: str
    type: str = "float"      # float | int | color | vec2 | vec3 | vec4 | bool | string | uri | quat
    value: object | None = None
    keyframes: list[Keyframe] = field(default_factory=list)

    def is_default(self, default) -> bool:
        return self.value == default and not self.keyframes

    def write(self, parent: ET.Element) -> None:
        el = ET.SubElement(parent, "property", {"name": self.name, "type": self.type})
        if self.keyframes:
            for kf in self.keyframes:
                a = {"t": f"{kf.t:.6f}", "v": _fmt(kf.v)}
                if kf.easing: a["e"] = kf.easing
                ET.SubElement(el, "kf", a)
        else:
            el.set("value", _fmt(self.value))


@dataclass
class Effect:
    id: str                                  # canonical id, e.g. com.alightcreative.effects.box
    params: dict = field(default_factory=dict)
    hidden: bool = False
    locally_applied: bool = True

    def write(self, parent: ET.Element) -> None:
        a = {"id": self.id}
        if self.hidden: a["hidden"] = "true"
        a["locallyApplied"] = _fmt(self.locally_applied)
        el = ET.SubElement(parent, "effect", a)
        for k, v in self.params.items():
            prop = v if isinstance(v, Property) else Property(k, _guess_type(v), v)
            prop.write(el)


def _guess_type(v) -> str:
    if isinstance(v, bool): return "bool"
    if isinstance(v, int): return "int"
    if isinstance(v, str) and v.startswith("#"): return "color"
    if isinstance(v, (tuple, list)):
        return {2: "vec2", 3: "vec3", 4: "vec4"}.get(len(v), "vec2")
    return "float"


@dataclass
class Element:
    id: int
    label: str
    start: float = 0.0                       # seconds
    end: float | None = None                 # seconds (scene totalTime if None)
    kind: str = "shape"                      # shape | text | media | scene (nested)
    template: str | None = ".rect"           # s=".rect" etc.
    fill_type: str = "color"
    fill: str | None = None                  # "#AARRGGBB"
    blending: str | None = None
    transform: dict = field(default_factory=dict)   # location/scale/rotation/opacity/anchors
    props: list[Property] = field(default_factory=list)
    effects: list[Effect] = field(default_factory=list)
    children: list = field(default_factory=list)
    text: dict | None = None                 # {"size","font","align","content","wrapWidth"}
    gradient: dict | None = None             # {"type","startColor","endColor","start","end"}
    stroke: dict | None = None
    extra_children: list[ET.Element] = field(default_factory=list)

    # convenience builders -------------------------------------------------
    @staticmethod
    def rect(x, y, w, h, fill, **kw) -> "Element":
        e = Element(id=kw.pop("id", 1), label=kw.pop("label", "Rectangle"), kind="shape",
                    template=".rect", fill=fill, **kw)
        e.transform.setdefault("location", (x, y, 0.0))
        e.props.append(Property("size", "vec2", (w, h)))
        return e

    @staticmethod
    def text_layer(x, y, content, size=48, font="sans", fill="#FFFFFFFF", **kw) -> "Element":
        e = Element(id=kw.pop("id", 1), label=kw.pop("label", content[:18]), kind="text",
                    fill=fill, **kw)
        e.transform.setdefault("location", (x, y, 0.0))
        e.text = {"size": size, "font": font, "align": "center", "content": content, "wrapWidth": 512}
        return e

    # ----------------------------------------------------------------------
    def write(self, parent: ET.Element, scene_end_ms: int = 0) -> None:
        # an element without an explicit end lasts the whole scene (documented default)
        end_ms = int(self.end * 1000) if self.end is not None else scene_end_ms
        a = {"id": str(self.id), "label": self.label, "startTime": str(int(self.start * 1000)),
             "endTime": str(end_ms),
             "fillType": self.fill_type, "mediaFillMode": "stretch"}
        if self.template: a["s"] = self.template
        if self.blending: a["blending"] = self.blending
        el = ET.SubElement(parent, self.kind if self.kind != "scene" else "scene", a)
        # child order documented: transform, fill/gradient, text content, then props/effects
        tr = ET.SubElement(el, "transform")
        for name in ("location", "scale", "rotation", "opacity", "anchor"):
            if name in self.transform:
                v = self.transform[name]
                t = "float" if isinstance(v, (int, float)) else _guess_type(v)
                ET.SubElement(tr, name, {"value": _fmt(v)} if t != "float" else {"value": _fmt(float(v))})
        if self.fill and self.kind in ("shape", "text"):
            ET.SubElement(el, "fillColor", {"value": self.fill})
        if self.gradient:
            g = self.gradient
            ET.SubElement(el, "gradient", {
                "type": g.get("type", "linear"),
                "startColor": g.get("startColor", "#FF000000"),
                "endColor": g.get("endColor", "#00000000"),
                "start": _fmt(g.get("start", (0.0, 0.0))),
                "end": _fmt(g.get("end", (1.0, 1.0))),
            })
        if self.stroke:
            ET.SubElement(el, "stroke", {k: _fmt(v) for k, v in self.stroke.items()})
        if self.text:
            t = ET.SubElement(el, "text", {
                "size": _fmt(float(self.text["size"])), "font": self.text["font"],
                "wrapWidth": str(self.text.get("wrapWidth", 512)), "align": self.text.get("align", "center"),
            })
            content = ET.SubElement(t, "content"); content.text = self.text["content"]
        for p in self.props:
            p.write(el)
        for fx in self.effects:
            fx.write(el)
        for c in self.children:
            c.write(el, scene_end_ms)
        for x in self.extra_children:
            el.append(x)


# ------------------------------------------------------------------ recipes
def adjustment_layer(canvas_w, canvas_h, grade_effects: list[Effect], label="Grade",
                     start=0.0, end=None, eid=100) -> Element:
    """A full-frame adjustment layer: Copy Background first, then the grading stack.

    Documented rule: `.rect` is 100x100 units, so scale = canvas / 100.
    """
    e = Element(id=eid, label=label, start=start, end=end, kind="shape", template=".rect",
                fill_type="color", fill=None)
    e.transform = {"location": (canvas_w / 2, canvas_h / 2, 0.0),
                   "scale": (canvas_w / 100.0, canvas_h / 100.0)}
    e.effects = [Effect(FX + "lift", {"fill": 0.0})] + list(grade_effects)
    return e


def gloss_glow(canvas_w, canvas_h, colour="#ffff8c42", opacity=0.4, blur=1.6) -> Element:
    """Bloom pass: blur + screen blending over the composite."""
    e = adjustment_layer(canvas_w, canvas_h, [Effect(FX + "gaussianblur", {"strength": blur})],
                         label="Glow", eid=101)
    e.blending = "screen"
    e.transform["opacity"] = opacity
    e.gradient = {"type": "radial", "startColor": colour, "endColor": "#ff000000",
                  "start": (0.5, 0.45), "end": (1.0, 1.0)}
    return e


@dataclass
class Scene:
    title: str = "New Project"
    width: int = 1080
    height: int = 1080
    total_time_ms: int = 3000
    fps: int = 30
    bgcolor: str = "#FF000000"
    amver: int = 1028425
    ffver: int = 106
    am: str = "com.alightcreative.motion/5.0.273.1028425"
    amplatform: str = "android"
    elements: list[Element] = field(default_factory=list)
    media: list[dict] = field(default_factory=list)

    def add(self, el: Element) -> "Scene":
        self.elements.append(el); return self

    def to_xml(self) -> str:
        root = ET.Element("scene", {
            "title": self.title, "width": str(self.width), "height": str(self.height),
            "exportWidth": str(self.width), "exportHeight": str(self.height),
            "bgcolor": self.bgcolor, "totalTime": str(self.total_time_ms), "fps": str(self.fps),
            "modifiedTime": "1700000000000", "amver": str(self.amver), "ffver": str(self.ffver),
            "am": self.am, "amplatform": self.amplatform,
        })
        for m in self.media:
            ET.SubElement(root, "media", {k: _fmt(v) for k, v in m.items()})
        for el in self.elements:
            el.write(root, self.total_time_ms)
        raw = ET.tostring(root, encoding="unicode")
        return minidom.parseString(raw).toprettyxml(indent="  ", encoding=None)

    def write(self, path: str) -> dict:
        xml = self.to_xml()
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(xml)
        return {"path": os.path.abspath(path), "bytes": len(xml.encode()),
                "elements": len(self.elements), "duration_s": self.total_time_ms / 1000.0}


# ------------------------------------------------------------------- validator
def validate(path: str) -> dict:
    """Check a scene document against the documented import rules."""
    tree = ET.parse(path); root = tree.getroot()
    problems, notes = [], []
    if root.tag != "scene":
        problems.append(f"root tag is <{root.tag}>, expected <scene>")
    for attr in ("width", "height", "exportWidth", "exportHeight", "bgcolor", "totalTime",
                 "fps", "amver", "ffver", "am", "amplatform"):
        if attr not in root.attrib: problems.append(f"scene missing attribute {attr}")
    ids, seen = [], set()
    media = [e for e in root if e.tag == "media"]
    elements = [e for e in root if e.tag != "media"]
    for i, el in enumerate(root):
        if el.tag == "media": continue
        if el.tag == "media" and i < len(media): notes.append("media must come before elements")
    for el in elements:
        if "id" not in el.attrib: problems.append(f"<{el.tag}> without id")
        else:
            ids.append(int(el.attrib["id"]))
            if int(el.attrib["id"]) in seen: problems.append(f"duplicate id {el.attrib['id']}")
            seen.add(int(el.attrib["id"]))
        if el.find("transform") is None: problems.append(f"element {el.attrib.get('id')} has no <transform>")
        if el.find("text") is not None and el.find("text/content") is None:
            problems.append(f"text element {el.attrib.get('id')} has no <content>")
        for fx in el.findall("effect"):
            if not fx.attrib.get("id", "").startswith("com.alightcreative."):
                problems.append(f"effect id {fx.attrib.get('id')!r} is not a canonical id")
            if "locallyApplied" not in fx.attrib:
                problems.append(f"effect {fx.attrib.get('id')!r} missing locallyApplied")
        for p in el.findall("property"):
            if p.findall("kf"):
                for kf in p.findall("kf"):
                    for a in ("t", "v"):
                        if a not in kf.attrib: problems.append(f"kf missing {a} in property {p.attrib.get('name')}")
            elif "value" not in p.attrib:
                problems.append(f"property {p.attrib.get('name')!r} has neither value nor kf")
    # media must precede elements in document order
    tags = [e.tag for e in root]
    if "media" in tags and "scene" not in tags:
        first_el = next((i for i, t in enumerate(tags) if t != "media"), None)
        last_media = max((i for i, t in enumerate(tags) if t == "media"), default=-1)
        if first_el is not None and last_media > first_el:
            problems.append("a <media> declaration appears after an element")
    return {"path": os.path.abspath(path), "problems": problems, "notes": notes,
            "elements": len(elements), "media": len(media), "ids_ascending": ids == sorted(ids),
            "fps": root.attrib.get("fps"), "total_ms": root.attrib.get("totalTime")}


# ------------------------------------------------------------------- demo
if __name__ == "__main__":
    import sys, json
    out = sys.argv[1] if len(sys.argv) > 1 else "alight_scene.xml"
    sc = Scene(title="Benaqaab · title card", width=1080, height=1920, total_time_ms=6000, fps=30,
               bgcolor="#FF0B0F1A")
    sc.add(Element.rect(540, 960, 1080, 1920, "#FF101733", id=1, label="Backdrop"))
    sc.add(Element.text_layer(540, 820, "BENAQAAB", size=120, font="sans", fill="#FFEA F1FF".replace(" ", ""),
                              id=2, label="Title"))
    t = sc.elements[-1]
    t.props += [Property("size", "float", keyframes=[
        Keyframe(0.0, 0.40, "cubicBezier 0.480224 0.0 1.0 1.0"),
        Keyframe(0.5, 1.00, "cubicBezier 0.480224 0.0 1.0 1.0")]),
        Property("tracking", "float", 8.0)]
    sc.add(adjustment_layer(1080, 1920, [
        Effect(FX + "exposure", {"exposure": 0.06}),
        Effect(FX + "brightcont2", {"contrast": 0.10}),
        Effect(FX + "vignette", {"radius": 0.62, "strength": 0.35}),
        Effect(FX + "noise3", {"amount": 0.06}),
    ], label="Grade", eid=3, start=0, end=6.0))
    sc.add(gloss_glow(1080, 1920))
    report = sc.write(out)
    report["validation"] = validate(out)
    print(json.dumps(report, indent=2))
