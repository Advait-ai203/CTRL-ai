# tools/accessibility_agents/screen_reader_test.py
import re

def audit_aria_landmarks(html_content: str) -> str:
    """Audits structural attributes within an HTML document block for essential accessibility compliance."""
    has_main = bool(re.search(r'<main[^>]*>|role=["\']main["\']', html_content, re.IGNORECASE))
    missing_alt_count = len(re.findall(r'<img(?!.*alt=)[^>]*>', html_content, re.IGNORECASE))
    
    status = "🟢 LOGIC VALIDATED" if has_main and missing_alt_count == 0 else "⚠️ COMPLIANCE WARNING"
    
    return f"""
    🛡️ **Screen Reader Document Audit Complete:**
    - Root Element Landmark (<main>): {"FOUND" if has_main else "MISSING"}
    - Unlabeled Asset Structures (<img missing alt>): {missing_alt_count}
    
    **Audit Matrix Conclusion:** {status}
    """
