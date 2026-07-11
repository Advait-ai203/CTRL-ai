# tools/engineering_dept/kicad_circuit_gen.py
import os

def generate_pcb_netlist(board_name: str, components: list) -> str:
    """Compiles a standard netlist for PCB design and hardware routing."""
    target_dir = "./generated_assets/circuits"
    os.makedirs(target_dir, exist_ok=True)

    netlist = f"(export (version D)\n  (design\n    (source "{board_name}.sch")\n  )\n  (components\n"

    for idx, comp in enumerate(components):
        netlist += f"    (comp (ref {comp['id']})\n      (value {comp['value']})\n      (footprint {comp['footprint']}))\n"

    netlist += "  )\n)\n"

    file_path = f"{target_dir}/{board_name}.net"
    with open(file_path, "w") as f:
        f.write(netlist)

    return f"🔌 **PCB Matrix Initialized:** Circuit netlist saved to `{file_path}`"
