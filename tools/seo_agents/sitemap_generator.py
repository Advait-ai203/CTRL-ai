# tools/seo_agents/sitemap_generator.py
import os
import datetime

def generate_xml_sitemap(domain: str, routes: list) -> str:
    """Compiles a standard sitemap.xml file for search engine crawlers."""
    target_dir = "./generated_assets/web_builds"
    os.makedirs(target_dir, exist_ok=True)

    date_today = datetime.date.today().strftime("%Y-%m-%d")

    xml_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'

    for route in routes:
        clean_route = route.lstrip("/")
        priority = "1.0" if clean_route == "" else "0.8"

        xml_content += f"""  <url>
    <loc>https://{domain}/{clean_route}</loc>
    <lastmod>{date_today}</lastmod>
    <priority>{priority}</priority>
  </url>\n"""

    xml_content += '</urlset>'

    file_path = os.path.join(target_dir, "sitemap.xml")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(xml_content)

    return f"🗺️ **XML Sitemap Compiled:** Indexed {len(routes)} routes at `{file_path}`"
