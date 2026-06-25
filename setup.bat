@echo off
echo ========================================
echo Murder Mystery Game - Setup Guide
echo ========================================
echo.
echo Step 1: Installing dependencies...
pip install -r requirements.txt
echo.
echo Step 2: Getting Gemini API Key
echo Open this link: https://makersuite.google.com/app/apikey
echo Copy your API key and paste it below when prompted
echo.
set /p API_KEY="Enter your Gemini API Key: "
setx GEMINI_API_KEY %API_KEY%
echo.
echo Step 3: API Key saved!
echo.
echo You can now run the game with:
echo   python main.py
echo.
pause
