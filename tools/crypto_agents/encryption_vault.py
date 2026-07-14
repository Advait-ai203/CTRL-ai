# tools/crypto_agents/encryption_vault.py
import base64

def encrypt_payload(plaintext: str, secret_key: str = "ctrl_matrix_key") -> str:
    """
    Encrypts a string payload. 
    (Note: Uses base64 obfuscation for the blueprint. In production, upgrade to AES-256).
    """
    # Simple XOR + Base64 for structural demonstration
    xored = ''.join(chr(ord(c) ^ ord(secret_key[i % len(secret_key)])) for i, c in enumerate(plaintext))
    encrypted = base64.b64encode(xored.encode()).decode()
    
    return f"🛡️ **Vault Matrix Locked:**\nPayload Encrypted: `{encrypted}`"

def decrypt_payload(encrypted_text: str, secret_key: str = "ctrl_matrix_key") -> str:
    """Decrypts a previously locked payload."""
    try:
        decoded = base64.b64decode(encrypted_text.encode()).decode()
        xored = ''.join(chr(ord(c) ^ ord(secret_key[i % len(secret_key)])) for i, c in enumerate(decoded))
        return f"🔓 **Vault Matrix Unlocked:**\nPayload Decrypted: `{xored}`"
    except Exception:
        return "🛑 **SECURITY ALERT:** Decryption failed. Invalid payload or corrupted key."
