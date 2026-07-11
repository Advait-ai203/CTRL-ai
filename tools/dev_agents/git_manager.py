# tools/dev_agents/git_manager.py
import subprocess

def execute_git_commit(commit_message: str) -> str:
    """Stages all changes and commits them to the local Git repository."""
    try:
        # Stage all files
        subprocess.run(["git", "add", "."], check=True, capture_output=True)
        
        # Commit with the provided message
        result = subprocess.run(["git", "commit", "-m", commit_message], check=True, capture_output=True, text=True)
        
        return f"🌿 **Git Matrix Updated:**\n```text\n{result.stdout.strip()}\n```"
    except subprocess.CalledProcessError as e:
        if "nothing to commit" in e.stdout:
            return "⚠️ Git Status: Working tree is clean. Nothing to commit."
        return f"⚠️ Git Execution Fault: {e.stderr.strip()}"
