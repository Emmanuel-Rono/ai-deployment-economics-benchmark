param(
    [string]$TaskDirectory = '.local-checks\harbor-task-submit',
    [string]$JobPrefix = 'aq-econ-submit'
)
$ErrorActionPreference = 'Continue'
Set-Location -LiteralPath $PSScriptRoot
$env:PYTHONUTF8 = '1'
$env:PYTHONIOENCODING = 'utf-8'
$harborExe = Join-Path $PSScriptRoot '.local-checks\venv\Scripts\harbor.exe'
$runLog = Join-Path $PSScriptRoot '.local-checks\harbor-live.log'
$taskPath = Join-Path $PSScriptRoot $TaskDirectory
$jobsPath = Join-Path $PSScriptRoot '.local-checks\harbor-jobs'
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'

function Write-LiveLog {
    param([Parameter(ValueFromPipeline = $true)]$Message)
    process {
        for ($logAttempt = 0; $logAttempt -lt 5; $logAttempt++) {
            try {
                Add-Content -LiteralPath $runLog -Value $Message.ToString() -Encoding utf8 -ErrorAction Stop
                break
            } catch [System.IO.IOException] {
                if ($logAttempt -eq 4) { Write-Warning "Log append unavailable; console and Harbor job logs still contain this output." }
                else { Start-Sleep -Milliseconds 100 }
            }
        }
        Write-Output $Message
    }
}

if (!(Test-Path -LiteralPath $harborExe)) { throw 'Harbor installation is incomplete.' }
if (!(Test-Path -LiteralPath (Join-Path $taskPath 'task.toml'))) { throw 'Clean package extraction is missing.' }

foreach ($agentName in @('nop', 'oracle')) {
    "`nStarting Harbor $agentName check ($stamp)." | Write-LiveLog
    & $harborExe run -p $taskPath -a $agentName --jobs-dir $jobsPath --job-name "$JobPrefix-$agentName-$stamp" 2>&1 |
        Write-LiveLog
    $runExit = $LASTEXITCODE
    "Harbor $agentName command exit code: $runExit" | Write-LiveLog
    if ($runExit -ne 0) { throw "Harbor $agentName command failed. Inspect the job logs before retrying." }
}
"`nBoth Harbor commands finished. Inspect reward and exception fields in the job results." |
    Write-LiveLog
