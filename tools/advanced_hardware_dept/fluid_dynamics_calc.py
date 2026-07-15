# tools/advanced_hardware_dept/fluid_dynamics_calc.py

def calculate_reynolds_number(velocity_m_s: float, pipe_diameter_m: float, kinematic_viscosity: float = 1.004e-6) -> str:
    """
    Computes fluid flow characteristics. 
    Default viscosity is set to water at 20°C (1.004 x 10^-6 m²/s).
    """
    
    reynolds_number = (velocity_m_s * pipe_diameter_m) / kinematic_viscosity
    
    if reynolds_number < 2000:
        flow_type = "Laminar Flow (Smooth)"
    elif 2000 <= reynolds_number <= 4000:
        flow_type = "Transient Flow (Unpredictable)"
    else:
        flow_type = "Turbulent Flow (Chaotic)"
        
    return f"""
    🌊 **Fluid Dynamics Matrix:**
    - Pipe Diameter: {pipe_diameter_m * 1000} mm
    - Flow Velocity: {velocity_m_s} m/s
    
    **Results:**
    - Reynolds Number (Re): **{reynolds_number:,.0f}**
    - Flow Characteristic: **{flow_type}**
    """
