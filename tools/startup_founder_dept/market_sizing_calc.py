# tools/startup_founder_dept/market_sizing_calc.py

def calculate_tam_sam_som(total_market_value: float, reachable_percent: float, capture_goal_percent: float) -> str:
    """Computes the standard venture capital market sizing metrics in INR."""
    
    sam = total_market_value * (reachable_percent / 100)
    som = sam * (capture_goal_percent / 100)
    
    return f"""
    🌍 **Market Sizing Matrix (INR):**
    - **TAM (Total Addressable Market):** ₹{total_market_value:,.0f}
      *The absolute maximum potential if you captured 100% of the global market.*
      
    - **SAM (Serviceable Available Market):** ₹{sam:,.0f} ({reachable_percent}%)
      *The segment of the TAM targeted by your specific products/geography.*
      
    - **SOM (Serviceable Obtainable Market):** ₹{som:,.0f} ({capture_goal_percent}%)
      *The realistic revenue you intend to capture in the next 3-5 years.*
    """
