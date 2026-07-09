# tools/web_agents/css_injector.py
# Injects global modular stylesheets into target web files

import os

def inject_styles_to_target(filename: str, custom_css: str) -> str:
    """Appends targeted stylistic modifications or global utility frameworks to static assets."""
    target_path = f"./generated_assets/web_builds/{filename}.html"
    
    if not os.path.exists(target_path):
        return f"⚠️ Style Injector Fault: Target web asset '{filename}.html' does not exist."
        
    style_block = f"\n<style>\n{custom_css}\n</style>\n</head>"
    
    try:
        with open(target_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Insert the styling before closing the head element
        if "</head>" in content:
            updated_content = content.replace("</head>", style_block)
            with open(target_path, "w", encoding="utf-8") as f:
                f.write(updated_content)
            return f"🎨 **Styles Successfully Blended:** Embedded visual rules into `{target_path}`"
        return "⚠️ Style Injector Fault: Document head element missing structural closing tags."
    except Exception as e:
        return f"⚠️ Style Injection Failure: {str(e)}"
