# core/omni_consensus.py
# Asynchronous multi-LLM cross-referencing

import asyncio
from langchain_google_genai import ChatGoogleGenerativeAI
from config.settings import settings

# Note: In the future, you can add import ChatOpenAI here when you get the keys.

async def fetch_primary_model(prompt: str) -> str:
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=settings.GOOGLE_API_KEY)
        return await llm.ainvoke(prompt).content
    except Exception as e:
        return f"[Model 1 Failed]: {str(e)}"

async def fetch_fast_model(prompt: str) -> str:
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=settings.GOOGLE_API_KEY)
        return await llm.ainvoke(prompt).content
    except Exception as e:
        return f"[Model 2 Failed]: {str(e)}"

async def execute_omni_consensus(user_prompt: str) -> str:
    """Fires prompt to multiple models at the exact same time and synthesizes the truth."""
    
    # Run both network requests simultaneously
    responses = await asyncio.gather(
        fetch_primary_model(user_prompt),
        fetch_fast_model(user_prompt)
    )
    
    ans_1, ans_2 = responses

    synthesizer = ChatGoogleGenerativeAI(model="gemini-1.5-pro", google_api_key=settings.GOOGLE_API_KEY, temperature=0.1)
    
    synthesis_prompt = f"""
    You are the Supreme Arbiter. The user asked: "{user_prompt}"
    
    Model 1 answered: {ans_1}
    Model 2 answered: {ans_2}
    
    Cross-reference their answers for factual accuracy. Identify any contradictions. 
    Synthesize the absolute best, most accurate final response. Do not mention the other models.
    """
    
    try:
        final_truth = synthesizer.invoke(synthesis_prompt).content
        return f"🌐 **Omni-Consensus Achieved:**\n\n{final_truth}"
    except Exception as e:
        return f"Consensus Synthesis Failed: {str(e)}"
