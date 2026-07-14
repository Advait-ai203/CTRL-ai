# tools/data_agents/csv_parser.py
import csv
import os

def parse_csv_to_matrix(file_path: str) -> dict:
    """Parses a CSV file into a structured dictionary format."""
    if not os.path.exists(file_path):
        return {"status": "error", "message": f"File not found at {file_path}"}
        
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
        return {
            "status": "success",
            "total_records": len(data),
            "headers": list(data[0].keys()) if data else [],
            "payload": data
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}
