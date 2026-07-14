# tools/team_agents/kpi_tracker.py

def log_weekly_kpis(brand: str, active_users: int, revenue: float, uptime_percentage: float) -> str:
    """Generates a snapshot of vital brand metrics."""
    
    status = "🟢 NOMINAL" if uptime_percentage > 99.0 and revenue > 0 else "🟡 NEEDS ATTENTION"
    
    return f"""
    📊 **Weekly KPI Snapshot: {brand.upper()}**
    - Active Users / Customers: {active_users:,}
    - Gross Revenue: ₹{revenue:,.2f}
    - System Uptime: {uptime_percentage}%
    
    **System Status:** {status}
    """
