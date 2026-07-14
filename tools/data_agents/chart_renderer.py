# tools/data_agents/chart_renderer.py

def render_terminal_bar_chart(data: dict, title: str = "Data Analytics Metrics") -> str:
    """Renders a clean text-based bar chart for terminal logs and analytics summaries."""
    if not data:
        return "⚠️ No data available to render chart."
        
    max_val = max(data.values()) if data.values() else 1
    max_label_len = max(len(str(k)) for k in data.keys())
    chart_width = 30
    
    output = f"\n📊 **{title.upper()}**\n" + "─" * (max_label_len + chart_width + 5) + "\n"
    
    for label, val in data.items():
        bar_len = int((val / max_val) * chart_width) if max_val > 0 else 0
        bar = "█" * bar_len
        output += f"{str(label).ljust(max_label_len)} │ {bar} ({val})\n"
        
    output += "─" * (max_label_len + chart_width + 5)
    return output
