# config/settings.py
# Master Configuration Loader for the ctrl matrix

import os
from dotenv import load_dotenv

# Force load the hidden .env file
load_dotenv()

class Settings:
    """Centralized configuration state for the entire platform."""
    
    # AI Brain Keys
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Core Application Settings
    APP_NAME: str = "ctrl-agent"
    APP_VERSION: str = "1.0.0"
    DEBUG_MODE: bool = True
    
    # Security Thresholds
    MAX_REQUESTS_PER_MINUTE: int = 15
    MAX_TOKENS_PER_RESPONSE: int = 4096
    
    # Output Delivery Paths
    OUTPUT_BASE_DIR: str = "generated_assets"
    
    def __init__(self):
        if not self.GOOGLE_API_KEY:
            print("⚠️ WARNING: GOOGLE_API_KEY is missing from the .env vault.")

# Instantiate a global settings object to be imported across the app
settings = Settings()
