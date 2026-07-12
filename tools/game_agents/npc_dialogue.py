# tools/game_agents/npc_dialogue.py
import json
import os

def compile_dialogue_tree(npc_name: str, dialogues: dict) -> str:
    """Compiles multi-branch NPC dialogue into a JSON dialogue tree."""
    target_dir = "./generated_assets/game_builds/dialogue"
    os.makedirs(target_dir, exist_ok=True)
    
    dialogue_file = {
        "metadata": {"npc_id": npc_name.lower(), "author": "ctrl_matrix_lead_advait"},
        "nodes": dialogues
    }
    
    file_path = os.path.join(target_dir, f"{npc_name.lower()}_tree.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(dialogue_file, f, indent=4)
        
    return f"💬 **NPC Dialogue Tree Compiled:** `{npc_name}` logic saved to `{file_path}`"
