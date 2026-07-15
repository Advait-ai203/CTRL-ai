# tools/music_production_dept/saxophone_tab_gen.py

def transpose_to_alto_sax(concert_notes: list) -> str:
    """
    Transposes Concert Pitch (Piano/Guitar) to E-flat Alto Saxophone pitch.
    To go from Concert to E-flat, you go up a major sixth (or down a minor third).
    """
    
    # Basic chromatic scale mapping for transposition
    chromatic = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    
    alto_notes = []
    for note in concert_notes:
        clean_note = note.upper().replace('B', '#') # Normalize flats for this basic matrix
        if clean_note in chromatic:
            index = chromatic.index(clean_note)
            # Shift up 9 semitones (Major 6th)
            alto_index = (index + 9) % 12
            alto_notes.append(chromatic[alto_index])
        else:
            alto_notes.append("?")
            
    # Sample fingering translation for the first note
    fingering = "Octave Key + 123 | 123" if alto_notes and alto_notes[0] == 'D' else "Standard layout"
            
    return f"""
    🎷 **E-Flat Alto Saxophone Matrix:**
    - Input (Concert Pitch): {', '.join(concert_notes)}
    - Output (Alto Pitch): **{', '.join(alto_notes)}**
    
    *Hardware Sync:* Tuned for standard Eb acoustic resonance and key action.
    *Initial Fingering Hint ({alto_notes[0] if alto_notes else ''}):* {fingering}
    """
