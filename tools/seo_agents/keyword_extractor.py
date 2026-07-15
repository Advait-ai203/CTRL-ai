# tools/seo_agents/keyword_extractor.py
from collections import Counter
import re

def extract_focus_keywords(content: str, top_n: int = 5) -> str:
    """Analyzes text to extract the highest frequency keyword clusters."""
    if not content.strip():
        return "⚠️ Keyword Extractor: No content provided."
        
    # Strip punctuation and convert to lowercase
    words = re.findall(r'\b[a-z]{4,}\b', content.lower())
    
    # Filter out common stop words
    stop_words = {'this', 'that', 'with', 'from', 'your', 'have', 'more', 'about'}
    filtered_words = [w for w in words if w not in stop_words]
    
    word_counts = Counter(filtered_words)
    top_keywords = word_counts.most_common(top_n)
    
    output = "🔑 **SEO Keyword Matrix:**\n"
    for word, count in top_keywords:
        output += f"- `{word}` (Frequency: {count})\n"
        
    return output
