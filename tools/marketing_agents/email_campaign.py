# tools/marketing_agents/email_campaign.py
import os

def generate_drip_email(subject_line: str, body_text: str, brand_name: str = "ctrl") -> str:
    """Compiles a clean HTML email template for marketing blasts."""
    target_dir = "./generated_assets/web_builds/emails"
    os.makedirs(target_dir, exist_ok=True)
    
    html_email = f"""
    <div style="font-family: 'Inter', sans-serif; max-width: 600px; margin: auto; padding: 20px; border: 1px solid #e0e0e0; border-radius: 8px;">
        <h2 style="color: #cf30aa; text-align: center;">{brand_name.upper()}</h2>
        <h3 style="color: #333;">{subject_line}</h3>
        <p style="color: #555; line-height: 1.6;">{body_text}</p>
        <div style="text-align: center; margin-top: 30px;">
            <a href="#" style="background-color: #00ff88; color: #000; padding: 10px 20px; text-decoration: none; font-weight: bold; border-radius: 5px;">Take Action</a>
        </div>
    </div>
    """
    
    file_path = os.path.join(target_dir, f"email_{subject_line.replace(' ', '_').lower()}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_email)
        
    return f"📧 **Email Template Compiled:** Saved to `{file_path}`"
