# tools/advanced_gaming_dept/procedural_map_gen.py
import random

def generate_cellular_layer(width: int, height: int, fill_probability: float = 0.45) -> list:
    """Generates a raw pseudo-random matrix map for cellular automata simulation processing."""
    matrix = []
    for y in range(height):
        row = []
        for x in range(width):
            # Enforce edge boundaries
            if x == 0 or x == width - 1 or y == 0 or y == height - 1:
                row.append(1)  # Solid wall boundary
            else:
                row.append(1 if random.random() < fill_probability else 0)
        matrix.append(row)
    return matrix
