# tools/sports_analytics_dept/player_form_tracker.py

def evaluate_form_index(recent_scores: list) -> str:
    """Calculates form rating weighting recent match results heavier than older ones."""
    if not recent_scores:
        return "⚠️ Insufficient historical records to evaluate form trajectory."
        
    # Apply standard exponential weighting factors
    total_weight = 0
    weighted_sum = 0
    
    for index, score in enumerate(reversed(recent_scores)):
        weight = 1.0 / (index + 1)
        weighted_sum += score * weight
        total_weight += weight
        
    form_index = round(weighted_sum / total_weight, 1)
    status = "🔥 ELITE IN-FORM" if form_index > 45 else "⏳ STABLE" if form_index > 25 else "⚠️ FORM SLUMP"
    
    return f"""
    📈 **Form Tracker Analytics Node:**
    - Sample Horizon: Last {len(recent_scores)} innings
    - Raw Sequence Evaluated: {recent_scores}
    - Calculated Form Index: **{form_index}**
    
    **Operational Assessment:** {status}
    """
