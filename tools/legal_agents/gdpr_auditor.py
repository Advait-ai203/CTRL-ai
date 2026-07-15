# tools/legal_agents/gdpr_auditor.py
import re

def audit_gdpr_readiness(html_source: str) -> str:
    """Scans frontend code for mandatory privacy consent mechanisms."""
    
    has_cookie_banner = bool(re.search(r'id=["\']cookie-consent["\']|class=["\']cookie-banner["\']', html_source, re.IGNORECASE))
    has_privacy_link = bool(re.search(r'href=["\'].*privacy.*["\']', html_source, re.IGNORECASE))
    
    if has_cookie_banner and has_privacy_link:
        return "🛡️ **GDPR Matrix:** Web build passes basic compliance scan (Consent Banner + Privacy Link detected)."
        
    errors = ""
    if not has_cookie_banner:
        errors += "- Missing Cookie/Tracking Consent UI element.\n"
    if not has_privacy_link:
        errors += "- Missing direct link to the Privacy Policy in the DOM.\n"
        
    return f"⚠️ **GDPR Violations Detected:**\n{errors}\n*Action Required: Inject consent components before deploying to European traffic.*"
