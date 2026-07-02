# ui/components/modal_popups.py
# Generates interactive buttons and verification checks

import chainlit as cl

async def trigger_deployment_confirmation(target_system: str):
    """Creates a clickable UI block to confirm critical actions."""
    
    actions = [
        cl.Action(name="confirm_deploy", value=target_system, label="🚀 Initiate Launch", description="Deploy to live server"),
        cl.Action(name="cancel_action", value="cancel", label="❌ Abort", description="Cancel the operation")
    ]
    
    await cl.Message(
        content=f"**WARNING:** You are about to deploy code to `{target_system}`. Are you sure you want to proceed?",
        actions=actions
    ).send()

# Note: You will need to add a callback listener in main.py to catch these button clicks:
# @cl.action_callback("confirm_deploy")
# async def on_action(action: cl.Action):
#     await cl.Message(content=f"Executing deployment to {action.value}...").send()
