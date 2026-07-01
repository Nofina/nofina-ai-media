from pathlib import Path


NEWS_FILE = Path("packages/news-research/outputs/latest_news.txt")


def load_articles():

    if not NEWS_FILE.exists():
        return []

    content = NEWS_FILE.read_text(encoding="utf-8")

    articles = []

    current_source = ""

    current_title = ""

    for line in content.splitlines():

        line = line.strip()

        if not line:
            continue

        if line.startswith("Source:"):
            current_source = line.replace("Source:", "").strip()

        elif line.startswith("Link:"):

            link = line.replace("Link:", "").strip()

            articles.append(
                {
                    "title": current_title,
                    "source": current_source,
                    "link": link,
                }
            )

        elif line[0].isdigit():

            try:
                current_title = line.split(".", 1)[1].strip()
            except:
                pass

    return articles