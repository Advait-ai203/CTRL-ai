# tools/ml_agents/predictive_model.py

def forecast_next_value(historical_sequence: list) -> str:
    """Generates an immediate predictive linear trend estimation."""
    if len(historical_sequence) < 2:
        return "⚠️ Insufficient history to calculate model trajectory."
        
    # Calculate simple directional changes over historical vectors
    deltas = [historical_sequence[i] - historical_sequence[i-1] for i in range(1, len(historical_sequence))]
    average_slope = sum(deltas) / len(deltas)
    
    predicted_next = historical_sequence[-1] + average_slope
    
    return f"""
    🔮 **Predictive Regression Node Inference:**
    - Historical Sequence Length: {len(historical_sequence)} points
    - Calculated Slope Vector: {average_slope:+.4f}
    
    **Forecast Target:**
    - Next Predicted Matrix Value: **{predicted_next:.2f}**
    """
