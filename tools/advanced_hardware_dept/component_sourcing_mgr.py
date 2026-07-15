# tools/advanced_hardware_dept/component_sourcing_mgr.py
import json

def generate_bom_cost(bom_items: dict, assembly_cost_per_unit: float) -> str:
    """Calculates total Cost of Goods Sold (COGS) from a Bill of Materials."""
    
    total_parts_cost = sum(bom_items.values())
    total_cogs = total_parts_cost + assembly_cost_per_unit
    
    # 60% gross margin target calculation
    target_retail = total_cogs / 0.40 
    
    return f"""
    📦 **Hardware Sourcing BOM Matrix:**
    - Total Component Cost: ₹{total_parts_cost:,.2f}
    - Labor/Assembly Cost: ₹{assembly_cost_per_unit:,.2f}
    
    **Unit Economics:**
    - Total COGS (Cost to Make): **₹{total_cogs:,.2f}**
    - Target Retail Price (60% Margin): **₹{target_retail:,.2f}**
    """
