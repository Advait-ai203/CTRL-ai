# tools/music_production_dept/midi_composer.py
import json

def generate_midi_sequence(bpm: int, sequence_length: int = 16) -> str:
    """Compiles a raw MIDI event matrix for synth triggering."""
    
    # 4/4 time signature baseline, 16th note resolution
    ticks_per_beat = 4 
    total_ticks = sequence_length * ticks_per_beat
    
    events = []
    for tick in range(0, total_ticks, 4):  # Four-on-the-floor baseline
        events.append({"tick": tick, "type": "note_on", "note": 60, "velocity": 100})
        events.append({"tick": tick + 2, "type": "note_off", "note": 60, "velocity": 0})
        
    midi_payload = {
        "metadata": {"tempo": bpm, "time_signature": "4/4"},
        "track_01": events
    }
    
    return f"🎹 **MIDI Sequence Matrix:**\n```json\n{json.dumps(midi_payload, indent=4)}\n```"
