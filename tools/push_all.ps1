# ═══════════════════════════════════════════════════════════════════
# Benaqaab India — Universal Dual-Remote Push (GitHub + Codeberg)
# Usage: powershell -ExecutionPolicy Bypass -File tools/push_all.ps1
# ═══════════════════════════════════════════════════════════════════

param (
    [string]$Branch = "main"
)

Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host " 🚀 BENAQAAB INDIA — DUAL PUSH (GITHUB + CODEBERG)" -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan

# 1. Push to GitHub Origin
Write-Host "`n[1/2] Pushing to GitHub (origin/$Branch)..." -ForegroundColor Yellow
git push origin $Branch
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✓ GitHub push successful!" -ForegroundColor Green
} else {
    Write-Host "  ❌ GitHub push failed (exit code $LASTEXITCODE)." -ForegroundColor Red
}

# 2. Push to Codeberg
Write-Host "`n[2/2] Pushing to Codeberg (codeberg/$Branch)..." -ForegroundColor Yellow
git push codeberg $Branch
if ($LASTEXITCODE -eq 0) {
    Write-Host "  ✓ Codeberg push successful!" -ForegroundColor Green
} else {
    Write-Host "  ❌ Codeberg push failed (exit code $LASTEXITCODE)." -ForegroundColor Red
    Write-Host "  Tip: If credentials expired, run 'git push codeberg main' interactively to refresh your browser token." -ForegroundColor Yellow
}

Write-Host "`n═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
Write-Host " Dual push routine complete." -ForegroundColor Cyan
Write-Host "═══════════════════════════════════════════════════════════" -ForegroundColor Cyan
