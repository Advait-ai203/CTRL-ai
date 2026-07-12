# tools/game_agents/level_designer.py
import random

def generate_tile_map(width: int = 20, height: int = 10, fill_density: float = 0.2) -> str:
    """Generates a procedural 2D tilemap using cellular density logic."""
    
    # 0 = Empty/Air, 1 = Solid Block
    level_grid = []
    for y in range(height):
        row = []
        for x in range(width):
            # Guarantee a solid floor
            if y == height - 1:
                row.append(1)
            else:
                row.append(1 if random.random() < fill_density else 0)
        level_grid.append(row)
        
    visual_grid = "\n".join(["".join(["🟩" if tile else "⬛" for tile in row]) for row in level_grid])
    
    return f"""
    🗺️ **Procedural Level Map Generated:**
    - Dimensions: {width}x{height}
    - Obstacle Density: {fill_density * 100}%
    
    {visual_grid}
    """
