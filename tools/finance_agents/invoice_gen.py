# tools/finance_agents/invoice_gen.py
import datetime
import os

def generate_invoice(client_name: str, services: dict, brand_name: str = "ctrl") -> str:
    """Compiles a professional invoice for software or hardware services."""
    target_dir = "./generated_assets/research_reports"
    os.makedirs(target_dir, exist_ok=True)

    invoice_id = f"INV-{datetime.datetime.now().strftime('%Y%m%d%H%M')}"
    date_today = datetime.date.today().strftime("%B %d, %Y")

    total_inr = sum(services.values())

    invoice_text = f"""
    ========================================
    INVOICE: {invoice_id}
    DATE: {date_today}
    FROM: {brand_name.upper()} STARTUP STUDIO (Delhi, India)
    TO: {client_name}
    ========================================
    SERVICES RENDERED:
    """

    for service, price in services.items():
        invoice_text += f"- {service}: ₹{price:,.2f}\n"

    invoice_text += f"\nTOTAL DUE: ₹{total_inr:,.2f}\n"
    invoice_text += "========================================\n"
    invoice_text += "Thank you for your business. Matrix connection closed."

    file_path = os.path.join(target_dir, f"{invoice_id}.txt")
    with open(file_path, "w") as f:
        f.write(invoice_text)

    return f"🧾 **Invoice Generated:** Saved to `{file_path}`"
