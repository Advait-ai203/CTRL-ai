# tools/design_agents/figma_exporter.py
import json
import os

def generate_figma_nodes(frame_name: str) -> str:
    """Outputs JSON structure matching the Figma REST API node format."""
    target_dir = "./generated_assets/research_reports"
    os.makedirs(target_dir, exist_ok=True)
    
    figma_node = {
        "type": "FRAME",
        "name": frame_name,
        "background": [{"type": "SOLID", "color": {"r": 0.03, "g": 0.03, "b": 0.03, "a": 1}}],
        "children": [
            {
                "type": "TEXT",
                "characters": "System Active",
                "fills": [{"type": "SOLID", "color": {"r": 0, "g": 1, "b": 0.53, "a": 1}}]
            }
        ]
    }
    
    file_path = os.path.join(target_dir, f"{frame_name}_figma_nodes.json")
    with open(file_path, "w") as f:
        json.dump(figma_node, f, indent=4)
        
    return f"💠 **Figma Export Ready:** Node mapping saved to `{file_path}`"
