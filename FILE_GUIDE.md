# 📚 File Guide - Murder Mystery Game

## 🎮 Game Files

### Core Game Files

| File | Purpose | Launch Command |
|------|---------|-----------------|
| `main.py` | Console version (text-based) | `python main.py` |
| `app.py` | Web version (Streamlit) | `streamlit run app.py` |
| `requirements.txt` | Python dependencies | `pip install -r requirements.txt` |

---

## 🪟 Launcher Files (Windows)

| File | Purpose |
|------|---------|
| `run_web.bat` | Quick launcher for web version |
| `SETUP_SIMPLE.bat` | One-click setup for dependencies |
| `setup.bat` | Original setup script |

**Just double-click any `.bat` file to use!**

---

## 📖 Documentation Files

### Main Guides

| File | Content | Best For |
|------|---------|----------|
| `README.md` | Complete overview of both versions | First time players |
| `COMPARISON.md` | Console vs Web comparison | Choosing which version |
| `WEB_QUICKSTART.md` | 30-second quick start for web | Fast learners |
| `STREAMLIT_GUIDE.md` | Detailed web version features | Web users |
| `QUICKSTART.md` | Quick start for console | Console users |
| `BEGINNER_GUIDE.md` | Beginner-friendly guide | New players |

### Technical Guides

| File | Content | Best For |
|------|---------|----------|
| `WEB_VERSION_GUIDE.md` | Deep dive into web features | Advanced web users |
| `SETUP.md` | Detailed setup instructions | Setup issues |

---

## 📊 Quick Reference

### What Should I Read First?

1. **New User?** → Read `README.md`
2. **Want Web Version?** → Read `WEB_QUICKSTART.md`
3. **Want Console?** → Read `QUICKSTART.md`
4. **Can't decide?** → Read `COMPARISON.md`
5. **Detailed Features?** → Read `WEB_VERSION_GUIDE.md`

### What Should I Run?

1. **First Time?**
   ```bash
   pip install -r requirements.txt
   streamlit run app.py  # OR python main.py
   ```

2. **Windows?**
   - Double-click `run_web.bat` for web
   - Run `python main.py` for console

3. **Again?**
   ```bash
   streamlit run app.py  # For web
   # OR
   python main.py  # For console
   ```

---

## 🎯 File Organization

```
Murder/
├── 🎮 GAME FILES
│   ├── main.py (Console game)
│   ├── app.py (Web game)
│   └── requirements.txt (Dependencies)
│
├── 🪟 LAUNCHERS
│   ├── run_web.bat (Launch web version)
│   ├── setup.bat (Full setup)
│   └── SETUP_SIMPLE.bat (Quick setup)
│
├── 📖 MAIN GUIDES
│   ├── README.md (Start here!)
│   ├── COMPARISON.md (Choose version)
│   ├── WEB_QUICKSTART.md (Fast web start)
│   ├── STREAMLIT_GUIDE.md (Web details)
│   ├── QUICKSTART.md (Console start)
│   └── BEGINNER_GUIDE.md (Beginner help)
│
└── 📚 TECHNICAL
    ├── WEB_VERSION_GUIDE.md (Web features)
    ├── SETUP.md (Setup details)
    └── FILE_GUIDE.md (This file!)
```

---

## 🚀 Quick Links

### To Play the Game:

**Web Version (Recommended):**
```bash
pip install -r requirements.txt
streamlit run app.py
```

**Console Version:**
```bash
pip install -r requirements.txt
python main.py
```

**Windows (Web):**
- Double-click `run_web.bat`

---

## 📋 File Contents Summary

### Game Logic (`main.py` & `app.py`)
- AI-powered content generation (Gemini)
- 3 suspects with unique profiles
- 8 clues with contradictions
- Scoring system (10 pts/contradiction, 25 bonus)
- 5 interrogation limit
- Detective theme and UI

### Dependencies (`requirements.txt`)
- google-generativeai ≥ 0.3.0
- streamlit ≥ 1.28.0

