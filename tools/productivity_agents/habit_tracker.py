# tools/productivity_agents/habit_tracker.py
import json
import os
import datetime

def update_habit_streak(habit_name: str, completed: bool) -> str:
    """Logs habit completions and updates continuous performance streaks."""
    target_dir = "./generated_assets/research_reports/productivity"
    os.makedirs(target_dir, exist_ok=True)
    ledger_path = os.path.join(target_dir, "habit_ledger.json")
    
    try:
        ledger = {}
        if os.path.exists(ledger_path):
            with open(ledger_path, "r") as f:
                ledger = json.load(f)
                
        current_streak = ledger.get(habit_name, {}).get("streak", 0)
        
        if completed:
            current_streak += 1
        else:
            current_streak = 0
            
        ledger[habit_name] = {
            "last_updated": str(datetime.date.today()),
            "streak": current_streak
        }
        
        with open(ledger_path, "w") as f:
            json.dump(ledger, f, indent=4)
            
        marker = "🔥" if current_streak > 0 else "❄️"
        return f"🔄 **Habit Matrix Updated:** '{habit_name}' streak is now {current_streak} {marker}"
    except Exception as e:
        return f"⚠️ Habit Ledger Fault: {str(e)}"
