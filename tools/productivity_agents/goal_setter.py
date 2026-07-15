# tools/productivity_agents/goal_setter.py
import datetime

def compile_smart_milestone(objective_text: str, metric_target: str, deadline_days: int) -> str:
    """Formats raw ambitions into clear deadlines and metrics."""
    
    target_date = (datetime.date.today() + datetime.timedelta(days=deadline_days)).strftime("%B %d, %Y")
    
    return f"""
    🎯 **SMART Objective Matrix Initialized:**
    - **Strategic Goal:** {objective_text}
    - **Success Metric:** {metric_target}
    - **Target Deadline:** {target_date} ({deadline_days} days remaining)
    
    *System Status: Active Tracking Engaged.*
    """
