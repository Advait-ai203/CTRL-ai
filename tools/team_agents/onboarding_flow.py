# tools/team_agents/onboarding_flow.py
import os

def generate_onboarding_doc(new_hire_name: str, role: str) -> str:
    """Compiles a standard operating procedure (SOP) document for new team additions."""
    target_dir = "./generated_assets/research_reports/team_sync"
    os.makedirs(target_dir, exist_ok=True)
    
    doc_content = f"""# Welcome to the Startup Studio: {new_hire_name}
    
**Role:** {role}
**Primary Directives:**
1. Default to action. 
2. We operate two brands: `ctrl` (Software) and `allmate` (Hardware). Keep data isolated.
3. Push all code and design files to the central `generated_assets/` matrix.

**Access Granted:**
- Slack/Discord Comms
- GitHub Repositories
- Figma Design Files

*Initiation Complete.*
"""
    file_path = os.path.join(target_dir, f"onboarding_{new_hire_name.lower()}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(doc_content)
        
    return f"👋 **Onboarding Protocol Executed:** Matrix docs compiled to `{file_path}`"
