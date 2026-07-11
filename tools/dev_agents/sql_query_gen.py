# tools/dev_agents/sql_query_gen.py

def format_sql_query(table_name: str, action: str, parameters: dict = None) -> str:
    """Formats safe, standard SQL execution blocks."""
    
    action = action.upper()
    query = ""
    
    if action == "SELECT":
        fields = ", ".join(parameters.get("fields", ["*"])) if parameters else "*"
        query = f"SELECT {fields} \nFROM {table_name};"
    elif action == "INSERT":
        keys = ", ".join(parameters.keys()) if parameters else ""
        vals = ", ".join([f"'{v}'" if isinstance(v, str) else str(v) for v in parameters.values()]) if parameters else ""
        query = f"INSERT INTO {table_name} ({keys}) \nVALUES ({vals});"
    else:
        query = f"-- {action} operation on {table_name} requires LLM strict formatting."
        
    return f"🗄️ **SQL Matrix Query:**\n```sql\n{query}\n```"
