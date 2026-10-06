# Benaqaab India — Central Private Repository

> **SACH · SABOOT · BEBAK** (truth · proof · outspoken)

This is the **single, centralised, private repository** for all Benaqaab India video-production
assets, AI agent skills, production tools, brand identity, knowledge base, and delivered projects.

---

## 🚀 Quick Start for Any AI Agent

1. **Read [`CENTRAL_AGENT_MEMORY.md`](CENTRAL_AGENT_MEMORY.md)** — the single source of truth.
2. **Consult [`CENTRAL_TOPICS_MASTER.md`](CENTRAL_TOPICS_MASTER.md)** — the single master registry for all video topics.
3. Then read [`BENAQAAB_AI_AGENT_COMPACT.md`](BENAQAAB_AI_AGENT_COMPACT.md) — your full operating manual.
4. Then follow the reading order in [`START_HERE.md`](START_HERE.md).

> **Rule of precedence:** `CENTRAL_AGENT_MEMORY.md` + `CENTRAL_TOPICS_MASTER.md` + the compact file outrank everything else.
> `MEMORY.md` is append-only history. The master skill file is a look-up reference, not a linear read.

---

## 📁 Structure Overview

| Folder/File | Purpose |
|---|---|
| `CENTRAL_AGENT_MEMORY.md` | **Centralised memory** — all agents read this first |
| `CENTRAL_TOPICS_MASTER.md` | **Centralised topics registry** — covered blacklist, live cycles & ready backlog |
| `BENAQAAB_AI_AGENT_COMPACT.md` | Operating manual (pipeline, gates, templates) |
| `BENAQAAB_AI_AGENT_MASTER_SKILL.md` | 45K-line complete reference (use §INDEX) |
| `MEMORY.md` | Full production history (append-only) |
| `SKILLS_*.md` | Domain-specific skill files |
| `brand/` | Logo, fonts (11 faces), presenter cutouts, style refs |
| `knowledge/` | Research data, catalogues, topic ideas |
| `tools/` | Quality gates, CapCut/Alight project writers |
| `viz/` | Rendering engine, motion libraries, episode recipes |
| `projects/` | 9 production projects (EP12–EP16 + 3 anime edits + Flight Surcharge) |
| `VIDEOS/` | Delivered MP4s (8 videos + gallery page) |

---

## 🔒 Security

- All credentials, API keys, and `.env` files are excluded via `.gitignore`.
- This repository is intended to remain **private**.
- Rendered MP4s are `.gitignore`d (too large for Git).

---

## 📋 Maintenance

- After every delivery → append to `MEMORY.md`
- After editing skills → run `python3 _assemble_agent_file.py`
- Never delete protected files (listed in `CENTRAL_AGENT_MEMORY.md` §11)
