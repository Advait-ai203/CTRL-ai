# tools/sports_analytics_dept/tournament_bracket_gen.py

def generate_knockout_fixtures(teams_list: list) -> list:
    """Pairs an array of competing teams into structured initial knockout structures."""
    sorted_teams = sorted(teams_list) # Alphabetical/seed ordering baseline
    fixtures = []
    
    while len(sorted_teams) >= 2:
        team_a = sorted_teams.pop(0)
        team_b = sorted_teams.pop(-1) # Seed matching strategy (Highest vs Lowest)
        fixtures.append({"matchup": f"{team_a} vs {team_b}", "bracket_stage": "Quarter-Finals" if len(teams_list) <= 8 else "Round of 16"})
        
    if sorted_teams:
        fixtures.append({"matchup": f"{sorted_teams[0]} receives BYE", "bracket_stage": "Advance Direct"})
        
    return fixtures
