# tools/seo_agents/schema_markup.py
import json

def generate_json_ld(schema_type: str, data: dict) -> str:
    """Generates structured JSON-LD data for Google Rich Snippets."""
    
    schema = {
        "@context": "https://schema.org",
        "@type": schema_type
    }
    
    # Merge custom data into the schema base
    schema.update(data)
    
    json_ld_string = json.dumps(schema, indent=2)
    
    script_tag = f"""
<script type="application/ld+json">
{json_ld_string}
</script>
"""
    return f"🧠 **Schema Markup Compiled ({schema_type}):**\n```html\n{script_tag}\n```"
