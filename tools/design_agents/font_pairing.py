# tools/design_agents/font_pairing.py

def get_font_pairing(vibe: str) -> str:
    """Returns optimal Google Font combinations for UI development."""
    
    pairings = {
        "tech": {"heading": "Space Grotesk", "body": "Inter"},
        "editorial": {"heading": "Playfair Display", "body": "Source Sans Pro"},
        "modern": {"heading": "Montserrat", "body": "Roboto"}
    }
    
    fonts = pairings.get(vibe.lower(), pairings["tech"])
    
    return f"""
    🔤 **Typography Matrix Locked:**
    - Headings (H1-H6): **{fonts['heading']}** (Suggested weights: 700, 800)
    - Body Text (p, span): **{fonts['body']}** (Suggested weights: 400, 500)
    
    *Inject these imports into your CSS architecture.*
    """
