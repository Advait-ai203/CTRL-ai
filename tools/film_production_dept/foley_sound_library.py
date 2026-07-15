# tools/film_production_dept/foley_sound_library.py

def get_audio_track_spec(category: str, intensity: str = "medium") -> str:
    """Retrieves standard mixing variables for ambient or action sound designs."""
    
    library = {
        "footsteps": f"Low-frequency impact transients, {intensity} resonance filtering.",
        "sci-fi": f"Synthesized modular sweeps, panning modulation, {intensity} echo variance.",
        "horror": f"High-frequency string dissonances, low sub-bass drones.",
        "ambient": "Constant low-gain noise environment profile."
    }
    
    spec = library.get(category.lower(), "Standard balanced sound profile.")
    
    return f"""
    🔊 **Foley Matrix Profile [{category.upper()}]:**
    - Synthesis Instruction: {spec}
    - Capture Method: Specialized dynamic directional array.
    """
