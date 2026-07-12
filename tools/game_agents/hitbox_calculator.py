# tools/game_agents/hitbox_calculator.py

def check_aabb_collision(rect_a: dict, rect_b: dict) -> str:
    """
    Computes Axis-Aligned Bounding Box (AABB) overlap.
    Expects dicts with x, y, width, and height.
    """
    
    # AABB Logic: True if all axes overlap
    collision = (
        rect_a['x'] < rect_b['x'] + rect_b['width'] and
        rect_a['x'] + rect_a['width'] > rect_b['x'] and
        rect_a['y'] < rect_b['y'] + rect_b['height'] and
        rect_a['y'] + rect_a['height'] > rect_b['y']
    )
    
    if collision:
        return "💥 **Collision Detected:** Entities are currently intersecting."
    else:
        return "📏 **Space Clear:** No intersection detected between entities."
