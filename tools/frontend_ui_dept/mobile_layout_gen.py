# tools/frontend_ui_dept/mobile_layout_gen.py

def generate_mobile_wrapper(content: str) -> str:
    """Wraps HTML content in a strictly constrained mobile-first viewport container."""
    
    wrapper = f"""
    <div style="max-width: 480px; margin: 0 auto; background: #000; min-height: 100vh; position: relative; overflow-x: hidden;">
        {content}
    </div>
    """
    return wrapper
