# tools/team_agents/performance_review.py

def evaluate_member_performance(member_name: str, tasks_completed: int, critical_bugs: int) -> str:
    """Calculates a quick performance matrix based on sprint output."""
    
    if tasks_completed == 0:
        return f"⚠️ {member_name} has no logged tasks for this cycle."
        
    efficiency = (tasks_completed / (tasks_completed + critical_bugs)) * 100
    
    status = "EXCEPTIONAL" if efficiency > 90 else "NOMINAL" if efficiency > 75 else "NEEDS REVIEW"
    
    return f"""
    📈 **Performance Matrix: {member_name.upper()}**
    - Sprint Tickets Closed: {tasks_completed}
    - Critical Faults Logged: {critical_bugs}
    - Operational Efficiency: {efficiency:.1f}%
    
    *Assessment:* {status}
    """
