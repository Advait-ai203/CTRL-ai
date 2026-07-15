# tools/productivity_agents/focus_timer.py

def evaluate_focus_session(session_minutes: int, distraction_count: int) -> str:
    """Calculates efficiency metrics for a completed deep-work session."""
    if session_minutes <= 0:
        return "⚠️ Session duration must be greater than zero."
        
    # Flow score algorithm based on duration and context-switching penalties
    penalty = distraction_count * 15
    flow_score = max(0, 100 - int((penalty / session_minutes) * 100))
    
    status = "🔥 Masterful Focus" if flow_score >= 85 else "⏳ Moderate Flow" if flow_score >= 60 else "⚠️ High Distraction Rate"
    
    return f"""
    ⏱️ **Focus Session Matrix Evaluation:**
    - Active Duration: {session_minutes} minutes
    - Interruptions Logged: {distraction_count}
    - Calculated Flow Index: **{flow_score}/100**
    
    **Session Assessment:** {status}
    """
