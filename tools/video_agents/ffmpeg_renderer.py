# tools/video_agents/ffmpeg_renderer.py
import subprocess
import os

def render_image_sequence(sequence_folder: str, output_name: str, fps: int = 24) -> str:
    """Stitches a folder of sequential images (e.g., frame_001.jpg) into an MP4."""
    output_path = f"./generated_assets/web_builds/{output_name}.mp4"
    os.makedirs("./generated_assets/web_builds", exist_ok=True)
    
    # FFmpeg command to compile images
    command = [
        "ffmpeg", "-y", 
        "-framerate", str(fps), 
        "-i", f"{sequence_folder}/frame_%03d.jpg", 
        "-c:v", "libx264", 
        "-pix_fmt", "yuv420p", 
        output_path
    ]
    
    try:
        # Run command headlessly
        subprocess.run(command, check=True, capture_output=True)
        return f"🎞️ **Video Render Complete:** Successfully compiled sequence to `{output_path}` at {fps} FPS."
    except FileNotFoundError:
        return "⚠️ FFmpeg Error: FFmpeg is not installed or not added to system PATH."
    except subprocess.CalledProcessError as e:
        return f"⚠️ Render Fault: {e.stderr.decode().strip()}"
