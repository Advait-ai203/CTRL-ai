# tools/advanced_gaming_dept/multiplayer_netcode.py
import time
import math

def synchronize_client_ticks(server_tick: int, client_latencies: dict) -> dict:
    """Calculates network tick synchronization and frame adjustments across clients."""
    sync_manifest = {}
    
    for client_id, latency_ms in client_latencies.items():
        # Convert round-trip latency milliseconds to tick offset (assuming 60 ticks per second)
        tick_offset = math.ceil((latency_ms / 2) / (1000 / 60))
        target_reconciliation_tick = server_tick + tick_offset
        
        sync_manifest[client_id] = {
            "compensated_tick": target_reconciliation_tick,
            "frame_delay_buffer": tick_offset,
            "status": "synchronized" if latency_ms < 150 else "jitter_warning"
        }
        
    return {
        "master_server_tick": server_tick,
        "active_nodes": len(client_latencies),
        "sync_manifest": sync_manifest
    }
