# tools/education_tech_dept/physics_simulator.py

def calculate_freefall_kinematics(time_seconds: float, gravity: float = 9.81) -> str:
    """Calculates velocity and distance of an object in freefall over time."""
    
    if time_seconds < 0:
        return "⚠️ Temporal Error: Time cannot be negative."
        
    # v = g * t
    final_velocity = gravity * time_seconds
    # d = 0.5 * g * t^2
    distance_fallen = 0.5 * gravity * (time_seconds ** 2)
    
    return f"""
    🍎 **Kinematics Engine (Freefall):**
    - Elapsed Time: {time_seconds}s
    - Gravitational Constant: {gravity} m/s²
    
    **Calculated Vectors:**
    - Terminal Velocity Reached: **{final_velocity:.2f} m/s**
    - Total Distance Displaced: **{distance_fallen:.2f} meters**
    """
