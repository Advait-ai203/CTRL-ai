# tools/marketing_agents/ab_test_mgr.py

def evaluate_ab_test(variant_a_clicks: int, variant_a_conversions: int, variant_b_clicks: int, variant_b_conversions: int) -> str:
    """Compares conversion rates of two marketing assets to declare a winner."""
    
    rate_a = (variant_a_conversions / variant_a_clicks) * 100 if variant_a_clicks > 0 else 0
    rate_b = (variant_b_conversions / variant_b_clicks) * 100 if variant_b_clicks > 0 else 0
    
    if rate_a > rate_b:
        winner = "Variant A"
        diff = rate_a - rate_b
    elif rate_b > rate_a:
        winner = "Variant B"
        diff = rate_b - rate_a
    else:
        return "⚖️ **A/B Test Result:** Statistical Tie. Both variants performed equally."
        
    return f"""
    🧪 **A/B Split Test Results:**
    - Variant A Conversion Rate: {rate_a:.2f}%
    - Variant B Conversion Rate: {rate_b:.2f}%
    
    🏆 **Winner:** {winner} (outperformed by {diff:.2f}%)
    *Recommendation: Route 100% of traffic to {winner}.*
    """
