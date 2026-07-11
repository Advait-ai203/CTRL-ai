# tools/dev_agents/ci_cd_pipeline.py
import os

def generate_github_action(project_type: str) -> str:
    """Scaffolds a GitHub Actions YAML file for continuous integration."""
    target_dir = "./generated_assets/web_builds/.github/workflows"
    os.makedirs(target_dir, exist_ok=True)
    
    yaml_code = f"""name: ctrl Matrix CI/CD - {project_type.upper()}

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    - name: Initialize Matrix Environment
      run: echo "Booting {project_type} deployment pipeline..."
    # Custom matrix execution steps follow below
"""
    file_path = os.path.join(target_dir, "main_pipeline.yml")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(yaml_code)
        
    return f"⚡ **CI/CD Pipeline Computed:** Workflow saved to `{file_path}`"
