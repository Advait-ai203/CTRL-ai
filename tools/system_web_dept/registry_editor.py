# tools/system_web_dept/registry_editor.py
import platform

def read_registry_key(hive: str, key_path: str, value_name: str) -> str:
    """Reads a specific value from the Windows Registry."""

    if platform.system() != "Windows":
        return "⚠️ OS Compatibility Error: Registry Editor only functions on Windows machines."

    try:
        import winreg

        # Map string inputs to actual winreg hive objects
        hives = {
            "HKCU": winreg.HKEY_CURRENT_USER,
            "HKLM": winreg.HKEY_LOCAL_MACHINE,
            "HKCR": winreg.HKEY_CLASSES_ROOT
        }

        target_hive = hives.get(hive.upper())
        if not target_hive:
            return f"⚠️ Registry Error: Unknown Hive '{hive}'. Use HKCU, HKLM, or HKCR."

        # Open the key in strictly Read-Only mode
        with winreg.OpenKey(target_hive, key_path, 0, winreg.KEY_READ) as key:
            value, reg_type = winreg.QueryValueEx(key, value_name)

        return f"""
        ⚙️ **Registry Query Successful:**
        - **Path:** {hive}\\{key_path}
        - **Value Name:** {value_name}
        - **Data:** {value}
        """
    except FileNotFoundError:
        return f"⚠️ Registry Target Missing: Could not find `{key_path}\\{value_name}`."
    except PermissionError:
        return "⚠️ Access Denied: ctrl requires Administrator privileges to read this key."
    except Exception as e:
        return f"Registry Editor Fault: {str(e)}"
