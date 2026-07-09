# tools/design_dept/svg_generator.py
# Dynamic design tool for outputting responsive vector files

import os

def render_vector_graphic(filename: str, inner_svg_elements: str, viewbox: str = "0 0 500 500") -> str:
    """Compiles scalable path, element, and shape definitions into vector assets."""
    target_dir = "./generated_assets/vector_art"
    os.makedirs(target_dir, exist_ok=True)
    
    full_svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="{viewbox}" width="100%" height="100%">
    {inner_svg_elements}
</svg>"""
    
    file_path = os.path.join(target_dir, f"{filename}.svg")
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(full_svg)
        return f"📐 **Vector Asset Generated Successfully:** Saved to `{file_path}`"
    except Exception as e:
        return f"⚠️ Design Compiler Fault: {str(e)}"
