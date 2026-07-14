# tools/marketing_agents/ad_copy_gen.py

def generate_ad_copy(product_name: str, value_prop: str, framework: str = "AIDA") -> str:
    """Drafts advertising copy using standard marketing frameworks."""
    
    if framework.upper() == "PAS":
        copy = f"""
        **[Problem]** Tired of complex, broken systems slowing you down?
        **[Agitation]** Every minute spent debugging is a minute lost building your empire.
        **[Solution]** Meet {product_name}. {value_prop}. Click to upgrade your workflow today.
        """
    else:
        # Default AIDA (Attention, Interest, Desire, Action)
        copy = f"""
        **[Attention]** Ready to revolutionize how you work?
        **[Interest]** {product_name} is built for speed, precision, and scale.
        **[Desire]** Imagine having {value_prop} at your fingertips.
        **[Action]** Secure your early access right now. Link in bio.
        """
        
    return f"✍️ **Ad Copy Generated ({framework.upper()} Framework):**\n{copy}"
