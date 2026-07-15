# tools/education_tech_dept/historical_timeline_gen.py

def generate_chronology(events: list) -> str:
    """Sorts a list of dictionaries (year, event) into a chronological timeline."""
    
    if not events:
        return "⚠️ Timeline Error: No events provided."
        
    # Sort events by year
    sorted_events = sorted(events, key=lambda x: x.get('year', 0))
    
    output = "⏳ **Historical Matrix: Chronology**\n"
    for item in sorted_events:
        year = item.get('year')
        desc = item.get('event', 'Unknown Event')
        output += f"- **{year}:** {desc}\n"
        
    return output
