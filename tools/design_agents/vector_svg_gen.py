# tools/design_agents/vector_svg_gen.py
import os

def generate_icon_svg(icon_name: str) -> str:
    """Compiles clean, mathematically precise SVG icons."""
    target_dir = "./generated_assets/web_builds/icons"
    os.makedirs(target_dir, exist_ok=True)
    
    # Example: A sharp, minimalist geometric 'Play' or 'Action' icon
    svg_code = """<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M5 3L19 12L5 21V3Z" stroke="#00FF88" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
</svg>"""

    file_path = os.path.join(target_dir, f"{icon_name}.svg")
    with open(file_path, "w") as f:
        f.write(svg_code)
        
    return f"🖋️ **Vector Asset Compiled:** Saved SVG to `{file_path}`"
