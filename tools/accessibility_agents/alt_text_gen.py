# tools/accessibility_agents/alt_text_gen.py

def compile_asset_alt_text(context_tag: str, visually_dominant_elements: list) -> str:
    """Builds clean, contextual descriptions for application visual elements."""
    elements_string = ", ".join(visually_dominant_elements)
    alt_text = f"Interface image displaying {elements_string}, configured for the {context_tag} workflow layer."
    
    return f"""
    🖼️ **Accessibility Alt Text Component Compiled:**
    - Context: {context_tag}
    - Generated String: "{alt_text}"
    - Code Snippet: `alt="{alt_text}"`
    """
