# tools/finance_agents/cap_table_mgr.py

def distribute_equity(founder_shares: dict, new_investment_amount: float, pre_money_valuation: float) -> str:
    """
    Simulates equity dilution when taking on outside capital.
    """
    try:
        post_money_val = pre_money_valuation + new_investment_amount
        investor_equity = new_investment_amount / post_money_val
        pool_remainder = 1.0 - investor_equity
        
        output = f"⚖️ **Capitalization Table Matrix (Post-Money: ₹{post_money_val:,.2f}):**\n\n"
        output += f"Incoming Investor Pool: {investor_equity * 100:.2f}%\n"
        
        for founder, initial_percentage in founder_shares.items():
            # Apply dilution ratio
            new_share = (initial_percentage / 100.0) * pool_remainder * 100
            output += f"- Founder ({founder}): {new_share:.2f}%\n"
            
        return output
    except ZeroDivisionError:
        return "⚠️ Cap Table Error: Valuation cannot be zero."
