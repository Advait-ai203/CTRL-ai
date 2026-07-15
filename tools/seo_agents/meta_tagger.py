# tools/seo_agents/meta_tagger.py

def validate_meta_tags(title: str, description: str) -> str:
    """Validates SEO meta tags against Google's optimal character limits."""
    
    title_len = len(title)
    desc_len = len(description)
    
    title_status = "🟢 OPTIMAL" if 40 <= title_len <= 60 else "🔴 REVISE (Keep between 40-60 chars)"
    desc_status = "🟢 OPTIMAL" if 120 <= desc_len <= 155 else "🔴 REVISE (Keep between 120-155 chars)"
    
    return f"""
    🏷️ **Meta Tag Validation Matrix:**
    
    **Title:** "{title}"
    - Length: {title_len} chars
    - Status: {title_status}
    
    **Description:** "{description}"
    - Length: {desc_len} chars
    - Status: {desc_status}
    """
