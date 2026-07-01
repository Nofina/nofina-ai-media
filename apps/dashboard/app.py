import sys
from pathlib import Path
import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
NEWS_RESEARCH = ROOT / "packages" / "news-research"
sys.path.append(str(NEWS_RESEARCH))

from brain import NofinaBrain
from content_generator import generate_content

st.set_page_config(page_title="Nofina Brain V2", page_icon="🧠", layout="wide")

st.title("🧠 Nofina AI Media")
st.caption("Opportunity Intelligence Dashboard v0.3")

news_file = ROOT / "packages" / "news-research" / "outputs" / "latest_news.txt"

brain = NofinaBrain()


def parse_articles(content):
    articles = []
    title = ""
    source = ""

    for line in content.splitlines():
        if line.startswith("Source:"):
            source = line.replace("Source:", "").strip()

        elif line.startswith("Link:"):
            link = line.replace("Link:", "").strip()
            article = {
                "title": title,
                "source": source,
                "link": link,
            }
            analysis = brain.analyze(article)
            article["analysis"] = analysis
            articles.append(article)

        elif line and line[0].isdigit():
            title = line.split(".", 1)[1].strip()

    return sorted(
        articles,
        key=lambda x: x["analysis"]["viral_score"],
        reverse=True,
    )


if not news_file.exists():
    st.warning("Belum ada berita. Jalankan news_agent.py dulu.")
    st.stop()

content = news_file.read_text(encoding="utf-8")
articles = parse_articles(content)

top_score = articles[0]["analysis"]["viral_score"] if articles else 0
high_count = sum(1 for a in articles if a["analysis"]["viral_score"] >= 80)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Opportunities", len(articles))
col2.metric("Top Score", top_score)
col3.metric("High Opportunities", high_count)
col4.metric("Engine Status", "Running")

st.divider()
st.subheader("🔥 Today's Top Opportunities")

for index, article in enumerate(articles):
    analysis = article["analysis"]

    with st.container(border=True):
        left, right = st.columns([3, 1])

        with left:
            st.markdown(f"### {article['title']}")
            st.caption(f"{article['source']}")

            st.write(f"🎯 **Audience:** {analysis['audience']}")
            st.write(f"📌 **Angle:** {analysis['angle']}")
            st.write(f"🚀 **Best Platform:** {analysis['platform']}")
            st.write(f"💰 **Monetization:** {analysis['monetization']}")

        with right:
            st.metric("Viral Score", analysis["viral_score"])
            st.write(f"💵 Revenue: **{analysis['revenue']}**")
            st.write(f"⚔️ Competition: **{analysis['competition']}**")
            st.write(f"♻️ Evergreen: **{analysis['evergreen']}**")

        col_a, col_b = st.columns(2)

        with col_a:
            st.link_button("📖 Read Article", article["link"])

        with col_b:
            if st.button("🚀 Generate Content", key=f"gen_{index}"):
                package = generate_content(article)

                st.success("Content generated")

                st.markdown("#### 🎬 YouTube Title")
                st.write(package["youtube_title"])

                st.markdown("#### 🪝 Hook")
                st.write(package["hook"])

                st.markdown("#### 📝 Script")
                st.text_area("Script", package["script"], height=260)

                st.markdown("#### 🖼 Thumbnail Prompt")
                st.text_area("Thumbnail Prompt", package["thumbnail_prompt"], height=180)

                st.markdown("#### # Hashtags")
                st.write(package["hashtags"])