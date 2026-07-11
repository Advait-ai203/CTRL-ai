# tools/system_web_dept/network_scanner.py
import socket

def scan_network_port(host: str, port: int) -> str:
    """Attempts a socket connection to verify if a specific port is open on a host."""

    # Strip http:// or https:// if the AI accidentally passes it
    clean_host = host.replace("http://", "").replace("https://", "").split('/')[0]

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2.0) # 2 second timeout so the UI doesn't hang forever

        result = sock.connect_ex((clean_host, port))
        sock.close()

        if result == 0:
            return f"🌐 **Network Scan:** Port `{port}` on `{clean_host}` is **OPEN** and responding."
        else:
            return f"🚫 **Network Scan:** Port `{port}` on `{clean_host}` is **CLOSED** or blocking connections."

    except socket.gaierror:
        return f"⚠️ DNS Error: Could not resolve hostname `{clean_host}`."
    except Exception as e:
        return f"Network Scanner Fault: {str(e)}"
