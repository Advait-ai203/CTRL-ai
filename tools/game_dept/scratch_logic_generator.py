# tools/game_dept/scratch_logic_generator.py
# Configures logical state arrays and interaction loops for custom logic maps

def structural_grid_map(rows: int = 20, cols: int = 20, element_positions: list = None) -> list:
    """Builds multi-dimensional bounding maps for canvas position rulesets."""
    # Build out an empty canvas boundary structure
    grid = [[0 for _ in range(cols)] for _ in range(rows)]
    
    if element_positions:
        for x, y, val in element_positions:
            if 0 <= x < rows and 0 <= y < cols:
                grid[x][y] = val
                
    return grid
