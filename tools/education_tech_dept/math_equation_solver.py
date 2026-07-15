# tools/education_tech_dept/math_equation_solver.py
import re

def solve_linear_equation(equation: str) -> str:
    """
    Parses and solves basic linear equations of the form 'ax + b = c'.
    Example input: '2x + 4 = 10'
    """
    try:
        # Strip spaces and normalize
        eq = equation.replace(" ", "").lower()
        
        # Basic regex to extract a, b, c from ax+b=c or ax-b=c
        match = re.match(r'(-?\d*)x([+-]\d+)?=(-?\d+)', eq)
        if not match:
            return "⚠️ Matrix Error: Equation must be in the format 'ax + b = c'."
            
        a_str, b_str, c_str = match.groups()
        
        a = float(a_str) if a_str not in ['', '-'] else (-1.0 if a_str == '-' else 1.0)
        b = float(b_str) if b_str else 0.0
        c = float(c_str)
        
        x = (c - b) / a
        
        return f"""
        ➗ **Algebraic Matrix Engine:**
        - Input: `{equation}`
        - Computation: x = ({c} - {b}) / {a}
        - Result: **x = {x}**
        """
    except Exception as e:
        return f"🛑 Solver Fault: {str(e)}"
