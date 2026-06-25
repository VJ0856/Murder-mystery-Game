import streamlit as st
import json
import random
import os
import google.genai as genai

# Page configuration
st.set_page_config(
    page_title="Murder Mystery Investigation",
    page_icon="🕵️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Get Gemini API Key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    st.error("❌ API Key Missing! Please set the GEMINI_API_KEY environment variable.")
    st.stop()

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Custom CSS for detective theme
st.markdown("""
<style>
    /* Detective Theme Colors */
    :root {
        --primary-color: #1a1a2e;
        --secondary-color: #16213e;
        --accent-color: #e94560;
        --text-light: #f0f0f0;
    }
    
    /* Main background */
    .main {
        background-color: #0f0f1e;
        color: #f0f0f0;
    }
    
    /* Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1a1a2e;
    }
    
    /* Headers */
    h1, h2, h3 {
        color: #e94560;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    
    /* Cards */
    .suspect-card {
        background: linear-gradient(135deg, #16213e 0%, #0f3460 100%);
        border: 2px solid #e94560;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 6px rgba(233, 69, 96, 0.2);
    }
    
    .clue-item {
        background: linear-gradient(135deg, #16213e 0%, #0f3460 100%);
        border-left: 4px solid #e94560;
        padding: 15px;
        margin: 10px 0;
        border-radius: 5px;
    }
    
    .score-box {
        background: linear-gradient(135deg, #e94560 0%, #c93a50 100%);
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        color: white;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .contradiction-alert {
        background-color: #d32f2f;
        border: 2px solid #ff5252;
        color: white;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    
    .success-alert {
        background-color: #388e3c;
        border: 2px solid #66bb6a;
        color: white;
        padding: 15px;
        border-radius: 5px;
        margin: 10px 0;
    }
    
    /* Buttons */
    .stButton > button {
        background-color: #e94560;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: bold;
    }
    
    .stButton > button:hover {
        background-color: #c93a50;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
    st.session_state.suspects = []
    st.session_state.clues = []
    st.session_state.contradictions = {}
    st.session_state.victim_name = ""
    st.session_state.murderer = None
    st.session_state.crime_scene = ""
    st.session_state.interrogations_used = 0
    st.session_state.detective_score = 0
    st.session_state.found_contradictions = []
    st.session_state.interrogated_suspects = set()
    st.session_state.game_won = None

def generate_game_content():
    """Generate unique murder mystery content using Gemini AI"""
    prompt = """Generate a unique murder mystery game in JSON format. Return ONLY valid JSON, nothing else.

The JSON must have this exact structure:
{
  "victim": "victim's full name",
  "crime_location": "specific location description",
  "crime_time": "time of crime",
  "crime_evidence": "main evidence at scene",
  "suspects": [
    {
      "name": "suspect name",
      "profession": "their profession",
      "motive": "reason they might have done it",
      "alibi": "their alibi for the crime"
    },
    {
      "name": "suspect name",
      "profession": "their profession", 
      "motive": "reason they might have done it",
      "alibi": "their alibi for the crime"
    },
    {
      "name": "suspect name",
      "profession": "their profession",
      "motive": "reason they might have done it", 
      "alibi": "their alibi for the crime"
    }
  ],
  "clues": [
    "specific clue related to crime scene or evidence",
    "clue that might contradict a suspect's alibi",
    "clue about weapon or method",
    "clue about suspect's movements",
    "clue about victim's activities",
    "clue about financial or personal evidence",
    "clue that supports one alibi",
    "clue that contradicts another alibi"
  ],
  "contradictions": {
    "0": "suspect name if clue 0 contradicts them",
    "1": "suspect name if clue 1 contradicts them",
    "2": "suspect name if clue 2 contradicts them",
    "3": "suspect name if clue 3 contradicts them",
    "4": "suspect name if clue 4 contradicts them",
    "7": "suspect name if clue 7 contradicts them"
  },
  "murderer_index": 0
}

Make it creative, unique, and interesting. Ensure contradictions are logical and make sense."""
    
    try:
        response = model.generate_content(prompt)
        response_text = response.text.strip()
        
        # Remove markdown code blocks if present
        if response_text.startswith("```"):
            response_text = response_text.split("```")[1]
            if response_text.startswith("json"):
                response_text = response_text[4:]
        if response_text.endswith("```"):
            response_text = response_text[:-3]
        
        game_data = json.loads(response_text)
        
        # Parse the generated content
        st.session_state.victim_name = game_data["victim"]
        st.session_state.suspects = game_data["suspects"]
        st.session_state.clues = game_data["clues"]
        murderer_index = game_data["murderer_index"]
        st.session_state.murderer = st.session_state.suspects[murderer_index]
        
        # Parse contradictions
        contradictions_raw = game_data["contradictions"]
        st.session_state.contradictions.clear()
        for clue_idx_str, suspect_name in contradictions_raw.items():
            if suspect_name:
                clue_idx = int(clue_idx_str)
                st.session_state.contradictions[clue_idx] = suspect_name
        
        # Create crime scene description
        st.session_state.crime_scene = f"""
**Victim:** {st.session_state.victim_name}
**Location:** {game_data["crime_location"]}
**Time of Crime:** Around {game_data["crime_time"]}
**Main Evidence:** {game_data["crime_evidence"]}
"""
        return True
        
    except Exception as e:
        st.error(f"Error generating case: {e}")
        return False

def display_suspect_cards():
    """Display suspects as cards"""
    st.subheader("🔍 SUSPECTS")
    
    cols = st.columns(3)
    for i, suspect in enumerate(st.session_state.suspects):
        with cols[i]:
            st.markdown(f"""
            <div class="suspect-card">
                <h3>{suspect['name']}</h3>
                <p><strong>Profession:</strong> {suspect['profession']}</p>
                <p><strong>Motive:</strong> {suspect['motive']}</p>
                <p><strong>Alibi:</strong> "{suspect['alibi']}"</p>
            </div>
            """, unsafe_allow_html=True)

def display_clues():
    """Display clues in a formatted way"""
    st.subheader("📋 EVIDENCE & CLUES")
    
    if st.session_state.clues:
        for i, clue in enumerate(st.session_state.clues, 1):
            st.markdown(f"""
            <div class="clue-item">
                <strong>Clue #{i}:</strong> {clue}
            </div>
            """, unsafe_allow_html=True)

def display_crime_scene():
    """Display crime scene details"""
    st.subheader("🔎 CRIME SCENE REPORT")
    st.markdown(st.session_state.crime_scene)

def interrogate_suspect(suspect_index):
    """Interrogate a suspect"""
    suspect = st.session_state.suspects[suspect_index]
    
    st.session_state.interrogations_used += 1
    st.session_state.interrogated_suspects.add(suspect['name'])
    
    # Display interrogation results
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="suspect-card">
            <h3>INTERROGATING: {suspect['name'].upper()}</h3>
            <p><strong>Profession:</strong> {suspect['profession']}</p>
            <p><strong>Possible Motive:</strong> {suspect['motive']}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="suspect-card">
            <h3>THEIR ALIBI</h3>
            <p style="font-style: italic;">"{suspect['alibi']}"</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Check for contradictions
    found_new_contradiction = False
    for clue_index, contradicted_suspect in st.session_state.contradictions.items():
        if contradicted_suspect == suspect['name']:
            contradiction_tuple = (suspect['name'], clue_index)
            if contradiction_tuple not in st.session_state.found_contradictions:
                st.markdown(f"""
                <div class="contradiction-alert">
                    <strong>🚨 CONTRADICTION DETECTED! 🚨</strong><br>
                    Clue #{clue_index + 1} contradicts their alibi!<br>
                    <em>"{st.session_state.clues[clue_index]}"</em><br>
                    <strong>✓ You earned 10 points!</strong>
                </div>
                """, unsafe_allow_html=True)
                st.session_state.detective_score += 10
                st.session_state.found_contradictions.append(contradiction_tuple)
                found_new_contradiction = True
    
    if not found_new_contradiction:
        if suspect == st.session_state.murderer:
            st.info("🤔 Hmm... their story seems a bit odd, but you're not sure why...")
        else:
            st.success("✓ Their story seems consistent with the evidence.")

def main():
    # Header
    st.markdown("<h1>🕵️ MURDER MYSTERY INVESTIGATION</h1>", unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.markdown("<h2>📊 DETECTIVE STATUS</h2>", unsafe_allow_html=True)
        
        # Score display
        st.markdown(f"""
        <div class="score-box">
            Score: {st.session_state.detective_score} points
        </div>
        """, unsafe_allow_html=True)
        
        # Game stats
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Interrogations", f"{st.session_state.interrogations_used}/5")
        with col2:
            st.metric("Contradictions", len(st.session_state.found_contradictions))
        
        st.divider()
        
        # Game controls
        st.markdown("<h3>⚙️ GAME CONTROLS</h3>", unsafe_allow_html=True)
        
        if not st.session_state.game_started:
            if st.button("🎮 START NEW INVESTIGATION", use_container_width=True):
                with st.spinner("🔄 Generating mystery case..."):
                    if generate_game_content():
                        st.session_state.game_started = True
                        st.session_state.interrogations_used = 0
                        st.session_state.detective_score = 0
                        st.session_state.found_contradictions = []
                        st.session_state.interrogated_suspects = set()
                        st.session_state.game_won = None
                        st.rerun()
        else:
            if st.button("🔄 NEW INVESTIGATION", use_container_width=True):
                st.session_state.game_started = False
                st.rerun()
            
            if st.session_state.interrogations_used >= 5:
                if st.button("🎯 MAKE ACCUSATION", use_container_width=True, type="primary"):
                    st.session_state.show_accusation = True
                    st.rerun()
    
    # Main content area
    if not st.session_state.game_started:
        st.markdown("""
        <div style="text-align: center; padding: 40px;">
            <h2>Welcome, Detective!</h2>
            <p>A crime has been committed. It's your job to solve it.</p>
            <p>Use the controls on the left to begin your investigation.</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Tab interface for game sections
        tab1, tab2, tab3, tab4 = st.tabs(["📍 Crime Scene", "👥 Suspects", "🔍 Clues", "⚖️ Accusation"])
        
        with tab1:
            display_crime_scene()
        
        with tab2:
            st.subheader("INTERROGATE SUSPECTS")
            display_suspect_cards()
            
            st.divider()
            st.markdown("### Select a suspect to interrogate:")
            
            if st.session_state.interrogations_used < 5:
                cols = st.columns(3)
                for i, suspect in enumerate(st.session_state.suspects):
                    with cols[i]:
                        if st.button(
                            f"🎤 Interrogate\n{suspect['name']}", 
                            use_container_width=True,
                            key=f"interrogate_{i}"
                        ):
                            with st.spinner(f"Interrogating {suspect['name']}..."):
                                interrogate_suspect(i)
            else:
                st.warning("⚠️ You've used all your interrogations! Make your accusation in the Accusation tab.")
        
        with tab3:
            display_clues()
            st.info("💡 TIP: Try to match these clues against each suspect's alibi. If a clue contradicts what they claim, you've found evidence!")
        
        with tab4:
            st.subheader("🎯 MAKE YOUR ACCUSATION")
            
            if st.session_state.interrogations_used >= 5:
                st.markdown("You've analyzed all the evidence. Now it's time to make your accusation!")
                st.divider()
                
                # Display suspects for accusation
                st.markdown("### Who is the murderer?")
                cols = st.columns(3)
                for i, suspect in enumerate(st.session_state.suspects):
                    with cols[i]:
                        if st.button(
                            f"⚖️ ACCUSE\n{suspect['name']}", 
                            use_container_width=True,
                            key=f"accuse_{i}"
                        ):
                            # Make accusation
                            if suspect == st.session_state.murderer:
                                st.session_state.detective_score += 25
                                st.session_state.game_won = True
                                st.balloons()
                                st.markdown(f"""
                                <div class="success-alert">
                                    <h2>🎉 CASE SOLVED! 🎉</h2>
                                    <p><strong>CORRECT!</strong> The murderer is {st.session_state.murderer['name'].upper()}!</p>
                                    <p><strong>Profession:</strong> {st.session_state.murderer['profession']}</p>
                                    <p><strong>Motive:</strong> {st.session_state.murderer['motive']}</p>
                                    <p><strong>Final Detective Score:</strong> {st.session_state.detective_score} points</p>
                                    <p>Excellent detective work! You solved the case! 🕵️</p>
                                </div>
                                """, unsafe_allow_html=True)
                            else:
                                st.session_state.game_won = False
                                st.markdown(f"""
                                <div class="contradiction-alert">
                                    <h2>❌ CASE FAILED! ❌</h2>
                                    <p><strong>WRONG!</strong> The real murderer was {st.session_state.murderer['name'].upper()}!</p>
                                    <p><strong>Profession:</strong> {st.session_state.murderer['profession']}</p>
                                    <p><strong>Motive:</strong> {st.session_state.murderer['motive']}</p>
                                    <p><strong>You Accused:</strong> {suspect['name']}</p>
                                    <p><strong>Final Score:</strong> {st.session_state.detective_score} points</p>
                                    <p>Better luck next time! Try again soon! 🔍</p>
                                </div>
                                """, unsafe_allow_html=True)
            else:
                st.warning(f"⚠️ You need to use more interrogations before making an accusation. ({st.session_state.interrogations_used}/5 used)")

if __name__ == "__main__":
    main()
