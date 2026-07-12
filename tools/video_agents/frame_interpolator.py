# tools/video_agents/frame_interpolator.py

def generate_interpolation_command(input_video: str, target_fps: int = 60) -> str:
    """Generates the advanced FFmpeg minterpolate filter command to smooth video."""
    output_video = input_video.replace(".mp4", f"_{target_fps}fps.mp4")
    
    command = f"ffmpeg -i {input_video} -filter:v \"minterpolate='mi_mode=mci:mc_mode=aobmc:vsbmc=1:fps={target_fps}'\" {output_video}"
    
    return f"""
    🌊 **Optical Flow Matrix Initialized:**
    - Target Smoothness: {target_fps} FPS
    
    **Execute this command in your terminal:**
    ```bash
    {command}
    ```
    """
