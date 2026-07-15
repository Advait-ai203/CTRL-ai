# tools/advanced_gaming_dept/jump_mechanic_logic.py

def compute_jump_trajectory(velocity_y: float, gravity: float, delta_time: float, current_y: float, is_grounded: bool) -> dict:
    """Evaluates frame-by-frame kinematics for a jumping entity."""
    if is_grounded and velocity_y <= 0:
        return {"position_y": current_y, "velocity_y": 0.0, "state": "grounded"}
        
    # Standard physics update equation: v = u + at, s = ut + 0.5at^2
    new_velocity_y = velocity_y - (gravity * delta_time)
    new_y = current_y + (new_velocity_y * delta_time)
    
    # Floor boundary safety check
    if new_y <= 0.0:
        return {"position_y": 0.0, "velocity_y": 0.0, "state": "grounded"}
        
    state = "ascending" if new_velocity_y > 0 else "descending"
    return {
        "position_y": round(new_y, 4),
        "velocity_y": round(new_velocity_y, 4),
        "state": state
    }
