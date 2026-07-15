# tools/sports_analytics_dept/fantasy_team_optimizer.py

def optimize_lineup(player_pool: list, budget_limit: float) -> dict:
    """Selects best possible player assets matching structural expenditure parameters."""
    # Expects list of dicts: [{"name": X, "cost": Y, "projected_points": Z}, ...]
    sorted_pool = sorted(player_pool, key=lambda p: p["projected_points"] / max(1, p["cost"]), reverse=True)
    
    selected_roster = []
    total_spend = 0.0
    accumulated_points = 0.0
    
    for player in sorted_pool:
        if total_spend + player["cost"] <= budget_limit:
            selected_roster.append(player["name"])
            total_spend += player["cost"]
            accumulated_points += player["projected_points"]
            
    return {
        "optimized_roster": selected_roster,
        "total_budget_spent": total_spend,
        "projected_points_total": round(accumulated_points, 1)
    }
