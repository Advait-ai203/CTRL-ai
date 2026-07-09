# tools/finance_dept/budget_tracker.py
# Processes cloud usage metrics, tool cost thresholds, and runtime overhead

def evaluate_runway_status(current_pool: float, fixed_costs_monthly: dict, dynamic_buffer: float = 0.0) -> dict:
    """Calculates financial health, burning rates, and remaining time on operational pipelines."""
    total_monthly_burn = sum(fixed_costs_monthly.values()) + dynamic_buffer
    
    try:
        months_remaining = current_pool / total_monthly_burn
        return {
            "monthly_burn_rate": total_monthly_burn,
            "operational_runway_months": round(months_remaining, 2),
            "safety_status": "NOMINAL" if months_remaining >= 6 else "WARNING_LOW_RUNWAY"
        }
    except ZeroDivisionError:
        return {"error": "Burn threshold cannot settle on zero base rules."}
