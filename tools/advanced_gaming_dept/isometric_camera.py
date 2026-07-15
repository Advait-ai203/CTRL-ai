# tools/advanced_gaming_dept/isometric_camera.py
import math

def project_to_isometric(x: float, y: float, z: float) -> tuple:
    """Transforms 3D world spaces into 2D screen coordinates using an isometric matrix projection."""
    # Standard 30-degree isometric projection formulas
    screen_x = (x - z) * math.cos(math.radians(30))
    screen_y = (x + z) * math.sin(math.radians(30)) - y
    
    return (round(screen_x, 2), round(screen_y, 2))
