# tools/education_tech_dept/interactive_quiz_bot.py

def evaluate_quiz_response(question: str, user_answer: str, correct_answer: str) -> str:
    """Evaluates a single active quiz node and provides real-time correction."""
    
    is_correct = user_answer.strip().lower() == correct_answer.strip().lower()
    
    if is_correct:
        return f"✅ **Correct.** Matrix logic verified."
    else:
        return f"❌ **Incorrect.**\n- Question: {question}\n- Your Answer: {user_answer}\n- Correct Matrix Answer: {correct_answer}"
