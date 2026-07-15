# tools/film_production_dept/call_sheet_maker.py
import datetime

def generate_daily_call_sheet(date_str: str, call_time: str, location: str) -> str:
    """Generates the master logistical call sheet template for a filming crew."""
    
    return f"""
    📅 **OFFICIAL CALL SHEET MATRIX**
    --------------------------------------------------
    Date: {date_str}
    Crew Call Time: {call_time}
    Location Base: {location}
    --------------------------------------------------
    SCHEDULE MATRIX:
    - 09:00 AM │ Base Setup & Rigging
    - 10:30 AM │ Block & Light Scene 1
    - 11:30 AM │ Principal Photography (A-Roll)
    - 03:00 PM │ B-Roll & Visual Asset Capture
    - 05:30 PM │ Wrap & Equipment Tear Down
    
    *Strict execution required. Maintain schedule velocity.*
    """
