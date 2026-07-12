# tools/game_agents/sprite_generator.py
import os
import random

def generate_pixel_sprite(entity_name: str, color_hex: str = "#00FF88") -> str:
    """Generates a procedural 8x8 symmetrical pixel-art sprite matrix."""
    target_dir = "./generated_assets/game_builds/sprites"
    os.makedirs(target_dir, exist_ok=True)
    
    # Generate a random 8x4 matrix and mirror it for symmetry (classic space invader style)
    half_grid = [[random.choice([0, 1]) for _ in range(4)] for _ in range(8)]
    full_grid = [row + row[::-1] for row in half_grid]
    
    # Convert matrix to a visual string representation
    visual_map = "\n".join(["".join(["██" if pixel else ".." for pixel in row]) for row in full_grid])
    
    # In a full production setup, this would also write an actual PNG or SVG file.
    file_path = os.path.join(target_dir, f"{entity_name}_map.txt")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Color: {color_hex}\n\n{visual_map}")
        
    return f"""
    👾 **Procedural Sprite Generated:** `{entity_name}`
    ```text
    {visual_map}
    ```
    *Sprite matrix saved to `{file_path}`*
    """
