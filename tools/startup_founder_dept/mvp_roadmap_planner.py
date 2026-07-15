# tools/startup_founder_dept/mvp_roadmap_planner.py

def stage_mvp_sprint(product_name: str, duration_weeks: int = 4) -> str:
    """Breaks down a rapid deployment cycle for the 3-person team."""
    
    return f"""
    🚀 **MVP Deployment Matrix: {product_name.upper()}**
    *Timeline: {duration_weeks} Weeks*
    
    **Phase 1: Architecture (Week 1)**
    - Advait: Finalize core logic and database schema.
    - Lokesh & Teammate 3: Map out UI wireframes and hardware specs.
    
    **Phase 2: Build & Iterate (Weeks 2-3)**
    - Execute core features only. Cut anything that isn't essential to the value prop.
    - Daily syncs to unblock deployment pipelines.
    
    **Phase 3: Launch & Audit (Week 4)**
    - QA testing, bug crushing, and final accessibility audits.
    - Push to production. Begin collecting user feedback.
    """
