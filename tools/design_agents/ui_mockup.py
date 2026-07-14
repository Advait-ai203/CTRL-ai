# tools/design_agents/ui_mockup.py

def synthesize_design_spec(brand_name: str) -> str:
    """Aggregates all visual data into a master design specification."""
    
    spec = f"""
    🖥️ **Master UI Mockup Specification: {brand_name.upper()}**
    
    **Visual Rules:**
    - Background: Deep black (#0a0a0a)
    - Accents: Neon Green (#00ff88) and Deep Pink (#cf30aa)
    - Typography: Space Grotesk (Headers) + Inter (Body)
    - Border Radius: Sharp edges (0px) or highly rounded (50px), no in-between.
    
    **Interaction Design:**
    - Buttons glow on hover.
    - Transitions are snappy (0.2s ease-out).
    
    *Route this specification to the `react_scaffolder.py` to begin component assembly.*
    """
    return spec
