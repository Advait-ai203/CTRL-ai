# tools/marketing_agents/influencer_tracker.py
import json
import os

def log_influencer_outreach(handle: str, platform: str, status: str = "contacted") -> str:
    """Logs influencer communication status into the marketing CRM."""
    target_dir = "./generated_assets/research_reports"
    os.makedirs(target_dir, exist_ok=True)
    crm_path = os.path.join(target_dir, "influencer_crm.json")
    
    entry = {"handle": handle, "platform": platform, "status": status}
    
    try:
        if os.path.exists(crm_path):
            with open(crm_path, "r") as f:
                crm = json.load(f)
        else:
            crm = []
            
        # Update existing or append new
        updated = False
        for record in crm:
            if record["handle"] == handle and record["platform"] == platform:
                record["status"] = status
                updated = True
                break
                
        if not updated:
            crm.append(entry)
            
        with open(crm_path, "w") as f:
            json.dump(crm, f, indent=4)
            
        return f"🤝 **CRM Matrix Updated:** {handle} on {platform} marked as '{status}'."
    except Exception as e:
        return f"⚠️ CRM Fault: {str(e)}"
