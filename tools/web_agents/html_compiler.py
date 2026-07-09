# tools/web_agents/html_compiler.py
# Compiles raw structural blocks into deployable HTML documents

import os

def compile_html_page(filename: str, body_content: str, title: str = "ctrl App Build") -> str:
    """Compiles clean, responsive structural HTML shells inside the asset directory."""
    base_dir = "./generated_assets/web_builds"
    os.makedirs(base_dir, exist_ok=True)
    
    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ margin: 0; padding: 0; font-family: 'Inter', sans-serif; background-color: #050505; color: #ffffff; }}
    </style>
</head>
<body>
    {body_content}
</body>
</html>"""
    
    file_path = os.path.join(base_dir, f"{filename}.html")
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(full_html)
        return f"🖥️ **HTML Compilation Successful:** Saved layout to `{file_path}`"
    except Exception as e:
        return f"⚠️ Compilation Failed: {str(e)}"
