# tools/finance_agents/tax_calculator.py

def estimate_startup_tax(gross_revenue_inr: float, total_expenses_inr: float) -> str:
    """Calculates estimated net profit and standard corporate tax liabilities."""

    net_profit = gross_revenue_inr - total_expenses_inr

    if net_profit <= 0:
        return "🛡️ **Tax Matrix:** Startup is operating at a loss. No corporate tax liability calculated."

    # Baseline estimate (25% for standard domestic companies)
    estimated_tax = net_profit * 0.25
    net_after_tax = net_profit - estimated_tax

    return f"""
    🏛️ **Corporate Tax Estimation:**
    - Gross Revenue: ₹{gross_revenue_inr:,.2f}
    - Total Expenses: ₹{total_expenses_inr:,.2f}
    - Net Profit: ₹{net_profit:,.2f}

    **Estimated Tax Liability (25%):** ₹{estimated_tax:,.2f}
    **Projected Net Income:** ₹{net_after_tax:,.2f}
    """
