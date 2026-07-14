# tools/design_agents/brand_guidelines.py
import os

def compile_brand_book(brand_name: str, mission_statement: str) -> str:
    """Writes the official Markdown brand guideline document."""
    target_dir = "./generated_assets/research_reports"
    os.makedirs(target_dir, exist_ok=True)
    
    markdown_content = f"""# {brand_name.upper()} - Official Brand Guidelines

## 1. Mission
{mission_statement}

## 2. Voice & Tone
- **Primary:** Candid, Insightful, Direct.
- **Forbidden:** No corporate jargon, no fluff.
- **Architect:** Advait

## 3. Logo Usage
- Must maintain a minimum clearance of 24px on all sides.
- Do not stretch, skew, or alter the primary aspect ratio.
"""
    file_path = os.path.join(target_dir, f"{brand_name}_brand_book.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(markdown_content)
        
    return f"📖 **Brand Guidelines Compiled:** Document saved to `{file_path}`"
