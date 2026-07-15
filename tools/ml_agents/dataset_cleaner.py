# tools/ml_agents/dataset_cleaner.py
import json

def clean_training_matrix(raw_records: list, strategy: str = "mean") -> dict:
    """Imputes missing data and normalizes numerical values in a dataset."""
    if not raw_records:
        return {"status": "error", "message": "Dataset is empty."}
        
    numeric_values = [r.get("value") for r in raw_records if isinstance(r.get("value"), (int, float))]
    
    if not numeric_values:
        return {"status": "warning", "message": "No numerical features identified for structural cleaning."}
        
    impute_value = sum(numeric_values) / len(numeric_values) if strategy == "mean" else sorted(numeric_values)[len(numeric_values)//2]
    
    cleaned_records = []
    for record in raw_records:
        cleaned_item = record.copy()
        if cleaned_item.get("value") is None:
            cleaned_item["value"] = impute_value
        cleaned_records.append(cleaned_item)
        
    return {
        "status": "success",
        "records_processed": len(raw_records),
        "imputation_value_applied": round(impute_value, 4),
        "payload": cleaned_records
    }
