# tools/legal_agents/tos_writer.py
import os

def generate_tos(business_type: str, brand_name: str) -> str:
    """Generates a base Terms of Service tailored to SaaS or E-commerce."""
    target_dir = "./generated_assets/research_reports/legal"
    os.makedirs(target_dir, exist_ok=True)
    
    if business_type.lower() == "ecommerce":
        liability_clause = "We are not liable for shipping delays, customs fees, or physical misuse of hardware products."
    else:
        liability_clause = "We provide this software 'as is' without warranty. We are not liable for server downtime or data loss."
        
    tos_text = f"""# Terms of Service for {brand_name.upper()}

## 1. Acceptance of Terms
By accessing our platform or purchasing our goods, you agree to be bound by these Terms of Service.

## 2. User Conduct
You agree not to use the services for any unlawful purpose or to conduct automated scraping without explicit matrix permission.

## 3. Limitation of Liability
{liability_clause}

## 4. Intellectual Property
All code, designs, and branding remain the exclusive property of {brand_name}.

[Drafted by ctrl Legal Matrix]
"""
    file_path = os.path.join(target_dir, f"ToS_{brand_name}.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(tos_text)
        
    return f"⚖️ **Terms of Service Compiled:** `{file_path}`"
