# tools/legal_agents/compliance_checker.py

def audit_corporate_compliance(entity_type: str, has_gst: bool, has_incorporation: bool) -> str:
    """Evaluates basic startup legal compliance status."""
    
    warnings = []
    if entity_type.lower() not in ["llp", "pvt ltd", "sole proprietorship"]:
        warnings.append("- Entity structure undefined.")
    if not has_gst:
        warnings.append("- Missing GST Registration (Required for physical E-commerce across states).")
    if not has_incorporation:
        warnings.append("- Not formally incorporated (Personal liability risk is high).")
        
    if not warnings:
        return "🟢 **Compliance Matrix:** All core corporate checkpoints cleared."
        
    formatted_warnings = "\n".join(warnings)
    return f"🟡 **Compliance Deficits Detected:**\n{formatted_warnings}\n\n*Action Required: File missing paperwork before scaling revenue operations.*"
