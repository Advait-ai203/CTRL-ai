# tools/advanced_hardware_dept/schematic_diagram_gen.py

def draw_flow_schematic(input_node: str, process_node: str, output_node: str) -> str:
    """Generates a text-based structural diagram of a hardware system flow."""
    
    diagram = f"""
    🔌 **Hardware Flow Schematic:**
    
      [ PWR / {input_node.upper()} ] 
           │
           ▼
     ┌───────────┐
     │           │
     │ {process_node.center(9)} │
     │           │
     └───────────┘
           │
           ▼
    [ OUT / {output_node.upper()} ]
    """
    return diagram
