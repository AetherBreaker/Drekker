param(
  [string]$CWDPath = (Get-Location).Path
)
Write-Host "Activating Python virtual environment in $CWDPath"
& "$CWDPath\.venv\Scripts\Activate.ps1"

# set the TEXTUAL environment variable to enable debug mode
# $env:TEXTUAL = "devtools"

# Start-Process -FilePath "python" -ArgumentList ".\src\__main__.py", "-u", "-X", "pycache_prefix=$CWDPath\PYCACHE"
# Write-Host "Textual Web Server started in $CWDPath"

Start-Process -FilePath "textual" -ArgumentList "console", "-v"
Write-Host "Textual Console started in $CWDPath"
