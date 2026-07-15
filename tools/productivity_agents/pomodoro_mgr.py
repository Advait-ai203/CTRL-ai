# tools/productivity_agents/pomodoro_mgr.py

def construct_pomodoro_cycle(total_available_minutes: int, custom_focus_length: int = 25) -> str:
    """Divides an open time block into specific focus and recovery intervals."""
    
    focus_block = custom_focus_length
    break_block = 5 if focus_block < 50 else 10
    
    cycle_length = focus_block + break_block
    total_cycles = total_available_minutes // cycle_length
    remaining = total_available_minutes % cycle_length
    
    return f"""
    🍅 **Pomodoro Interval Strategy Framework:**
    - Planned Block Allocation: {total_available_minutes} minutes
    - Focus Window: {focus_block} mins │ Break Window: {break_block} mins
    
    **Execution Schedule:**
    - Completed Cycles Staged: **{total_cycles} consecutive sets**
    - Unallocated Residual Buffers: {remaining} minutes
    """
