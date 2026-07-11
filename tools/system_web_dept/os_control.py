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

---

### 2. Live Web Scraper
**File:** `tools/system_web_dept/browser_tool.py`
This tool allows the AI to bypass its training data cutoff by reading live websites, scraping text, and ignoring visual clutter.

```python
# tools/system_web_dept/browser_tool.py
# Allows ctrl to crawl live websites and extract data

import requests
from bs4 import BeautifulSoup

def execute_browser_tool(url: str) -> str:
    """
    Pings a live website, strips away the messy HTML, 
    and returns pure readable text to the AI brain.
    """
    if not url.startswith("http"):
        return "⚠️ Browser Error: Invalid URL provided. Must start with http:// or https://"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            return f"⚠️ Connection Failed: Website returned status code {response.status_code}"

        soup = BeautifulSoup(response.text, 'html.parser')
        
        for script in soup(["script", "style"]):
            script.extract()
            
        raw_text = soup.get_text(separator=' ', strip=True)
        clean_text = raw_text[:4000] 
        
        return f"🌐 **Live Web Data Extracted from {url}:**\n\n{clean_text}...\n\n*(Data truncated for token limits)*"
        
    except requests.exceptions.Timeout:
        return f"⚠️ Browser Timeout: The website '{url}' took too long to respond."
    except Exception as e:
        return f"Web Scraper Fault: {str(e)}"
