# tools/frontend_ui_dept/component_library_mgr.py

def get_ui_component(component_name: str) -> str:
    """Retrieves standard, pre-styled HTML components from the internal library."""
    
    library = {
        "primary_button": "<button style='background: #00FF88; color: #000; padding: 12px 24px; border: none; font-weight: bold; cursor: pointer;'>Execute</button>",
        "matrix_card": "<div style='border: 1px solid #333; padding: 20px; border-radius: 8px; background: #1a1a1a;'>Card Content</div>",
        "search_bar": "<input type='text' placeholder='Search the matrix...' style='width: 100%; padding: 10px; background: #222; color: #fff; border: 1px solid #444;' />"
    }
    
    component = library.get(component_name.lower(), "")
    return component
