# core/orchestrator.py
# The central intelligence router for the ctrl matrix

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field
from config.settings import settings

class EngineDecision(BaseModel):
    """Schema forcing the AI to output exactly one of the matrix department strings."""
    target_department: str = Field(
        description="Target MUST be one of: 'blender', 'browser', 'web', 'startup_founder', 'design', 'game', 'finance', 'video', 'os_control', or 'standard_chat'"
    )

def run_orchestrator(processed_text: str) -> str:
    """Evaluates raw inputs and passes management control to the precise sub-agent."""
    
    # Fast, zero-creativity model for pure logic routing
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash", 
        google_api_key=settings.GOOGLE_API_KEY, 
        temperature=0.0
    )
    
    structured_llm = llm.with_structured_output(EngineDecision)
    
    system_prompt = (
        "You are the master Orchestrator for the ctrl platform.\n"
        "Analyze the user's prompt and route it to the exact operational department:\n"
        "- 'blender': 3D modeling, CAD, or STL requests.\n"
        "- 'browser': Searching the live web or scraping data.\n"
        "- 'web': Writing HTML/CSS/React frontend code.\n"
        "- 'startup_founder': Pitch decks, business models, or cap tables.\n"
        "- 'design': UI layouts, SVGs, or brand colors.\n"
        "- 'game': Mechanics, sprites, or physics engines.\n"
        "- 'finance': Budgets, crypto tracking, or burn rates.\n"
        "- 'video': Stop-motion, rendering, or FFmpeg.\n"
        "- 'os_control': Local file management and CMD execution.\n"
        "- 'standard_chat': General conversation, greetings, or undefined tasks."
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}")
    ])
    
    try:
        decision = (prompt | structured_llm).invoke({"input": processed_text})
        return decision.target_department
    except Exception as e:
        print(f"Orchestrator Routing Failure: {e}")
        return "standard_chat"
