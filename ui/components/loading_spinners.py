# ui/components/loading_spinners.py
# Displays dynamic loading states while AI models process

def get_radar_spinner(text: str = "Scanning Matrix...") -> str:
    """Returns HTML for a high-tech radar scanning animation."""
    return f"""
    <div style="display: flex; align-items: center; gap: 15px; padding: 15px; color: #00ff88; font-family: monospace;">
        <div style="width: 24px; height: 24px; border: 2px solid #00ff88; border-radius: 50%; border-top-color: transparent; animation: spin 1s linear infinite;"></div>
        <style>@keyframes spin {{ 100% {{ transform: rotate(360deg); }} }}</style>
        <span>{text}</span>
    </div>
    """

def get_pulse_loader(text: str = "Compiling Data...") -> str:
    """Returns HTML for a breathing pulse animation."""
    return f"""
    <div style="display: flex; align-items: center; gap: 10px; color: #89b4fa; font-family: sans-serif;">
        <div style="width: 10px; height: 10px; background: #89b4fa; border-radius: 50%; animation: pulse 1.5s infinite;"></div>
        <div style="width: 10px; height: 10px; background: #89b4fa; border-radius: 50%; animation: pulse 1.5s infinite 0.2s;"></div>
        <div style="width: 10px; height: 10px; background: #89b4fa; border-radius: 50%; animation: pulse 1.5s infinite 0.4s;"></div>
        <style>@keyframes pulse {{ 0%, 100% {{ opacity: 0.3; transform: scale(0.8); }} 50% {{ opacity: 1; transform: scale(1.2); }} }}</style>
        <span style="margin-left: 10px;">{text}</span>
    </div>
    """
