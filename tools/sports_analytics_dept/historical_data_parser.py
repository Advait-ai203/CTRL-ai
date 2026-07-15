# tools/sports_analytics_dept/historical_data_parser.py
import csv
import io

def parse_historical_csv_payload(csv_string_data: str) -> list:
    """Converts raw historical log datasets into structural analytics streams."""
    parsed_records = []
    f = io.StringIO(csv_string_data.strip())
    reader = csv.DictReader(f)
    
    for row in reader:
        try:
            parsed_records.append({
                "year": int(row.get("Year", 0)),
                "winner": row.get("Winner", "Unknown"),
                "margin_runs": int(row.get("MarginRuns", 0))
            })
        except ValueError:
            continue
            
    return parsed_records
