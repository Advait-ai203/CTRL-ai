# tools/data_agents/web_scraper.py
import urllib.request
import re

def scrape_page_headlines(url: str) -> str:
    """Fetches text contents from standard web documents and extracts header matches."""
    try:
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ctrl-matrix/1.0'}
        )
        with urllib.request.urlopen(req, timeout=5) as response:
            html = response.read().decode('utf-8', errors='ignore')
            
        # Extract title and standard header elements via regex patterns
        title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
        title = title_match.group(1) if title_match else "Unknown Title"
        
        headings = re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>', html, re.IGNORECASE)
        cleaned_headings = [re.sub(r'<[^>]+>', '', h).strip() for h in headings][:10]
        
        output = f"🌐 **Scraper Node Payload: {title}**\n- Target URL: {url}\n\n**Extracted Headlines:**\n"
        for i, h in enumerate(cleaned_headings, 1):
            if h:
                output += f"{i}. {h}\n"
        return output
        
    except Exception as e:
        return f"❌ Scraping Network Exception: {str(e)}"
