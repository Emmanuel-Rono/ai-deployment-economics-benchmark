$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$runLog = Join-Path $PSScriptRoot '.local-checks\harbor-live.log'
Write-Host 'Aq_Econ — live Harbor run log' -ForegroundColor Cyan
Write-Host 'This window shows installation status and the nop/oracle run results.'
Write-Host 'Press Ctrl+C to stop watching; the run continues independently.'
Get-Content -LiteralPath $runLog -Tail 100 -Wait
