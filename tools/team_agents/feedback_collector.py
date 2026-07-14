# tools/team_agents/feedback_collector.py
import json
import os
import datetime

def log_sprint_feedback(sprint_id: str, blocker_notes: str, morale_score: int) -> str:
    """Logs internal team feedback to optimize future operational sprints."""
    target_dir = "./generated_assets/research_reports/team_sync"
    os.makedirs(target_dir, exist_ok=True)
    log_path = os.path.join(target_dir, "sprint_retro.json")
    
    if morale_score < 1 or morale_score > 10:
        return "⚠️ Morale score must be between 1 and 10."
        
    entry = {
        "date": str(datetime.date.today()),
        "sprint": sprint_id,
        "blockers": blocker_notes,
        "morale_index": morale_score
    }
    
    try:
        if os.path.exists(log_path):
            with open(log_path, "r") as f:
                retro = json.load(f)
        else:
            retro = []
            
        retro.append(entry)
        
        with open(log_path, "w") as f:
            json.dump(retro, f, indent=4)
            
        return f"🔄 **Retrospective Logged:** Sprint {sprint_id} feedback secured in the matrix."
    except Exception as e:
        return f"⚠️ Retro Fault: {str(e)}"
