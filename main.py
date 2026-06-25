import random
import os
from dotenv import load_dotenv
load_dotenv()
import json
import google.generativeai as genai

# Get Gemini API Key from environment variable
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    print("❌ Error: GEMINI_API_KEY environment variable not set!")
    print("Please set it before running the game.")
    print("Example: set GEMINI_API_KEY=your_api_key_here")
    exit(1)

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

# Game state
interrogations_used = 0
max_interrogations = 5
detective_score = 0
suspects = []
clues = []
contradictions = {}
found_contradictions = []
victim_name = ""
murderer = None
CRIME_SCENE = ""


def generate_game_content():
    """Use Gemini AI to generate unique game content"""
    global suspects, clues, contradictions, victim_name, murderer, CRIME_SCENE
    
    print("\n" + "="*60)
    print("⏳ GENERATING YOUR MYSTERY CASE ⏳")
    print("="*60)
    print("\nUsing AI to create a unique murder mystery...")
    print("   • Generating victim...")
    print("   • Creating suspects...")
    print("   • Adding clues...")
    print("   • Setting up contradictions...")
    print("\nPlease wait...")
    
    # Prompt Gemini to generate the game content
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
        victim_name = game_data["victim"]
        suspects = game_data["suspects"]
        clues = game_data["clues"]
        murderer_index = game_data["murderer_index"]
        murderer = suspects[murderer_index]
        
        # Convert contradictions to match our format (string keys to int keys)
        contradictions_raw = game_data["contradictions"]
        contradictions.clear()
        for clue_idx_str, suspect_name in contradictions_raw.items():
            if suspect_name:  # Only add if there's a suspect name
                clue_idx = int(clue_idx_str)
                contradictions[clue_idx] = suspect_name
        
        # Create crime scene description
        CRIME_SCENE = f"""
The victim was found in their study at midnight.
Victim: {victim_name}
Location: {game_data["crime_location"]}
Time: Around {game_data["crime_time"]}
Evidence: {game_data["crime_evidence"]}
"""
        
        print("\n✅ Mystery case generated successfully!")
        print("="*60)
        return True
        
    except json.JSONDecodeError as e:
        print(f"\n⚠️  Error generating case: {e}")
        print("Using default case instead...")
        return False
    except Exception as e:
        print(f"\n⚠️  Error: {e}")
        print("Using default case instead...")
        return False


def use_default_content():
    """Use hardcoded content if Gemini fails"""
    global suspects, clues, contradictions, victim_name, murderer, CRIME_SCENE
    
    victim_name = "Robert Martinez"
    
    suspects = [
        {
            "name": "Alice Johnson",
            "profession": "Banker",
            "motive": "Financial dispute",
            "alibi": "I was at the coffee shop",
        },
        {
            "name": "Bob Smith",
            "profession": "Chef",
            "motive": "Love triangle",
            "alibi": "I was cooking at home",
        },
        {
            "name": "Carol Davis",
            "profession": "Lawyer",
            "motive": "Revenge",
            "alibi": "I was working late at the office",
        }
    ]
    
    clues = [
        "A muddy footprint was found near the crime scene",
        "A chef's knife was discovered in the trash",
        "The victim's calendar showed a meeting with Alice",
        "Bob's apartment has recent financial troubles",
        "Carol's phone records show a call to the victim at 10:30 PM",
        "Expensive jewelry matching Bob's description was seen at a pawn shop",
        "Alice has a solid alibi at the coffee shop (security footage)",
        "Carol's office was empty that night - no one saw her"
    ]
    
    contradictions = {
        0: "Bob Smith",
        1: "Bob Smith",
        2: "Alice Johnson",
        4: "Carol Davis",
        7: "Carol Davis"
    }
    
    murderer = random.choice(suspects)
    
    CRIME_SCENE = f"""
The victim was found in their study at midnight.
Victim: {victim_name}
Location: Downtown apartment, 5th floor
Time: Around 11:00 PM
Evidence: Signs of a struggle, stolen jewelry
"""


