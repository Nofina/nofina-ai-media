import streamlit as st
from pathlib import Path
from datetime import datetime

st.set_page_config(page_title="Nofina Brain", page_icon="🧠", layout="wide")

st.title("🧠 Nofina Brain")
st.caption("Opportunity Intelligence Engine + Content Package Generator")

news_file = Path("packages/news-research/outputs/latest_news.txt")
package_dir = Path("packages/news-research/outputs/content_packages")
package_dir.mkdir(parents=True, exist_ok=True)


def calculate_score(title):
    score = 50
    keywords = {
        "ai": 15, "openai": 20, "chatgpt": 20, "google": 10,
        "microsoft": 10, "nvidia": 15, "tesla": 12,
        "business": 10, "bisnis": 10, "money": 12, "startup": 12,
        "indonesia": 8, "viral": 15, "robot": 12, "technology": 10,
        "launch": 10, "future": 8, "price": 8
    }

    lower = title.lower()
    for word, value in keywords.items():
        if word in lower:
            score += value

    return min(score, 100)


def detect_category(title):
    lower = title.lower()
    if any(x in lower for x in ["ai", "openai", "chatgpt", "robot"]):
        return "🤖 AI & Technology"
    if any(x in lower for x in ["business", "bisnis", "startup", "money"]):
        return "💰 Business Opportunity"
    if any(x in lower for x in ["indonesia", "jakarta", "rupiah"]):
        return "🇮🇩 Indonesia Trend"
    if any(x in lower for x in ["tesla", "apple", "google", "microsoft", "nvidia"]):
        return "📈 Big Tech"
    return "📰 General Trend"


def recommended_platforms(score):
    if score >= 85:
        return "YouTube Shorts, TikTok, Instagram Reels, Facebook Reels"
    if score >= 70:
        return "YouTube Shorts, Facebook Reels, Instagram Reels"
    return "Facebook Post, Threads, Short Commentary"


def generate_package(article):
    title = article["title"]
    source = article["source"]
    category = article["category"]
    platforms = article["platforms"]

    return f"""
NOFINA CONTENT PACKAGE
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}
Source: {source}
Category: {category}
Opportunity Score: {article["score"]}
Recommended Platforms: {platforms}

ORIGINAL NEWS:
{title}

SHORTS SCRIPT:

HOOK:
Kamu harus tahu berita ini, karena bisa jadi peluang besar.

BODY:
Hari ini ada kabar penting: {title}

Topik ini menarik karena berhubungan dengan tren yang sedang naik.
Kalau dikemas dengan cepat, ini bisa menjadi konten pendek yang kuat untuk YouTube Shorts, TikTok, Instagram Reels, dan Facebook Reels.

ANGLE:
Jangan cuma lihat ini sebagai berita.
Lihat ini sebagai peluang konten, peluang bisnis, dan peluang traffic.

CTA:
Follow Nofina AI Media untuk update peluang teknologi, bisnis, dan tren terbaru.

YOUTUBE TITLE OPTIONS:
1. Berita Ini Bisa Jadi Peluang Besar!
2. Tren Baru yang Harus Kamu Tahu
3. Jangan Abaikan Kabar Ini

CAPTION YOUTUBE:
Berita terbaru ini bisa menjadi peluang besar untuk konten dan bisnis digital. Simak sampai akhir.

CAPTION INSTAGRAM:
Tren ini menarik banget buat diperhatikan. Bisa jadi peluang konten berikutnya.

CAPTION TIKTOK:
Berita ini kelihatannya biasa, tapi potensinya besar.

CAPTION FACEBOOK:
Topik ini sedang menarik perhatian dan bisa menjadi peluang bagus untuk dipantau.

HASHTAGS:
#NofinaAIMedia #AI #Business #Technology #TrendingNews #PeluangBisnis #KontenAI
"""


def parse_articles(content):
    articles = []
    title = ""
    source = ""
    link = ""

    for line in content.splitlines():
        if line.startswith("Source:"):
            source = line.replace("Source:", "").strip()

        elif line.startswith("Link:"):
            link = line.replace("Link:", "").strip()
            score = calculate_score(title)
            category = detect_category(title)

            articles.append({
                "title": title,
                "source": source,
                "link": link,
                "score": score,
                "category": category,
                "platforms": recommended_platforms(score)
            })

        elif line and line[0].isdigit():
            title = line.split(".", 1)[1].strip()

    return sorted(articles, key=lambda x: x["score"], reverse=True)


if not news_file.exists():
    st.warning("Belum ada berita. Jalankan news_agent.py dulu.")
    st.stop()

content = news_file.read_text(encoding="utf-8")
articles = parse_articles(content)

col1, col2, col3 = st.columns(3)
col1.metric("Total Opportunities", len(articles))
col2.metric("Top Score", articles[0]["score"] if articles else 0)
col3.metric("Engine Status", "Running")

st.subheader("🔥 Top Opportunities Today")

for index, article in enumerate(articles):
    with st.container(border=True):
        st.markdown(f"### {article['title']}")
        st.caption(f"{article['source']} | {article['category']}")

        c1, c2, c3 = st.columns(3)
        c1.metric("Opportunity Score", article["score"])
        c2.write("Recommended Platforms")
        c2.success(article["platforms"])
        c3.link_button("📖 Read Article", article["link"])

        if st.button("🚀 Generate Full Content Package", key=f"pkg_{index}"):
            package = generate_package(article)

            safe_name = "".join(
                char for char in article["title"][:50]
                if char.isalnum() or char in (" ", "-", "_")
            ).strip().replace(" ", "_")

            output_file = package_dir / f"{safe_name}.txt"
            output_file.write_text(package, encoding="utf-8")

            st.success(f"Content package saved: {output_file}")
            st.text_area("Generated Content Package", package, height=520)