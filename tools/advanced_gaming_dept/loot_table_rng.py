# tools/advanced_gaming_dept/loot_table_rng.py
import random

def evaluate_loot_drop(loot_table: dict) -> str:
    """Calculates a random weighted selection from an explicit items dictionary."""
    items = list(loot_table.keys())
    weights = list(loot_table.values())
    
    total_weight = sum(weights)
    if total_weight <= 0:
        return "Empty Drop"
        
    choice = random.uniform(0, total_weight)
    current_sum = 0
    
    for item, weight in zip(items, weights):
        current_sum += weight
        if choice <= current_sum:
            return item
            
    return items[-1]
