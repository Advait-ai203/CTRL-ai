# tools/data_agents/pandas_analyzer.py
import json

def generate_dataset_summary(data_list: list, numeric_key: str) -> str:
    """Simulates foundational pandas descriptive analytics over a list of dictionaries."""
    if not data_list:
        return "⚠️ Empty dataset provided."
        
    values = []
    for item in data_list:
        if numeric_key in item:
            try:
                values.append(float(item[numeric_key]))
            except (ValueError, TypeError):
                continue
                
    if not values:
        return f"⚠️ Numeric key '{numeric_key}' not found or contains no parsable values."
        
    values.sort()
    total = sum(values)
    count = len(values)
    mean = total / count
    median = values[count // 2] if count % 2 != 0 else (values[count // 2 - 1] + values[count // 2]) / 2
    
    summary = {
        "metric_analyzed": numeric_key,
        "count": count,
        "min": min(values),
        "max": max(values),
        "mean": round(mean, 2),
        "median": round(median, 2),
        "sum": round(total, 2)
    }
    
    return f"📈 **Pandas Analogue Summary Matrix:**\n```json\n{json.dumps(summary, indent=4)}\n```"
