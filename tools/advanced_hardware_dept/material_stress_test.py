# tools/advanced_hardware_dept/material_stress_test.py

def evaluate_tensile_stress(force_newtons: float, cross_section_area_mm2: float, material: str = "aluminum") -> str:
    """Calculates axial stress and compares it against material yield strengths."""
    
    yield_strengths_mpa = {
        "aluminum": 275.0,  # 6061-T6
        "titanium": 880.0,  # Grade 5
        "steel": 400.0,
        "nylon": 45.0
    }
    
    if cross_section_area_mm2 <= 0:
        return "⚠️ Area must be greater than 0."
        
    # Stress (MPa) = Force (N) / Area (mm²)
    applied_stress_mpa = force_newtons / cross_section_area_mm2
    material_limit = yield_strengths_mpa.get(material.lower(), 250.0)
    
    safety_factor = material_limit / applied_stress_mpa if applied_stress_mpa > 0 else float('inf')
    
    if safety_factor < 1.0:
        status = "🔴 FAILURE EMINENT: Material will plastically deform."
    elif safety_factor < 2.0:
        status = "🟡 MARGINAL: Operates too close to yield limit."
    else:
        status = "🟢 SAFE: Component is structurally sound."
        
    return f"""
    ⚙️ **Material Stress Matrix [{material.upper()}]:**
    - Applied Force: {force_newtons:,.1f} N
    - Applied Stress: {applied_stress_mpa:.1f} MPa
    - Material Yield Limit: {material_limit:.1f} MPa
    
    **Factor of Safety (FoS): {safety_factor:.2f}**
    *Assessment:* {status}
    """
