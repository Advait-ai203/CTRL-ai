# tools/productivity_agents/mindmap_gen.py

def generate_text_mindmap(root_node: str, sub_elements: list) -> str:
    """Compiles a logical structure tree out of central brainstorming ideas."""
    
    output = f"🧠 **Brainstorming Mindmap Architecture:**\n\n└── 📁 {root_node}\n"
    
    for idx, element in enumerate(sub_elements):
        prefix = "    ├── 📄 " if idx < len(sub_elements) - 1 else "    └── 📄 "
        output += f"{prefix}{element}\n"
        
    return output
