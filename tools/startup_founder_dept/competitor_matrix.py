# tools/startup_founder_dept/competitor_matrix.py
import json

def build_competitive_analysis(your_brand: str, competitors: list) -> str:
    """Compiles a feature-by-feature battlecard against rival companies."""
    
    # Generic matrix for structural output
    matrix = {
        your_brand: {"Price": "Aggressive", "Tech": "Agentic/Custom", "Design": "Premium", "Speed": "High"},
    }
    
    for comp in competitors:
        matrix[comp] = {"Price": "High", "Tech": "Legacy", "Design": "Standard", "Speed": "Slow"}
        
    return f"""
    🤺 **Competitive Battlecard Compiled:**
    ```json
    {json.dumps(matrix, indent=4)}
    ```
    *Insight: Emphasize 'Agentic Tech' and 'Speed' during the pitch to differentiate.*
    """
