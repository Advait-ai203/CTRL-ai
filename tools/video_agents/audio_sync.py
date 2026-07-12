# tools/video_agents/audio_sync.py

def sync_audio_to_video(video_path: str, audio_path: str, output_name: str) -> str:
    """Generates the command to mux (merge) an audio track into a video file without re-encoding video."""
    
    command = (
        f"ffmpeg -i {video_path} -i {audio_path} "
        f"-c:v copy -c:a aac -map 0:v:0 -map 1:a:0 -shortest "
        f"./generated_assets/web_builds/{output_name}.mp4"
    )
    
    return f"""
    🔊 **Audio Synchronization Matrix:**
    Merging `{video_path}` with `{audio_path}`.
    
    **Execute Muxing Command:**
    ```bash
    {command}
    ```
    """
