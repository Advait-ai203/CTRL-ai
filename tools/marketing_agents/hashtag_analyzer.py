# tools/marketing_agents/hashtag_analyzer.py

def generate_hashtags(niche: str) -> str:
    """Generates optimized hashtag clusters based on target industry."""
    
    clusters = {
        "tech": "#TechStartup #SoftwareEngineering #FutureOfTech #CodingLife #SaaS",
        "ecommerce": "#Streetwear #EverydayCarry #allmate #ProductDesign #ShopLocal",
        "film": "#StopMotion #IndieFilm #BehindTheScenes #VGLegends #Filmmaking",
        "default": "#Innovation #Creator #StartupGrind #Entrepreneur"
    }
    
    selected_tags = clusters.get(niche.lower(), clusters["default"])
    
    return f"""
    🏷️ **Hashtag Matrix Optimized for '{niche.upper()}':**
    ```text
    {selected_tags}
    ```
    *Status: Ready for payload injection.*
    """
