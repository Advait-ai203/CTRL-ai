# ui/components/action_buttons.py
# Cyberpunk-styled interactive buttons

def get_cyberpunk_button(label: str = "EXECUTE", action_id: str = "btn_execute") -> str:
    """
    Generates a neon terminal button with a slice/glitch hover effect.
    """
    return f"""
    <style>
    .ctrl-btn-container button, .ctrl-btn-container button::after {{
      padding: 16px 20px;
      font-size: 18px;
      background: linear-gradient(45deg, transparent 5%, #000 5%);
      border: 0;
      color: #fff;
      letter-spacing: 3px;
      line-height: 1;
      box-shadow: 6px 0px 0px #00e6f6;
      outline: transparent;
      position: relative;
      font-family: 'Courier New', Courier, monospace;
      font-weight: bold;
      cursor: pointer;
    }}

    .ctrl-btn-container button::after {{
      content: 'EXECUTE';
      display: block;
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: linear-gradient(45deg, transparent 3%, #00e6f6 3%, #00e6f6 5%, #000 5%);
      text-shadow: -3px -3px 0px #F8F005, 3px 3px 0px #00e6f6;
      clip-path: inset(50% 50% 50% 50%);
    }}

    .ctrl-btn-container button:hover::after {{
      animation: 1s glitch;
      animation-timing-function: steps(2, end);
    }}

    @keyframes glitch {{
      0% {{ clip-path: inset(80% -6px 0 0); transform: translate(-20px, 20px); }}
      10% {{ clip-path: inset(10% -6px 85% 0); transform: translate(20px, 10px); }}
      20% {{ clip-path: inset(80% -6px 0 0); transform: translate(-10px, 20px); }}
      30% {{ clip-path: inset(10% -6px 85% 0); transform: translate(0px, 5px); }}
      40% {{ clip-path: inset(50% -6px 30% 0); transform: translate(-5px, 0px); }}
      50% {{ clip-path: inset(10% -6px 85% 0); transform: translate(5px, 0px); }}
      60% {{ clip-path: inset(40% -6px 43% 0); transform: translate(5px, 10px); }}
      70% {{ clip-path: inset(50% -6px 30% 0); transform: translate(-10px, 10px); }}
      80% {{ clip-path: inset(80% -6px 5% 0); transform: translate(20px, -10px); }}
      90% {{ clip-path: inset(80% -6px 0 0); transform: translate(-10px, 0px); }}
      100% {{ clip-path: inset(50% 50% 50% 50%); transform: translate(0); }}
    }}
    </style>

    <div class="ctrl-btn-container" style="margin: 20px 0;">
        <button id="{action_id}">{label}</button>
    </div>
    """
