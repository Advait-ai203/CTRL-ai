# tools/music_production_dept/sheet_music_parser.py

def parse_abc_notation(abc_string: str) -> dict:
    """Extracts tempo, key signature, and notes from ABC notation text."""
    
    metadata = {}
    notes = []
    
    for line in abc_string.split('\n'):
        if line.startswith('T:'): metadata['title'] = line[2:].strip()
        elif line.startswith('M:'): metadata['meter'] = line[2:].strip()
        elif line.startswith('K:'): metadata['key'] = line[2:].strip()
        elif line.startswith('Q:'): metadata['tempo'] = line[2:].strip()
        elif not line.startswith('%') and not ":" in line:
            # Very basic extraction of note characters
            notes.extend([c for c in line if c.isalpha()])
            
    return {
        "status": "Parsed",
        "metadata": metadata,
        "note_count": len(notes),
        "raw_stream": notes[:10] # Show first 10 for structural proof
    }
