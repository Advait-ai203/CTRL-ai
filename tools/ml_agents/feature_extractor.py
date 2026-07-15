# tools/ml_agents/feature_extractor.py
import re

def extract_text_features(text_input: str) -> dict:
    """Transforms raw text blocks into normalized numerical feature matrices."""
    cleaned_text = re.sub(r'[^\w\s]', '', text_input.lower())
    words = cleaned_text.split()
    total_words = len(words) if words else 1
    
    # Calculate essential structural metrics
    features = {
        "char_count": len(text_input),
        "word_count": total_words,
        "average_word_length": round(sum(len(w) for w in words) / total_words, 2),
        "exclamation_density": text_input.count("!"),
        "uppercase_ratio": round(sum(1 for c in text_input if c.isupper()) / (len(text_input) or 1), 3)
    }
    
    return features
