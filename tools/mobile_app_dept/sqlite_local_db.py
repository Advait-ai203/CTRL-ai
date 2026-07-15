# tools/mobile_app_dept/sqlite_local_db.py

def generate_local_schema(table_name: str) -> str:
    """Generates raw SQLite schema for local mobile caching."""
    
    if table_name == "inventory":
        schema = """
        CREATE TABLE IF NOT EXISTS allmate_inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sku TEXT UNIQUE NOT NULL,
            item_name TEXT NOT NULL,
            stock_count INTEGER DEFAULT 0,
            last_synced TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """
    else:
        schema = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_payload TEXT NOT NULL
        );
        """
        
    return f"🗄️ **Local SQLite Database Matrix:**\n```sql\n{schema}\n```"
