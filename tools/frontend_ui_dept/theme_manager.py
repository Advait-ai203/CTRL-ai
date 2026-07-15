# tools/frontend_ui_dept/theme_manager.py

def generate_css_variables(theme_name: str = "cyberpunk") -> str:
    """Generates the :root CSS variables for global app theming."""
    
    if theme_name == "cyberpunk":
        css = """
        :root {
            --bg-primary: #0a0a0a;
            --text-main: #ffffff;
            --accent-1: #00ff88;
            --accent-2: #cf30aa;
        }
        """
    else:
        css = """
        :root {
            --bg-primary: #ffffff;
            --text-main: #111111;
            --accent-1: #007bff;
            --accent-2: #6c757d;
        }
        """
        
    return f"🎨 **Theme Variables Compiled:**\n```css\n{css}\n```"
