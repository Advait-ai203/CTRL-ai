# tools/seo_agents/serp_tracker.py
import json
import os
import datetime

def log_keyword_ranking(keyword: str, position: int, url: str) -> str:
    """Records Search Engine Results Page (SERP) positions into the matrix ledger."""
    target_dir = "./generated_assets/research_reports/seo_logs"
    os.makedirs(target_dir, exist_ok=True)
    tracker_path = os.path.join(target_dir, "serp_rankings.json")
    
    entry = {
        "date": str(datetime.date.today()),
        "keyword": keyword,
        "position": position,
        "url": url
    }
    
    try:
        if os.path.exists(tracker_path):
            with open(tracker_path, "r") as f:
                rankings = json.load(f)
        else:
            rankings = []
            
        rankings.append(entry)
        
        with open(tracker_path, "w") as f:
            json.dump(rankings, f, indent=4)
            
        trend = "🚀 Front Page" if position <= 10 else "🧗 Climbing"
        return f"📈 **SERP Matrix Updated:** '{keyword}' logged at Position #{position} ({trend})."
    except Exception as e:
        return f"⚠️ SERP Tracker Fault: {str(e)}"
