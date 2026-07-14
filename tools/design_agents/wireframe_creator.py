# tools/design_agents/wireframe_creator.py
import json

def generate_wireframe(page_type: str) -> str:
    """Scaffolds a logical UI wireframe in a structured JSON matrix."""
    
    if page_type == "landing":
        layout = {
            "header": ["logo_left", "nav_links_center", "cta_button_right"],
            "hero_section": ["h1_headline", "subtext", "primary_cta", "product_mockup_image"],
            "features_grid": ["icon_1", "text_1", "icon_2", "text_2", "icon_3", "text_3"],
            "footer": ["social_links", "legal_text"]
        }
    else:
        layout = {"status": "unsupported_layout", "message": "Specify 'landing' or 'dashboard'"}

    return f"📐 **Wireframe Computed ({page_type.upper()}):**\n```json\n{json.dumps(layout, indent=2)}\n```"
