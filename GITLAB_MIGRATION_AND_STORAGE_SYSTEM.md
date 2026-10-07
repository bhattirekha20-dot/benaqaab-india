# 🦊 GITLAB MIGRATION & LARGE STORAGE SYSTEM
## Benaqaab India — Video Assets & Vault Storage Architecture

> **Context:** GitHub enforces a **100 MB hard limit per file** (blocking high-bitrate MP4s like `Flight_Surcharge_Short.mp4` at 115.5 MB) and restricts free Git LFS to **1 GB storage / 1 GB bandwidth per month**. Once breached, all repository pushes are frozen.  
> **Solution:** Migrating primary storage to **GitLab** gives **5 GB – 10 GB free repository quota**, native high-capacity Git LFS, and direct support for full documentary MP4 deliverables and master audio assets.

---

## ⚡ Quick Comparison: GitHub vs GitLab for Video Production

| Dimension | GitHub | GitLab | Benaqaab Verdict |
|---|---|---|---|
| **Max Single File Size (Direct Push)** | 100 MB *(Hard block)* | Up to 5 GB *(configurable / LFS)* | 🦊 **GitLab wins** — 115MB+ videos push freely |
| **Git LFS Free Storage** | 1 GB total | 5 GB – 10 GB per namespace | 🦊 **GitLab wins** — 5x to 10x more headroom |
| **Git LFS Bandwidth Quota** | 1 GB / month *(Over-quota blocks push)* | Included in namespace quota | 🦊 **GitLab wins** — No sudden lockouts |
| **Private Repo Size Limit** | 1 GB soft / 5 GB hard | 5 GB (GitLab.com) / Unlimited (Self-hosted) | 🦊 **GitLab wins** |
| **Built-in Cloud Video Rendering** | Limited Actions minutes | Native GitLab CI/CD with Docker & artifacts | 🦊 **GitLab wins** |

---

## 🛠️ Step 1: Create Your GitLab Project

1. Go to [https://gitlab.com](https://gitlab.com) and log in.
2. Click **New Project** → **Create blank project**.
3. Settings:
   - **Project name:** `benaqaab-india`
   - **Project URL:** `https://gitlab.com/<your-gitlab-username>/benaqaab-india`
   - **Visibility Level:** `Private` 🔒 (Essential for unreleased documentaries and investigative research)
   - **Initialize with README:** **Uncheck this** (we already have our complete repository locally).
4. Click **Create project**.

---

## 🚀 Step 2: Configure Remotes (Dual-Remote or Full Cutover)

You have two simple options. **Option A is recommended** if you want to keep GitHub as a public/lightweight mirror and GitLab as your full media storage vault.

### Option A: Dual-Remote Setup (Best of Both Worlds)
Keep GitHub for lightweight docs/code, and push full video storage to GitLab:

```powershell
# 1. Add GitLab as a new remote
git remote add gitlab https://gitlab.com/<your-gitlab-username>/benaqaab-india.git

# 2. Verify remotes
git remote -v
# Output will show:
# gitlab  https://gitlab.com/<username>/benaqaab-india.git (fetch)
# gitlab  https://gitlab.com/<username>/benaqaab-india.git (push)
# origin  https://github.com/bhattirekha20-dot/benaqaab-india.git (fetch)
# origin  https://github.com/bhattirekha20-dot/benaqaab-india.git (push)
```

### Option B: Complete Move to GitLab (Replace Origin)
If you want to move 100% of your work to GitLab:

```powershell
# Rename current github remote to github-backup
git remote rename origin github-backup

# Set GitLab as your primary origin
git remote add origin https://gitlab.com/<your-gitlab-username>/benaqaab-india.git
```

---

## 📦 Step 3: Git LFS (Large File Storage) Setup for GitLab

Git LFS is already installed on this machine (`git-lfs/3.7.1`). The workspace now includes `.gitattributes` pre-configured for video and audio formats:

```text
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.mov filter=lfs diff=lfs merge=lfs -text
*.mkv filter=lfs diff=lfs merge=lfs -text
*.wav filter=lfs diff=lfs merge=lfs -text
*.mp3 filter=lfs diff=lfs merge=lfs -text
*.zip filter=lfs diff=lfs merge=lfs -text
*.psd filter=lfs diff=lfs merge=lfs -text
*.aep filter=lfs diff=lfs merge=lfs -text
```

### Activate Git LFS in the workspace:
```powershell
# Initialize Git LFS hooks
git lfs install

# Verify tracked file types
git lfs track
```

---

## 📤 Step 4: First Push to GitLab

```powershell
# 1. Stage the new files and LFS attributes
git add .gitattributes BENAQAAB_AI_VIDEO_MAKER_BIBLE.md GITLAB_MIGRATION_AND_STORAGE_SYSTEM.md README.md START_HERE.md

# 2. Commit the updates
git commit -m "feat: setup GitLab storage migration and AI Video Maker Bible"

# 3. Push LFS objects and main branch to GitLab
git push -u gitlab main
```

*(If prompted for credentials, enter your GitLab username and a **GitLab Personal Access Token** with `write_repository` scope).*

---

## 💡 How to Generate a GitLab Personal Access Token

1. In GitLab, click your avatar (top-left or top-right) → **Preferences** (or **Edit Profile**).
2. On the left sidebar, click **Access Tokens**.
3. Click **Add new token**:
   - **Token name:** `benaqaab-desktop-sync`
   - **Expiration date:** Leave blank or set 1 year
   - **Select scopes:** Check `read_repository`, `write_repository`
4. Click **Create personal access token**.
5. Copy the generated token string (starts with `glpat-...`).
6. When `git push gitlab main` asks for Password, paste this token!

---

## ⚡ Automated 1-Click Sync Script

A PowerShell script is provided at `tools/gitlab_sync.ps1` for rapid synchronization:

```powershell
# From workspace root:
powershell -ExecutionPolicy Bypass -File tools/gitlab_sync.ps1
```

This script:
1. Verifies Git LFS status.
2. Checks for files larger than 50MB and ensures they are safely handled.
3. Automatically pushes branches and LFS objects to the GitLab remote.

---

## 🎬 Storage Strategy for Video Renders

### Rule 1: The Master Source Code is Sacred (`comp.html`)
The HTML5/Canvas source code (`comp.html` + `BEATS.json` + `motion.py`) is lightweight (typically 20KB – 2MB) and is **100% deterministic**. Any agent or machine with Playwright/Chromium can rebuild the exact frame-accurate MP4 from source code at any time.

### Rule 2: Delivered MP4s Belong in Git LFS on GitLab
- Put final 1080x1920 (9:16) Shorts and 1920x1080 (16:9) Long-form videos in `projects/<topic_id>/delivery/` or `VIDEOS/`.
- With `.gitattributes` active, GitLab stores them via Git LFS without bloating standard git clone size.

### Rule 3: Scratch Renders Stay Local (`.gitignore`)
- Intermediate frame dumps, `.cache/`, and raw temp clips stay excluded in `.gitignore` so your repo remains clean, fast, and structured.
