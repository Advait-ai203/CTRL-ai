# ui/layouts/presentation_mode.py
# Cinematic wrapper for pitch decks and slides

def wrap_in_presentation(slide_content: str) -> str:
    """Wraps content in a cinematic, distraction-free container."""
    return f"""
    <style>
    .ctrl-presentation {{
        width: 100%;
        aspect-ratio: 16 / 9;
        background: radial-gradient(circle at center, #1a1a24 0%, #0a0a0a 100%);
        border: 1px solid rgba(207, 48, 170, 0.3);
        border-radius: 16px;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 40px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.8);
    }}
    </style>
    <div class="ctrl-presentation">
        {slide_content}
    </div>
    """
