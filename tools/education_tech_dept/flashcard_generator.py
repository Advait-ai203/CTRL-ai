# tools/education_tech_dept/flashcard_generator.py
import json
import os

def compile_flashcard_deck(deck_name: str, terms_and_definitions: dict) -> str:
    """Saves a dictionary of terms into a structured JSON study deck."""
    target_dir = "./generated_assets/research_reports/study_decks"
    os.makedirs(target_dir, exist_ok=True)
    
    deck = []
    for term, definition in terms_and_definitions.items():
        deck.append({"front": term, "back": definition, "mastery_level": 0})
        
    file_path = os.path.join(target_dir, f"{deck_name.replace(' ', '_').lower()}.json")
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(deck, f, indent=4)
        
    return f"🗂️ **Flashcard Matrix Compiled:** Deck '{deck_name}' saved with {len(deck)} cards at `{file_path}`."
