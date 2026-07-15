# tools/advanced_hardware_dept/thermal_heat_mapper.py

def calculate_component_temp(power_dissipated_watts: float, surface_area_m2: float, ambient_temp_c: float = 25.0) -> str:
    """Estimates baseline component surface temperature using a simplified convection model."""
    
    # Standard natural convection heat transfer coefficient (h) ~ 10 W/(m²K)
    h_convection = 10.0 
    
    if surface_area_m2 <= 0:
        return "⚠️ Surface area must be positive."
        
    delta_t = power_dissipated_watts / (h_convection * surface_area_m2)
    final_temp = ambient_temp_c + delta_t
    
    status = "🔥 CRITICAL: Requires active cooling (fan/heatsink)." if final_temp > 85.0 else "🟢 STABLE: Passive cooling sufficient."
    
    return f"""
    🌡️ **Thermal Dissipation Matrix:**
    - Power Load: {power_dissipated_watts} W
    - Ambient Temperature: {ambient_temp_c}°C
    
    **Thermal Forecast:**
    - Steady-State Surface Temp: **{final_temp:.1f}°C**
    - Assessment: {status}
    """
