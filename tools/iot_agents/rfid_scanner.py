# tools/iot_agents/rfid_scanner.py
import datetime

def process_rfid_scan(tag_uid: str) -> str:
    """Decodes an RFID/NFC tag UID and logs it into the inventory matrix."""
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Simulated inventory database lookup
    inventory_db = {
        "04:5A:B2:71": "allmate Heavyweight Hoodie (Black/L)",
        "04:8C:99:12": "allmate EDC Utility Pouch",
        "04:11:F3:A9": "ctrl Matrix Developer Keycard"
    }
    
    item_identified = inventory_db.get(tag_uid.upper(), "UNKNOWN TAG - UNREGISTERED")
    
    return f"""
    📻 **RFID Scanner Matrix:**
    - Tag UID: `{tag_uid.upper()}`
    - Scan Time: {timestamp}
    - Object Identified: **{item_identified}**
    
    *Logged to central inventory.*
    """
