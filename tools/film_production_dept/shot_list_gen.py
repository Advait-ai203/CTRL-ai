# tools/film_production_dept/shot_list_gen.py

def compile_shot_item(shot_id: str, size: str, movement: str, description: str) -> dict:
    """Structures a single record item within the master operational shot list."""
    
    return {
        "shot_reference": shot_id,
        "framing_size": size.upper(),  # e.g., MCU, ECU, WS
        "camera_movement": movement.upper(),  # e.g., PAN, TILT, TRACKING
        "narrative_focus": description,
        "verification_flag": "Staged for execution"
    }
