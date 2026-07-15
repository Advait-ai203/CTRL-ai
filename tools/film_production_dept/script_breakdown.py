# tools/film_production_dept/script_breakdown.py
import re

def analyze_scene_requirements(script_text: str) -> dict:
    """Scans scene text blocks to extract key assets, locations, and characters."""
    
    # Simple regex parsing for standard script elements
    sluglines = re.findall(r'(INT\.|EXT\.)\s+([A-Z0-9_\-\s]+)', script_text)
    props = re.findall(r'\[Prop:\s*([\w\s]+)\]', script_text, re.IGNORECASE)
    
    # Look for capitalized character names preceding dialogue blocks
    potential_characters = set(re.findall(r'\n([A-Z][A-Z\s]+)\n', script_text))
    cleaned_characters = [c.strip() for c in potential_characters if len(c.strip()) > 1]
    
    return {
        "locations_detected": [f"{s[0]} {s[1].strip()}" for s in sluglines],
        "props_required": list(set(props)),
        "characters_present": cleaned_characters
    }
