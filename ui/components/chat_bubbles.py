# ui/components/chat_bubbles.py
# Formats ctrl outputs into distinct visual blocks

def format_system_alert(message: str) -> str:
    """Formats text as a critical system alert (Red/Orange)."""
    return f"""
    <div style="border-left: 4px solid #ff4444; background: rgba(255,68,68,0.1); padding: 12px; border-radius: 4px; color: #ff4444; font-family: monospace;">
        <strong>⚠️ SYSTEM ALERT:</strong><br/>
        {message}
    </div>
    """

def format_success_block(title: str, message: str) -> str:
    """Formats text as a successful matrix execution (Green)."""
    return f"""
    <div style="border: 1px solid rgba(0,255,136,0.3); background: rgba(0,255,136,0.05); padding: 15px; border-radius: 8px;">
        <h4 style="color: #00ff88; margin-top: 0;">✅ {title}</h4>
        <p style="color: #e0e0e0; margin-bottom: 0;">{message}</p>
    </div>
    """

def format_code_review(reviewer: str, critique: str) -> str:
    """Formats the output of the Swarm Consensus debate."""
    return f"""
    <div style="background: #1e1e2e; border-radius: 6px; padding: 10px; margin: 10px 0; border-left: 3px solid #89b4fa;">
        <span style="color: #89b4fa; font-weight: bold; font-size: 0.9em;">[{reviewer}]:</span> 
        <span style="color: #cdd6f4;">{critique}</span>
    </div>
    """
