# tools/design_agents/logo_generator.py

def generate_text_logo(brand_name: str, color_hex: str = "#00FF88") -> str:
    """Generates an immediate CSS-styled text logo for rapid prototyping."""
    
    html_logo = f"""
    <div style="font-family: 'Space Grotesk', monospace; font-size: 32px; font-weight: 800; letter-spacing: -1.5px; color: #FFFFFF;">
        {brand_name.lower()}<span style="color: {color_hex};">.</span>
    </div>
    """
    
    return f"✨ **Brand Mark Generated:**\n```html\n{html_logo}\n```"
