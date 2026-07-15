# tools/sports_analytics_dept/pitch_weather_analyzer.py

def analyze_match_conditions(venue: str, humidity: float, overhead_cloud_percent: float) -> str:
    """Evaluates how climate conditions impact ball dynamics and pitch degradation."""
    
    if humidity > 70.0 and overhead_cloud_percent > 60.0:
        condition_assessment = "🏏 High aerial moisture present. Enhanced swing conditions anticipated for fast bowlers."
    elif humidity < 40.0:
        condition_assessment = "☀️ Dry atmospheric profile. Pitch likely to crack, offering significant turn to spinners later in the match."
    else:
        condition_assessment = "⚖️ Balanced climate profile. Standard neutral playing surface performance expected."
        
    return f"""
    🏟️ **Environmental Conditions Matrix [{venue.upper()}]:**
    - Ambient Humidity: {humidity}%
    - Cloud Density: {overhead_cloud_percent}%
    
    **Tactical Outlook:** {condition_assessment}
    """
