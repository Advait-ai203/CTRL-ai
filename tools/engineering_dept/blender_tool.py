# tools/engineering_dept/blender_tool.py
import os

def execute_blender_tool(mesh_instructions: str, file_name: str = "ctrl_model") -> str:
    """Generates a Blender Python script to automate 3D modeling."""
    target_dir = "./generated_assets/models"
    os.makedirs(target_dir, exist_ok=True)

    script_content = f"""import bpy

# ctrl Matrix - Automated Mesh Generation
# Clear existing scene
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.delete(use_global=False)

# Execute AI Matrix Instructions
{mesh_instructions}

# Save output
bpy.ops.wm.save_as_mainfile(filepath="{target_dir}/{file_name}.blend")
"""
    file_path = f"{target_dir}/{file_name}_script.py"
    with open(file_path, "w") as f:
        f.write(script_content)

    return f"🧊 **Blender Matrix Initialized:** Automation script saved to `{file_path}`. Run this via Blender terminal to generate the 3D asset."
