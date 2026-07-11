# tools/web_agents/api_endpoint_gen.py

def generate_fastapi_route(route_name: str, method: str = "GET") -> str:
    """Scaffolds a clean, async Python FastAPI route."""
    clean_route = route_name.lower().replace(" ", "_")
    
    code = f"""
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class {clean_route.title()}Response(BaseModel):
    status: str
    message: str
    data: dict

@router.{method.lower()}("/{clean_route}", response_model={clean_route.title()}Response)
async def handle_{clean_route}():
    \"\"\"Auto-generated endpoint by the ctrl matrix.\"\"\"
    try:
        # TODO: Inject core logic here
        return {{"status": "success", "message": "Endpoint reached", "data": {{}}}}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
"""
    return f"🔗 **API Route Computed ({method.upper()} /{clean_route}):**\n```python\n{code}\n```"
