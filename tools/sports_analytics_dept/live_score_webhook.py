# tools/sports_analytics_dept/live_score_webhook.py
import json

def construct_score_webhook_payload(match_id: str, batting_team: str, runs: int, wickets: int, overs: float) -> str:
    """Structures live score updates into web-broadcast standard telemetry logs."""
    
    payload = {
        "event_type": "live_match_tick",
        "match_id": match_id,
        "telemetry": {
            "batting_side": batting_team,
            "current_score": f"{runs}/{wickets}",
            "overs_completed": overs,
            "run_rate_actual": round(runs / overs, 2) if overs > 0 else 0.0
        }
    }
    
    return f"📡 **Webhook Broadcast Matrix Ready:**\n```json\n{json.dumps(payload, indent=4)}\n```"
