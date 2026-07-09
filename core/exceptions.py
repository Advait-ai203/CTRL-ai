# core/exceptions.py
# Global fault tolerance and error routing

import traceback

def global_error_handler(fault: Exception) -> str:
    """
    Catches any fatal system errors, prevents server crashes, 
    and formats a clean UI alert for the operator.
    """
    error_type = type(fault).__name__
    error_msg = str(fault)
    
    # We can print the deep traceback to the terminal for debugging
    print(f"\n[CRITICAL FAULT CAUGHT]: {error_type} - {error_msg}")
    traceback.print_exc()
    
    # Return a UI-friendly error block to the frontend
    return f"""
    <div style="border-left: 4px solid #ff4444; background: rgba(255,68,68,0.1); padding: 12px; border-radius: 4px; color: #ff4444; font-family: 'Courier New', monospace;">
        <strong>⚠️ CTRL SYSTEM ALERT: {error_type}</strong><br/>
        <span style="color: #e0e0e0; font-size: 14px;">The execution matrix encountered a critical fault.</span><br/>
        <span style="color: #ffaa00; font-size: 12px;">Trace: {error_msg}</span>
    </div>
    """
