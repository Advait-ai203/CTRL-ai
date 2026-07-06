# ui/layouts/mobile_view.py
# Structural wrapper for mobile device access

def wrap_in_mobile_stack(*html_components: str) -> str:
    """Stacks UI elements vertically for mobile screens."""
    
    inner_html = "\n".join([f'<div class="mobile-stack-item">{c}</div>' for c in html_components])
    
    return f"""
    <style>
    .ctrl-mobile-stack {{
        display: flex;
        flex-direction: column;
        gap: 16px;
        width: 100%;
        padding: 10px;
    }}
    .mobile-stack-item {{
        width: 100%;
        overflow-x: hidden;
    }}
    </style>
    <div class="ctrl-mobile-stack">
        {inner_html}
    </div>
    """
