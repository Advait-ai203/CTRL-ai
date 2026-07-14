# tools/accessibility_agents/voice_nav_setup.py
import json

def register_voice_commands() -> str:
    """Builds a JSON index mapping spoken navigation triggers to programmatic internal system calls."""
    commands_schema = {
        "system_engine": "voice-navigation-core",
        "commands": [
            {"trigger": "open dashboard", "action": "navigate_to_main_terminal()"},
            {"trigger": "run diagnostics", "action": "trigger_system_check()"},
            {"trigger": "execute deployment", "action": "compile_production_build()"},
            {"trigger": "scroll down", "action": "smooth_scroll_window('down')"}
        ]
    }
    
    return f"🎙️ **Voice Command Framework Initialized:**\n```json\n{json.dumps(commands_schema, indent=4)}\n```"
