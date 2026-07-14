# tools/team_agents/wiki_generator.py
import os

def compile_master_wiki() -> str:
    """Scans the research_reports directory and builds a central index linking all documentation."""
    source_dir = "./generated_assets/research_reports"
    wiki_path = os.path.join(source_dir, "MASTER_WIKI.md")
    
    if not os.path.exists(source_dir):
        return "⚠️ Wiki Compilation Error: No research_reports directory found."
        
    files = [f for f in os.listdir(source_dir) if f.endswith('.md') and f != "MASTER_WIKI.md"]
    
    wiki_content = "# 🧠 ctrl Startup Studio: Central Wiki\n\n## Master Index\n"
    
    if not files:
        wiki_content += "*No documentation files detected in the matrix yet.*\n"
    else:
        for file in files:
            wiki_content += f"- [{file}](./{file})\n"
            
    with open(wiki_path, "w", encoding="utf-8") as f:
        f.write(wiki_content)
        
    return f"📚 **Central Wiki Compiled:** Index mapped to `{wiki_path}`"
