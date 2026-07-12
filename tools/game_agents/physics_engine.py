# tools/game_agents/physics_engine.py

def calculate_trajectory(initial_velocity_y: float, gravity: float = -9.8, delta_time: float = 0.016) -> str:
    """Calculates frame-by-frame positional data for a jumping/falling entity."""
    
    # Formula: v = u + at, s = ut + 1/2at^2
    velocity = initial_velocity_y + (gravity * delta_time)
    displacement = (initial_velocity_y * delta_time) + (0.5 * gravity * (delta_time ** 2))
    
    return f"""
    ☄️ **Rigid-Body Physics Calculation:**
    - **Delta Time (dt):** {delta_time}s (assuming ~60 FPS)
    - **Gravity Vector:** {gravity} m/s^2
    - **New Y-Velocity:** {velocity:.3f} m/s
    - **Y-Displacement (this frame):** {displacement:.4f} m
    """
