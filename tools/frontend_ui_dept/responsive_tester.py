# tools/frontend_ui_dept/responsive_tester.py

def generate_viewport_meta() -> str:
    """Outputs the strict viewport scaling rules for responsive web design."""
    
    meta_tag = '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">'
    
    return f"📱 **Viewport Rules Configured:**\n```html\n{meta_tag}\n```"
