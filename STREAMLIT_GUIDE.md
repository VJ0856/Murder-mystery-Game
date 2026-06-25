# 🌐 Murder Mystery - Streamlit Web Version

A beautiful, detective-themed web application for playing the Murder Mystery game!

## 🚀 Quick Start

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Streamlit App
```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## 🎮 Features

### 🕵️ Detective-Themed UI
- Dark, professional design perfect for a detective theme
- Red and dark blue color scheme (classic detective noir)
- Text shadows and styling for authentic detective feel
- Responsive layout works on all screen sizes

### 📊 Sidebar Dashboard
- Real-time score display
- Investigation status (interrogations used)
- Contradiction counter
- Game controls (Start/New Investigation)
- Professional status metrics

### 🔵 Suspect Cards
- Large, readable suspect information cards
- Shows profession, motive, and alibi
- Arranged in an easy-to-read 3-column layout
- Styled with detective theme colors

### 📋 Clue Display
- All clues displayed in an organized list
- Each clue has visual styling
- Easy to review while interrogating
- Color-coded for quick scanning

### 🎯 Tabbed Interface
- **Crime Scene Tab** - View full crime details
- **Suspects Tab** - Interrogate each suspect
- **Clues Tab** - Review all evidence
- **Accusation Tab** - Make your final accusation

## 🎮 How to Play

1. **Start Investigation** - Click "START NEW INVESTIGATION" button
2. **Review Evidence** - Check crime scene and clues
3. **Interrogate Suspects** - Click interrogate buttons to question suspects
4. **Find Contradictions** - Match clues against alibis
5. **Make Accusation** - After 5 interrogations, accuse the murderer
6. **Check Results** - See if you solved the case!

## 🎨 UI Elements

### Detective Theme Colors
- **Primary Black:** `#1a1a2e`
- **Secondary Dark:** `#16213e`
- **Accent Red:** `#e94560`
- **Text Light:** `#f0f0f0`

### Custom Styled Components
- **Suspect Cards** - Gradient background with red borders
- **Clue Items** - Red left border with subtle background
- **Score Box** - Red gradient with white text
- **Alerts** - Color-coded for success (green) and failures (red)

## 📱 Responsive Design
- Works on desktop, tablet, and mobile
- Adapts to different screen sizes
- Touch-friendly buttons
- Scrollable content areas

## 💡 Game Mechanics

### Scoring System
- **+10 points** - Each contradiction found
- **+25 bonus points** - Correct final accusation
- **0 points** - Wrong accusation

### Interrogations
- Maximum 5 interrogations per game
- Track interrogations in sidebar
- Can interrogate same suspect multiple times
- Status shown in real-time

### Contradictions
- Automatic detection when interrogating
- Visual alerts with clue details
- Immediate point feedback
- Counter in sidebar

## 🌟 Advantages Over Console Version

✨ **Visual Appeal** - Detective-themed UI instead of text
✨ **Organization** - Tabs and cards for better structure
✨ **Interaction** - Buttons and clickable elements
✨ **Feedback** - Visual alerts and animations
✨ **Accessibility** - Easier to read and navigate
✨ **Professional** - Looks like a real detective app!

## 🔧 Technical Features

- **Streamlit Framework** - Lightweight web app framework
- **Session State** - Game progress persists during session
- **Responsive Design** - Works on all devices
- **Custom CSS** - Detective-themed styling
- **AI Integration** - Gemini AI for content generation
- **Dynamic Content** - Unique case every game

## 📊 Sidebar Status

The sidebar always shows:
- Current detective score
- Interrogations used (0/5)
- Contradictions found count
- Game control buttons
- Professional styling

## 🎲 Every Game is Different

Each game generates:
- New victim name
- Different suspects with unique profiles
- Fresh professions and motives
- Original alibis
- 8 brand new clues
- Unique logical contradictions

**No two games are ever the same!**

## ⚡ Performance

- Fast loading times
- AI generation takes 2-3 seconds
- Smooth interactions
- Responsive UI updates

## 🎯 Game Flow

```
START INVESTIGATION
    ↓
REVIEW CRIME SCENE
    ↓
INTERROGATE SUSPECTS (repeat up to 5 times)
    ↓
FIND CONTRADICTIONS
    ↓
MAKE ACCUSATION
    ↓
CHECK RESULTS (Won/Lost)
```

## 💬 User Feedback

- Immediate contradiction alerts
- Score updates in real-time
- Visual success/failure messages
- Helpful tips and guidance
- Professional tone throughout

## 🎉 End Game

After accusation, see:
- Whether you were correct
- The murderer's details
- Your final score
- Encouragement to play again

---

Enjoy the web version of Murder Mystery! It's more immersive and visually appealing than the console version. 🕵️
