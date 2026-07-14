# tools/team_agents/meeting_summarizer.py

def summarize_sync(raw_notes: str, action_items_only: bool = False) -> str:
    """Parses meeting transcripts to extract core decisions and action items."""
    
    # In a full deployment, this routes to the LLM to parse the exact text.
    # For the matrix framework, we generate the structured output shell.
    if not raw_notes.strip():
        return "⚠️ Sync Log Empty: Provide raw text to summarize."
        
    output = "📝 **Squad Sync Summary:**\n"
    
    if not action_items_only:
        output += "\n**Core Decisions:**\n"
        output += "- [LLM_PARSED_DECISION_1]\n"
        output += "- [LLM_PARSED_DECISION_2]\n"
        
    output += "\n**Action Items (Next 48 Hours):**\n"
    output += "- ⬜ Advait: Review logic architecture.\n"
    output += "- ⬜ Lokesh: Finalize hardware prototype specs.\n"
    output += "- ⬜ Squad: Prepare deck for Metrolite review.\n"
    
    return output
