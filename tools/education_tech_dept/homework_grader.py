# tools/education_tech_dept/homework_grader.py

def grade_assignment(student_answers: list, master_key: list) -> str:
    """Compares submitted answers against an answer key to compute accuracy."""
    
    if len(student_answers) != len(master_key):
        return "⚠️ Grading Error: Number of answers does not match the master key."
        
    correct = 0
    feedback = []
    
    for i, (student, key) in enumerate(zip(student_answers, master_key)):
        if str(student).lower().strip() == str(key).lower().strip():
            correct += 1
            feedback.append(f"Q{i+1}: ✅ Correct")
        else:
            feedback.append(f"Q{i+1}: ❌ Incorrect (Expected: {key})")
            
    score_percentage = (correct / len(master_key)) * 100
    grade = "A" if score_percentage >= 90 else "B" if score_percentage >= 80 else "C" if score_percentage >= 70 else "F"
    
    feedback_str = "\n".join(feedback)
    
    return f"""
    📝 **Automated Grading Matrix:**
    - Final Score: {correct}/{len(master_key)} (**{score_percentage:.1f}%**)
    - Assessed Grade: **{grade}**
    
    **Detailed Feedback:**
    {feedback_str}
    """
