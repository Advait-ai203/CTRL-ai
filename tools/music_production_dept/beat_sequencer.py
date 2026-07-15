# tools/music_production_dept/beat_sequencer.py

def generate_drum_pattern(genre: str = "lofi") -> str:
    """Builds a 16-step grid sequencer pattern based on genre."""
    
    if genre.lower() == "lofi":
        kick  = "[x] [ ] [ ] [ ] [ ] [ ] [x] [ ] [x] [ ] [ ] [ ] [ ] [ ] [ ] [ ]"
        snare = "[ ] [ ] [ ] [ ] [x] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [x] [ ] [ ] [ ]"
        hihat = "[x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x] [x]"
    else:
        # Default 4-on-the-floor House
        kick  = "[x] [ ] [ ] [ ] [x] [ ] [ ] [ ] [x] [ ] [ ] [ ] [x] [ ] [ ] [ ]"
        snare = "[ ] [ ] [ ] [ ] [x] [ ] [ ] [ ] [ ] [ ] [ ] [ ] [x] [ ] [ ] [ ]"
        hihat = "[ ] [ ] [x] [ ] [ ] [ ] [x] [ ] [ ] [ ] [x] [ ] [ ] [ ] [x] [ ]"
        
    return f"""
    🥁 **16-Step Sequencer Matrix [{genre.upper()}]:**
    KICK:  {kick}
    SNARE: {snare}
    HATS:  {hihat}
    """
