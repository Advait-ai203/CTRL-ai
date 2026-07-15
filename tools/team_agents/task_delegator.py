# tools/team_agents/task_delegator.py
import json
import os

def load_matrix_config() -> list:
    """Loads the core team roster dynamically from the root config file."""
    config_path = "./matrix_config.json"
    try:
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                config = json.load(f)
                return config.get("core_team", [])
        return []
    except Exception:
        return []

def assign_task(task_name: str, assignee: str, priority: str = "High", brand: str = "ctrl") -> str:
    """Logs a new sprint task and assigns it to a valid squad member."""
    target_dir = "./generated_assets/research_reports/team_sync"
    os.makedirs(target_dir, exist_ok=True)
    board_path = os.path.join(target_dir, "kanban_board.json")
    
    # Dynamically pull the team from the user's config file
    valid_team = load_matrix_config()
    
    if not valid_team:
        return "⚠️ Config Error: No `matrix_config.json` found or core_team array is empty. Please configure your matrix."
    
    if assignee not in valid_team:
        return f"⚠️ Assignment Error: '{assignee}' is not recognized in your matrix_config.json roster. Valid users: {', '.join(valid_team)}"
        
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
