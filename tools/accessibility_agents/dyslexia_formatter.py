# tools/accessibility_agents/dyslexia_formatter.py

def apply_readability_styling(raw_html_content: str) -> str:
    """Wraps structural code elements into specific style parameters optimized for reading clarity."""
    accessible_wrapper = f"""
    <div style="font-family: 'OpenDyslexic', 'Comic Sans MS', sans-serif; line-height: 2.0; letter-spacing: 0.35ch; word-spacing: 1.2ch;">
        {raw_html_content}
    </div>
    """
    return f"📖 **Dyslexia Style Wrapping Generated:**\n```html\n{accessible_wrapper}\n```"
