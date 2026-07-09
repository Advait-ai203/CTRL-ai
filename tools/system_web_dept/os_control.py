# tools/system_web_dept/os_control.py
# Grants ctrl direct access to the local operating system

import subprocess
import platform

def execute_os_control(command: str) -> str:
    """
    Executes a direct terminal/command-prompt instruction on the host machine.
    """
    system_os = platform.system()
    
    # 🛑 SECURITY: Hardcoded blocklist to prevent catastrophic self-deletion
    danger_words = ["rm -rf /", "del /f /s /q C:\\", "format"]
    if any(danger in command for danger in danger_words):
        return "🛑 **SECURITY OVERRIDE:** Destructive OS command blocked by auth_guard."

    try:
        # Run the command silently in the background and capture the output
        if system_os == "Windows":
            result = subprocess.run(["cmd", "/c", command], capture_output=True, text=True, timeout=15)
        else:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=15)
            
        output = result.stdout if result.stdout else result.stderr
        
        if not output:
            output = "Command executed successfully with no return output."
            
        return f"💻 **OS Execution Complete:**\n
http://googleusercontent.com/immersive_entry_chip/0

Which operational department should we wire up for the squad next? We can build out the `engineering_dept` to handle 3D generation, or dive into the `startup_founder_dept` to automate business pitch logic.