def display_welcome():
    """Display the game welcome message"""
    print("\n" + "="*60)
    print(" "*15 + "MURDER MYSTERY INVESTIGATION")
    print("="*60)
    print("\n🕵️  A CRIME HAS BEEN COMMITTED!")
    print("\nYou are a detective solving a murder case.")
    print("You have LIMITED resources - use them wisely!")
    print("\n📋 YOUR MISSION:")
    print("  • Interrogate 3 suspects (max 5 interrogations)")
    print("  • Review clues and find contradictions")
    print("  • Find the killer before time runs out")
    print("  • Make your accusation!")
    print("\n💡 TIPS FOR BEGINNERS:")
    print("  • Listen carefully to each suspect's alibi")
    print("  • Match clues against the alibis")
    print("  • Contradictions = Points! (10 points each)")
    print("  • Correct accusation = 25 bonus points")
    print("  • Wrong accusation = Game Over!")
    print("\n" + "="*60)
    print("Let's begin! Press Enter to see the crime scene...")
    input()
    print()


def display_crime_scene():
    """Display the crime scene information"""
    print("\n" + "="*60)
    print("🔍 CRIME SCENE REPORT 🔍")
    print("="*60)
    print(CRIME_SCENE)
    print("="*60)


def display_clues():
    """Display all discovered clues"""
    print("\n" + "="*60)
    print("📋 EVIDENCE & CLUES 📋")
    print("="*60)
    
    if not clues:
        print("No clues found yet.")
    else:
        print("\nClues collected at the crime scene:\n")
        for i, clue in enumerate(clues, 1):
            print(f"{i}. {clue}")
        print("\n💡 TIP: Try to match these clues against each suspect's alibi!")
        print("   If a clue contradicts what they claim, you've found evidence!")
    
    print("\n" + "="*60)


def display_suspects():
    """Display all suspects"""
    print("\n" + "-"*60)
    print("SUSPECTS IN THE CASE")
    print("-"*60)
    for i, suspect in enumerate(suspects, 1):
        print(f"\n{i}. {suspect['name'].upper()}")
        print(f"   Profession: {suspect['profession']}")
        print(f"   Possible Motive: {suspect['motive']}")
    print("\n" + "-"*60)


def interrogate_suspect(suspect_index):
    """Interrogate a suspect and display their information"""
    global interrogations_used, detective_score
    
    if interrogations_used >= max_interrogations:
        print("\n⚠️  You've used all your interrogations!")
        print("You must make an accusation now!")
        return False
    
    suspect = suspects[suspect_index - 1]
    print("\n" + "="*60)
    print(f"INTERROGATING: {suspect['name'].upper()}")
    print("="*60)
    print(f"\n📋 Details:")
    print(f"   Profession: {suspect['profession']}")
    print(f"   Possible Motive: {suspect['motive']}")
    print(f"\n💬 Their Alibi:")
    print(f"   \"{suspect['alibi']}\"")
    
    # Check for contradictions with clues
    found_new_contradiction = False
    for clue_index, contradicted_suspect in contradictions.items():
        if contradicted_suspect == suspect['name']:
            contradiction_tuple = (suspect['name'], clue_index)
            if contradiction_tuple not in found_contradictions:
                print(f"\n🚨 CONTRADICTION DETECTED! 🚨")
                print(f"   Clue #{clue_index + 1} contradicts their story!")
                print(f"   Clue: \"{clues[clue_index]}\"")
                print(f"\n   ✓ You earned 10 points for finding this contradiction!")
                detective_score += 10
                found_contradictions.append(contradiction_tuple)
                found_new_contradiction = True
    
    if not found_new_contradiction:
        if suspect == murderer:
            print(f"\n🤔 Hmm... their story seems a bit odd, but you're not sure why...")
        else:
            print(f"\n✓ Their story seems consistent with the evidence.")
    
    print("\n" + "="*60)
    interrogations_used += 1
    print(f"Interrogations used: {interrogations_used}/{max_interrogations}")
    return True


