# tools/finance_agents/pitch_deck_analyzer.py

def analyze_pitch_strength(deck_content: str, target_investor: str = "Metrolite Chairman") -> str:
    """Evaluates business pitch text for key venture capital metrics."""

    keywords = ["revenue", "market size", "disruption", "runway", "customer acquisition", "multigrade filter", "saas"]
    score = sum(1 for word in keywords if word in deck_content.lower())

    strength = "HIGH" if score >= 4 else "NEEDS REVISION"

    return f"""
    📊 **Pitch Deck Matrix Analysis:**
    - Target Audience: {target_investor}
    - Strategic Keywords Detected: {score}/{len(keywords)}
    - Readiness Score: {strength}

    *Recommendation:* {"Pitch is ready for deployment." if score >= 4 else "Inject more hard data regarding market size and revenue loops."}
    """
