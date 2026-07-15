# tools/iot_agents/arduino_serial.py

def mock_serial_write(com_port: str, command_string: str, baud_rate: int = 9600) -> str:
    """Simulates sending a string payload over a USB Serial connection to a microcontroller."""
    
    if not com_port.startswith("COM") and not com_port.startswith("/dev/tty"):
        return f"⚠️ Invalid Serial Port Format: {com_port}"
        
    return f"""
    🔌 **Serial Bus Matrix (Baud: {baud_rate}):**
    - Target Port: `{com_port}`
    - TX (Transmitted): `{command_string}`
    - RX (Received): `ACK_OK`
    
    *Connection closed cleanly.*
    """
