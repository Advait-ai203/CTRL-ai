# tools/education_tech_dept/project_rubric_maker.py
import json

def compile_grading_rubric(project_title: str) -> str:
    """Outputs a standard 4-point grading rubric for project evaluation."""
    
    rubric = {
        "project": project_title,
        "criteria": [
            {
                "category": "Technical Execution",
                "weight": "40%",
                "4_points": "Code is bug-free, highly optimized, and follows architectural standards.",
                "1_point": "Code fails to compile or crashes frequently."
            },
            {
                "category": "Design & UI",
                "weight": "30%",
                "4_points": "Interface is intuitive, accessible, and matches brand guidelines.",
                "1_point": "Interface is broken, unstyled, or unusable."
            },
            {
                "category": "Innovation",
                "weight": "30%",
                "4_points": "Provides a unique, out-of-the-box solution to the core problem.",
                "1_point": "Derivative work with no clear value addition."
            }
        ]
    }
    
    return f"📐 **Assessment Rubric Generated ({project_title}):**\n```json\n{json.dumps(rubric, indent=4)}\n```"
