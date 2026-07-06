# ui/layouts/split_screen_editor.py
# Side-by-side IDE layout

def get_split_screen(left_panel: str, right_panel: str) -> str:
    """Creates a side-by-side layout for code/preview workflows."""
    return f"""
    <style>
    .ctrl-split-view {{
        display: flex;
        width: 100%;
        height: 60vh;
        min-height: 500px;
        border: 1px solid #333;
        border-radius: 12px;
        overflow: hidden;
        background: #000;
    }}
    .split-pane {{
        flex: 1;
        padding: 20px;
        overflow-y: auto;
    }}
    .split-left {{ border-right: 1px solid #333; }}
    .split-right {{ background: rgba(255,255,255,0.02); }}
    </style>
    
    <div class="ctrl-split-view">
        <div class="split-pane split-left">{left_panel}</div>
        <div class="split-pane split-right">{right_panel}</div>
    </div>
    """
