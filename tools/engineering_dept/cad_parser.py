# tools/engineering_dept/cad_parser.py
# Utility for processing structural constraints and bounding dimensions

def recalculate_bounding_box(vertices_list: list) -> dict:
    """Calculates strict boundaries, volume coefficients, and spatial properties from an array of coordinates."""
    if not vertices_list:
        return {"error": "Missing coordinates block."}
        
    try:
        x_coords = [v[0] for v in vertices_list]
        y_coords = [v[1] for v in vertices_list]
        z_coords = [v[2] for v in vertices_list]
        
        dims = {
            "width_x": max(x_coords) - min(x_coords),
            "length_y": max(y_coords) - min(y_coords),
            "height_z": max(z_coords) - min(z_coords)
        }
        dims["total_volume_units"] = dims["width_x"] * dims["length_y"] * dims["height_z"]
        return dims
    except Exception as e:
        return {"error": f"Mathematical mapping fault: {str(e)}"}
