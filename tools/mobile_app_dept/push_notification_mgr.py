# tools/mobile_app_dept/push_notification_mgr.py
import json

def format_push_payload(device_token: str, title: str, body: str) -> str:
    """Formats the FCM JSON structure to broadcast lock-screen notifications."""
    
    payload = {
        "message": {
            "token": device_token,
            "notification": {
                "title": title,
                "body": body
            },
            "android": {
                "priority": "high",
                "notification": {
                    "color": "#00FF88",
                    "sound": "default"
                }
            }
        }
    }
    
    return f"🔔 **FCM Push Matrix Staged:**\n```json\n{json.dumps(payload, indent=4)}\n```"
