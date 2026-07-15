# tools/iot_agents/mqtt_broker.py

def generate_mqtt_config(broker_url: str, client_id: str = "ctrl_master_node") -> str:
    """Generates the connection configuration for an MQTT messaging broker."""
    
    config = f"""
    🔌 **MQTT Broker Connection Matrix Locked:**
    - Client ID: `{client_id}`
    - Broker URL: `tcp://{broker_url}:1883`
    - Keep-Alive: 60 seconds
    
    *Implementation Note:* Use `pip install paho-mqtt` to bind this configuration to your local Python runtime.
    Subscribe to `allmate/inventory/#` or `ctrl/telemetry/#` for data streams.
    """
    return config
