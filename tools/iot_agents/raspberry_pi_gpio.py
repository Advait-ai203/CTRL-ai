# tools/iot_agents/raspberry_pi_gpio.py

def toggle_gpio_pin(pin_number: int, state: bool) -> str:
    """Simulates RPi.GPIO logic to control physical board pins."""
    
    if pin_number < 1 or pin_number > 40:
        return "⚠️ GPIO Fault: Pin number out of bounds (1-40)."
        
    signal = "HIGH (3.3v)" if state else "LOW (0v)"
    action = "Activated" if state else "Deactivated"
    
    return f"""
    🍓 **Raspberry Pi GPIO Matrix:**
    - Target Pin: `BCM {pin_number}`
    - Signal Logic: {signal}
    - Hardware Response: Component {action}.
    """
  
