# tools/startup_founder_dept/cap_table_simulator.py

def simulate_acquisition_payout(exit_valuation: float, founder_equity_percent: float, investor_equity_percent: float) -> str:
    """Models the financial payout distribution during a liquidity event."""
    
    if founder_equity_percent + investor_equity_percent > 100:
        return "⚠️ Cap Table Error: Total equity cannot exceed 100%."
        
    founder_payout = exit_valuation * (founder_equity_percent / 100)
    investor_payout = exit_valuation * (investor_equity_percent / 100)
    option_pool = exit_valuation - (founder_payout + investor_payout)
    
    return f"""
    💰 **Liquidity Event Matrix:**
    - Exit Valuation: ₹{exit_valuation:,.2f}
    
    **Payout Distribution:**
    - Founder Pool ({founder_equity_percent}%): **₹{founder_payout:,.2f}**
    - Investor Pool ({investor_equity_percent}%): **₹{investor_payout:,.2f}**
    - Employee Option Pool: **₹{option_pool:,.2f}**
    """
