# tools/iot_agents/sensor_reader.py
import random
import datetime

def read_dht11_sensor(sensor_id: str) -> str:
    """Polls a simulated DHT11 temperature/humidity sensor."""
    
    # Simulating standard Delhi climate data
    temp_c = round(random.uniform(28.0, 35.5), 1)
    humidity = round(random.uniform(40.0, 65.0), 1)
    timestamp = datetime.datetime.now().strftime("%H:%M:%S")
    
    status = "🟢 OPTIMAL" if temp_c < 32.0 else "🟡 WARM"
    
    return f"""
    🌡️ **Sensor Matrix Telemetry ({sensor_id}):**
    - Timestamp: {timestamp}
    - Ambient Temperature: {temp_c}°C
    - Relative Humidity: {humidity}%
    
    *Hardware Status: {status}*
    """
