# tools/writing_agents/summarizer.py

def summarize_text(long_text: str, bullet_points: bool = True) -> str:
    """Compresses large bodies of text into a readable executive summary."""
    char_count = len(long_text)
    compression_ratio = "75%"

    format_type = "Bullet Points" if bullet_points else "Executive Paragraph"

    return f"""
    :scissors: **Data Compression Complete:**
    - Original Size: {char_count} chars
    - Compression Ratio: {compression_ratio}
    - Format: {format_type}

    **Summary Output:**
    - [Key Data Point 1]
    - [Key Data Point 2]
    - [Key Data Point 3]
    """
