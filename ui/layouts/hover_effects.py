# ui/animations/hover_effects.py
# CSS injector for global interactive states

def inject_neon_hover() -> str:
    """Returns CSS to apply a neon glow on hover to any element with class 'neon-hover'."""
    return """
    <style>
    .neon-hover {
        transition: all 0.3s ease;
    }
    .neon-hover:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 25px rgba(0, 255, 136, 0.3);
        border-color: rgba(0, 255, 136, 0.8);
    }
    
    .pink-glow-hover {
        transition: all 0.3s ease;
    }
    .pink-glow-hover:hover {
        transform: scale(1.02);
        box-shadow: 0 0 30px rgba(207, 48, 170, 0.4);
        border-color: #cf30aa;
    }
    </style>
    """
