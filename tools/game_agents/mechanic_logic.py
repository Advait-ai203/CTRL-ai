# tools/game_agents/mechanic_logic.py

def compile_state_machine(mechanic_name: str, states: list, transitions: dict) -> str:
    """Compiles a finite state machine dictionary for core game mechanics."""
    
    logic_code = f"""class {mechanic_name.title()}StateMachine:
    def __init__(self):
        self.states = {states}
        self.current_state = '{states[0]}'
        self.transitions = {transitions}

    def trigger(self, action):
        valid_actions = self.transitions.get(self.current_state, {{}})
        if action in valid_actions:
            self.current_state = valid_actions[action]
            return f"State Transition: -> {{self.current_state}}"
        return "Invalid Action for current state."
"""
    return f"⚙️ **Mechanic Logic Compiled: {mechanic_name.title()}**\n```python\n{logic_code}\n```"
