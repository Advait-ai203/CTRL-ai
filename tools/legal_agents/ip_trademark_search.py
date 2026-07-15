# tools/legal_agents/ip_trademark_search.py

def check_trademark_availability(brand_name: str, industry_class: str) -> str:
    """Simulates a database check for brand name conflicts."""
    
    # Simulating the matrix logic
    high_risk_names = ["apple", "meta", "google", "ctrl", "nike"]
    
    if brand_name.lower() in high_risk_names and industry_class.lower() in ["software", "tech"]:
        return f"❌ **IP Conflict Detected:** The mark '{brand_name.upper()}' has highly probable conflicts in the {industry_class} class. Expect legal friction."
        
    return f"✅ **IP Matrix Clear:** No immediate major conflicts found for '{brand_name.upper()}' in class {industry_class}. *Note: Conduct a formal registry search before filing.*"
