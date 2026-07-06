# ui/layouts/desktop_grid.py
# Structural wrapper for desktop-scale dashboards

def wrap_in_desktop_grid(*html_components: str, columns: int = 2) -> str:
    """Wraps multiple UI widgets into a responsive CSS grid."""
    
    inner_html = "\n".join(html_components)
    
    return f"""
    <style>
    .ctrl-desktop-grid {{
        display: grid;
        grid-template-columns: repeat({columns}, 1fr);
        gap: 24px;
        width: 100%;
        max-width: 1200px;
        margin: 0 auto;
        padding: 20px;
    }}
    @media (max-width: 1024px) {{
        .ctrl-desktop-grid {{ grid-template-columns: 1fr; }}
    }}
    </style>
    <div class="ctrl-desktop-grid">
        {inner_html}
    </div>
    """
