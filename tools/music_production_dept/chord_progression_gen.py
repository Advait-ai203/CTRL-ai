# tools/music_production_dept/chord_progression_gen.py

def generate_progression(key: str, mood: str) -> str:
    """Constructs harmonic chord progressions based on scale degrees and mood."""
    
    # Generic relative mappings for structural demonstration
    if mood.lower() == "sad":
        # i - VI - III - VII (Minor)
        progression = f"{key}m - {key}maj(VI) - {key}maj(III) - {key}maj(VII)"
        theory = "i - VI - III - VII"
    elif mood.lower() == "jazz":
        # ii - V - I
        progression = f"{key}m7 - {key}7 - {key}maj7"
        theory = "ii7 - V7 - Imaj7"
    else:
        # Standard Pop: I - V - vi - IV
        progression = f"{key} - {key}(V) - {key}m(vi) - {key}(IV)"
        theory = "I - V - vi - IV"
        
    return f"""
    🎵 **Harmonic Progression Matrix:**
    - Root Key: {key}
    - Aesthetic: {mood.capitalize()}
    - Theoretical Structure: {theory}
    
    **Chords to play:** `{progression}`
    """
