# tools/film_production_dept/web_series_manager.py
import json
import os

def update_episode_status(episode_id: str, title: str, status: str) -> str:
    """Logs and tracks the structural development phase of an episode."""
    target_dir = "./generated_assets/research_reports/cinema"
    os.makedirs(target_dir, exist_ok=True)
    ledger_path = os.path.join(target_dir, "series_tracker.json")
    
    valid_statuses = ["Scripting", "Pre-Production", "Shooting", "Post-Production", "Done"]
    current_status = status if status in valid_statuses else "Scripting"
    
    try:
        tracker = {}
        if os.path.exists(ledger_path):
            with open(ledger_path, "r") as f:
                tracker = json.load(f)
                
        tracker[episode_id] = {
            "title": title,
            "status": current_status,
            "completion_percentage": (valid_statuses.index(current_status) + 1) * 20
        }
        
        with open(ledger_path, "w") as f:
            json.dump(tracker, f, indent=4)
            
        return f"🎬 **Series Matrix Updated:** '{title}' locked at phase [{current_status}]."
    except Exception as e:
        return f"⚠️ Series Manager Fault: {str(e)}"
