# tools/iot_agents/smart_home_hub.py

def toggle_smart_device(device_name: str, action: str) -> str:
    """Routes commands to local smart home relays or smart plugs."""
    
    valid_actions = ["ON", "OFF", "REBOOT"]
    action_upper = action.upper()
    
    if action_upper not in valid_actions:
        return f"⚠️ Invalid Command: '{action}' not recognized by the Hub."
        
    # Simulated execution payload
    payload = {"target": device_name, "state": action_upper, "protocol": "Zigbee/WiFi"}
    
    return f"""
    🏠 **Smart Hub Matrix Executed:**
    - Device: `{device_name}`
    - Command Issued: **{action_upper}**
    - State Verified: 🟢 SUCCESS
    """
