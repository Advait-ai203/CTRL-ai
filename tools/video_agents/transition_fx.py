# tools/video_agents/transition_fx.py

def generate_crossfade(clip_a: str, clip_b: str, duration: float = 1.0) -> str:
    """Generates an FFmpeg complex filter command to crossfade two video clips."""
    
    # FFmpeg xfade requires offset calculation, assuming clip A is at least 3 seconds long for the matrix default
    offset = 3.0 - duration 
    
    command = (
        f"ffmpeg -i {clip_a} -i {clip_b} "
        f"-filter_complex \"[0:v][1:v]xfade=transition=fade:duration={duration}:offset={offset}[v]\" "
        f"-map \"[v]\" output_transition.mp4"
    )
    
    return f"""
    🪄 **Transition FX Generated:**
    - Type: Crossfade
    - Duration: {duration}s
    
    **Execution Command:**
    ```bash
    {command}
    ```
    """
