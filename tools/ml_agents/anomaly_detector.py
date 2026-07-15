# tools/ml_agents/anomaly_detector.py

def evaluate_data_anomalies(value_stream: list, threshold_deviations: float = 2.0) -> dict:
    """Identifies outliers in numerical streams using standard deviations."""
    if not value_stream:
        return {"status": "empty"}
        
    mean = sum(value_stream) / len(value_stream)
    variance = sum((x - mean) ** 2 for x in value_stream) / len(value_stream)
    std_dev = variance ** 0.5 if variance > 0 else 1.0
    
    anomalies = []
    for idx, val in enumerate(value_stream):
        deviation = abs(val - mean) / std_dev
        if deviation > threshold_deviations:
            anomalies.append({"index": idx, "value": val, "deviation": round(deviation, 2)})
            
    return {
        "mean": round(mean, 2),
        "standard_deviation": round(std_dev, 2),
        "anomalies_detected": len(anomalies),
        "flags": anomalies
    }
