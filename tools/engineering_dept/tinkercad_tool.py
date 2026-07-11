# tools/engineering_dept/tinkercad_tool.py
import json
import os

def generate_tinkercad_primitive(shape_type: str, dimensions: dict) -> str:
    """Generates a primitive geometric structure for rapid CAD prototyping."""
    target_dir = "./generated_assets/models"
    os.makedirs(target_dir, exist_ok=True)

    cad_data = {
        "metadata": {"generator": "ctrl_matrix", "type": "tinkercad_primitive"},
        "object": {
            "type": shape_type,
            "parameters": dimensions,
            "material": "solid_default"
        }
    }

    file_path = f"{target_dir}/primitive_{shape_type}.json"
    with open(file_path, "w") as f:
        json.dump(cad_data, f, indent=4)

    return f"📐 **Rapid Prototype Generated:** Geometric data saved to `{file_path}`"
