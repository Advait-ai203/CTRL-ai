# tools/startup_founder_dept/business_model_gen.py

def generate_monetization_strategy(venture_type: str) -> str:
    """Outlines revenue loops based on whether the venture is digital or physical."""
    
    if venture_type.lower() == "software":
        strategy = """
        💻 **SaaS Matrix (ctrl):**
        - **Tier 1 (Core):** Freemium access to basic tools.
        - **Tier 2 (Pro):** ₹999/month for advanced agentic automation and unlimited API calls.
        - **Enterprise:** Custom SLA pricing for B2B clients integrating our matrix.
        - **LTV/CAC Goal:** > 3.0
        """
    else:
        strategy = """
        📦 **D2C Matrix (allmate):**
        - **Revenue Model:** Direct-to-consumer digital storefront.
        - **Margin Target:** 60%+ gross margin on apparel and EDC gear.
        - **Growth Loop:** Limited "drop" model to drive scarcity and organic social sharing.
        - **AOV (Average Order Value):** Targeting ₹2,500+ per checkout.
        """
        
    return f"💸 **Business Model Synthesized:**\n{strategy}"
