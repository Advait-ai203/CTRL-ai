# ui/components/toggles.py
# Advanced interactive toggle switches for the ctrl UI

def get_cosmic_toggle(toggle_id: str = "main_system_toggle") -> str:
    """
    Generates a 3D cosmic toggle switch with rotating rings, 
    energy lines, and a particle burst effect on activation.
    """
    return f"""
    <style>
    .cosmic-toggle-container {{
      display: flex;
      align-items: center;
      justify-content: center;
      margin: 20px 0;
    }}
    
    .cosmic-toggle-container .cosmic-toggle {{
      position: relative;
      width: 140px;
      height: 70px;
      display: inline-block;
      cursor: pointer;
      transform-style: preserve-3d;
      perspective: 500px;
    }}
    
    .cosmic-toggle-container .toggle {{
      opacity: 0;
      width: 0;
      height: 0;
      position: absolute;
    }}
    
    .cosmic-toggle-container .slider {{
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background-color: #0a0a0a;
      border-radius: 50px;
      border: 2px solid #1e1e1e;
      transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
      overflow: hidden;
      box-shadow: inset 0 0 20px rgba(0, 0, 0, 0.8);
      z-index: 1;
    }}
    
    /* Deep space background effect */
    .cosmic-toggle-container .cosmos {{
      position: absolute;
      width: 100%;
      height: 100%;
      background: radial-gradient(circle at center, rgba(207, 48, 170, 0.1) 0%, transparent 70%);
      transition: 0.5s;
    }}
    
    /* Horizontal tracking lines */
    .cosmic-toggle-container .energy-line {{
      position: absolute;
      height: 1px;
      background: rgba(255, 255, 255, 0.05);
      width: 100%;
      z-index: 0;
    }}
    .cosmic-toggle-container .energy-line:nth-child(2) {{ top: 30%; }}
    .cosmic-toggle-container .energy-line:nth-child(3) {{ top: 50%; }}
    .cosmic-toggle-container .energy-line:nth-child(4) {{ top: 70%; }}
    
    /* The moving switch button */
    .cosmic-toggle-container .toggle-orb {{
      position: absolute;
      height: 50px;
      width: 50px;
      left: 8px;
      bottom: 8px;
      background-color: #111;
      border-radius: 50%;
      transition: all 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
      display: flex;
      justify-content: center;
      align-items: center;
      box-shadow: 0 0 15px rgba(207, 48, 170, 0.3);
      z-index: 3;
    }}
    
    /* The glowing center */
    .cosmic-toggle-container .inner-orb {{
      width: 18px;
      height: 18px;
      background: #cf30aa;
      border-radius: 50%;
      box-shadow: 0 0 10px #cf30aa, 0 0 20px #cf30aa;
      transition: 0.5s;
    }}
    
    /* The spinning outer ring */
    .cosmic-toggle-container .ring {{
      position: absolute;
      width: 60px;
      height: 60px;
      border: 2px solid transparent;
      border-top-color: #cf30aa;
      border-bottom-color: #cf30aa;
      border-radius: 50%;
      animation: cosmic-spin 4s linear infinite;
      transition: 0.5s;
    }}
    
    @keyframes cosmic-spin {{
      100% {{ transform: rotate(360deg); }}
    }}
    
    /* --- ACTIVE / CHECKED STATE --- */
    .cosmic-toggle-container .toggle:checked + .slider {{
      border-color: rgba(0, 255, 136, 0.5);
      background-color: #05150a;
    }}
    
    .cosmic-toggle-container .toggle:checked + .slider .cosmos {{
      background: radial-gradient(circle at center, rgba(0, 255, 136, 0.1) 0%, transparent 70%);
    }}
    
    .cosmic-toggle-container .toggle:checked + .slider .toggle-orb {{
      transform: translateX(70px);
      box-shadow: 0 0 20px rgba(0, 255, 136, 0.5);
    }}
    
    .cosmic-toggle-container .toggle:checked + .slider .inner-orb {{
      background: #00ff88;
      box-shadow: 0 0 10px #00ff88, 0 0 30px #00ff88;
    }}
    
    .cosmic-toggle-container .toggle:checked + .slider .ring {{
      border-top-color: #00ff88;
      border-bottom-color: #00ff88;
      animation: cosmic-spin 2s linear infinite reverse;
    }}
    
    /* --- PARTICLE BURST LOGIC --- */
    .cosmic-toggle-container .particles {{
      position: absolute;
      top: 50%;
      left: 33px; /* Centers under the inactive orb */
      transform: translateY(-50%);
      z-index: 2;
      transition: 0.5s cubic-bezier(0.68, -0.55, 0.265, 1.55);
    }}
    
    .cosmic-toggle-container .toggle:checked + .slider .particles {{
      left: 103px; /* Moves with the orb */
    }}
    
    .cosmic-toggle-container .particle {{
      position: absolute;
      width: 4px;
      height: 4px;
      background: #cf30aa;
      border-radius: 50%;
      top: -2px;
      left: -2px;
      opacity: 0;
      transform: rotate(var(--angle)) translateY(0px);
      transition: 0.4s ease-out;
    }}
    
    .cosmic-toggle-container .toggle:active + .slider .particle,
    .cosmic-toggle-container .toggle:checked + .slider .particle {{
      opacity: 1;
      background: #00ff88;
      box-shadow: 0 0 8px #00ff88;
      transform: rotate(var(--angle)) translateY(35px) scale(0);
    }}
    </style>

    <div class="cosmic-toggle-container">
        <label class="cosmic-toggle">
            <input class="toggle" type="checkbox" id="{toggle_id}" />
            <div class="slider">
                <div class="cosmos"></div>
                <div class="energy-line"></div>
                <div class="energy-line"></div>
                <div class="energy-line"></div>
                <div class="toggle-orb">
                    <div class="inner-orb"></div>
                    <div class="ring"></div>
                </div>
                <div class="particles">
                    <div style="--angle: 30deg" class="particle"></div>
                    <div style="--angle: 60deg" class="particle"></div>
                    <div style="--angle: 90deg" class="particle"></div>
                    <div style="--angle: 120deg" class="particle"></div>
                    <div style="--angle: 150deg" class="particle"></div>
                    <div style="--angle: 180deg" class="particle"></div>
                    <div style="--angle: 210deg" class="particle"></div>
                    <div style="--angle: 240deg" class="particle"></div>
                    <div style="--angle: 270deg" class="particle"></div>
                    <div style="--angle: 300deg" class="particle"></div>
                    <div style="--angle: 330deg" class="particle"></div>
                    <div style="--angle: 360deg" class="particle"></div>
                </div>
            </div>
        </label>
    </div>
    """
