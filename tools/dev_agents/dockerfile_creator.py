# tools/dev_agents/dockerfile_creator.py
import os

def generate_dockerfile(runtime: str, entrypoint: str) -> str:
    """Writes a secure, lightweight Docker container specification."""
    target_dir = "./generated_assets/web_builds/docker"
    os.makedirs(target_dir, exist_ok=True)
    
    if "python" in runtime.lower():
        base_image = "python:3.11-slim"
        install_cmd = "COPY requirements.txt .\nRUN pip install --no-cache-dir -r requirements.txt"
    elif "node" in runtime.lower():
        base_image = "node:18-alpine"
        install_cmd = "COPY package*.json ./\nRUN npm install --production"
    else:
        base_image = "ubuntu:22.04"
        install_cmd = "# Add custom installation commands here"

    docker_code = f"""# ctrl Matrix Containerization
FROM {base_image}

WORKDIR /app
{install_cmd}

COPY . .

# Security: Run as non-root user
RUN useradd -m ctrl_user
USER ctrl_user

CMD ["{entrypoint}"]
"""
    file_path = os.path.join(target_dir, "Dockerfile")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(docker_code)
        
    return f"🐳 **Docker Matrix Initialized:** Container spec saved to `{file_path}`"
