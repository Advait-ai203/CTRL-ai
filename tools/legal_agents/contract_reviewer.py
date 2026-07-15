# tools/legal_agents/contract_reviewer.py

def analyze_contract_risk(contract_text: str) -> str:
    """Scans raw contract text for aggressive or non-standard legal clauses."""
    
    red_flags = ["perpetual", "irrevocable", "exclusive", "indemnify", "liquidated damages", "waive"]
    found_risks = [word for word in red_flags if word in contract_text.lower()]
    
    if not found_risks:
        return "✅ **Contract Scan:** Matrix found no standard red-flag terminology. Proceed with standard review."
        
    warnings = "\n".join([f"- ⚠️ Flagged term: '{word.upper()}'" for word in found_risks])
    
    return f"""
    🛑 **Contract Risk Analysis Matrix:**
    High-risk terminology detected in the provided text. 
    {warnings}
    
    *Action Required: Ensure you fully understand the scope of these clauses before signing.*
    """
