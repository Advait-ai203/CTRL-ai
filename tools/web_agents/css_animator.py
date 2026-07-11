# tools/web_agents/css_animator.py

def generate_keyframe_animation(animation_name: str, effect_type: str = "pulse") -> str:
    """Outputs pure CSS keyframe logic for UI elements."""
    
    if effect_type == "glitch":
        css = f"""
@keyframes {animation_name} {{
  0% {{ clip-path: inset(80% -6px 0 0); transform: translate(-20px, 20px); }}
  20% {{ clip-path: inset(80% -6px 0 0); transform: translate(-10px, 20px); }}
  40% {{ clip-path: inset(50% -6px 30% 0); transform: translate(-5px, 0px); }}
  60% {{ clip-path: inset(40% -6px 43% 0); transform: translate(5px, 10px); }}
  80% {{ clip-path: inset(80% -6px 5% 0); transform: translate(20px, -10px); }}
  100% {{ clip-path: inset(50% 50% 50% 50%); transform: translate(0); }}
}}
.{animation_name}-class {{ animation: {animation_name} 1s infinite; }}
"""
    else:
        # Default smooth hover float
        css = f"""
@keyframes {animation_name} {{
  0% {{ transform: translateY(0px); box-shadow: 0 5px 15px rgba(0,255,136,0.2); }}
  50% {{ transform: translateY(-10px); box-shadow: 0 15px 25px rgba(0,255,136,0.4); }}
  100% {{ transform: translateY(0px); box-shadow: 0 5px 15px rgba(0,255,136,0.2); }}
}}
.{animation_name}-class {{ animation: {animation_name} 3s ease-in-out infinite; }}
"""
    return f"✨ **CSS Animation Computed:**\n```css\n{css}\n```"
