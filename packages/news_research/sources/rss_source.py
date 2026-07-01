import urllib.request
import xml.etree.ElementTree as ET


def fetch_rss_news(feed_url, limit=5):
    with urllib.request.urlopen(feed_url, timeout=10) as response:
        data = response.read()

    root = ET.fromstring(data)
    articles = []

    for item in root.findall(".//item")[:limit]:
        articles.append({
            "title": item.findtext("title", default="No title").strip(),
            "link": item.findtext("link", default="No link").strip(),
            "description": item.findtext("description", default="No description").strip(),
        })

    return articles