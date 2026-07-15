# tools/seo_agents/page_speed_tester.py
import random

def simulate_lighthouse_audit(url: str) -> str:
    """Simulates a core web vitals performance test."""
    
    # Simulating standard matrix load times
    fcp = round(random.uniform(0.8, 1.5), 2)  # First Contentful Paint
    lcp = round(random.uniform(1.2, 2.5), 2)  # Largest Contentful Paint
    cls = round(random.uniform(0.0, 0.05), 3) # Cumulative Layout Shift
    
    score = 100 - int((lcp * 10) + (cls * 100))
    status = "🟢 FAST" if score >= 90 else "🟡 AVERAGE"
    
    return f"""
    ⚡ **Core Web Vitals Matrix: {url}**
    - Performance Score: {score}/100 ({status})
    - First Contentful Paint (FCP): {fcp}s
    - Largest Contentful Paint (LCP): {lcp}s
    - Cumulative Layout Shift (CLS): {cls}
    
    *Recommendation: Optimize image assets to reduce LCP.*
    """
