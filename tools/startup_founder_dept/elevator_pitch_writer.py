# tools/startup_founder_dept/elevator_pitch_writer.py

def draft_elevator_pitch(brand: str, target_audience: str, key_benefit: str) -> str:
    """Creates a punchy, 30-second conversational hook."""
    
    pitch = f"You know how {target_audience} always struggle with slow, inefficient systems? "
    pitch += f"We built {brand} to solve exactly that. We provide {key_benefit}, "
    pitch += "allowing teams to execute faster and scale without the usual friction. "
    pitch += "We are currently preparing for our seed round—I'd love to show you the prototype."
    
    return f"⏱️ **30-Second Pitch Matrix:**\n\n\"{pitch}\""
