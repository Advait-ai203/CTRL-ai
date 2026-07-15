# tools/iot_agents/device_pinger.py
import subprocess
import platform

def ping_iot_device(ip_address: str) -> str:
    """Executes an ICMP ping to verify if an IoT device is connected to the local network."""
    
    # Determine OS to set correct ping parameters
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', ip_address]
    
    try:
        # Suppress output for clean matrix logging
        response = subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        
        if response == 0:
            return f"📡 **Network Matrix:** Device at `{ip_address}` is ONLINE and responding."
        else:
            return f"⚠️ **Network Matrix:** Device at `{ip_address}` is OFFLINE (Unreachable)."
    except Exception as e:
        return f"🛑 Ping Execution Fault: {str(e)}"
