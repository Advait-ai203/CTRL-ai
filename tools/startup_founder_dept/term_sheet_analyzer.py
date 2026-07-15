# tools/startup_founder_dept/term_sheet_analyzer.py

def analyze_term_sheet(text: str) -> str:
    """Scans proposed investment terms for common founder pitfalls."""
    
    pitfalls = {
        "participating preferred": "Double-dipping on exit payouts.",
        "3x liquidation": "Investors get 3x their money back before you see a dime.",
        "full ratchet": "Severe equity dilution for founders in down rounds.",
        "board control": "Potential loss of CEO voting power."
    }
    
    flags = []
    for term, warning in pitfalls.items():
        if term in text.lower():
            flags.append(f"- ⚠️ **{term.title()}**: {warning}")
            
    if not flags:
        return "✅ **Term Sheet Matrix:** No major predatory keywords detected. (Still requires legal review)."
        
    return f"🛑 **High-Risk Clauses Detected:**\n" + "\n".join(flags)
