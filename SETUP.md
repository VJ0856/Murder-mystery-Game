# Quick Start Guide

## For Windows Users (Easiest Method)

1. **Run the setup batch file:**
   ```
   setup.bat
   ```
   This will:
   - Install required packages
   - Prompt you to enter your Gemini API key
   - Save the key automatically

2. **Start playing:**
   ```
   python main.py
   ```

---

## For Manual Setup (All Platforms)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Get Gemini API Key

1. Visit https://makersuite.google.com/app/apikey
2. Click "Create API Key"
3. Copy the key (looks like: `AIzaSy...`)

### Step 3: Set Environment Variable

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY = YOUR_API_KEY_HERE
```

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=YOUR_API_KEY_HERE

**Mac/Linux:**
```bash
export GEMINI_API_KEY="YOUR_API_KEY_HERE
```

### Step 4: Run the Game
```bash
python main.py
```

---

## Troubleshooting

**"ERROR: GEMINI_API_KEY environment variable not set!"**
- Make sure you've set the environment variable correctly
- Restart your terminal/command prompt after setting the variable

**Game falls back to default content**
- Check your internet connection
- Verify your API key is correct
- Gemini API might be temporarily unavailable

**"ModuleNotFoundError: No module named 'google'"**
- Run: `pip install -r requirements.txt`

---

## What's Different Each Game?

- ✨ Different victim
- 🕵️ Three new suspects with unique professions
- 💀 Unique motivations and alibis
- 🔍 8 brand new clues
- 🎯 Logical contradictions between clues and alibis
- 🎲 Random murderer selection from the suspects

Every game is completely unique!
