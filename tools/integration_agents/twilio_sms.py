# tools/integration_agents/twilio_sms.py
# Handles outbound SMS and Voice Calls for the ctrl matrix

import os
from twilio.rest import Client

def execute_twilio_comm(action_type: str, target_number: str, message: str) -> str:
    """
    Triggers an outbound phone call or text message using the Twilio API.
    
    Args:
        action_type (str): "call" or "sms"
        target_number (str): The phone number to dial (e.g., "+919876543210")
        message (str): What ctrl will say or text.
    """
    # Grab credentials from the secure vault
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    ctrl_number = os.getenv("TWILIO_PHONE_NUMBER")

    if not all([account_sid, auth_token, ctrl_number]):
        return "⚠️ Twilio Error: API keys are missing from the .env vault. Cannot execute telecom protocols."

    try:
        client = Client(account_sid, auth_token)

        if action_type == "call":
            # TwiML (Twilio Markup Language) translates text to robotic speech
            twiml_instructions = f"<Response><Say voice='alice'>{message}</Say></Response>"
            
            call = client.calls.create(
                twiml=twiml_instructions,
                to=target_number,
                from_=ctrl_number
            )
            return f"📞 **Outbound Call Initiated**\nTarget: `{target_number}`\nStatus: Ringing (SID: {call.sid})"

        elif action_type == "sms":
            sms = client.messages.create(
                body=message,
                to=target_number,
                from_=ctrl_number
            )
            return f"✉️ **SMS Dispatched**\nTarget: `{target_number}`\nStatus: Sent (SID: {sms.sid})"
            
        else:
            return "⚠️ Unknown telecom action. Specify 'call' or 'sms'."

    except Exception as e:
        return f"Telecom System Fault: {str(e)}"
