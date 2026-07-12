# tools/video_agents/color_grader.py

def apply_color_grade(input_video: str, style: str = "cyberpunk") -> str:
    """Outputs the FFmpeg video filter string for specific cinematic color grades."""
    
    styles = {
        "cyberpunk": "eq=contrast=1.2:brightness=0.0:saturation=1.5:gamma=0.9, colorbalance=rs=.2:gs=-.1:bs=.3",
        "cinematic_teal_orange": "colorbalance=rs=.1:gs=.0:bs=-.1:rm=-.1:gm=.1:bm=.2",
        "vintage": "eq=contrast=0.9:saturation=0.6, curves=preset=vintage"
    }
    
    filter_string = styles.get(style.lower(), styles["cinematic_teal_orange"])
    output_video = input_video.replace(".mp4", f"_graded.mp4")
    
    command = f"ffmpeg -i {input_video} -vf \"{filter_string}\" -c:a copy {output_video}"
    
    return f"""
    🎨 **Color Grade Profile: {style.upper()}**
    Run this matrix command to apply the visual look:
    ```bash
    {command}
    ```
    """
