# tools/film_production_dept/render_farm_mgr.py
import random

def monitor_render_job(job_id: str, total_frames: int) -> str:
    """Simulates multi-threaded frame compilation metrics for asset generation."""
    
    rendered = random.randint(0, total_frames)
    failed = random.randint(0, max(1, int(rendered * 0.01)))
    
    progress = (rendered / total_frames) * 100 if total_frames > 0 else 100
    status = "COMPILING" if rendered < total_frames else "SUCCESSFULLY BAKED"
    
    return f"""
    🖥️ **Distributed Render Node [{job_id}]:**
    - Job State: **{status}**
    - Progress Core: {rendered}/{total_frames} Frames ({progress:.1f}%)
    - Failed Vectors Dropped: {failed} frames
    
    *Resource Allocation: Distributed matrix active.*
    """
