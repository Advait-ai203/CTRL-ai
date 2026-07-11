# tools/writing_agents/tone_analyzer.py

def analyze_tone(text: str) -> str:
    """Evaluates text for sentiment, emotional weight, and professional tone."""
    words = text.lower().split()

    # Basic logic for the matrix matrix
    aggressive_words = ['must', 'demand', 'immediately', 'failure', 'worst']
    passive_words = ['maybe', 'perhaps', 'sorry', 'just', 'wondering']

    agg_score = sum(1 for w in words if w in aggressive_words)
    pass_score = sum(1 for w in words if w in passive_words)

    primary_tone = "Neutral / Professional"
    if agg_score > pass_score and agg_score > 1:
        primary_tone = "Aggressive / Urgent"
    elif pass_score > agg_score and pass_score > 1:
        primary_tone = "Passive / Hesitant"

    return f"""
    🎛️ **Tone Analysis Matrix:**
    - Primary Sentiment: **{primary_tone}**
    - Word Count: {len(words)}
    - Recommendation: {"Soften language" if agg_score > 1 else "Ready to send."}
    """
