# middleware/rate_limiter.py
# Prevents API spam and protects billing thresholds

import time
from config.settings import settings

# In-memory dictionary to track user timestamps
# Format: {"user_id": [timestamp1, timestamp2, ...]}
_user_requests = {}

def is_rate_limited(user_id: str = "ctrl_prime_operator") -> bool:
    """
    Checks if a user has exceeded the maximum allowed requests per minute.
    Returns True if blocked, False if permitted to proceed.
    """
    current_time = time.time()
    
    # Initialize user array if they don't exist
    if user_id not in _user_requests:
        _user_requests[user_id] = []
        
    # Filter out requests that are older than 60 seconds
    valid_requests = [t for t in _user_requests[user_id] if current_time - t < 60]
    
    # Update the tracking list
    _user_requests[user_id] = valid_requests
    
    # Check against the threshold set in config/settings.py
    if len(valid_requests) >= settings.MAX_REQUESTS_PER_MINUTE:
        return True # Block the request
        
    # Log this new request and allow
    _user_requests[user_id].append(current_time)
    return False
