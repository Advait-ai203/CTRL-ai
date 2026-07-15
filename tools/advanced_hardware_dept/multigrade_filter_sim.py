# tools/advanced_hardware_dept/multigrade_filter_sim.py

def simulate_mgf_performance(flow_rate_m3_hr: float, suspended_solids_ppm: float) -> str:
    """Calculates filtration efficiency and pressure drop for a Multigrade Filter (MGF)."""
    
    if flow_rate_m3_hr <= 0:
        return "⚠️ Simulation Error: Flow rate must be positive."
        
    # Baseline efficiency logic for layered filtration media
    base_efficiency = 0.98
    velocity_penalty = max(0.0, (flow_rate_m3_hr - 15.0) * 0.015)
    final_efficiency = max(0.60, base_efficiency - velocity_penalty)
    
    effluent_ppm = suspended_solids_ppm * (1.0 - final_efficiency)
    pressure_drop_bar = 0.2 + (flow_rate_m3_hr * 0.05)
    
    status = "🟢 OPTIMAL" if final_efficiency > 0.90 else "🟡 WARNING: High Velocity Clogging Risk"
    
    return f"""
    💧 **Multigrade Filter (MGF) Matrix Simulation:**
    - Input Flow Rate: {flow_rate_m3_hr} m³/hr
    - Influent TSS: {suspended_solids_ppm} ppm
    
    **Calculated Outputs:**
    - Filtration Efficiency: **{(final_efficiency * 100):.1f}%**
    - Effluent Quality: {effluent_ppm:.2f} ppm
    - Estimated Pressure Drop: {pressure_drop_bar:.2f} Bar
    
    *System Status:* {status}
    """
