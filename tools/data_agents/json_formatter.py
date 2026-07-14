# tools/data_agents/json_formatter.py
import json

def format_json_string(raw_string: str, indent: int = 4) -> str:
    """Validates raw text string inputs and outputs pretty-printed structural JSON."""
    try:
        parsed = json.loads(raw_string)
        return json.dumps(parsed, indent=indent)
    except json.JSONDecodeError as je:
        return f"❌ Invalid JSON Syntax: {str(je)}"
    except Exception as e:
        return f"⚠️ Formatting Error: {str(e)}"
