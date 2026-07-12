# tools/game_agents/particle_fx.py
import json

def generate_particle_config(fx_name: str, base_color: str, lifespan_ms: int = 500) -> str:
    """Generates standard JSON parameters for game engine particle systems."""
    
    config = {
        "fx_id": fx_name,
        "emission_rate": 50,
        "lifespan_ms": lifespan_ms,
        "start_color": base_color,
        "end_color": "#00000000", # Fade to transparent
        "velocity_variance": [ -5.0, 5.0 ],
        "gravity_modifier": 0.5,
        "blend_mode": "additive"
    }
    
    json_output = json.dumps(config, indent=4)
    return f"✨ **Particle FX Initialized: {fx_name.upper()}**\n```json\n{json_output}\n```"
