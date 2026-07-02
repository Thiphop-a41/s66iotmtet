@echo off
title Calculator
cd /d "%~dp0"

where py >nul 2>&1
if %errorlevel%==0 (
    start "" pyw cal.py
) else (
    start "" pythonw cal.py
)

exit