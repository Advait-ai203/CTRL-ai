# tools/team_agents/task_delegator.py
import json
import os

def assign_task(task_name: str, assignee: str, priority: str = "High", brand: str = "ctrl") -> str:
    """Logs a new sprint task and assigns it to a specific squad member."""
    target_dir = "./generated_assets/research_reports/team_sync"
    os.makedirs(target_dir, exist_ok=True)
    board_path = os.path.join(target_dir, "kanban_board.json")
    
    # Updated Core Roster
    valid_team = ["Advait", "Tarun", "Nicky", "Shubhansh"]
    
    if assignee not in valid_team:
        return f"⚠️ Assignment Error: '{assignee}' is not recognized in the core roster."
        
    entry = {
        "task": task_name,
        "brand": brand,
        "owner": assignee,
        "priority": priority.upper(),
        "status": "In Progress"
    }
    
    try:
        if os.path.exists(board_path):
            with open(board_path, "r") as f:
                board = json.load(f)
        else:
            board = []
            
        board.append(entry)
        
        with open(board_path, "w") as f:
            json.dump(board, f, indent=4)
            
        return f"🎯 **Task Delegated:** '{task_name}' assigned to {assignee} for {brand.upper()}."
    except Exception as e:
        return f"⚠️ Task Matrix Fault: {str(e)}"
