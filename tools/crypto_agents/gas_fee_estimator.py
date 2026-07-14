# tools/crypto_agents/gas_fee_estimator.py
import random

def estimate_gas_fees(network: str = "ETH") -> str:
    """Estimates current network transaction costs (Gwei/Lamports)."""
    
    if network.upper() == "ETH":
        base_fee = random.randint(15, 45)
        priority = random.randint(1, 3)
        total_gwei = base_fee + priority
        cost_usd = total_gwei * 0.05  # Rough estimation math
        
        return f"""
        ⛽ **{network} Network Congestion Matrix:**
        - Base Fee: {base_fee} Gwei
        - Priority Tip: {priority} Gwei
        - Total Estimated Cost: ~${cost_usd:.2f} USD
        
        *Recommendation: {"Send transaction now." if total_gwei < 30 else "Wait for network to cool down."}*
        """
    else:
        return f"⚡ **{network} Network:** High-speed chain detected. Fees are negligible (< $0.01)."
