# memory/chat_history.py
# Manages the active sliding window of the current conversation

class ActiveSessionMemory:
    def __init__(self):
        # Stores the last 20 interactions to keep context fast and cheap
        self.history = []
        self.max_memory_length = 20

    def add_interaction(self, user_prompt: str, ai_response: str):
        """Logs a single conversational turn."""
        self.history.append({"role": "user", "content": user_prompt})
        self.history.append({"role": "assistant", "content": ai_response})
        
        # Trim the oldest memories if we exceed the limit
        if len(self.history) > self.max_memory_length * 2:
            self.history = self.history[-self.max_memory_length * 2:]

    def get_context_string(self) -> str:
        """Formats the recent history for the Orchestrator to read."""
        if not self.history:
            return "No previous context."
            
        context = "Recent Conversation History:\n"
        for entry in self.history:
            context += f"[{entry['role'].upper()}]: {entry['content'][:100]}...\n"
        return context

    def wipe_memory(self):
        """Clears the session when the user logs out or switches tasks."""
        self.history = []

# Instantiate a global session tracker
session_memory = ActiveSessionMemory()
