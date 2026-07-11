# tools/system_web_dept/cron_scheduler.py
import json
import os
import datetime

def schedule_background_task(task_name: str, execute_at_time: str, command: str) -> str:
    """
    Logs a background task into a local JSON queue.
    (Requires a background loop in main.py to actively check this file).
    """
    queue_dir = "./generated_assets/task_queue"
    os.makedirs(queue_dir, exist_ok=True)
    queue_file = os.path.join(queue_dir, "cron_jobs.json")

    new_job = {
        "task_name": task_name,
        "scheduled_time": execute_at_time,
        "command": command,
        "created_at": datetime.datetime.now().isoformat(),
        "status": "pending"
    }

    try:
        # Load existing jobs or create a new list
        if os.path.exists(queue_file):
            with open(queue_file, "r") as f:
                jobs = json.load(f)
        else:
            jobs = []

        jobs.append(new_job)

        with open(queue_file, "w") as f:
            json.dump(jobs, f, indent=4)

        return f"⏰ **Task Scheduled:** `{task_name}` queued for execution at {execute_at_time}."
    except Exception as e:
        return f"Scheduler Fault: {str(e)}"
