import os
import time
import speech_recognition as sr
from dotenv import load_dotenv

# Initialize the secure vault before loading the brain
load_dotenv()

from core.orchestrator import run_orchestrator

def listen_for_wake_word():
    """Background daemon that constantly monitors for the 'Hey ctrl' activation phrase."""
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    print("🎙️ ctrl Audio Daemon Initialized. Listening for 'Hey ctrl'...")
    
    with microphone as source:
        # Calibrate for 1 second to ignore background room noise
        recognizer.adjust_for_ambient_noise(source, duration=1)
        
    while True:
        try:
            with microphone as source:
                # Listen in 5-second chunks
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            
            # Transcribe the audio using standard web speech protocols
            text = recognizer.recognize_google(audio).lower()
            print(f"[Acoustic Sensor]: Heard '{text}'")
            
            # Check for the brand wake word (accepting common phonetic spellings)
            if "hey control" in text or "hey ctrl" in text:
                # Strip the wake word out to isolate the actual command
                command = text.replace("hey control", "").replace("hey ctrl", "").strip()
                print(f"⚡ Wake word detected! Processing command: '{command}'")
                
                if not command:
                    print("ctrl: Awaiting your command...")
                    continue
                
                # Push the spoken command directly into the AI Router Brain
                target_dept = run_orchestrator(command)
                print(f"[Router]: Task assigned to -> {target_dept.upper()}")
                
                # If it's a local OS command, execute it immediately in the background
                if target_dept == "os_control":
                    # Dynamic import prevents the script from crashing if the tool isn't built yet
                    from tools.system_web_dept.os_control import execute_os_control
                    result = execute_os_control(command)
                    print(f"[Execution Output]:\n{result}")
                else:
                    print(f"[System]: '{command}' requires the visual UI. Please type this in the Chainlit dashboard.")
                    
        except sr.WaitTimeoutError:
            pass # No speech detected, loop silently
        except sr.UnknownValueError:
            pass # Speech was mumbled or unrecognizable, ignore safely
        except Exception as e:
            print(f"⚠️ [Audio Daemon Fault]: {str(e)}")
            time.sleep(1) # Prevent rapid error looping

if __name__ == "__main__":
    if not os.getenv("GOOGLE_API_KEY"):
        print("⚠️ Warning: GOOGLE_API_KEY not found. The Orchestrator will fail to classify intents.")
    listen_for_wake_word()
