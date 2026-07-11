# tools/web_agents/seo_optimizer.py

def generate_meta_tags(page_title: str, description: str, keywords: list) -> str:
    """Generates Google and Social Media (OpenGraph) compliant HTML meta tags."""

    keyword_str = ", ".join(keywords)

    html_tags = f"""
<title>{page_title}</title>
<meta name="description" content="{description}">
<meta name="keywords" content="{keyword_str}">

<meta property="og:title" content="{page_title}">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
"""
    return f"📈 **SEO Tags Generated:** Inject these into your `<head>` block.\n```html\n{html_tags}\n```"
