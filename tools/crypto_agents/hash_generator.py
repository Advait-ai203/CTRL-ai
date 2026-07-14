# tools/crypto_agents/hash_generator.py
import hashlib

def generate_sha256_hash(data_string: str) -> str:
    """Generates a secure SHA-256 hash for data integrity and password storage."""
    
    encoded_data = data_string.encode('utf-8')
    secure_hash = hashlib.sha256(encoded_data).hexdigest()
    
    return f"""
    🔐 **Cryptographic Hash Generated:**
    - Input Length: {len(data_string)} characters
    - Algorithm: SHA-256
    
    **Resulting Hash:**
    `{secure_hash}`
    """
