# tools/advanced_gaming_dept/pathfinding_ai.py

def calculate_manhattan_heuristic(start_coord: tuple, end_coord: tuple) -> int:
    """Computes basic grid pathfinding heuristic value using absolute Manhattan distance calculation."""
    x1, y1 = start_coord
    x2, y2 = end_coord
    return abs(x1 - x2) + abs(y1 - y2)
