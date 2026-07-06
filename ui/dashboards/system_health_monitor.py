# ui/dashboards/system_health_monitor.py
# Real-time telemetry for the ctrl matrix

def get_system_health_widget(cpu: str = "34%", ram: str = "2.1GB", latency: str = "12ms") -> str:
    """Generates a terminal-style grid showing live system telemetry."""
    return f"""
    <style>
    .health-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 15px;
        background: #0a0a0a;
        padding: 20px;
        border: 1px solid #1e1e1e;
        border-radius: 12px;
        font-family: 'Courier New', Courier, monospace;
        box-shadow: inset 0 0 20px rgba(0, 255, 136, 0.05);
    }}
    .health-node {{
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 15px;
        background: rgba(0, 255, 136, 0.05);
        border: 1px solid rgba(0, 255, 136, 0.2);
        border-radius: 8px;
    }}
    .node-label {{ color: #a099d8; font-size: 12px; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; }}
    .node-value {{ color: #00ff88; font-size: 24px; font-weight: bold; text-shadow: 0 0 10px rgba(0, 255, 136, 0.4); }}
    .pulse-dot {{ width: 6px; height: 6px; background: #00ff88; border-radius: 50%; margin-top: 10px; animation: pulse 2s infinite; }}
    </style>
    
    <div class="health-grid">
        <div class="health-node">
            <span class="node-label">CPU Load</span>
            <span class="node-value">{cpu}</span>
            <div class="pulse-dot"></div>
        </div>
        <div class="health-node">
            <span class="node-label">Mem Alloc</span>
            <span class="node-value">{ram}</span>
            <div class="pulse-dot"></div>
        </div>
        <div class="health-node">
            <span class="node-label">Latency</span>
            <span class="node-value">{latency}</span>
            <div class="pulse-dot"></div>
        </div>
    </div>
    """
