# tools/advanced_hardware_dept/cad_blueprint_exporter.py
import os

def export_geometry_manifest(part_name: str, dimensions_mm: dict) -> str:
    """Compiles dimensional data into a manufacturing-ready structural manifest."""
    target_dir = "./generated_assets/hardware_blueprints"
    os.makedirs(target_dir, exist_ok=True)
    
    manifest = f"""# CNC/3D PRINT MANIFEST: {part_name.upper()}
Format: G-Code / STEP Base Vector Parameters

## Primary Dimensions (mm)
- Length (X): {dimensions_mm.get('x', 0.0):.2f}
- Width  (Y): {dimensions_mm.get('y', 0.0):.2f}
- Height (Z): {dimensions_mm.get('z', 0.0):.2f}

## Tolerances
- General Machining: ±0.1mm
- Critical Bore Holes: ±0.05mm

[Exported by ctrl Matrix Architecture]
"""
    file_path = os.path.join(target_dir, f"{part_name}_manifest.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(manifest)
        
    return f"📐 **CAD Matrix Exported:** Blueprint staged at `{file_path}`"
