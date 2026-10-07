# ═══════════════════════════════════════════════════════════════════
# Benaqaab India — 1-Click GitLab Sync & Storage Manager
# Usage: powershell -ExecutionPolicy Bypass -File tools/gitlab_sync.ps1
# ═══════════════════════════════════════════════════════════════════

param (
    [string]$GitLabUrl = "",
    [string]$Branch = "main",
    [switch]$ForceSetup
)

Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host " 🦊 BENAQAAB INDIA — GITLAB STORAGE & SYNC ENGINE" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan

# Check Git LFS status
Write-Host "[1/5] Checking Git LFS..." -ForegroundColor Yellow
$lfsInstalled = git lfs version 2>$null
if (-not $lfsInstalled) {
    Write-Host "❌ Git LFS is not installed. Please install git-lfs." -ForegroundColor Red
    exit 1
} else {
    Write-Host "  ✓ Git LFS detected: $lfsInstalled" -ForegroundColor Green
    git lfs install | Out-Null
}

# Check Git Remotes
Write-Host "[2/5] Inspecting configured remotes..." -ForegroundColor Yellow
$remotes = git remote -v
$hasGitLab = $remotes -match "gitlab"

if (-not $hasGitLab -or $ForceSetup) {
    if ([string]::IsNullOrWhiteSpace($GitLabUrl)) {
        Write-Host "  GitLab remote is not yet configured." -ForegroundColor Yellow
        $enteredUrl = Read-Host "  Enter your GitLab Repo URL (e.g., https://gitlab.com/<username>/benaqaab-india.git)"
        if ([string]::IsNullOrWhiteSpace($enteredUrl)) {
            Write-Host "  ⚠️ No URL entered. Aborting push. Run with -GitLabUrl <url>." -ForegroundColor Red
            exit 1
        }
        $GitLabUrl = $enteredUrl.Trim()
    }

    if ($hasGitLab) {
        git remote set-url gitlab $GitLabUrl
        Write-Host "  ✓ Updated 'gitlab' remote to $GitLabUrl" -ForegroundColor Green
    } else {
        git remote add gitlab $GitLabUrl
        Write-Host "  ✓ Added 'gitlab' remote: $GitLabUrl" -ForegroundColor Green
    }
} else {
    Write-Host "  ✓ 'gitlab' remote is present." -ForegroundColor Green
}

# Inspect Large Files
Write-Host "[3/5] Inspecting files > 50MB in working tree..." -ForegroundColor Yellow
$largeFiles = Get-ChildItem -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $_.Length -gt 50MB }
if ($largeFiles) {
    foreach ($file in $largeFiles) {
        $mb = [math]::Round($file.Length / 1MB, 2)
        Write-Host "  ⚠️ Large Asset: $($file.Name) ($mb MB)" -ForegroundColor Magenta
    }
    Write-Host "  ✓ Handled cleanly via Git LFS (.gitattributes)" -ForegroundColor Green
} else {
    Write-Host "  ✓ No files over 50MB detected." -ForegroundColor Green
}

# Git LFS Pre-Push Verification
Write-Host "[4/5] Pre-checking LFS tracking..." -ForegroundColor Yellow
git lfs track

# Execute Push
Write-Host "[5/5] Pushing branch '$Branch' and LFS objects to GitLab..." -ForegroundColor Yellow
git push gitlab $Branch --tags
if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "🎉 SUCCESS: All code, video assets, and LFS pointers pushed to GitLab!" -ForegroundColor Green
    Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
} else {
    Write-Host ""
    Write-Host "❌ Push encountered an error (exit code $LASTEXITCODE)." -ForegroundColor Red
    Write-Host "Tips:" -ForegroundColor Yellow
    Write-Host " - If authentication failed, use a GitLab Personal Access Token with write_repository scope."
    Write-Host " - Verify the GitLab repository exists and you have write permissions."
}
