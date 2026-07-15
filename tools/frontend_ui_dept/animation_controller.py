# tools/frontend_ui_dept/animation_controller.py

def get_keyframes(animation_type: str) -> str:
    """Returns CSS keyframes for standard UI motion graphics."""
    
    if animation_type == "pulse":
        keyframes = """
        @keyframes matrixPulse {
            0% { transform: scale(1); opacity: 1; }
            50% { transform: scale(1.05); opacity: 0.8; }
            100% { transform: scale(1); opacity: 1; }
        }
        """
    elif animation_type == "fade_in":
        keyframes = """
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }
        """
    else:
        keyframes = "/* Animation not found */"
        
    return f"🎬 **Animation Engine:**\n```css\n{keyframes}\n```"
