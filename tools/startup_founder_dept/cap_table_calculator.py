# tools/startup_founder_dept/cap_table_calculator.py
# Evaluates venture ownership shares, investments, and equity scaling models

def calculate_dilution_metrics(founders_shares: dict, new_investment: float, pre_money_valuation: float) -> dict:
    """
    Simulates investment entry scenarios and handles corporate share division calculations.
    """
    try:
        post_money_val = pre_money_valuation + new_investment
        investor_equity = new_investment / post_money_val
        pool_remainder = 1.0 - investor_equity
        
        updated_table = {}
        for founder, initial_percentage in founders_shares.items():
            # Apply dilution ratio across internal shareholders
            updated_table[founder] = round(initial_percentage * pool_remainder * 100, 2)
            
        updated_table["Incoming Investor Pool"] = round(investor_equity * 100, 2)
        return {
            "financial_summary": {
                "pre_money": pre_money_valuation,
                "capital_injected": new_investment,
                "post_money": post_money_val
            },
            "equity_allotments_percentage": updated_table
        }
    except ZeroDivisionError:
        return {"error": "Valuation matrix calculation boundary cannot equate to zero."}
