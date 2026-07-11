# tools/web_agents/accessibility_auditor.py

def audit_html_accessibility(html_string: str) -> str:
    """Performs a lightweight scan on HTML to ensure screen-reader compliance."""
    warnings = []
    
    if "<img" in html_string and "alt=" not in html_string:
        warnings.append("❌ Missing `alt` attributes on image tags.")
        
    if "<button" in html_string and "aria-label=" not in html_string:
        warnings.append("⚠️ Buttons detected without `aria-label` definitions.")
        
    if "<html" in html_string and "lang=" not in html_string:
        warnings.append("❌ Root HTML tag is missing the `lang` attribute.")
        
    if not warnings:
        return "✅ **Accessibility Audit:** Code passes basic screen-reader compliance."
        
    formatted_warnings = "\n".join(warnings)
    return f"🔍 **Accessibility Violations Detected:**\n{formatted_warnings}\n\n*Action Required: Update structural tags.*"
