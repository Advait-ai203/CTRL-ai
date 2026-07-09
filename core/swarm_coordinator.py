# core/swarm_coordinator.py
# Multi-agent debate and consensus engine

from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from config.settings import settings

class SwarmDebate(BaseModel):
    developer_draft: str = Field(description="The initial technical or strategic solution proposed.")
    reviewer_critique: str = Field(description="A harsh, critical teardown of the draft, pointing out logical flaws, bugs, or weak business strategy.")
    final_consensus: str = Field(description="The perfected output after resolving the critique.")

def run_swarm_logic(task_description: str) -> str:
    """Spins up a multi-agent debate to solve complex logic."""
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro", # Using Pro here for deep reasoning
        google_api_key=settings.GOOGLE_API_KEY, 
        temperature=0.4
    )
    
    structured_swarm = llm.with_structured_output(SwarmDebate)
    
    prompt = f"""
    You are an elite 3-person operational squad. 
    1. The Developer writes the initial solution.
    2. The Reviewer tears it down and finds structural or logical flaws.
    3. The Manager takes both and outputs the perfect final consensus.
    
    Target Objective: {task_description}
    """
    
    try:
        debate = structured_swarm.invoke(prompt)
        
        # Format the debate using our custom UI components
        from ui.components.chat_bubbles import format_code_review, format_success_block
        
        output = format_success_block("Swarm Consensus Reached", "The internal team has finalized the architecture.")
        output += format_code_review("Lead Developer", debate.developer_draft)
        output += format_code_review("Security/Logic Reviewer", debate.reviewer_critique)
        output += f"\n\n### Final Master Output\n{debate.final_consensus}"
        
        return output
    except Exception as e:
        return f"Swarm Synchronization Fault: {str(e)}"
