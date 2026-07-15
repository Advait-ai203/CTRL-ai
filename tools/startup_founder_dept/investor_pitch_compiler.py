# tools/startup_founder_dept/investor_pitch_compiler.py
import os

def compile_pitch_narrative(brand_focus: str, target_investor: str = "Metrolite Chairman") -> str:
    """Structures a complete presentation narrative for high-level board pitches."""
    target_dir = "./generated_assets/research_reports/founder_desk"
    os.makedirs(target_dir, exist_ok=True)
    
    if brand_focus.lower() == "ctrl":
        problem_statement = "Legacy software development is slow, fragmented, and lacks agentic automation."
        solution = "A unified, AI-driven matrix architecture that accelerates deployment by 10x."
    else:
        problem_statement = "The everyday carry and streetwear market lacks cohesive, utility-first design."
        solution = "Premium, highly functional physical goods engineered for daily utility."

    deck = f"""# MASTER PITCH OUTLINE: {brand_focus.upper()}
**Prepared for:** {target_investor}
**Architect:** Advait

1. **The Hook:** We are a dual-threat startup studio.
2. **The Problem:** {problem_statement}
3. **The Solution:** {solution}
4. **The Market:** Multi-billion dollar TAM ready for disruption.
5. **The Squad:** A lean, 3-person operation executing faster than legacy teams.
6. **The Ask:** Strategic capital injection to scale our server infrastructure and initial manufacturing run.
"""
    file_path = os.path.join(target_dir, f"{brand_focus}_Pitch_Narrative.md")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(deck)
        
    return f"🗣️ **Pitch Compiled:** Narrative flow saved to `{file_path}`"
