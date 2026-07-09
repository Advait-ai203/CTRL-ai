# tools/startup_founder_dept/pitch_deck_generator.py
# Outlines, builds, and writes operational slide structures for investments

import json
import os

def output_pitch_structure(venture_name: str, problem: str, solution: str, target_market: str) -> str:
    """Generates a presentation roadmap configuration file."""
    deck_dir = "./generated_assets/business_decks"
    os.makedirs(deck_dir, exist_ok=True)
    
    deck_template = {
        "company": venture_name,
        "slides": [
            {"slide_id": 1, "header": venture_name, "content": "Elevator Focus Strategy"},
            {"slide_id": 2, "header": "The Market Disruption", "content": problem},
            {"slide_id": 3, "header": "The Operational Vector", "content": solution},
            {"slide_id": 4, "header": "Demographic Capture Strategy", "content": target_market}
        ]
    }
    
    file_path = os.path.join(deck_dir, f"{venture_name.lower()}_pitch_blueprint.json")
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(deck_template, f, indent=4)
        return f"💼 **Strategic Pitch Matrix Initialized:** Slide layout file mapped to `{file_path}`"
    except Exception as e:
        return f"⚠️ Structural Save Error: {str(e)}"
