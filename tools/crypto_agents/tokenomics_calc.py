# tools/crypto_agents/tokenomics_calc.py

def calculate_token_metrics(total_supply: int, launch_price_usd: float, circulating_percent: float) -> str:
    """Computes Fully Diluted Valuation (FDV) and initial market cap."""
    
    fdv = total_supply * launch_price_usd
    circulating_supply = total_supply * (circulating_percent / 100)
    initial_mcap = circulating_supply * launch_price_usd
    
    return f"""
    📈 **Tokenomics Matrix Computed:**
    - Total Supply: {total_supply:,} tokens
    - Launch Price: ${launch_price_usd:.4f}
    - Circulating Supply ({circulating_percent}%): {circulating_supply:,.0f} tokens
    
    **Valuations:**
    - Initial Market Cap: **${initial_mcap:,.2f}**
    - Fully Diluted Valuation (FDV): **${fdv:,.2f}**
    """
