"""
WorkPilot AI - Math Engine
ALL calculations happen here. AI is FORBIDDEN from doing math.
This prevents hallucinations in financial data.
"""

def calculate_discrepancies(contract_items, invoice_items):
    """
    Compare contract items vs invoice items and calculate exact discrepancies.
    Returns list of discrepancies and total overcharge.
    """
    discrepancies = []
    total_overcharge = 0.0
    
    for c_item in contract_items:
        for i_item in invoice_items:
            # Fuzzy match: check if descriptions overlap
            c_desc = c_item.get("description", "").lower()
            i_desc = i_item.get("description", "").lower()
            
            if c_desc and i_desc and (c_desc in i_desc or i_desc in c_desc):
                try:
                    c_rate = float(c_item.get("agreed_rate", 0))
                    c_qty = float(c_item.get("quantity", 0))
                    i_rate = float(i_item.get("billed_rate", 0))
                    i_qty = float(i_item.get("quantity", 0))
                    
                    c_total = c_rate * c_qty
                    i_total = i_rate * i_qty
                    diff = i_total - c_total
                    
                    if diff > 0.01:  # Overcharge detected
                        discrepancies.append({
                            "item": c_item.get("description", "Unknown"),
                            "contract_file": c_item.get("source_file", "N/A"),
                            "invoice_file": i_item.get("source_file", "N/A"),
                            "agreed_rate": c_rate,
                            "billed_rate": i_rate,
                            "quantity": c_qty,
                            "expected_total": round(c_total, 2),
                            "billed_total": round(i_total, 2),
                            "overcharge": round(diff, 2)
                        })
                        total_overcharge += diff
                except (ValueError, TypeError):
                    continue
    
    return discrepancies, round(total_overcharge, 2)

def calculate_time_saved(module_key, time_savings_config):
    """Calculate time saved for a specific module."""
    if module_key not in time_savings_config:
        return 0
    config = time_savings_config[module_key]
    saved_min = config["manual_min"] - (config["ai_sec"] / 60)
    return round(saved_min, 1)