# tools/frontend_ui_dept/glassmorphism_gen.py

def get_glass_css(opacity: float = 0.1, blur_px: int = 10) -> str:
    """Generates CSS for the frosted glass (glassmorphism) aesthetic."""
    
    css = f"""
    background: rgba(255, 255, 255, {opacity});
    backdrop-filter: blur({blur_px}px);
    -webkit-backdrop-filter: blur({blur_px}px);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 12px;
    """
    
    return f"🧊 **Glassmorphism CSS Generated:**\n```css\n{css}\n```"
