# tools/education_tech_dept/syllabus_planner.py

def generate_weekly_syllabus(subject: str, topics: list, weeks: int = 4) -> str:
    """Divides a list of topics into a structured weekly learning matrix."""
    if not topics:
        return "⚠️ Syllabus Error: No topics provided."
        
    topics_per_week = max(1, len(topics) // weeks)
    
    output = f"📚 **Syllabus Matrix: {subject.upper()} ({weeks} Weeks)**\n"
    output += "--------------------------------------------------\n"
    
    for i in range(weeks):
        start_idx = i * topics_per_week
        # Give the remainder to the last week
        end_idx = start_idx + topics_per_week if i < weeks - 1 else len(topics)
        
        week_topics = topics[start_idx:end_idx]
        formatted_topics = ", ".join(week_topics) if week_topics else "Review & Assessment"
        
        output += f"**Week {i+1}:** {formatted_topics}\n"
        
    return output
