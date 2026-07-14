# tools/marketing_agents/analytics_dashboard.py

def calculate_campaign_roas(ad_spend: float, revenue_generated: float) -> str:
    """Calculates Return on Ad Spend (ROAS) to determine campaign profitability."""
    
    if ad_spend <= 0:
        return "⚠️ Analytics Error: Ad spend must be greater than zero."
        
    roas = revenue_generated / ad_spend
    multiplier = roas * 100
    
    status = "🔥 HIGHLY PROFITABLE" if roas >= 3.0 else "⚠️ REVIEW CAMPAIGN" if roas < 1.0 else "🟢 PROFITABLE"
    
    return f"""
    📈 **Marketing Analytics Matrix:**
    - Total Ad Spend: ₹{ad_spend:,.2f}
    - Total Revenue: ₹{revenue_generated:,.2f}
    - ROAS: **{roas:.2f}x** ({multiplier:.0f}% Return)
    - System Assessment: {status}
    """
