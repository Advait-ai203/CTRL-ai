# tools/productivity_agents/calendar_sync.py
import datetime

def block_time_slot(event_title: str, start_time_str: str, duration_minutes: int) -> dict:
    """Validates and stages a time block block within the schedule matrix."""
    try:
        start_time = datetime.datetime.strptime(start_time_str, "%H:%M")
        end_time = start_time + datetime.timedelta(minutes=duration_minutes)
        
        return {
            "status": "synchronized",
            "event": event_title,
            "time_window": f"{start_time.strftime('%I:%M %p')} - {end_time.strftime('%I:%M %p')}",
            "allocation_slots": round(duration_minutes / 30, 1),
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d")
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
