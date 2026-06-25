# 🔐 API Key Setup Guide

## Step 1: Get Your API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikeys)
2. Click "Create API Key"
3. Copy your API key

## Step 2: Set Up Environment Variable

### Option A: Windows (Easiest)

**Set temporarily (current session only):**
```powershell
$env:GEMINI_API_KEY=YOUR_API_KEY_HERE
```

**Set permanently (all sessions):**
1. Open **Settings** → **System** → **Advanced system settings**
2. Click **Environment Variables**
3. Click **New** under User variables
4. Variable name: `GEMINI_API_KEY`
5. Variable value: `your_api_key_here`
6. Click OK, restart terminal

**Or use this PowerShell command:**
```powershell
[Environment]::SetEnvironmentVariable("GEMINI_API_KEY", "your_api_key_here", "User")
```

### Option B: Linux / macOS

**Set temporarily:**
```bash
export GEMINI_API_KEY="your_api_key_here"
```

**Set permanently (add to ~/.bashrc or ~/.zshrc):**
```bash
echo 'export GEMINI_API_KEY="your_api_key_here"' >> ~/.bashrc
source ~/.bashrc
```

### Option C: Use .env File (Local Only)

1. Copy `.env.example` to `.env`
2. Edit `.env` and add your API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
3. Install python-dotenv:
   ```bash
   pip install python-dotenv
   ```

## Step 3: Verify It Works

### For Web Version:
```bash
streamlit run app.py
```

### For Console Version:
```bash
python main.py
```

If you see the game start, your API key is set correctly! ✅

---

## 🔒 Important Security Notes

✅ **DO:**
- Keep your `.env` file private (it's in .gitignore)
- Use environment variables in production
- Regenerate keys if accidentally exposed
- Never commit `.env` to GitHub

❌ **DON'T:**
- Hardcode API keys in source files
- Share your API key publicly
- Commit `.env` to GitHub
- Put API keys in version control

---

## 🐛 Troubleshooting

**Error: "API Key Missing!"**
→ You haven't set the GEMINI_API_KEY environment variable yet

**Error: "Invalid API key"**
→ Your API key is invalid or expired. Get a new one from [Google AI Studio](https://aistudio.google.com/app/apikeys)

**Game works locally but not on GitHub**
→ Correct! Keep the API key local only. It's safe to upload the code to GitHub now.

---

## 📤 Now You Can Upload to GitHub!

Your code is now ready for GitHub:
- ✅ No API key in source files
- ✅ `.gitignore` prevents `.env` upload
- ✅ `.env.example` shows what's needed
- ✅ Clean, safe repository

```bash
git add .
git commit -m "Murder Mystery Game - Hide API key"
git push origin main
```

---

## 🎮 Running After Upload

When someone clones your repo from GitHub:

1. Clone the repo
2. Set GEMINI_API_KEY environment variable locally
3. Run the game!

```bash
git clone your-repo
export GEMINI_API_KEY=YOUR_API_KEY_HERE
streamlit run app.py
```

Perfect! 🎉
