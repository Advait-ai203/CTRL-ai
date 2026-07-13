# tools/finance_agents/crypto_portfolio.py

def get_portfolio_value(wallet_address: str, holdings: dict) -> str:
    """Calculates total valuation of a simulated crypto wallet."""
    # Simulated current market prices in USD
    market_prices = {
        "BTC": 64500.00,
        "ETH": 3400.00,
        "SOL": 145.00,
        "USDT": 1.00
    }

    total_usd = 0.0
    output = f"💼 **Decentralized Wallet Analysis: {wallet_address[:8]}...**\n"

    for coin, amount in holdings.items():
        if coin in market_prices:
            value = amount * market_prices[coin]
            total_usd += value
            output += f"- {coin}: {amount} (${value:,.2f})\n"

    output += f"\n💰 **Total On-Chain Liquidity:** ${total_usd:,.2f}"
    return output
