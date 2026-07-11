# tools/engineering_dept/gcode_compiler.py
import os

def compile_gcode(layer_height: float, print_speed: int) -> str:
    """Generates standard G-Code boilerplate for CNC and 3D printing operations."""
    target_dir = "./generated_assets/models"
    os.makedirs(target_dir, exist_ok=True)

    gcode = f"""
; ctrl Matrix - G-Code Generator
; Layer Height: {layer_height}mm
; Print Speed: {print_speed}mm/s
G28 ; Home all axes
G1 Z15.0 F6000 ; Move Z axis up
G92 E0 ; Reset extruder
G1 F200 E3 ; Extrude filament
G92 E0
; --- BEGIN LAYER OPERATIONS ---
G1 X50 Y50 Z{layer_height} F{print_speed}
G1 X100 Y50 E1.5
G1 X100 Y100 E3.0
G1 X50 Y100 E4.5
G1 X50 Y50 E6.0
"""
    file_path = f"{target_dir}/print_job.gcode"
    with open(file_path, "w") as f:
        f.write(gcode)

    return f"🖨️ **G-Code Compiled:** Ready for 3D printing at `{file_path}`"
