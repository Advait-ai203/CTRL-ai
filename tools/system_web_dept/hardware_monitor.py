# tools/system_web_dept/hardware_monitor.py
import psutil

def get_system_telemetry() -> str:
    """Extracts live hardware usage metrics from the host machine."""
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        # Format bytes to Gigabytes
        ram_total_gb = ram.total / (1024 ** 3)
        ram_used_gb = ram.used / (1024 ** 3)
        disk_total_gb = disk.total / (1024 ** 3)
        disk_free_gb = disk.free / (1024 ** 3)

        return f"""
        📊 **ctrl Local Hardware Telemetry:**
        - **CPU Load:** {cpu_usage}%
        - **Memory (RAM):** {ram_used_gb:.1f}GB / {ram_total_gb:.1f}GB ({ram.percent}% used)
        - **Storage (Disk):** {disk_free_gb:.1f}GB free of {disk_total_gb:.1f}GB
        - **Status:** {"CRITICAL" if cpu_usage > 90 or ram.percent > 90 else "NOMINAL"}
        """
    except Exception as e:
        return f"⚠️ Hardware Sensor Fault: {str(e)}"
