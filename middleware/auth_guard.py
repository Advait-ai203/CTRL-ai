# middleware/auth_guard.py
# Verifies admin privileges before executing sensitive OS or deployment tools

def verify_admin_clearance(user_id: str, action: str) -> bool:
    """
    Acts as a security checkpoint for high-risk executions.
    (e.g., deleting local files, deploying code to production)
    """
    # For a local startup build, you are the prime operator
    # If this goes to the web, you will wire this into a real database check
    prime_operators = ["ctrl_prime_operator", "advait_admin", "lokesh_admin"]
    
    if user_id in prime_operators:
        return True
        
    print(f"🛑 SECURITY BREACH: User {user_id} attempted restricted action: [{action}]")
    return False