### Documentation (`README.md`)
- Feature overview
- Two version comparison
- Game mechanics
- How to play

### Web Guide (`WEB_VERSION_GUIDE.md`)
- UI elements explained
- Color scheme details
- Sidebar features
- Tab interface
- Responsive design
- Gameplay flow

### Comparison (`COMPARISON.md`)
- Feature table
- Performance metrics
- Choosing a version
- Setup comparison
- Pros and cons

### Quick Start (`WEB_QUICKSTART.md`)
- 30-second setup
- Game controls
- Scoring tips
- Troubleshooting

---

## 📝 Reading Guide by User Type

### I'm a Complete Beginner
1. Read: `README.md` (5 min)
2. Choose: Console or Web
3. Follow: `QUICKSTART.md` or `WEB_QUICKSTART.md` (2 min)
4. Install: `pip install -r requirements.txt` (2 min)
5. Play: `python main.py` or `streamlit run app.py`

### I Want the Web Version
1. Read: `WEB_QUICKSTART.md` (2 min)
2. Install: `pip install -r requirements.txt`
3. Run: `streamlit run app.py`
4. Explore: `WEB_VERSION_GUIDE.md` for details

### I Want the Console Version
1. Read: `QUICKSTART.md` (2 min)
2. Install: `pip install -r requirements.txt`
3. Run: `python main.py`

### I Want Everything
1. Read: `README.md`
2. Read: `COMPARISON.md`
3. Read: `WEB_VERSION_GUIDE.md`
4. Read: `WEB_QUICKSTART.md`
5. Try both versions!

### I'm a Developer
1. Check: `app.py` and `main.py`
2. Read: `WEB_VERSION_GUIDE.md`
3. Modify and customize!
4. Deploy web version to cloud!

---

## 🎯 File Purposes at a Glance

| Type | Files | Purpose |
|------|-------|---------|
| **Game** | main.py, app.py | The actual game code |
| **Setup** | requirements.txt | What to install |
| **Launch** | run_web.bat, setup.bat | Quick starters |
| **Guide** | README.md, QUICKSTART.md | How to get started |
| **Docs** | All .md files | Detailed information |

---

## 💾 Total File Count

- **Game files:** 3 (main.py, app.py, requirements.txt)
- **Launcher files:** 3 (.bat files)
- **Documentation:** 9 (.md files)
- **Total:** 15 files

---

## 🔄 How to Update

To update just the dependencies:
```bash
pip install --upgrade -r requirements.txt
```

To update Streamlit:
```bash
pip install --upgrade streamlit
```

To update Gemini API:
```bash
pip install --upgrade google-generativeai
```

---

## 📱 Mobile Support

- **Console Version:** No (terminal only)
- **Web Version:** Yes! (full mobile support)

For mobile, use:
```bash
streamlit run app.py
```

Then open on mobile browser at your computer's IP address!

---

## 🌍 Online Deployment

To deploy the web version online:

1. **Streamlit Cloud** (easiest):
   - Push `app.py` to GitHub
   - Deploy via Streamlit Cloud (free!)

2. **Heroku:**
   - Push code to Heroku
   - Add Procfile

3. **Any Web Server:**
   - Run on VPS or server
   - Use reverse proxy (nginx)

---

## 📞 Need Help?

- **Installation issues?** → See `SETUP.md`
- **Want quick start?** → See `WEB_QUICKSTART.md` or `QUICKSTART.md`
- **Want detailed info?** → See `WEB_VERSION_GUIDE.md`
- **Choosing version?** → See `COMPARISON.md`
- **Complete overview?** → See `README.md`

---

## ✅ Checklist Before Playing

- [ ] Python 3.8+ installed
- [ ] `pip install -r requirements.txt` completed
- [ ] Read the appropriate quick start guide
- [ ] API key ready (already hardcoded!)
- [ ] Internet connection active
- [ ] Browser ready (for web version)

---

**You're all set! Pick a version and start investigating!** 🕵️

