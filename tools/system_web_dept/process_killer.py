# tools/system_web_dept/process_killer.py
import psutil

def terminate_process(process_name: str) -> str:
    """Finds and forcefully terminates a running OS process by name."""

    # 🛑 SECURITY: Blocklist of critical system processes you should never kill
    protected_processes = ["svchost.exe", "explorer.exe", "system", "registry", "smss.exe"]
    if process_name.lower() in protected_processes:
        return f"🛑 **SECURITY OVERRIDE:** Process '{process_name}' is a protected system file. Termination blocked."

    terminated_count = 0
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] and process_name.lower() in proc.info['name'].lower():
                proc.kill()
                terminated_count += 1

        if terminated_count > 0:
            return f"⚔️ **Process Terminated:** Successfully killed {terminated_count} instance(s) of `{process_name}`."
        else:
            return f"⚠️ Process Not Found: No active application matching `{process_name}` is currently running."

    except psutil.AccessDenied:
        return f"⚠️ Access Denied: ctrl does not have admin privileges to kill `{process_name}`."
    except Exception as e:
        return f"Process Killer Fault: {str(e)}"
