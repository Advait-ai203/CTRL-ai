# tools/finance_agents/burn_rate_monitor.py

def calculate_runway(current_cash_reserves: float, average_monthly_burn: float) -> str:
    """Evaluates venture capital runway and survival thresholds."""

    if average_monthly_burn <= 0:
        return "🟢 **Runway Status:** INFINITE (Matrix is cash-flow positive or neutral)."

    months_left = current_cash_reserves / average_monthly_burn

    status = "NOMINAL"
    if months_left < 3:
        status = "🔴 CRITICAL: Immediate capital injection required."
    elif months_left < 6:
        status = "🟡 WARNING: Begin fundraising cycle."

    return f"""
    🔥 **Burn Rate Diagnostics:**
    - Cash Reserves: ₹{current_cash_reserves:,.2f}
    - Monthly Burn: ₹{average_monthly_burn:,.2f}
    - Operational Runway: **{months_left:.1f} Months**
    - Alert Status: {status}
    """
