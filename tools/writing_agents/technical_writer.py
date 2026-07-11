# tools/writing_agents/technical_writer.py
import os

def generate_documentation(code_snippet: str, module_name: str) -> str:
    """Parses code blocks and generates standard Markdown documentation."""
    target_dir = "./generated_assets/research_reports"
    os.makedirs(target_dir, exist_ok=True)

    doc_template = f"""# {module_name.upper()} Documentation

## Overview
Automatically generated technical spec for `{module_name}`.

## Functions & Logic
The provided matrix handles operational logic and execution pathways.

## Implementation
```python
{code_snippet[:200]} # Truncated for preview
""" file_path = os.path.join(target_dir, f"{module_name}_docs.md") with open(file_path, "w", encoding="utf-8") as f: f.write(doc_template)

return f"📄 **Technical Docs Compiled:** Saved Markdown spec to `{file_path}`"
