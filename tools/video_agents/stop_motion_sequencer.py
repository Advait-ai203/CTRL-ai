# tools/video_agents/stop_motion_sequencer.py

def generate_shot_list(scene_name: str, duration_seconds: float, target_fps: int = 12) -> str:
    """Calculates frame-rate parameters and exposure sequences for physical animation."""
    total_frames = int(duration_seconds * target_fps)
    shift_per_frame_mm = round(24.0 / target_fps, 2)
    
    return f"""
    🎬 **Stop-Motion Sequence Computed: {scene_name.upper()}**
    - Target Playback: {target_fps} FPS
    - Total Duration: {duration_seconds}s
    - Total Images Required: {total_frames} frames
    
    **Animation Guidelines:**
    - Capture Interval: {int((1 / target_fps) * 1000)}ms per frame
    - Recommended Object Shift: ~{shift_per_frame_mm}mm per frame for fluid motion.
    
    *Status: Ready for camera capture.*
    """
