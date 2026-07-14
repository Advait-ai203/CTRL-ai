# tools/marketing_agents/social_scheduler.py
import json
import os
from datetime import datetime

def schedule_post(platform: str, content: str, post_time: str, brand: str = "ctrl") -> str:
    """Queues a social media post for automated deployment."""
    target_dir = "./generated_assets/research_reports/social_queue"
    os.makedirs(target_dir, exist_ok=True)
    queue_path = os.path.join(target_dir, "master_queue.json")
    
    entry = {
        "brand": brand,
        "platform": platform,
        "content": content,
        "scheduled_time": post_time,
        "status": "pending"
    }
    
    try:
        if os.path.exists(queue_path):
            with open(queue_path, "r") as f:
                queue = json.load(f)
        else:
            queue = []
            
        queue.append(entry)
        
        with open(queue_path, "w") as f:
            json.dump(queue, f, indent=4)
            
        return f"📅 **Post Scheduled:** Queued for {platform.upper()} at {post_time}."
    except Exception as e:
        return f"⚠️ Scheduler Fault: {str(e)}"
