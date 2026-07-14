# tools/finance_agents/budget_tracker.py
import json
import os

def log_expense(brand_id: str, category: str, amount: float) -> str:
    """Logs a financial expense to the central matrix ledger."""
    target_dir = "./generated_assets/research_reports"
    os.makedirs(target_dir, exist_ok=True)
    ledger_path = os.path.join(target_dir, "master_ledger.json")
    
    entry = {"brand": brand_id, "category": category, "amount_inr": amount}
    
    try:
        if os.path.exists(ledger_path):
            with open(ledger_path, "r") as f:
                ledger = json.load(f)
        else:
            ledger = []
            
        ledger.append(entry)
        
        with open(ledger_path, "w") as f:
            json.dump(ledger, f, indent=4)
            
        return f"💸 **Ledger Updated:** Logged ₹{amount:,.2f} against `{brand_id}` ({category})."
    except Exception as e:
        return f"⚠️ Ledger Fault: {str(e)}"
