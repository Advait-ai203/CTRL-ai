# tools/productivity_agents/daily_journal.py
import os
import datetime

def commit_daily_reflection(wins_list: list, system_bottlenecks: str) -> str:
    """Saves structural review logs for continuous process improvement."""
    target_dir = "./generated_assets/research_reports/productivity"
    os.makedirs(target_dir, exist_ok=True)
    
    timestamp = datetime.date.today().strftime("%Y-%m-%d")
    formatted_wins = "\n".join([f"- {win}" for win in wins_list])
    
    log_content = f"""# Engineering Sync & Reflection: {timestamp}
    
## Core Progress & Velocity Wins
{formatted_wins}

## System Bottlenecks Identified
{system_bottlenecks}

[Committed to System Log]
"""
    file_path = os.path.join(target_dir, f"journal_{timestamp}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(log_content)
        
    return f"📝 **Reflection Log Secure:** Matrix entry committed to `{file_path}`"
