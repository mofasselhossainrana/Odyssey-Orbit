@echo off
title Odyssey ^& Orbit - local server
rem This launcher lives in tools\ : serve the project folder one level up
cd /d "%~dp0.."
echo Starting Odyssey ^& Orbit at http://localhost:8731/
echo Keep this window open while you use the site. Close it to stop.
start "" /min cmd /c "timeout /t 2 /nobreak >nul & start "" http://localhost:8731/index.html"
where python >nul 2>nul && (python -m http.server 8731 & goto :eof)
where py >nul 2>nul && (py -m http.server 8731 & goto :eof)
echo.
echo Python was not found. Install it from https://www.python.org/ or open index.html directly in Chrome.
pause
