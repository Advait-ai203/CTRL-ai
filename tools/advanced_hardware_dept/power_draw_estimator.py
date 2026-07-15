# tools/advanced_hardware_dept/power_draw_estimator.py

def estimate_battery_life(battery_capacity_mah: float, total_current_draw_ma: float) -> str:
    """Computes expected operational lifespan for battery-powered hardware."""
    
    if total_current_draw_ma <= 0:
        return "⚠️ Current draw must be strictly positive."
        
    # Standard battery de-rating factor (lithium-ion efficiency curve ~ 0.85)
    efficiency = 0.85 
    usable_capacity = battery_capacity_mah * efficiency
    
    hours_runtime = usable_capacity / total_current_draw_ma
    
    return f"""
    🔋 **Power Matrix Estimator:**
    - Battery Cell: {battery_capacity_mah} mAh (85% usable depth)
    - System Draw: {total_current_draw_ma} mA
    
    **Runtime Projection:**
    - Estimated Continuous Uptime: **{hours_runtime:.2f} Hours**
    """