def make_accusation():
    """Allow player to make an accusation"""
    global detective_score
    
    print("\n" + "="*60)
    print("TIME TO MAKE YOUR ACCUSATION!")
    print("="*60)
    print("\nChoose who the murderer is:")
    display_suspects()
    
    while True:
        try:
            choice = int(input("\nEnter the number of the suspect you accuse (1-3): "))
            if 1 <= choice <= 3:
                break
            else:
                print("❌ Please enter 1, 2, or 3")
        except ValueError:
            print("❌ Please enter a valid number")
    
    accused = suspects[choice - 1]
    
    if accused == murderer:
        # Award bonus points for correct accusation
        detective_score += 25
        print("\n" + "🎉"*30)
        print("\n" + " "*15 + "CASE SOLVED! 🎉")
        print("\n" + "🎉"*30)
        print(f"\n✅ CORRECT! The murderer is {murderer['name'].upper()}!")
        print(f"\n📋 Case Details:")
        print(f"   Profession: {murderer['profession']}")
        print(f"   Motive: {murderer['motive']}")
        print(f"   Alibi was: \"{murderer['alibi']}\"")
        print(f"\n🏆 FINAL DETECTIVE SCORE: {detective_score} points")
        print("\nExcellent detective work! You solved the case! 🕵️")
        print("\n" + "="*60)
        return True
    else:
        print("\n" + "❌"*30)
        print("\n" + " "*20 + "CASE FAILED! ❌")
        print("\n" + "❌"*30)
        print(f"\n❌ WRONG! The real murderer was {murderer['name'].upper()}!")
        print(f"\n📋 The Actual Murderer:")
        print(f"   Profession: {murderer['profession']}")
        print(f"   Motive: {murderer['motive']}")
        print(f"\n You accused: {accused['name']}")
        print(f"   Score before accusation: {detective_score - (detective_score - 10 * len(found_contradictions))} points")
        print(f"   Final score: {detective_score} points")
        print("\nBetter luck next time! Try again soon! 🔍")
        print("\n" + "="*60)
        return False


def main():
    """Main game loop"""
    global interrogations_used, detective_score
    
    # Generate unique game content using Gemini AI
    success = generate_game_content()
    if not success:
        use_default_content()
    
    # Reset game state
    interrogations_used = 0
    detective_score = 0
    found_contradictions.clear()
    
    display_welcome()
    display_crime_scene()
    
    game_won = False
    
    while interrogations_used < max_interrogations and not game_won:
        print(f"\n📊 INVESTIGATION STATUS:")
        print(f"   Interrogations: {interrogations_used}/{max_interrogations}")
        print(f"   Detective Score: {detective_score} points")
        print(f"   Contradictions Found: {len(found_contradictions)}")
        
        print("\n" + "="*60)
        print("WHAT WOULD YOU LIKE TO DO?")
        print("="*60)
        print("\n1️⃣  INTERROGATE a suspect")
        print("   └─ Question a suspect about their alibi")
        print("\n2️⃣  VIEW CLUES")
        print("   └─ Review the evidence collected at the crime scene")
        print("\n3️⃣  VIEW CRIME SCENE")
        print("   └─ Review details of where the crime happened")
        print("\n4️⃣  MAKE ACCUSATION")
        print("   └─ Accuse the suspect you believe is the murderer!")
        print("\n5️⃣  QUIT GAME")
        print("   └─ Exit the investigation")
        print("\n" + "="*60)
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == "1":
            display_suspects()
            try:
                suspect_num = int(input("\nEnter the number of the suspect to interrogate (1-3): "))
                if 1 <= suspect_num <= 3:
                    interrogate_suspect(suspect_num)
                else:
                    print("❌ Please choose 1, 2, or 3")
            except ValueError:
                print("❌ Please enter a valid number")
        
        elif choice == "2":
            display_clues()
        
        elif choice == "3":
            display_crime_scene()
        
        elif choice == "4":
            game_won = make_accusation()
            if not game_won:
                # Wrong accusation, game over
                break
        
        elif choice == "5":
            print("\n👋 You quit the investigation. Case left unsolved!")
            print(f"Your final score: {detective_score} points")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1, 2, 3, 4, or 5")
    
    if not game_won and interrogations_used >= max_interrogations:
        print("\n⏰ TIME'S UP!")
        print("You ran out of interrogations before solving the case.")
        print(f"The murderer was: {murderer['name']} - {murderer['profession']}")
        print(f"Final Detective Score: {detective_score} points")


if __name__ == "__main__":
    main()
