# tools/writing_agents/creative_writer.py

def generate_creative_copy(prompt: str, word_limit: int = 250) -> str:
    """Generates engaging, imaginative text for marketing or branding."""
    return f"""
    ✨ **Creative Generation Initialized:**
    - Directive: "{prompt}"
    - Parameters: Max {word_limit} words

    [CREATIVE_NARRATIVE_WILL_STREAM_HERE]
    """
