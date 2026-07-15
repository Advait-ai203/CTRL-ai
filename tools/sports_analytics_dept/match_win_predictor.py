# tools/sports_analytics_dept/match_win_predictor.py

def calculate_live_probability(target: int, current_score: int, overs_remaining: float, wickets_down: int) -> dict:
    """Calculates structural chasing team win probabilities based on resource metrics."""
    runs_required = target - current_score
    
    if runs_required <= 0:
        return {"chaser_win_pct": 100.0, "defender_win_pct": 0.0, "state": "Match Concluded"}
    if wickets_down >= 10 or overs_remaining <= 0:
        return {"chaser_win_pct": 0.0, "defender_win_pct": 100.0, "state": "Match Concluded"}
        
    balls_remaining = int(overs_remaining) * 6 + int((overs_remaining % 1) * 10)
    wickets_remaining = 10 - wickets_down
    
    # Simple heuristic balance check evaluating run rate vs resource limits
    required_run_rate = (runs_required / balls_remaining) * 6 if balls_remaining > 0 else 99.0
    
    # Dynamic matrix weight adjustments
    base_chaser_chance = 50.0 + (wickets_remaining * 4) - (required_run_rate * 5)
    chaser_pct = max(1.0, min(99.0, base_chaser_chance))
    
    return {
        "chaser_win_pct": round(chaser_pct, 1),
        "defender_win_pct": round(100.0 - chaser_pct, 1),
        "required_run_rate_per_over": round(required_run_rate, 2)
    }
