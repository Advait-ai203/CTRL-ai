# ui/dashboards/analytics_view.py
# Frosted glass data presentation components

def get_glass_data_card(title: str, value: str, subtext: str = "System Nominal") -> str:
    """
    Generates a frosted glass dashboard card for displaying critical AI outputs.
    """
    return f"""
    <style>
    .glass-card-wrapper {{
      width: 320px;
      height: 160px;
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 16px;
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      padding: 24px;
      position: relative;
      overflow: hidden;
      box-shadow: 0 4px 30px rgba(0, 0, 0, 0.5);
      font-family: 'Inter', sans-serif;
    }}
    
    .glass-card-wrapper::before {{
      content: "";
      position: absolute;
      top: -50%;
      left: -50%;
      width: 200%;
      height: 200%;
      background: radial-gradient(circle, rgba(207, 48, 170, 0.15) 0%, transparent 60%);
      opacity: 0.5;
      z-index: -1;
    }}

    .glass-card-title {{
      color: #a099d8;
      font-size: 14px;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      margin-bottom: 8px;
    }}

    .glass-card-value {{
      color: #ffffff;
      font-size: 36px;
      font-weight: 700;
      margin: 0;
      text-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
    }}

    .glass-card-subtext {{
      color: #00ff88;
      font-size: 12px;
      font-family: 'Courier New', Courier, monospace;
      position: absolute;
      bottom: 24px;
      display: flex;
      align-items: center;
      gap: 6px;
    }}
    
    .glass-status-dot {{
      width: 8px;
      height: 8px;
      background-color: #00ff88;
      border-radius: 50%;
      box-shadow: 0 0 8px #00ff88;
    }}
    </style>

    <div class="glass-card-wrapper">
        <div class="glass-card-title">{title}</div>
        <div class="glass-card-value">{value}</div>
        <div class="glass-card-subtext">
            <div class="glass-status-dot"></div>
            {subtext}
        </div>
    </div>
    """
