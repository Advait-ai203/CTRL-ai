# tools/legal_agents/privacy_policy_gen.py
import os

def generate_privacy_policy(brand_name: str, collects_payments: bool = True) -> str:
    """Drafts a standard Privacy Policy detailing data handling."""
    target_dir = "./generated_assets/research_reports/legal"
    os.makedirs(target_dir, exist_ok=True)
    
    payment_clause = "- Payment Data: Processed securely via third-party gateways (Stripe/Razorpay). We do not store raw credit card numbers on our servers." if collects_payments else ""
    
    policy = f"""# Privacy Policy: {brand_name.upper()}

## Data Collection Matrix
We collect the following information to operate our services:
- Account Data: Email addresses and basic profile information.
- Usage Data: Analytics regarding how you interact with our platform.
{payment_clause}

## Data Security
Your data is secured using industry-standard cryptography and stored in access-controlled environments.

## User Rights
You have the right to request a full export of your data or request complete account deletion at any time.
"""
    file_path = os.path.join(target_dir, f"Privacy_Policy_{brand_name}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(policy)
        
    return f"🔒 **Privacy Policy Compiled:** `{file_path}`"
