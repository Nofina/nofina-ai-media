from pathlib import Path
from sources.rss_source import fetch_rss_news


NEWS_SOURCES = [
    {
        "name": "BBC Technology",
        "url": "https://feeds.bbci.co.uk/news/technology/rss.xml",
    },
    {
        "name": "Google News Indonesia - Teknologi",
        "url": "https://news.google.com/rss/search?q=teknologi%20Indonesia&hl=id&gl=ID&ceid=ID:id",
    },
    {
        "name": "Google News Indonesia - Bisnis",
        "url": "https://news.google.com/rss/search?q=bisnis%20Indonesia&hl=id&gl=ID&ceid=ID:id",
    },
]


def show_banner():
    print("=" * 50)
    print("NOFINA AI MEDIA")
    print("News Research Agent v0.2")
    print("=" * 50)


def main():
    show_banner()

    output_path = Path("packages/news-research/outputs/latest_news.txt")

    with output_path.open("w", encoding="utf-8") as file:
        file.write("NOFINA AI MEDIA - Latest News\n")
        file.write("=" * 50 + "\n\n")

        for source in NEWS_SOURCES:
            print(f"\nSource: {source['name']}")
            print("-" * 50)

            file.write(f"Source: {source['name']}\n")
            file.write("-" * 50 + "\n")

            try:
                articles = fetch_rss_news(source["url"], limit=5)

                for index, article in enumerate(articles, start=1):
                    print(f"{index}. {article['title']}")
                    print(f"   Link: {article['link']}")
                    print()

                    file.write(f"{index}. {article['title']}\n")
                    file.write(f"Link: {article['link']}\n\n")

            except Exception as error:
                print(f"Failed to fetch {source['name']}: {error}")
                file.write(f"Failed to fetch {source['name']}: {error}\n\n")

    print("=" * 50)
    print(f"News saved to: {output_path}")


if __name__ == "__main__":
    main()