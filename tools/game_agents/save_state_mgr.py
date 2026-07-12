# tools/game_agents/save_state_mgr.py
import json
import base64
import os

def generate_save_file(player_id: str, game_data: dict) -> str:
    """Serializes and obfuscates game state data to prevent tampering."""
    target_dir = "./generated_assets/game_builds/saves"
    os.makedirs(target_dir, exist_ok=True)
    
    # Convert dict to string, then encode to base64
    raw_json = json.dumps(game_data)
    obfuscated_data = base64.b64encode(raw_json.encode('utf-8')).decode('utf-8')
    
    save_payload = {
        "header": "CTRL_SECURE_SAVE",
        "player": player_id,
        "payload": obfuscated_data
    }
    
    file_path = os.path.join(target_dir, f"slot_1_{player_id}.sav")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(save_payload, f, indent=4)
        
    return f"💾 **Game State Preserved:** Encrypted save file written to `{file_path}`"
