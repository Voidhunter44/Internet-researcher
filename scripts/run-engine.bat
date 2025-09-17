@echo off
echo Starting Internet Research Engine...
echo.
set PROJECT_DIR=%~dp0..
cd /d "%PROJECT_DIR%"
echo Research engine running in: %cd%
python src\ResearchEngine\research_engine.py
echo.
echo Research engine has stopped
pause