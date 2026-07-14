# tools/design_agents/color_palette.py
import json

def generate_palette(theme: str = "cyberpunk") -> str:
    """Computes a 5-color hex palette based on the requested aesthetic."""

    palettes = {
        "cyberpunk": ["#0A0A0A", "#1E1E1E", "#00FF88", "#CF30AA", "#FFFFFF"],
        "minimalist": ["#FFFFFF", "#F5F5F5", "#333333", "#000000", "#007BFF"],
        "allmate_earth": ["#F4EBD0", "#B68D40", "#122620", "#D6AD60", "#FFFFFF"]
    }

    selected = palettes.get(theme.lower(), palettes["cyberpunk"])

    output = f"🎨 **Color Matrix Initialized ({theme.upper()}):**\n"
    output += f"- Background: `{selected[0]}`\n"
    output += f"- Surface: `{selected[1]}`\n"
    output += f"- Primary Accent: `{selected[2]}`\n"
    output += f"- Secondary Accent: `{selected[3]}`\n"
    output += f"- Text/Highlight: `{selected[4]}`\n"

    return output
