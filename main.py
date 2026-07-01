import os
import chainlit as cl

# --- Core Middleware & Exceptions ---
from middleware.rate_limiter import is_rate_limited
from core.exceptions import global_error_handler
from core.orchestrator import run_orchestrator

@cl.on_chat_start
async def initialize_ctrl_system():
    """Boots the ctrl system, connects inputs, and initializes delivery folders."""
    cl.user_session.set("user_id", "ctrl_prime_operator")
    cl.user_session.set("incognito", False)
    
    # Auto-verify Delivery Box folders exist for output assets
    directories = ["models", "circuits", "web_builds", "app_apks", "sheet_music", "research_reports"]
    for folder in directories:
        os.makedirs(f"generated_assets/{folder}", exist_ok=True)
        
    await cl.Message(
        content="⚡ **ctrl System Online.** Optical and Audio Senses initialized. The 230+ Tool Matrix is standing by."
    ).send()

@cl.on_message
async def process_incoming_event(message: cl.Message):
    """Processes multimodal inputs, invokes the Orchestrator, and fires execution matrices."""
    
    # 1. Security & Rate Limiting
    if is_rate_limited():
        await cl.Message(content="⚠️ Operational rate threshold exceeded. Pause executions briefly.").send()
        return

    user_text = message.content
    elements_to_display = []
    
    # Secure Session Toggle
    if user_text.strip().lower() == "/incognito":
        current_state = not cl.user_session.get("incognito")
        cl.user_session.set("incognito", current_state)
        status = "ENABLED (Logs disabled)" if current_state else "DISABLED"
        await cl.Message(content=f"🔒 **Incognito Mode: {status}**").send()
        return

    # 2. SENSES: Multimodal File Interception (Vision)
    if message.elements:
        for element in message.elements:
            if "image" in element.mime:
                # Dynamically import to keep startup fast
                from senses.vision_processor import process_incoming_vision
                with cl.Step(name="Activating ctrl Vision..."):
                    # Reads the image and appends the description directly to the user's prompt
                    image_description = process_incoming_vision(element.path)
                    user_text += f"\n\n[Visual Context Ingested]: {image_description}"

    # 3. ADVANCED TRIGGER: Omni-Consensus Engine
    if user_text.lower().startswith("omni") or user_text.lower().startswith("deep check"):
        from core.omni_consensus import execute_omni_consensus
        with cl.Step(name="Firing Omni-Consensus Engine (Querying Multiple LLMs)..."):
            response_content = await execute_omni_consensus(user_text)
        await cl.Message(content=response_content).send()
        return # Exit early so standard router doesn't run

    # 4. ADVANCED TRIGGER: Swarm Intelligence
    if "debate" in user_text.lower() or "swarm" in user_text.lower():
        from core.swarm_coordinator import run_swarm_logic
        with cl.Step(name="Initializing Swarm Debate..."):
            response_content = run_swarm_logic(user_text)
        await cl.Message(content=response_content).send()
        return

    # 5. BRAIN: Standard Routing through Orchestrator
    target_dept = run_orchestrator(user_text)
    
    try:
        response_content = ""
        
        with cl.Step(name=f"Routing to [{target_dept.upper()}] Sub-System"):
            
            # --- Specific Tool Executions ---
            if target_dept == "blender":
                from tools.engineering_dept.blender_tool import execute_blender_tool
                response_content, output_file = execute_blender_tool(user_text)
                if output_file and os.path.exists(output_file):
                    elements_to_display.append(cl.File(name=os.path.basename(output_file), path=output_file, display="inline"))
                    
            elif target_dept == "browser":
                from tools.system_web_dept.browser_tool import execute_browser_tool
                response_content = execute_browser_tool(user_text)
                
            elif target_dept == "web":
                from tools.web_agents.html_compiler import execute_html_compiler
                response_content, output_file = execute_html_compiler(user_text)
                if output_file and os.path.exists(output_file):
                    elements_to_display.append(cl.File(name=os.path.basename(output_file), path=output_file, display="inline"))
            
            # --- Catch-All for Modules Under Construction ---
            elif target_dept not in ["standard_chat"]:
                response_content = f"⚠️ Route '{target_dept}' detected. The ctrl squad is still wiring the APIs for this module in the backend."
                
            # --- Fallback: Standard Chat ---
            else:
                from langchain_google_genai import ChatGoogleGenerativeAI
                from config.settings import settings
                llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=settings.GOOGLE_API_KEY)
                response_content = llm.invoke(user_text).content

        # 6. Final Delivery
        await cl.Message(content=response_content, elements=elements_to_display).send()

    except Exception as fault:
        error_msg = global_error_handler(fault)
        await cl.Message(content=error_msg).send()
