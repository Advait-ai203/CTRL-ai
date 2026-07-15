# tools/ml_agents/sentiment_analyzer.py

def analyze_feedback_sentiment(text_feedback: str) -> str:
    """Evaluates lexical tokens to classify text sentiment."""
    
    pos_tokens = {"excellent", "love", "fast", "perfect", "clean", "smooth", "incredible"}
    neg_tokens = {"broken", "slow", "error", "fail", "crash", "expensive", "annoying"}
    
    words = text_feedback.lower().split()
    pos_hits = sum(1 for w in words if w in pos_tokens)
    neg_hits = sum(1 for w in words if w in neg_tokens)
    
    score = pos_hits - neg_hits
    classification = "POSITIVE 🟢" if score > 0 else "NEGATIVE 🔴" if score < 0 else "NEUTRAL 🟡"
    
    return f"""
    🧠 **Sentiment Parsing Engine:**
    - Feedback Sample: "{text_feedback}"
    
    **Analysis Result:**
    - Metric Balance: (+{pos_hits} / -{neg_hits})
    - Evaluated Category: **{classification}**
    """
